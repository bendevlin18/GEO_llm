"""
Generate wiki markdown pages from classified RNA-seq data.
Produces per-modality and per-organism pages with dataset tables.
"""
import json
import os
from collections import Counter, defaultdict

with open("rnaseq_classified.json") as f:
    data = json.load(f)

WIKI = "wiki"

# Derive date range from data
_dates = sorted(set(r["pub_date"] for r in data if r.get("pub_date")))
DATE_RANGE = f"{_dates[0]} – {_dates[-1]}" if _dates else "unknown"


def suppfile_summary(records):
    """Summarize supplementary file types."""
    supps = Counter()
    for r in records:
        for s in r["suppfile"].split(", "):
            if s.strip():
                supps[s.strip()] += 1
    return supps


def top_items(records, key, n=15):
    """Count top values for a given field."""
    return Counter(r[key] for r in records if r[key]).most_common(n)


def dataset_table(records, max_rows=50):
    """Generate a markdown table of datasets."""
    lines = []
    lines.append("| Accession | Title | Organism | Samples | Archive Contents | Date |")
    lines.append("|-----------|-------|----------|--------:|-----------------|------|")
    for r in records[:max_rows]:
        title = r["title"][:80] + ("..." if len(r["title"]) > 80 else "")
        acc = r["accession"]
        link = f"[{acc}](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={acc})"
        lines.append(f"| {link} | {title} | {r['organism']} | {r['n_samples']} | {r['suppfile']} | {r['pub_date']} |")
    if len(records) > max_rows:
        lines.append(f"\n*...and {len(records) - max_rows} more datasets.*")
    return "\n".join(lines)


def write_modality_page(modality, label, description, records):
    """Write a modality wiki page."""
    orgs = top_items(records, "organism")
    supps = suppfile_summary(records)

    content = f"""# {label}

> {len(records)} datasets | {DATE_RANGE}

{description}

## Organism Distribution

| Organism | Count |
|----------|------:|
"""
    for org, c in orgs:
        content += f"| {org} | {c} |\n"

    content += f"""
## Archive Contents (file types inside supplementary TAR/gz)

| Type | Count | Description |
|------|------:|-------------|
"""
    type_desc = {
        "TXT": "Text files (count matrices, gene lists, metadata)",
        "CSV": "Comma-separated (count matrices, DE results)",
        "TSV": "Tab-separated (10x barcodes/features, metadata)",
        "XLSX": "Excel (DE results, sample annotations)",
        "XLS": "Excel (legacy format)",
        "MTX": "Sparse matrices (10x CellRanger output)",
        "H5": "HDF5 (CellRanger filtered matrices)",
        "H5AD": "AnnData HDF5 (scanpy/Python ecosystem)",
        "RDS": "R serialized objects (Seurat, SingleCellExperiment)",
        "BW": "BigWig (coverage tracks)",
        "BIGWIG": "BigWig (coverage tracks)",
        "TAR": "Tar archives (bundled outputs)",
        "JSON": "JSON (cell metadata, spatial coordinates)",
        "PNG": "Images (spatial, QC plots)",
        "JPG": "Images (spatial, QC plots)",
        "LOOM": "Loom files (single-cell matrices)",
    }
    for s, c in supps.most_common(15):
        desc = type_desc.get(s, "")
        content += f"| {s} | {c} | {desc} |\n"

    # Recent datasets
    recent = sorted(records, key=lambda r: r["pub_date"], reverse=True)
    content += f"\n## Recent Datasets\n\n{dataset_table(recent)}\n"

    path = os.path.join(WIKI, "assays", f"{modality}.md")
    with open(path, "w") as f:
        f.write(content)
    print(f"  Wrote {path} ({len(records)} records)")


