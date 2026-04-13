# WGBS (Whole Genome Bisulfite Sequencing)

> 1240 datasets | 2015/01/01 – 2026/04/08

Whole Genome Bisulfite Sequencing (WGBS). Provides single-base resolution methylation maps across the entire genome by treating DNA with sodium bisulfite (which converts unmethylated cytosines to uracil) before sequencing. Supplementary files typically include CpG methylation calls (BED, BedGraph, TXT) and coverage tracks (BigWig).

## Organism Distribution

| Organism | Count |
|----------|------:|
| Mus musculus | 444 |
| Homo sapiens | 369 |
| Arabidopsis thaliana | 118 |
| Oryza sativa | 24 |
| Bos taurus | 21 |
| Homo sapiens; Mus musculus | 17 |
| Danio rerio | 16 |
| Sus scrofa | 14 |
| Rattus norvegicus | 11 |
| Gallus gallus | 6 |
| Canis lupus familiaris | 6 |
| Oryzias latipes | 5 |
| Ovis aries | 5 |
| Solanum lycopersicum | 5 |
| Mus musculus; Homo sapiens | 4 |

## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
| TXT | 587 | Text files (methylation tables, coverage files, metadata) |
| BED | 258 | BED files (CpG methylation calls, DMR intervals) |
| BW | 191 | BigWig coverage / methylation tracks |
| BIGWIG | 162 | BigWig coverage / methylation tracks |
| BIGBED | 132 |  |
| BEDGRAPH | 114 | BedGraph methylation coverage |
| COV | 110 | Coverage / bismark bismark .cov files |
| TSV | 65 | Tab-separated methylation data |
| CSV | 42 | Comma-separated methylation data |
| XLSX | 41 | Excel (methylation tables, differential analysis) |
| WIG | 31 |  |
| CGMAP | 18 |  |
| TDF | 17 |  |
| TAB | 15 |  |
| GFF | 12 |  |

## Analyzing These Datasets

| File Types | Protocol | Effort |
|------------|----------|--------|
| CSV, TAB, TSV, TXT, XLS, XLSX | [CSV / TSV Count Matrices](../protocols/csv_tsv_counts.md) | ⭐ Easy |
| RDA, RDS | [RDS / Seurat Objects](../protocols/rds_seurat.md) | ⭐⭐ Easy–Medium |
| H5 | [H5 / CellRanger HDF5](../protocols/h5_cellranger.md) | ⭐⭐⭐ Medium |
| MTX | [MTX / 10x Sparse Matrices](../protocols/mtx_10x.md) | ⭐⭐⭐ Medium |

