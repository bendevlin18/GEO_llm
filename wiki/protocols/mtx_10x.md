# MTX / 10x CellRanger Sparse Matrices

**Effort: ⭐⭐⭐ Medium | Total time: half a day to 1 day**

The standard output format from 10x Genomics CellRanger. Three files together make a complete count matrix: a sparse matrix file (`.mtx`), a cell barcode list (`barcodes.tsv`), and a gene list (`features.tsv` or `genes.tsv`). This is raw data — no cell type labels, no clustering — so you'll run the standard QC and analysis pipeline yourself.

## Requirements

| | |
|---|---|
| **OS** | Mac or Windows for data loading and analysis; Linux strongly recommended if you need to re-align from FASTQ |
| **Compute** | Laptop or desktop for QC and clustering; no cluster needed for <50,000 cells |
| **RAM** | **Rule of thumb: 5–10× the compressed MTX file size in memory.** A 50 MB `matrix.mtx.gz` → ~250–500 MB in memory. A 400 MB MTX → ~2–4 GB. MTX is sparse — final Seurat/AnnData object is typically 2–5× the matrix alone. |
| **Storage** | Keep compressed trios on disk; decompress into R/Python in memory only |
| **Key packages** | R: `Seurat`, `ggplot2`; Python: `scanpy`, `anndata`, `scipy` |

> **Windows note:** R and Python both work well on Windows. Install R + RStudio from [posit.co](https://posit.co/) and Python via [Miniforge](https://github.com/conda-forge/miniforge). Parallelism in Seurat works with `plan("multisession")`; replace `plan("multicore")` if you see an error.

---

## The three files

| File | Contents |
|---|---|
| `matrix.mtx.gz` | Sparse count matrix in Matrix Market format |
| `barcodes.tsv.gz` | One cell barcode per line |
| `features.tsv.gz` (or `genes.tsv.gz`) | Gene IDs and symbols, one per line |

GEO deposits often have these as individual files prefixed with the GSE accession, or bundled inside a `RAW.tar`. If there are multiple samples, each sample gets its own trio.

## Identifying the files

```
# Single sample — direct files
GSE115931_10XGenomics_Pancreas_E14-5_1.barcodes.tsv.gz
GSE115931_10XGenomics_Pancreas_E14-5_1.genes.tsv.gz
GSE115931_10XGenomics_Pancreas_E14-5_1.matrix.mtx.gz

# Multi-sample — one directory per sample inside RAW.tar
sample1/
  barcodes.tsv.gz
  features.tsv.gz
  matrix.mtx.gz
sample2/
  barcodes.tsv.gz
  ...
```

---

## Steps (R — Seurat)

### Step 1 — Install Seurat *(first time only, ~10–20 min)*

```r
install.packages("Seurat")

# Optional but recommended
install.packages("harmony")     # batch correction for multi-sample datasets
```

> **Windows:** if you get compilation errors, install [Rtools](https://cran.r-project.org/bin/windows/Rtools/) first, then retry.

### Step 2 — Download the MTX files from GEO *(~5–30 min)*

Download individual files from the GEO supplementary files section, or download `RAW.tar` if all samples are bundled.

```bash
# Individual files
wget "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE115nnn/GSE115931/suppl/GSE115931_10XGenomics_Pancreas_E14-5_1.matrix.mtx.gz"
wget "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE115nnn/GSE115931/suppl/GSE115931_10XGenomics_Pancreas_E14-5_1.genes.tsv.gz"
wget "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE115nnn/GSE115931/suppl/GSE115931_10XGenomics_Pancreas_E14-5_1.barcodes.tsv.gz"

# Or download the whole bundle
wget "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE115nnn/GSE115931/suppl/GSE115931_RAW.tar"
tar -xf GSE115931_RAW.tar
```

> **Windows:** download via browser or use the GEO web interface.

### Step 3 — Load the count matrix *(~2–10 min)*

```r
library(Seurat)

# Standard CellRanger directory — three files in the same folder
counts <- Read10X(data.dir = "path/to/files/")
sobj <- CreateSeuratObject(counts = counts,
                           project = "GSE115931",
                           min.cells = 3,
                           min.features = 200)

# Non-standard filenames — specify each file explicitly
counts <- ReadMtx(
  mtx      = "GSE115931_10XGenomics_Pancreas_E14-5_1.matrix.mtx.gz",
  features = "GSE115931_10XGenomics_Pancreas_E14-5_1.genes.tsv.gz",
  cells    = "GSE115931_10XGenomics_Pancreas_E14-5_1.barcodes.tsv.gz"
)
sobj <- CreateSeuratObject(counts = counts)

# Multiple samples — load each then merge
s1 <- CreateSeuratObject(Read10X("sample1/"), project = "sample1")
s2 <- CreateSeuratObject(Read10X("sample2/"), project = "sample2")
merged <- merge(s1, y = s2, add.cell.ids = c("s1", "s2"))
```

> **RAM check:** if R throws an "out of memory" error, you need more RAM. On 8 GB machines, datasets >20,000 cells may hit limits during clustering.

### Step 4 — QC and filter *(~10–20 min)*

```r
# Compute QC metrics
sobj[["percent.mt"]] <- PercentageFeatureSet(sobj, pattern = "^MT-")  # human
# sobj[["percent.mt"]] <- PercentageFeatureSet(sobj, pattern = "^mt-")  # mouse

# Visualize to choose thresholds
VlnPlot(sobj, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3)
FeatureScatter(sobj, feature1 = "nCount_RNA", feature2 = "nFeature_RNA")

# Filter — adjust thresholds based on your violin plots
sobj <- subset(sobj,
               subset = nFeature_RNA > 200 &
                        nFeature_RNA < 6000 &
                        percent.mt < 20)
```

> These thresholds are starting points. Adjust `nFeature_RNA` upper cutoff based on your cell types — neurons express 5,000–8,000 genes; blood cells often <3,000.

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

ElbowPlot(sobj)  # check the PCA elbow to validate your choice of dims
DimPlot(sobj, label = TRUE)
```

> **Time:** PCA + neighbors + UMAP on 5,000 cells: ~2–5 min on a laptop. On 50,000 cells: ~15–30 min. On 200,000+ cells, consider a cluster node with 32+ cores or 64 GB RAM.

### Step 6 — (Optional) Find marker genes *(~5–20 min)*

```r
markers <- FindAllMarkers(sobj, only.pos = TRUE,
                          min.pct = 0.25, logfc.threshold = 0.25)
top_markers <- markers |>
  dplyr::group_by(cluster) |>
  dplyr::slice_max(avg_log2FC, n = 5)

# Dot plot of top markers
DotPlot(sobj, features = unique(top_markers$gene)) + RotatedAxis()
```

---

## Steps (Python — scanpy)

### Step 1 — Set up environment *(first time only, ~10 min)*

```bash
conda create -n scrna python=3.11 scanpy anndata scipy matplotlib seaborn -y
conda activate scrna
```

### Step 2 — Download files *(~5–30 min)*

Same as the R Step 2 above.

### Step 3 — Load the count matrix *(~2–10 min)*

```python
import scanpy as sc

# Standard CellRanger directory structure
adata = sc.read_10x_mtx(
    "path/to/files/",
    var_names="gene_symbols",   # or "gene_ids" to avoid duplicate-symbol issues
    cache=True
)

# Non-standard filenames — read manually
from scipy.io import mmread
from scipy.sparse import csr_matrix
import pandas as pd
import anndata

matrix = csr_matrix(mmread("GSE115931_matrix.mtx.gz").T)  # transpose: cells × genes
barcodes = pd.read_csv("GSE115931_barcodes.tsv.gz", header=None, sep="\t")[0]
features = pd.read_csv("GSE115931_genes.tsv.gz", header=None, sep="\t")

adata = anndata.AnnData(X=matrix,
                        obs=pd.DataFrame(index=barcodes),
                        var=pd.DataFrame(index=features[1]))  # gene symbols in col 1
```

### Step 4 — QC and filter *(~10–20 min)*

```python
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

adata.var["mt"] = adata.var_names.str.startswith("MT-")  # human; use "mt-" for mouse
sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], percent_top=None, log1p=False, inplace=True)

