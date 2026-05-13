# Benchmark Results — 2026-05-12

Scoring rubric (1–3 each): Accuracy · Completeness · Constraint adherence · Domain interpretation · Explanation quality · Hallucination · Tool efficiency

| Query | App Score | Agentic Score | Notes |
|---|---|---|---|
| Q2 | | | |
| Q3 | | | |

---
## Q2 (T1)
**Query:** How many CITE-seq datasets profile human PBMCs?

### App pipeline
*Shards: multiomics | Terms: CITE, profile, PBMCs | Expanded: PBMC, peripheral blood mononuclear cells, protein expression, surface markers, multimodal, immune cells, CD45+, leukocytes | Candidates: 89 | multiomics: 89 (+88 via synonyms)*

## Human PBMC CITE-seq Datasets in GEO

Based on the search results, I identified **27 CITE-seq datasets** profiling human PBMCs (directly or as a primary tissue). Here are the most relevant ones:

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE100866](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100866) | Homo sapiens | 12 | RNA + ADT UMI matrices (.csv.gz) | CITE-seq: Large scale simultaneous measurement of epitopes and transcriptomes in single cells |
| [GSE164378](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE164378) | Homo sapiens | 9 | RAW.tar (1.4GB), meta CSVs | Integrated analysis of multimodal single-cell data |
| [GSE213282](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE213282) | Homo sapiens | 8 | .mtx.gz, .tsv.gz, metadata .csv.gz | Titration of 124 antibodies using CITE-Seq on human PBMCs |
| [GSE190570](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE190570) | Homo sapiens | 8 | Antibody + gene raw CSVs, metadata | CITE-seq of human PBMCs (coronary artery disease severity) |
| [GSE205320](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE205320) | Homo sapiens | 5 | CSV | Combined protein and transcript scRNA-seq in human PBMCs |
| [GSE144434](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE144434) | Homo sapiens | 1 | RAW.tar (15MB) | CITEseq of human PBMC from healthy adult blood |
| [GSE158769](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158769) | Homo sapiens | 1 | exprs_norm.tsv.gz (3GB), metadata | Multimodal profiling of 500,000 memory T cells from a tuberculosis cohort |
| [GSE191332](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE191332) | Homo sapiens | 6 | RAW.tar, Seurat .RDS.gz | CITE-Seq of total PBMC pre/post-PfSPZ vaccination (IMRAS trial) |
| [GSE196198](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE196198) | Homo sapiens | 100 | Cell-type-split count matrices + TCR/BCR | Longitudinal single-cell multiomics across COVID-19 severity |
| [GSE229791](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229791) | Homo sapiens | 102 | ADT + GEX matrices (.txt.gz) | Multimodal hierarchical classification for CITE-seq annotation |
| [GSE202150](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE202150) | Homo sapiens | 57 | CSV, H5, TXT | Mapping Immune Responses in Acute Infection by Proteomics and CITESeq |
| [GSE226039](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE226039) | Homo sapiens | 46 | RAW.tar (136MB) | scRNAseq from PBMC, ileum, and rectal tissue (healthy & Crohn's disease) |
| [GSE277117](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE277117) | Homo sapiens | 62 | .h5ad (4.7GB), RAW.tar | scRNA-seq and PBMC profiling upon TNF Inhibitor Response in Ankylosing Spondylitis |
| [GSE284075](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE284075) | Homo sapiens | 122 | RAW.tar (1014MB) | Divergent Evolution of Malignant Subclones in cutaneous T-cell lymphoma |
| [GSE291290](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291290) | Homo sapiens | 6 | Raw Ab/Gene CSVs, metadata, VDJ CSV | CITE-seq of human PBMCs post heart transplantation |
| [GSE295725](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295725) | Homo sapiens | 98 | TPM TSV | Multimodal delineation of exhausted CD8 T cells in tumors |
| [GSE269335](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE269335) | Homo sapiens | 118 | .mtx.gz, obs/var .txt.gz | Single-cell multimodal profiling of monocytes and cardiovascular disease |
| [GSE269478](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE269478) | Homo sapiens | 30 | .mtx.gz, obs/var .txt.gz | Single-cell multimodal profiling of monocytes — CITE-seq arm |
| [GSE246317](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246317) | Homo sapiens | 6 | MTX, TSV | Immune checkpoint signatures in atherosclerosis — human PBMC CITE-seq |
| [GSE308814](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308814) | Homo sapiens | 43 | AbSeq DBEC MolsPerCell CSVs | Circulating immune cell profiling in alpha-gal syndrome |
| [GSE314400](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314400) | Homo sapiens | 4 | RAW.tar (228MB), QC CSVs | CIPHER-seq: low-stress intracellular multimodal profiling of immune activation in PBMCs |
| [GSE135325](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE135325) | Homo sapiens | 6 | FASTA, RAW.tar, SampleSheet | Targeted multi-omic analysis of protein and low-abundance transcripts (BD Rhapsody) |
| [GSE180410](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE180410) | Homo sapiens | 4 | CSV, MTX, TSV | CITE-seq on ALS4 and control CD8 T cells from PBMCs |
| [GSE229187](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229187) | Homo sapiens | 2 | RAW.tar (77MB), FASTA | CITE-seq of peripheral immune cells after SARS-CoV-2 vaccination in myeloma patients |
| [GSE216884](https://www.ncbi.nlm.

### Agentic pipeline
*Tool calls: rnaseq_singlecell(CITE-seq, PBMC, human); multiomics(CITE-seq, PBMC, human); rnaseq_snrnaseq(CITE-seq, PBMC, human)*

Here are the **3 unique CITE-seq datasets** profiling human PBMCs found in the index:

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE213282](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE213282) | *Homo sapiens* | 8 | .mtx.gz, .tsv.gz, .csv.gz | Titration of 124 antibodies using CITE-Seq on human PBMCs |
| [GSE185712](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185712) | *Homo sapiens* | 6 | .h5 (ADT + RNA) | scRNAseq on sorted T-cells and CITE-seq on PBMCs |
| [GSE291290](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291290) | *Homo sapiens* | 6 | .csv.gz | Single cell multi-omic sequencing of PBMCs post heart transplantation |

---

### Summary & Notes

- **3 datasets** match CITE-seq + human PBMC across the index (confirmed across `rnaseq_singlecell`, `multiomics`, and `rnaseq_snrnaseq` shards, with no duplicates).
- All three have **processed data available** (`.h5`, `.mtx.gz`, `.csv.gz` files).
- **Best for antibody panel benchmarking:** GSE213282 — profiles 124 antibodies, making it ideal for panel design or normalization studies.
- **Best for T-cell biology:** GSE185712 — combines sorted T-cell scRNA-seq with PBMC CITE-seq from healthy donors.
- **Best for disease context:** GSE291290 — includes post-heart-transplant patients with multi-omic (CITE-seq + VDJ-seq) readouts.
- ⚠️ **Caveat:** This index covers 2015–2026 but may not capture every deposited dataset; some studies may use synonyms like "Cellular Indexing of Transcriptomes and Epitopes" or embed CITE-seq as part of larger cohort studies. A broader search (e.g., removing the PBMC filter) could surface additional datasets.

---
## Q3 (T2)
**Query:** Mouse kidney snRNA-seq with at least 5 samples and H5 files available

### App pipeline
*Shards: rnaseq_snrnaseq, rnaseq_bulk | Terms: snRNA-seq, kidney, files, available | Expanded: kidney single-nucleus RNA sequencing, renal snRNA-seq, glomerulus, proximal tubule, collecting duct, HDF5, Mus musculus kidney | Candidates: 300 | snRNA-seq: 124 (+3 via synonyms), bulk RNA-seq: 248 (+98 via synonyms)*

## Mouse Kidney snRNA-seq Datasets (≥5 Samples, H5 Files Available)

Strictly meeting **all three criteria** (Mus musculus + snRNA-seq + ≥5 samples + .h5 files):

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE184652](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE184652) | Mus musculus | 70 | count_matrix_combined_after_cellbender.tar.gz (3.1GB), metadata.csv.gz (29MB), RAW.tar (7.7GB) | Mapping the Single Cell Transcriptomic Response of Murine Diabetic Kidney Disease to Therapies |
| [GSE268494](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE268494) | Mus musculus | 32 | count_RNA.rds.gz (518MB), count_peaks.rds.gz (2.0GB), metadata.csv.gz (7MB), RAW.tar (36.7GB) | Single Cell Multiomics Profiling for the Mouse Polycystic Kidney Disease |
| [GSE171417](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171417) | Mus musculus | 9 | Metadata.txt.gz (138KB), Mouse_control_UMIcounts.txt.gz (15MB), Mouse_IRI_UMIcounts.txt.gz (24MB) | Single-nuclear transcriptomics reveals a diversity of proximal tubule cell states in a dynamic response to acute kidney injury |
| [GSE150284](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150284) | Mus musculus | 8 | Converted_counttable.txt.gz (209MB), Native_counttable.txt.gz (218MB) | CoolMPS for robust sequencing of single-nuclear RNAs captured by droplet-based method |
| [GSE280119](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE280119) | Mus musculus | 6 | integrated_batch_20230921_KO.rds.gz (970MB) | PCK1 loss contributes to kidney disease progression by altering mitochondrial fitness [snRNA-seq_PCK1KO] |
| [GSE218056](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE218056) | Mus musculus | 6 | RAW.tar (162MB) | Gene expression profile at single cell level of adrenal glands from Tmem127 WT and KO mice |
| [GSE237816](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE237816) | Mus musculus | 12 | RAW.tar (1.6GB) | Cell-type-specific expression and regulation in cerebral cortex and kidney of atypical Schinzel Giedion Syndrome mice |
| [GSE119531](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119531) | Mus musculus | 5 | Healthy.combined.dge.txt.gz (14MB), UUO.dge.txt.gz (6MB), cell annotation files | Advantages of single nucleus over single cell RNA-seq in adult kidney |