> **Protocol pages coming soon:** **BED / BigWig / Peak files** (BED, BEDGRAPH, BIGWIG, BROADPEAK, BW, NARROWPEAK, WIG); **Bismark coverage / CpG call files** (COV).

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE272676](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE272676) | Mechanisms Underlying the Progression of Congenital Scoliosis Involving Bone Mar... | Homo sapiens | 13 | BW | 2026/04/08 |
| [GSE319118](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319118) | Simultaneous orthogonal cell engineering by a single CRISPR-Cas9 polyfunctional ... | Homo sapiens | 24 | COV | 2026/04/06 |
| [GSE293142](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293142) | Simultaneous orthogonal cell engineering by a single CRISPR-Cas9 polyfunctional ... | Homo sapiens | 17 | COV | 2026/04/06 |
| [GSE229140](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229140) | ROS1 regulates blueberry fruit ripening in a negatively ABA manner (WGBS) | Vaccinium corymbosum | 15 | CGMAP | 2026/04/06 |
| [GSE320262](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320262) | Pan-Cancer Analysis Reveals Mutation-Driven TE Dysregulation as a Contributor to... | Homo sapiens | 8 | BW | 2026/04/01 |
| [GSE307211](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307211) | KDM5C and KDM5D influence DNA methylation in adult mouse liver | Mus musculus | 28 | TXT | 2026/04/01 |
| [GSE310508](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310508) | Cooperative care influences genome-wide levels of DNA methylation in nestling ch... | Pomatostomus ruficeps | 28 | CSV | 2026/03/31 |
| [GSE297777](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297777) | DNMT1 loss leads to hypermethylation of a subset of late replicating domains by ... | Homo sapiens | 2 | BIGWIG, COV | 2026/03/26 |
| [GSE312765](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312765) | whole-genome bisulfite sequencing (WGBS) of wild-type and Uhrf1-/- ESCs | Mus musculus | 8 | COV | 2026/03/21 |
| [GSE285665](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285665) | Ancestral Bisphenol A Exposure Induces Sexually Dimorphic Nonalcoholic Fatty Liv... | Oryzias latipes | 24 | COV | 2026/03/18 |
| [GSE282256](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282256) | Xist RNA Dependent and Independent Mechanisms Regulate Dynamic X Chromosome Inac... | Mus musculus | 6 | BEDGRAPH | 2026/03/17 |
| [GSE324619](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324619) | An atlas of genetic effects on the monocyte methylome across European and Africa... | Homo sapiens | 495 | TSV | 2026/03/16 |
| [GSE299606](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299606) | Unique sequence features define epigenetic longevity of inflammatory memory [Bis... | Mus musculus | 24 | BW | 2026/03/16 |
| [GSE303400](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303400) | TET3-mediated DNA demethylation contributes to the formation of stable epiallele... | Solanum lycopersicum | 54 | BW, TSV | 2026/03/13 |
| [GSE324116](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324116) | Wollemia nobilis methylation sequencing | Wollemia nobilis | 2 | BED | 2026/03/11 |
| [GSE322759](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322759) | Whole-Genome Bisulfite Sequencing (WGBS) Analysis of Tail Tip Tissues from F2 Ge... | Mus musculus | 4 | TXT | 2026/03/08 |
| [GSE298943](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE298943) | Discovery of a Novel DNMT1 Inhibitor with Improved Efficacy in Treating β-Thalas... | Homo sapiens | 2 | COV | 2026/03/04 |
| [GSE298431](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE298431) | Establishment of Human Formative Pluripotent Stem Cell Like Cells Exhibiting Amn... | Homo sapiens | 2 | BW | 2026/03/01 |
| [GSE225961](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225961) | Systemic acquired adaptation induced by mito-stress (WGBS) | Arabidopsis thaliana | 2 | TXT | 2026/02/28 |
| [GSE255302](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE255302) | Genomics Analysis of met1-derived epiRILs [BiSulfite-seq] | Arabidopsis thaliana | 77 | TXT | 2026/02/25 |
| [GSE319533](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319533) | Whole-Genome Bisulfite Sequencing Reveals Formaldehyde-Induced DNA Methylation A... | Gallus gallus | 16 | BW | 2026/02/18 |
| [GSE126437](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126437) | Timecourse of Chromium exposure (Bisulfite-Seq) | Homo sapiens | 15 | TXT | 2026/02/14 |
| [GSE189768](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE189768) | A Dominant mutation in Dnmt1 leads epigenetic changes (RNA-BS-seq) | Mus musculus | 4 | COV | 2026/02/12 |
| [GSE282073](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282073) | Diverse Roles of Arabidopsis ROS1 in Regulating Chromatin Accessibility and DNA ... | Arabidopsis thaliana | 15 | BW | 2026/02/06 |
| [GSE275219](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE275219) | Weaning-Driven Gut Microbiome Shapes Intestinal Stem Cell Epigenetics to Train I... | Mus musculus | 20 | XLSX | 2026/02/06 |
| [GSE291574](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291574) | Long-distance transport of siRNAs with functional roles in pollen development [B... | Capsella rubella | 24 | TXT | 2026/02/02 |
| [GSE231658](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE231658) | Convergence of aging- and rejuvenation-related epigenetic alterations on PRC2 ta... | Mus musculus | 22 | BW | 2026/02/02 |
| [GSE316331](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316331) | S-adenosylhomocysteine hydrolase deficiency exacerbates clonal 1 hematopoiesis a... | Mus musculus | 6 | TXT | 2026/01/31 |
| [GSE317052](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317052) | DNA methylation analysis of the Parkin gene in wild-type and TIGAR-deficient mou... | Mus musculus | 4 | BEDGRAPH | 2026/01/30 |
| [GSE310855](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310855) | Distinct Control of Histone H1 Expression within the Histone Locus Body by CRAMP... | Homo sapiens | 3 | COV | 2026/01/30 |
| [GSE295869](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295869) | Dnmt1 mediates epigenetic restriction of invasive traits in clonal crayfish [BiS... | Procambarus virginalis | 4 | TXT | 2026/01/29 |
| [GSE290278](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290278) | A plant histone H3.3-specific amino acid safeguards the deposition of H3K36 meth... | Arabidopsis thaliana | 14 | TXT | 2026/01/29 |
| [GSE309064](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309064) | BMX-001, a selective radioprotector in phase II clinical trials, can reverse rad... | Mus musculus | 12 | TSV | 2026/01/28 |
| [GSE310160](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310160) | Embryonic stem cell factors DPPA2/4 amplify active H3K4me3-H2AK119ub chromatin d... | Homo sapiens | 18 | BEDGRAPH, BW, COV | 2026/01/20 |
| [GSE301728](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301728) | Methylation variability and LINE-1 activation in multiple myeloma [WGBS] | Homo sapiens | 15 | BW | 2026/01/20 |
| [GSE312070](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312070) | Allelic chromatin structure is a pervasive feature of imprinted domains and func... | Mus musculus | 6 | TXT | 2026/01/13 |
| [GSE297432](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297432) | Systemic comparison  of dCas9-based DNA methylation editing systems for specific... | Homo sapiens | 95 | CSV | 2026/01/13 |
| [GSE297389](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297389) | Systemic comparison  of dCas9-based DNA methylation editing systems for specific... | Homo sapiens | 30 | CSV | 2026/01/13 |
| [GSE307897](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307897) | Whole-genome bisulfite sequencing (WGBS) for LKB1 overexpressing and NNMT knockd... | Homo sapiens | 8 | TXT | 2025/12/31 |
| [GSE300000](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE300000) | Tet2 and Tp53 cooperate to promote leukemia and modulate response to inflammatio... | Mus musculus | 7 | WIG | 2025/12/31 |
| [GSE313872](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313872) | Genome-scale DNA methylome and transcriptome profiling of midgut of Bombyx mori ... | Bombyx mori | 8 | BW | 2025/12/25 |
| [GSE285260](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285260) | Characterizing the expression, binding and function properties of Methyl-CpG-bin... | Solanum lycopersicum | 6 | BW | 2025/12/22 |
| [GSE180571](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE180571) | Studies on genomic imprinting in preimplantation embryos of non-human primates [... | Macaca mulatta | 5 | COV | 2025/12/22 |
| [GSE289850](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289850) | Whole-genome bisulfite sequencing of whole blood cells in dog lymphomas cases | Canis lupus familiaris | 20 | TDF | 2025/12/16 |
| [GSE165094](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE165094) | Whole genome bisulfite sequencing of peach fruits | Prunus persica | 12 | BW | 2025/12/11 |
| [GSE109189](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109189) | Whole genome bisulfite sequencing of pear fruits | Pyrus x bretschneideri | 8 |  | 2025/12/11 |
| [GSE109188](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109188) | Whole genome bisulfite sequencing of apple fruits | Malus domestica | 8 |  | 2025/12/11 |
| [GSE311296](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311296) | DNA methylation mediates transcriptional stability and transposon-driven trans-r... | Triticum aestivum | 2 | TXT | 2025/12/04 |
| [GSE252313](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE252313) | Novel culture systems for naive human embryonic stem cells  based on chemical mo... | Homo sapiens | 10 | TXT | 2025/12/01 |
| [GSE168398](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE168398) | De novo methylation enforces long-term lineage-specific programing of TFH and TH... | Mus musculus | 10 | BED | 2025/12/01 |

*...and 1190 more datasets.*
