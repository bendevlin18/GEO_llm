# RNA + ATAC Multiome

> 86 datasets | 2016/04/12 – 2026/04/08

Joint profiling of gene expression (RNA) and chromatin accessibility (ATAC) from the same single cells. The 10x Genomics Chromium Single Cell Multiome ATAC + Gene Expression kit is the most common platform. Related methods include SHARE-seq and SNARE-seq. Supplementary files include both RNA count matrices (H5, MTX) and ATAC fragment files (TSV) or peak calls (BED, BigWig).

## Organism Distribution

| Organism | Count |
|----------|------:|
| Homo sapiens | 60 |
| Mus musculus | 16 |
| Homo sapiens; Mus musculus | 6 |
| Mus musculus; Homo sapiens | 4 |

## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
| TXT | 46 | Text files (count matrices, cell metadata) |
| TAR | 36 | Tar archives (bundled multi-modal outputs) |
| TSV | 29 | Tab-separated data (barcodes, features, fragment files) |
| MTX | 16 | Sparse count matrices (10x CellRanger output, RNA or ATAC) |
| CSV | 14 | Comma-separated data (count matrices, protein counts, metadata) |
| H5 | 12 | HDF5 (CellRanger filtered matrices, combined RNA+ATAC) |
| TBI | 9 |  |
| BED | 8 | BED peak calls (ATAC accessibility) |
| H5AD | 7 | AnnData HDF5 (scanpy/Python ecosystem, multi-modal) |
| RDS | 6 | R serialized objects (Seurat, MultiAssayExperiment) |
| BEDPE | 2 |  |
| ZIP | 2 |  |
| RDA | 1 | R data files (multi-assay objects) |
| NARROWPEAK | 1 |  |
| PY | 1 |  |

## Analyzing These Datasets

| File Types | Protocol | Effort |
|------------|----------|--------|
| CSV, TSV, TXT | [CSV / TSV Count Matrices](../protocols/csv_tsv_counts.md) | ⭐ Easy |
| RDA, RDS | [RDS / Seurat Objects](../protocols/rds_seurat.md) | ⭐⭐ Easy–Medium |
| H5AD | [H5AD / AnnData (scanpy)](../protocols/h5ad_anndata.md) | ⭐⭐ Easy–Medium |
| H5 | [H5 / CellRanger HDF5](../protocols/h5_cellranger.md) | ⭐⭐⭐ Medium |
| MTX | [MTX / 10x Sparse Matrices](../protocols/mtx_10x.md) | ⭐⭐⭐ Medium |

