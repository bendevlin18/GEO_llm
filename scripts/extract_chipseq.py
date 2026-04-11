"""
Extract ChIP-seq (and related chromatin profiling) datasets from GEO metadata.
Classifies by protocol modality and target type.

Modalities:
  chip_seq       — standard ChIP-seq (default)
  cut_and_run    — CUT&RUN (Cleavage Under Targets & Release Using Nuclease)
  cut_and_tag    — CUT&Tag (Cleavage Under Targets & Tagmentation)
  atac_seq       — ATAC-seq (open chromatin, same GEO type as ChIP-seq)
  chip_exo       — ChIP-exo (higher resolution ChIP variant)

Target types (chip_seq / cut_and_run / cut_and_tag only):
  histone        — histone modification marks (H3K27ac, H3K4me3, etc.)
  tf             — transcription factor binding
  other          — CTCF, cohesin, Pol2, chromatin structural proteins, etc.

Can be run standalone or imported (chipseq_filter, classify_chipseq).
"""
import json
import re
import glob
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
from tag_topics import tag_topics

# ── Protocol modality keywords ─────────────────────────────────────────────

ATAC_KEYWORDS = [
    "atac-seq", "atac seq", "atac_seq", "atacseq",
    "chromatin accessibility", "open chromatin",
    "assay for transposase", "transposase-accessible",
    "snATAC", "scATAC", "single-cell atac", "single-nucleus atac",
]

CUT_AND_RUN_KEYWORDS = [
    "cut&run", "cut-and-run", "cutana",
    "cleavage under targets and release",
    "cleavage under targets & release",
]

CUT_AND_TAG_KEYWORDS = [
    "cut&tag", "cut-and-tag",
    "cleavage under targets and tagmentation",
    "cleavage under targets & tagmentation",
]

CHIP_EXO_KEYWORDS = [
    "chip-exo", "chipexo", "chip exo",
]

# ── Target type keywords ────────────────────────────────────────────────────

# Common histone modification mark patterns
HISTONE_PATTERNS = [
    r'\bH[234][KAT]\d+(?:me[123]|ac|ub|ph|cr|la|bu)\b',   # H3K27ac, H3K4me3, H2AZ, etc.
    r'\bH[234]\b.*\b(?:acetyl|methyl|trimethyl|dimethyl|ubiquit|phospho)',
    r'\bhistone mark\b', r'\bhistone modification\b', r'\bhistone acetyl',
    r'\bhistone methyl', r'\bH3\.3\b', r'\bmacroH2A\b',
]

# Common TF keywords and names (non-exhaustive — catches most cases)
TF_KEYWORDS = [
    "transcription factor", "tf binding", "tf chip",
    "ctcf",         # architectural — we'll put this in "other" below
    "p53", "tp53",
    "myc", "c-myc", "n-myc",
    "stat1", "stat2", "stat3", "stat4", "stat5", "stat6",
    "nf-kb", "nfkb", "rela", "relb",
    "ar ", " ar-", "androgen receptor",
    "er ", "estrogen receptor", "esr1",
    "foxa1", "foxa2",
    "gata", "runx", "nrf2",
    "e2f", "rb1", "brca1", "brca2",
    "spi1", "pu.1", "cebp",
    "yap", "taz", "tead",
    "sox", "oct4", "nanog", "klf4",
    "tead", "brd4", "brd2",
]

# Chromatin structural / architectural proteins → "other"
STRUCTURAL_KEYWORDS = [
    "ctcf", "cohesin", "smc1", "smc3", "rad21", "stag1", "stag2",
    "rna polymerase", "pol ii", "pol2", "polii", "rnap",
    "mediator", "nipbl", "wapl",
    "lamin", "lamina",
    "dnase", "faire",
]


def chipseq_filter(record: dict) -> bool:
    """Return True if the record is a ChIP-seq or related chromatin profiling dataset."""
    return "Genome binding/occupancy profiling by high throughput sequencing" in record.get("gds_type", "")


def classify_chipseq(record: dict) -> tuple[str, str]:
    """
    Return (modality, target_type).

    modality:    chip_seq | cut_and_run | cut_and_tag | atac_seq | chip_exo
    target_type: histone | tf | other  (only meaningful for chip_seq / cut_and_run / cut_and_tag)
    """
    text = f"{record['title']} {record['summary']}".lower()

    # ── Protocol modality (most specific first) ──
    if any(kw in text for kw in ATAC_KEYWORDS):
        return "atac_seq", "n/a"

    if any(kw in text for kw in CUT_AND_TAG_KEYWORDS):
        modality = "cut_and_tag"
    elif any(kw in text for kw in CUT_AND_RUN_KEYWORDS):
        modality = "cut_and_run"
    elif any(kw in text for kw in CHIP_EXO_KEYWORDS):
        modality = "chip_exo"
    else:
        modality = "chip_seq"

    # ── Target type ──
    # Check structural/architectural first (CTCF etc.) before general TF check
    if any(kw in text for kw in STRUCTURAL_KEYWORDS):
        return modality, "other"

    # Histone marks via regex patterns
    full_text = f"{record['title']} {record['summary']}"
    if any(re.search(pat, full_text, re.IGNORECASE) for pat in HISTONE_PATTERNS):
        return modality, "histone"

    # TF binding
    if any(kw in text for kw in TF_KEYWORDS):
        return modality, "tf"

    return modality, "other"


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*",
                        help="Data JSON files (default: all data/geo_metadata_*.json)")
    parser.add_argument("-o", "--output", default="chipseq_classified.json",
                        help="Output file (default: chipseq_classified.json)")
    args = parser.parse_args()

    paths = args.files or sorted(glob.glob("data/geo_metadata_*.json"))
    if not paths:
        sys.exit("No data files found.")

    # Load and deduplicate
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
    chip_records = [r for r in all_records if chipseq_filter(r)]
    print(f"ChIP-seq / chromatin profiling records: {len(chip_records):,}")

    classified = []
    for r in chip_records:
        modality, target_type = classify_chipseq(r)
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
            "target_type": target_type,
        })

    # Tag topics (reuse RNA-seq topic tagger — topics are assay-agnostic)
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

    print("\nTarget type breakdown (chip_seq / cut_and_run / cut_and_tag only):")
    chromatin = [r for r in classified if r["modality"] not in ("atac_seq",)]
    targets = Counter(r["target_type"] for r in chromatin)
    for t, c in targets.most_common():
        print(f"  {c:>6}  {t}")

    print("\nTop organisms:")
    orgs = Counter(r["organism"] for r in classified)
    for org, c in orgs.most_common(10):
        print(f"  {c:>6}  {org}")

    with open(args.output, "w") as f:
        json.dump(classified, f, indent=2)
    print(f"\nSaved {len(classified):,} records to {args.output}")


if __name__ == "__main__":
    main()
