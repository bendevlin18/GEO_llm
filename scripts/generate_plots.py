"""
Generate static PNG charts for the GitHub README from classified dataset files.

Outputs to assets/ (checked into git, renders on GitHub without setup).

Charts produced:
  assets/plot_assay_overview.png    — total datasets by assay family
  assets/plot_rnaseq_modalities.png — RNA-seq breakdown by modality
  assets/plot_growth_over_time.png  — datasets added per year, by assay family
  assets/plot_top_organisms.png     — top 15 organisms (RNA-seq)
  assets/plot_topics.png            — top research topics (RNA-seq)

Requires: matplotlib (conda install -n GEO_llm matplotlib)
"""
import json
import os
import sys
from collections import Counter, defaultdict

try:
    import matplotlib
    matplotlib.use("Agg")  # non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mticker
except ImportError:
    sys.exit(
        "matplotlib not found. Install it with:\n"
        "  conda install -n GEO_llm matplotlib"
    )

# ── Config ────────────────────────────────────────────────────────────────────

ASSETS = "assets"
os.makedirs(ASSETS, exist_ok=True)

DPI = 150
FIG_W = 9       # inches — ~1350px at 150dpi, scales nicely in GitHub

# Assay family colors (consistent across all charts)
ASSAY_COLORS = {
    "RNA-seq":      "#4C72B0",
    "ChIP-seq":     "#DD8452",
    "ATAC-seq":     "#55A868",
    "Methylation":  "#C44E52",
    "CUT&RUN/Tag":  "#8172B2",
    "Multiomics":   "#937860",
}

# Modality display names and colors within RNA-seq
MODALITY_LABELS = {
    "bulk":          "Bulk RNA-seq",
    "single-cell":   "scRNA-seq",
    "single-nucleus":"snRNA-seq",
    "spatial":       "Spatial",
}
MODALITY_COLORS = {
    "bulk":          "#4C72B0",
    "single-cell":   "#55A868",
    "single-nucleus":"#DD8452",
    "spatial":       "#C44E52",
}

plt.rcParams.update({
    "font.family":  "sans-serif",
    "font.size":    11,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.grid":         True,
    "axes.grid.axis":    "x",
    "grid.alpha":        0.4,
    "grid.linewidth":    0.8,
})


# ── Load data ─────────────────────────────────────────────────────────────────

def load(path):
    if not os.path.exists(path):
        print(f"  Warning: {path} not found — skipping")
        return []
    with open(path) as f:
        return json.load(f)

print("Loading classified data...")
rnaseq   = load("rnaseq_classified.json")
chipseq  = load("chipseq_classified.json")
methyl   = load("methylation_classified.json")
multiom  = load("multiomics_classified.json")

if not rnaseq:
    sys.exit("rnaseq_classified.json is required. Run bootstrap.py first.")

print(f"  RNA-seq:    {len(rnaseq):,}")
print(f"  ChIP-seq:   {len(chipseq):,}")
print(f"  Methylation:{len(methyl):,}")
print(f"  Multiomics: {len(multiom):,}")


def parse_year(pub_date: str) -> int | None:
    """Extract year from pub_date string like '2022/03/15' or '2022-03-15'."""
    if not pub_date:
        return None
    try:
        return int(pub_date.replace("-", "/").split("/")[0])
    except (ValueError, IndexError):
        return None


# ── Plot 1: Assay family overview ─────────────────────────────────────────────

