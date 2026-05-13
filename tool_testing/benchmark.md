# Benchmark Summary — 2026-05-12

Scoring rubric (1–3 each): Accuracy · Completeness · Constraint adherence · Domain interpretation · Explanation quality · Hallucination · Tool efficiency

## Overlap statistics

| Query | Tier | App | Agentic | Overlap | Jaccard | Query |
|---|---|---|---|---|---|---|
| Q1 | T1 | 10 | 7 | 5 | 0.42 | Find zebrafish spatial transcriptomics datasets |
| Q2 | T1 | 25 | 3 | 2 | 0.08 | How many CITE-seq datasets profile human PBMCs? |
| Q3 | T2 | 8 | 10 | 3 | 0.20 | Mouse kidney snRNA-seq with at least 5 samples and H5 f |
| Q4 | T2 | 20 | 0 | 0 | 0.00 | Human bulk RNA-seq cancer datasets with processed count |
| Q5 | T2 | 18 | 19 | 12 | 0.48 | H3K27ac ChIP-seq datasets in mouse embryonic stem cells |
| Q6 | T3 | 20 | 31 | 11 | 0.28 | Find single-cell RNA-seq from APP/PS1 or 5XFAD mice |
| Q7 | T3 | 10 | 4 | 2 | 0.17 | Find datasets from the Tabula Muris project |
| Q8 | T4 | 5 | 5 | 3 | 0.43 | Find two comparable snRNA-seq datasets of human kidney  |
| Q9 | T4 | 18 | 36 | 4 | 0.08 | I want to study chromatin accessibility in mouse brain  |
| Q10 | T5 | 17 | 13 | 4 | 0.15 | I'm studying liver fibrosis — what's the best dataset t |

## Scoring

| Query | App Score | Agentic Score | Notes |
|---|---|---|---|
| Q1 | | | |
| Q2 | | | |
| Q3 | | | |
| Q4 | | | |
| Q5 | | | |
| Q6 | | | |
| Q7 | | | |
| Q8 | | | |
| Q9 | | | |
| Q10 | | | |

---

## Q1 (T1)
**Query:** Find zebrafish spatial transcriptomics datasets  
**Source file:** `2026-05-12_Q1.md`

**Overlap (5):** GSE128350, GSE241156, GSE262578, GSE274407, GSE294097  
**App only (5):** GSE120509, GSE159709, GSE192740, GSE317420, GSE66688  
**Agentic only (2):** GSE192741, GSE325620

### App pipeline
*Shards: rnaseq_spatial, rnaseq_bulk | Terms: zebrafish | Expanded: Danio rerio, in situ hybridization, ISH, FISH, whole mount, larval development, embryonic stages, organ development | Candidates: 222 | spatial transcriptomics: 69 (+61 via synonyms), bulk RNA-seq: 153 (+3 via synonyms)*

## Zebrafish Spatial Transcriptomics Datasets

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE262578](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262578) | *Danio rerio* | 53 | .rds.gz (processed) | Construction of Danio rerio Asymmetrical Maps (DreAM) |
| [GSE274407](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE274407) | *Danio rerio* | 5 | RAW.tar (1.3GB) | Spatiotemporal dynamics of the developing zebrafish enteric nervous system at the whole organ level |
| [GSE159709](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE159709) | *Danio rerio* | 6 | RAW.tar (3.8GB) | Spatially resolved transcriptomics reveals the architecture of the tumor-microenvironment interface |
| [GSE241156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241156) | *Mus musculus*; *Danio rerio* | 14 | RAW.tar + Excel tables (processed) | Interspecies comparison reveals Hmga1 as driver of cardiac regeneration [TOMOseq mouse and zebrafish] |
| [GSE294097](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294097) | *Danio rerio* | 4 | RAW.tar (4.9GB) | P301S Mutant Tau-Driven Zebrafish Platform — Pharmacological GSK3β Inhibitors with Anti-Neurodegenerative Efficacy |
| [GSE128350](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128350) | Multi-species incl. *Danio rerio* | 27 | RAW.tar (15MB) | Multi-species tomo-sequencing identifies new HSC regulators in the embryonic aorta microenvironment |
| [GSE66688](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE66688) | *Danio rerio* | 1152 | .txt.gz (processed) | Spatial reconstruction of single-cell gene expression |
| [GSE192740](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192740) | Multi-species incl. *Danio rerio* | 132 | RAW.tar + .rds.gz (processed) | Spatial proteogenomics — evolutionarily-conserved hepatic macrophage niches (single cells) |
| [GSE317420](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317420) | *Danio rerio* | 27 | .txt.gz (processed) | YAP disrupts bile acid homeostasis to drive cancer-associated cachexia |
| [GSE120509](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE120509) | *Danio rerio* | 72 | .txt.gz (processed) | Multi-dimensional transcriptome analysis of an intact hematopoietic organ (CHT) for HSPC expansion |

---

### Best Matches & Notes

**Purely zebrafish, true spatial transcriptomics:**

- **GSE262578** 🏆 is the strongest pure-zebrafish spatial dataset — 53 samples using serial bulk RNA-seq tomography (tomo-seq) to build whole-embryo asymmetric expression maps (DreAM) at three developmental stages, with processed `.rds.gz` files ready for analysis.
- **GSE274407** is particularly noteworthy for **whole-organ spatial resolution of the enteric nervous system** — a rare and rich dataset covering gut neuroscience and development with 5 samples.
- **GSE159709** applies spatially resolved transcriptomics specifically to zebrafish **tumor-microenvironment** — useful for cancer-focused queries.
- **GSE294097** is a very recent (2024) dataset using spatial transcriptomics to study **Alzheimer's-like tau pathology** in zebrafish — unique intersection of neurodegenerative disease modeling and zebrafish spatial methods.

**Multi-species datasets with zebrafish spatial data:**
- **GSE241156** (TOMOseq, zebrafish + mouse cardiac regeneration) and **GSE128350** (tomo-seq across zebrafish, mouse, chicken, human) are excellent for cross-species spatial comparisons.
- **GSE192740** includes zebrafish liver spatial/single-cell data across 7 species with processed `.rds.gz` files — ideal for evolutionary comparisons.

**Tomo-seq / serial-section bulk RNA-seq (spatial by slicing):**
- **GSE66688** (1,152 samples) is a landmark early dataset for spatial single-cell gene expression reconstruction and remains one of the largest zebrafish spatial resources in GEO.
- **GSE120509** (72 samples, CHT hematopoietic organ) uses spatial dissection of a whole organ — useful for hematopoiesis researchers.

### ⚠️ Important Caveats
1. **"Spatial" here spans multiple technologies**: tomo-seq (serial sectioning + bulk RNA-seq), 10x Visium, Slide-seq, and FISH-based methods — verify the platform in the study before use.
2. Several datasets (e.g., GSE317420, GSE120509) are indexed under the spatial category due to spatial dissection approaches but are **not** spot-based Visium-style assays.
3. GSE274407 and GSE294097 have only **4–5 samples** — sufficient for discovery but limited for statistical power.
4. The multi-species datasets (GSE192740, GSE128350) require careful sample-level filtering to isolate zebrafish-specific data.

### Agentic pipeline
*Tool calls: rnaseq_spatial(zebrafish); multiomics(zebrafish, spatial)*

Here are the zebrafish spatial transcriptomics datasets found in GEO:

| Accession | Organism | Samples | Files | Title |
|---|---|---|---|---|
| [GSE262578](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262578) | *Danio rerio* | 53 | .rds.gz (processed) | Construction of Danio rerio Asymmetrical Maps (DreAM) |
| [GSE274407](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE274407) | *Danio rerio* | 5 | RAW.tar (1.3 GB) | Spatiotemporal dynamics of the developing zebrafish enteric nervous system at the whole organ level |
| [GSE294097](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294097) | *Danio rerio* | 4 | RAW.tar (4.9 GB) | P301S Mutant Tau-Driven Zebrafish Platform Enables Systematic Identification of Pharmacological GSK3β Inhibitors with Anti-Neurodegenerative Efficacy |
| [GSE325620](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325620) | *Danio rerio* | 14 | RAW.tar (1.5 GB) | Comparative single-cell multiomic analysis reveals evolutionarily conserved and species-specific cellular mechanisms mediating natural retinal aging |
| [GSE241156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241156) | *Mus musculus* + *Danio rerio* | 14 | RAW.tar + .xlsx tables | Interspecies comparison reveals Hmga1 as driver of cardiac regeneration [TOMOseq] |
| [GSE128350](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128350) | Multi-species incl. *Danio rerio* | 27 | RAW.tar (15 MB) | Multi-species tomo-sequencing identifies new major hematopoietic stem cell regulators in the embryonic aorta |
| [GSE192741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192741) | *Homo sapiens* + *Mus musculus* (+ zebrafish reference) | 15 | RAW.tar + .rds.gz (processed) | Spatial proteogenomics reveals distinct and evolutionarily-conserved hepatic macrophage niches |

---

### 🔍 Best Matches & Notes

- **[GSE262578](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262578)** is the most comprehensive **zebrafish-only** spatial dataset (53 samples), using serial bulk RNA-seq tomography (Tomo-seq) to build the *Danio rerio* Asymmetrical Maps (DreAM) during axis establishment. Processed `.rds.gz` files are available — great for reanalysis.

- **[GSE274407](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE274407)** focuses on the **enteric nervous system** development at whole-organ spatial resolution — a unique neuroscience/gut biology resource.

- **[GSE294097](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294097)** is a notable **disease model** dataset using spatial transcriptomics in a tau/Alzheimer's-like zebrafish platform — rare use case for neurodegeneration in fish.

- **[GSE325620](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325620)** is a **multiome (RNA + ATAC)** dataset focused on retinal aging — useful for eye/epigenetics research.

- **[GSE241156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241156)** and **[GSE128350](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128350)** both use **Tomo-seq** (tomographic RNA-seq) for spatial resolution and include zebrafish in cross-species comparisons.

> ⚠️ **Caveat:** Most of these datasets use **Tomo-seq** (serial sectioning + bulk RNA-seq) rather than spot-based platforms like 10x Visium. True Visium/in-situ zebrafish datasets remain rare. GSE274407 and GSE294097 are more likely to use modern spatial platforms — check the RAW files for confirmation.

---

