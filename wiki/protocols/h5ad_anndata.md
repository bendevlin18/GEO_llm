# H5AD / AnnData (scanpy)

**Effort: ⭐⭐ Easy–Medium | Time: a few hours**

AnnData HDF5 files (`.h5ad`) are the Python single-cell ecosystem's equivalent of Seurat's RDS objects. Loading one gives you the authors' processed data, cell type annotations, and dimensionality reductions immediately, without re-running the pipeline.

## What's inside

An AnnData object has a well-defined structure:

| Attribute | Contents |
|---|---|
| `adata.X` | Normalized expression matrix (cells × genes) |
| `adata.raw` | Raw counts before normalization (if stored) |
| `adata.obs` | Cell metadata — **cell type labels, clusters, sample IDs live here** |
| `adata.var` | Gene metadata — gene symbols, highly variable gene flags |
| `adata.obsm` | Dimensionality reductions — `X_pca`, `X_umap`, `X_tsne` |
| `adata.obsp` | Neighbor graphs (connectivity, distances) |
| `adata.uns` | Unstructured metadata — color palettes, DE results, etc. |

## Loading and inspecting

```python
import scanpy as sc
import pandas as pd

# Load (handles .gz automatically in newer versions; otherwise decompress first)
adata = sc.read_h5ad("GSE161228_adata_all_panPN_annotated_final.h5ad.gz")

# Overview
print(adata)
# AnnData object with n_obs × n_vars = 11509 × 15000
#     obs: 'cell_type', 'sample', 'leiden', 'n_genes', 'n_counts'
#     var: 'gene_ids', 'highly_variable'
#     obsm: 'X_pca', 'X_umap'

# Cell metadata
print(adata.obs.columns.tolist())
print(adata.obs["cell_type"].value_counts())

# Gene metadata
print(adata.var.head())

# Expression matrix shape: cells × genes
print(adata.X.shape)
```

## Visualizing existing annotations

```python
sc.settings.figdir = "figures/"
sc.settings.set_figure_params(dpi=100, frameon=False)

# UMAP with authors' cell type labels
sc.pl.umap(adata, color="cell_type", legend_loc="on data",
           title="Cell types", save="_celltypes.png")

# Gene expression on UMAP
sc.pl.umap(adata, color=["Slc17a7", "Gad2", "Aqp4"],
           ncols=3, save="_markers.png")

# Dot plot of marker genes by cell type
marker_genes = {"Excitatory": ["Slc17a7", "Camk2a"],
                "Inhibitory": ["Gad2", "Pvalb"],
                "Astrocyte":  ["Aqp4", "Aldh1l1"]}
sc.pl.dotplot(adata, marker_genes, groupby="cell_type",
              save="_dotplot.png")
```

## Re-clustering a subset

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

## Differential expression

```python
# scanpy's built-in rank_genes_groups (Wilcoxon)
sc.tl.rank_genes_groups(adata, groupby="cell_type", method="wilcoxon")
sc.pl.rank_genes_groups(adata, n_genes=20, save="_degs.png")

# Export results to DataFrame
de_results = sc.get.rank_genes_groups_df(adata, group="Neuron_A")
print(de_results.head(20))

# For more rigorous DE, export to pseudo-bulk and use pydeseq2
import numpy as np
from scipy.sparse import issparse

def pseudobulk(adata, group_col, sample_col):
    groups = adata.obs[group_col].unique()
    results = {}
    for g in groups:
        sub = adata[adata.obs[group_col] == g]
        X = sub.X.toarray() if issparse(sub.X) else sub.X
        results[g] = pd.Series(X.sum(axis=0), index=adata.var_names)
    return pd.DataFrame(results).T   # groups × genes

pb = pseudobulk(adata, "cell_type", "sample")
```

## Converting to Seurat (R)

If you need to work in R but the dataset is only available as H5AD:

```r
# Option 1: Convert with SeuratDisk
library(SeuratDisk)
Convert("adata.h5ad", dest = "h5seurat", overwrite = TRUE)
sobj <- LoadH5Seurat("adata.h5seurat")

# Option 2: Read the H5AD directly with zellkonverter (Bioconductor)
library(zellkonverter)
sce <- readH5AD("adata.h5ad")
sobj <- as.Seurat(sce)
```

## Real GEO examples

### [GSE161228](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161228) — Drosophila olfactory projection neurons over time
- **Organism:** Drosophila melanogaster | **Samples:** 11,509 cells | **Topics:** neuroscience, development
- **Files:** `GSE161228_adata_all_panPN_annotated_final.h5ad.gz` (34 MB), multiple timepoint h5ad files
- Fully annotated with neuron subtype labels; multiple developmental time points as separate files

### [GSE162121](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162121) — Drosophila olfactory receptor neurons
- **Organism:** Drosophila melanogaster | **Samples:** 8,813 cells | **Topics:** neuroscience, development
- **Files:** `GSE162121_ORN.h5ad.gz` (23 MB)
- Single clean H5AD — ideal for learning the format; well-annotated ORN subtypes

### [GSE154759](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE154759) — TF-driven iPSC programming to multiple fates
- **Organism:** Homo sapiens | **Samples:** 95 samples | **Topics:** development, gene_regulation
- **Files:** `GSE154759_adata.h5ad.gz` (3 MB), raw matrix TSV also provided
- Small file size — good for testing a new workflow; raw counts available alongside

### [GSE163426](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE163426) — COVID-19 ARDS tracheal aspirate scRNA-seq
- **Organism:** Homo sapiens | **Samples:** 58 samples | **Topics:** immunology, infectious_disease, lung_respiratory
- **Files:** `GSE163426_Artik_AnnData_041221_Pos_LogNorm_QCFiltered.h5ad.gz` (514 MB)
- Large object — note the filename specifies log-normalized, QC-filtered; raw counts also in CSV

## Common pitfalls

- **`.h5ad.gz` decompression:** older versions of scanpy can't read gzipped H5AD directly. If you get an error, decompress first: `gunzip file.h5ad.gz`, then `sc.read_h5ad("file.h5ad")`.
- **`adata.X` is normalized:** by default `adata.X` contains normalized/log-transformed counts. Raw counts are usually in `adata.raw.X` if the author stored them. Always check `adata.raw` before running DE.
- **Sparse vs. dense matrix:** `adata.X` is often a sparse matrix (`scipy.sparse.csr_matrix`). To convert to numpy: `X = adata.X.toarray()` — but only do this for subsets; full matrices can be many GB.
- **scanpy version:** H5AD files written by scanpy 0.x may not load cleanly in scanpy 1.x. Try `anndata.read_h5ad()` directly if `sc.read_h5ad()` fails.
- **Missing obsm:** some deposits don't include the UMAP embedding. If `adata.obsm` is empty, re-run `sc.pp.neighbors()` + `sc.tl.umap()`.