sc.pl.violin(adata, ["n_genes_by_counts", "total_counts", "pct_counts_mt"],
             jitter=0.4, multi_panel=True)

adata = adata[adata.obs.n_genes_by_counts < 6000, :]
adata = adata[adata.obs.pct_counts_mt < 20, :]
```

### Step 5 — Normalize and cluster *(~10–30 min for <50k cells)*

```python
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
adata.raw = adata          # save raw before subsetting to HVGs
adata = adata[:, adata.var.highly_variable]
sc.pp.pca(adata, n_comps=50)
sc.pp.neighbors(adata, n_pcs=20)
sc.tl.leiden(adata)
sc.tl.umap(adata)
sc.pl.umap(adata, color="leiden")
```

---

## Real GEO examples

### [GSE115931](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE115931) — Pancreatic development at single-cell resolution
- **Organism:** Mus musculus | **Samples:** 2,197 cells | **Topics:** development, signal_transduction
- **Files:** Multiple MTX trios (barcodes + genes + matrix) per timepoint, 16–47 MB each
- Well-organized naming convention; multiple developmental stages available as separate MTX sets

### [GSE124031](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE124031) — Cerebral organoids from neuronal migration disorder patients
- **Organism:** Homo sapiens | **Samples:** 807 cells | **Topics:** neuroscience, development
- **Files:** `GSE124031_GAC028_*_barcodes.tsv.gz` + `matrix.mtx.gz` per condition (8–13 MB each)
- Mix of MTX format and a dense CSV — illustrates common multi-format deposits

### [GSE103354](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103354) — CFTR-expressing ionocytes in the airway epithelium
- **Organism:** Mus musculus | **Samples:** 325 cells | **Topics:** development, lung_respiratory
- **Files:** `GSE103354_PulseSeq_UMI_counts.mtx.gz` (403 MB), RDS also available
- Large MTX for its cell count (dense expression); RDS file also provided if you prefer Seurat directly

## Common pitfalls

- **Transposed matrix:** some authors deposit the matrix as genes × cells instead of the standard cells × genes. If `adata.X.shape` looks wrong (more columns than rows when expecting more genes than cells), transpose: `adata = adata.T` or use `mmread(...).T`.
- **`genes.tsv` vs `features.tsv`:** CellRanger 3+ uses `features.tsv` (3 columns: ID, symbol, type); older versions use `genes.tsv` (2 columns). Seurat's `Read10X()` handles both; in Python check the column count.
- **Multiple samples in `RAW.tar`:** extract the tar and load each sample directory separately, then merge/concatenate.
- **Ambient RNA:** MTX files from CellRanger contain all detected barcodes, not just real cells. If the deposit is unfiltered (filename contains "raw" not "filtered"), you'll need to filter barcodes with tools like EmptyDrops or SoupX before proceeding.
- **Gene symbol duplicates:** some genomes have duplicate gene symbols. `Read10X()` handles this with `make.unique()`; scanpy will error — set `var_names="gene_ids"` and map symbols separately.
- **Windows RAM:** on Windows, R's memory.limit() defaults can cap available RAM in some configurations. If you hit limits, run `memory.limit(size = 32000)` (for 32 GB machines) before loading large matrices.