> **Protocol pages coming soon:** **BED / BigWig / Peak files** (BED, NARROWPEAK).

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE314803](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314803) | Dominant Malignant Clones Leverage Lineage Restricted Epigenomic Programs to Dri... | Mus musculus | 18 | H5, TBI, TSV | 2026/03/25 |
| [GSE306582](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306582) | Astrocyte glucocorticoid receptor signaling restricts neuronal plasticity [SHARE... | Mus musculus | 2 | RDS | 2026/03/20 |
| [GSE291097](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291097) | Depolymerizing F-actin accelerates the exit from pluripotency to enhance stem ce... | Homo sapiens | 5 | MTX, TSV | 2026/03/13 |
| [GSE291096](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291096) | Depolymerizing F-actin accelerates the exit from pluripotency to enhance stem ce... | Homo sapiens | 8 | BED, CSV, H5, TBI, TSV | 2026/03/13 |
| [GSE293298](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293298) | Expression of synaptic function genes in iPSC-derived induced human neurons | Homo sapiens; Mus musculus | 2 | TSV | 2026/02/04 |
| [GSE284047](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE284047) | Inferring differential dynamics from multi-lineage, multi-omic, and multi-sample... | Homo sapiens | 6 | BEDPE, MTX, TSV | 2025/10/01 |
| [GSE302246](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302246) | Mapping enhancer-gene regulatory interactions from single-cell data | Homo sapiens | 2 |  | 2025/08/01 |
| [GSE249572](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE249572) | Human neuron subtype programming through combinatorial patterning with scSeq rea... | Homo sapiens | 21 | CSV, H5AD, TSV | 2025/07/15 |
| [GSE294772](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294772) | Single-Cell Epigenomics Uncovers Heterochromatin Instability and Transcription F... | Mus musculus | 142 | H5, H5AD, TBI, TSV | 2025/05/02 |
| [GSE254290](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE254290) | A feedback amplifier circuit with Notch and E2A orchestrates T-cell fate and sup... | Mus musculus | 4 | MTX, TSV | 2025/03/12 |
| [GSE269947](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE269947) | Single-nuclei transcriptional and chromatin accessibility profile of Beckwith-Wi... | Homo sapiens | 18 | CSV | 2025/03/07 |
| [GSE274040](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE274040) | Transcriptional and chromatin accessibility landscapes of hematopoiesis in a mou... | Mus musculus | 16 | ARROW, MTX, RDS, TSV | 2025/02/05 |
| [GSE277326](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE277326) | Single-cell analysis of the epigenome and 3D chromatin architecture in the human... | Homo sapiens | 18 | MTX, TBI, TSV | 2025/01/15 |
| [GSE286856](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286856) | snRNA-seq from left lung (ENCSR966DDY) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286848](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286848) | snRNA-seq from ovary (ENCSR938CZJ) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286824](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286824) | snRNA-seq from Right ventricle myocardium superior (ENCSR813PWQ) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286806](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286806) | snRNA-seq from heart left ventricle (ENCSR755CIF) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286796](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286796) | snRNA-seq from heart left ventricle (ENCSR727OYO) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286794](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286794) | snRNA-seq from adrenal gland (ENCSR726IPC) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286793](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286793) | snRNA-seq from adrenal gland (ENCSR724KET) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286789](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286789) | snRNA-seq from posterior vena cava (ENCSR716VLR) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286785](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286785) | snRNA-seq from left cardiac atrium (ENCSR700UVN) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286769](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286769) | snRNA-seq from fallopian tube (ENCSR642GFM) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286745](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286745) | snRNA-seq from left cardiac atrium (ENCSR527MGL) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286733](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286733) | snRNA-seq from heart left ventricle (ENCSR481QQR) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286731](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286731) | snRNA-seq from pancreas (ENCSR478FQR) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286727](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286727) | snRNA-seq from pancreas (ENCSR472RRP) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286726](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286726) | snRNA-seq from psoas muscle (ENCSR471YTA) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286724](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286724) | snRNA-seq from left cardiac atrium (ENCSR463EEP) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286722](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286722) | snRNA-seq from mucosa of descending colon (ENCSR460MGC) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286708](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286708) | snRNA-seq from heart right ventricle (ENCSR426PDU) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286700](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286700) | snRNA-seq from heart left ventricle (ENCSR405YKM) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286691](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286691) | snRNA-seq from left lobe of liver (ENCSR369UFT) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286690](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286690) | snRNA-seq from right lobe of liver (ENCSR367YUX) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286686](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286686) | snRNA-seq from adrenal gland (ENCSR362YDM) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286667](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286667) | snRNA-seq from left colon (ENCSR289ANH) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286665](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286665) | snRNA-seq from psoas muscle (ENCSR281RIH) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286664](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286664) | snRNA-seq from pancreas (ENCSR281NBH) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286657](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286657) | snRNA-seq from pancreas (ENCSR261BXB) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286655](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286655) | snRNA-seq from heart right ventricle (ENCSR258SZI) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286649](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286649) | snRNA-seq from lung (ENCSR225OII) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286640](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286640) | snRNA-seq from psoas muscle (ENCSR203THX) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286621](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286621) | snRNA-seq from Right ventricle myocardium inferior (ENCSR151ONW) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286606](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286606) | snRNA-seq from left ventricle myocardium superior (ENCSR079LVG) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286601](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286601) | snRNA-seq from heart right ventricle (ENCSR060ZXZ) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286600](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286600) | snRNA-seq from bile duct (ENCSR060SEA) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286586](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286586) | snRNA-seq from heart left ventricle (ENCSR012APQ) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286584](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286584) | snRNA-seq from fallopian tube (ENCSR011EDH) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE286580](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286580) | snRNA-seq from psoas muscle (ENCSR005TCL) | Homo sapiens | 1 | TAR, TXT | 2025/01/14 |
| [GSE237938](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE237938) | 10X Multiome AKSP | Mus musculus | 2 | MTX, TSV | 2024/10/17 |

*...and 36 more datasets.*
