"""
Extract multiomics datasets from GEO metadata and back-annotate related
classified JSON files with is_multiomics: true.

Multiomics = simultaneous profiling of multiple molecular modalities from
the same cells/samples in a single experiment (e.g. RNA + protein, RNA + ATAC).
Does NOT include studies that simply measure multiple assay types separately.

Modalities:
  cite_seq          — RNA + surface protein (CITE-seq, REAP-seq, ASAP-seq, etc.)
  multiome          — RNA + ATAC chromatin accessibility (10x Multiome, SHARE-seq,
                      SNARE-seq, Paired-seq)
  spatial_multiomics — Spatial transcriptomics paired with another assay
  other_multiomics  — Multi-assay joint profiling not in the above categories
                      (TEA-seq, DOGMA-seq, Perturb-CITE, triomics, etc.)

Back-annotation:
  After building multiomics_classified.json, this script patches
  rnaseq_classified.json and chipseq_classified.json in-place, setting
  is_multiomics: true on any record whose accession appears in the multiomics
  set. Records not in the multiomics set are not modified.

Can be run standalone or imported (multiomics_filter, classify_multiomics).
"""
import json
import glob
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
from tag_topics import tag_topics

# ── High-confidence keywords (protocol-specific) ──────────────────────────────
# These are precise enough to classify regardless of gds_type.

CITE_SEQ_KEYWORDS = [
    "cite-seq", "citeseq", "cite seq",
    "reap-seq", "reapseq",
    "asap-seq", "asapseq",
    "perturb-cite", "perturbcite",
    "eccite-seq", "ecciteseq",
    "protein and rna sequencing",   # deliberate narrow phrase
    "rna and protein sequencing",
    "antibody-derived tags",        # ADT — core CITE-seq concept (full phrase, not abbreviation)
    "feature barcoding",
]

MULTIOME_KEYWORDS = [
    "10x multiome", "10x chromium multiome",
    "share-seq", "shareseq",        # "share seq" omitted — substring of "share sequence"
    "snare-seq", "snareseq",        # "snare seq" omitted — substring of "snare sequence"
    "paired-seq", "pairedseq",      # "paired seq" omitted — substring of "paired sequencing"
    "sccat-seq", "sccatseq",
    "rna+atac", "rna + atac",
    "atac+rna", "atac + rna",
]

SPATIAL_MULTIOMICS_KEYWORDS = [
    "spatial multiomics", "spatial multi-omics",
    "spatial proteomics", "spatial transcriptomics and proteomics",
    "spatial epigenomics", "spatial transcriptomics and epigenomics",
    "spatial transcriptomics and atac",
    "stereo-cite", "slide-tags",
]

OTHER_MULTIOMICS_KEYWORDS = [
    "tea-seq", "teaseq",            # "tea seq" omitted — too generic
    "dogma-seq", "dogmaseq",
    "triome", "tri-omic", "tri-modal",
    "mome-seq", "momeseq",
    "scnmt-seq", "scnmt seq",        # single-cell nucleosome, methylation, transcription
    "multiome plus",
]

# ── Context-dependent keywords ────────────────────────────────────────────────
# These fire only when gds_type is a compound type (contains ";"), which signals
# that GEO itself classified the record under multiple assay categories.
# This filters out abstracts that merely mention multiple omic types in passing.

CONTEXT_DEPENDENT_KEYWORDS = [
    "joint profiling",
    "simultaneous profiling",
    "simultaneous measurement",
    "simultaneous sequencing",
    "multiome",          # without "10x" prefix — too generic alone
    "multi-ome",
    "co-profiling",
    "dual profiling",
    "parallel profiling",
    "single-cell multiomics",
    "single cell multiomics",
    "sc-multiomics",
]

# GDS types that strongly suggest joint profiling (contain multiple categories)
COMPOUND_GDS_TYPES = {
    "Expression profiling by high throughput sequencing; Other",
    "Expression profiling by high throughput sequencing; Genome binding/occupancy profiling by high throughput sequencing",
    "Genome binding/occupancy profiling by high throughput sequencing; Expression profiling by high throughput sequencing",
    "Expression profiling by high throughput sequencing; Genome binding/occupancy profiling by high throughput sequencing; Other",
    "Expression profiling by high throughput sequencing; Methylation profiling by high throughput sequencing",
    "Methylation profiling by high throughput sequencing; Expression profiling by high throughput sequencing",
    "Other",
}


