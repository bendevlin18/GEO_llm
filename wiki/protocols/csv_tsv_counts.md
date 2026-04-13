# CSV / TSV Count Matrices

**Effort: ⭐ Easy | Time: minutes to an hour**

Pre-processed count or expression tables in plain text format. The most immediately usable format on GEO — no special tools required to read the file, just a spreadsheet or a single `read.csv()` call.

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

## Loading in R

```r
# Read a gzipped TSV — works directly, no need to decompress first
counts <- read.table("GSE65485_HCC_FPKM.txt.gz",
                     header = TRUE, row.names = 1, sep = "\t")

# Or CSV
counts <- read.csv("GSExxxxxx_counts.csv.gz", row.names = 1)

# Quick sanity check
dim(counts)          # genes x samples
head(rownames(counts))  # gene identifiers
colnames(counts)        # sample IDs
```

### Differential expression with DESeq2 (raw counts)

```r
library(DESeq2)

# counts must be integer raw counts (not FPKM/TPM)
# coldata: a data.frame with a 'condition' column matching colnames(counts)
coldata <- data.frame(
  condition = factor(c("control", "control", "treated", "treated")),
  row.names = colnames(counts)
)

dds <- DESeqDataSetFromMatrix(countData = counts,
                              colData   = coldata,
                              design    = ~ condition)
dds <- DESeq(dds)
res <- results(dds, contrast = c("condition", "treated", "control"))
res_ordered <- res[order(res$padj), ]
head(res_ordered)
```

### Visualization

```r
# PCA of normalized counts
vst_counts <- vst(dds, blind = FALSE)
plotPCA(vst_counts, intgroup = "condition")

# Heatmap of top DE genes
library(pheatmap)
top_genes <- head(rownames(res_ordered), 50)
pheatmap(assay(vst_counts)[top_genes, ], scale = "row")
```

## Loading in Python

```python
import pandas as pd
import numpy as np

# Reads gzipped files automatically
counts = pd.read_csv("GSE65485_HCC_FPKM.txt.gz", sep="\t", index_col=0)

print(counts.shape)    # (genes, samples)
print(counts.head())

# Quick DE with pydeseq2 (pip install pydeseq2)
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

metadata = pd.DataFrame({"condition": ["ctrl", "ctrl", "treat", "treat"]},
                         index=counts.columns)

dds = DeseqDataSet(counts=counts.T.astype(int),   # pydeseq2 expects samples x genes
                   metadata=metadata,
                   design_factors="condition")
dds.deseq2()

stat_res = DeseqStats(dds, contrast=["condition", "treat", "ctrl"])
stat_res.summary()
results_df = stat_res.results_df
```

## Real GEO examples

### [GSE67427](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE67427) — Human innate immune response to Mycobacterial infection
- **Organism:** Homo sapiens | **Samples:** 156 | **Topics:** immunology, infectious_disease
- **Files:** `GSE67427_table-s1.txt.gz` (15 MB)
- Good starting point: large cohort, bulk RNA-seq, single expression table

### [GSE65485](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE65485) — HBV integration in hepatocellular carcinoma
- **Organism:** Homo sapiens | **Samples:** 55 | **Topics:** cancer, liver
- **Files:** `GSE65485_HCC_FPKM.txt.gz` (3 MB)
- Note: FPKM values — good for visualization, use raw counts from SRA for DE

### [GSE65540](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE65540) — Adipose tissue RNA-seq before/after bariatric surgery
- **Organism:** Homo sapiens | **Samples:** 44 | **Topics:** metabolism, immunology
- **Files:** `GSE65540_SAT_processed_counts.txt.gz` (4 MB)
- Processed counts, condition metadata available on the GEO sample pages

### [GSE60571](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60571) — Drosophila sex-transformed heads RNA-seq
- **Organism:** Drosophila melanogaster | **Samples:** 249 | **Topics:** development
- **Files:** Raw counts + FPKM + DESeq2-normalized tables all provided (4–22 MB each)
- Example of a well-deposited dataset: multiple normalizations, large sample size

## Common pitfalls

- **Rows vs. columns:** some matrices are samples × genes (transposed). Check `dim()` — if you have more rows than columns and you expected genes as rows, transpose with `t()`.
- **FPKM ≠ counts:** FPKM/TPM cannot be used as input to DESeq2 or edgeR. Use them for visualization only. If the dataset only provides FPKM, you'll need to download raw reads from SRA to run DE analysis.
- **Gene ID format:** row names may be Ensembl IDs (`ENSG00000...`), gene symbols, or Entrez IDs. Check with `head(rownames(counts))` and convert with `org.Hs.eg.db` (R) or `mygene` (Python) if needed.
- **Multi-sheet Excel:** some authors use XLSX instead of CSV. Load with `readxl::read_excel()` in R or `pd.read_excel()` in Python — and check which sheet has the counts.
