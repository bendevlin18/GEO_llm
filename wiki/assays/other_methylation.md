# Other Methylation Profiling

> 3750 datasets | 2015/01/01 – 2026/04/08

Methylation profiling datasets where the specific protocol could not be determined from the title and summary. Includes SuperSeries that aggregate multiple SubSeries, studies using targeted bisulfite amplicon sequencing, and records with minimal metadata.

## Organism Distribution

| Organism | Count |
|----------|------:|
| Mus musculus | 1330 |
| Homo sapiens | 1290 |
| Arabidopsis thaliana | 265 |
| Rattus norvegicus | 89 |
| Homo sapiens; Mus musculus | 71 |
| Mus musculus; Homo sapiens | 51 |
| Danio rerio | 43 |
| Bos taurus | 29 |
| Sus scrofa | 25 |
| Oryza sativa | 25 |
| Saccharomyces cerevisiae | 16 |
| Solanum lycopersicum | 15 |
| Drosophila melanogaster | 14 |
| Oryza sativa Japonica Group | 12 |
| Zea mays | 12 |

## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
| TXT | 1515 | Text files (methylation tables, coverage files, metadata) |
| BW | 698 | BigWig coverage / methylation tracks |
| TSV | 659 | Tab-separated methylation data |
| BED | 533 | BED files (CpG methylation calls, DMR intervals) |
| BEDGRAPH | 294 | BedGraph methylation coverage |
| CSV | 274 | Comma-separated methylation data |
| COV | 219 | Coverage / bismark bismark .cov files |
| XLSX | 212 | Excel (methylation tables, differential analysis) |
| BIGWIG | 167 | BigWig coverage / methylation tracks |
| WIG | 165 |  |
| NARROWPEAK | 130 |  |
| CEL | 55 |  |
| MTX | 55 |  |
| XLS | 53 |  |
| GFF | 49 |  |

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
| [GSE293143](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293143) | Simultaneous orthogonal cell engineering by a single CRISPR-Cas9 polyfunctional ... | Homo sapiens | 84 | COV, TXT | 2026/04/03 |
| [GSE320398](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320398) | Pan-Cancer Analysis Reveals Mutation-Driven TE Dysregulation as a Contributor to... | Homo sapiens | 28 | BW | 2026/04/01 |
| [GSE229883](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229883) | N6-methyladenosine (m6A) sequencing in mouse trophoblast stem cells (mTSCs) with... | Mus musculus | 6 | BIGWIG | 2026/04/01 |
| [GSE311005](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311005) | Integrated Multiomic Profiling Enhances Risk Stratification and Prognostication ... | Canis lupus familiaris | 61 | TXT | 2026/03/30 |
| [GSE297847](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297847) | DNMT1 loss leads to hypermethylation of a subset of late replicating domains by ... | Homo sapiens | 42 | BIGWIG, COV, TXT | 2026/03/26 |
| [GSE188327](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE188327) | Next Generation Sequencing of Transcriptomes from Murine Articular Chondrocytes ... | Mus musculus | 22 | BIGWIG | 2026/03/25 |
| [GSE188326](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE188326) | Next Generation Sequencing of Transcriptomes from Murine Articular Chondrocytes ... | Mus musculus | 9 | BIGWIG | 2026/03/25 |
| [GSE268414](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE268414) | Retrospective analysis reveals the early origin and development of pulmonary per... | Mus musculus | 37 | BW, MTX, TSV | 2026/03/23 |
| [GSE268412](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE268412) | Retrospective analysis reveals the early origin and development of pulmonary per... | Mus musculus | 30 | BW | 2026/03/23 |
| [GSE293557](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293557) | A nanovaccine targeting cancer stem cells and bulk cancer cells reduces post-sur... | Mus musculus | 4 | BED | 2026/03/21 |
| [GSE309819](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309819) | Nucleosome spacing regulates linker methylation by DNMT3A2/3B3 | synthetic construct | 40 | PILEUP, VCF | 2026/03/18 |
| [GSE319319](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319319) | Xist RNA Dependent and Independent Mechanisms Regulate Dynamic X Chromosome Inac... | Mus musculus | 202 | BED, BEDGRAPH, BW | 2026/03/17 |
| [GSE296494](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296494) | Widespread non-Mendelian inheritance of DNA methylation patterns in mice [ONT Mu... | Mus musculus | 23 | BED | 2026/03/16 |
| [GSE292304](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292304) | The m5C orchestrator NSUN7 drives SPARC/HMGB1 axis–mediated inflammation to exac... | Homo sapiens | 12 | XLSX | 2026/03/15 |
| [GSE266668](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE266668) | Widespread non-Mendelian inheritance of DNA methylation patterns in mice. | Mus musculus | 109 | BED, SF, TSV, TXT | 2026/03/14 |
| [GSE314735](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314735) | Genome-wide methylation analysis identifies epigenetic differences in human ILC2... | Homo sapiens | 12 | CSV, PDF | 2026/03/12 |
| [GSE313891](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313891) | Genome-wide methylation analysis defines the epigenetic identity of human innate... | Homo sapiens | 12 | CSV, PDF | 2026/03/12 |
| [GSE311530](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311530) | Sir proteins impede, but do not prevent, access to silent chromatin in living Sa... | Saccharomyces cerevisiae | 62 | BW | 2026/03/12 |
| [GSE303457](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303457) | TET3-mediated DNA demethylation contributes to the formation of stable epiallele... | Solanum lycopersicum | 60 | BW, TSV | 2026/03/12 |
| [GSE317361](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317361) | A genome wide code to define cell-type specific CTCF binding and chromatin organ... | Mus musculus | 4 | BW | 2026/03/09 |
| [GSE305606](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE305606) | Intrinsically disordered regions restrain genomic targeting of RNA and histone d... | Arabidopsis thaliana; Mus musculus | 87 | BED, BROADPEAK, NARROWPEAK, TXT | 2026/03/09 |
| [GSE285802](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285802) | Intrinsically disordered regions restrain genomic targeting of RNA and histone d... | Arabidopsis thaliana | 20 | TSV | 2026/03/09 |
| [GSE323391](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE323391) | Reconstitution of spermatogenesis and continuous generation of functional haploi... | Mus musculus | 21 | TXT | 2026/03/08 |
| [GSE291548](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291548) | Epigenetic Regulation During Flatfish Metamorphosis: Integrative Omics Analysis ... | Scophthalmus maximus | 11 | TXT | 2026/03/07 |
| [GSE319461](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319461) | DNA methylation stochasticity is linked to transcriptional variability and ident... | Homo sapiens | 82 | BED, BW, TSV | 2026/03/06 |
| [GSE295634](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295634) | Decitabine-Primed CAR T-Cell Therapy for Relapsed/Refractory Non-Hodgkin's Lymph... | Homo sapiens | 32 | CSV, MTX, TSV, TXT | 2026/03/05 |
| [GSE287841](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE287841) | Intrinsically disordered regions restrain genomic targeting of RNA and histone d... | Arabidopsis thaliana; Mus musculus | 277 | BED, BROADPEAK, BW, NARROWPEAK | 2026/03/02 |
| [GSE307442](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307442) | Nucleolar Protein Nop2 Promotes Neural Differentiation by Regulating Ribosome Bi... | Danio rerio | 4 | TXT | 2026/03/01 |
| [GSE298432](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE298432) | Establishment of Human Formative Pluripotent Stem Cell Like Cells Exhibiting Amn... | Homo sapiens; Mus musculus | 21 | BW | 2026/03/01 |
| [GSE320108](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320108) | Integrating copy number, methylation, and fusion detection in one assay: A Nanop... | Homo sapiens | 20 | TSV | 2026/02/27 |
| [GSE310848](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310848) | Repeated Disuse Atrophy in Aged Rat Skeletal Muscle (Reduced Representation Enzy... | Rattus norvegicus | 28 | COV | 2026/02/24 |
| [GSE319295](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319295) | A significant change in the 5-hmCSeal signal is observed between UT-7 WT cells a... | Homo sapiens | 4 | BW | 2026/02/18 |
| [GSE126438](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126438) | Timecourse of Chromium exposure | Homo sapiens | 23 | TXT | 2026/02/14 |
| [GSE319289](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319289) | The Age-Dependent Resident Myonuclear Multi-Omic Response to an Acute Skeletal M... | Mus musculus | 49 | COV, CSV, H5, TXT | 2026/02/12 |
| [GSE319280](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319280) | A genome-wide DNA methylation survey reveals salicylic acid-induced distinct hyp... | Arabidopsis thaliana | 12 | TXT | 2026/02/12 |
| [GSE299486](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299486) | Single-molecule tracking in living cells reveals dynamics of DNMT1 through the c... | Homo sapiens | 24 | BED | 2026/02/11 |
| [GSE249809](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE249809) | The RNA 5-methylcytosine writer NSUN5 promotes hepatocellular carcinoma cell pro... | Homo sapiens | 12 | XLSX | 2026/02/09 |
| [GSE318059](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE318059) | Generational Stability of Environmentally Induced Epigenetic Transgenerational I... | Rattus norvegicus | 36 | CSV | 2026/02/04 |
| [GSE282076](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282076) | Occupancy-based Mechanism Is the Chief Mode of ROS1 Function in Preventing DNA H... | Brassica napus; Arabidopsis thaliana | 151 | BROADPEAK, BW, NARROWPEAK | 2026/02/03 |
| [GSE289856](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE289856) | Convergence of aging- and rejuvenation-related epigenetic alterations on PRC2 ta... | Mus musculus | 39 | BW | 2026/02/02 |
| [GSE145759](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE145759) | Soybean Pol IV and V Mutants | Glycine max | 72 | TXT | 2026/02/02 |
| [GSE145757](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE145757) | DNA Methylation Profiles in Soybean Pol IV and V Mutants | Glycine max | 12 | TXT | 2026/02/02 |
| [GSE283289](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE283289) | Multi-omic sequencing reveals distinctive gene expression and epigenetic alterat... | Homo sapiens | 25 | BEDGRAPH | 2026/01/31 |
| [GSE317924](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317924) | Effect of intrauterine growth restriction on the DNA methylation of microglia in... | Mus musculus | 4 | TDF, TXT | 2026/01/30 |
| [GSE293866](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293866) | Non-disruptive in vitro monitoring of cellular states with cell-free DNA methyla... | Homo sapiens; Mus musculus | 21 | BED, BW, H5AD, TSV | 2026/01/29 |
| [GSE316619](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316619) | Clonal memory of colitis accumulates and promotes tumor growth | Mus musculus | 47 | BW, JPG, JSON, MTX, PARQUET, PNG, TIFF, TSV | 2026/01/28 |
| [GSE225702](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225702) | Charting the DNA methylation landscape of the Killifish across age and tissues | Nothobranchius furzeri; Nothobranchius orthonotus | 44 | BW | 2026/01/28 |
| [GSE310173](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310173) | Embryonic stem cell factors DPPA2/4 amplify active H3K4me3-H2AK119ub chromatin d... | Homo sapiens | 300 | BEDGRAPH, BW, COV, NARROWPEAK, TXT | 2026/01/20 |
| [GSE302851](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302851) | Methylation variability and LINE-1 activation in multiple myeloma | Homo sapiens | 23 | BW, TAB | 2026/01/20 |
| [GSE296765](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296765) | Methionine metabolism and NOP2 methyltransferase are essential for MYC-Driven li... | Mus musculus | 18 | TXT | 2026/01/20 |

*...and 3700 more datasets.*
