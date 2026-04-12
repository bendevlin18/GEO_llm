"""
Generate wiki markdown pages from classified RNA-seq and ChIP-seq data.
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

# ── ChIP-seq / ATAC-seq pages ──────────────────────────────────────────────

CHIPSEQ_FILE = "chipseq_classified.json"

if os.path.exists(CHIPSEQ_FILE):
    with open(CHIPSEQ_FILE) as f:
        chipseq_data = json.load(f)

    _chip_dates = sorted(set(r["pub_date"] for r in chipseq_data if r.get("pub_date")))
    CHIP_DATE_RANGE = f"{_chip_dates[0]} – {_chip_dates[-1]}" if _chip_dates else "unknown"

    CHIPSEQ_FILE_TYPES = {
        "BED":        "BED peak calls (genomic intervals)",
        "BIGWIG":     "BigWig coverage tracks",
        "BW":         "BigWig coverage tracks",
        "NARROWPEAK": "ENCODE narrowPeak format (TF / sharp peaks)",
        "BROADPEAK":  "ENCODE broadPeak format (histone / broad marks)",
        "BEDGRAPH":   "BedGraph coverage files",
        "BAM":        "Aligned reads (BAM)",
        "TXT":        "Text files (peak lists, count tables, metadata)",
        "CSV":        "Comma-separated data",
        "TSV":        "Tab-separated data",
        "TAR":        "Tar archives (bundled outputs)",
        "WIG":        "Wiggle coverage format",
        "GTF":        "Gene/peak annotation (GTF/GFF)",
        "BAR":        "BAR peak files (older format)",
        "PEAKS":      "Peak call files",
    }

    def write_chipseq_modality_page(slug: str, label: str, description: str,
                                    records: list, show_target_breakdown: bool = True) -> None:
        orgs = top_items(records, "organism")
        supps = suppfile_summary(records)

        content = f"""# {label}

> {len(records)} datasets | {CHIP_DATE_RANGE}

{description}
"""
        if show_target_breakdown and any("target_type" in r for r in records):
            targets = Counter(r.get("target_type", "other") for r in records)
            content += """
## Target Type Breakdown

| Target Type | Count | Description |
|-------------|------:|-------------|
"""
            target_descs = {
                "histone": "Histone modification marks (H3K27ac, H3K4me3, H3K27me3, etc.)",
                "tf":      "Transcription factor binding sites",
                "other":   "Chromatin structural proteins (CTCF, cohesin, Pol2, etc.)",
                "n/a":     "Not applicable",
            }
            for t, c in targets.most_common():
                desc = target_descs.get(t, "")
                content += f"| {t} | {c} | {desc} |\n"

        content += """
## Organism Distribution

| Organism | Count |
|----------|------:|
"""
        for org, c in orgs:
            content += f"| {org} | {c} |\n"

        content += """
## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
"""
        for s, c in supps.most_common(15):
            desc = CHIPSEQ_FILE_TYPES.get(s.upper(), "")
            content += f"| {s} | {c} | {desc} |\n"

        recent = sorted(records, key=lambda r: r["pub_date"], reverse=True)
        content += f"\n## Recent Datasets\n\n{dataset_table(recent)}\n"

        os.makedirs(os.path.join(WIKI, "assays"), exist_ok=True)
        path = os.path.join(WIKI, "assays", f"{slug}.md")
        with open(path, "w") as f:
            f.write(content)
        print(f"  Wrote {path} ({len(records)} records)")

    chipseq_modality_info = {
        "chip_seq": {
            "label": "ChIP-seq",
            "filter": "chip_seq",
            "desc": (
                "Chromatin immunoprecipitation followed by sequencing (ChIP-seq). "
                "Profiles histone modification marks, transcription factor binding sites, "
                "and chromatin-associated proteins genome-wide. "
                "Supplementary files typically include peak calls (BED, narrowPeak, broadPeak) "
                "and coverage tracks (BigWig)."
            ),
            "target_breakdown": True,
        },
        "atac_seq": {
            "label": "ATAC-seq",
            "filter": "atac_seq",
            "desc": (
                "Assay for Transposase-Accessible Chromatin with sequencing (ATAC-seq). "
                "Maps open/accessible chromatin regions genome-wide using Tn5 transposase. "
                "Available as bulk ATAC-seq and single-cell ATAC-seq (scATAC-seq). "
                "Supplementary files typically include peak calls (BED, narrowPeak) and "
                "coverage tracks (BigWig), with fragment files (TSV) for single-cell data."
            ),
            "target_breakdown": False,
        },
        "cut_and_run": {
            "label": "CUT&RUN",
            "filter": "cut_and_run",
            "desc": (
                "Cleavage Under Targets and Release Using Nuclease (CUT&RUN). "
                "An antibody-targeted approach that uses tethered MNase to cleave chromatin "
                "near bound proteins. Lower background than ChIP-seq, works well with fewer cells. "
                "Supplementary files follow the same conventions as ChIP-seq (BED, BigWig)."
            ),
            "target_breakdown": True,
        },
        "cut_and_tag": {
            "label": "CUT&Tag",
            "filter": "cut_and_tag",
            "desc": (
                "Cleavage Under Targets and Tagmentation (CUT&Tag). "
                "Uses protein-A-Tn5 fusion to simultaneously cut and tag chromatin near "
                "antibody-bound targets. Even lower background than CUT&RUN, compatible with "
                "single cells. Supplementary files: BED, BigWig, narrowPeak."
            ),
            "target_breakdown": True,
        },
        "chip_exo": {
            "label": "ChIP-exo",
            "filter": "chip_exo",
            "desc": (
                "ChIP-exo adds an exonuclease digestion step to standard ChIP-seq, "
                "providing single-nucleotide resolution of protein-DNA binding. "
                "Primarily used for precise TF binding site mapping."
            ),
            "target_breakdown": True,
        },
    }

    print("\nGenerating ChIP-seq / chromatin assay pages...")
    for slug, info in chipseq_modality_info.items():
        records = [r for r in chipseq_data if r["modality"] == info["filter"]]
        if not records:
            continue
        write_chipseq_modality_page(
            slug, info["label"], info["desc"], records,
            show_target_breakdown=info["target_breakdown"],
        )
else:
    print("\nNo chipseq_classified.json found — skipping ChIP-seq wiki pages.")

# ── Methylation pages ─────────────────────────────────────────────────────────

METHYLATION_FILE = "methylation_classified.json"

if os.path.exists(METHYLATION_FILE):
    with open(METHYLATION_FILE) as f:
        meth_data = json.load(f)

    _meth_dates = sorted(set(r["pub_date"] for r in meth_data if r.get("pub_date")))
    METH_DATE_RANGE = f"{_meth_dates[0]} – {_meth_dates[-1]}" if _meth_dates else "unknown"

    METHYLATION_FILE_TYPES = {
        "TXT":    "Text files (methylation tables, coverage files, metadata)",
        "BED":    "BED files (CpG methylation calls, DMR intervals)",
        "CSV":    "Comma-separated methylation data",
        "TSV":    "Tab-separated methylation data",
        "BIGWIG": "BigWig coverage / methylation tracks",
        "BW":     "BigWig coverage / methylation tracks",
        "BEDGRAPH": "BedGraph methylation coverage",
        "IDAT":   "Illumina array raw intensity data (450K / EPIC)",
        "CG":     "CpG methylation call files (Bismark, BSseeker)",
        "TAR":    "Tar archives (bundled outputs)",
        "XLSX":   "Excel (methylation tables, differential analysis)",
        "RDS":    "R serialized objects (minfi, SummarizedExperiment)",
        "H5":     "HDF5 methylation data",
        "BIS":    "Bismark alignment / methylation extraction output",
        "COV":    "Coverage / bismark bismark .cov files",
    }

    def write_methylation_page(slug: str, label: str, description: str,
                               records: list) -> None:
        orgs = top_items(records, "organism")
        supps = suppfile_summary(records)

        content = f"""# {label}

> {len(records)} datasets | {METH_DATE_RANGE}

{description}

## Organism Distribution

| Organism | Count |
|----------|------:|
"""
        for org, c in orgs:
            content += f"| {org} | {c} |\n"

        content += """
## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
"""
        for s, c in supps.most_common(15):
            desc = METHYLATION_FILE_TYPES.get(s.upper(), "")
            content += f"| {s} | {c} | {desc} |\n"

        recent = sorted(records, key=lambda r: r["pub_date"], reverse=True)
        content += f"\n## Recent Datasets\n\n{dataset_table(recent)}\n"

        os.makedirs(os.path.join(WIKI, "assays"), exist_ok=True)
        path = os.path.join(WIKI, "assays", f"{slug}.md")
        with open(path, "w") as f:
            f.write(content)
        print(f"  Wrote {path} ({len(records)} records)")

    methylation_modality_info = {
        "methylation": {
            "label": "DNA Methylation Profiling",
            "filter": None,   # all records = overview page
            "desc": (
                "All DNA methylation profiling datasets on GEO, including bisulfite sequencing "
                "(WGBS, RRBS), enzymatic methods (EM-seq), hydroxymethylation profiling (5hmC-seq), "
                "immunoprecipitation-based approaches (MeDIP-seq), and Illumina Infinium arrays "
                "(450K, EPIC). See individual assay pages for protocol-specific views."
            ),
        },
        "wgbs": {
            "label": "WGBS (Whole Genome Bisulfite Sequencing)",
            "filter": "wgbs",
            "desc": (
                "Whole Genome Bisulfite Sequencing (WGBS). Provides single-base resolution "
                "methylation maps across the entire genome by treating DNA with sodium bisulfite "
                "(which converts unmethylated cytosines to uracil) before sequencing. "
                "Supplementary files typically include CpG methylation calls (BED, BedGraph, "
                "TXT) and coverage tracks (BigWig)."
            ),
        },
        "rrbs": {
            "label": "RRBS (Reduced Representation Bisulfite Sequencing)",
            "filter": "rrbs",
            "desc": (
                "Reduced Representation Bisulfite Sequencing (RRBS). A cost-efficient bisulfite "
                "sequencing approach that focuses coverage on CpG-rich regions by using "
                "restriction enzyme digestion (typically MspI) prior to sequencing. Provides "
                "single-base resolution at a fraction of the cost of WGBS."
            ),
        },
        "methylation_array": {
            "label": "Methylation Arrays (450K / EPIC)",
            "filter": "methylation_array",
            "desc": (
                "Illumina Infinium methylation arrays, including the 27K, 450K (HumanMethylation450), "
                "and EPIC (850K) platforms. Measure methylation beta-values at hundreds of thousands "
                "of CpG sites. Widely used in epigenome-wide association studies (EWAS) and clinical "
                "research. Supplementary files often include IDAT files (raw intensities) or "
                "processed beta-value matrices (CSV, TXT, RDS)."
            ),
        },
        "em_seq": {
            "label": "EM-seq (Enzymatic Methyl-seq)",
            "filter": "em_seq",
            "desc": (
                "Enzymatic Methyl-seq (EM-seq) uses TET2 and APOBEC3A enzymes instead of "
                "bisulfite conversion to distinguish methylated from unmethylated cytosines. "
                "Preserves DNA integrity better than bisulfite treatment, enabling higher "
                "complexity libraries and more uniform coverage."
            ),
        },
        "medip_seq": {
            "label": "MeDIP-seq",
            "filter": "medip_seq",
            "desc": (
                "Methylated DNA Immunoprecipitation sequencing (MeDIP-seq). Uses an antibody "
                "against 5-methylcytosine to immunoprecipitate methylated DNA fragments before "
                "sequencing. Provides genome-wide methylation enrichment data but at lower "
                "resolution than bisulfite-based methods."
            ),
        },
        "hmc_seq": {
            "label": "5hmC Sequencing",
            "filter": "hmc_seq",
            "desc": (
                "Profiling of 5-hydroxymethylcytosine (5hmC), an oxidized form of 5mC produced "
                "by TET enzymes and linked to active DNA demethylation. Methods include "
                "hMeDIP-seq (antibody-based), TAB-seq (bisulfite-based), and chemical labeling "
                "approaches. Enriched in brain tissue, embryonic cells, and gene regulatory "
                "regions."
            ),
        },
        "oxbs_seq": {
            "label": "oxBS-seq / TAB-seq",
            "filter": "oxbs_seq",
            "desc": (
                "Oxidative Bisulfite Sequencing (oxBS-seq) uses potassium perruthenate to "
                "oxidize 5hmC to 5fC before bisulfite conversion, allowing strand-specific "
                "5mC quantification at single-base resolution. TET-Assisted Bisulfite "
                "sequencing (TAB-seq) is a related approach for profiling 5hmC directly."
            ),
        },
        "other_methylation": {
            "label": "Other Methylation Profiling",
            "filter": "other_methylation",
            "desc": (
                "Methylation profiling datasets where the specific protocol could not be "
                "determined from the title and summary. Includes SuperSeries that aggregate "
                "multiple SubSeries, studies using targeted bisulfite amplicon sequencing, "
                "and records with minimal metadata."
            ),
        },
    }

    print("\nGenerating methylation assay pages...")
    for slug, info in methylation_modality_info.items():
        if info["filter"] is None:
            records = meth_data   # overview page = all records
        else:
            records = [r for r in meth_data if r["modality"] == info["filter"]]
        if not records:
            print(f"  Skipping {slug} — no records")
            continue
        write_methylation_page(slug, info["label"], info["desc"], records)
else:
    print("\nNo methylation_classified.json found — skipping methylation wiki pages.")

print("\nDone.")