## Q2 (T1)
**Query:** How many CITE-seq datasets profile human PBMCs?  
**Source file:** `2026-05-12_Q2.md`

**Overlap (2):** GSE213282, GSE291290  
**App only (23):** GSE100866, GSE135325, GSE144434, GSE158769, GSE164378, GSE180410, GSE190570, GSE191332, GSE196198, GSE202150, GSE205320, GSE216884, GSE226039, GSE229187, GSE229791, GSE246317, GSE269335, GSE269478, GSE277117, GSE284075, GSE295725, GSE308814, GSE314400  
**Agentic only (1):** GSE185712

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

## Summary & Notes

- **3 datasets** match CITE-seq + human PBMC across the index (confirmed across `rnaseq_singlecell`, `multiomics`, and `rnaseq_snrnaseq` shards, with no duplicates).
- All three have **processed data available** (`.h5`, `.mtx.gz`, `.csv.gz` files).
- **Best for antibody panel benchmarking:** GSE213282 — profiles 124 antibodies, making it ideal for panel design or normalization studies.
- **Best for T-cell biology:** GSE185712 — combines sorted T-cell scRNA-seq with PBMC CITE-seq from healthy donors.
- **Best for disease context:** GSE291290 — includes post-heart-transplant patients with multi-omic (CITE-seq + VDJ-seq) readouts.
- ⚠️ **Caveat:** This index covers 2015–2026 but may not capture every deposited dataset; some studies may use synonyms like "Cellular Indexing of Transcriptomes and Epitopes" or embed CITE-seq as part of larger cohort studies. A broader search (e.g., removing the PBMC filter) could surface additional datasets.

---

---

## Q3 (T2)
**Query:** Mouse kidney snRNA-seq with at least 5 samples and H5 files available  
**Source file:** `2026-05-12_Q3.md`

**Overlap (3):** GSE171417, GSE184652, GSE268494  
**App only (5):** GSE119531, GSE150284, GSE218056, GSE237816, GSE280119  
**Agentic only (7):** GSE139107, GSE220493, GSE241213, GSE244839, GSE275526, GSE282959, GSE295103

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

## ⭐ Best Matches

**Top picks for mouse kidney snRNA-seq with direct H5/processed data:**

1. **[GSE184652](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE184652)** is the standout dataset — 70 samples from a db/db diabetic kidney disease model with multiple drug treatments (ACEi, SGLT2i, Rosiglitazone), including CellBender-processed count matrices and metadata. Ideal for disease modeling and drug response studies.

2. **[GSE268494](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE268494)** — 32-sample multiome dataset (snRNA-seq + snATAC-seq) of polycystic kidney disease (PKD) in mice, with well-organized RDS processed files. Good for trajectory/regulatory analyses.

3. **[GSE171417](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171417)** — 9 samples focused on proximal tubule responses to acute kidney injury (IRI model, 7-day and 28-day timepoints). Clean UMI count matrices provided separately by condition.

4. **[GSE119531](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119531)** — A methodological benchmark paper directly comparing snRNA-seq vs. scRNA-seq in adult mouse kidney (healthy + UUO fibrosis model). Useful as a reference atlas.

---

## ⚠️ Important Caveats

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

## 🔍 Best Matches & Notes

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

---

## Q4 (T2)
**Query:** Human bulk RNA-seq cancer datasets with processed count matrices (CSV or TSV files)  
**Source file:** `2026-05-12_Q4.md`

**Overlap (0):** none  
**App only (20):** GSE100327, GSE103424, GSE110875, GSE112509, GSE121827, GSE122509, GSE123619, GSE124751, GSE138717, GSE149184, GSE149262, GSE151159, GSE192877, GSE228101, GSE229032, GSE280284, GSE304485, GSE327166, GSE89225, GSE97774  
**Agentic only (0):** none

### App pipeline
*Shards: rnaseq_bulk | Terms: cancer, processed, count, matrices, files | Expanded: RNA-seq, transcriptomics, gene expression, HTSeq, featureCounts, TCGA, COUNT, DESeq2 | Candidates: 249 | bulk RNA-seq: 249 (+99 via synonyms)*

## Human Bulk RNA-seq Cancer Datasets with Processed Count Matrices (CSV/TSV Files)

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE304485](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE304485) | Homo sapiens | 6,310 | `expression_data.csv.gz` (794MB) | Bulk RNA-Seq gene expression profiles from 13 TCGA cancer types and normal tissues for tumor classification |
| [GSE327166](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327166) | Homo sapiens | 89 | `bulkRNA_rawcounts_matrix.tsv.gz`, `bulkRNA_TPM_matrix.tsv.gz` | Bulk RNA-seq profiling of pleural mesothelioma and comparator pleural specimens |
| [GSE229032](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229032) | Homo sapiens | 73 | `AML_Samples_RNASeq_Processed_counts_corrected.csv.gz` | Transcriptomic profiling of human AML cell lines and primary AML samples |
| [GSE121827](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE121827) | Homo sapiens | 222 | `RNAseq_PD1_raw_counts.csv.gz`, `RNAseq_Tfh_raw_counts.csv.gz`, `RNAseq_Treg_raw_counts.csv.gz` (+ normalized) | RNA-seq analysis on Tfh and Treg before and after abatacept treatment |
| [GSE89225](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE89225) | Homo sapiens | 54 | `Illumina_counts.csv.gz`, `Iontorrent_counts.csv.gz` | Regulatory T cells exhibit distinct features in human breast cancer |
| [GSE110875](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE110875) | Homo sapiens | 80 | `ProcessedData.txt.gz` | RNA sequencing data for diffuse gastric cancer |
| [GSE112509](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE112509) | Homo sapiens | 80 | `DESeq2_normalized_counts.txt.gz` | RNA-seq identifies different transcriptomic types and developmental trajectories of primary melanomas |
| [GSE103424](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103424) | Homo sapiens | 36 | `DESeq2_norm_data.txt.gz`, `HTseq_count.txt.gz` | Integrating resistance functions to predict response to induction chemotherapy in de novo AML |
| [GSE228101](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE228101) | Homo sapiens | 26 | `Raw_RNA_sequencing_count_data.txt.gz`, `Processed_RNA_sequencing_count_data.txt.gz`, VST normalized | Relapsed atypical teratoid/rhabdoid tumors (AT/RT) reveal distinct features of progression |
| [GSE280284](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE280284) | Homo sapiens | 12 | `gene.count.anno.txt.gz`, `Processed_data_files.txt.gz` | Identification and validation of KIF20A for predicting prognosis in breast cancer |
| [GSE192877](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192877) | Homo sapiens | 12 | `CD44_OE_HCT116_SW480_processed.counts.txt.gz` | Alternative spliced genes downstream of EMT in colon cancer |
| [GSE97774](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE97774) | Homo sapiens | 44 | `counts.csv.gz` | Cell-cycle-resolved RNA expression in neuroblastoma cells upon MYCN knockdown |
| [GSE123619](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE123619) | Homo sapiens | 12 | `expression_counts.csv.gz`, `expression_fpkm.csv.gz` | Distinct structural classes of activating FOXA1 alterations in prostate cancer [RNA-Seq] |
| [GSE122509](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122509) | Homo sapiens | 12 | `counts_matrix.txt.gz` | SWI/SNF mutations mediate resistance to ibrutinib plus venetoclax in mantle cell lymphoma |
| [GSE149184](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE149184) | Homo sapiens | 27 | `Molm13_compound-10_EPZ5676_raw_counts_rmdup.txt.gz` | Novel Inhibitors of DOT1L Show Potent Antileukemic Activity in PDX models |
| [GSE151159](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE151159) | Homo sapiens | 32 | `all_final_DESeq2_batch+response_all_countsNormalized.txt.gz` (multiple) | Gene expression profiling predicts sensitivity of CLL cells to dasatinib |
| [GSE138717](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE138717) | Homo sapiens | 17 | `PCD_Norm_counts_DESEQ2_FINAL_HUGO_T1.txt.gz` | Phase II Study: Pomalidomide + Cyclophosphamide + Dexamethasone in Relapsed/Refractory Multiple Myeloma |
| [GSE124751](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE124751) | Homo sapiens | 206 | `rna.processed.hcc_I.log2.txt.gz` | Gene expression profile of hepatocellular carcinoma with marked immune cell infiltration I |
| [GSE149262](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE149262) | Homo sapiens | 36 | `IL22KRAS_featurecounts.csv.gz`, `IL22KRAS_log2RPKM1.csv.gz` | Transcriptional changes in DLD-1 KRAS MUT/WT colorectal cancer cells following IL-22/IL-6 stimulation |
| [GSE100327](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE100327) | Homo sapiens | 30 | `Scully_raw_gene_counts.txt.gz` | RNA-seq profiles of five pancreatic cancer cell lines engineered to express E47 |

---

### Best Matches & Key Notes

**Top picks for large-scale human cancer count matrices:**

- 🏆 **GSE304485** is the standout dataset for breadth: **6,310 samples** across **13 TCGA cancer types**, delivered as a single `expression_data.csv.gz`. This is ideal for pan-cancer classification or benchmarking — but note it has

### Agentic pipeline
*Tool calls: rnaseq_bulk(cancer, human, csv); rnaseq_bulk(tumor, human, csv); rnaseq_bulk(carcinoma, human, csv); rnaseq_bulk(breast cancer, human, count, csv); rnaseq_bulk(lung cancer, human, count, csv); rnaseq_bulk(colorectal, human, count, csv)*

(pipeline error)

---

## Q5 (T2)
**Query:** H3K27ac ChIP-seq datasets in mouse embryonic stem cells  
**Source file:** `2026-05-12_Q5.md`

**Overlap (12):** GSE103262, GSE116990, GSE131924, GSE160890, GSE160974, GSE201101, GSE232845, GSE266929, GSE309460, GSE60204, GSE66023, GSE98604  
**App only (6):** GSE154379, GSE195856, GSE212994, GSE70661, GSE75722, GSE89220  
**Agentic only (7):** GSE108114, GSE135562, GSE161993, GSE168688, GSE189561, GSE193085, GSE213501

### App pipeline
*Shards: chipseq | Terms: H3K27ac, ChIP, embryonic, stem | Expanded: H3K27 acetylation, active chromatin, enhancer mapping, mESC, ES cells, pluripotent stem cells, histone acetylation, open chromatin | Candidates: 236 | ChIP-seq: 236 (+86 via synonyms)*

