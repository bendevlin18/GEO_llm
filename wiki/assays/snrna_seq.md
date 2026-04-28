# Single-Nucleus RNA-seq (snRNA-seq)

> 2003 datasets | 2015/01/01 – 2026/04/27

Transcriptome profiling from isolated nuclei rather than whole cells. Preferred for tissues that are difficult to dissociate (e.g., brain, adipose, muscle) or for frozen archival samples.

## Organism Distribution

| Organism | Count |
|----------|------:|
| Mus musculus | 1029 |
| Homo sapiens | 664 |
| Rattus norvegicus | 46 |
| Homo sapiens; Mus musculus | 24 |
| Sus scrofa | 20 |
| Drosophila melanogaster | 19 |
| Mus musculus; Homo sapiens | 16 |
| Arabidopsis thaliana | 15 |
| Macaca mulatta | 13 |
| Gallus gallus | 9 |
| Danio rerio | 7 |
| Bos taurus | 6 |
| Macaca mulatta; Homo sapiens | 5 |
| Homo sapiens; Canis lupus familiaris; Mus musculus | 4 |
| Mus musculus; Homo sapiens; Canis lupus familiaris | 4 |

## Archive Contents (file types inside supplementary TAR/gz)

| Type | Count | Description |
|------|------:|-------------|
| TSV | 837 | Tab-separated (10x barcodes/features, metadata) |
| MTX | 732 | Sparse matrices (10x CellRanger output) |
| TXT | 627 | Text files (count matrices, gene lists, metadata) |
| TAR | 468 | Tar archives (bundled outputs) |
| CSV | 312 | Comma-separated (count matrices, DE results) |
| H5 | 270 | HDF5 (CellRanger filtered matrices) |
| RDS | 170 | R serialized objects (Seurat, SingleCellExperiment) |
| XLSX | 57 | Excel (DE results, sample annotations) |
| TBI | 57 |  |
| H5AD | 55 | AnnData HDF5 (scanpy/Python ecosystem) |
| BED | 32 |  |
| BW | 21 | BigWig (coverage tracks) |
| RDATA | 18 |  |
| GTF | 12 |  |
| ZIP | 10 |  |

## Analyzing These Datasets

| File Types | Protocol | Effort |
|------------|----------|--------|
| CSV, TAB, TSV, TXT, XLS, XLSX | [CSV / TSV Count Matrices](../protocols/csv_tsv_counts.md) | ⭐ Easy |
| RDA, RDATA, RDS | [RDS / Seurat Objects](../protocols/rds_seurat.md) | ⭐⭐ Easy–Medium |
| H5AD | [H5AD / AnnData (scanpy)](../protocols/h5ad_anndata.md) | ⭐⭐ Easy–Medium |
| H5 | [H5 / CellRanger HDF5](../protocols/h5_cellranger.md) | ⭐⭐⭐ Medium |
| MTX | [MTX / 10x Sparse Matrices](../protocols/mtx_10x.md) | ⭐⭐⭐ Medium |

