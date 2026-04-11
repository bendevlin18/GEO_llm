"""
Merge multiple GEO metadata snapshots, deduplicate, classify, tag, and rebuild
the search index and wiki pages.

Usage:
    python merge_and_rebuild.py data/geo_metadata_2025-Q4.json data/geo_metadata_2026-04-09.json
"""
import json
import glob
import os
import sys
from datetime import datetime

# Import classification and tagging logic (add scripts/ to path for imports)
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from extract_rnaseq import classify, rna_filter
from tag_topics import tag_topics


def load_and_merge(paths):
    """Load multiple JSON files, deduplicate by accession (latest file wins)."""
    seen = {}
    for path in paths:
        with open(path) as f:
            records = json.load(f)
        for r in records:
            acc = r.get("accession", "")
            if acc:
                seen[acc] = r
        print(f"  Loaded {len(records):,} records from {path}")

    merged = list(seen.values())
    print(f"  Total unique records after dedup: {len(merged):,}")
    return merged


def main():
    if len(sys.argv) < 2:
        # Default: load all JSON files in data/
        paths = sorted(glob.glob("data/geo_metadata_*.json"))
    else:
        paths = sys.argv[1:]

    if not paths:
        print("No data files found.")
        sys.exit(1)

    print("Step 1: Merging data snapshots...")
    all_records = load_and_merge(paths)

    print("\nStep 2: Filtering to RNA-seq and classifying modality...")
    rna_records = [r for r in all_records if rna_filter(r)]
    classified = []
    for r in rna_records:
        modality = classify(r)
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

    from collections import Counter
    modalities = Counter(r["modality"] for r in classified)
    print(f"  RNA-seq records: {len(classified):,}")
    for m, c in modalities.most_common():
        print(f"    {c:>5}  {m}")

    print("\nStep 3: Tagging topics...")
    for r in classified:
        r["topics"] = tag_topics(r)

    tagged = sum(1 for r in classified if r["topics"])
    print(f"  Tagged: {tagged:,} / {len(classified):,}")

    # Save classified data
    with open("rnaseq_classified.json", "w") as f:
        json.dump(classified, f, indent=2)
    print(f"  Saved rnaseq_classified.json")

    print("\nStep 4: Rebuilding search index...")
    os.system("conda run -n GEO_llm python scripts/build_search_index.py")

    print("\nStep 5: Regenerating wiki pages...")
    os.system("conda run -n GEO_llm python scripts/generate_wiki.py")

    # Update log
    today = datetime.now().strftime("%Y-%m-%d")
    dates = sorted(set(r["pub_date"] for r in classified if r["pub_date"]))
    date_range = f"{dates[0]} – {dates[-1]}" if dates else "unknown"
    log_entry = (
        f"- **{today}**: Merged {len(paths)} snapshots. "
        f"{len(all_records):,} total GEO records, "
        f"{len(classified):,} RNA-seq datasets "
        f"(covering {date_range}). "
        f"Modalities: {dict(modalities.most_common())}."
    )
    log_path = "wiki/log.md"
    with open(log_path, "a") as f:
        f.write(log_entry + "\n")
    print(f"\n  Appended to {log_path}")

    print("\nDone!")


if __name__ == "__main__":
    main()
