# DNA Methylation Profiling

> 7258 datasets | 2015/01/01 – 2026/04/08

All DNA methylation profiling datasets on GEO, including bisulfite sequencing (WGBS, RRBS), enzymatic methods (EM-seq), hydroxymethylation profiling (5hmC-seq), immunoprecipitation-based approaches (MeDIP-seq), and Illumina Infinium arrays (450K, EPIC). See individual assay pages for protocol-specific views.

## Organism Distribution

| Organism | Count |
|----------|------:|
| Homo sapiens | 3150 |
| Mus musculus | 2234 |
| Arabidopsis thaliana | 389 |
| Rattus norvegicus | 155 |
| Homo sapiens; Mus musculus | 108 |
| Danio rerio | 78 |
| Bos taurus | 76 |
| Mus musculus; Homo sapiens | 68 |
| Sus scrofa | 61 |
| Oryza sativa | 55 |
| Gallus gallus | 21 |
| Saccharomyces cerevisiae | 21 |
| Solanum lycopersicum | 20 |
| Drosophila melanogaster | 18 |
| Zea mays | 17 |

## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
| TXT | 3160 | Text files (methylation tables, coverage files, metadata) |
| IDAT | 1031 | Illumina array raw intensity data (450K / EPIC) |
| BW | 1019 | BigWig coverage / methylation tracks |
| BED | 924 | BED files (CpG methylation calls, DMR intervals) |
| TSV | 784 | Tab-separated methylation data |
| CSV | 574 | Comma-separated methylation data |
| BEDGRAPH | 508 | BedGraph methylation coverage |
| COV | 442 | Coverage / bismark bismark .cov files |
| BIGWIG | 359 | BigWig coverage / methylation tracks |
| XLSX | 358 | Excel (methylation tables, differential analysis) |
| WIG | 246 |  |
| NARROWPEAK | 163 |  |
| BIGBED | 140 |  |
| CEL | 96 |  |
| XLS | 87 |  |

## Analyzing These Datasets

| File Types | Protocol | Effort |
|------------|----------|--------|
| CSV, TAB, TSV, TXT, XLS, XLSX | [CSV / TSV Count Matrices](../protocols/csv_tsv_counts.md) | ⭐ Easy |
| RDA, RDATA, RDS | [RDS / Seurat Objects](../protocols/rds_seurat.md) | ⭐⭐ Easy–Medium |
| H5AD | [H5AD / AnnData (scanpy)](../protocols/h5ad_anndata.md) | ⭐⭐ Easy–Medium |
| H5 | [H5 / CellRanger HDF5](../protocols/h5_cellranger.md) | ⭐⭐⭐ Medium |
| MTX | [MTX / 10x Sparse Matrices](../protocols/mtx_10x.md) | ⭐⭐⭐ Medium |

