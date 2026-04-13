# Methylation Arrays (450K / EPIC)

> 1347 datasets | 2015/01/01 – 2026/04/08

Illumina Infinium methylation arrays, including the 27K, 450K (HumanMethylation450), and EPIC (850K) platforms. Measure methylation beta-values at hundreds of thousands of CpG sites. Widely used in epigenome-wide association studies (EWAS) and clinical research. Supplementary files often include IDAT files (raw intensities) or processed beta-value matrices (CSV, TXT, RDS).

## Organism Distribution

| Organism | Count |
|----------|------:|
| Homo sapiens | 1178 |
| Mus musculus | 59 |
| Rattus norvegicus | 16 |
| Bos taurus | 8 |
| Homo sapiens; Mus musculus; Rattus norvegicus | 8 |
| Homo sapiens; Mus musculus | 6 |
| Mus musculus; Homo sapiens | 6 |
| Sus scrofa | 6 |
| Macaca mulatta; Homo sapiens | 5 |
| Mus musculus; Rattus norvegicus; Homo sapiens | 4 |
| Rattus norvegicus; Homo sapiens; Mus musculus | 3 |
| Homo sapiens; Papio sp. | 2 |
| Rattus norvegicus; Mus musculus; Homo sapiens | 2 |
| Homo sapiens; Rattus norvegicus; Mus musculus | 2 |
| Pan troglodytes; Homo sapiens | 1 |

## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
| IDAT | 999 | Illumina array raw intensity data (450K / EPIC) |
| TXT | 695 | Text files (methylation tables, coverage files, metadata) |
| CSV | 211 | Comma-separated methylation data |
| CEL | 41 |  |
| XLSX | 41 | Excel (methylation tables, differential analysis) |
| TSV | 32 | Tab-separated methylation data |
| DOCX | 20 |  |
| BW | 16 | BigWig coverage / methylation tracks |
| NARROWPEAK | 14 |  |
| BED | 12 | BED files (CpG methylation calls, DMR intervals) |
| PAIR | 10 |  |
| CHP | 6 |  |
| BEDGRAPH | 6 | BedGraph methylation coverage |
| BIGWIG | 5 | BigWig coverage / methylation tracks |
| GFF | 5 |  |

## Analyzing These Datasets

| File Types | Protocol | Effort |
|------------|----------|--------|
| CSV, TAB, TSV, TXT, XLS, XLSX | [CSV / TSV Count Matrices](../protocols/csv_tsv_counts.md) | ⭐ Easy |
| RDATA, RDS | [RDS / Seurat Objects](../protocols/rds_seurat.md) | ⭐⭐ Easy–Medium |
| MTX | [MTX / 10x Sparse Matrices](../protocols/mtx_10x.md) | ⭐⭐⭐ Medium |