> **Protocol pages coming soon:** **BED / BigWig / Peak files** (BED, BEDGRAPH, BIGWIG, BW, NARROWPEAK, WIG); **IDAT (Illumina array raw intensities)** (IDAT).

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE328195](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328195) | Gene regulatory co-option drives birdsong neural circuit specialization [overexp... | Gallus gallus | 3 | MTX, TSV | 2026/04/24 |
| [GSE294786](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294786) | A lineage shared core gene expression network specific to human infants, links h... | Homo sapiens | 6 | TSV | 2026/04/24 |
| [GSE280266](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE280266) | Reprogramming of Cellular Plasticity via ETS and MYC Core-regulatory circuits Du... | Homo sapiens | 48 | TXT | 2026/04/24 |
| [GSE277487](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE277487) | Single-nucleus RNA-seq of mouse cortex following CCI-induced traumatic brain inj... | Mus musculus | 12 | CSV, MTX, TSV | 2026/04/24 |
| [GSE326221](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326221) | Acquired genetic and cell state changes in IDH-mutant glioma progression [snRNA-... | Homo sapiens | 75 | H5, MTX, TSV | 2026/04/23 |
| [GSE324860](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324860) | Acquired genetic and cell state changes in IDH-mutant glioma progression [organo... | Homo sapiens | 6 | MTX, TSV | 2026/04/23 |
| [GSE322712](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322712) | Distinct activity in prefrontal projections promotes temporal control of action | Mus musculus | 8 | H5 | 2026/04/23 |
| [GSE328680](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328680) | Hepatocyte-specific PPARγ Deletion Uncovers Role of an Antagonistic PPARγ–HNF4α ... | Mus musculus | 12 | TXT | 2026/04/22 |
| [GSE285766](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285766) | Single-cell multi-omic sequencing reveals cell-specific transcriptomic and chrom... | Mus musculus | 12 | CSV, MTX | 2026/04/22 |
| [GSE312674](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312674) | Pressure Overload-Induced Ventricular Crosstalk Activates Regenerative Mechanism... | Mus musculus | 1 | CSV, MTX, TSV, XLSX | 2026/04/21 |
| [GSE302892](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302892) | Transcriptomic Profiling of the Left Ventricle Using Single-Nucleus RNA Sequenci... | Mus musculus | 3 | H5 | 2026/04/21 |
| [GSE302702](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302702) | Single-nucleus RNA sequencing of human visceral adipose tissue biopsies from 11 ... | Homo sapiens | 11 | MTX, TSV | 2026/04/21 |
| [GSE302599](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302599) | Single-nucleus RNA sequencing of human visceral adipose tissue biopsies from 63 ... | Homo sapiens | 63 | MTX, TSV | 2026/04/21 |
| [GSE325391](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325391) | Unique transcriptional profiles of adult human immature neurons in healthy aging... | Homo sapiens | 27 | RDS | 2026/04/20 |
| [GSE324714](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324714) | Acquired genetic and cell state changes in IDH-mutant glioma progression [cocult... | Homo sapiens; Mus musculus | 16 | MTX, TSV | 2026/04/20 |
| [GSE324694](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324694) | Acquired genetic and cell state changes in IDH-mutant glioma progression | Homo sapiens | 10 | MTX, TSV | 2026/04/20 |
| [GSE324481](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324481) | Acquired genetic and cell state changes in IDH-mutant glioma progression | Homo sapiens | 4 | MTX, TSV | 2026/04/20 |
| [GSE328026](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328026) | MiT Fusions, TSC1–TSC2 Divergence, and Stem-like Programs Reveal Distinct Origin... | Homo sapiens | 69 | TXT | 2026/04/18 |
| [GSE327937](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327937) | MiT Fusions, TSC1–TSC2 Divergence, and Stem-like Programs Reveal Distinct Origin... | Homo sapiens | 5 | CSV, H5 | 2026/04/18 |
| [GSE328077](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328077) | Cultured ex vivo human brain tissue maintains cell-type transcriptional identiti... | Homo sapiens | 12 | H5 | 2026/04/16 |
| [GSE305396](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305396) | PGC-1alpha pathway dysregulation disrupts myofiber specification in a mouse mode... | Mus musculus | 6 | MTX, TSV | 2026/04/15 |
| [GSE305395](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305395) | PGC-1alpha pathway dysregulation disrupts myofiber specification in a mouse mode... | Mus musculus | 27 | CSV | 2026/04/15 |
| [GSE286360](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286360) | Angiopoietin-2 aggravates Alzheimer’s disease by promoting BBB breakdown and neu... | Mus musculus | 7 | MTX, TSV | 2026/04/15 |
| [GSE271813](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE271813) | Location matters: spatial-dependent effects of myofibroblasts determine survival... | Homo sapiens | 5 | MTX, TSV | 2026/04/15 |
| [GSE293016](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293016) | Glycogen metabolism in Sertoli cells sustains germ cell survival through lactate... | Mus musculus | 6 | BIGWIG, TXT | 2026/04/13 |
| [GSE289992](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289992) | Persistent dopamine-dependent remodeling of the neural transcriptome in response... | Mus musculus | 15 | MTX, TSV | 2026/04/13 |
| [GSE327236](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327236) | Integrated single-nucleus RNA-seq dataset of mouse brain from a multi-factorial ... | Mus musculus | 4 | MTX, TSV | 2026/04/12 |
| [GSE327614](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327614) | Early cell autonomous and niche-mediated alveolar epithelial response to influen... | Homo sapiens; Mus musculus | 24 | H5, RDS, TSV | 2026/04/10 |
| [GSE327108](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327108) | Tet governs transcriptional programs required for intestinal stem cell developme... | Drosophila melanogaster | 10 | H5AD | 2026/04/10 |
| [GSE308982](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308982) | Intravitreal AAV delivery induces integrin-dependent ocular inflammation and act... | Sus scrofa | 8 | MTX, TSV | 2026/04/07 |
| [GSE303719](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303719) | SnRNAseq of tumors isolated from Apc cKO; Kras-mutant animals | Mus musculus | 12 | H5 | 2026/04/05 |
| [GSE301123](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301123) | GPSM1 restricts CD73+CD103+ Treg cells in adipose tissue, critical for promoting... | Mus musculus | 6 | MTX, TSV | 2026/04/05 |
| [GSE296274](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296274) | Hcn1-dependent engram neurons in the PVN encode gastric inflammatory memory [gas... | Mus musculus | 2 | TAR | 2026/04/04 |
| [GSE275354](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE275354) | Exploring the Mechanism of SETDB1 in Regulating Neuroinflammation and Anxiety-De... | Mus musculus | 4 | MTX, TSV | 2026/04/04 |
| [GSE275353](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE275353) | Exploring the Mechanism of SETDB1 in Regulating Neuroinflammation and Anxiety-De... | Mus musculus | 19 | COUNTS | 2026/04/04 |
| [GSE326425](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326425) | Aldosterone-induced gene expression changes in the brain [scRNA-Seq] | Mus musculus | 4 | H5 | 2026/04/03 |
| [GSE326424](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326424) | Aldosterone-induced gene expression changes in the brain [Multiomic] | Mus musculus | 8 | H5, TSV | 2026/04/03 |
| [GSE302701](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302701) | Single-nucleus RNA sequencing of human subcutaneous adipose tissue biopsies from... | Homo sapiens | 59 | MTX, TSV | 2026/04/02 |
| [GSE325932](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325932) | Disease-associated microRNA, miR-9-2, is required for the timing of retinal prog... | Mus musculus | 32 | H5, RDS | 2026/04/01 |
| [GSE324206](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324206) | Spatially-Resolved Multiomic Atlas of Leiomyosarcoma Identifies Two Clinically R... | Homo sapiens | 32 | CSV, H5, TBI, TSV, TXT | 2026/04/01 |
| [GSE320334](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320334) | Nuclei Isolation from Rat and Bovine White Adipose Tissue for Single-Nuclei RNA ... | Bos taurus; Rattus norvegicus | 6 | CSV, MTX, TSV | 2026/04/01 |
| [GSE313595](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313595) | Single-nucleus RNA sequencing and functional studies of acute methamphetamine-in... | Mus musculus | 6 | MTX, TSV | 2026/04/01 |
| [GSE296012](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296012) | NeuID is a novel neuron-specific lncRNA that regulates neuronal function in Alzh... | Mus musculus | 12 | CSV | 2026/04/01 |
| [GSE235285](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE235285) | Rebalancing the brain: The therapeutic potential of false neurotransmitters in e... | Mus musculus | 8 | MTX, TSV | 2026/04/01 |
| [GSE303893](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303893) | Single-nuclus RNA sequencing of stem cell-derived human trophoblast organoids cu... | Homo sapiens | 1 | MTX, TSV | 2026/03/31 |
| [GSE292960](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292960) | single-nucleus RNA sequencing analysis for the molecular taxonomy of primate cla... | Macaca mulatta | 5 | MTX, TSV | 2026/03/31 |
| [GSE297148](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297148) | A Compendium of Cancer Organoid Models for Diverse Cancer Type | Homo sapiens | 16 | H5, H5AD | 2026/03/30 |
| [GSE324211](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324211) | Inducible XIST-mediated trisomy 21 correction uncovers a USP16-p16 senescence ax... | Homo sapiens | 4 | MTX, TSV | 2026/03/29 |
| [GSE322851](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322851) | Inducible XIST-mediated trisomy 21 correction uncovers a USP16-p16 senescence ax... | Homo sapiens | 45 | TXT | 2026/03/29 |
| [GSE293075](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293075) | Evolutionary transcriptomic and cellular specializations within the mammalian st... | Pan troglodytes; Macaca mulatta; Homo sapiens; Phyllostomus discolor | 42 | MTX, TSV | 2026/03/27 |

*...and 1953 more datasets.*
