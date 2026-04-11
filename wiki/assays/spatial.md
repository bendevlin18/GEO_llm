# Spatial Transcriptomics

> 1027 datasets | 2015/01/01 – 2026/04/08

Spatially-resolved transcriptomics that preserves tissue context. Includes sequencing-based (10x Visium, Slide-seq, Stereo-seq) and imaging-based (MERFISH, seqFISH, CosMx, Xenium) methods. Supplementary files may include spatial coordinates (JSON/CSV) and tissue images (PNG/JPG).

## Organism Distribution

| Organism | Count |
|----------|------:|
| Homo sapiens | 441 |
| Mus musculus | 435 |
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
| Macaca mulatta | 3 |
| Dugesia japonica | 3 |
| Homo sapiens; blank sample | 2 |

## Archive Contents (file types inside supplementary TAR/gz)

| Type | Count | Description |
|------|------:|-------------|
| TSV | 428 | Tab-separated (10x barcodes/features, metadata) |
| MTX | 364 | Sparse matrices (10x CellRanger output) |
| CSV | 339 | Comma-separated (count matrices, DE results) |
| TXT | 213 | Text files (count matrices, gene lists, metadata) |
| H5 | 209 | HDF5 (CellRanger filtered matrices) |
| PNG | 163 | Images (spatial, QC plots) |
| JSON | 146 | JSON (cell metadata, spatial coordinates) |
| JPG | 121 | Images (spatial, QC plots) |
| TAR | 110 | Tar archives (bundled outputs) |
| TIFF | 75 |  |
| RDS | 71 | R serialized objects (Seurat, SingleCellExperiment) |
| XLSX | 62 | Excel (DE results, sample annotations) |
| H5AD | 40 | AnnData HDF5 (scanpy/Python ecosystem) |
| DCC | 34 |  |
| ZIP | 17 |  |

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
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
| [GSE317073](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317073) | Oncogenic and tumor-suppressive forces converge on a progenitor-orchestrated nic... | Mus musculus | 4 | H5AD, MTX, TSV | 2026/03/18 |
| [GSE315670](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE315670) | Oncogenic and tumor-suppressive forces converge on a progenitor-orchestrated nic... | Mus musculus | 6 | MTX, TSV | 2026/03/18 |
| [GSE315242](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE315242) | Oncogenic and tumor-suppressive forces converge on a progenitor-orchestrated nic... | Mus musculus | 8 | MTX, TSV | 2026/03/18 |
| [GSE315241](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE315241) | Oncogenic and tumor-suppressive forces converge on a progenitor-orchestrated nic... | Mus musculus | 1 | JSON, MTX, TSV | 2026/03/18 |
| [GSE313305](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313305) | Oncogenic and tumor-suppressive forces converge on a progenitor-orchestrated nic... | Mus musculus | 17 | MTX, TSV | 2026/03/18 |
| [GSE276088](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276088) | Single-cell transcriptomic and spatial subcellular landscape of the articular di... | Mus musculus | 18 | CSV | 2026/03/18 |
| [GSE324074](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324074) | Integrated spatial transcriptomics (Stereo-seq) and bulk RNA-seq of cardiac sono... | Rattus norvegicus | 13 | TXT | 2026/03/17 |
| [GSE292145](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292145) | Dynamic plasticity of gastric neck cells contributes to regeneration and metapla... | Mus musculus | 11 | TSV | 2026/03/17 |
| [GSE290367](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290367) | Single-cell multiomic integration identifies widespread, cell-type resolved feta... | Homo sapiens | 90 | H5AD, TSV | 2026/03/15 |
| [GSE289709](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289709) | Tff2 marks gastric corpus progenitors that give rise to pyloric metaplasia/SPEM ... | Mus musculus | 2 | MTX, TSV | 2026/03/14 |
| [GSE293781](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293781) | An organoid model of the human adrenal cortex identifies drivers of steroidogene... | Homo sapiens | 9 | H5AD | 2026/03/12 |
| [GSE286328](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286328) | Single-Cell Chromatin Accessibility Landscape of Developing Perinatal Mouse Skin... | Mus musculus | 10 | H5, TSV | 2026/03/12 |
| [GSE323357](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE323357) | Single-cell and Spatial Transcriptomic Profiling of the Bone Metastatic Microenv... | Mus musculus | 5 | CSV, JPG, JSON, MTX, PNG, TSV | 2026/03/11 |
| [GSE324453](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324453) | Dissecting the cellular architecture of breast cancer brain metastases reveals p... | Homo sapiens | 28 | RDS | 2026/03/10 |
| [GSE322943](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322943) | Dissecting the cellular architecture of breast cancer brain metastases reveals p... | Homo sapiens | 100 | XLSX | 2026/03/10 |
| [GSE299050](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299050) | Immune Dynamics in Palmoplantar Pustulosis Unveiled by Single-Cell and High-Reso... | Homo sapiens | 5 | H5 | 2026/03/09 |
| [GSE317680](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317680) | Single Cell and Spatial Transcriptomics Identify Novel Immune-Stromal Interactio... | Homo sapiens | 13 | CSV, MTX, RDS | 2026/03/06 |
| [GSE304864](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE304864) | Multiomics immune profiling of a patient-relevant orthotopic lung cancer model u... | Mus musculus | 11 | CSV, H5 | 2026/03/06 |
| [GSE299711](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299711) | Clonal dynamics reveal cancer resistance arises from adaptive programs [scRNA-Se... | Homo sapiens | 8 | RDS | 2026/03/04 |

*...and 977 more datasets.*