def _has_compound_gds(record: dict) -> bool:
    gds = record.get("gds_type", "")
    # Any gds_type with a semicolon, or explicitly "Other"
    return ";" in gds or gds == "Other"


def multiomics_filter(record: dict) -> bool:
    """Return True if the record is a joint multiomics dataset."""
    text = f"{record.get('title', '')} {record.get('summary', '')}".lower()

    # High-confidence: protocol-specific keywords match unconditionally
    if any(kw in text for kw in CITE_SEQ_KEYWORDS):
        return True
    if any(kw in text for kw in MULTIOME_KEYWORDS):
        return True
    if any(kw in text for kw in SPATIAL_MULTIOMICS_KEYWORDS):
        return True
    if any(kw in text for kw in OTHER_MULTIOMICS_KEYWORDS):
        return True

    # Context-dependent: only when gds_type is compound
    if _has_compound_gds(record):
        if any(kw in text for kw in CONTEXT_DEPENDENT_KEYWORDS):
            return True

    return False


def classify_multiomics(record: dict) -> str:
    """
    Return the multiomics modality string.

    cite_seq | multiome | spatial_multiomics | other_multiomics
    """
    text = f"{record.get('title', '')} {record.get('summary', '')}".lower()

    if any(kw in text for kw in SPATIAL_MULTIOMICS_KEYWORDS):
        return "spatial_multiomics"

    if any(kw in text for kw in OTHER_MULTIOMICS_KEYWORDS):
        return "other_multiomics"

    if any(kw in text for kw in MULTIOME_KEYWORDS):
        return "multiome"

    if any(kw in text for kw in CITE_SEQ_KEYWORDS):
        return "cite_seq"

    # Context-dependent hits default to other_multiomics
    return "other_multiomics"


def back_annotate(multiomics_accessions: set[str], classified_path: str) -> int:
    """
    Set is_multiomics: true on records in classified_path whose accession
    is in multiomics_accessions. Returns the count of records updated.
    """
    if not os.path.exists(classified_path):
        print(f"  Skipping back-annotation: {classified_path} not found")
        return 0

    with open(classified_path) as f:
        records = json.load(f)

    updated = 0
    for r in records:
        if r.get("accession") in multiomics_accessions:
            if not r.get("is_multiomics"):
                r["is_multiomics"] = True
                updated += 1

    with open(classified_path, "w") as f:
        json.dump(records, f, indent=2)

    print(f"  Back-annotated {updated:,} records in {classified_path}")
    return updated


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "files", nargs="*",
        help="Data JSON files (default: all data/geo_metadata_*.json)",
    )
    parser.add_argument(
        "-o", "--output", default="multiomics_classified.json",
        help="Output file (default: multiomics_classified.json)",
    )
    parser.add_argument(
        "--no-back-annotate", action="store_true",
        help="Skip back-annotating rnaseq_classified.json and chipseq_classified.json",
    )
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
    multi_records = [r for r in all_records if multiomics_filter(r)]
    print(f"Multiomics records: {len(multi_records):,}")

    classified = []
    for r in multi_records:
        modality = classify_multiomics(r)
        classified.append({
            "accession": r["accession"],
            "title": r["title"],
            "summary": r.get("summary", "")[:500],
            "organism": r.get("organism", ""),
            "n_samples": r.get("n_samples", 0),
            "platform_id": r.get("platform_id", ""),
            "suppfile": r.get("suppfile", ""),
            "pub_date": r.get("pub_date", ""),
            "modality": modality,
        })

    # Tag topics
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
    orgs = Counter(r.get("organism", "") for r in classified)
    for org, c in orgs.most_common(10):
        print(f"  {c:>6}  {org}")

    # Save multiomics_classified.json
    with open(args.output, "w") as f:
        json.dump(classified, f, indent=2)
    print(f"\nSaved {len(classified):,} records to {args.output}")

    # Back-annotate related classified files
    if not args.no_back_annotate:
        multiomics_accessions = {r["accession"] for r in classified}
        print("\nBack-annotating related classified files...")
        back_annotate(multiomics_accessions, "rnaseq_classified.json")
        back_annotate(multiomics_accessions, "chipseq_classified.json")
        back_annotate(multiomics_accessions, "methylation_classified.json")


if __name__ == "__main__":
    main()
