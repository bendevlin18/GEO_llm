"""
Extract RNA-seq datasets from GEO metadata and classify by modality.
Rule-based first pass, with ambiguous records flagged for LLM review.

Can be run standalone or imported (classify, rna_filter).
"""
import json
import re
from collections import Counter

SC_KEYWORDS = [
    "single-cell", "single cell", "scrna-seq", "scrna seq", "scrnaseq",
    "10x genomics", "10x chromium", "drop-seq", "dropseq", "indrops",
    "smart-seq", "smartseq", "cel-seq", "celseq",
    "single-cell rna", "sc-rna", "sc rna-seq",
]

SN_KEYWORDS = [
    "single-nucleus", "single nucleus", "snrna-seq", "snrna seq", "snrnaseq",
    "sn-rna", "nuclei rna", "sn rna",
]

SPATIAL_KEYWORDS = [
    "spatial transcriptom", "visium", "merfish", "slide-seq", "slideseq",
    "seqfish", "starmap", "10x spatial", "stereo-seq", "stereoseq",
    "spatial rna", "cosmx", "xenium",
]

# Supplementary file types strongly associated with single-cell
SC_SUPPFILES = ["MTX", "H5AD", "H5", "LOOM"]

BULK_SIGNALS = [
    "bulk rna-seq", "bulk rna seq", "bulk rnaseq", "mrna-seq", "mrna seq",
    "poly-a rna", "polya rna", "bulk transcriptom",
]


def rna_filter(record):
    """Return True if the record is an RNA-seq dataset."""
    return "Expression profiling by high throughput sequencing" in record.get("gds_type", "")


def classify(record):
    """Rule-based classification of RNA-seq modality."""
    text = f"{record['title']} {record['summary']}".lower()
    suppfile = record.get("suppfile", "").upper()

    # Spatial (most specific — check first)
    if any(kw in text for kw in SPATIAL_KEYWORDS):
        return "spatial"

    # Single-nucleus
    if any(kw in text for kw in SN_KEYWORDS):
        return "single-nucleus"

    # Single-cell by keywords
    if any(kw in text for kw in SC_KEYWORDS):
        return "single-cell"

    # Single-cell by supplementary file type (MTX, H5AD, H5, LOOM)
    if any(x in suppfile for x in SC_SUPPFILES):
        return "single-cell"

    # Explicit bulk signal
    if any(kw in text for kw in BULK_SIGNALS):
        return "bulk"

    # Default: bulk (most HTS expression profiling without sc markers is bulk)
    return "bulk"


if __name__ == "__main__":
    with open("geo_metadata.json") as f:
        data = json.load(f)

    rna = [r for r in data if rna_filter(r)]

    results = []
    for r in rna:
        modality = classify(r)
        results.append({
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

    # Stats
    modalities = Counter(r["modality"] for r in results)
    print("RNA-seq modality classification:")
    for m, c in modalities.most_common():
        print(f"  {c:>5}  {m}")
    print(f"\nTotal: {len(results)}")

    # Organism breakdown per modality
    print("\nOrganism breakdown per modality:")
    for mod in ["bulk", "single-cell", "single-nucleus", "spatial"]:
        subset = [r for r in results if r["modality"] == mod]
        orgs = Counter(r["organism"] for r in subset)
        print(f"\n  {mod} ({len(subset)}):")
        for org, c in orgs.most_common(5):
            print(f"    {c:>5}  {org}")

    # Save
    with open("rnaseq_classified.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nSaved to rnaseq_classified.json")