> **Protocol pages coming soon:** **BED / BigWig / Peak files** (BED, BEDGRAPH, BIGWIG, BROADPEAK, BW, NARROWPEAK, WIG); **Bismark coverage / CpG call files** (COV); **IDAT (Illumina array raw intensities)** (IDAT).

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE272676](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE272676) | Mechanisms Underlying the Progression of Congenital Scoliosis Involving Bone Mar... | Homo sapiens | 13 | BW | 2026/04/08 |
| [GSE289742](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289742) | EPIMETRIC (EPIgenetic MEthylation-based Algorithm for Respiratory Illness Classi... | Homo sapiens | 128 | IDAT, TAB | 2026/04/07 |
| [GSE319118](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319118) | Simultaneous orthogonal cell engineering by a single CRISPR-Cas9 polyfunctional ... | Homo sapiens | 24 | COV | 2026/04/06 |
| [GSE293142](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293142) | Simultaneous orthogonal cell engineering by a single CRISPR-Cas9 polyfunctional ... | Homo sapiens | 17 | COV | 2026/04/06 |
| [GSE229140](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229140) | ROS1 regulates blueberry fruit ripening in a negatively ABA manner (WGBS) | Vaccinium corymbosum | 15 | CGMAP | 2026/04/06 |
| [GSE228952](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE228952) | Human bladder cancer tissues: tumor VS adjacent normal | Homo sapiens | 12 | TXT | 2026/04/05 |
| [GSE293143](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293143) | Simultaneous orthogonal cell engineering by a single CRISPR-Cas9 polyfunctional ... | Homo sapiens | 84 | COV, TXT | 2026/04/03 |
| [GSE326292](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326292) | Mitochondrial L-2-hydroxyglutarate is a physiologic signaling metabolite [mRRBS] | Mus musculus | 8 | COV | 2026/04/02 |
| [GSE320398](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320398) | Pan-Cancer Analysis Reveals Mutation-Driven TE Dysregulation as a Contributor to... | Homo sapiens | 28 | BW | 2026/04/01 |
| [GSE320262](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320262) | Pan-Cancer Analysis Reveals Mutation-Driven TE Dysregulation as a Contributor to... | Homo sapiens | 8 | BW | 2026/04/01 |
| [GSE318387](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE318387) | Promoter hypomethylation of cadherin-7: a novel epigenetic marker associated wit... | Homo sapiens | 32 | IDAT, TSV | 2026/04/01 |
| [GSE307211](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307211) | KDM5C and KDM5D influence DNA methylation in adult mouse liver | Mus musculus | 28 | TXT | 2026/04/01 |
| [GSE229883](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229883) | N6-methyladenosine (m6A) sequencing in mouse trophoblast stem cells (mTSCs) with... | Mus musculus | 6 | BIGWIG | 2026/04/01 |
| [GSE320000](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320000) | Alterations in gene expression and DNA methylation in the bovine blastocyst caus... | Bos taurus | 7 | TXT | 2026/03/31 |
| [GSE310508](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310508) | Cooperative care influences genome-wide levels of DNA methylation in nestling ch... | Pomatostomus ruficeps | 28 | CSV | 2026/03/31 |
| [GSE314295](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314295) | Identification of  Therapeutic Targets for Low-Grade Serous Ovarian Carcinoma [E... | Homo sapiens | 14 | CSV | 2026/03/30 |
| [GSE311005](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311005) | Integrated Multiomic Profiling Enhances Risk Stratification and Prognostication ... | Canis lupus familiaris | 61 | TXT | 2026/03/30 |
| [GSE205810](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205810) | Methylome analysis of HGG_F samples | Homo sapiens | 20 | IDAT, TXT | 2026/03/30 |
| [GSE325694](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325694) | Multi-omic analysis reveals brain-blood concordance and persistent neuroimmune r... | Mus musculus | 44 | TSV | 2026/03/27 |
| [GSE297847](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297847) | DNMT1 loss leads to hypermethylation of a subset of late replicating domains by ... | Homo sapiens | 42 | BIGWIG, COV, TXT | 2026/03/26 |
| [GSE297777](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297777) | DNMT1 loss leads to hypermethylation of a subset of late replicating domains by ... | Homo sapiens | 2 | BIGWIG, COV | 2026/03/26 |
| [GSE211070](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211070) | Multiplex Enhanced Reduced Representation Bisulfite Sequencing (mERRBS) Analysis... | Homo sapiens | 15 | TXT | 2026/03/26 |
| [GSE188327](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE188327) | Next Generation Sequencing of Transcriptomes from Murine Articular Chondrocytes ... | Mus musculus | 22 | BIGWIG | 2026/03/25 |
| [GSE188326](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE188326) | Next Generation Sequencing of Transcriptomes from Murine Articular Chondrocytes ... | Mus musculus | 9 | BIGWIG | 2026/03/25 |
| [GSE268414](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE268414) | Retrospective analysis reveals the early origin and development of pulmonary per... | Mus musculus | 37 | BW, MTX, TSV | 2026/03/23 |
| [GSE268412](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE268412) | Retrospective analysis reveals the early origin and development of pulmonary per... | Mus musculus | 30 | BW | 2026/03/23 |
| [GSE325146](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325146) | Targeted DNA methylation editing in vivo [mouse spleen] | Trametes gibbosa; Mus musculus | 12 | IDAT, TXT | 2026/03/22 |
| [GSE325144](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325144) | Targeted DNA methylation editing in vivo [mouse brain] | Mus musculus | 12 | IDAT, TXT | 2026/03/22 |
| [GSE312765](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312765) | whole-genome bisulfite sequencing (WGBS) of wild-type and Uhrf1-/- ESCs | Mus musculus | 8 | COV | 2026/03/21 |
| [GSE293557](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293557) | A nanovaccine targeting cancer stem cells and bulk cancer cells reduces post-sur... | Mus musculus | 4 | BED | 2026/03/21 |
| [GSE305349](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305349) | Epigenetic evolution of IDHwt glioblastomas | Homo sapiens | 64 | CSV, IDAT | 2026/03/19 |
| [GSE309819](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309819) | Nucleosome spacing regulates linker methylation by DNMT3A2/3B3 | synthetic construct | 40 | PILEUP, VCF | 2026/03/18 |
| [GSE285849](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285849) | Integrated clinical and molecular landscape of disseminated pediatric low-grade ... | Homo sapiens | 97 | CSV, IDAT | 2026/03/18 |
| [GSE285665](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285665) | Ancestral Bisphenol A Exposure Induces Sexually Dimorphic Nonalcoholic Fatty Liv... | Oryzias latipes | 24 | COV | 2026/03/18 |
| [GSE319319](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319319) | Xist RNA Dependent and Independent Mechanisms Regulate Dynamic X Chromosome Inac... | Mus musculus | 202 | BED, BEDGRAPH, BW | 2026/03/17 |
| [GSE282256](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282256) | Xist RNA Dependent and Independent Mechanisms Regulate Dynamic X Chromosome Inac... | Mus musculus | 6 | BEDGRAPH | 2026/03/17 |
| [GSE324619](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324619) | An atlas of genetic effects on the monocyte methylome across European and Africa... | Homo sapiens | 495 | TSV | 2026/03/16 |
| [GSE299606](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299606) | Unique sequence features define epigenetic longevity of inflammatory memory [Bis... | Mus musculus | 24 | BW | 2026/03/16 |
| [GSE296494](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296494) | Widespread non-Mendelian inheritance of DNA methylation patterns in mice [ONT Mu... | Mus musculus | 23 | BED | 2026/03/16 |
| [GSE324138](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324138) | A Comparative Analysis of the Methylation Status of Non-Coding RNA promoters in ... | Homo sapiens | 16 | TXT | 2026/03/15 |
| [GSE292304](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292304) | The m5C orchestrator NSUN7 drives SPARC/HMGB1 axis–mediated inflammation to exac... | Homo sapiens | 12 | XLSX | 2026/03/15 |
| [GSE266668](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE266668) | Widespread non-Mendelian inheritance of DNA methylation patterns in mice. | Mus musculus | 109 | BED, SF, TSV, TXT | 2026/03/14 |
| [GSE324175](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324175) | Prenatal Heat Calls Program DNA Methylation in the Embryonic Zebra Finch Brain | Taeniopygia guttata | 40 | TXT | 2026/03/13 |
| [GSE303826](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303826) | Identification and validation of liquid biopsy-based methylation biomarkers: a  ... | Homo sapiens | 17 | IDAT, TXT | 2026/03/13 |
| [GSE303825](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303825) | Identification and validation of liquid biopsy-based methylation biomarkers: a  ... | Homo sapiens | 54 | IDAT, TXT | 2026/03/13 |
| [GSE303824](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303824) | Identification and validation of liquid biopsy-based methylation biomarkers: a  ... | Homo sapiens | 16 | IDAT, TXT | 2026/03/13 |
| [GSE303400](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303400) | TET3-mediated DNA demethylation contributes to the formation of stable epiallele... | Solanum lycopersicum | 54 | BW, TSV | 2026/03/13 |
| [GSE314735](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314735) | Genome-wide methylation analysis identifies epigenetic differences in human ILC2... | Homo sapiens | 12 | CSV, PDF | 2026/03/12 |
| [GSE313891](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313891) | Genome-wide methylation analysis defines the epigenetic identity of human innate... | Homo sapiens | 12 | CSV, PDF | 2026/03/12 |
| [GSE311530](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311530) | Sir proteins impede, but do not prevent, access to silent chromatin in living Sa... | Saccharomyces cerevisiae | 62 | BW | 2026/03/12 |

*...and 7208 more datasets.*