---

### ⭐ Best Matches

**Top picks for mouse kidney snRNA-seq with direct H5/processed data:**

1. **[GSE184652](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE184652)** is the standout dataset — 70 samples from a db/db diabetic kidney disease model with multiple drug treatments (ACEi, SGLT2i, Rosiglitazone), including CellBender-processed count matrices and metadata. Ideal for disease modeling and drug response studies.

2. **[GSE268494](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE268494)** — 32-sample multiome dataset (snRNA-seq + snATAC-seq) of polycystic kidney disease (PKD) in mice, with well-organized RDS processed files. Good for trajectory/regulatory analyses.

3. **[GSE171417](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171417)** — 9 samples focused on proximal tubule responses to acute kidney injury (IRI model, 7-day and 28-day timepoints). Clean UMI count matrices provided separately by condition.

4. **[GSE119531](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119531)** — A methodological benchmark paper directly comparing snRNA-seq vs. scRNA-seq in adult mouse kidney (healthy + UUO fibrosis model). Useful as a reference atlas.

---

### ⚠️ Important Caveats

- **H5 files specifically**: None of the strictly mouse kidney snRNA-seq datasets with ≥5 samples provide `.h5` or `.h5ad` files directly — processed data is distributed as `.rds.gz`, `.txt.gz`, or via `RAW.tar`. If `.h5` format is essential, you may need to convert from these formats.
- **GSE237816** and **GSE218056** involve kidney tissue but their primary focus is adrenal gland/cortex biology or multi-tissue comparison — verify kidney sample counts before use.
- **GSE268494** carries a `multiomics` flag — confirm snRNA-seq samples can be analyzed independently from the ATAC component.
- **GSE150284** is primarily a sequencing chemistry benchmarking study (CoolMPS), not a disease model — useful for technical comparisons.

