# Single-Cell RNA-seq (scRNA-seq)

> 23260 datasets | 2015/01/01 – 2026/04/27

Transcriptome profiling at single-cell resolution. Typically uses droplet-based (10x Chromium, Drop-seq) or plate-based (Smart-seq) protocols. Supplementary files often include sparse count matrices (MTX), HDF5 objects (H5/H5AD), or R objects (RDS/Seurat).

## Organism Distribution

| Organism | Count |
|----------|------:|
| Mus musculus | 11770 |
| Homo sapiens | 8397 |
| Homo sapiens; Mus musculus | 467 |
| Danio rerio | 422 |
| Mus musculus; Homo sapiens | 257 |
| Rattus norvegicus | 206 |
| Drosophila melanogaster | 189 |
| Macaca mulatta | 103 |
| Sus scrofa | 97 |
| Gallus gallus | 86 |
| Arabidopsis thaliana | 66 |
| Bos taurus | 56 |
| Macaca fascicularis | 51 |
| Caenorhabditis elegans | 44 |
| Saccharomyces cerevisiae | 29 |

## Archive Contents (file types inside supplementary TAR/gz)

| Type | Count | Description |
|------|------:|-------------|
| TSV | 11914 | Tab-separated (10x barcodes/features, metadata) |
| MTX | 10670 | Sparse matrices (10x CellRanger output) |
| TXT | 5684 | Text files (count matrices, gene lists, metadata) |
| CSV | 4918 | Comma-separated (count matrices, DE results) |
| H5 | 3203 | HDF5 (CellRanger filtered matrices) |
| RDS | 1272 | R serialized objects (Seurat, SingleCellExperiment) |
| TAR | 1070 | Tar archives (bundled outputs) |
| XLSX | 955 | Excel (DE results, sample annotations) |
| BW | 564 | BigWig (coverage tracks) |
| H5AD | 549 | AnnData HDF5 (scanpy/Python ecosystem) |
| BED | 363 |  |
| BIGWIG | 265 | BigWig (coverage tracks) |
| TBI | 206 |  |
| TAB | 200 |  |
| NARROWPEAK | 155 |  |

## Analyzing These Datasets

| File Types | Protocol | Effort |
|------------|----------|--------|
| CSV, TAB, TSV, TXT, XLS, XLSX | [CSV / TSV Count Matrices](../protocols/csv_tsv_counts.md) | ⭐ Easy |
| RDA, RDATA, RDS | [RDS / Seurat Objects](../protocols/rds_seurat.md) | ⭐⭐ Easy–Medium |
| H5AD | [H5AD / AnnData (scanpy)](../protocols/h5ad_anndata.md) | ⭐⭐ Easy–Medium |
| H5 | [H5 / CellRanger HDF5](../protocols/h5_cellranger.md) | ⭐⭐⭐ Medium |
| MTX | [MTX / 10x Sparse Matrices](../protocols/mtx_10x.md) | ⭐⭐⭐ Medium |
| no_suppl / RAW.tar / FASTQ | [FASTQ / SRA Alignment](../protocols/fastq_alignment.md) | ⭐⭐⭐⭐ Hard |

