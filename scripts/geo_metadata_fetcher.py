"""
GEO Metadata Fetcher
====================
Pulls all GEO Series (GSE) metadata published in the last year
using NCBI's Entrez E-Utilities API.

Usage:
    python geo_metadata_fetcher.py [--email your@email.com] [--output results.json]

NCBI requires an email for API usage. Provide one via --email or set
the NCBI_EMAIL environment variable.
"""

import argparse
import json
import os
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# NCBI asks for <=3 requests/sec without an API key, <=10/sec with one
REQUEST_DELAY = 0.35  # seconds between requests


def eutils_get(endpoint: str, params: dict) -> ET.Element:
    """Make a GET request to an E-Utils endpoint and return parsed XML."""
    safe_chars = '+[]"'
    url = f"{BASE_URL}/{endpoint}?{urlencode(params, safe=safe_chars)}"
    for attempt in range(3):
        try:
            req = Request(url, headers={"User-Agent": "GEO-Metadata-Fetcher/1.0"})
            with urlopen(req, timeout=60) as resp:
                return ET.parse(resp).getroot()
        except (HTTPError, URLError, ET.ParseError) as e:
            if attempt < 2:
                wait = 2 ** (attempt + 1)
                print(f"  ⚠ Request failed ({e}), retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
    # unreachable, but keeps type checkers happy
    raise RuntimeError("Request failed after 3 attempts")


def search_geo(email: str, api_key: str | None, months: int = 12,
               start_date: str | None = None, end_date: str | None = None) -> tuple[str, str, int]:
    """
    Run eSearch for all GSE records published in a date range.
    If start_date/end_date are provided (YYYY/MM/DD), use those directly.
    Otherwise, search the last `months` months from today.
    Returns (query_key, webenv, total_count) using the History server.
    """
    if start_date and end_date:
        mindate = start_date
        maxdate = end_date
    else:
        today = datetime.now()
        start = today - timedelta(days=months * 30)
        mindate = start.strftime("%Y/%m/%d")
        maxdate = today.strftime("%Y/%m/%d")

    params = {
        "db": "gds",
        "term": "GSE[ETYP]",
        "datetype": "pdat",
        "mindate": mindate,
        "maxdate": maxdate,
        "retmax": 0,          # we only need history params, not IDs
        "usehistory": "y",
        "email": email,
    }
    if api_key:
        params["api_key"] = api_key

    date_range = f"{mindate}:{maxdate}"
    print(f"Searching GEO for Series published {date_range} ...")
    root = eutils_get("esearch.fcgi", params)

    count = int(root.findtext("Count", "0"))
    query_key = root.findtext("QueryKey", "")
    webenv = root.findtext("WebEnv", "")

    if not query_key or not webenv:
        print("Error: eSearch did not return history parameters.")
        sys.exit(1)

    print(f"Found {count:,} Series records.\n")
    return query_key, webenv, count


def fetch_summaries(
    email: str,
    api_key: str | None,
    query_key: str,
    webenv: str,
    total: int,
    batch_size: int = 200,
) -> list[dict]:
    """
    Fetch document summaries in batches using eSummary (version 2.0 JSON).
    Returns a list of parsed record dicts.
    """
    records = []
    fetched = 0

    while fetched < total:
        params = {
            "db": "gds",
            "query_key": query_key,
            "WebEnv": webenv,
            "retstart": fetched,
            "retmax": batch_size,
            "email": email,
            "version": "2.0",
        }
        if api_key:
            params["api_key"] = api_key

        print(f"  Fetching records {fetched + 1}–{min(fetched + batch_size, total)} of {total} ...")

        # eSummary v2.0 returns XML with <DocumentSummary> elements
        root = eutils_get("esummary.fcgi", params)

        for doc in root.iter("DocumentSummary"):
            record = parse_doc_summary(doc)
            if record:
                records.append(record)

        fetched += batch_size
        time.sleep(REQUEST_DELAY)

    return records


def parse_doc_summary(doc: ET.Element) -> dict | None:
    """Extract useful fields from an eSummary DocumentSummary element."""
    uid = doc.get("uid", "")

    def txt(tag: str) -> str:
        el = doc.find(tag)
        return (el.text or "").strip() if el is not None else ""

    accession = txt("Accession")

    # Only keep GSE (Series) records, skip GDS/GPL/GSM if they sneak in
    if accession and not accession.startswith("GSE"):
        return None

    # Parse sample accessions list
    samples = []
    samples_el = doc.find("Samples")
    if samples_el is not None:
        for s in samples_el.findall("Sample"):
            acc = s.get("Accession", "")
            title = s.findtext("Title", "")  if s.find("Title") is not None else ""
            if acc:
                samples.append({"accession": acc, "title": title})

    return {
        "uid": uid,
        "accession": accession,
        "title": txt("title"),
        "summary": txt("summary"),
        "organism": txt("taxon"),
        "entry_type": txt("entryType"),
        "gds_type": txt("gdsType"),
        "platform_id": txt("GPL"),
        "platform_title": txt("PlatformTitle"),
        "platform_technology": txt("PlatformTechType"),
        "n_samples": txt("n_samples"),
        "pubmed_ids": txt("PubMedIds"),
        "ftp_link": txt("FTPLink"),
        "pub_date": txt("PDAT"),
        "suppfile": txt("suppFile"),
        "samples": samples,
    }


def build_ftp_url(accession: str, fmt: str = "soft") -> str:
    """Construct the FTP download URL for a given GSE accession and format."""
    prefix = accession[:-3] + "nnn" if len(accession) > 6 else "GSEnnn"
    base = f"ftp://ftp.ncbi.nlm.nih.gov/geo/series/{prefix}/{accession}"
    if fmt == "soft":
        return f"{base}/soft/{accession}_family.soft.gz"
    elif fmt == "miniml":
        return f"{base}/miniml/{accession}_family.xml.tgz"
    elif fmt == "matrix":
        return f"{base}/matrix/"
    elif fmt == "suppl":
        return f"{base}/suppl/"
    return base


def print_summary_stats(records: list[dict]):
    """Print some quick stats about the fetched records."""
    organisms = {}
    platforms = {}
    types = {}
    total_samples = 0

    for r in records:
        org = r["organism"] or "Unknown"
        organisms[org] = organisms.get(org, 0) + 1

        plat = r["platform_title"] or r["platform_id"] or "Unknown"
        platforms[plat] = platforms.get(plat, 0) + 1

        gtype = r["gds_type"] or "Unknown"
        types[gtype] = types.get(gtype, 0) + 1

        try:
            total_samples += int(r["n_samples"])
        except (ValueError, TypeError):
            pass

    print("\n" + "=" * 60)
    print(f"  SUMMARY — {len(records):,} GSE records fetched")
    print("=" * 60)

    print(f"\n  Total samples across all series: {total_samples:,}")

    print(f"\n  Top 10 organisms:")
    for org, cnt in sorted(organisms.items(), key=lambda x: -x[1])[:10]:
        print(f"    {cnt:>5,}  {org}")

    print(f"\n  Top 10 data types:")
    for t, cnt in sorted(types.items(), key=lambda x: -x[1])[:10]:
        print(f"    {cnt:>5,}  {t}")

    print(f"\n  Top 10 platforms:")
    for p, cnt in sorted(platforms.items(), key=lambda x: -x[1])[:10]:
        print(f"    {cnt:>5,}  {p}")

    print()


def main():
    parser = argparse.ArgumentParser(description="Fetch GEO Series metadata from the last year.")
    parser.add_argument("--email", default=os.environ.get("NCBI_EMAIL", ""),
                        help="Email for NCBI API (required by NCBI policy)")
    parser.add_argument("--api-key", default=os.environ.get("NCBI_API_KEY"),
                        help="NCBI API key (optional, raises rate limit to 10 req/s)")
    parser.add_argument("--months", type=int, default=12,
                        help="How many months back to search (default: 12)")
    parser.add_argument("--batch-size", type=int, default=200,
                        help="Records per eSummary request (default: 200, max 500)")
    parser.add_argument("--output", "-o", default="geo_metadata.json",
                        help="Output JSON file (default: geo_metadata.json)")
    parser.add_argument("--start-date", default=None,
                        help="Start date YYYY/MM/DD (overrides --months)")
    parser.add_argument("--end-date", default=None,
                        help="End date YYYY/MM/DD (overrides --months)")
    parser.add_argument("--add-ftp-urls", action="store_true",
                        help="Add constructed FTP download URLs to each record")
    args = parser.parse_args()

    if not args.email:
        print("Error: NCBI requires an email address.")
        print("  Use --email you@example.com or set NCBI_EMAIL env var.")
        sys.exit(1)

    # Step 1: Search
    query_key, webenv, total = search_geo(
        args.email, args.api_key, args.months,
        start_date=args.start_date, end_date=args.end_date,
    )

    if total == 0:
        print("No records found. Exiting.")
        sys.exit(0)

    # Step 2: Fetch summaries
    records = fetch_summaries(
        args.email, args.api_key, query_key, webenv, total, args.batch_size
    )

    # Step 3: Optionally add FTP URLs
    if args.add_ftp_urls:
        for r in records:
            acc = r["accession"]
            if acc:
                r["ftp_urls"] = {
                    "soft": build_ftp_url(acc, "soft"),
                    "miniml": build_ftp_url(acc, "miniml"),
                    "matrix": build_ftp_url(acc, "matrix"),
                    "suppl": build_ftp_url(acc, "suppl"),
                }

    # Step 4: Stats
    print_summary_stats(records)

    # Step 5: Save
    output_path = args.output
    with open(output_path, "w") as f:
        json.dump(records, f, indent=2)

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Saved {len(records):,} records to {output_path} ({size_mb:.1f} MB)")
    print(f"\nExample record:")
    if records:
        example = {k: v for k, v in records[0].items() if k != "samples"}
        example["samples"] = f"[{len(records[0].get('samples', []))} samples]"
        print(json.dumps(example, indent=2))


if __name__ == "__main__":
    main()
