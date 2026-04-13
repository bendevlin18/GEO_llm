# CITE-seq

> 376 datasets | 2016/04/12 – 2026/04/08

Cellular Indexing of Transcriptomes and Epitopes by Sequencing (CITE-seq). Simultaneously measures gene expression (RNA) and surface protein abundance using antibody-derived tags (ADTs) from the same single cell. Closely related methods include REAP-seq, ASAP-seq, and feature barcoding on the 10x platform. Supplementary files typically include separate RNA and ADT count matrices (CSV, TSV, H5, RDS/Seurat).

## Organism Distribution

| Organism | Count |
|----------|------:|
| Homo sapiens | 196 |
| Mus musculus | 164 |
| Mus musculus; Homo sapiens | 5 |
| Homo sapiens; Mus musculus | 5 |
| Macaca mulatta | 2 |
| Homo sapiens; synthetic construct | 1 |
| Homo sapiens; Escherichia coli | 1 |
| Sus scrofa; Mus musculus; Danio rerio; Gallus gallus; Macaca mulatta; Homo sapiens; Mesocricetus auratus | 1 |
| Mus musculus; Rattus norvegicus | 1 |

## Supplementary File Types

| Type | Count | Description |
|------|------:|-------------|
| CSV | 194 | Comma-separated data (count matrices, protein counts, metadata) |
| TSV | 182 | Tab-separated data (barcodes, features, fragment files) |
| MTX | 148 | Sparse count matrices (10x CellRanger output, RNA or ATAC) |
| TXT | 81 | Text files (count matrices, cell metadata) |
| H5 | 75 | HDF5 (CellRanger filtered matrices, combined RNA+ATAC) |
| RDS | 48 | R serialized objects (Seurat, MultiAssayExperiment) |
| TAR | 21 | Tar archives (bundled multi-modal outputs) |
| XLSX | 19 | Excel (metadata, differential results) |
| H5AD | 9 | AnnData HDF5 (scanpy/Python ecosystem, multi-modal) |
| FASTA | 8 |  |
| BW | 4 | BigWig coverage tracks |
| JSON | 3 |  |
| PNG | 3 |  |
| ZIP | 3 |  |
| TBI | 3 |  |

## Analyzing These Datasets

| File Types | Protocol | Effort |
|------------|----------|--------|
| CSV, TSV, TXT, XLSX | [CSV / TSV Count Matrices](../protocols/csv_tsv_counts.md) | ⭐ Easy |
| RDATA, RDS | [RDS / Seurat Objects](../protocols/rds_seurat.md) | ⭐⭐ Easy–Medium |
| H5AD | [H5AD / AnnData (scanpy)](../protocols/h5ad_anndata.md) | ⭐⭐ Easy–Medium |
| H5 | [H5 / CellRanger HDF5](../protocols/h5_cellranger.md) | ⭐⭐⭐ Medium |
| MTX | [MTX / 10x Sparse Matrices](../protocols/mtx_10x.md) | ⭐⭐⭐ Medium |

> **Protocol pages coming soon:** **BED / BigWig / Peak files** (BED, BIGWIG, BROADPEAK, BW, NARROWPEAK).

## Recent Datasets