## H3K27ac ChIP-seq Datasets in Mouse Embryonic Stem Cells

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE160974](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE160974) | Mus musculus | 52 | .xlsx, .txt.gz (processed) | Genome-wide maps of histone PTMs and co-factors in pluripotent mESCs and epiblast-like cells (EpiLCs) |
| [GSE160890](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE160890) | Mus musculus | 87 | .bw (processed, large) | KMT2C/KMT2D Histone Methyltransferase Activity Dependent Chromatin Organization at Enhancers during ESC Differentiation |
| [GSE154379](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE154379) | Mus musculus | 136 | .bed.gz (processed peaks) | Symmetric inheritance of parental histones governs epigenome maintenance and stem cell identity |
| [GSE116990](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116990) | Mus musculus | 111 | RAW.tar (122.8 GB) | ChIPseq on H3K27ac, H4ac, H3K9ac, H3K4me3, H3K4me1, H3K27me3 and H2AK119Ub on TX1072 mESCs |
| [GSE266929](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE266929) | Mus musculus | 33 | .bed.gz (processed) | Rescuing DNMT1 Fails to Fully Reverse Molecular Repercussions of Its Loss in mESCs |
| [GSE232845](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE232845) | Mus musculus | 46 | .narrowPeak.gz, RAW.tar (processed) | Effect of JMJD2/KDM4 triple-knockout on gene expression in mESCs |
| [GSE131924](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE131924) | Mus musculus | 8 | RAW.tar | Dynamic Lineage Priming by ERK via Transcription Factor-Independent Enhancer Regulation [H3K27ac ChIP-seq] |
| [GSE98604](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE98604) | Mus musculus | 8 | RAW.tar (9.9 GB) | Effects of dominant-negative G784E Smarca4 mutation on enhancer marks in mESCs |
| [GSE309460](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309460) | Mus musculus | 25 | .bed.gz, RAW.tar (processed peaks) | Post-mitotic transcriptional activation and 3D regulatory interactions; cohesin depletion in mESCs |
| [GSE212994](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212994) | Mus musculus | 15 | .bw, .bed.gz (processed) | Systematic mapping of 3D enhancer interactions across early mouse developmental cell lines [H3K27ac] |
| [GSE201101](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE201101) | Mus musculus | 8 | RAW.tar | ChIP-Seq of p53, H3K4me3 and H3K27ac in mESCs with/without DNA damage |
| [GSE75722](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE75722) | Mus musculus | 19 | .bed.gz (processed) | Lineage-specific enhancers activate self-renewal genes in macrophages and embryonic stem cells |
| [GSE60204](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60204) | Mus musculus | 54 | .bed.gz (processed peaks) | Quantitative Dynamics of Chromatin Remodeling during Germ Cell Specification from mESCs |
| [GSE66023](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE66023) | Mus musculus; Homo sapiens | 10 | .bedGraph.gz, .bed.gz (processed) | Histone H3 globular domain acetylation identifies new class of enhancers in mESCs |
| [GSE103262](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103262) | Mus musculus | 24 | .bw (processed bigWigs) | RNAseq and ChIPseq on mESCs and Sorted Mesendoderm Progenitor Cells [H3K27ac + H3K4me3] |
| [GSE195856](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE195856) | Mus musculus | 41 | .bed.gz (processed peaks) | H3K18la marks active tissue-specific enhancers — includes ESC and ESC-2i conditions |
| [GSE89220](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE89220) | Mus musculus | 22 | .csv.gz, RAW.tar (processed) | ChIP-seq of H3K27ac and H3K9me3 on MEF-derived cells during reprogramming to iPSCs |
| [GSE70661](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE70661) | Mus musculus | 20 | RAW.tar | Taf4 required for preinitiation complex formation; H3K27ac profiled in ESCs and embryoid bodies |

---

### Best Matches & Key Notes

**Top picks for canonical H3K27ac in undifferentiated mESCs:**

- **GSE160974** (52 samples) is the most comprehensive reference dataset — it directly profiles H3K27ac alongside other PTMs (H3K27me1/2/3, Med1, Pol-II) in both mESCs and EpiLCs with processed output files (.xlsx). Excellent for enhancer/promoter annotation.
- **GSE116990** (111 samples) is the largest dataset and includes H3K27ac in WT, Hdac3-KO, and Hdac3-AID TX1072 female mESCs, making it ideal for studying HDAC-dependent acetylation dynamics during X-chromosome inactivation. ⚠️ RAW data only (122.8 GB tar).
- **GSE160890** (87 samples) profiles H3K27ac in both ESCs and NPCs ± MLL3/4 catalytic mutations, with ready-to-use .bw bigWig files — great for enhancer activity comparisons across differentiation.
- **GSE266929** and **GSE232845** are recent (2023–2024) datasets with processed peak files directly from mESCs, studying DNA methylation and KDM4 demethylase effects respectively.
- **GSE131924** is the most specifically titled H3K27ac mESC ChIP-seq dataset (ERK/enhancer regulation), with a small, clean 8-sample design.

### Agentic pipeline
*Tool calls: chipseq(H3K27ac, embryonic stem, mouse); chipseq(H3K27ac, mESC)*

Here are the H3K27ac ChIP-seq datasets in mouse embryonic stem cells (mESCs) found across GEO:

---

## H3K27ac ChIP-seq — Mouse Embryonic Stem Cells

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE160974](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE160974) | *Mus musculus* | 52 | .xlsx, .txt.gz | Genome-wide maps of histone PTMs and co-factors in pluripotent mESCs and epiblast-like cells (EpiLCs) |
| [GSE160890](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE160890) | *Mus musculus* | 87 | .bw (many) | KMT2C/KMT2D (MLL3/MLL4) Histone Methyltransferase Activity Dependent Chromatin Organization at Enhancers during ESC Differentiation |
| [GSE116990](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116990) | *Mus musculus* | 111 | RAW.tar (122.8 GB) | ChIPseq on H3K27ac, H4ac, H3K9ac, H3K4me3, H3K4me1, H3K27me3 and H2AK119Ub in TX1072 WT & Hdac3-/- mESCs |
| [GSE189561](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE189561) | *Mus musculus* | 86 | RAW.tar (58.2 GB) | Histone modifications and SOX2 occupancy in asynchronous and mitotic mESCs |
| [GSE161993](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161993) | *Mus musculus* (+human/Drosophila) | 110 | .bw, .bed.gz | BAP1 constrains pervasive H2AK119ub1 to control transcriptional potential of the genome |
| [GSE232845](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE232845) | *Mus musculus* | 46 | .narrowPeak.gz, RAW.tar | JMJD2/KDM4 triple-KO effects on H3K27ac and chromatin in mESCs |
| [GSE266929](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE266929) | *Mus musculus* | 33 | .bed.gz, RAW.tar | Rescuing DNMT1 Fails to Fully Reverse Repercussions of Its Loss in mESCs |
| [GSE135562](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE135562) | *Mus musculus* | 18 | .bw (WT & PML KO) | ChIP-seq analysis of wild-type and PML KO mESCs (H3K27ac, H3K27me3, H3K4me3, H3K9me3) |
| [GSE131924](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE131924) | *Mus musculus* | 8 | RAW.tar | Dynamic Lineage Priming by ERK is Driven by Transcription Factor-Independent Enhancer Regulation |
| [GSE98604](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE98604) | *Mus musculus* | 8 | RAW.tar | Effects of dominant-negative G784E Smarca4 mutation on enhancer marks in mESCs |
| [GSE201101](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE201101) | *Mus musculus* | 8 | RAW.tar | ChIP-Seq of p53, H3K4me3, and H3K27ac in mESCs with/without DNA damage |
| [GSE193085](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE193085) | *Mus musculus* | 11 | .bw | HDAC activity modulation reprogramming mESC to trophoblast stem cell (H3K27ac, H3K9ac) |
| [GSE309460](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309460) | *Mus musculus* | 25 | .bed.gz, RAW.tar | Post-mitotic transcriptional activation and 3D regulatory interactions: sensitivity to cohesin depletion |
| [GSE103262](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103262) | *Mus musculus* | 24 | .bw | H3K27ac & H3K4me3 in mESCs and sorted Mesendoderm Progenitor Cells |
| [GSE60204](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60204) | *Mus musculus* | 54 | .bed.gz, .tdf | Chromatin Remodeling during Germ Cell Specification from mESCs (H3K27ac, H3K4me3, H3K27me3, H3K9me2) |
| [GSE168688](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE168688) | *Mus musculus* | 14 | .txt.gz | ChIP-seq of H3K27ac & H3K9me3 in mESC treated with doxorubicin (DNA damage) |
| [GSE66023](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE66023) | *Mus musculus* + Human | 10 | .bedGraph.gz, .bed.gz | Histone H3 globular domain acetylation (H3K64ac, H3K122ac, H3K27ac) identifies new class of enhancers in mESCs |
| [GSE213501](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE213501) | *Mus musculus* | 30 | .hic, .mcool, RAW.tar | Enhancer Cis-Elements Instruct Promoter-Enhancer Interaction (H3K27ac HiChIP + ChIP-seq in mESCs) |

---

### Highlights & Notes

- **Best reference datasets (clean mESC H3K27ac profiling):**
  - **GSE160974** (52 samples) is a comprehensive multi-PTM atlas in mESCs and EpiLCs — excellent reference for enhancer/promoter annotation.
  - **GSE116990** (111 samples) is the largest dataset, covering multiple histone marks in WT and Hdac3-KO mESCs during X-chromosome inactivation.
  - **GSE189561** (86 samples) covers H3K27ac alongside 7 other marks in both asynchronous and mitotic cells — valuable for cell-cycle studies.

- **Perturbation / KO studies:**
  - **GSE160890** — MLL3/MLL4 KO; includes ESC→NPC differentiation
  - **GSE232845** — JMJD2/KDM4 triple KO
  - **GSE135562** — PML KO; very clean 4-mark panel with processed .bw files
  - **GSE266929** — DNMT1 loss/rescue; multi-mark panel with processed .bed.gz peaks

- **DNA damage context:** GSE201101 and GSE168688 both profile H3K27ac in mESCs following genotoxic stress.

- **3D chromatin / HiChIP:** GSE213501 includes H3K27ac HiChIP in mESCs — useful for enhancer–promoter loop analysis.

