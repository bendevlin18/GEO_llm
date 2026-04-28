# Spatial Transcriptomics

> 1046 datasets | 2015/01/01 – 2026/04/27

Spatially-resolved transcriptomics that preserves tissue context. Includes sequencing-based (10x Visium, Slide-seq, Stereo-seq) and imaging-based (MERFISH, seqFISH, CosMx, Xenium) methods. Supplementary files may include spatial coordinates (JSON/CSV) and tissue images (PNG/JPG).

## Organism Distribution

| Organism | Count |
|----------|------:|
| Homo sapiens | 451 |
| Mus musculus | 440 |
| Homo sapiens; Mus musculus | 23 |
| Rattus norvegicus | 11 |
| Danio rerio | 10 |
| Mus musculus; Homo sapiens | 9 |
| Sus scrofa | 8 |
| Gallus gallus | 5 |
| Xenopus laevis | 4 |
| Mus | 4 |
| Nematostella vectensis | 3 |
| Arabidopsis thaliana | 3 |
| Macaca fascicularis | 3 |
| Macaca mulatta | 3 |
| Dugesia japonica | 3 |

## Archive Contents (file types inside supplementary TAR/gz)

| Type | Count | Description |
|------|------:|-------------|
| TSV | 439 | Tab-separated (10x barcodes/features, metadata) |
| MTX | 374 | Sparse matrices (10x CellRanger output) |
| CSV | 343 | Comma-separated (count matrices, DE results) |
| TXT | 217 | Text files (count matrices, gene lists, metadata) |
| H5 | 213 | HDF5 (CellRanger filtered matrices) |
| PNG | 165 | Images (spatial, QC plots) |
| JSON | 148 | JSON (cell metadata, spatial coordinates) |
| JPG | 122 | Images (spatial, QC plots) |
| TAR | 110 | Tar archives (bundled outputs) |
| TIFF | 76 |  |
| RDS | 76 | R serialized objects (Seurat, SingleCellExperiment) |
| XLSX | 62 | Excel (DE results, sample annotations) |
| H5AD | 40 | AnnData HDF5 (scanpy/Python ecosystem) |
| DCC | 34 |  |
| ZIP | 17 |  |

## Analyzing These Datasets

| File Types | Protocol | Effort |
|------------|----------|--------|
| CSV, TAB, TSV, TXT, XLS, XLSX | [CSV / TSV Count Matrices](../protocols/csv_tsv_counts.md) | ⭐ Easy |
| RDA, RDATA, RDS | [RDS / Seurat Objects](../protocols/rds_seurat.md) | ⭐⭐ Easy–Medium |
| H5AD | [H5AD / AnnData (scanpy)](../protocols/h5ad_anndata.md) | ⭐⭐ Easy–Medium |
| H5 | [H5 / CellRanger HDF5](../protocols/h5_cellranger.md) | ⭐⭐⭐ Medium |
| MTX | [MTX / 10x Sparse Matrices](../protocols/mtx_10x.md) | ⭐⭐⭐ Medium |