| Accession | Title | Organism | Samples | Archive Contents | Date |
|-----------|-------|----------|--------:|-----------------|------|
| [GSE314400](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314400) | CIPHER-seq enables low-stress intracellular multimodal profiling of immune activ... | Homo sapiens | 4 | CSV, H5 | 2026/04/08 |
| [GSE320583](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE320583) | Necroptosis triggers inflammatory interferon signatures in patient-derived metas... | Homo sapiens | 3 | CSV | 2026/04/07 |
| [GSE313215](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313215) | Targeting LPAR4 overcomes stress adaptation to CDK4/6 inhibition in soft tissue ... | Mus musculus | 4 | CSV, RDS | 2026/04/01 |
| [GSE254983](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE254983) | CITE-seq analysis of Mycobacterium tuberculosis infected wild-type and IL-1R KO ... | Mus musculus | 6 | MTX, RDS, TSV | 2026/04/01 |
| [GSE254926](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE254926) | CITE-seq analysis of Mycobacterium tuberculosis infected Irg1- and iNOS-deficien... | Mus musculus | 9 | MTX, RDS, TSV | 2026/04/01 |
| [GSE299902](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299902) | Circulatory ILC2 convert and persist as part of the long-term tissue-resident po... | Mus musculus | 18 | CSV, H5, RDS | 2026/03/30 |
| [GSE299900](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299900) | Circulatory ILC2 convert and persist as part of the long-term tissue-resident po... | Mus musculus | 24 | CSV, H5, RDS | 2026/03/30 |
| [GSE316247](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316247) | Dendritic cells accelerate CAR T cells in irradiated tumors through chimeric syn... | Mus musculus | 12 | CSV, RDS | 2026/03/25 |
| [GSE302632](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302632) | Single-cell transcriptome profiling of hematopoietic stem and progenitor cells i... | Mus musculus | 9 | MTX, TSV, TXT | 2026/03/25 |
| [GSE250041](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE250041) | Identification of senescent cell subpopulations by CITE-seq analysis | Homo sapiens | 4 | MTX, TSV | 2026/03/23 |
| [GSE318707](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE318707) | ST8Sia6-dependent glycosylation restrains gut inflammation and pathogenic Th1 an... | Mus musculus | 18 | MTX, TSV | 2026/03/22 |
| [GSE303880](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303880) | MAIT cell enrichment in Lynch syndrome is associated with immune surveillance an... | Homo sapiens | 3 | RDS | 2026/03/16 |
| [GSE292038](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292038) | CITE-Seq analysis of intratumoral immune cells from YUMM1.7 melanoma treated wit... | Mus musculus | 6 | CSV, MTX, TSV | 2026/03/15 |
| [GSE292829](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292829) | Inhibition of NFAT after human uterus transplant promotes loss of tissue-residen... | Homo sapiens | 58 | MTX, TSV | 2026/03/10 |
| [GSE314416](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314416) | Immune-microbiome coordination defines interferon setpoints in healthy humans [C... | Homo sapiens | 108 | CSV, H5, RDS | 2026/03/09 |
| [GSE322634](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322634) | LIF induced tumor plasticity establishes an immunosuppressive myeloid niche in L... | Mus musculus | 2 | CSV, RDS | 2026/03/07 |
| [GSE322633](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE322633) | LIF induced tumor plasticity establishes an immunosuppressive myeloid niche in L... | Mus musculus | 3 | CSV, RDS | 2026/03/07 |
| [GSE317605](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317605) | A Phase II Trial of Pembrolizumab plus Granulocyte Macrophage Colony Stimulating... | Homo sapiens | 168 | MTX, TSV, XLSX | 2026/03/01 |
| [GSE306608](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306608) | Sensitive CAR T cells redefine targetable CD70 expression in solid tumors [CITE-... | Homo sapiens | 6 | CSV, MTX, TSV | 2026/02/26 |
| [GSE313153](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313153) | CITE-seq profiling of human splenic dendritic cells | Homo sapiens | 4 | RDS, XLSX | 2026/02/23 |
| [GSE283984](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE283984) | A pipeline to unravel complexity of the human peripheral blood B cell compartmen... | Homo sapiens | 3 | CSV | 2026/02/18 |
| [GSE317004](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317004) | CITE-seq of cardiac CD45+ leukocytes in mice with myocardial infarction and NK c... | Mus musculus | 3 | H5, TXT | 2026/02/10 |
| [GSE316673](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316673) | Ontogeny and transcriptional regulation of Thetis cells [CITE-Seq] | Mus musculus | 2 | MTX, TSV, TXT | 2026/02/04 |
| [GSE314596](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314596) | Targeting Modulated Vascular Smooth Muscle Cells in Atherosclerosis via FAP-Dire... | Homo sapiens | 58 | CSV, RDS | 2026/02/02 |
| [GSE308689](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308689) | The integrated stress response promotes immune evasion through Lipocalin 2 | Mus musculus | 2 | CSV, RDS | 2026/01/28 |
| [GSE287998](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE287998) | Type I and II interferons drive inflammation through STAT1 in murine macrophage ... | Mus musculus | 8 | CSV, H5 | 2026/01/28 |
| [GSE312479](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312479) | RORγt⁺ Dendritic Cells Are a Distinct Lymphoid-Derived Lineage [CITE-seq] | Mus musculus | 4 | MTX, TSV, XLSX | 2026/01/26 |
| [GSE316782](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316782) | Multimodal single-cell and spatial profiling reveals altered T cell-mediated imm... | Homo sapiens | 18 | CSV, TSV | 2026/01/21 |
| [GSE316096](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE316096) | Clonal expansion of cytotoxic CD8+ T cells in lecanemab-associated ARIA | Homo sapiens | 18 | CSV, H5 | 2026/01/20 |
| [GSE312960](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312960) | Cohesin-mediated chromatin remodeling controls the differentiation and function ... | Mus musculus | 2 | CSV, MTX, RDS, TSV | 2026/01/13 |
| [GSE306777](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE306777) | Transcription factor Etv3 controls the tolerogenic function of dendritic cells (... | Mus musculus | 2 | CSV, MTX, RDS, TSV | 2026/01/13 |
| [GSE315610](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE315610) | Heterogeneity and plasticity of the naive CD4+ T cell compartment [mouse CITEseq... | Mus musculus | 2 | MTX, TSV, TXT | 2026/01/09 |
| [GSE315609](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE315609) | Heterogeneity and plasticity of the naive CD4+ T cell compartment [human CITEseq... | Homo sapiens | 2 | MTX, TSV, TXT | 2026/01/09 |
| [GSE262394](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262394) | B cell leukemia co-opts a hematopoietic stem cell-CD4 T cell tolerance program t... | Mus musculus | 3 | CSV, MTX, RDS, TSV, TXT | 2025/12/31 |
| [GSE313642](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE313642) | Immunosuppressive monocytes are enriched in hepatocellular carcinoma patients wi... | Homo sapiens | 194 | MTX, TSV | 2025/12/12 |
| [GSE266455](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE266455) | hiv-seq reveals global host gene expression differences between hiv-transcribing... | Homo sapiens | 48 | MTX, TSV | 2025/12/10 |
| [GSE290161](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE290161) | Immune profiling of the lung in Influenza-Associated Pulmonary Aspergillosis usi... | Mus musculus | 8 | CSV, H5 | 2025/12/04 |
| [GSE255903](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE255903) | Primate resident memory T cells activate humoral and stromal immunity [CITE-seq] | Macaca mulatta | 16 | CSV, MTX, TSV | 2025/12/04 |
| [GSE311344](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311344) | T cells in B16 tumor model with ACT and checkpoint blockade - scRNA-seq, CITE-se... | Mus musculus | 15 | CSV, MTX, TSV | 2025/12/01 |
| [GSE278892](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE278892) | CITEseq of migratory nLCncDC1 of skin-draining lymph nodes from MC903-treated mi... | Mus musculus | 3 | MTX, TSV, TXT | 2025/12/01 |
| [GSE303868](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303868) | A tumor-associated macrophage-targeted immunocytokine leveraging T and NK cell s... | Homo sapiens | 36 | CSV, MTX, TSV | 2025/11/19 |
| [GSE293108](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293108) | SKIDA1 transiently sustains MLL::ENL-Expressing hematopoietic progenitors during... | Mus musculus | 3 | MTX, TSV | 2025/11/04 |
| [GSE266608](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE266608) | A unified workflow to define multipotent progenitor hierarchies (CITE-Seq and Ce... | Mus musculus | 63 | H5 | 2025/10/21 |
| [GSE302846](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302846) | Periostin promotes sarcoma growth by increasing tumor associated macrophages. [C... | Mus musculus | 4 | CSV, H5, RDS | 2025/10/20 |
| [GSE291290](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291290) | Single cell multi-omic sequencing of human peripheral mononuclear cells (PBMCs) ... | Homo sapiens | 6 | CSV | 2025/10/15 |
| [GSE299416](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299416) | TCRs enable traceability of CAR-T cells but impair function in dual target cell ... | Homo sapiens | 9 | CSV, H5 | 2025/10/06 |
| [GSE299415](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE299415) | TCRs enable traceability of CAR-T cells but impair function in dual target cell ... | Homo sapiens | 4 | CSV, H5 | 2025/10/06 |
| [GSE279451](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE279451) | Multiomics Analyses Unveil Immune Landscape in Pediatric and Adult Sepsis [CITE-... | Homo sapiens | 40 | MTX, TSV | 2025/09/28 |
| [GSE295654](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295654) | Exploring the dendritic cell subset regulating naïve CD8 T cell homeostasis | Mus musculus | 4 | CSV, H5 | 2025/09/24 |
| [GSE308814](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308814) | Single-cell mRNA analysis and surface marker expression profiling of circulating... | Homo sapiens | 43 | CSV | 2025/09/22 |

*...and 326 more datasets.*
