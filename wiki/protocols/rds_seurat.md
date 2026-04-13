# RDS / Seurat Objects

**Effort: ⭐⭐ Easy–Medium | Total time: 2–4 hours**

R serialized objects (`.rds`, `.RData`, `.rda`) containing a fully-processed single-cell analysis. Loading a Seurat object gives you the authors' cell type annotations, dimensionality reductions, and clustering immediately — no pipeline to rerun.

## Requirements

| | |
|---|---|
| **OS** | Mac or Windows laptop is fine — no cluster needed |
| **Compute** | Laptop or desktop; a modern machine with a good CPU helps for re-clustering |
| **RAM** | **Rule of thumb: 3–4× the compressed file size.** A 33 MB `.rds.gz` → ~100–130 MB in memory (fine). A 400 MB `.rds.gz` → 1.2–1.6 GB (still fine on 16 GB). A 2 GB `.rds.gz` → 6–8 GB — needs 16–32 GB RAM. |
| **Storage** | Keep compressed files on disk; R holds the expanded object in memory only |
| **Key packages** | `Seurat`, `ggplot2`, `dplyr`; optionally `harmony` (batch correction), `DESeq2` (pseudo-bulk DE) |

> **Windows note:** R and Seurat work well on Windows. Install R from [cran.r-project.org](https://cran.r-project.org/) and RStudio from [posit.co](https://posit.co/). The only limitation is that some parallel processing options (e.g., `future` with `multicore`) don't work on Windows — use `multisession` instead.

---

## Steps

### Step 1 — Install Seurat *(first time only, ~10–20 min)*

```r
install.packages("Seurat")      # Seurat v5 from CRAN

# Optional but recommended
install.packages("harmony")     # batch correction
BiocManager::install("DESeq2")  # pseudo-bulk DE
```

> Seurat v5 installation on Mac with Apple Silicon (M1/M2/M3) is straightforward via CRAN. On Windows, some dependencies require [Rtools](https://cran.r-project.org/bin/windows/Rtools/) — install it first if you get compilation errors.

### Step 2 — Download the RDS file from GEO *(~5–30 min depending on file size)*

Download from the GEO supplementary files section. Files range from a few MB to several hundred MB — check the size in the search index `files` column before downloading.

```bash
wget "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE139nnn/GSE139412/suppl/GSE139412_striatum_final.rds.gz"
```

> **Windows:** download via browser or use the GEO web interface.

### Step 3 — Load and identify the object type *(~1–10 min)*

```r
library(Seurat)

sobj <- readRDS("GSE139412_striatum_final.rds.gz")  # gzip handled automatically

# Always check class first — not all RDS files are Seurat objects
class(sobj)      # "Seurat", "SingleCellExperiment", "ExpressionSet", etc.
dim(sobj)        # genes × cells (if Seurat)
```

> **RAM check:** if R throws an "out of memory" error here, you need more RAM or a machine with more memory. On a shared cluster, request a high-memory interactive node for loading.

### Step 4 — Explore the object structure *(~10–20 min)*

```r
# What's inside?
Assays(sobj)     # e.g. "RNA", "SCT", "ATAC"
Reductions(sobj) # e.g. "pca", "umap", "harmony"
colnames(sobj@meta.data)   # all cell metadata columns — cell type labels live here

# Distribution of annotations
table(sobj@meta.data$seurat_clusters)
table(sobj@meta.data$cell_type)   # column name varies by author
```

### Step 5 — Visualize existing annotations *(~10–20 min)*

```r
# Authors' UMAP with cell type labels
DimPlot(sobj, group.by = "cell_type", label = TRUE, repel = TRUE) + NoLegend()

# Gene expression on UMAP
FeaturePlot(sobj, features = c("Pdgfra", "Rbfox3", "Gad2"), ncol = 3)

# Proportion of cell types per sample
table(sobj$cell_type, sobj$orig.ident)
```

### Step 6 — (Optional) Subset and re-analyze *(~30–90 min)*

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

> **Time estimate:** PCA + neighbors + UMAP on 5,000 cells takes ~2–5 min on a laptop. On 50,000+ cells, expect 15–30 min.

### Step 7 — (Optional) Pseudo-bulk differential expression *(~20–60 min)*

```r
library(DESeq2)

# Aggregate counts per sample × cell type
pseudo_bulk <- AggregateExpression(sobj,
                                   group.by = c("cell_type", "orig.ident"),
                                   assays = "RNA", slot = "counts",
                                   return.seurat = FALSE)$RNA

# Build coldata from column names
coldata <- data.frame(
  cell_type = sub("_.*", "", colnames(pseudo_bulk)),
  sample    = sub(".*_", "", colnames(pseudo_bulk))
)
rownames(coldata) <- colnames(pseudo_bulk)

# Filter to one cell type and run DESeq2
ct <- "Neuron"
sel <- coldata$cell_type == ct
dds <- DESeqDataSetFromMatrix(pseudo_bulk[, sel], coldata[sel, ],
                               design = ~ sample)
dds <- DESeq(dds)
```

---

## Loading a SingleCellExperiment object

```r
library(SingleCellExperiment)

sce <- readRDS("GSExxxxxx_sce.rds.gz")
class(sce)           # "SingleCellExperiment"
colData(sce)         # cell metadata (equivalent to @meta.data)
reducedDimNames(sce) # "PCA", "UMAP", etc.

# Convert to Seurat if preferred
sobj <- as.Seurat(sce)
```

---

## Real GEO examples

### [GSE139412](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE139412) — Neuron types of the adult mouse striatum
- **Organism:** Mus musculus | **Cells:** 1,207 | **Topics:** neuroscience
- **Files:** `GSE139412_striatum_final.rds.gz` (33 MB) — raw counts CSV also provided
- Small file, well-annotated — ideal first dataset to practice this protocol

### [GSE111976](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE111976) — Human endometrium across the menstrual cycle
- **Organism:** Homo sapiens | **Cells:** 2,158 | **Topics:** development, reproduction
- **Files:** `GSE111976_ct_endo_10x.rds.gz` (408 MB) — needs ~1.5 GB RAM
- Large object with temporal cell state annotations; raw CSV also available

### [GSE118723](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE118723) — Variance QTLs in human iPSCs
- **Organism:** Homo sapiens | **Cells:** 7,584 | **Topics:** development
- **Files:** `GSE118723_eset.rds.gz` (80 MB) — **ExpressionSet format, not Seurat**
- Load with `readRDS()` then check `class()` before assuming Seurat structure

### [GSE121265](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE121265) — Continuous cell-cycle phase from scRNA-seq
- **Organism:** Homo sapiens | **Cells:** 1,536 | **Topics:** cell cycle
- **Files:** `GSE121265_eset-final.rds.gz` (7 MB) and `-raw.rds.gz` (15 MB)
- Two objects: raw and processed — useful for understanding the full pipeline

## Common pitfalls

- **Seurat version mismatches:** objects saved with Seurat v4 may need updating for v5: `sobj <- UpdateSeuratObject(sobj)`. Objects from Seurat v2 require more manual work.
- **RAM errors on large files:** if you hit memory limits, try loading on a machine with more RAM, or use a cloud instance (AWS `r6i.2xlarge` has 64 GB RAM and is ~$0.50/hr). On a cluster, request a high-memory interactive node.
- **Normalized vs. raw counts:** Seurat objects store both. Raw counts: `GetAssayData(sobj, slot = "counts")`; normalized: `slot = "data"`. Use raw counts for DE.
- **Cell type label column names vary:** authors use `cell_type`, `CellType`, `ident`, `cluster_label`, `annotation`. Always inspect `colnames(sobj@meta.data)` first.
- **RData vs. RDS:** `.RData` files may contain multiple objects. Load with `load("file.RData")` (not `readRDS`) then `ls()` to see what was loaded.
- **Windows parallel processing:** replace `plan("multicore")` with `plan("multisession")` if using the `future` package for parallelism.