- **Caveat:** GSE66023, GSE161993, and GSE108114 include both mouse and human samples — filter by organism when downloading.

---

## Q6 (T3)
**Query:** Find single-cell RNA-seq from APP/PS1 or 5XFAD mice  
**Source file:** `2026-05-12_Q6.md`

**Overlap (11):** GSE161224, GSE161227, GSE175389, GSE176085, GSE178296, GSE198027, GSE199027, GSE208683, GSE225503, GSE230116, GSE235527  
**App only (9):** GSE148405, GSE160527, GSE160529, GSE176032, GSE192616, GSE192964, GSE223394, GSE226938, GSE271192  
**Agentic only (20):** GSE140399, GSE140510, GSE143758, GSE224647, GSE243576, GSE249611, GSE255965, GSE262881, GSE266046, GSE273139, GSE273690, GSE287555, GSE288410, GSE295077, GSE296091, GSE296662, GSE298597, GSE302153, GSE307686, GSE327886

### App pipeline
*Shards: rnaseq_singlecell, rnaseq_bulk | Terms: APP/PS1, 5XFAD | Expanded: amyloid precursor protein, presenilin-1, PS1, 5X familial Alzheimer disease, FAD, Alzheimer disease, amyloid-beta, neuroinflammation | Candidates: 200 | scRNA-seq: 100 (via synonyms), bulk RNA-seq: 100 (+98 via synonyms)*

## scRNA-seq Datasets from APP/PS1 or 5XFAD Mice

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE226938](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE226938) | Mus musculus | 36 | GSE226938_RAW.tar (6MB) | Early amyloid-induced changes in microglia gene expression in APP/PS1 mice [scRNA-seq] |
| [GSE271192](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE271192) | Mus musculus | 17 | GSE271192_cell_metadata.txt.gz, GSE271192_RAW.tar | Single cell RNA seq analysis of microglia from aged wild-type, NLRP3-/-, APP/PS1 and APP/PS1.NLRP3-/- mice |
| [GSE160529](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE160529) | Mus musculus | 10 | GSE160529_RAW.tar (9MB) | Single-cell and bulk sequencing of endothelial cells of WT and APP/PS1 mice |
| [GSE160527](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE160527) | Mus musculus | 1 | GSE160527_RAW.tar (9MB) | Single-cell sequencing of endothelial cells of WT and APP/PS1 mice |
| [GSE198027](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198027) | Mus musculus | 34 | GSE198027_RAW.tar (1.1GB) | Diversity of astrocytes across the mouse CNS [scRNA-seq] — includes APP/PS1dE9 |
| [GSE235527](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE235527) | Mus musculus | 12 | GSE235527_RAW.tar (362MB) | Young bone marrow transplantation rejuvenates immune cells and attenuates Aβ in APP/PS1 mice |
| [GSE223394](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE223394) | Mus musculus | 4 | GSE223394_RAW.tar (169MB) | Endothelial Cell Senescence in APPswe/PS1dE9 Mouse Model (scRNA-seq) |
| [GSE208683](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE208683) | Mus musculus | 8 | GSE208683_Allcell_6m_UMI_matrix.txt.gz (181MB), GSE208683_Microglia_6m_UMI_matrix.txt.gz | Single-nuclei transcriptome sequencing of 5xFAD mouse brain hemisphere with myelin dysfunction |
| [GSE176032](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE176032) | Mus musculus | 6 | GSE176032_metadata*.csv.gz, GSE176032_RAW.tar (65MB) | CSF1R inhibition rescues tau pathology in A/T/N model with 5xFAD pathologies |
| [GSE199027](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE199027) | Mus musculus | 9 | GSE199027_RAW.tar (543MB) | Bace-1 inhibition facilitates transition from homeostatic microglia to DAM-1 [5xFAD] |
| [GSE225503](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225503) | Mus musculus | 8 | GSE225503_adapoe.rds.gz (2.5GB), GSE225503_mglia_only.rds.gz, GSE225503_multiome*.rds.gz | scRNA-seq and scATAC-seq of CD45+ cells from 5XFAD mice with distinct APOE alleles across age |
| [GSE192616](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192616) | Mus musculus | 295 | GSE192616_5xFAD_adata.h5ad.gz, GSE192616_sc_adata*.h5ad.gz (up to 1.2GB) | Multi-omics and 3D-imaging reveal bone heterogeneity and unique calvaria cells in neuroinflammation [5xFAD] |
| [GSE148405](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE148405) | Mus musculus | 1152 | GSE148405_counts.csv.gz (8MB) | Single cell RNA-seq of microglia isolated from different brain regions of WT and 5xFAD mice |
| [GSE161227](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161227) | Mus musculus | 24 | GSE161227_RAW.tar (737MB) | Cortical scRNA-seq of microglia-specific TREM2 inducible models — middle stage amyloid [5xFAD] |
| [GSE161224](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161224) | Mus musculus | 24 | GSE161224_RAW.tar (1.5GB) | Cortical scRNA-seq of microglia-specific TREM2 inducible models — early stage amyloid [5xFAD] |
| [GSE230116](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE230116) | Mus musculus | 8 | GSE230116_RAW.tar (526MB) | BACE1 regulates Clusterin in astrocytes for β-amyloid clearance [5xFAD scRNA-seq] |
| [GSE192964](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192964) | Mus musculus | 15 | GSE192964_gene_count*.txt.gz, GSE192964_RAW.tar (70MB) | Autophagy restricts senescence in microglia engaging amyloid plaques [5xFAD] |
| [GSE178296](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE178296) | Mus musculus | 16 | GSE178296_Raw_gene_counts_matrix.csv.gz, GSE178296_TPM_gene_counts_matrix.csv.gz | Transcriptome profiling of microglia in Cnp null mice with 5xFAD background |
| [GSE175389](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE175389) | Mus musculus | 11 | GSE175389_RAW.tar (2MB) | Deletion of Abi3 exacerbates neuropathological features in 5XFAD model [scRNA-seq] |
| [GSE176085](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE176085) | Mus musculus | 63 | GSE

### Agentic pipeline
*Tool calls: rnaseq_singlecell(APP/PS1, mouse); rnaseq_singlecell(5XFAD, mouse); rnaseq_snrnaseq(APP/PS1, mouse); rnaseq_snrnaseq(5XFAD, mouse)*

Here is a comprehensive table of all findings, organized by model:

---

## 🧠 APP/PS1 Datasets (scRNA-seq)

| Accession | Organism | Samples | Files | Title |
|---|---|---|---|---|
| [GSE198027](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198027) | Mus musculus | 34 | RAW.tar (1.1 GB) | Diversity of astrocytes across the mouse CNS [scRNA-seq] |
| [GSE235527](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE235527) | Mus musculus | 12 | RAW.tar (362 MB) | Young bone marrow transplantation rejuvenates immune cells, attenuates Aβ accumulation in APP/PS1 mice |
| [GSE243576](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE243576) | Mus musculus | 4 | .h5 (193 MB) ✅ | Vascular senescence and BBB breakdown in Alzheimer's disease models (APP/PS1) |
| [GSE249611](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE249611) | Mus musculus | 10 | .csv.gz ✅ | Inflammasome signaling in β-amyloid neuropathology — NLRP3 KO × APP/PS1 |

---

## 🧠 5XFAD Datasets (scRNA-seq)

| Accession | Organism | Samples | Files | Title |
|---|---|---|---|---|
| [GSE161227](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161227) | Mus musculus | 24 | RAW.tar (737 MB) | Cortical scRNA-seq of microglia-specific TREM2 inducible models — middle stage amyloid (5xFAD) |
| [GSE161224](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161224) | Mus musculus | 24 | RAW.tar (1.5 GB) | Cortical scRNA-seq of microglia-specific TREM2 inducible models — early stage amyloid (5xFAD) |
| [GSE175389](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE175389) | Mus musculus | 11 | RAW.tar (2 MB) | Abi3 gene deletion exacerbates neuropathology in 5XFAD |
| [GSE176085](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE176085) | Mus musculus | 63 | RAW.tar (37 MB) | Blood-borne macrophages in AD — TREM2-independent pathway (Trem2⁻/⁻ × 5xFAD) |
| [GSE199027](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE199027) | Mus musculus | 9 | RAW.tar (543 MB) | BACE-1 inhibition and homeostatic-to-DAM microglial transition (5xFAD) |
| [GSE208683](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE208683) | Mus musculus | 8 | UMI matrix .txt.gz ✅ | Single-nuclei transcriptome of 5xFAD brain with myelin dysfunction |
| [GSE178296](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE178296) | Mus musculus | 16 | .csv.gz ✅ | Microglia transcriptomics in Cnp-null × 5xFAD mice |
| [GSE224647](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE224647) | Mus musculus | 8 | .rds.gz (2.9 GB) ✅ | Cell-type vulnerability in Alzheimer's — subcortical limbic circuit (5XFAD) |
| [GSE225503](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225503) | Mus musculus | 8 | .rds.gz + RAW.tar ✅ | scRNA-seq & scATAC-seq of CD45+ brain immune cells — 5XFAD × APOE alleles |
| [GSE230116](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE230116) | Mus musculus | 8 | RAW.tar (526 MB) | BACE1 regulates Clusterin in astrocytes for Aβ clearance (5xFAD) |
| [GSE266046](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE266046) | Mus musculus | 2 | RAW.tar (79 MB) | Astrocyte-to-neuron conversion in 5xFAD hippocampus |
| [GSE273139](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE273139) | Mus musculus | 2 | RAW.tar (321 MB) | MR1/MAIT cell axis reduces dystrophic neurites in 5XFAD |
| [GSE273690](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE273690) | Mus musculus | 48 | RAW.tar (1.7 GB) | ADGRG1 promotes protective microglial response in AD (5xFAD) |
| [GSE287555](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE287555) | Mus musculus | 5 | RAW.tar (74 MB) | CD8+ T cell roles in regulating amyloid pathology (5xFAD) |
| [GSE288410](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288410) | Mus musculus | 4 | .mtx.gz ✅ | ACE expression in microglia reduces Aβ deposition (5xFAD) |
| [GSE296662](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296662) | Mus musculus | 2 | RAW.tar (386 MB) | Microglial cGAS deletion alleviates Aβ pathogenesis (5xFAD) |
| [GSE298597](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE298597) | Mus musculus | 12 | RAW.tar (1.2 GB) | Tet2-mutant peripheral myeloid cell CNS infiltration protects from AD (5xFAD) |
| [GSE307686](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307686) | Mus musculus | 15 | RAW.tar (12.6 GB) | TREM2-T96K gain-of-function mutation impairs microglial function (5xFAD) |
| [GSE327886](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE327886) | Mus musculus | 6 | MTX, RDS, TSV ✅ | Brain-spleen axis disruption impairs monocyte-microglia communication (5xFAD) |

