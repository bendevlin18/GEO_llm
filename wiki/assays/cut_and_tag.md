# CUT&Tag

> 712 datasets | 2015/01/01 – 2026/04/08

Cleavage Under Targets and Tagmentation (CUT&Tag). Uses protein-A-Tn5 fusion to simultaneously cut and tag chromatin near antibody-bound targets. Even lower background than CUT&RUN, compatible with single cells. Supplementary files: BED, BigWig, narrowPeak.

## Target Type Breakdown

| Target Type | Count | Description |
|-------------|------:|-------------|
| tf | 350 | Transcription factor binding sites |
| histone | 221 | Histone modification marks (H3K27ac, H3K4me3, H3K27me3, etc.) |
| other | 141 | Chromatin structural proteins (CTCF, cohesin, Pol2, etc.) |

## Organism Distribution

| Organism | Count |
|----------|------:|
| Mus musculus | 318 |
| Homo sapiens | 295 |
| Drosophila melanogaster | 13 |
| Homo sapiens; Mus musculus | 13 |
| Danio rerio | 9 |
| Rattus norvegicus | 9 |
| Mus musculus; Homo sapiens | 7 |
| Toxoplasma gondii | 7 |
| Anopheles gambiae | 5 |
| Plasmodium falciparum | 4 |
| Gallus gallus | 3 |
| Bos taurus | 3 |
| Oryza sativa | 3 |
| Arabidopsis thaliana | 2 |
| Caenorhabditis elegans | 2 |

## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
| BW | 488 | BigWig coverage tracks |
| NARROWPEAK | 116 | ENCODE narrowPeak format (TF / sharp peaks) |
| BED | 104 | BED peak calls (genomic intervals) |
| BIGWIG | 85 | BigWig coverage tracks |
| TXT | 64 | Text files (peak lists, count tables, metadata) |
| BEDGRAPH | 28 | BedGraph coverage files |
| XLSX | 23 |  |
| TSV | 17 | Tab-separated data |
| CSV | 16 | Comma-separated data |
| BROADPEAK | 14 | ENCODE broadPeak format (histone / broad marks) |
| XLS | 6 |  |
| PDF | 4 |  |
| TDF | 4 |  |
| WIG | 3 | Wiggle coverage format |
| TAB | 3 |  |

## Analyzing These Datasets

| File Types | Protocol | Effort |
|------------|----------|--------|
| CSV, TAB, TSV, TXT, XLS, XLSX | [CSV / TSV Count Matrices](../protocols/csv_tsv_counts.md) | ⭐ Easy |
| RDS | [RDS / Seurat Objects](../protocols/rds_seurat.md) | ⭐⭐ Easy–Medium |
| H5 | [H5 / CellRanger HDF5](../protocols/h5_cellranger.md) | ⭐⭐⭐ Medium |
| MTX | [MTX / 10x Sparse Matrices](../protocols/mtx_10x.md) | ⭐⭐⭐ Medium |

