# MTX / 10x CellRanger Sparse Matrices

**Effort: ⭐⭐⭐ Medium | Time: half a day**

The standard output format from 10x Genomics CellRanger. Three files together make a complete count matrix: a sparse matrix file (`.mtx`), a cell barcode list (`barcodes.tsv`), and a gene list (`features.tsv` or `genes.tsv`). This is raw — no cell type labels, no clustering — so you'll run the standard QC and analysis pipeline yourself.

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

## Loading in R (Seurat)

```r
library(Seurat)

# Single sample — files in the same directory
counts <- Read10X(data.dir = "path/to/files/")
sobj <- CreateSeuratObject(counts = counts,
                           project = "GSE115931",
                           min.cells = 3,
                           min.features = 200)

# If files have non-standard names, specify them manually
counts <- ReadMtx(
  mtx      = "GSE115931_10XGenomics_Pancreas_E14-5_1.matrix.mtx.gz",
  features = "GSE115931_10XGenomics_Pancreas_E14-5_1.genes.tsv.gz",
  cells    = "GSE115931_10XGenomics_Pancreas_E14-5_1.barcodes.tsv.gz"
)
sobj <- CreateSeuratObject(counts = counts)

# Multiple samples — merge after loading each
s1 <- CreateSeuratObject(Read10X("sample1/"), project = "sample1")
s2 <- CreateSeuratObject(Read10X("sample2/"), project = "sample2")
merged <- merge(s1, y = s2, add.cell.ids = c("s1", "s2"))
```

## Standard QC and clustering pipeline (R)

```r
library(Seurat)

# QC metrics
sobj[["percent.mt"]] <- PercentageFeatureSet(sobj, pattern = "^MT-")  # human
# sobj[["percent.mt"]] <- PercentageFeatureSet(sobj, pattern = "^mt-")  # mouse

VlnPlot(sobj, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3)
FeatureScatter(sobj, feature1 = "nCount_RNA", feature2 = "nFeature_RNA")

# Filter — adjust thresholds based on your violin plots
sobj <- subset(sobj,
               subset = nFeature_RNA > 200 &
                        nFeature_RNA < 6000 &
                        percent.mt < 20)

# Normalize, find variable features, scale
sobj <- NormalizeData(sobj)
sobj <- FindVariableFeatures(sobj, nfeatures = 2000)
sobj <- ScaleData(sobj)

# Dimensionality reduction and clustering
sobj <- RunPCA(sobj)
ElbowPlot(sobj)  # choose number of PCs

sobj <- FindNeighbors(sobj, dims = 1:20)
sobj <- FindClusters(sobj, resolution = 0.5)
sobj <- RunUMAP(sobj, dims = 1:20)

DimPlot(sobj, label = TRUE)
```

## Loading in Python (scanpy)

```python
import scanpy as sc

# Standard CellRanger directory structure
adata = sc.read_10x_mtx(
    "path/to/files/",
    var_names="gene_symbols",   # or "gene_ids"
    cache=True
)

# Non-standard filenames — read manually
from scipy.io import mmread
from scipy.sparse import csr_matrix
import pandas as pd
import numpy as np

matrix = csr_matrix(mmread("GSE115931_matrix.mtx.gz").T)  # transpose: cells x genes
barcodes = pd.read_csv("GSE115931_barcodes.tsv.gz", header=None, sep="\t")[0]
features = pd.read_csv("GSE115931_genes.tsv.gz", header=None, sep="\t")

import anndata
adata = anndata.AnnData(X=matrix,
                        obs=pd.DataFrame(index=barcodes),
                        var=pd.DataFrame(index=features[1]))  # gene symbols in col 1
```

## Standard QC pipeline (Python)

```python
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

# Mitochondrial QC
adata.var["mt"] = adata.var_names.str.startswith("MT-")  # human; use "mt-" for mouse
sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], percent_top=None, log1p=False, inplace=True)

sc.pl.violin(adata, ["n_genes_by_counts", "total_counts", "pct_counts_mt"],
             jitter=0.4, multi_panel=True)

# Filter — adjust based on violin plots
adata = adata[adata.obs.n_genes_by_counts < 6000, :]
adata = adata[adata.obs.pct_counts_mt < 20, :]

# Normalize, log, HVG, PCA, neighbors, clustering
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

## Real GEO examples

### [GSE115931](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE115931) — Pancreatic development at single-cell resolution
- **Organism:** Mus musculus | **Samples:** 2,197 cells | **Topics:** development, signal_transduction
- **Files:** Multiple MTX trios (barcodes + genes + matrix) per timepoint, 16–47 MB each
- Well-organized naming convention; multiple developmental stages available as separate MTX sets

### [GSE124031](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE124031) — Cerebral organoids from neuronal migration disorder patients
- **Organism:** Homo sapiens | **Samples:** 807 cells | **Topics:** neuroscience, development
- **Files:** `GSE124031_GAC028_*_barcodes.tsv.gz` + `matrix.mtx.gz` per condition (8–13 MB each)
- Mix of MTX format and a dense CSV for comparison — illustrates common multi-format deposits

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