---

## 🧠 5XFAD Datasets (snRNA-seq)

| Accession | Organism | Samples | Files | Title |
|---|---|---|---|---|
| [GSE140510](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE140510) | Mus musculus | 12 | RAW.tar (704 MB) | Human & mouse snRNA-seq — TREM2-dependent responses in AD (5XFAD, 7 months) |
| [GSE140399](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE140399) | Mus musculus | 8 | RAW.tar (71 MB) | Human & mouse snRNA-seq — TREM2-dependent responses in AD (5XFAD, 15 months) |
| [GSE143758](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE143758) | Mus musculus | 37 | .csv.gz ✅ | Single-nuclei RNA-seq of 5xFAD brain — disease-associated astrocytes (DAAs) |
| [GSE255965](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE255965) | Mus musculus | 6 | .mtx.gz + .csv.gz ✅ | Sex-specific disease progression across genotypes in 5xFAD (snRNA-seq) |
| [GSE262881](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262881) | Mus musculus | 24 | RAW.tar (14.0 GB) | Single-cell atlas of **all cell types** across the entire 5xFAD brain |
| [GSE295077](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295077) | Mus musculus | 16 | .rds ✅ | BBB impairment and cerebral metabolism in prodromal 5XFAD (snRNA-seq) |
| [GSE302153](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE302153) | Mus musculus | 32 | RAW.tar (2.0 GB) | Age-related transcriptomic changes in dorsal/ventral hippocampus — 5xFAD |
| [GSE296091](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296091) | Mus musculus | 8 | RAW.tar (10.5 GB) | Inter-cellular communications during AD pathogenesis — 5xFAD + human entorhinal cortex |

---

## 🔍 Highlights & Caveats

### 🌟 Top Picks
- **[GSE262881](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262881)** — A comprehensive **whole-brain atlas** of all cell types across 5xFAD mice; largest snRNA-seq resource here (24 samples, 14 GB).
- **[GSE176085](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE176085)** — Largest scRNA-seq study (63 samples); focuses on blood-borne macrophage vs. microglia contributions.
- **[GSE143758](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE143758)** — Timecourse snRNA-seq (3 timepoints) in hippocampus/cortex of 5xFAD; identifies disease-associated astrocytes (DAAs).
- **[GSE225503](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225503)** — Multimodal (scRNA-seq + scATAC-seq) with APOE allele × 5XFAD design; RDS files ready for R analysis ✅.
- **[GSE249611](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE249611)** — APP/PS1 timecourse (3m, 6m, 9m) with NLRP3 KO; processed .csv.gz files available ✅.

### ⚠️ Caveats
- Datasets marked ✅ have **immediately usable processed data** (.h5, .rds, .mtx.gz, .csv.gz). Others require extraction from RAW tarballs.
- **GSE140510** and **GSE140399** are companion datasets from the same study (7 vs. 15 months), ideal for **longitudinal comparison**.
- **GSE161224/GSE161227** are paired early vs. middle amyloid-stage scRNA-seq from the same TREM2 inducible model.
- The 5XFAD datasets skew heavily toward **microglial/immune** biology; astrocyte and neuronal focus studies are fewer.

---

## Q7 (T3)
**Query:** Find datasets from the Tabula Muris project  
**Source file:** `2026-05-12_Q7.md`

**Overlap (2):** GSE109774, GSE132042  
**App only (8):** GSE106707, GSE120745, GSE121386, GSE143435, GSE81686, GSE81904, GSE82187, GSE87631  
**Agentic only (2):** GSE132040, GSE149590

### App pipeline
*Shards: rnaseq_singlecell, rnaseq_bulk, rnaseq_snrnaseq, rnaseq_spatial | Terms: Tabula, Muris, project | Expanded: Mus musculus, FACS, droplet-based scRNA-seq, tissue atlases, single-cell transcriptomics, organ mapping, cell type annotation, Smart-seq2 | Candidates: 300 | scRNA-seq: 100 (via synonyms), bulk RNA-seq: 100 (via synonyms), snRNA-seq: 100 (via synonyms), spatial transcriptomics: 100 (via synonyms)*

# Tabula Muris Dataset Search Results

**Important Notice Upfront:** The Tabula Muris project has a **specific, well-known GEO accession** — but it does **not appear in the search results returned**. The canonical Tabula Muris accessions are:

- **[GSE109774](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109774)** — Tabula Muris (FACS + Smart-seq2, 20 organs)
- **[GSE132042](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE132042)** — Tabula Muris Senis (aging atlas, 18 tissues)

Neither was returned by the index search. The results below are the **closest matches** from the search results, but they are **not** Tabula Muris data.

---

## Closest Returned Datasets (Partial Matches Only)

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE87631](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE87631) | *Mus musculus* | 1,152 | GSE87631_RAW.tar (134MB) | Single Cell RNA-Sequencing using Smart-seq2 of young and old murine hematopoietic stem cells |
| [GSE82187](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE82187) | *Mus musculus* | 1,208 | GSE82187_cast_all_forGEO.csv.gz (21MB) | Cellular Taxonomy of the Mouse Striatum as Revealed by Single-Cell RNAseq |
| [GSE81686](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE81686) | *Mus musculus* | 93 | GSE81686_macrophages_bulk.csv.gz (20MB) | Differentiation and specification of resident tissue macrophages [SMART-Seq2] |
| [GSE121386](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE121386) | *Mus musculus* | 764 | GSE121386_SI.counts.txt.gz, GSE121386_spleen.counts.txt.gz | Molecular and functional heterogeneity of IL-10-producing CD4+ T cells [Mouse SMART-seq2] |
| [GSE81904](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE81904) | *Mus musculus* | 6 | GSE81904_BipolarUMICounts_Cell2016.txt.gz (43MB); .Rdata.gz (109MB) | Drop-Seq analysis of P17 FACS sorted retinal cells |
| [GSE106707](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE106707) | *Mus musculus* | 3,417 | GSE106707_expression_data.tab.gz (3MB) | Single cell RNA sequencing of interneurons of the mouse dorsolateral striatum II |
| [GSE120745](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE120745) | *Mus musculus* | 2,688 | GSE120745_geosubmission_counts.csv.gz (22MB) | Single cell RNA-seq of microglia cells from normal mouse brain at three ages |
| [GSE143435](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE143435) | *Mus musculus* | 5 | FACSatlas_normalizeddata.txt.gz (multiple, up to 108MB) | Single-cell transcriptomic atlas of FACS-sorted mouse muscle tissue cells |

---

## Explanation and Key Caveats

### ⚠️ Primary Caveat: Tabula Muris Not Found
The **Tabula Muris** (Tabula Muris Consortium, *Nature* 2018) is one of the most cited mouse single-cell atlases. It profiled **~100,000 cells across 20 organs** from *Mus musculus* using both:
- **FACS + Smart-seq2** (full-length transcripts, ~44,000 cells)
- **Microfluidic droplets (10x Genomics)** (~55,000 cells)

The canonical accession **GSE109774** was not returned by this index search, suggesting it may be outside the indexed date range, indexed under different keywords, or requires a direct accession lookup.

### Best Partial Matches from Results
- **GSE87631** and **GSE82187** are the closest in spirit — large-scale, multi-sample, FACS + Smart-seq2 in mouse — but are focused on specific tissues (HSCs, striatum), not multi-organ atlases.
- **GSE143435** ("FACS atlas of mouse muscle tissue") explicitly uses the term "atlas" and FACS sorting with 10X, making it the most conceptually similar dataset returned.
- **GSE81904** is notable as a Drop-seq dataset with large processed data files (.Rdata, .txt.gz) with good reuse potential.

### Recommended Next Steps
1. **Access directly**: [GSE109774](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109774) (Tabula Muris) and [GSE132042](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE132042) (Tabula Muris Senis)
2. **Also check**: The Tabula Muris data is also hosted at **CZI CELLxGENE** and **figshare** with `.h5ad` files for direct AnnData/Scanpy use.

### Agentic pipeline
*Tool calls: rnaseq_singlecell(Tabula Muris); rnaseq_snrnaseq(Tabula Muris); rnaseq_bulk(Tabula Muris); multiomics(Tabula Muris); rnaseq_singlecell(Tabula Muris Senis)*

Here are all the Tabula Muris datasets found in the index:

---

## Tabula Muris Datasets

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE109774](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109774) | *Mus musculus* | 46 | Per-tissue `.tar.gz` archives (20 tissues, ~374 MB RAW) | Tabula Muris: Transcriptomic characterization of 20 organs and tissues from *Mus musculus* at single cell resolution |
| [GSE132042](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE132042) | *Mus musculus* | 996 | `GSE132042_RAW.tar` (5.1 GB) | Tabula Muris (SuperSeries) |
| [GSE132040](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE132040) | *Mus musculus* | 947 | `.csv.gz` (38 MB) + metadata | Tabula Muris Senis: Bulk Sequencing |
| [GSE149590](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE149590) | *Mus musculus* | 2 | `GSE149590_RAW.tar` (4.0 GB) | Tabula Muris Senis (scRNA-seq) |

---

### Summary & Notes

1. **[GSE109774](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109774)** — The **original Tabula Muris** (2018, *Nature*). Single-cell RNA-seq (Smart-seq2 + 10x Genomics) across **20 organs and tissues** from young adult mice (~3 months). Processed data is available as per-tissue `.tar.gz` archives. ✅ Processed data available.

2. **[GSE132042](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE132042)** — A **SuperSeries** (996 samples) likely encompassing the **Tabula Muris Senis** project, which extended profiling across the mouse lifespan (ages 1–30 months). The large RAW tar (5.1 GB) suggests processed expression matrices are bundled. ✅ Processed data available.

