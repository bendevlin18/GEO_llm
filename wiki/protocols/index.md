# Analysis Protocols — Getting Started with GEO Data

When you find a dataset in this wiki, the next question is: *what do I actually do with it?* This depends almost entirely on what supplementary files the authors deposited. This page helps you figure that out and points you to the right protocol.

## Step 1 — Look at the files

Check the dataset's FTP listing (linked from each GEO accession page, or visible in the search index `files` column). The file extensions tell you where you are on the effort scale:

| What you see | Format | Protocol | Effort |
|---|---|---|:---:|
| `*_counts.csv.gz`, `*_FPKM.txt.gz`, `*_TPM.tsv.gz` | Count matrix (text) | [CSV / TSV counts](csv_tsv_counts.md) | ⭐ |
| `*.rds.gz`, `*.RData.gz` | Seurat / R object | [RDS / Seurat](rds_seurat.md) | ⭐⭐ |
| `*.h5ad.gz` | AnnData (scanpy) | [H5AD / AnnData](h5ad_anndata.md) | ⭐⭐ |
| `*.h5`, `*filtered_feature_bc_matrix.h5` | CellRanger HDF5 | [H5 / CellRanger](h5_cellranger.md) | ⭐⭐⭐ |
| `*.mtx.gz` + `barcodes.tsv.gz` + `features.tsv.gz` | 10x sparse matrix | [MTX / 10x](mtx_10x.md) | ⭐⭐⭐ |
| `RAW.tar` only, or no supplementary files | Raw reads on SRA | [FASTQ / SRA](fastq_alignment.md) | ⭐⭐⭐⭐ |

## Effort tiers

| Tier | Starting point | Time to first analysis | Difficulty |
|:---:|---|---|---|
| ⭐ | Processed count matrix — ready to load | Minutes to an hour | Easy |
| ⭐⭐ | Serialized analysis object — load and explore | A few hours | Easy–Medium |
| ⭐⭐⭐ | Raw count matrix — needs filtering and clustering | Half a day | Medium |
| ⭐⭐⭐⭐ | Raw reads only — needs alignment | 1–3 days | Hard |

## Step 2 — Know your ecosystem

Most genomics analysis happens in either **R** (Bioconductor, Seurat, DESeq2) or **Python** (scanpy, AnnData). The format often implies the ecosystem:

- **RDS / RData** → R (Seurat, SingleCellExperiment, DESeq2Results)
- **H5AD** → Python (scanpy / anndata)
- **MTX / H5 / CSV** → either; both ecosystems have readers

If you're starting fresh and the dataset has both RDS and H5AD, pick whichever ecosystem you know better — the analysis steps are equivalent.

## Step 3 — Check for accompanying metadata

Good datasets deposit more than just the count matrix. Look for:

- **Cell metadata** — `*_metadata.csv`, `*_annotation.txt`, `*_obs.csv` — contains cell type labels, cluster assignments, sample IDs, conditions
- **Gene metadata** — `*_genes.tsv`, `*_features.tsv` — gene IDs and symbols
- **DE results** — `*_DEGs.csv`, `*_markers.xlsx` — pre-computed differential expression
- **README** — authors sometimes explain the file structure; always worth reading

If a dataset has an RDS file plus a metadata CSV, you may be able to skip re-clustering entirely and work directly from the authors' annotations.

## Protocol pages

- [CSV / TSV count matrices](csv_tsv_counts.md) — bulk RNA-seq, pre-processed expression tables
- [RDS / Seurat objects](rds_seurat.md) — single-cell, load directly into Seurat
- [H5AD / AnnData](h5ad_anndata.md) — single-cell, Python/scanpy ecosystem
- [H5 / CellRanger HDF5](h5_cellranger.md) — single-cell, 10x output in HDF5 format
- [MTX / 10x sparse matrices](mtx_10x.md) — single-cell, raw CellRanger output (3 files)
- [FASTQ / SRA](fastq_alignment.md) — raw reads, requires alignment pipeline
