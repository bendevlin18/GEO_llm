# ChIP-seq

> 35540 datasets | 2015/01/01 – 2026/04/08

Chromatin immunoprecipitation followed by sequencing (ChIP-seq). Profiles histone modification marks, transcription factor binding sites, and chromatin-associated proteins genome-wide. Supplementary files typically include peak calls (BED, narrowPeak, broadPeak) and coverage tracks (BigWig).

## Target Type Breakdown

| Target Type | Count | Description |
|-------------|------:|-------------|
| tf | 18040 | Transcription factor binding sites |
| other | 11575 | Chromatin structural proteins (CTCF, cohesin, Pol2, etc.) |
| histone | 5925 | Histone modification marks (H3K27ac, H3K4me3, H3K27me3, etc.) |

## Organism Distribution

| Organism | Count |
|----------|------:|
| Homo sapiens | 18424 |
| Mus musculus | 9048 |
| Drosophila melanogaster | 1928 |
| Caenorhabditis elegans | 1409 |
| Saccharomyces cerevisiae | 621 |
| Arabidopsis thaliana | 619 |
| Homo sapiens; Mus musculus | 534 |
| Mus musculus; Homo sapiens | 332 |
| Schizosaccharomyces pombe | 201 |
| Rattus norvegicus | 171 |
| Danio rerio | 112 |
| Oryza sativa | 81 |
| Gallus gallus | 70 |
| Plasmodium falciparum | 62 |
| Zea mays | 47 |

## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
| TXT | 18499 | Text files (peak lists, count tables, metadata) |
| BED | 14872 | BED peak calls (genomic intervals) |
| BIGWIG | 13652 | BigWig coverage tracks |
| BIGBED | 9933 |  |
| BW | 9619 | BigWig coverage tracks |
| NARROWPEAK | 2550 | ENCODE narrowPeak format (TF / sharp peaks) |
| BEDGRAPH | 2072 | BedGraph coverage files |
| TSV | 1390 | Tab-separated data |
| WIG | 1329 | Wiggle coverage format |
| STARCH | 1084 |  |
| CSV | 920 | Comma-separated data |
| XLSX | 777 |  |
| BROADPEAK | 698 | ENCODE broadPeak format (histone / broad marks) |
| MTX | 611 |  |
| TDF | 425 |  |

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
| [GSE327055](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327055) | LncRNA Gas5 directs SUV39H2 to establish heterochromatin and maintain genome sta... | Mus musculus | 14 | BW, TAB | 2026/04/08 |
| [GSE326768](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326768) | Evidence for coordinate epigenomic roles for CTCF and histone H3.3 in K27M diffu... | Homo sapiens | 2 | NARROWPEAK | 2026/04/08 |
| [GSE307601](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307601) | NAT10-Dependent N4-acetylcytidine (ac4C) on R-loops Drive Glioblastoma Tumorigen... | Homo sapiens | 38 | BW | 2026/04/08 |
| [GSE296815](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296815) | Polycomb Chromatin Topology Enables Long-Range Enhancer Recruitment during Crani... | Mus musculus | 98 | BW, HIC, TXT, WIG | 2026/04/08 |
| [GSE295340](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295340) | Polycomb Chromatin Topology Enables Long-Range Enhancer Recruitment during Crani... | Mus musculus | 42 | BW, WIG | 2026/04/08 |
| [GSE327100](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327100) | Mesenchymal stem cell–derived extracellular vesicles alleviate immunoparalysis i... | Homo sapiens | 8 | BEDGRAPH, TXT | 2026/04/07 |
| [GSE327017](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327017) | Multimodal profiling reveals a Notch-responsive regenerative subpopulation of co... | Mus musculus | 14 |  | 2026/04/07 |
| [GSE317671](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317671) | Pediatric Cancer Dependencies Accelerator | Homo sapiens | 19 | BW, HIC | 2026/04/07 |
| [GSE295585](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295585) | Sirtuin 7 regulates dosage compensation and safeguards the female X-chromosome [... | Mus musculus | 8 | BW | 2026/04/07 |
| [GSE295584](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295584) | Sirtuin 7 regulates dosage compensation and safeguards the female X-chromosome [... | Mus musculus | 12 | BW | 2026/04/07 |
| [GSE295583](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295583) | Sirtuin 7 regulates dosage compensation and safeguards the female X-chromosome [... | Mus musculus | 24 | BROADPEAK, TSV | 2026/04/07 |
| [GSE295582](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295582) | Sirtuin 7 regulates dosage compensation and safeguards the female X-chromosome [... | Mus musculus | 24 | BROADPEAK, TSV | 2026/04/07 |
| [GSE293974](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293974) | Spatially resolved profiling and Footprint Analysis of the Steroid Nuclear Recep... | Homo sapiens; Mus musculus; Saccharomyces cerevisiae | 180 | BW, TXT | 2026/04/07 |
| [GSE256283](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE256283) | Sirtuin 7 regulates dosage compensation and safeguards the female X-chromosome [... | Mus musculus | 5 | TSV | 2026/04/07 |
| [GSE256282](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE256282) | Sirtuin 7 regulates dosage compensation and safeguards the female X-chromosome [... | Mus musculus | 20 | BROADPEAK, BW | 2026/04/07 |
| [GSE256281](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE256281) | Sirtuin 7 regulates dosage compensation and safeguards the female X-chromosome [... | Mus musculus | 16 | BROADPEAK, BW | 2026/04/07 |
| [GSE256279](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE256279) | Sirtuin 7 regulates dosage compensation and safeguards the female X-chromosome [... | Mus musculus | 8 | BW | 2026/04/07 |
| [GSE256278](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE256278) | Sirtuin 7 regulates dosage compensation and safeguards the female X-chromosome [... | Mus musculus | 16 | BROADPEAK, BW | 2026/04/07 |
| [GSE243355](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE243355) | A novel triple-action Pt(IV) prodrug presents multiple anti-cancer effects and o... | Homo sapiens | 10 | BW | 2026/04/07 |
| [GSE309806](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309806) | MRE11 proximal polyadenylation site-mediated looping impacts transcription and g... | Homo sapiens | 15 | BW | 2026/04/06 |
| [GSE298229](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE298229) | The PLAGL1-KLF4-IRX5 axis promotes the osteogenesis of periosteal progenitors du... | Mus musculus | 9 | XLSX | 2026/04/06 |
| [GSE291272](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291272) | The placentalia specific histone H3.4 promotes germ cell development and reprodu... | Mus musculus | 41 | BW | 2026/04/06 |
| [GSE301970](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301970) | Multiome analysis of Kras-mutant intestinal epithelium 10 days post-recombinatio... | Mus musculus | 20 | H5, TSV | 2026/04/05 |
| [GSE301967](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301967) | Multiome analysis of tumors isolated from Apc cKO; Kras-mutant animals | Mus musculus | 12 | H5, TSV | 2026/04/05 |
| [GSE293892](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293892) | HDAC5 Deficiency Induces Intrinsic Resistance to KRASG12D Inhibition by Disrupti... | Homo sapiens | 3 | BW | 2026/04/05 |
| [GSE291274](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291274) | The placentalia specific histone H3.4 promotes germ cell development and reprodu... | Mus musculus | 167 | BW | 2026/04/05 |
| [GSE283000](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE283000) | Chromatin binding of nuclear transport factor Importin α in human cultured cance... | Homo sapiens | 3 | BW | 2026/04/05 |
| [GSE326310](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326310) | EpCAM identifies a developmentally poised DN thymocyte subset that drives T-cell... | Mus musculus | 4 | NARROWPEAK | 2026/04/04 |
| [GSE326616](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326616) | Aldosterone-induced gene expression changes in the brain | Mus musculus | 12 | H5, TSV | 2026/04/03 |
| [GSE326424](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326424) | Aldosterone-induced gene expression changes in the brain [Multiomic] | Mus musculus | 8 | H5, TSV | 2026/04/03 |
| [GSE325163](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325163) | Nuclear envelope rupture causes RNA polymerase loss in LMNA cardiomyopathy | Mus musculus | 12 | BW | 2026/04/03 |
| [GSE281482](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE281482) | Single-cell multi-omic analysis of post-transplant mesenchymal cells reveals mol... | Homo sapiens | 8 | H5 | 2026/04/03 |
| [GSE176375](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE176375) | The genomic landscape of HSF1 binding in beige adipocytes. | Mus musculus | 2 | BW | 2026/04/03 |
| [GSE326893](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326893) | SPECIFIC REACTIVITY OF ABASIC SITES WITH POLYAMINES ENABLES THEIR GENOMIC MAPPIN... | Homo sapiens | 48 | BIGWIG | 2026/04/02 |
| [GSE324042](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324042) | HIRA-mediated H3.3 deposition preserves hepatocyte cell identity during non-prol... | Mus musculus | 2 | BW | 2026/04/02 |
| [GSE313488](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313488) | “Zipper” Grammar of CTD Governs the Spatial Programing of the Transcription Cycl... | Homo sapiens | 10 | BW | 2026/04/02 |
| [GSE299967](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299967) | AATF supports proliferation of glioblastoma cells by sustaining mitochondrial re... | Homo sapiens | 2 | BIGWIG, BROADPEAK | 2026/04/02 |
| [GSE293544](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293544) | CUX1 Manifests Species-Dependent Regulation in Controlling Adipocyte Differentia... | Mus musculus; Homo sapiens | 6 | BW | 2026/04/02 |
| [GSE293156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293156) | Noncanonical PRC1.1 Targets BTG2 to Retain Cyclin Gene Expression and Cell Growt... | Homo sapiens | 4 | BW | 2026/04/02 |
| [GSE282341](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282341) | Identification of GLIS2 direct target genes in kidney | Mus musculus | 2 | BIGWIG, TXT | 2026/04/02 |
| [GSE273473](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE273473) | Mitochondrial L-2-hydroxyglutarate is a physiologic signaling metabolite [ChIP-s... | Mus musculus | 14 | BW | 2026/04/02 |
| [GSE324208](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324208) | Epigenetic reprogramming drives cellular and phenotypic plasticity in liposarcom... | Homo sapiens | 42 | CSV, H5, TBI, TSV, TXT | 2026/04/01 |
| [GSE322777](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322777) | ChIP-seq of RNA polymerase II and HNF4alpha in mouse liver after cytokine stimul... | Mus musculus | 9 | BED, XLS | 2026/04/01 |
| [GSE320398](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320398) | Pan-Cancer Analysis Reveals Mutation-Driven TE Dysregulation as a Contributor to... | Homo sapiens | 28 | BW | 2026/04/01 |
| [GSE311053](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311053) | SIRT1 is a therapeutic target of brain metabolic and developmental consequences ... | Mus musculus | 13 | BW, XLSX | 2026/04/01 |
| [GSE305296](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305296) | Activation of the aryl hydrocarbon receptor in human melanoma cells enhances can... | Homo sapiens | 43 | BW | 2026/04/01 |
| [GSE305225](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305225) | Plant-specific function of H3K9me3 as a permissive chromatin mark during Arabido... | Arabidopsis thaliana | 19 | BW | 2026/04/01 |
| [GSE304148](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE304148) | Activation of the aryl hydrocarbon receptor in human melanoma cells enhances can... | Homo sapiens | 9 | BW | 2026/04/01 |
| [GSE300270](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE300270) | Loss of WWOX Drives Cutaneous Squamous Cell Carcinoma (cSCC) through Regulating ... | Homo sapiens; Mus musculus | 24 | BIGWIG | 2026/04/01 |
| [GSE299484](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299484) | DOT1L enhances BLM-induced pulmonary fibrosis by inducing endothelial-to-mesench... | Homo sapiens | 4 | BW | 2026/04/01 |

*...and 35490 more datasets.*
