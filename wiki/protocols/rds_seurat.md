# RDS / Seurat Objects

**Effort: ⭐⭐ Easy–Medium | Time: a few hours**

R serialized objects (`.rds`, `.RData`, `.rda`) containing a fully-processed single-cell analysis. The most convenient format to work with in R — loading a Seurat object gives you immediate access to the authors' cell type annotations, dimensionality reductions, and clustering, without needing to rerun the pipeline.

## What you'll find

A `.rds` file from a scRNA-seq paper is usually one of:

- **Seurat object** — the most common; contains raw counts, normalized data, PCA/UMAP embeddings, and cluster/cell-type labels in `@meta.data`
- **SingleCellExperiment (SCE)** — Bioconductor equivalent; used by scran, scater workflows
- **DESeqDataSet / DESeqResults** — bulk RNA-seq, contains model fits and DE results
- **ExpressionSet** — legacy Bioconductor format, mostly pre-2018 datasets

The GEO title and summary usually say which. If not, `readRDS()` and `class()` will tell you immediately.

## Loading a Seurat object

```r
library(Seurat)

sobj <- readRDS("GSE139412_striatum_final.rds.gz")  # gzip is handled automatically

# What's in it?
class(sobj)      # "Seurat"
dim(sobj)        # genes x cells
Assays(sobj)     # e.g. "RNA", "SCT", "ATAC"
Reductions(sobj) # e.g. "pca", "umap", "harmony"

# Cell metadata — this is where cell type labels live
head(sobj@meta.data)
table(sobj@meta.data$seurat_clusters)
table(sobj@meta.data$cell_type)   # column name varies by author

# Authors' UMAP with cell type labels
DimPlot(sobj, group.by = "cell_type", label = TRUE) + NoLegend()
```

## Exploring existing annotations

```r
# What metadata columns exist?
colnames(sobj@meta.data)

# Distribution of cell types across samples/conditions
table(sobj$cell_type, sobj$orig.ident)

# Gene expression on the UMAP
FeaturePlot(sobj, features = c("Pdgfra", "Rbfox3", "Gad2"))

# Violin plot by cell type
VlnPlot(sobj, features = "nFeature_RNA", group.by = "cell_type")

# Marker genes for each cluster (if not pre-computed)
markers <- FindAllMarkers(sobj, only.pos = TRUE, min.pct = 0.25,
                          logfc.threshold = 0.5)
top_markers <- markers |> dplyr::group_by(cluster) |>
               dplyr::slice_max(avg_log2FC, n = 5)
```

## Re-analyzing a subset

```r
# Subset to a cell type of interest
neurons <- subset(sobj, subset = cell_type == "Neuron")

# Re-run clustering on the subset
neurons <- RunPCA(neurons)
neurons <- FindNeighbors(neurons, dims = 1:20)
neurons <- FindClusters(neurons, resolution = 0.5)
neurons <- RunUMAP(neurons, dims = 1:20)
DimPlot(neurons, label = TRUE)
```

## Pseudo-bulk differential expression

```r
library(DESeq2)

# Aggregate counts per sample x cell type
pseudo_bulk <- AggregateExpression(sobj,
                                   group.by = c("cell_type", "orig.ident"),
                                   assays = "RNA", slot = "counts",
                                   return.seurat = FALSE)$RNA

# Build DESeq2 object and run DE (adjust coldata to your experiment)
# ...
```

## Loading a SingleCellExperiment object

```r
library(SingleCellExperiment)

sce <- readRDS("GSExxxxxx_sce.rds.gz")
class(sce)           # "SingleCellExperiment"
dim(sce)             # genes x cells
colData(sce)         # cell metadata (equivalent to Seurat @meta.data)
reducedDimNames(sce) # "PCA", "UMAP", etc.

# Convert to Seurat if you prefer that ecosystem
sobj <- as.Seurat(sce)
```

## Real GEO examples

### [GSE139412](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE139412) — Neuron types of the adult mouse striatum
- **Organism:** Mus musculus | **Samples:** 1,207 cells | **Topics:** neuroscience
- **Files:** `GSE139412_striatum_final.rds.gz` (33 MB), raw counts CSV also provided
- Well-annotated Seurat object with published cell type labels — ideal for exploring existing annotations or subsetting specific neuron populations

### [GSE111976](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE111976) — Human endometrium across the menstrual cycle
- **Organism:** Homo sapiens | **Samples:** 2,158 cells | **Topics:** development, reproduction
- **Files:** `GSE111976_ct_endo_10x.rds.gz` (408 MB), `GSE111976_ct.csv.gz` (12 MB)
- Large Seurat object with temporal cell state annotations; raw counts also available as CSV

### [GSE118723](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE118723) — Variance QTLs in human iPSCs
- **Organism:** Homo sapiens | **Samples:** 7,584 cells | **Topics:** development, genetics
- **Files:** `GSE118723_eset.rds.gz` (80 MB) — note: ExpressionSet format, not Seurat
- Load with `readRDS()` then `class()` to confirm format before assuming Seurat

### [GSE121265](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE121265) — Continuous cell-cycle phase from scRNA-seq
- **Organism:** Homo sapiens | **Samples:** 1,536 cells | **Topics:** cell cycle
- **Files:** `GSE121265_eset-final.rds.gz` (7 MB), `GSE121265_eset-raw.rds.gz` (15 MB)
- Two objects: raw and processed — good for understanding the full pipeline

## Common pitfalls

- **Seurat version mismatches:** objects saved with Seurat v4 may need updating for v5: `sobj <- UpdateSeuratObject(sobj)`. Objects from Seurat v2 may require more work.
- **Large file size:** a 400 MB `.rds.gz` expands to several GB in memory. Make sure you have at least 3–4× the compressed file size as free RAM before loading.
- **Normalized vs. raw counts:** Seurat objects typically store both. Raw counts are in `GetAssayData(sobj, slot = "counts")`, normalized in `slot = "data"`. Use raw counts for DE analysis.
- **Column name variation:** authors use different names for cell type labels — `cell_type`, `CellType`, `ident`, `cluster_label`, `annotation`. Always inspect `colnames(sobj@meta.data)` first.
- **RData vs. RDS:** `.RData` files may contain multiple objects. Load with `load("file.RData")` (not `readRDS`) and then `ls()` to see what was loaded.