### Agentic pipeline
*Tool calls: rnaseq_snrnaseq(mouse, kidney); rnaseq_singlecell(mouse, kidney, snRNA); rnaseq_snrnaseq(mouse, kidney, h5); multiomics(mouse, kidney, snRNA); rnaseq_snrnaseq(mouse, kidney, RAW.tar)*

Here are all qualifying datasets — **mouse kidney snRNA-seq with ≥5 samples**. Datasets with `RAW.tar` archives very commonly contain per-sample 10x Genomics `.h5` files (filtered_feature_bc_matrix.h5), and some have explicitly named `.h5` or `.h5ad` files:

---

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE184652](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE184652) | *Mus musculus* | 70 | RAW.tar (7.7GB), CellBender count matrix tar, metadata CSV | Mapping the Single Cell Transcriptomic Response of Murine Diabetic Kidney Disease to Therapies |
| [GSE139107](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE139107) | *Mus musculus* | 24 | 6× DGE .txt.gz + metadata | Cell profiling of acute kidney injury reveals conserved cellular responses to injury |
| [GSE241213](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241213) | *Mus musculus* | 40 | sn_counts.csv.gz, bulk_counts.csv.gz, metadata | Gene expression at bulk and single-nucleus level post sham/unilateral nephrectomy |
| [GSE268494](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE268494) | *Mus musculus* | 32 | RAW.tar (36.7GB), RDS files (RNA, ATAC, SCT), metadata | Single Cell Multiomics Profiling for Mouse Polycystic Kidney Disease |
| [GSE171417](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171417) | *Mus musculus* | 9 | UMI count .txt.gz (control + IRI), metadata | Single-nuclear transcriptomics of proximal tubule cell states in acute kidney injury |
| [GSE220493](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE220493) | *Mus musculus* | 6 | RAW.tar (440MB) | Unified Mouse and Human Kidney Single-Cell Expression Atlas (Disease States) |
| [GSE244839](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE244839) | *Mus musculus* | 5 | RAW.tar (1.6GB) | EGFR Activation is Essential for Kidney Fibrosis Development |
| [GSE275526](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE275526) | *Mus musculus* | 6 | RAW.tar (1.2GB) | snRNA-seq of kidney tissue in cecal ligation and puncture (CLP) sepsis model |
| [GSE295103](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295103) | *Mus musculus* | 6 | RAW.tar (1.3GB) | Single nucleus RNA-seq of mouse kidney throughout postnatal development |
| [GSE282959](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282959) | *Mus musculus* | 8 | RAW.tar (16MB) | TFAP2A orchestrates gene regulatory networks in kidney outer medullary collecting ducts |

