# CSV / TSV Count Matrices

**Effort: ⭐ Easy | Total time: ~30 minutes to 2 hours**

Pre-processed count or expression tables in plain text format. The most immediately usable format on GEO — no special tools required to read the file, just a spreadsheet or a single `read.csv()` call.

## Requirements

| | |
|---|---|
| **OS** | Mac, Windows, or Linux — any works equally well |
| **Compute** | Laptop or desktop — no cluster needed |
| **RAM** | 4–8 GB is sufficient for most datasets; large cohorts (200+ samples) may need 16 GB |
| **Storage** | Files are small (1–50 MB compressed); expand to 2–10× uncompressed in R/Python |
| **Key packages** | R: `DESeq2`, `edgeR`, `pheatmap`; Python: `pandas`, `pydeseq2` |

## What you'll find

These files typically contain one of:

- **Raw counts** — integer read counts per gene per sample (use for DE analysis with DESeq2 / edgeR)
- **Normalized counts** — DESeq2-normalized or TMM-normalized values
- **FPKM / RPKM / TPM** — length-normalized expression values (useful for visualization; generally not appropriate as input to DESeq2)

The column names are usually sample IDs or condition labels. The row names are gene symbols or Ensembl IDs. Always check: are rows genes or samples? (It varies.)

## Common filename patterns

```
GSExxxxxx_counts.csv.gz
GSExxxxxx_raw_read_counts.txt.gz
GSExxxxxx_FPKM.txt.gz
GSExxxxxx_TPM.tsv.gz
GSExxxxxx_DESeq2_normalized.txt.gz
GSExxxxxx_expression_matrix.csv.gz
```

---

## Steps (R)

### Step 1 — Install packages *(first time only, ~5 min)*

```r
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install(c("DESeq2", "pheatmap"))
```