def write_organism_page(organism, slug, records):
    """Write an organism wiki page."""
    modalities = Counter(r["modality"] for r in records)
    supps = suppfile_summary(records)

    content = f"""# {organism}

> {len(records)} RNA-seq datasets | {DATE_RANGE}

## Modality Breakdown

| Modality | Count |
|----------|------:|
"""
    for mod, c in modalities.most_common():
        content += f"| {mod} | {c} |\n"

    content += f"""
## Archive Contents (file types inside supplementary TAR/gz)

| Type | Count |
|------|------:|
"""
    for s, c in supps.most_common(10):
        content += f"| {s} | {c} |\n"

    recent = sorted(records, key=lambda r: r["pub_date"], reverse=True)
    content += f"\n## Recent Datasets\n\n{dataset_table(recent)}\n"

    path = os.path.join(WIKI, "organisms", f"{slug}.md")
    with open(path, "w") as f:
        f.write(content)
    print(f"  Wrote {path} ({len(records)} records)")


# --- Generate modality pages ---

modality_info = {
    "bulk_rnaseq": {
        "filter": "bulk",
        "label": "Bulk RNA-seq",
        "desc": "Standard RNA-sequencing of bulk tissue or cell populations. Each sample represents the averaged transcriptome of many cells.",
    },
    "scrna_seq": {
        "filter": "single-cell",
        "label": "Single-Cell RNA-seq (scRNA-seq)",
        "desc": "Transcriptome profiling at single-cell resolution. Typically uses droplet-based (10x Chromium, Drop-seq) or plate-based (Smart-seq) protocols. Supplementary files often include sparse count matrices (MTX), HDF5 objects (H5/H5AD), or R objects (RDS/Seurat).",
    },
    "snrna_seq": {
        "filter": "single-nucleus",
        "label": "Single-Nucleus RNA-seq (snRNA-seq)",
        "desc": "Transcriptome profiling from isolated nuclei rather than whole cells. Preferred for tissues that are difficult to dissociate (e.g., brain, adipose, muscle) or for frozen archival samples.",
    },
    "spatial": {
        "filter": "spatial",
        "label": "Spatial Transcriptomics",
        "desc": "Spatially-resolved transcriptomics that preserves tissue context. Includes sequencing-based (10x Visium, Slide-seq, Stereo-seq) and imaging-based (MERFISH, seqFISH, CosMx, Xenium) methods. Supplementary files may include spatial coordinates (JSON/CSV) and tissue images (PNG/JPG).",
    },
}

print("Generating modality pages...")
for slug, info in modality_info.items():
    records = [r for r in data if r["modality"] == info["filter"]]
    write_modality_page(slug, info["label"], info["desc"], records)

# --- Generate organism pages ---

print("\nGenerating organism pages...")
org_groups = defaultdict(list)
for r in data:
    org_groups[r["organism"]].append(r)

# Only generate pages for organisms with >= 20 datasets
for org, records in sorted(org_groups.items(), key=lambda x: -len(x[1])):
    if len(records) < 20:
        continue
    slug = org.lower().replace(" ", "_").replace(";", "").replace("/", "_")
    write_organism_page(org, slug, records)

# --- Generate topic pages ---

# Topic display names (must match keys used in tag_topics.py)
TOPIC_NAMES = {
    "cancer": "Cancer",
    "immunology": "Immunology",
    "neuroscience": "Neuroscience",
    "development": "Development & Differentiation",
    "cardiovascular": "Cardiovascular",
    "metabolism": "Metabolism & Metabolic Disease",
    "epigenetics": "Epigenetics & Chromatin",
    "infectious_disease": "Infectious Disease",
    "fibrosis_wound": "Fibrosis & Wound Healing",
    "aging": "Aging & Senescence",
    "kidney": "Kidney & Renal",
    "gut_intestine": "Gut & Intestinal Biology",
    "lung_respiratory": "Lung & Respiratory",
    "skeletal_muscle": "Muscle & Musculoskeletal",
    "skin": "Skin & Dermatology",
    "reproduction": "Reproductive Biology",
    "hematopoiesis": "Hematopoiesis & Blood",
    "crispr_gene_editing": "CRISPR & Gene Editing",
    "drug_response": "Drug Response & Pharmacology",
    "plant_biology": "Plant Biology",
    "microbiology": "Microbiology",
    "cell_stress": "Cell Stress & Homeostasis",
    "rna_biology": "RNA Biology & Regulation",
    "gene_regulation": "Gene Regulation & Transcription",
    "cell_cycle": "Cell Cycle & Proliferation",
    "signal_transduction": "Signal Transduction",
    "eye_vision": "Eye & Vision",
    "liver": "Liver & Hepatology",
}


