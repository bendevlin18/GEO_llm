# H5 / CellRanger HDF5

**Effort: ⭐⭐⭐ Medium | Total time: half a day**

HDF5 files (`.h5`) from 10x Genomics CellRanger are a single-file alternative to the MTX trio. They contain the same count matrix but packed into one binary file, which is faster to load and easier to transfer. Like MTX, this is raw data — no cell type labels — so you'll run QC and clustering yourself.

## Requirements

| | |
|---|---|
| **OS** | Mac or Windows — any works equally well for loading and analysis |
| **Compute** | Laptop or desktop — no cluster needed for <50,000 cells |
| **RAM** | **Rule of thumb: 5–10× the compressed H5 file size.** A 10 MB `.h5` → ~50–100 MB in memory (trivial). A 76 MB `.h5` → ~400–800 MB. A 1.8 GB `.h5` → 10–20 GB — needs a high-RAM machine or cluster. H5 files load as sparse matrices by default; only densify when strictly necessary. |
| **Storage** | H5 files are single files (no extraction needed); keep on local disk |
| **Key packages** | R: `Seurat`, `ggplot2`; Python: `scanpy`, `anndata`, `h5py` |

> **Windows note:** R and Seurat work on Windows without issues. Python via [Miniforge](https://github.com/conda-forge/miniforge) (conda) is the easiest path. `h5py` installs cleanly via conda. Use `plan("multisession")` instead of `plan("multicore")` if using the `future` package.

---

## What's inside

CellRanger produces two H5 files per sample:

| File | Contents |
|---|---|
| `filtered_feature_bc_matrix.h5` | Cells that passed CellRanger's cell calling (recommended starting point) |
| `raw_feature_bc_matrix.h5` | All barcodes including empty droplets (needs additional filtering) |

GEO deposits typically provide the filtered version. Filenames vary — authors often rename them with the GSE accession prefix.

```
# Typical GEO filenames
GSE117963_10X_plaque_14w_filtered_gene_bc_matrices_h5.h5
GSE154989_mmLungPlate_fQC_dSp_rawCount.h5
GSE102934_iCell_10x_brain.h5
```

---

## Steps (R — Seurat)

### Step 1 — Install Seurat *(first time only, ~10–20 min)*

```r
install.packages("Seurat")
```

> **Windows:** install [Rtools](https://cran.r-project.org/bin/windows/Rtools/) first if you get compilation errors.

### Step 2 — Download the H5 file from GEO *(~2–20 min depending on file size)*

```bash
wget "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE117nnn/GSE117963/suppl/GSE117963_10X_plaque_14w_filtered_gene_bc_matrices_h5.h5"
```

> **Windows:** use the GEO web interface or paste the URL directly into your browser.

### Step 3 — Load the H5 file *(~1–5 min)*

```r
library(Seurat)

# Single sample
counts <- Read10X_h5("GSE117963_10X_plaque_14w_filtered_gene_bc_matrices_h5.h5")
sobj <- CreateSeuratObject(counts = counts,
                           project = "GSE117963_plaque_14w",
                           min.cells = 3,
                           min.features = 200)

# Multiple samples — load each then merge
files <- list.files(pattern = "*.h5")
sobj_list <- lapply(files, function(f) {
  counts <- Read10X_h5(f)
  CreateSeuratObject(counts, project = tools::file_path_sans_ext(basename(f)),
                     min.cells = 3, min.features = 200)
})
merged <- Reduce(function(a, b) merge(a, b), sobj_list)
```

> **RAM check:** a 1.8 GB H5 file can expand to 10–20 GB in memory as a dense matrix. Load into sparse format (default) and only densify subsets.

### Step 4 — QC and filter *(~10–20 min)*

```r
# QC metrics
sobj[["percent.mt"]] <- PercentageFeatureSet(sobj, pattern = "^MT-")  # human
# sobj[["percent.mt"]] <- PercentageFeatureSet(sobj, pattern = "^mt-")  # mouse

VlnPlot(sobj, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3)

# Filter — adjust thresholds based on your violin plots
sobj <- subset(sobj,
               subset = nFeature_RNA > 200 &
                        nFeature_RNA < 6000 &
                        percent.mt < 20)
```

### Step 5 — Normalize and cluster *(~10–30 min for <50k cells; ~30–90 min for 50k–200k)*

```r
# Normalize → variable features → scale → PCA → neighbors → cluster → UMAP
sobj <- NormalizeData(sobj) |>
        FindVariableFeatures(nfeatures = 2000) |>
        ScaleData() |>
        RunPCA() |>
        FindNeighbors(dims = 1:20) |>
        FindClusters(resolution = 0.5) |>
        RunUMAP(dims = 1:20)

DimPlot(sobj, label = TRUE)

# Find marker genes per cluster (~5–20 min)
markers <- FindAllMarkers(sobj, only.pos = TRUE,
                          min.pct = 0.25, logfc.threshold = 0.25)
```

> **Time:** PCA + neighbors + UMAP on 5,000 cells: ~2–5 min on a laptop. On 50,000 cells: ~15–30 min. On 200,000+ cells, consider a cluster node with 64 GB RAM.

---

## Steps (Python — scanpy)

### Step 1 — Set up environment *(first time only, ~10 min)*

```bash
conda create -n scrna python=3.11 scanpy anndata h5py matplotlib seaborn -y
conda activate scrna
```

### Step 2 — Download and load *(~2–20 min)*

```python
import scanpy as sc

# Single sample
adata = sc.read_10x_h5("GSE117963_10X_plaque_14w_filtered_gene_bc_matrices_h5.h5")
adata.var_names_make_unique()

# Multiple samples — concatenate
import anndata
samples = {
    "plaque_14w": sc.read_10x_h5("GSE117963_10X_plaque_14w_filtered_gene_bc_matrices_h5.h5"),
    "plaque_18w": sc.read_10x_h5("GSE117963_10X_plaque_18w_filtered_gene_bc_matrices_h5.h5"),
}
for name, s in samples.items():
    s.obs["sample"] = name
    s.var_names_make_unique()

adata = anndata.concat(samples.values(), label="sample",
                       keys=samples.keys(), join="outer")
```

### Step 3 — QC and cluster *(~20–60 min)*

```python
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

adata.var["mt"] = adata.var_names.str.startswith("MT-")   # human; "mt-" for mouse
sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], inplace=True)

sc.pl.violin(adata, ["n_genes_by_counts", "total_counts", "pct_counts_mt"],
             jitter=0.4, multi_panel=True)

adata = adata[adata.obs.pct_counts_mt < 20, :]
adata = adata[adata.obs.n_genes_by_counts < 6000, :]

sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
adata.raw = adata
adata = adata[:, adata.var.highly_variable]
sc.pp.pca(adata)
sc.pp.neighbors(adata, n_pcs=20)
sc.tl.leiden(adata)
sc.tl.umap(adata)
sc.pl.umap(adata, color="leiden")
```

---

## Reading with h5py directly (when standard loaders fail)

Occasionally GEO H5 files use a non-CellRanger internal structure. Inspect with h5py:

```python
import h5py

with h5py.File("GSE154989_mmLungPlate_fQC_dSp_rawCount.h5", "r") as f:
    def print_tree(name, obj):
        print(name)
    f.visititems(print_tree)
```

This prints the internal key structure so you can figure out where the matrix, barcodes, and genes are stored.

---

## Real GEO examples

### [GSE117963](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE117963) — Smooth muscle cell transcriptomes in atherosclerotic plaques
- **Organism:** Mus musculus | **Samples:** 317 cells | **Topics:** cardiovascular, development
- **Files:** 4 separate H5 files (10–13 MB each) — one per tissue/timepoint; bulk RNA-seq also provided
- Good example of a multi-sample H5 deposit; manageable file sizes for getting started

### [GSE154989](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE154989) — High-plasticity cell states during lung cancer evolution
- **Organism:** Mus musculus | **Samples:** 7,282 cells | **Topics:** cancer, lung_respiratory
- **Files:** `GSE154989_mmLungPlate_fQC_dSp_rawCount.h5` (76 MB), `normTPM.h5` (191 MB)
- Two H5 files: raw counts and normalized TPM — use raw counts for DE; TPM for visualization

### [GSE102934](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102934) — bigSCale: framework for large-scale scRNA-seq
- **Organism:** Homo sapiens | **Samples:** 1,847 cells | **Topics:** neuroscience, development
- **Files:** `GSE102934_iCell_10x_brain.h5` (1.8 GB)
- Very large H5 file — a good stress test for your loading pipeline; ensure sufficient RAM (16–32 GB)

### [GSE150551](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150551) — Epigenetic bistability in neuron-specific genes
- **Organism:** Mus musculus | **Samples:** 39 | **Topics:** neuroscience, cancer
- **Files:** `GSE150551_filtered_feature_bc_matrix.h5` (6 MB) — standard CellRanger filename
- Small, cleanly named file — ideal for testing your H5 loading code

## Common pitfalls

- **`raw` vs. `filtered`:** if the filename contains "raw" it contains all barcodes, most of which are empty droplets. Use `filtered` if available; if only `raw` is provided, filter barcodes with `sc.external.pp.scrublet()` or Seurat's emptydrops-based approach.
- **Non-CellRanger H5 files:** some labs produce custom HDF5 files with non-standard structure (see the h5py inspection recipe above). Common alternative structures have keys like `/counts`, `/matrix/data`, or simply store a dense array.
- **Feature types:** CellRanger H5 files from Multiome or CITE-seq experiments contain multiple feature types (`Gene Expression`, `Antibody Capture`, `Peaks`). Seurat's `Read10X_h5()` returns a list; access RNA with `counts$`Gene Expression``. In scanpy use the `gex_only` parameter.
- **File size vs. RAM:** a 1.8 GB H5 file expands to 10–20 GB in memory as a dense matrix. Load into a sparse format (CellRanger H5 files are sparse by default) and only densify when necessary.
- **Windows file paths:** use forward slashes or raw strings in Python (`r"C:\path\to\file.h5"`) to avoid path escape issues.