> **Protocol pages coming soon:** **BED / BigWig / Peak files** (BED, BEDGRAPH, BIGWIG, BROADPEAK, BW, NARROWPEAK, WIG); **Bismark coverage / CpG call files** (COV); **IDAT (Illumina array raw intensities)** (IDAT).

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE289742](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289742) | EPIMETRIC (EPIgenetic MEthylation-based Algorithm for Respiratory Illness Classi... | Homo sapiens | 128 | IDAT, TAB | 2026/04/07 |
| [GSE228952](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE228952) | Human bladder cancer tissues: tumor VS adjacent normal | Homo sapiens | 12 | TXT | 2026/04/05 |
| [GSE318387](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE318387) | Promoter hypomethylation of cadherin-7: a novel epigenetic marker associated wit... | Homo sapiens | 32 | IDAT, TSV | 2026/04/01 |
| [GSE205810](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205810) | Methylome analysis of HGG_F samples | Homo sapiens | 20 | IDAT, TXT | 2026/03/30 |
| [GSE325146](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325146) | Targeted DNA methylation editing in vivo [mouse spleen] | Trametes gibbosa; Mus musculus | 12 | IDAT, TXT | 2026/03/22 |
| [GSE325144](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325144) | Targeted DNA methylation editing in vivo [mouse brain] | Mus musculus | 12 | IDAT, TXT | 2026/03/22 |
| [GSE305349](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305349) | Epigenetic evolution of IDHwt glioblastomas | Homo sapiens | 64 | CSV, IDAT | 2026/03/19 |
| [GSE285849](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285849) | Integrated clinical and molecular landscape of disseminated pediatric low-grade ... | Homo sapiens | 97 | CSV, IDAT | 2026/03/18 |
| [GSE324138](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324138) | A Comparative Analysis of the Methylation Status of Non-Coding RNA promoters in ... | Homo sapiens | 16 | TXT | 2026/03/15 |
| [GSE303826](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303826) | Identification and validation of liquid biopsy-based methylation biomarkers: a  ... | Homo sapiens | 17 | IDAT, TXT | 2026/03/13 |
| [GSE303825](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303825) | Identification and validation of liquid biopsy-based methylation biomarkers: a  ... | Homo sapiens | 54 | IDAT, TXT | 2026/03/13 |
| [GSE303824](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303824) | Identification and validation of liquid biopsy-based methylation biomarkers: a  ... | Homo sapiens | 16 | IDAT, TXT | 2026/03/13 |
| [GSE228867](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE228867) | Epigenome analysis of control-siRNA and PHGDH-siRNA treated Human Immortalized E... | Homo sapiens | 4 | IDAT, XLSX | 2026/02/26 |
| [GSE319589](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319589) | Maternal Inflammation Alters Nuclear and Mitochondrial DNA Methylation Patterns ... | Mus musculus | 12 | CSV, IDAT | 2026/02/19 |
| [GSE290136](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290136) | Methylation profiling of BRAF-altered pediatric low-grade gliomas | Homo sapiens | 87 | CSV, IDAT | 2026/02/19 |
| [GSE289869](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289869) | Genome-wide methylation analysis of pterygium in Indian population | Homo sapiens | 15 | CSV, IDAT | 2026/02/15 |
| [GSE314658](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314658) | Genome-wide DNA methylation analysis of placentas from pregnancies complicated b... | Homo sapiens | 16 | CSV, IDAT | 2026/02/11 |
| [GSE311289](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311289) | Multi-omics Analysis Revealed Unique Features of Age-associated Type2 CD8 Memory... | Homo sapiens | 20 | CSV, IDAT | 2026/02/11 |
| [GSE286743](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286743) | H3K27-mutant diffuse hemispheric glioma presenting typical molecular features of... | Homo sapiens | 1 | IDAT, XLSX | 2025/12/31 |
| [GSE229984](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229984) | Attenuation of DNMT1-mediated DNA methylation upregulates CYP11A1 expression in ... | Homo sapiens | 8 | IDAT, TXT | 2025/12/31 |
| [GSE288652](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288652) | Genome wide DNA methylation of colon low grade and high grade adenoma | Homo sapiens | 32 | IDAT, TXT | 2025/12/18 |
| [GSE310390](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310390) | Adipose tissue-derived microRNAs as epigenetic modulators of type 2 diabetes | Mus musculus | 12 | IDAT, XLSX | 2025/12/17 |
| [GSE308675](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308675) | Lactate Is a Metabolic–Epigenetic Signal That Links HIIT to miRNA-Centered Remod... | Mus musculus | 28 | CSV, IDAT | 2025/12/17 |
| [GSE293262](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293262) | Genome-wide DNA Methylation Profiling in Methamphetamine Addiction | Homo sapiens | 8 | CSV, IDAT, XLSX | 2025/12/17 |
| [GSE289021](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289021) | Differential DNA methylation in infants with Ig E mediated and non-Ig E mediated... | Homo sapiens | 32 | IDAT, TXT | 2025/12/17 |
| [GSE222549](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE222549) | Generation and characterisation of a preclinical model of IDH-mutant astrocytoma | Mus musculus | 51 | IDAT, TXT, ZIP | 2025/12/01 |
| [GSE283386](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE283386) | DNA methylation analysis of colonic epithelial cells from 5-AZA and DSS treated ... | Mus musculus | 12 | CSV, IDAT | 2025/11/30 |
| [GSE279837](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE279837) | Reappraisal of Soft Tissue Myoepithelial Tumors by DNA Methylation Profiling Rev... | Homo sapiens | 30 | CSV, IDAT | 2025/11/30 |
| [GSE310605](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310605) | UHRF1 Deficiency Exacerbates Intestinal Inflammation by Epigenetic Modulation of... | Homo sapiens | 2 | CSV, IDAT | 2025/11/22 |
| [GSE290457](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290457) | Interferon signaling underlies radiotherapy responses in malignant peripheral ne... | Homo sapiens | 7 | IDAT, TXT | 2025/11/22 |
| [GSE294234](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294234) | Genome-wide methylation profiles of post-mortem tissue samples (human) | Homo sapiens | 3 | IDAT, TXT, XLSX | 2025/11/06 |
| [GSE281062](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE281062) | Methylation Array Signals are Predictive of Chronological Age Without Bisulfite ... | Mus musculus | 93 | CSV, IDAT | 2025/11/04 |
| [GSE280730](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE280730) | Oligoastrocytoma consisting of IDH-mutant 1p/19q-codeleted oligodendroglioma and... | Homo sapiens | 2 | IDAT, TXT, XLSX | 2025/10/31 |
| [GSE307696](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307696) | Epigenomic analysis of human advanced heart failure | Homo sapiens | 17 | IDAT, TXT | 2025/10/22 |
| [GSE286412](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286412) | Multi-modal Omics Analysis of a Paediatric Melanoma Highlights Mechanisms Underl... | Homo sapiens | 3 | IDAT, TXT | 2025/10/20 |
| [GSE237433](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE237433) | DNA-hypermethylated human gastric cancer circumvents apoptosis and premature sen... | Homo sapiens | 6 | IDAT, TXT | 2025/10/02 |
| [GSE52423](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52423) | Integrative Epigenomic and Genomic Profiling of HCC Patients to Identify Key Dri... | Homo sapiens | 128 | TXT | 2025/10/01 |
| [GSE253176](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE253176) | DNA methylation patterns facilitate tracing the origin of neuroendocrine neoplas... | Homo sapiens | 198 | IDAT, TXT | 2025/09/29 |
| [GSE308997](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308997) | Methylation profiling of PDX-AML samples using Illumina Infinium MethylationEPIC... | Homo sapiens | 25 | IDAT, TXT | 2025/09/25 |
| [GSE277537](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE277537) | The Effect of Methyl Donors in a Murine Model of MASLD in a Multidisciplinary St... | Mus musculus | 9 | CSV, IDAT, TXT | 2025/09/23 |
| [GSE308297](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308297) | A Ternary-code DNA Methylome Atlas of Mouse Tissues | Mus musculus | 4 | COV | 2025/09/17 |
| [GSE289990](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289990) | Comparative DNA methylation profiling of human and murine ALK-positive B-cell ne... | Mus musculus | 15 | IDAT, TXT | 2025/09/10 |
| [GSE289988](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289988) | Comparative DNA methylation profiling of human and murine ALK-positive B-cell ne... | Homo sapiens | 9 | IDAT, TXT | 2025/09/10 |
| [GSE306846](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306846) | The Effect of Epstein Barr Virus Latency on Cellular DNA Methylation Profile of ... | Homo sapiens | 48 | CSV, IDAT | 2025/08/30 |
| [GSE212300](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212300) | Gene expression-based, individualized outcome prediction for surgically treated ... | Homo sapiens | 12 | TXT | 2025/08/29 |
| [GSE212035](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212035) | Differential N6-methyladenosine(m6A) modification in hypertrophic scar v.s. norm... | Homo sapiens | 8 | TXT, XLSX | 2025/08/25 |
| [GSE306227](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306227) | A Cell Type Enrichment Analysis Tool for Brain DNA  Methylation Data (CEAM) [UKB... | Homo sapiens | 75 | IDAT, TXT | 2025/08/23 |
| [GSE306226](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306226) | A Cell Type Enrichment Analysis Tool for Brain DNA  Methylation Data (CEAM) [BDR... | Homo sapiens | 80 | IDAT, TXT | 2025/08/23 |
| [GSE289118](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289118) | New Cell lines Expanding the Diversity of Ewing Sarcoma Models | Homo sapiens | 44 | CEL, IDAT, TSV, TXT | 2025/08/22 |
| [GSE289061](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289061) | New Cell lines Expanding the Diversity of Ewing Sarcoma Models - methylation | Homo sapiens | 11 | IDAT, TXT | 2025/08/22 |

*...and 1297 more datasets.*