def plot_assay_overview():
    chip_only  = [r for r in chipseq if r["modality"] in ("chip_seq", "chip_exo")]
    atac_only  = [r for r in chipseq if r["modality"] == "atac_seq"]
    cut_only   = [r for r in chipseq if r["modality"] in ("cut_and_run", "cut_and_tag")]

    families = [
        ("RNA-seq",      len(rnaseq),    ASSAY_COLORS["RNA-seq"]),
        ("ChIP-seq",     len(chip_only), ASSAY_COLORS["ChIP-seq"]),
        ("ATAC-seq",     len(atac_only), ASSAY_COLORS["ATAC-seq"]),
        ("Methylation",  len(methyl),    ASSAY_COLORS["Methylation"]),
        ("CUT&RUN/Tag",  len(cut_only),  ASSAY_COLORS["CUT&RUN/Tag"]),
        ("Multiomics",   len(multiom),   ASSAY_COLORS["Multiomics"]),
    ]
    # Sort descending
    families.sort(key=lambda x: x[1], reverse=True)

    labels  = [f[0] for f in families]
    values  = [f[1] for f in families]
    colors  = [f[2] for f in families]

    fig, ax = plt.subplots(figsize=(FIG_W, 4))
    bars = ax.barh(labels[::-1], values[::-1], color=colors[::-1], height=0.6)

    # Value labels
    for bar, val in zip(bars, values[::-1]):
        ax.text(bar.get_width() + max(values) * 0.01, bar.get_y() + bar.get_height() / 2,
                f"{val:,}", va="center", ha="left", fontsize=10)

    ax.set_xlabel("Number of GEO datasets")
    ax.set_title("GEO Datasets by Assay Type", fontsize=13, fontweight="bold", pad=12)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_xlim(0, max(values) * 1.18)
    fig.tight_layout()
    path = f"{ASSETS}/plot_assay_overview.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Wrote {path}")


# ── Plot 2: RNA-seq modality breakdown ────────────────────────────────────────

def plot_rnaseq_modalities():
    counts = Counter(r["modality"] for r in rnaseq)
    order  = ["bulk", "single-cell", "single-nucleus", "spatial"]
    labels = [MODALITY_LABELS.get(m, m) for m in order]
    values = [counts.get(m, 0) for m in order]
    colors = [MODALITY_COLORS.get(m, "#999") for m in order]

    fig, ax = plt.subplots(figsize=(FIG_W, 3.2))
    bars = ax.barh(labels[::-1], values[::-1], color=colors[::-1], height=0.55)

    for bar, val in zip(bars, values[::-1]):
        pct = 100 * val / sum(values)
        ax.text(bar.get_width() + max(values) * 0.01, bar.get_y() + bar.get_height() / 2,
                f"{val:,}  ({pct:.0f}%)", va="center", ha="left", fontsize=10)

    ax.set_xlabel("Number of datasets")
    ax.set_title("RNA-seq Datasets by Modality", fontsize=13, fontweight="bold", pad=12)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_xlim(0, max(values) * 1.28)
    fig.tight_layout()
    path = f"{ASSETS}/plot_rnaseq_modalities.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Wrote {path}")


# ── Plot 3: Growth over time ──────────────────────────────────────────────────

def plot_growth_over_time():
    chip_only = [r for r in chipseq if r["modality"] in ("chip_seq", "chip_exo")]
    atac_only = [r for r in chipseq if r["modality"] == "atac_seq"]
    cut_only  = [r for r in chipseq if r["modality"] in ("cut_and_run", "cut_and_tag")]

    datasets = {
        "RNA-seq":     rnaseq,
        "ChIP-seq":    chip_only,
        "ATAC-seq":    atac_only,
        "Methylation": methyl,
        "CUT&RUN/Tag": cut_only,
        "Multiomics":  multiom,
    }

    # Count by year for each family
    year_counts: dict[str, Counter] = {}
    all_years: set[int] = set()
    for family, records in datasets.items():
        c = Counter()
        for r in records:
            y = parse_year(r.get("pub_date", ""))
            if y and 2015 <= y <= 2026:
                c[y] += 1
                all_years.add(y)
        year_counts[family] = c

    years = sorted(all_years)

    fig, ax = plt.subplots(figsize=(FIG_W, 4.5))

    for family, color in ASSAY_COLORS.items():
        counts = [year_counts[family].get(y, 0) for y in years]
        ax.plot(years, counts, marker="o", markersize=4, linewidth=2,
                color=color, label=family)

    ax.set_xlabel("Publication year")
    ax.set_ylabel("Datasets published")
    ax.set_title("GEO Dataset Growth Over Time", fontsize=13, fontweight="bold", pad=12)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_xticks(years)
    # Mark 2026 as partial year
    xlabels = [str(y) if y != 2026 else "2026*" for y in years]
    ax.set_xticklabels(xlabels, rotation=45, ha="right")
    ax.legend(loc="upper left", framealpha=0.85, fontsize=9)
    ax.grid(axis="y", alpha=0.4)
    ax.grid(axis="x", alpha=0)
    ax.text(0.99, 0.02, "* 2026 data through April only",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=8, color="gray", style="italic")
    fig.tight_layout()
    path = f"{ASSETS}/plot_growth_over_time.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Wrote {path}")


