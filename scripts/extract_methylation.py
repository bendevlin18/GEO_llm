"""
Extract methylation profiling datasets from GEO metadata.
Classifies by protocol modality.

Modalities:
  wgbs              — Whole Genome Bisulfite Sequencing (WGBS)
  rrbs              — Reduced Representation Bisulfite Sequencing (RRBS)
  em_seq            — Enzymatic Methyl-seq (EM-seq)
  oxbs_seq          — Oxidative Bisulfite Sequencing (oxBS-seq)
  hmc_seq           — 5-Hydroxymethylcytosine sequencing (5hmC-seq, hMeDIP, TAB-seq, etc.)
  medip_seq         — Methylated DNA Immunoprecipitation sequencing (MeDIP-seq)
  methylation_array — Illumina Infinium arrays (450K, EPIC/850K, 27K)
  other_methylation — Other / unclassified methylation profiling

GEO type filters used:
  "Methylation profiling by high throughput sequencing"
  "Methylation profiling by array"

Can be run standalone or imported (methylation_filter, classify_methylation).
"""
import json
import re
import glob
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
from tag_topics import tag_topics

# ── Protocol modality keywords ────────────────────────────────────────────────

RRBS_KEYWORDS = [
    "rrbs", "reduced representation bisulfite",
    "reduced-representation bisulfite",
]

EM_SEQ_KEYWORDS = [
    "em-seq", "emseq", "em seq",
    "enzymatic methyl", "enzymatic-methyl",
]

OXBS_KEYWORDS = [
    "oxbs", "ox-bs", "oxidative bisulfite",
    "tab-seq", "tab seq",           # TET-Assisted Bisulfite
    "ace-seq", "ace seq",           # APOBEC-Coupled Epigenetic Sequencing
]

MEDIP_KEYWORDS = [
    "medip", "me-dip",
    "methylated dna immunoprecipitation",
    "methylated dna ip",
]

WGBS_KEYWORDS = [
    "wgbs", "whole genome bisulfite", "whole-genome bisulfite",
    "bs-seq", "bsseq", "bisulfite sequencing",
    "bisulfite-seq", "whole-genome methylation sequencing",
]

HMC_SEQ_KEYWORDS = [
    "5hmc-seq", "5hmc seq", "hmc-seq", "hmcseq",
    "5-hydroxymethylcytosine sequencing", "5hmC profiling",
    "hydroxymethylcytosine sequencing", "hydroxymethylome",
    "hmedip", "hydroxymethylated dna immunoprecipitation",
    "tet-assisted bisulfite", "tab-seq", "tab seq",
    "5hmC-seal", "seal-seq",
    "5fc", "5cam", "5-formylcytosine", "5-carboxylcytosine",
]

ARRAY_KEYWORDS = [
    "450k", "450 k", "infinium 450",
    "epic array", "epic chip", "850k", "850 k", "infinium epic",
    "27k", "27 k", "infinium 27",
    "methylation array", "methylation chip",
    "illumina methylation", "infinium methylation",
    "beadchip", "bead chip",
]


def methylation_filter(record: dict) -> bool:
    """Return True if the record is a methylation profiling dataset."""
    gds_type = record.get("gds_type", "")
    return (
        "Methylation profiling by high throughput sequencing" in gds_type
        or "Methylation profiling by array" in gds_type
    )


def classify_methylation(record: dict) -> str:
    """
    Return the methylation modality string.

    wgbs | rrbs | em_seq | oxbs_seq | medip_seq | methylation_array | other_methylation
    """
    text = f"{record['title']} {record['summary']}".lower()
    gds_type = record.get("gds_type", "")

    # Array: gds_type is the strongest signal
    if "Methylation profiling by array" in gds_type:
        return "methylation_array"

    # Check most-specific protocols first
    if any(kw in text for kw in EM_SEQ_KEYWORDS):
        return "em_seq"

    if any(kw in text for kw in OXBS_KEYWORDS):
        return "oxbs_seq"

    if any(kw in text for kw in HMC_SEQ_KEYWORDS):
        return "hmc_seq"

    if any(kw in text for kw in MEDIP_KEYWORDS):
        return "medip_seq"

    if any(kw in text for kw in RRBS_KEYWORDS):
        return "rrbs"

    if any(kw in text for kw in WGBS_KEYWORDS):
        return "wgbs"

    # Array keywords in title/summary even if gds_type says "sequencing"
    if any(kw in text for kw in ARRAY_KEYWORDS):
        return "methylation_array"

    return "other_methylation"


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*",
                        help="Data JSON files (default: all data/geo_metadata_*.json)")
    parser.add_argument("-o", "--output", default="methylation_classified.json",
                        help="Output file (default: methylation_classified.json)")
    args = parser.parse_args()

    paths = args.files or sorted(glob.glob("data/geo_metadata_*.json"))
    if not paths:
        sys.exit("No data files found.")

    # Load and deduplicate (latest snapshot wins)
    seen: dict[str, dict] = {}
    for path in paths:
        with open(path) as f:
            records = json.load(f)
        for r in records:
            acc = r.get("accession", "")
            if acc:
                seen[acc] = r
        print(f"  Loaded {len(records):,} from {path}")

    all_records = list(seen.values())
    print(f"\nTotal unique records: {len(all_records):,}")

    # Filter and classify
    meth_records = [r for r in all_records if methylation_filter(r)]
    print(f"Methylation profiling records: {len(meth_records):,}")

    classified = []
    for r in meth_records:
        modality = classify_methylation(r)
        classified.append({
            "accession": r["accession"],
            "title": r["title"],
            "summary": r["summary"][:500],
            "organism": r["organism"],
            "n_samples": r["n_samples"],
            "platform_id": r["platform_id"],
            "suppfile": r.get("suppfile", ""),
            "pub_date": r["pub_date"],
            "modality": modality,
        })

    # Tag topics (assay-agnostic tagger)
    print("Tagging topics...")
    for r in classified:
        r["topics"] = tag_topics(r)

    tagged = sum(1 for r in classified if r["topics"])
    print(f"Tagged: {tagged:,} / {len(classified):,}")

    # Stats
    print("\nModality breakdown:")
    modalities = Counter(r["modality"] for r in classified)
    for m, c in modalities.most_common():
        print(f"  {c:>6}  {m}")

    print("\nTop organisms:")
    orgs = Counter(r["organism"] for r in classified)
    for org, c in orgs.most_common(10):
        print(f"  {c:>6}  {org}")

    with open(args.output, "w") as f:
        json.dump(classified, f, indent=2)
    print(f"\nSaved {len(classified):,} records to {args.output}")


if __name__ == "__main__":
    main()