3. **[GSE132040](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE132040)** — **Tabula Muris Senis bulk RNA-seq** component (947 samples across organs and ages). Processed as a `.csv.gz` count matrix — very convenient for bulk-level aging analysis. ✅ Processed data available.

4. **[GSE149590](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE149590)** — A **Tabula Muris Senis** single-cell component (only 2 GSM entries, likely representing aggregated cell atlas objects). The 4 GB RAW tar likely contains `.h5ad` or similar cell × gene matrices. ✅ Processed data available.

### ⚠️ Caveats
- GSE132042 is a **SuperSeries** — downstream SubSeries (e.g., GSE132040) contain the actual sample-level data.
- GSE149590 has only 2 GSM entries, which likely represent **aggregated/combined atlas files** rather than individual biological replicates.
- For the aging atlas (Senis), pair **GSE132040** (bulk) with **GSE149590** (single-cell) for multi-resolution analysis.

---

## Q8 (T4)
**Query:** Find two comparable snRNA-seq datasets of human kidney that I could use to replicate an analysis — similar sample counts preferred  
**Source file:** `2026-05-12_Q8.md`

**Overlap (3):** GSE121862, GSE151302, GSE185948  
**App only (2):** GSE220222, GSE232479  
**Agentic only (2):** GSE114569, GSE220251

### App pipeline
*Shards: rnaseq_snrnaseq, rnaseq_bulk | Terms: snRNA-seq, comparable, kidney, replicate, sample, counts, preferred | Expanded: snRNA-seq, single-nucleus RNA-seq, kidney transcriptome, renal cortex, glomerulus, proximal tubule, collecting duct, nephron | Candidates: 300 | snRNA-seq: 106 (+94 via synonyms), bulk RNA-seq: 248 (+98 via synonyms)*

## Human Kidney snRNA-seq Datasets — Comparable Pairs

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE121862](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE121862) | Homo sapiens | 47 | GSE121862_UCSD-WU_Single_Nuclei_Cluster_Annotated_Raw_UMI_Matrix.tsv.gz (19MB), GSE121862_UCSD-WU_Single_Nuclei_Cluster_Annotations.csv.gz | A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys |
| [GSE151302](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE151302) | Homo sapiens | 10 | GSE151302_RAW.tar (8.1GB) | Single Cell Transcriptional and Chromatin Accessibility Profiling on the human adult kidneys |
| [GSE185948](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185948) | Homo sapiens | 26 | GSE185948_count_RNA.rds.gz (1.8GB), GSE185948_metadata_RNA.csv.gz, + ATAC files | Single Cell Transcriptional and Chromatin Accessibility Profiling on the human adult kidneys with ADPKD |
| [GSE220222](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE220222) | Homo sapiens | 15 | GSE220222_all_rnaseq_gene_counts.tsv.gz (2MB) | Predicting drivers of proximal tubule cell state through regularized regression analysis of single cell multiomic sequencing |
| [GSE232479](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE232479) | Homo sapiens | 10 | GSE232479_RAW.tar (219MB) | Comparative single-cell analyses identify shared and divergent features of human and mouse kidney development [human snRNA-seq] |

---

### Best Matched Pairs for Replication Analysis

#### 🥇 Top Recommendation: GSE151302 (n=10) ↔ GSE232479 (n=10)
These two datasets are the closest match in sample count (both n=10) and are directly comparable:
- Both profile **healthy adult human kidney** using snRNA-seq
- Both have similar file sizes suggesting comparable sequencing depth
- GSE151302 focuses on adult cortex cell-type mapping; GSE232479 emphasizes developmental context but includes adult human data
- **Note:** GSE151302 also links to additional control samples deposited in GSE185948, so you can extend the cohort if needed

#### 🥈 Strong Alternative: GSE151302 (n=10) ↔ GSE185948 (n=26)
These are **explicitly from the same laboratory and study design** — GSE185948 lists GSE151302 controls as part of its series (healthy samples deposited there), making them methodologically matched. The contrast here is **healthy kidney vs. ADPKD**, which may be exactly what a replication analysis needs if your target paper involves disease comparison.

#### 🥉 Broader Atlas Option: GSE121862 (n=47)
This is the largest and most cited human kidney snRNA-seq atlas in the index, profiling **30 distinct cell populations** via snDrop-seq. It provides annotated UMI matrices and cell-type labels — ideal as a reference dataset to replicate clustering or cell-type annotation pipelines against any of the smaller datasets above.

---

### Important Caveats

| Caveat | Details |
|--------|---------|
| **GSE151302 is multimodal** | Contains both snRNA-seq and snATAC-seq in the same RAW.tar — confirm RNA-only samples are extractable |
| **GSE185948 processed data** | `.rds.gz` files are R/Seurat objects — ready for immediate replication but platform-locked |
| **GSE220222 is a light file set** | Only a single `.tsv.gz` (2MB) — likely aggregated counts rather than per-cell matrices; verify resolution is sufficient |
| **Sample count ≠ donor count** | In snRNA-seq, one GSM may represent one donor or one library; check metadata to confirm biological replicate structure |
| **GSE151302/GSE185948 overlap** | The healthy controls from GSE151302 are re-used in GSE185948 — do not treat these as fully independent datasets |

### Agentic pipeline
*Tool calls: rnaseq_snrnaseq(human, kidney); rnaseq_snrnaseq(kidney, nucleus, human)*

I have a rich set of results. Let me now focus on the top candidates for comparable, purely snRNA-seq kidney datasets with similar sample counts — highlighting **GSE121862** (47 samples) and **GSE114569** (17 samples), and a few mid-range options. Here are the best matches:

---

## Human Kidney snRNA-seq Datasets

| Accession | Organism | Samples | Files | Title |
|---|---|---|---|---|
| [GSE121862](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE121862) | *Homo sapiens* | 47 | `.tsv.gz` (annotated UMI matrix + cluster annotations) | A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys |
| [GSE114569](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114569) | *Homo sapiens* | 17 | `.tsv.gz` (annotated UMI matrix) | Cellular recruitment by podocyte-derived pro-migratory factors in assembly of the human renal filter |
| [GSE151302](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE151302) | *Homo sapiens* | 10 | RAW.tar (8.1 GB) | Single Cell Transcriptional and Chromatin Accessibility Profiling on the human adult kidneys |
| [GSE185948](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185948) | *Homo sapiens* | 26 | `.rds.gz` (RNA + ATAC counts, metadata) | Single Cell Transcriptional and Chromatin Accessibility Profiling — adult kidneys with ADPKD |
| [GSE220251](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE220251) | *Homo sapiens* | 23 | `.h5` per sample | Single nucleus RNA-seq, ATAC-seq, and multiomic sequencing of adult human kidney |

---

## 🏆 Best Comparable Pair

### **GSE121862 × GSE114569** — ⭐ Top recommendation

| Feature | GSE121862 | GSE114569 |
|---|---|---|
| Samples | 47 | 17 |
| Platform | snDrop-seq | snRNA-seq (droplet) |
| Focus | Broad molecular anatomy, 30+ cell types | Podocyte biology, renal filter assembly |
| Data format | Annotated UMI matrix + cluster labels (.tsv.gz) | Annotated UMI matrix (.tsv.gz) |
| Processed data | ✅ Yes | ✅ Yes |

Both use **pre-annotated, cluster-labeled count matrices in matched formats**, making direct import and side-by-side analysis very straightforward.

### **GSE151302 × GSE185948** — Runner-up pair (~10 vs. 26 samples)
These two are actually **biologically linked** — GSE185948 explicitly reuses healthy controls from GSE151302, making them an excellent **matched healthy vs. ADPKD disease** comparison pair if disease modeling is of interest. Both have processed `.rds.gz` files ready for Seurat/R workflows.

---

## ⚠️ Caveats
- **GSE220251** and **GSE185948** also include ATAC-seq data — great for multiomics but adds complexity if you only want RNA.
- Sample counts (GSMs) reflect the number of GEO samples submitted, not the number of nuclei profiled. GSE121862 is noted to contain **~30 distinct cell populations**, suggesting deep coverage.
- GSE114569 covers multiple disease contexts (diabetes, hypertension) alongside healthy tissue — check sample metadata to subset to controls if needed for a clean replication.

---

## Q9 (T4)
**Query:** I want to study chromatin accessibility in mouse brain development — what datasets are available?  
**Source file:** `2026-05-12_Q9.md`

**Overlap (4):** GSE154067, GSE167047, GSE167048, GSE210804  
**App only (14):** GSE116144, GSE116598, GSE116599, GSE122172, GSE123576, GSE164989, GSE201400, GSE201487, GSE201488, GSE225726, GSE240782, GSE280169, GSE82010, GSE86365  
**Agentic only (32):** GSE126074, GSE172, GSE172535, GSE172572, GSE172582, GSE172668, GSE172676, GSE172688, GSE172698, GSE172703, GSE172713, GSE172723, GSE172759, GSE172767, GSE172800, GSE172861, GSE172874, GSE172900, GSE172911, GSE172912, GSE172993, GSE173047, GSE210805, GSE211786, GSE218576, GSE233153, GSE241429, GSE255405, GSE255406, GSE276002, GSE294772, GSE308599

### App pipeline
*Shards: atacseq | Terms: chromatin, accessibility, brain, development, available | Expanded: ATAC-seq, DNase-seq, FAIRE-seq, histone acetylation, H3K4me3, H3K27ac, neocortex development, neural progenitor cells | Candidates: 246 | ATAC-seq: 246 (+96 via synonyms)*

# Chromatin Accessibility in Mouse Brain Development — GEO Dataset Results