> **Protocol pages coming soon:** **BED / BigWig / Peak files** (BED, BIGWIG, BW).

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE308140](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308140) | Spatiotemporal regulation of arbuscular mycorrhizal symbiosis at cellular resolu... | Oryza sativa | 38 | CSV | 2026/04/27 |
| [GSE328649](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328649) | Lineage 2-Beijing Mycobacterium tuberculosis strains suppress BCG-trained innate... | Homo sapiens | 39 | TXT | 2026/04/26 |
| [GSE328930](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE328930) | The DUTRENEO trial: bulk prospective biomarker-guided therapy selection and spat... | Homo sapiens | 66 | TSV | 2026/04/24 |
| [GSE324158](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324158) | Single-cell multi-omic and spatial landscape of primate pineal gland reveals cir... | Macaca fascicularis | 4 | BED, CSV, H5, JSON, MTX, PNG, TBI, TIFF, TSV, TXT | 2026/04/23 |
| [GSE294765](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294765) | A skeletal muscle atlas shows neuromuscular junction adaptations to growth and a... | Mus musculus | 35 | CSV, JPG, JSON, MTX, PNG, TSV | 2026/04/23 |
| [GSE277893](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE277893) | Single-Cell Spatial Mapping of Human Kidney Development Reveals Cellular Niches ... | Homo sapiens | 5 | MTX, TSV | 2026/04/22 |
| [GSE295236](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295236) | Excitatory neurons and astrocytes-specific dysregulation and aberrant interactio... | Homo sapiens | 6 | MTX, TSV | 2026/04/21 |
| [GSE327442](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327442) | Cellular Signatures of Melanocortin Pathway Genes Across the Locus Coeruleus [sn... | Homo sapiens | 4 | MTX, RDS, TSV | 2026/04/20 |
| [GSE296374](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296374) | Region- and cell type-specific changes in gene expression in the cerebellum afte... | Mus musculus | 3 | H5 | 2026/04/19 |
| [GSE327665](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327665) | Ustekinumab Resistance in Individuals with Ulcerative Colitis is Associated with... | Homo sapiens | 6 | MTX, TSV | 2026/04/17 |
| [GSE305558](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305558) | Single-cell profiling reveals RAB13+ endothelial cells and profibrotic mesenchym... | Homo sapiens | 12 | H5 | 2026/04/15 |
| [GSE294771](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294771) | A cellular anatomy of normal adult human female urethra | Homo sapiens | 4 | H5, RDS | 2026/04/15 |
| [GSE293947](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293947) | Spatially organizing million callus cells identify the core-network enable tomat... | Solanum lycopersicum | 84 | CSV, TXT | 2026/04/15 |
| [GSE293946](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293946) | Spatially organizing million callus cells identify the core-network enable tomat... | Solanum lycopersicum | 8 | RDS | 2026/04/15 |
| [GSE285362](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285362) | Identification of Cryosensitive Niches and a Targetable FOS/AP‑1 Program in the ... | Homo sapiens | 7 | MTX, TSV | 2026/04/15 |
| [GSE278973](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE278973) | Multi-omic profiling reveals epithelial remodeling in necrotizing enterocolitis | Mus musculus | 4 | MTX, TSV | 2026/04/15 |
| [GSE327488](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327488) | Mutual interaction between Schwann cells and CD4+T cells promotes the progressio... | Homo sapiens | 12 | TXT | 2026/04/14 |
| [GSE327303](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327303) | Spatiotemporal transcriptomics characterizes immune microenvironment during mous... | Mus musculus | 7 | MTX, RDS, TSV | 2026/04/13 |
| [GSE327302](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327302) | Spatiotemporal transcriptomics characterizes immune microenvironment during mous... | Mus musculus | 7 | MTX, RDS, TSV | 2026/04/13 |
| [GSE318565](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE318565) | Single-cell, clonal and spatial atlases of neural plate border and neurogenic pl... | Mus musculus | 12 | CSV, H5 | 2026/04/07 |
| [GSE326312](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326312) | Development and first-in-human CAR T therapy targeting the pathognomonic MiT-fus... | Homo sapiens | 20 | CSV, MTX, TSV | 2026/04/02 |
| [GSE325772](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325772) | CAR T therapy against the MiTF-driven protein GPNMB [Multiome-Seq] | Homo sapiens | 16 | CSV, MTX, TSV | 2026/04/02 |
| [GSE325620](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325620) | Comparative single-cell multiomic analysis reveals evolutionarily conserved and ... | Danio rerio | 14 | H5 | 2026/04/02 |
| [GSE325478](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325478) | Comparative single-cell multiomic analysis reveals evolutionarily conserved and ... | Mus musculus | 18 | H5 | 2026/04/02 |
| [GSE283385](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE283385) | CAR T therapy against the MiTF-driven protein GPNMB | Homo sapiens | 14 | CSV, MTX, TSV | 2026/04/02 |
| [GSE295641](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295641) | Multimodal profiling of oral squamous cell carcinoma identifies genomic alterati... | Homo sapiens | 2 | TXT | 2026/04/01 |
| [GSE325798](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325798) | Circuit Organization and Transcriptomic Heterogeneity of Sympathetic Circuits In... | Mus musculus | 4 | RDS | 2026/03/31 |
| [GSE324977](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324977) | Pathogenesis of Diffuse Large B-cell Lymphoma Proteogenotypes | Homo sapiens | 53 | TXT | 2026/03/31 |
| [GSE299387](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299387) | Comparative transcriptomics reveals emergent cortical architecture and plasticit... | Monodelphis domestica | 2 | MTX, TSV | 2026/03/31 |
| [GSE296276](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296276) | Distinct tissue niches contribute to prostate TRM cell differentiation and heter... | Mus musculus | 12 | CSV | 2026/03/31 |
| [GSE320592](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320592) | Hypoxia-EPAS1 imprints immunoregulation and maintenance of type 2 tissue-residen... | Mus musculus | 4 | H5 | 2026/03/30 |
| [GSE320591](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320591) | Hypoxia-EPAS1 imprints immunoregulation and maintenance of type 2 tissue-residen... | Mus musculus | 11 | BW, FPKM_TRACKING | 2026/03/30 |
| [GSE320590](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320590) | Hypoxia-EPAS1 imprints immunoregulation and maintenance of type 2 tissue-residen... | Mus musculus | 6 | FPKM_TRACKING | 2026/03/30 |
| [GSE320588](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320588) | Hypoxia-EPAS1 imprints immunoregulation and maintenance of type 2 tissue-residen... | Mus musculus | 16 | BIGWIG, H5 | 2026/03/30 |
| [GSE304621](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE304621) | Single-cell and spatial transcriptomic analyses of gene therapy-associated retin... | Macaca mulatta | 10 | MTX, TSV | 2026/03/30 |
| [GSE294277](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294277) | Integrative single cell RNA-sequencing and spatial transcriptomics uncovers dist... | Homo sapiens | 22 | CSV, JPG, JSON, MTX, PNG, TSV, XLSX | 2026/03/28 |
| [GSE326150](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326150) | Single-cell profiles delineate immune cell remodeling and enhanced tumor-fibrobl... | Homo sapiens | 1 | CSV, MTX, TSV | 2026/03/27 |
| [GSE314550](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314550) | Mapping neuro-vascular unit communications reveals distinct angiogenic programs ... | Mus musculus | 3 | CSV, H5, RDS | 2026/03/27 |
| [GSE292970](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292970) | Spatially organizing million callus cells identify the core-network enable tomat... | Homo sapiens | 54 | CSV | 2026/03/27 |
| [GSE288200](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288200) | A rewired myeloid niche in spleen establishes stress erythropoiesis | Mus musculus | 9 | H5AD, TAR | 2026/03/27 |
| [GSE242214](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242214) | A molecular atlas of brain neurovascular interactions reveals a spatiotemporal r... | Mus musculus | 6 | H5, PNG, RDS, TIFF, TSV | 2026/03/27 |
| [GSE325829](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325829) | Single-cell transcriptome atlas of human embryos after gastrulation | Homo sapiens | 124 | H5AD | 2026/03/26 |
| [GSE312237](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312237) | Spatial transcriptomic profiling identifies lacrimal gland epithelial cell-drive... | Mus musculus | 90 | DCC | 2026/03/25 |
| [GSE325123](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325123) | The melanocytic transcriptomic state is independently associated with poor overa... | Homo sapiens | 272 | CSV, TXT | 2026/03/24 |
| [GSE293457](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293457) | Retinoic acid drives cell fate specification, maturation and retinal regionality... | Homo sapiens | 4 | H5 | 2026/03/22 |
| [GSE322686](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322686) | Longitudinal Multiomic and Spatial Transcriptomic Profiling of Lupus Nephritis P... | Mus musculus | 13 | CSV, JPG, JSON, MTX, PNG, TSV, TXT, XLSX | 2026/03/21 |
| [GSE312235](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312235) | Tumors Hijack Immune-Privileging Regulons via Distinct Cell Types to Confer T Ce... | Homo sapiens | 72 | TSV | 2026/03/21 |
| [GSE325371](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325371) | SlCAX3 drives the formation of crystal idioblasts for tomato ion compartmentaliz... | Solanum lycopersicum | 10 | RDS, TAR | 2026/03/20 |
| [GSE317209](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317209) | Mapping Endothelial-Macrophage Interactions in Diabetic Vasculature: Role of TRE... | Homo sapiens | 6 | TXT | 2026/03/20 |
| [GSE293428](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293428) | Mapping Endothelial-Macrophage Interactions in Diabetic Vasculature: Role of TRE... | Homo sapiens | 18 | MTX, TSV | 2026/03/20 |

*...and 996 more datasets.*