def write_topic_page(topic_key, topic_name, records):
    """Write a topic wiki page."""
    modalities = Counter(r["modality"] for r in records)
    orgs = top_items(records, "organism", n=10)
    supps = suppfile_summary(records)

    # Co-occurring topics
    co_topics = Counter()
    for r in records:
        for t in r.get("topics", []):
            if t != topic_key:
                co_topics[t] += 1

    content = f"""# {topic_name}

> {len(records)} RNA-seq datasets | {DATE_RANGE}

## Modality Breakdown

| Modality | Count |
|----------|------:|
"""
    for mod, c in modalities.most_common():
        content += f"| {mod} | {c} |\n"

    content += """
## Organism Distribution

| Organism | Count |
|----------|------:|
"""
    for org, c in orgs:
        content += f"| {org} | {c} |\n"

    # Related topics
    if co_topics:
        content += """
## Related Topics

| Topic | Co-occurring Datasets |
|-------|---------------------:|
"""
        for t, c in co_topics.most_common(10):
            tname = TOPIC_NAMES.get(t, t)
            content += f"| [{tname}]({t}.md) | {c} |\n"

    content += """
## Archive Contents (file types inside supplementary TAR/gz)

| Type | Count |
|------|------:|
"""
    for s, c in supps.most_common(10):
        content += f"| {s} | {c} |\n"

    recent = sorted(records, key=lambda r: r["pub_date"], reverse=True)
    content += f"\n## Recent Datasets\n\n{dataset_table(recent)}\n"

    path = os.path.join(WIKI, "topics", f"{topic_key}.md")
    with open(path, "w") as f:
        f.write(content)
    print(f"  Wrote {path} ({len(records)} records)")


print("\nGenerating topic pages...")
os.makedirs(os.path.join(WIKI, "topics"), exist_ok=True)

topic_groups = defaultdict(list)
for r in data:
    for t in r.get("topics", []):
        topic_groups[t].append(r)

topic_summary = []
for key in sorted(topic_groups, key=lambda k: -len(topic_groups[k])):
    records = topic_groups[key]
    name = TOPIC_NAMES.get(key, key)
    write_topic_page(key, name, records)
    topic_summary.append((key, name, len(records)))

# --- Update index.md with topics ---

topic_table = "| Topic | Count | Page |\n|-------|------:|------|\n"
for key, name, count in topic_summary:
    topic_table += f"| {name} | {count:,} | [{key}.md](topics/{key}.md) |\n"

# Read current index and insert/replace topics section
index_path = os.path.join(WIKI, "index.md")
with open(index_path) as f:
    index = f.read()

# Insert topic section after modality section
if "## By Research Topic" in index:
    # Replace existing
    before = index[:index.index("## By Research Topic")]
    after_marker = "## By Organism"
    after = index[index.index(after_marker):]
    index = before + f"## By Research Topic\n\n{topic_table}\n{after}"
else:
    # Insert before "## By Organism"
    marker = "## By Organism"
    idx = index.index(marker)
    index = index[:idx] + f"## By Research Topic\n\n{topic_table}\n{index[idx:]}"

with open(index_path, "w") as f:
    f.write(index)
print(f"\n  Updated {index_path} with topic index")

print("\nDone.")