## Top Datasets (Mus musculus, Brain/Neural, ATAC-seq / Histone ChIP)

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE167047](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE167047) | *Mus musculus* | 8 | RAW.tar (979MB) | Single nuclei ATAC-seq of MGE, CGE, LGE and cortical regions from mouse embryonic forebrain |
| [GSE167048](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE167048) | *Mus musculus* | 4 | RAW.tar (362MB) | Single nuclei ATAC-seq (10X Genomics) of FACS-enriched cortical and hippocampal interneurons from P30 mouse brains |
| [GSE164989](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE164989) | *Mus musculus* | 8 | 2× .bw (373–407MB) | BAF subunit switching regulates chromatin accessibility to control cell cycle exit in the developing mammalian cortex |
| [GSE116144](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116144) | *Mus musculus* | 12 | RAW.tar (16MB) | Specific chromatin accessibility in subtypes of neocortical projection neurons over developmental time |
| [GSE123576](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE123576) | *Mus musculus* | 12 | RAW.tar + processed files incl. **countsData.csv.gz** (1.3GB) | High-throughput combinatorial indexing enables scalable single-cell chromatin accessibility profiling [mouse brain] |
| [GSE122172](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122172) | *Mus musculus* | 8 | RAW.tar (2.1GB) | Chromatin remodelling contributions of Snf2l in cerebellar granule neuron differentiation |
| [GSE201487](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE201487) | *Mus musculus* | 12 | 4× .bed.gz + .bw | CUT&Tag (H3K4me3) in MGE, CGE, LGE and cortical regions from mouse embryonic forebrain |
| [GSE201488](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE201488) | *Mus musculus* | 11 | 4× .bed.gz + .bw | CUT&Tag (H3K27me3) in MGE, CGE, LGE and cortical regions from mouse embryonic forebrain |
| [GSE201400](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE201400) | *Mus musculus* | 8 | 4× .bed.gz + .bw | CUT&RUN (H3K27Ac) in MGE, CGE, LGE and cortical regions from mouse embryonic forebrain |
| [GSE154067](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE154067) | *Mus musculus* | 6 | RAW.tar (13MB) | Cell type-specific chromatin accessibility analysis in the mouse brain (ATAC-seq) |
| [GSE225726](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225726) | *Mus musculus* | 19 | processed counts .txt.gz (11MB) | Chromatin accessibility profiling of neural stem cells differentiating into astrocytes (homeostatic & inflammatory) |
| [GSE116598](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116598) | *Mus musculus* | 10 | RAW.tar (466MB) | Oligodendrocyte precursor differentiation requires chromatin remodeling by Chd7 and Chd8 [ATAC-seq] |
| [GSE116599](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE116599) | *Mus musculus* | 8 | Dataset1.xlsx + RAW.tar | Oligodendrocyte precursor differentiation — Chd7/Chd8 [ChIP-seq companion] |
| [GSE240782](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE240782) | *Mus musculus* | 25 | rlog_normalized_peaks.xlsx (17MB) | Hmgb2 improves astrocyte-to-neuron conversion by increasing chromatin accessibility of neuronal maturation genes |
| [GSE86365](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE86365) | *Mus musculus* | 3 | RAW.tar (3MB) | Neuronal activity modifies chromatin accessibility in the adult brain — dentate gyrus (ATAC-seq) |
| [GSE82010](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE82010) | *Mus musculus* | 12 | RAW.tar (10MB) | Neuronal activity modifies chromatin accessibility in the adult brain — WT time points |
| [GSE280169](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE280169) | *Mus musculus* | 19 | RAW.tar (5.2GB) | Early Bisphenol A exposure effects on chromatin accessibility in brain oligodendrocytes of juvenile mice |
| [GSE210804](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE210804) | *Mus musculus* | 179 | RAW.tar (7.4GB) | scNMT-seq of mouse brain — DNA methylation and chromatin accessibility (multi-omic) |

---

## Best Matches Explained

### 🥇 Tier 1 — Core mouse brain developmental ATAC-seq datasets

**GSE167047** and **GSE167048** are the strongest pair for embryonic forebrain development. GSE167047 profiles snATAC-seq across **MGE, CGE, LGE, and cortex** at embryonic stages, while GSE167048 extends this to **postnatal (P30) interneurons**. Together they span embryonic neurogenesis through postnatal maturation in inhibitory neuron lineages. Both are from the **same research group** and use 10X Genomics Chromium snATAC-seq, making them highly compatible for integrated analysis.

**GSE201487 / GSE201488 / GSE201400** form a **companion histone modification trio** (H3K4me3, H3K27me3, H3K27Ac by CUT&Tag/CUT&RUN) covering the same four embryonic forebrain regions. These three datasets were designed to complement the snATAC-seq data and are ideal for cross-modal chromatin state analysis.

**GSE164989** directly addresses a key developmental mechanism: **BAF complex subunit switching** at the G1 exit checkpoint in cortical progenitors (E15 knockout vs. heterozygous), with bigWig files ready for visualization.

**GSE116144** is particularly valuable for studying **layer

### Agentic pipeline
*Tool calls: atacseq(mouse, brain, development); multiomics(mouse, brain, development, ATAC)*

Here is a comprehensive overview of available datasets for **chromatin accessibility in mouse brain development**, organized by category:

---

## 🧠 ENCODE Bulk ATAC-seq — Embryonic & Postnatal Time Course

These are high-quality ENCODE-project datasets covering multiple brain regions across embryonic stages (e11–e16) and postnatal timepoints:

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE172582](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172582) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **forebrain** (e11) |
| [GSE172572](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172572) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **hindbrain** (e11) |
| [GSE172900](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172900) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **midbrain** (e11) |
| [GSE172861](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172861) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **midbrain** (e12) |
| [GSE172676](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172676) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **forebrain** (e12) |
| [GSE172723](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172723) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **hindbrain** (e12) |
| [GSE172912](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172912) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **hindbrain** (e13) |
| [GSE172874](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172874) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **forebrain** (e13) |
| [GSE172713](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172713) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **midbrain** (e13) |
| [GSE172703](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172703) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **forebrain** (e14) |
| [GSE172911](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172911) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **midbrain** (e14) |
| [GSE172668](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172668) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **hindbrain** (e14) |
| [GSE172535](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172535) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **midbrain** (e15) |
| [GSE173047](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE173047) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **forebrain** (e15) |
| [GSE172767](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172767) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **forebrain** (e16) |
| [GSE172759](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172759) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **midbrain** (e16) |
| [GSE172800](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172800) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **hindbrain** (e16) |
| [GSE172688](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172688) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **forebrain** (postnatal) |
| [GSE172993](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172993) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **midbrain** (postnatal) |
| [GSE172698](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172698) | *M. musculus* | 2 | .bed.gz, .bigWig, .bigBed | ATAC-seq from **hindbrain** (postnatal) |

---

## 🔬 Single-Cell / Single-Nucleus ATAC-seq (snATAC-seq)

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE167047](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE167047) | *M. musculus* | 8 | RAW.tar | **snATAC-seq** of MGE, CGE, LGE, and cortex from embryonic forebrain (10x Genomics) |
| [GSE167048](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE167048) | *M. musculus* | 4 | RAW.tar | **snATAC-seq** of cortical & hippocampal interneurons (P30) |
| [GSE154067](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE154067) | *M. musculus* | 6 | RAW.tar | Cell type-specific chromatin accessibility in mouse brain |
| [GSE276002](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276002) | *M. musculus* | 7 | RAW.tar | **snATAC-seq** of E12 embryonic mouse brains (maternal gut-immune axis) |

---

## 🔗 Multi-omics (ATAC + RNA in Mouse Brain Development)

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE126074](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126074) | *M. musculus* | 36 | .mtx.gz, .tsv.gz | **SNARE-seq**: simultaneous chromatin accessibility + transcriptome, neonatal & adult mouse cortex ✅ |
| [GSE218576](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE218576) | *M. musculus* | 18 | .h5, atac_fragments.tsv.gz | snMultiome (RNA+ATAC) across mouse brain developmental stages (e12–e14) ✅ |
| [GSE241429](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241429) | *M. musculus*; *M. mulatta* | 33 | .mtx.gz, .txt.gz | Comparative single-cell multiome: neural progenitors in mouse & macaque prefrontal cortex ✅ |
| [GSE233153](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE233153) | *M. musculus* | 12 | RAW.tar | 10x Multiome in embryonic **MGE** under Ezh2 deletion ✅ |
| [GSE255405](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE255406) | *M. musculus* | 1 | RAW.tar | scMultiome defining OPC populations in postnatal cortex ✅ |
| [GSE308599](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE308599) | *M. musculus* | 28 | RAW.tar | **Tri-omics atlas** of postnatal mouse brain development & neuroinflammation ✅ |
| [GSE294772](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294772) | *M. musculus* | 142 | .h5ad | snATAC-seq/10x Multiome across **8 brain regions** and ages — aging & development ✅ |
| [GSE211786](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211786) | *M. musculus* | 2084 | .csv.gz, RAW.tar | **scNMT-seq** of adult neural stem cell lineage (methylation + chromatin accessibility) ✅ |

---

## 💡 Highlights & Recommendations

1. **ENCODE time-course (GSE172xxx series):** This is a gold-standard resource covering **forebrain, midbrain, and hindbrain** from e11 through postnatal, with fully processed peak calls (.bed.gz), bigWig signal tracks, and IDR-thresholded peaks. Ideal for comparative regulatory landscape analysis across brain regions and developmental stages.

2. **GSE167047** is the best single-dataset resource for **cell-type-resolved embryonic forebrain** chromatin, covering MGE, CGE, LGE, and cortex at single-nucleus resolution (10x Chromium).

3. **GSE126074** (SNARE-seq) is a landmark multiomics study with **paired chromatin + transcriptome** in P0 and adult mouse brain cortex — processed data in .mtx.gz format.

4. **GSE294772** is the largest single dataset (n=142, .h5ad format) with snATAC-seq across 8 brain regions — excellent for **aging vs. development comparisons**.

5. **GSE308599** is a cutting-edge **tri-omics atlas** of postnatal mouse brain development including spatial, epigenomic, and transcriptomic data.

> ⚠️ **Caveat:** The ENCODE GSE172xxx datasets each contain only 2 samples (duplicates) and are deposited as individual experiments per region/timepoint — you may want to aggregate several for a broader developmental trajectory analysis. Also note that GSE210804/GSE210805 are labeled "pancreatic organoids" in the title but describe a mouse brain scNMT-seq protocol — verify your sample of interest before downloading.

---

## Q10 (T5)
**Query:** I'm studying liver fibrosis — what's the best dataset to start with?  
**Source file:** `2026-05-12_Q10.md`

**Overlap (4):** GSE132662, GSE136103, GSE212837, GSE244832  
**App only (13):** GSE140641, GSE141100, GSE151251, GSE181987, GSE202379, GSE208413, GSE230468, GSE238159, GSE253493, GSE256377, GSE256398, GSE304675, GSE68108  
**Agentic only (9):** GSE109345, GSE114261, GSE119606, GSE122340, GSE126848, GSE134512, GSE137720, GSE171904, GSE174748