> **Protocol pages coming soon:** **BED / BigWig / Peak files** (BED, BEDGRAPH, BIGWIG, BROADPEAK, BW, NARROWPEAK, WIG).

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE304479](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE304479) | Copper control of the suppressive capacity in regulatory T cells [CUT&Tag] | Mus musculus | 14 | NARROWPEAK | 2026/04/03 |
| [GSE324283](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324283) | HIRA-mediated H3.3 deposition preserves hepatocyte cell identity during non-prol... | Mus musculus | 18 | BW | 2026/04/02 |
| [GSE320261](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320261) | Pan-Cancer Analysis Reveals Mutation-Driven TE Dysregulation as a Contributor to... | Homo sapiens | 3 | BW | 2026/04/01 |
| [GSE312506](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312506) | The deubiquitinase USP1 promotes the progression of AML by stabilizing ID1 [ID1 ... | Homo sapiens | 4 | BED, BW | 2026/04/01 |
| [GSE316882](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316882) | Autism-like phenotypes and increased NMDAR2D expression in mice with KDM5B histo... | Mus musculus | 6 | BEDGRAPH, BIGWIG | 2026/03/31 |
| [GSE295183](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295183) | HIF2ɑ Requires Engagement with YAP/TAZ and AP-1 Transcription Factors to Maintai... | Homo sapiens | 60 | BW | 2026/03/31 |
| [GSE277417](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE277417) | Non-canonical PRC1.1 licenses transcriptional response to enable Treg plasticity... | Homo sapiens; Mus musculus | 38 | BW | 2026/03/31 |
| [GSE314913](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314913) | FACT maintains nucleosomes around promoters and opposes to the spreading of chro... | Mus musculus | 36 | BW | 2026/03/30 |
| [GSE299350](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299350) | R-loops shape the H2A.Z landscape and promote balanced lineage allocation during... | Mus musculus | 10 | BEDGRAPH | 2026/03/30 |
| [GSE299115](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299115) | R-loops shape the H2A.Z landscape and promote balanced lineage allocation during... | Mus musculus | 56 | BED, BW, CSV | 2026/03/30 |
| [GSE325799](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325799) | KMT2C and KMT2D amplify GRHL2-driven enhancer activation [CUT&Tag] | Mus musculus | 80 | BW | 2026/03/28 |
| [GSE315190](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE315190) | Vitamin D Deficiency Activates Gdnf-Ret-pErk1/2 Signal and induces Kidney Malfor... | Mus musculus | 4 | XLSX | 2026/03/26 |
| [GSE310426](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310426) | Genome-wide Maps of Chromatin State in Control and DDX21-deficient Hematopoietic... | Mus musculus | 2 | BW | 2026/03/20 |
| [GSE262991](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262991) | Chronic stress induces neural stem cell quiescence in the hippocampus by repress... | Mus musculus | 2 | BW, NARROWPEAK | 2026/03/20 |
| [GSE325209](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325209) | Targeting branched-chain amino acids alleviates pulmonary fibrosis | Mus musculus | 6 | BW | 2026/03/18 |
| [GSE278361](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE278361) | DHX9 sustains hematopoietic stem cell function in cooperation with H3 acetylatio... | Mus musculus | 5 | BW | 2026/03/18 |
| [GSE325132](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325132) | SLC1A5 prevents aortic aneurysm and dissection by glutaminolytic-epigenetic orch... | Mus musculus | 8 | BW | 2026/03/17 |
| [GSE295425](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295425) | Targeting branched-chain amino acids alleviates pulmonary fibrosis [CUT&Tag, his... | Mus musculus | 20 | BW | 2026/03/17 |
| [GSE295424](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295424) | Targeting branched-chain amino acids alleviates pulmonary fibrosis [CUT&Tag] | Mus musculus | 6 | BW | 2026/03/17 |
| [GSE306768](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306768) | Glutamine Deprivation Triggers TRIB3-Dependent G4-DNA Resolution to Maintain DNA... | Homo sapiens | 18 | BW | 2026/03/13 |
| [GSE319239](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319239) | YY1 and ZFP384 CUT&Tag of BV2 cells and microglia after ischemic stroke | Mus musculus | 13 | BW | 2026/03/11 |
| [GSE313568](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313568) | p300-Mediated Histone H3K18 Lactylation Promotes Mitochondrial ROS Accumulation ... | Mus musculus | 4 | TXT | 2026/03/11 |
| [GSE294263](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294263) | CUT&Tag for AML cell line CMK | Homo sapiens | 14 | BW | 2026/03/11 |
| [GSE310734](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310734) | Wnt-materials sustain H3K14-acetylation in human skeletal stem cells for tissue ... | Homo sapiens | 12 | BW | 2026/03/09 |
| [GSE322715](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322715) | AP2Ⅺ-3 is critical for the cell cycle of Toxoplasma to progress through the G1 p... | Toxoplasma | 6 | BW | 2026/03/08 |
| [GSE317232](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317232) | Dual mechanisms for the antagonistic crosstalk between H3 glycation and H3K4me3 ... | Homo sapiens | 18 | BW | 2026/03/07 |
| [GSE291224](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291224) | AF9/KLF2 gene regulatory circuit links histone lactylation to breast cancer meta... | Homo sapiens | 22 | NARROWPEAK | 2026/03/03 |
| [GSE316695](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316695) | Gene syntax defines supercoiling-mediated transcriptional feedback [CUT&Tag II] | Homo sapiens | 64 | BW | 2026/03/02 |
| [GSE291664](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291664) | Lactate and histone H3K18 lactylation are associated with metabolic control of g... | Mus musculus | 7 | BED, BIGWIG, TSV, XLSX | 2026/03/02 |
| [GSE291663](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291663) | Lactate and histone H3K18 lactylation are associated with metabolic control of g... | Mus musculus | 10 | BIGWIG, TSV, XLSX | 2026/03/02 |
| [GSE296647](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296647) | Indirect identification of genomic G-quadruplexes via a small protein probe that... | Homo sapiens | 24 | BIGWIG | 2026/03/01 |
| [GSE290824](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290824) | Targeted genes of Isl1 in E13.5 mouse retina with CUT&Tag | Mus musculus | 2 | BED | 2026/02/27 |
| [GSE309203](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309203) | ZNF200 interacts with DDX17 to regulate the transcriptional activity of RBP-J. [... | Homo sapiens | 16 | BW | 2026/02/26 |
| [GSE279197](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE279197) | To explore MBD1-related ferroptosis targets | Homo sapiens | 1 | BW | 2026/02/25 |
| [GSE319889](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319889) | Transcriptional regulation by TES and TEAD1 in SNB19 glioblastoma cells: Cut&Tag | Homo sapiens | 8 | BW, NARROWPEAK | 2026/02/23 |
| [GSE311349](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311349) | Polycomb Repressive Complex 1 Primes Non-Growing Oocytes for Growth and Early Em... | Mus musculus | 32 | BED, BW | 2026/02/23 |
| [GSE310421](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310421) | Transcriptome-wide mapping reveals an RNA-dependent mechanism of platinum cancer... | Homo sapiens | 6 | BW, TXT | 2026/02/23 |
| [GSE309968](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309968) | CUT&Tag profiling of PARIS binding in CamK-PARIS mouse brain | Mus musculus | 2 | BED, BIGWIG, TXT | 2026/02/20 |
| [GSE317694](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317694) | Reporter-gene-assisted small molecule inhibitor screening of heterochromatin bou... | Plasmodium falciparum | 15 | BEDGRAPH | 2026/02/19 |
| [GSE287680](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE287680) | Sex-specific KDM6A-HNF4A-CREBH network controls lipoprotein cholesterol metaboli... | Homo sapiens | 22 | BIGWIG | 2026/02/19 |
| [GSE289683](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289683) | The iPSC-derived pulmonary epithilial cells in micro-patterned culture plate [CU... | Homo sapiens | 12 | BW | 2026/02/18 |
| [GSE297567](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297567) | The Conserved Non-Coding Sequence CNS11 Is A Master Control Region for Rorc Tran... | Mus musculus | 6 | BW | 2026/02/17 |
| [GSE307936](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307936) | PKM2 lactylation promotes colorectal cancer vasculogenic mimicry and resistance ... | Homo sapiens | 4 | XLSX | 2026/02/14 |
| [GSE318896](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE318896) | CUT&Tag profiling of Irx3 binding sites in AC16 cardiomyocytes supporting studie... | Homo sapiens | 3 | BED, NARROWPEAK | 2026/02/12 |
| [GSE306920](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306920) | Newly Evolved Endogenous Retroviruses Prime the Ovarian Reserve for Activation [... | Mus musculus | 22 | BW | 2026/02/12 |
| [GSE301206](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301206) | Histone lactylation-mediated metabolic remodeling in vascular smooth muscle cell... | Homo sapiens | 4 | BW | 2026/02/12 |
| [GSE295697](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295697) | RBM22 CUT&Tag Profiling of Regenerative (P1) and Non-Regenerative (P8) Neonatal ... | Mus musculus | 2 | BW | 2026/02/12 |
| [GSE292265](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292265) | Genetic deletion of RUNX1 or RUNX2 in adipocytes enhanced beige fat formation [C... | Mus musculus | 56 | BED, BW, NARROWPEAK, TXT | 2026/02/12 |
| [GSE280637](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE280637) | Epigenomic Roadmap of Ovarian Reserve Development: Polycomb-Mediated Programming... | Mus musculus | 30 | BED, BW | 2026/02/12 |
| [GSE306053](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306053) | INO80 regulates promoter-associated R-loops to coordinate transcription and main... | Mus musculus | 4 | BW | 2026/02/11 |

*...and 662 more datasets.*