> **Windows note:** R on Windows works fine for this protocol. Install R from [cran.r-project.org](https://cran.r-project.org/) and RStudio from [posit.co](https://posit.co/).

### Step 2 — Download the file from GEO *(~2–10 min depending on file size)*

Download the supplementary file from the GEO accession page (Supplementary files section) or directly from the FTP link shown in the search index.

```bash
# From the GEO FTP — replace with the actual filename
wget "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE65nnn/GSE65485/suppl/GSE65485_HCC_FPKM.txt.gz"
```

> **Windows note:** use the GEO web interface to download, or install [wget for Windows](https://eternallybored.org/misc/wget/). Alternatively, paste the URL directly into your browser.

### Step 3 — Load and inspect the matrix *(~5 min)*

```r
# Gzipped files load directly — no need to decompress first
counts <- read.table("GSE65485_HCC_FPKM.txt.gz",
                     header = TRUE, row.names = 1, sep = "\t")

# Or CSV
counts <- read.csv("GSExxxxxx_counts.csv.gz", row.names = 1)

# Sanity check
dim(counts)             # should be genes × samples (e.g. 20000 × 55)
head(rownames(counts))  # gene identifiers — symbols or Ensembl IDs
colnames(counts)        # sample IDs
range(counts)           # if values > 100 and non-integer, likely FPKM/TPM not raw counts
```

> **RAM:** A 10 MB compressed file typically expands to ~150–400 MB in R — trivial on any modern machine.

### Step 4 — Build a sample metadata table *(~10–20 min)*

DESeq2 requires a data frame describing each sample's condition. This information is usually in the GEO sample pages or a README file.

```r
# Build manually (check the GEO sample pages for condition labels)
coldata <- data.frame(
  condition = factor(c("control", "control", "treated", "treated")),
  row.names = colnames(counts)
)

# Or read from a metadata CSV if the authors provided one
coldata <- read.csv("GSExxxxxx_metadata.csv", row.names = 1)
```

### Step 5 — Run differential expression with DESeq2 *(~5–30 min)*

> **Note:** DESeq2 requires **raw integer counts**. If your file contains FPKM or TPM, skip to visualization or return to SRA for raw reads.

```r
library(DESeq2)

dds <- DESeqDataSetFromMatrix(countData = counts,
                              colData   = coldata,
                              design    = ~ condition)
dds <- DESeq(dds)   # ~5 min for 50 samples; ~20–30 min for 200+ samples

res <- results(dds, contrast = c("condition", "treated", "control"))
res_ordered <- res[order(res$padj), ]
head(res_ordered)

# Export results
write.csv(as.data.frame(res_ordered), "DE_results.csv")
```

### Step 6 — Visualize *(~10–20 min)*

```r
# PCA
vst_counts <- vst(dds, blind = FALSE)
plotPCA(vst_counts, intgroup = "condition")

# Heatmap of top DE genes
library(pheatmap)
top_genes <- head(rownames(res_ordered[!is.na(res_ordered$padj), ]), 50)
pheatmap(assay(vst_counts)[top_genes, ], scale = "row",
         annotation_col = coldata)

# Volcano plot
plot(res$log2FoldChange, -log10(res$padj),
     pch = 20, col = ifelse(res$padj < 0.05, "red", "grey"),
     xlab = "log2 Fold Change", ylab = "-log10 adjusted p-value")
```

---

## Steps (Python)

### Step 1 — Set up environment *(first time only, ~5 min)*

```bash
conda create -n rnaseq python=3.11 pandas numpy pydeseq2 matplotlib seaborn -y
conda activate rnaseq
```

### Step 2 — Load and inspect *(~5 min)*

```python
import pandas as pd

# Reads gzipped files automatically
counts = pd.read_csv("GSE65485_HCC_FPKM.txt.gz", sep="\t", index_col=0)

print(counts.shape)    # (genes, samples)
print(counts.head())
print(counts.describe())
```

### Step 3 — Differential expression with pydeseq2 *(~10–20 min)*

```python
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

metadata = pd.DataFrame({"condition": ["ctrl", "ctrl", "treat", "treat"]},
                         index=counts.columns)

dds = DeseqDataSet(counts=counts.T.astype(int),  # pydeseq2 expects samples × genes
                   metadata=metadata,
                   design_factors="condition")
dds.deseq2()

stat_res = DeseqStats(dds, contrast=["condition", "treat", "ctrl"])
stat_res.summary()
results_df = stat_res.results_df.sort_values("padj")
results_df.to_csv("DE_results.csv")
```

---

## Real GEO examples

### [GSE67427](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE67427) — Human innate immune response to Mycobacterial infection
- **Organism:** Homo sapiens | **Samples:** 156 | **Topics:** immunology, infectious_disease
- **Files:** `GSE67427_table-s1.txt.gz` (15 MB)
- Large cohort, single expression table — good starting point

### [GSE65485](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE65485) — HBV integration in hepatocellular carcinoma
- **Organism:** Homo sapiens | **Samples:** 55 | **Topics:** cancer, liver
- **Files:** `GSE65485_HCC_FPKM.txt.gz` (3 MB)
- FPKM values — good for visualization; use raw counts from SRA for DE

### [GSE65540](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE65540) — Adipose tissue RNA-seq before/after bariatric surgery
- **Organism:** Homo sapiens | **Samples:** 44 | **Topics:** metabolism, immunology
- **Files:** `GSE65540_SAT_processed_counts.txt.gz` (4 MB)
- Processed counts with condition metadata on the GEO sample pages

### [GSE60571](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60571) — Drosophila sex-transformed heads RNA-seq
- **Organism:** Drosophila melanogaster | **Samples:** 249 | **Topics:** development
- **Files:** Raw counts + FPKM + DESeq2-normalized tables (4–22 MB each)
- Well-deposited: multiple normalizations provided; large sample size

## Common pitfalls

- **Rows vs. columns:** some matrices are samples × genes (transposed). Check `dim()` — if you have more rows than columns when expecting genes as rows, transpose with `t()`.
- **FPKM ≠ counts:** FPKM/TPM cannot be used as input to DESeq2 or edgeR. Use them for visualization only. If the dataset only provides FPKM, you'll need to download raw reads from SRA.
- **Gene ID format:** row names may be Ensembl IDs (`ENSG00000...`), gene symbols, or Entrez IDs. Check with `head(rownames(counts))` and convert with `org.Hs.eg.db` (R) or `mygene` (Python) if needed.
- **Multi-sheet Excel:** some authors use XLSX. Load with `readxl::read_excel()` in R or `pd.read_excel()` in Python — check which sheet has the counts.