### App pipeline
*Shards: rnaseq_singlecell, rnaseq_bulk, rnaseq_snrnaseq, rnaseq_spatial | Terms: studying, liver, fibrosis, best, dataset, start | Expanded: hepatic fibrosis, cirrhosis, hepatic stellate cells, HSCs, Col1a1, alpha-smooth muscle actin, αSMA, TGF-β | Candidates: 233 | scRNA-seq: 102 (+100 via synonyms), bulk RNA-seq: 111 (+100 via synonyms), snRNA-seq: 12 (via synonyms), spatial transcriptomics: 8 (+7 via synonyms)*

# Best Datasets for Liver Fibrosis Research

## Top Picks: Single-Cell / Single-Nucleus

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE136103](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136103) | Human + Mouse | 26 | RAW.tar (416MB) | Resolving the fibrotic niche of human liver cirrhosis using single-cell transcriptomics |
| [GSE212837](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212837) | Human + Mouse | 20 | .h5ad.gz (3.1GB) ✅ | Autocrine signaling circuit in HSCs underlies advanced fibrosis in NASH |
| [GSE256398](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE256398) | Human + Mouse | 30 | RAW.tar (3.5GB) | Hepatic stellate cells control liver zonation via R-spondin 3 |
| [GSE244832](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE244832) | Human | 36 | .tar.gz (694MB) ✅ | Multi-modal HSC profiling for MASLD therapeutic targets |
| [GSE202379](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE202379) | Human | 59 | .rds.gz (2.6GB) ✅ | snRNA-seq mapping NAFLD/NASH progression spectrum |
| [GSE132662](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE132662) | Mouse | 10 | .csv.gz + RAW.tar | scRNA-seq: HSC and myofibroblast subsets in liver fibrosis |
| [GSE181987](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE181987) | Zebrafish + Human | 6 | .rds.gz (2.0GB) ✅ | scRNA-seq of healthy vs. fibrotic liver — conserved pathways with human |
| [GSE304675](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE304675) | Human | 4 | .rds (1.4GB) ✅ | Heterogeneity in reverted iPSC-derived hepatic stellate cells |

## Top Picks: Bulk RNA-seq (HSC-focused)

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE151251](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE151251) | Human | 6 | .tsv.gz (2MB) ✅ | Human HSCs treated with TGF-β (key fibrosis driver) |
| [GSE140641](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE140641) | Human + Mouse | 39 | .xlsx + RAW.tar | Lineage-specific TFs suppress HSC activation in fibrosis |
| [GSE253493](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE253493) | Human | 12 | RAW.tar (59MB) | Primary HSCs + LX-2 treated with TGF-β; NASH-relevant |
| [GSE141100](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE141100) | Human + Mouse | 14 | .csv.gz ✅ | Alcohol-activated human and mouse HSCs — shared gene profiles |
| [GSE238159](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE238159) | Human + Mouse | 18 | RAW.tar (33MB) | lncRNA TILAM promotes fibrosis — conserved in human and mouse |
| [GSE68108](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE68108) | Human | 22 | RAW.tar (733MB) | Genome-wide lncRNA mapping in HSCs (RNA-seq + ChIP-seq) |
| [GSE230468](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE230468) | Mouse | 25 | .csv.gz ✅ | Host genetic variation, hepacivirus clearance, and liver fibrosis |

## Top Picks: Spatial Transcriptomics

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE208413](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE208413) | Human | 57 | .txt.gz ✅ | Spatial mRNA profiling — liver inflammation and postoperative failure |

---

## Recommendations & Caveats

### 🥇 Best starting point: **GSE136103**
This is the **landmark human liver cirrhosis atlas** — >100,000 cells, covering all non-parenchymal cell types (HSCs, macrophages, endothelial, cholangiocytes), both healthy and cirrhotic human tissue, with paired mouse data for cross-species validation. It defines the "fibrotic niche" at single-cell resolution and is the most-cited dataset in this space.

### 🥈 Best for NASH/MASH fibrosis specifically: **GSE212837**
Focused on HSC activation in NASH, cross-species (human + mouse), and critically — **processed `.h5ad` is available**, making it immediately loadable in Scanpy/AnnData without preprocessing from scratch.

### 🥉 Best for disease progression trajectory: **GSE202379** or **GSE244832**
Both are **snRNA-seq in human liver** across NAFLD→NASH→cirrhosis stages (59 and 36 samples respectively), with processed `.rds`/`.tar.gz` objects ready to use. GSE244832 is multi-modal (RNA + ATAC accessibility).

### For bulk RNA-seq baselines:
- **GSE151251** and **GSE253493** are clean, small, and directly comparable: primary human HSCs ± TGF-β stimulation — ideal for identifying canonical activation signatures or validating findings.
- **GSE140641** (n=39, human + mouse) is larger and examines HSC quiescence vs. activation vs. inactivation — useful for trajectory analysis complement.

### ⚠️ Important caveats:
1. **"HSCs" disambiguation**: Many results returned hematopoietic stem cells (HSCs), which share the abbreviation with **hepatic stellate cells** — the key fibrosis effector. All datasets in the tables above have been filtered to hepatic stellate cell / liver fibrosis context.
2. **Model heterogeneity**: Mouse fibrosis models used vary across datasets (CCl₄, BDL, NASH diet, MASH/CDAA) — check model compatibility before cross-dataset comparisons.
3. **GSE256398** (n=30, R-spondin 3) includes a companion bulk dataset **GSE256377** if you want matched scRNA + bulk from the same study.
4. **GSE181987** (zebrafish) is excellent for evolutionary conservation analysis but requires cross-species integration tools (e.g., ortholog mapping).

### Agentic pipeline
*Tool calls: rnaseq_bulk(liver, fibrosis); rnaseq_singlecell(liver, fibrosis); rnaseq_snrnaseq(liver, fibrosis)*

Here's a curated selection of the **best liver fibrosis datasets** across different modalities and study contexts:

---

## 🔬 Top Liver Fibrosis Datasets on GEO

### 🟦 Single-Cell / Single-Nucleus RNA-seq (Best for Cell-Type Resolution)

| Accession | Organism | Samples | Files | Title |
|---|---|---|---|---|
| [GSE136103](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136103) | Human + Mouse | 26 | RAW.tar (416 MB) | **Resolving the fibrotic niche of human liver cirrhosis using single-cell transcriptomics** |
| [GSE212837](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212837) | Mouse + Human | 20 | .h5ad.gz, RAW.tar | **Autocrine HSC signaling underlies advanced NASH fibrosis** |
| [GSE171904](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171904) | Mouse | 3 | .rds.gz, RAW.tar | **HSC activation roadmap and myofibroblast origin during liver fibrosis** |
| [GSE137720](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE137720) | Mouse | 11 | RAW.tar (249 MB) | **Zonation of mesenchyme function during liver fibrosis (scRNA-seq)** |
| [GSE132662](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE132662) | Mouse | 10 | .csv.gz, RAW.tar | **scRNA-seq identifies HSC and myofibroblast subsets in fibrosis** |
| [GSE244832](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE244832) | Human | 36 | RAW.tar, processed files | **Multi-modal HSC profiling in MASLD/MASH — novel therapeutic targets** |
| [GSE174748](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174748) | Human | 4 | .rds.gz, RAW.tar | **HSC populations imbalance in liver fibrosis → hepatocarcinogenesis (snRNA-seq)** |

---

### 🟩 Bulk RNA-seq (Best for Gene Signatures & Drug Studies)

| Accession | Organism | Samples | Files | Title |
|---|---|---|---|---|
| [GSE136103](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136103) | Human + Mouse | 26 | RAW.tar | Fibrotic niche cirrhosis — large cell atlas |
| [GSE126848](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126848) | Human | 57 | raw counts .txt.gz | **Hepatic transcriptome across NAFLD → NASH → fibrosis spectrum** |
| [GSE109345](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109345) | Mouse | 78 | RAW.tar | **Molecular signature for onset of NASH-related fibrosis** (large n) |
| [GSE119606](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119606) | Human | 15 | raw .tsv.gz | **TGF-β / PDGF-driven HSC activation in fibrosis** |
| [GSE122340](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122340) | Human | 178 | RAW.tar | **Biliary atresia fibrosis molecular signature** — largest human cohort |
| [GSE114261](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114261) | Mouse | 12 | RAW.tar | **BET inhibition improves NASH and liver fibrosis** |
| [GSE134512](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE134512) | Mouse | 9 | DESeq2 .txt.gz | **Activated fibroblasts in CCl4 vs. NASH fibrosis models** |

---

## ⭐ Best Datasets to Start With — Recommendations

### **#1 — [GSE136103](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136103)** *(Human + Mouse scRNA-seq, 26 samples, 100,000+ cells)*
> **"Resolving the fibrotic niche of human liver cirrhosis using single-cell transcriptomics"**
This is the landmark liver fibrosis single-cell atlas. It profiled >100,000 cells from healthy and cirrhotic human livers, identifying key cell types including a novel **TREM2+CD9+ scar-associated macrophage** population. Highly cited, processed data available, and directly translatable to human disease.

### **#2 — [GSE212837](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212837)** *(Human + Mouse scRNA-seq + bulk, 20 samples)*
> Integrates mouse and human NASH fibrosis data with an `.h5ad` processed file — great for diving straight into analysis. Focuses on **HSC autocrine signaling** as a drug target.

### **#3 — [GSE126848](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126848)** *(Human bulk RNA-seq, 57 samples)*
> Covers the **full NAFLD → NASH → fibrosis spectrum** in patients, ideal for identifying transcriptomic biomarkers and disease-stage comparisons.

---

## ⚠️ Caveats to Keep in Mind
- **Fibrosis model variability**: Mouse datasets use different models (CCl4, BDL, NASH diet, MDR2-KO) — results may not generalize across models.
- **Human vs. mouse**: HSC gene programs diverge; cross-species validation is advised.
- **Processed data**: GSE212837 (`.h5ad`), GSE171904 (`.rds`), and GSE244832 have ready-to-use processed files. Others may require re-processing from raw counts.

Would you like me to narrow down by a specific aspect (e.g., hepatic stellate cells, NASH-specific fibrosis, a specific fibrosis model like CCl4, or a particular assay like ATAC-seq or spatial transcriptomics)?

---