# ── Plot 4: Top organisms (RNA-seq) ──────────────────────────────────────────

def plot_top_organisms():
    # Exclude compound organism strings (multi-species studies)
    single = [r for r in rnaseq if ";" not in r.get("organism", "")]
    counts = Counter(r["organism"] for r in single)
    top = counts.most_common(15)

    labels = [t[0] for t in top]
    values = [t[1] for t in top]

    # Italicize species names (matplotlib uses mathtext for italics — use LaTeX-style)
    # Simple approach: just use regular text, it's cleaner in a bar chart
    fig, ax = plt.subplots(figsize=(FIG_W, 5.5))
    bars = ax.barh(labels[::-1], values[::-1], color=ASSAY_COLORS["RNA-seq"], height=0.65)

    for bar, val in zip(bars, values[::-1]):
        ax.text(bar.get_width() + max(values) * 0.005, bar.get_y() + bar.get_height() / 2,
                f"{val:,}", va="center", ha="left", fontsize=9)

    ax.set_xlabel("RNA-seq datasets")
    ax.set_title("Top 15 Organisms (RNA-seq)", fontsize=13, fontweight="bold", pad=12)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_xlim(0, max(values) * 1.15)
    ax.tick_params(axis="y", labelsize=10)
    fig.tight_layout()
    path = f"{ASSETS}/plot_top_organisms.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Wrote {path}")


# ── Plot 5: Research topics (RNA-seq) ────────────────────────────────────────

def plot_topics():
    topic_counts: Counter = Counter()
    for r in rnaseq:
        for t in r.get("topics", []):
            topic_counts[t] += 1

    # Pretty names
    TOPIC_LABELS = {
        "cancer": "Cancer", "development": "Development", "immunology": "Immunology",
        "neuroscience": "Neuroscience", "epigenetics": "Epigenetics",
        "gene_regulation": "Gene Regulation", "metabolism": "Metabolism",
        "infectious_disease": "Infectious Disease", "drug_response": "Drug Response",
        "cell_stress": "Cell Stress", "hematopoiesis": "Hematopoiesis",
        "cardiovascular": "Cardiovascular", "aging": "Aging",
        "rna_biology": "RNA Biology", "signal_transduction": "Signal Transduction",
        "gut_intestine": "Gut / Intestine", "lung_respiratory": "Lung / Respiratory",
        "crispr_gene_editing": "CRISPR / Gene Editing", "fibrosis_wound": "Fibrosis / Wound",
        "kidney": "Kidney", "cell_cycle": "Cell Cycle", "reproduction": "Reproduction",
        "liver": "Liver", "microbiology": "Microbiology", "skin": "Skin",
        "plant_biology": "Plant Biology", "skeletal_muscle": "Skeletal Muscle",
        "eye_vision": "Eye / Vision",
    }

    top = topic_counts.most_common(20)
    labels = [TOPIC_LABELS.get(t[0], t[0]) for t in top]
    values = [t[1] for t in top]

    fig, ax = plt.subplots(figsize=(FIG_W, 6.5))
    bars = ax.barh(labels[::-1], values[::-1], color=ASSAY_COLORS["RNA-seq"], height=0.65)

    for bar, val in zip(bars, values[::-1]):
        ax.text(bar.get_width() + max(values) * 0.005, bar.get_y() + bar.get_height() / 2,
                f"{val:,}", va="center", ha="left", fontsize=9)

    ax.set_xlabel("RNA-seq datasets tagged with topic")
    ax.set_title("Top Research Topics (RNA-seq)", fontsize=13, fontweight="bold", pad=12)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.set_xlim(0, max(values) * 1.18)
    ax.tick_params(axis="y", labelsize=10)
    fig.tight_layout()
    path = f"{ASSETS}/plot_topics.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Wrote {path}")


# ── Run all ───────────────────────────────────────────────────────────────────

print("\nGenerating plots...")
plot_assay_overview()
plot_rnaseq_modalities()
plot_growth_over_time()
plot_top_organisms()
plot_topics()
print("\nDone. PNGs saved to assets/")
