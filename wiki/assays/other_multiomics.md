# Other Multiomics

> 389 datasets | 2016/04/12 – 2026/04/08

Joint profiling experiments that don't fall into the CITE-seq or RNA+ATAC categories. Includes triomics approaches (TEA-seq: RNA + ATAC + protein; DOGMA-seq: DNA methylation + chromatin + RNA), single-cell joint methylome + transcriptome profiling (scNMT-seq), and other simultaneous multi-assay designs.

## Organism Distribution

| Organism | Count |
|----------|------:|
| Homo sapiens | 163 |
| Mus musculus | 157 |
| Homo sapiens; Mus musculus | 16 |
| Mus musculus; Homo sapiens | 9 |
| Gallus gallus | 8 |
| Danio rerio | 4 |
| Arabidopsis thaliana | 4 |
| Drosophila melanogaster | 2 |
| Macaca mulatta | 2 |
| Homo sapiens; Mus musculus; Macaca fascicularis | 2 |
| Rattus norvegicus | 2 |
| synthetic construct; Mus musculus | 1 |
| Homo sapiens; synthetic construct | 1 |
| Homo sapiens; Oryza sativa Indica Group | 1 |
| Drosophila melanogaster; Mus musculus; Homo sapiens | 1 |

## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
| TSV | 261 | Tab-separated data (barcodes, features, fragment files) |
| H5 | 151 | HDF5 (CellRanger filtered matrices, combined RNA+ATAC) |
| MTX | 123 | Sparse count matrices (10x CellRanger output, RNA or ATAC) |
| TXT | 80 | Text files (count matrices, cell metadata) |
| CSV | 76 | Comma-separated data (count matrices, protein counts, metadata) |
| TBI | 76 |  |
| BED | 50 | BED peak calls (ATAC accessibility) |
| RDS | 34 | R serialized objects (Seurat, MultiAssayExperiment) |
| TAR | 21 | Tar archives (bundled multi-modal outputs) |
| BW | 19 | BigWig coverage tracks |
| BIGWIG | 18 | BigWig coverage tracks (ATAC or RNA coverage) |
| PAIRS | 12 |  |
| XLSX | 11 | Excel (metadata, differential results) |
| BEDGRAPH | 10 |  |
| JSON | 10 |  |

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE301970](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301970) | Multiome analysis of Kras-mutant intestinal epithelium 10 days post-recombinatio... | Mus musculus | 20 | H5, TSV | 2026/04/05 |
| [GSE301967](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301967) | Multiome analysis of tumors isolated from Apc cKO; Kras-mutant animals | Mus musculus | 12 | H5, TSV | 2026/04/05 |
| [GSE296612](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296612) | The impact of KLF2-KLF3 regulated cellular localization on exhausted T cell diff... | Mus musculus | 6 | H5, TBI, TSV | 2026/04/03 |
| [GSE281482](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE281482) | Single-cell multi-omic analysis of post-transplant mesenchymal cells reveals mol... | Homo sapiens | 8 | H5 | 2026/04/03 |
| [GSE325772](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325772) | CAR T therapy against the MiTF-driven protein GPNMB [Multiome-Seq] | Homo sapiens | 16 | CSV, MTX, TSV | 2026/04/02 |
| [GSE324206](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324206) | Spatially-Resolved Multiomic Atlas of Leiomyosarcoma Identifies Two Clinically R... | Homo sapiens | 32 | CSV, H5, TBI, TSV, TXT | 2026/04/01 |
| [GSE199064](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE199064) | Single cell multiomic landscape reveals gene programs driving lipid droplet hete... | Mus musculus | 4 | H5 | 2026/04/01 |
| [GSE267884](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE267884) | Foxp3 and BATF cooperatively direct cis-regulatory programs and gene expression ... | Mus musculus | 16 | H5, TBI, TSV | 2026/03/31 |
| [GSE309545](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309545) | Inflammatory signaling differentially changes chromatin accessibility and gene e... | Mus musculus | 64 | BIGWIG, H5, TSV | 2026/03/26 |
| [GSE309354](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309354) | Inflammatory signaling differentially changes chromatin accessibility and gene e... | Homo sapiens | 24 | BIGWIG, H5, TSV | 2026/03/26 |
| [GSE314911](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314911) | Dominant Malignant Clones Leverage Lineage Restricted Epigenomic Programs to Dri... | Homo sapiens | 21 | H5, TBI, TSV | 2026/03/25 |
| [GSE269937](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE269937) | Single cell multiome  atlas of pediatric ependymoma | Mus musculus | 10 | H5, TBI, TSV | 2026/03/25 |
| [GSE315670](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE315670) | Oncogenic and tumor-suppressive forces converge on a progenitor-orchestrated nic... | Mus musculus | 6 | MTX, TSV | 2026/03/18 |
| [GSE324568](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324568) | Gammaherpesviruses reprogram long-term myelopoiesis through CD8⁺ T cell–monocyte... | Mus musculus | 4 | BED, H5, TBI, TSV | 2026/03/17 |
| [GSE269703](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE269703) | Microbiota-derived polyphosphates govern mucosal immunity through multilevel sup... | Mus musculus | 16 | H5, TBI, TSV | 2026/03/17 |
| [GSE315967](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE315967) | Foxl2 preserves chromatin accessibility at a distal super-enhancer which regulat... | Mus musculus | 4 | MTX, TSV | 2026/03/16 |
| [GSE296329](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296329) | Single-cell epigenetic landscape, microenvironment interactions, and gene regula... | Homo sapiens | 12 | H5 | 2026/03/16 |
| [GSE296139](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296139) | Single-cell epigenetic landscape, microenvironment interactions, and gene regula... | Homo sapiens | 12 | H5 | 2026/03/16 |
| [GSE313719](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313719) | GFI1 regulates NK cell maturation and function [scMultiome-seq]. | Mus musculus | 8 | BED, ZIP | 2026/03/13 |
| [GSE322785](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322785) | Single-nucleus multiome analysis of the adult anthropoid cerebellar cortex acros... | Macaca mulatta; Homo sapiens; Callithrix jacchus; Pan troglodytes | 28 | H5, TSV | 2026/03/11 |
| [GSE322964](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322964) | Single cell and spatial sequencing analysis of cancer associated fibroblasts in ... | Homo sapiens | 22 | CSV, MTX, TSV | 2026/03/09 |
| [GSE317773](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317773) | Identification of a human hematopoietic stem cell subset that retains memory of ... | Homo sapiens | 2 | MTX, RDS, TSV, TXT | 2026/03/09 |
| [GSE305070](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305070) | Single-nucleus multiome ATAC-seq and RNA-seq analysis of GCM1 knockout in rotati... | Homo sapiens | 4 | BED, H5, TSV | 2026/03/09 |
| [GSE322480](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322480) | Multiome Profiling Reveals Astrocyte and Neuroendocrine Targets of Prenatal Acou... | Taeniopygia guttata | 16 | BED, MTX, TBI, TSV | 2026/03/06 |
| [GSE290061](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290061) | Single-cell multi-omics provide insights into molecular drivers of CAR T Cell Pe... | Homo sapiens | 22 | CSV, MTX, TSV | 2026/03/04 |
| [GSE292920](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292920) | Mesenchymal stromal cells induce MYC repression in activated T cells | Homo sapiens | 24 | MTX, TSV | 2026/03/01 |
| [GSE303996](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303996) | HDACs repress runaway stress and cell identity to promote  reprogramming in root... | Arabidopsis thaliana | 25 | BED, CSV, MTX, RDATA, RDS, TSV | 2026/02/25 |
| [GSE267255](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE267255) | Multi-dimensional characterization of a human cDC2 homeostatic maturation progra... | Homo sapiens | 2 | RDS, TSV | 2026/02/23 |
| [GSE309268](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309268) | Transcriptional programs dictating tumor cell fate decisions in neuroblastoma ly... | Homo sapiens | 19 | H5, TSV | 2026/02/18 |
| [GSE312572](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312572) | Unbalanced chromatin binding of Polycomb complexes drives neurodevelopmental dis... | Mus musculus | 22 | RDS | 2026/02/17 |
| [GSE302350](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302350) | KMT2D-deficiency destabilizes lineage progression in immature neural progenitors | Homo sapiens | 16 | H5, TSV | 2026/02/17 |
| [GSE281196](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE281196) | An immunobiliary single-cell atlas resolves crosstalk between type 2 conventiona... | Mus musculus | 4 | MTX, TSV | 2026/02/17 |
| [GSE287770](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE287770) | Simultaneous profiling of native-state proteomes and transcriptomes of brain cel... | Homo sapiens; Mus musculus | 74 | TXT | 2026/02/16 |
| [GSE319044](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319044) | Single-cell multiomic profiling of lung immune cells identifies novel asthma ris... | Homo sapiens | 32 | BED, CSV, H5, MTX, TBI, TSV, TXT | 2026/02/12 |
| [GSE290274](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290274) | KLF5 modulates epigenetic modifications driving human pancreatic ductal adenocar... | Homo sapiens | 16 | H5 | 2026/02/10 |
| [GSE276656](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276656) | Gene expression + ATAC multiome profiling of mPFC engram cells after OSK partial... | Mus musculus | 20 | H5, TBI, TSV | 2026/02/10 |
| [GSE279314](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE279314) | TGF-β controls epigenetic re-programing of IFN-antiviral trained immunity and im... | Macaca mulatta | 14 | CSV, H5, TBI, TSV | 2026/02/06 |
| [GSE317226](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317226) | HIF regulatory network reflects kidney disease progression in diabetes and rever... | Homo sapiens | 4 | CLOUPE, JPG, JSON, MTX, PARQUET, PNG, RDS, TIFF, TSV | 2026/02/05 |
| [GSE295977](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295977) | The Cd4+ T cell population Partners with Tpex CD8 T cells to mediate Antitumor I... | Homo sapiens | 2 | H5, MTX, TSV | 2026/02/05 |
| [GSE288697](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288697) | Multiple defects in mouse stem cell based embryo models lacking all Hox function... | Mus musculus | 8 | BED, LOOM, RDS, TAR, TXT | 2026/02/04 |
| [GSE288579](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288579) | Detecting Circadian Rhythmicity By Single Cell Multiomics | Mus musculus | 12 | H5 | 2026/02/04 |
| [GSE297040](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297040) | ZFP148 is a transcriptional regulator of effector CD8+ T cell differentiation [s... | Mus musculus | 4 | MTX, TSV | 2026/02/02 |
| [GSE316763](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316763) | Clonal memory of colitis accumulates and promotes tumor growth [IVFP] | Mus musculus | 13 | BW | 2026/02/01 |
| [GSE316618](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316618) | Clonal memory of colitis accumulates and promotes tumor growth [Visium] | Mus musculus | 2 | JPG, JSON, MTX, PARQUET, PNG, TIFF, TSV | 2026/02/01 |
| [GSE314943](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314943) | Single-cell multiomics uncovers an endothelial mechanosensitive PIEZO1-IL-33 axi... | Mus musculus | 18 | CSV, H5, MTX, TBI, TSV | 2026/01/30 |
| [GSE307731](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307731) | Genetic background and transient prenatal disruption of vitamin A signaling dete... | Mus musculus | 8 | H5, TBI, TSV | 2026/01/28 |
| [GSE297418](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297418) | MitoPerturb-Seq identifies gene-specific single-cell responses to mitochondrial ... | Mus musculus | 8 | BED, MTX, TBI, TSV | 2026/01/27 |
| [GSE277797](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE277797) | Multi-omic profiling unveils molecular landscapes and heterogeneous tumor microe... | Homo sapiens | 8 | H5, TSV | 2026/01/26 |
| [GSE310246](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310246) | EBF1 regulates sensory establishment in the cochlea by positioning the medial bo... | Mus musculus | 8 | CSV, H5, TSV | 2026/01/23 |
| [GSE312315](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312315) | Multi-ome profiles of KP4 cells, a Pancreatic Ductal adenocarcinoma cell line | Homo sapiens | 2 | MTX, TSV | 2026/01/16 |

*...and 339 more datasets.*