---

### 🔍 Best Matches & Notes

**Top picks with likely H5 files (via RAW.tar from 10x Genomics runs):**
- 🏆 **GSE184652** — The largest dataset (70 samples), covering a diabetic kidney disease model with multiple drug treatments at two timepoints. The `CellBender`-processed count matrix tar strongly implies 10x `.h5` inputs were used.
- 🏆 **GSE268494** — 32 samples, snRNA-seq + snATAC-seq multiome on polycystic kidney disease. The large RAW.tar (36.7 GB) almost certainly contains per-sample `.h5` files; also ships processed `.rds` objects.
- 🏆 **GSE244839**, **GSE275526**, **GSE295103**, **GSE220493** — All have large RAW.tar archives (440 MB–1.6 GB) consistent with 10x `.h5` bundles.

**Processed data available (non-H5 formats):**
- **GSE139107** — DGE text matrices only (no RAW.tar); likely no raw `.h5`.
- **GSE241213** — CSV count matrices provided directly; no RAW.tar.
- **GSE171417** — UMI count text files; no RAW.tar.

⚠️ **Caveat:** H5 file presence within `RAW.tar` archives must be confirmed by downloading or inspecting the archive manifest on GEO. The index does not always list internal archive contents explicitly.

---
# Benchmark Results — 2026-05-12

Scoring rubric (1–3 each): Accuracy · Completeness · Constraint adherence · Domain interpretation · Explanation quality · Hallucination · Tool efficiency

| Query | App Score | Agentic Score | Notes |
|---|---|---|---|
| Q1 | | | |

---
