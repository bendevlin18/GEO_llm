# Single-Cell RNA-seq (scRNA-seq)

> 23057 datasets | 2015/01/01 – 2026/04/08

Transcriptome profiling at single-cell resolution. Typically uses droplet-based (10x Chromium, Drop-seq) or plate-based (Smart-seq) protocols. Supplementary files often include sparse count matrices (MTX), HDF5 objects (H5/H5AD), or R objects (RDS/Seurat).

## Organism Distribution

| Organism | Count |
|----------|------:|
| Mus musculus | 11665 |
| Homo sapiens | 8332 |
| Homo sapiens; Mus musculus | 461 |
| Danio rerio | 418 |
| Mus musculus; Homo sapiens | 256 |
| Rattus norvegicus | 200 |
| Drosophila melanogaster | 188 |
| Macaca mulatta | 103 |
| Sus scrofa | 96 |
| Gallus gallus | 85 |
| Arabidopsis thaliana | 63 |
| Bos taurus | 56 |
| Macaca fascicularis | 51 |
| Caenorhabditis elegans | 44 |
| Mus | 29 |

## Archive Contents (file types inside supplementary TAR/gz)

| Type | Count | Description |
|------|------:|-------------|
| TSV | 11790 | Tab-separated (10x barcodes/features, metadata) |
| MTX | 10554 | Sparse matrices (10x CellRanger output) |
| TXT | 5650 | Text files (count matrices, gene lists, metadata) |
| CSV | 4870 | Comma-separated (count matrices, DE results) |
| H5 | 3165 | HDF5 (CellRanger filtered matrices) |
| RDS | 1257 | R serialized objects (Seurat, SingleCellExperiment) |
| TAR | 1064 | Tar archives (bundled outputs) |
| XLSX | 941 | Excel (DE results, sample annotations) |
| BW | 560 | BigWig (coverage tracks) |
| H5AD | 546 | AnnData HDF5 (scanpy/Python ecosystem) |
| BED | 358 |  |
| BIGWIG | 264 | BigWig (coverage tracks) |
| TBI | 201 |  |
| TAB | 198 |  |
| NARROWPEAK | 154 |  |

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
| [GSE326782](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326782) | Mitochondrial L-2-hydroxyglutarate is a physiologic signaling metabolite [scRNA-... | Mus musculus | 7 | CSV, MTX, TSV | 2026/04/08 |
| [GSE320212](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320212) | Identifying Senescence and Immune Biomarkers Predictive of Benefit to Combined C... | Homo sapiens | 23 | CSV, H5, RDA | 2026/04/08 |
| [GSE314400](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314400) | CIPHER-seq enables low-stress intracellular multimodal profiling of immune activ... | Homo sapiens | 4 | CSV, H5 | 2026/04/08 |
| [GSE309616](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309616) | Therapeutic Synergy Overcomes Carboplatin Resistance in Triple-Negative Breast C... | Homo sapiens | 2 | TAR | 2026/04/08 |
| [GSE284348](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE284348) | Generation of Stable Chambered Cardioids from human Pluripotent Stem Cells | Homo sapiens | 1 | MTX, TSV | 2026/04/08 |
| [GSE261506](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE261506) | Single-cell transcriptional profiling of lung epithelial cells after naphthalene... | Mus musculus | 12 | H5 | 2026/04/08 |
| [GSE327208](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327208) | Control of Cellular Differentiation Trajectories for Cancer Reversion | Homo sapiens | 12 | TSV | 2026/04/07 |
| [GSE327167](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327167) | Single-cell RNA-seq profiling of pleural mesothelioma and comparator pleural spe... | Homo sapiens | 113 | MTX, TSV, TXT | 2026/04/07 |
| [GSE326854](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326854) | Gene expression profile at single cell level of different phenotypic tumors deri... | Homo sapiens | 6 | H5 | 2026/04/07 |
| [GSE326833](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326833) | Population Heterogeneity of Lactobacillus delbrueckii subsp. bulgaricus in Micro... | Lactobacillus delbrueckii subsp. bulgaricus | 3 | MTX, TSV | 2026/04/07 |
| [GSE326100](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326100) | scRNA-seq of mouse cochlea organoid cells | Mus musculus | 768 | TXT | 2026/04/07 |
| [GSE324735](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324735) | PEPITEM regulates the synovial microenvironment during immune-mediated inflammat... | Mus musculus | 6 | MTX, TSV | 2026/04/07 |
| [GSE324449](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324449) | Single-cell transcriptomic profiling of SPAST exon 17 deletion–induced neurodege... | Homo sapiens | 2 | MTX, TSV | 2026/04/07 |
| [GSE320583](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320583) | Necroptosis triggers inflammatory interferon signatures in patient-derived metas... | Homo sapiens | 3 | CSV | 2026/04/07 |
| [GSE318313](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE318313) | Pulsed photobiomodulation reprograms the tumor immune microenvironment to restor... | Mus musculus | 2 | MTX, TSV | 2026/04/07 |
| [GSE312076](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312076) | Zone-specific hepatocytes orchestrate the early onset of host defence mechanisms... | Mus musculus | 3 | H5, TAR | 2026/04/07 |
| [GSE310468](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310468) | scRNAseq of whole lung homogenates from WT and Scnn1b-Tg mice. | Mus musculus | 5 | MTX, RDS, TSV | 2026/04/07 |
| [GSE297816](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE297816) | Early-life RNA sequencing of colon stromal cells and iNKT cells | Mus musculus | 40 | MTX, TSV, TXT | 2026/04/07 |
| [GSE295600](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295600) | Combinatorial delivery of low-dose irradiation and immunotherapy to patients wit... | Homo sapiens | 18 | CSV | 2026/04/07 |
| [GSE295599](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295599) | Combinatorial delivery of low-dose irradiation and immunotherapy to patients wit... | Homo sapiens | 29 | TXT | 2026/04/07 |
| [GSE284713](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE284713) | Pulmonary fibroblast activation during Aspergillus fumigatus infection enhances ... | Mus musculus | 4 | H5, XLSX | 2026/04/07 |
| [GSE284270](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE284270) | Pulmonary fibroblast activation during Aspergillus fumigatus infection enhances ... | Mus musculus | 8 | XLSX | 2026/04/07 |
| [GSE283574](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE283574) | A Tunable Cas12a Platform for Single-Cell Perturbation Screening and CRISPRi | Homo sapiens | 26 | CSV, MTX, TSV, TXT | 2026/04/07 |
| [GSE277691](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE277691) | Elucidating early intestinal stem cell response to bacterial infection | Mus musculus | 12 | CSV, MTX, TSV | 2026/04/07 |
| [GSE264636](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE264636) | Lymphomatoid papulosis vs. advanced-stage cutaneous T-cell lymphomas: Single-cel... | Homo sapiens | 15 | MTX, TSV | 2026/04/07 |
| [GSE242697](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242697) | Single-cell RNA sequencing of iALI epithelial and mesenchymal cell derived from ... | Homo sapiens | 3 | MTX, TSV | 2026/04/07 |
| [GSE196044](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE196044) | Single-Cell Transcriptomic and Chromatin Accessibility Atlas of Peripheral Blood... | Sus scrofa | 6 | H5, XLS | 2026/04/07 |
| [GSE327152](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327152) | Cardiac tertiary immune niches drive immune activation in immune checkpoint inhi... | Mus musculus | 1 | CSV, MTX, RDS, TSV | 2026/04/06 |
| [GSE327057](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327057) | Systematically characterizing the roles of E3-ligase family members in inflammat... | Mus musculus | 169 | CSV, H5AD | 2026/04/06 |
| [GSE326978](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326978) | Essential lncRNAs in the human transcriptome [CRISPR] | Homo sapiens | 16 | CSV, MTX, TSV | 2026/04/06 |
| [GSE326938](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326938) | Discovery of a primed endothelial progenitor that requires VEGF/ERK inhibition t... | Homo sapiens | 10 | H5 | 2026/04/06 |
| [GSE326936](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326936) | Discovery of a primed endothelial progenitor that requires VEGF/ERK inhibition t... | Homo sapiens | 6 | H5 | 2026/04/06 |
| [GSE324222](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE324222) | Enhanced endocrine–metabolic support and axonemal assembly in high-sperm-motilit... | Anser cygnoides | 6 | MTX, TSV | 2026/04/06 |
| [GSE318563](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE318563) | Expression of Atg8a in Somatic Follicle Cells Prevents Age-Associated Decline in... | Drosophila melanogaster | 2 | MTX, TSV | 2026/04/06 |
| [GSE317642](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317642) | Mutation-dependent responses to sleep and exercise in clonal hematopoiesis | Mus musculus | 8 | CSV, H5 | 2026/04/06 |
| [GSE313334](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313334) | The intestinal microbiota impacts nutritional immunity and resistance to Acineto... | Mus musculus | 4 | CSV, H5 | 2026/04/06 |
| [GSE309821](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309821) | Enhancer-directed gene delivery for digit regeneration based on conserved epider... | Danio rerio | 5 | H5 | 2026/04/06 |
| [GSE309792](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309792) | Enhancer-directed gene delivery for digit regeneration based on conserved epider... | Mus musculus | 4 | TSV | 2026/04/06 |
| [GSE295045](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295045) | A local sympathetic-immune axis inhibits melanoma growth in mice by dictating ad... | Mus musculus | 4 | CSV, H5 | 2026/04/06 |
| [GSE294864](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294864) | Engineered cytokine-secreting cells to prevent foreign body response against imp... | Mus musculus | 7 | H5 | 2026/04/06 |
| [GSE292341](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292341) | Single cell RNA sequencing of hippocampus and hypothalamus in AD mice with fruct... | Mus musculus | 48 | CSV, MTX, TSV | 2026/04/06 |
| [GSE287930](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE287930) | Epigenetic modulation of polyamine biosynthetic pathways rectifies T cell dysfun... | Homo sapiens | 2 | TAR | 2026/04/06 |
| [GSE279368](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE279368) | Cell clusters during mandibular bone regeneration [scRNA-seq] | Mus musculus | 1 | MTX, TSV | 2026/04/06 |
| [GSE326605](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326605) | Bile acid uptake activates STAT signaling and impairs natural killer cells in me... | Homo sapiens | 4 | MTX, TSV, TXT | 2026/04/05 |
| [GSE301970](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301970) | Multiome analysis of Kras-mutant intestinal epithelium 10 days post-recombinatio... | Mus musculus | 20 | H5, TSV | 2026/04/05 |
| [GSE301967](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301967) | Multiome analysis of tumors isolated from Apc cKO; Kras-mutant animals | Mus musculus | 12 | H5, TSV | 2026/04/05 |
| [GSE293911](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293911) | A Unique System of Paired PDX Models to Investigate the Progression of Potential... | Homo sapiens | 2 | MTX, TSV | 2026/04/05 |
| [GSE287799](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE287799) | Epigenetic modulation of polyamine biosynthetic pathways rectifies T cell dysfun... | Homo sapiens | 6 | TXT | 2026/04/05 |
| [GSE326484](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326484) | Combined dopamine receptor inhibition and radiotherapy target mesothelioma-initi... | Homo sapiens | 4 | MTX, TSV | 2026/04/04 |
| [GSE326368](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE326368) | Zona-pellucida-inspired cellular microenvironment induces the formation of human... | Homo sapiens | 6 | CSV | 2026/04/04 |

*...and 23007 more datasets.*
