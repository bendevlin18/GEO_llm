# H5AD / AnnData (scanpy)

**Effort: ⭐⭐ Easy–Medium | Total time: 2–4 hours**

AnnData HDF5 files (`.h5ad`) are the Python single-cell ecosystem's equivalent of Seurat's RDS objects. Loading one gives you the authors' processed data, cell type annotations, and dimensionality reductions immediately — no pipeline to rerun.

## Requirements

| | |
|---|---|
| **OS** | Mac, Windows, or Linux — all work equally well |
| **Compute** | Laptop or desktop — no cluster needed for exploration; re-clustering large datasets (100k+ cells) benefits from more cores |
| **RAM** | **Rule of thumb: 3–5× the compressed file size.** A 34 MB `.h5ad.gz` → ~100–170 MB in memory (trivial). A 500 MB `.h5ad.gz` → ~1.5–2.5 GB. H5AD supports memory-mapping for very large files (see pitfalls). |
| **Storage** | Keep compressed files on disk; Python holds the expanded object in memory |
| **Key packages** | `scanpy`, `anndata`, `matplotlib`, `seaborn`; optionally `scvi-tools` (deep learning), `diffxpy` or `pydeseq2` (DE) |

> **Windows note:** everything works on Windows via conda. Use [Miniforge](https://github.com/conda-forge/miniforge) or Anaconda. If you use WSL2, the Linux instructions apply directly.

---

## Steps

### Step 1 — Set up Python environment *(first time only, ~10 min)*

```bash
conda create -n scrna python=3.11 scanpy anndata matplotlib seaborn -y
conda activate scrna

# Optional: for DE analysis
pip install pydeseq2
```

> **Mac Apple Silicon (M1/M2/M3):** use Miniforge (arm64) for best compatibility. Most packages have native ARM builds and run faster than under Rosetta.

### Step 2 — Download the H5AD file *(~5–30 min depending on file size)*

```bash
wget "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE161nnn/GSE161228/suppl/GSE161228_adata_all_panPN_annotated_final.h5ad.gz"
```

> **Windows:** download via browser or use the GEO web interface.

### Step 3 — Decompress if needed *(~1–5 min)*

Newer versions of scanpy (1.9+) can read `.h5ad.gz` directly. Older versions cannot.

```bash
# If sc.read_h5ad() throws an error, decompress first:
gunzip GSE161228_adata_all_panPN_annotated_final.h5ad.gz
# This produces a plain .h5ad file (~3–5× larger)
```

### Step 4 — Load and inspect *(~1–10 min)*

```python
import scanpy as sc

adata = sc.read_h5ad("GSE161228_adata_all_panPN_annotated_final.h5ad")

# Overview
print(adata)
# AnnData object with n_obs × n_vars = 11509 × 15000
#     obs: 'cell_type', 'sample', 'leiden', 'n_genes', 'n_counts'
#     obsm: 'X_pca', 'X_umap'

# What metadata columns are available?
print(adata.obs.columns.tolist())
print(adata.obs["cell_type"].value_counts())

# Gene info
print(adata.var.head())
```

> **RAM check:** if Python raises a `MemoryError`, the dataset is too large for your machine. Options: (1) use memory-mapped loading — `sc.read_h5ad("file.h5ad", backed="r")` — which keeps data on disk and only loads slices; (2) subset to cells of interest before loading fully; (3) use a machine or cloud instance with more RAM.

### Step 5 — Visualize existing annotations *(~10–20 min)*

```python
sc.settings.figdir = "figures/"
sc.settings.set_figure_params(dpi=100, frameon=False)

# UMAP with authors' labels
sc.pl.umap(adata, color="cell_type", legend_loc="on data",
           title="Cell types", save="_celltypes.png")

# Gene expression
sc.pl.umap(adata, color=["Slc17a7", "Gad2", "Aqp4"], ncols=3,
           save="_markers.png")

# Dot plot
marker_genes = {"Excitatory": ["Slc17a7"], "Inhibitory": ["Gad2"]}
sc.pl.dotplot(adata, marker_genes, groupby="cell_type", save="_dotplot.png")
```

> **Time:** plotting on 10,000 cells takes ~10–30 seconds per figure. On 100,000+ cells, expect 1–3 minutes per figure.

### Step 6 — (Optional) Re-cluster a subset *(~20–60 min)*

```python
# Subset to cells of interest
mask = adata.obs["cell_type"].isin(["Neuron_A", "Neuron_B"])
sub = adata[mask].copy()

# Re-run pipeline on subset
sc.pp.highly_variable_genes(sub, n_top_genes=2000)
sc.pp.pca(sub)
sc.pp.neighbors(sub, n_pcs=20)
sc.tl.leiden(sub, resolution=0.5)
sc.tl.umap(sub)
sc.pl.umap(sub, color=["leiden", "cell_type"])
```

> **Time:** PCA + neighbors + UMAP on 5,000 cells: ~1–2 min on a laptop. On 50,000 cells: ~10–20 min. On 200,000+ cells, consider using a machine with 32+ cores or a cluster.

### Step 7 — (Optional) Differential expression *(~5–30 min)*

```python
# Quick DE with scanpy's Wilcoxon test
sc.tl.rank_genes_groups(adata, groupby="cell_type", method="wilcoxon")
de_results = sc.get.rank_genes_groups_df(adata, group="Neuron_A")
print(de_results.head(20))

# Export
de_results.to_csv("DE_Neuron_A_vs_rest.csv", index=False)
```

### Step 8 — (Optional) Convert to Seurat for R analysis *(~10–30 min)*

```r
library(SeuratDisk)
Convert("adata.h5ad", dest = "h5seurat", overwrite = TRUE)
sobj <- LoadH5Seurat("adata.h5seurat")

# Or with zellkonverter (Bioconductor)
library(zellkonverter)
sce <- readH5AD("adata.h5ad")
sobj <- as.Seurat(sce)
```

---

## Real GEO examples

### [GSE161228](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161228) — Drosophila olfactory projection neurons over time
- **Organism:** Drosophila melanogaster | **Cells:** 11,509 | **Topics:** neuroscience, development
- **Files:** `GSE161228_adata_all_panPN_annotated_final.h5ad.gz` (34 MB); multiple timepoint files also provided
- Fully annotated; multiple developmental stages as separate H5AD files

### [GSE162121](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162121) — Drosophila olfactory receptor neurons
- **Organism:** Drosophila melanogaster | **Cells:** 8,813 | **Topics:** neuroscience, development
- **Files:** `GSE162121_ORN.h5ad.gz` (23 MB)
- Single clean H5AD — ideal for learning the format

### [GSE154759](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE154759) — TF-driven iPSC programming to multiple fates
- **Organism:** Homo sapiens | **Samples:** 95 | **Topics:** development, gene_regulation
- **Files:** `GSE154759_adata.h5ad.gz` (3 MB) — very small, good for testing
- Raw matrix also provided as TSV

### [GSE163426](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE163426) — COVID-19 ARDS tracheal aspirate scRNA-seq
- **Organism:** Homo sapiens | **Samples:** 58 | **Topics:** immunology, infectious_disease, lung_respiratory
- **Files:** `GSE163426_Artik_AnnData_041221_Pos_LogNorm_QCFiltered.h5ad.gz` (514 MB) — needs ~2–2.5 GB RAM
- Filename specifies log-normalized, QC-filtered; raw counts also available as CSV

## Common pitfalls

- **`.h5ad.gz` decompression:** older scanpy versions can't read gzipped H5AD. If you get an error on `sc.read_h5ad()`, run `gunzip file.h5ad.gz` first.
- **`adata.X` is normalized:** by default `adata.X` contains normalized/log-transformed counts. Raw counts are in `adata.raw.X` if stored. Always check `adata.raw` before DE.
- **Sparse vs. dense:** `adata.X` is often a sparse matrix. Convert to numpy with `adata.X.toarray()` — but only for subsets; full matrices can be many GB.
- **Missing UMAP:** if `adata.obsm` is empty, re-run: `sc.pp.neighbors(adata)` then `sc.tl.umap(adata)`.
- **scanpy version mismatches:** H5AD files written by old scanpy versions may not load in new ones. Try `anndata.read_h5ad()` directly if `sc.read_h5ad()` fails.
- **Windows parallel processing:** scanpy's default parallelism works on Windows. If using `numba`-accelerated functions (e.g., UMAP), ensure you have a compatible C++ compiler or install pre-built wheels via conda.