> **Protocol pages coming soon:** **BED / BigWig / Peak files** (BED, BEDGRAPH, BIGWIG, BROADPEAK, BW, NARROWPEAK, WIG); **Bismark coverage / CpG call files** (COV); **IDAT (Illumina array raw intensities)** (IDAT).

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE325884](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325884) | Generation of a prop1 knockin zebrafish enables single-cell transcriptomics of e... | Danio rerio | 2 | MTX, TSV | 2026/04/27 |
| [GSE319205](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319205) | Thrombospondin-1:CD47 signaling contributes to the development of T cell exhaust... | Mus musculus | 4 | MTX, TSV | 2026/04/27 |
| [GSE314567](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314567) | Age- and Tissue-dependent Diversity of Human Plasmacytoid Dendritic Cells Uncove... | Mus musculus | 4 | H5, XLSX | 2026/04/27 |
| [GSE310710](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310710) | Post-Hoc Trial and Preclinical Data Identify IL1RAP as a Tumor Microenvironment ... | Mus musculus | 2 | MTX, TSV | 2026/04/27 |
| [GSE308520](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308520) | Deciphering the Single-Cell Molecular Landscape of Ampullary Cancer: A Rare Gast... | Homo sapiens | 5 | TSV | 2026/04/27 |
| [GSE305908](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305908) | Clusterin marks maladaptive regenerative responses throughout the kidney followi... | Mus musculus | 4 | MTX, TSV | 2026/04/27 |
| [GSE292130](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292130) | Longitudinal changes in DNA methylation in IDH-mutant glioma fuel disease progre... | Homo sapiens | 31 | RDS | 2026/04/27 |
| [GSE291885](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291885) | Longitudinal changes in DNA methylation in IDH-mutant glioma fuel disease progre... | Homo sapiens | 1 | TSV, XLSX | 2026/04/27 |
| [GSE289741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289741) | ROS-responsive OMV-liposome hybrid targets macrophages and annulus fibrosus cell... | Rattus norvegicus | 6 | TXT | 2026/04/27 |
| [GSE288156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288156) | Progressive intestinal tumor cell plasticity, Myc activation and loss of Lgr5+ t... | Mus musculus | 14 | BED, MTX, TSV | 2026/04/27 |
| [GSE287227](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE287227) | Transient SP140 inhibition unlocks hematopoietic stem cell fate from human pluri... | Homo sapiens | 9 | MTX, TSV | 2026/04/27 |
| [GSE273852](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE273852) | Age- and Tissue-dependent Diversity of Human Plasmacytoid Dendritic Cells Uncove... | Homo sapiens | 11 | CSV, MTX, TSV | 2026/04/27 |
| [GSE328779](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328779) | Single cell RNA-seq characterization of non-fibrotic stromal wound repopulation ... | Oryctolagus cuniculus | 8 | H5 | 2026/04/26 |
| [GSE328617](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328617) | Early-life nutritional imbalance impairs colonic epithelial regeneration through... | Mus musculus | 6 | MTX, TSV | 2026/04/26 |
| [GSE305390](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305390) | Stromal and Endothelial Transcriptional Changes during Progression from MGUS to ... | Mus musculus | 6 | H5 | 2026/04/26 |
| [GSE305389](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305389) | Stromal and Endothelial Transcriptional Changes during Progression from MGUS to ... | Homo sapiens | 25 | TXT | 2026/04/26 |
| [GSE299448](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299448) | scRNA-Seq of CD45+ cells in B16F10 tumor after adoptive cytotoxic T lymphocyte i... | Mus musculus | 3 | MTX, TSV | 2026/04/26 |
| [GSE289193](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289193) | Histone H4 lysine 20 tri-methylation safeguards breast cancer lineage fidelity a... | Homo sapiens; Mus musculus | 160 | BW, MTX, TSV | 2026/04/26 |
| [GSE289192](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289192) | Histone H4 lysine 20 tri-methylation safeguards breast cancer lineage fidelity a... | Mus musculus | 12 | MTX, TSV | 2026/04/26 |
| [GSE329070](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE329070) | TCF7L2 Promotes Abdominal Aortic Aneurysm through Smooth Muscle Cell-Mediated Ex... | Homo sapiens | 8 | TXT | 2026/04/25 |
| [GSE307142](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307142) | Tumor sialylation controls effective anti-cancer immunity in breast cancer | Mus musculus | 2 | H5 | 2026/04/25 |
| [GSE295702](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295702) | Human Nail Single-Cell Landscape Identifies KRT19+ NSCs and SOX2/SOX9-WNT Regula... | Homo sapiens | 3 | TAR | 2026/04/25 |
| [GSE262462](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262462) | Generation of synthetic kidneys from expandable kidney progenitors [Days 5 and 9... | Mus musculus | 4 | H5 | 2026/04/25 |
| [GSE328669](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328669) | A spatial in situ hybridization platform for T cell receptor variable gene-based... | Homo sapiens | 10 | CSV, H5 | 2026/04/24 |
| [GSE328550](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328550) | Macrophage-fibroblast crosstalk shapes wound repair signaling in vitro | Mus musculus | 2 | H5 | 2026/04/24 |
| [GSE314466](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314466) | Global knockout of melanoma differentiation-associated protein 5 protects mice f... | Homo sapiens | 6 | TXT | 2026/04/24 |
| [GSE310955](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310955) | Epithelial chemokine CCL25 integrates T cell development and intestinal homeosta... | Mus musculus | 2 | H5 | 2026/04/24 |
| [GSE308184](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308184) | Stress granule phase separation in stress-responsive cytosolic extract-in-oil dr... | Homo sapiens | 15 | TXT | 2026/04/24 |
| [GSE299936](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299936) | Phenotypic profiling of neutrophils in acute Clostridioides difficile infection ... | Mus musculus | 5 | CSV, H5, RDS | 2026/04/24 |
| [GSE295724](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295724) | Neuronal microexons modulate arousal via the cAMP-PKA-CREB pathway in zebrafish | Danio rerio | 59 | H5, TXT | 2026/04/24 |
| [GSE290574](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290574) | Gene Regulatory Networks Orchestrating Oocyte Fate Bifurcation in Primordial Fol... | Mus musculus | 386 | TXT | 2026/04/24 |
| [GSE328709](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328709) | Type I interferon signaling in microglia drives synaptic engulfment and neuronal... | Mus musculus | 13 | H5 | 2026/04/23 |
| [GSE328424](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328424) | Ductal Epithelial MXD3 Promotes Disease Progression in Acute Pancreatitis throug... | Rattus norvegicus | 0 | TXT | 2026/04/23 |
| [GSE328242](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328242) | Precision Editing of Cyclophilin A Generates Cyclosporine and Voclosporin Resist... | Homo sapiens | 24 | H5, TSV | 2026/04/23 |
| [GSE326070](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326070) | Interleukin-34 induced Arg1+ macrophages play a key role in breast cancer brain ... | Mus musculus | 1 | MTX, TSV | 2026/04/23 |
| [GSE310103](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310103) | Runx3 instructs Aire+ mTEC development, TSA gene expression, and central toleran... | Mus musculus | 2 | MTX, TSV | 2026/04/23 |
| [GSE306092](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306092) | Patient-Derived Lymphoma Spheroids Reveal Predictive Markers of Glofitamab Resis... | Homo sapiens | 12 | TAR | 2026/04/23 |
| [GSE305418](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305418) | ATF7ip inhibits the tumor immune response by promoting terminal CD8+ T cell Exha... | Mus musculus | 2 | MTX, TSV | 2026/04/23 |
| [GSE303977](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303977) | MECP2 Mutations Rewire Human ESC Fate and Bias Cortical Lineage Commitment II | Homo sapiens | 8 | CSV, MTX | 2026/04/23 |
| [GSE303838](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303838) | MECP2 Mutations Rewire Human ESC Fate and Bias Cortical Lineage Commitment [RNA-... | Homo sapiens | 48 | CSV | 2026/04/23 |
| [GSE303813](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303813) | MECP2 Mutations Rewire Human ESC Fate and Bias Cortical Lineage Commitment | Homo sapiens | 2 | CSV, MTX | 2026/04/23 |
| [GSE299896](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299896) | Micropeptide UEIS attenuates cGAS-STING-type I IFN signalling to repress anti-tu... | Mus musculus | 2 | MTX, TSV | 2026/04/23 |
| [GSE295557](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295557) | First-in-Class CAR T Cell Therapy Selectively Eliminates Mutant Calreticulin-Dri... | Homo sapiens | 5 | RDS | 2026/04/23 |
| [GSE294573](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294573) | HNF4a controls growth, identity and response to KRAS inhibition in IMA. | Homo sapiens; Mus musculus | 60 | BW, H5 | 2026/04/23 |
| [GSE294571](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294571) | HNF4a controls growth, identity and response to KRAS inhibition in IMA [scRNA-se... | Mus musculus | 2 | H5 | 2026/04/23 |
| [GSE294109](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294109) | Hypoxia shapes both therapeutic response and resistance in metastatic clear cell... | Homo sapiens | 25 | MTX, TSV | 2026/04/23 |
| [GSE293952](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293952) | Hypoxia shapes both therapeutic response and resistance in metastatic clear cell... | Homo sapiens | 61 | TXT | 2026/04/23 |
| [GSE293450](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293450) | Hypoxia shapes both therapeutic response and resistance in metastatic clear cell... | Mus musculus | 38 | MTX, TSV | 2026/04/23 |
| [GSE291623](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291623) | Glycine-modulating Slc6a20a-ASO restores NMDA receptor function in SHANK2 and SH... | Homo sapiens | 1 | MTX, TSV | 2026/04/23 |
| [GSE290144](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290144) | Thymic alveolar type II epithelial mimetic cells revealed by Runx1-deficiency [s... | Mus musculus | 2 | MTX, TSV | 2026/04/23 |

*...and 23210 more datasets.*
