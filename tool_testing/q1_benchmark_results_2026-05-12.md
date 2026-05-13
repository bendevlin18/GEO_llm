# Benchmark Results — 2026-05-12

Scoring rubric (1–3 each): Accuracy · Completeness · Constraint adherence · Domain interpretation · Explanation quality · Hallucination · Tool efficiency

| Query | App Score | Agentic Score | Notes |
|---|---|---|---|
| Q1 | | | |

---
## Q1 (T1)
**Query:** Find zebrafish spatial transcriptomics datasets

### App pipeline
*Shards: rnaseq_spatial, rnaseq_bulk | Terms: zebrafish | Expanded: Danio rerio, in situ hybridization, ISH, FISH, spatial RNA-seq, whole-mount, larval development, embryonic zebrafish | Candidates: 231 | spatial transcriptomics: 76 (+68 via synonyms), bulk RNA-seq: 155 (+5 via synonyms)*

## Zebrafish Spatial Transcriptomics Datasets

| Accession | Organism | Samples | Files | Title |
|-----------|----------|---------|-------|-------|
| [GSE262578](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262578) | *Danio rerio* | 53 | .rds.gz ✓ | Construction of Danio rerio Asymmetrical Maps (DreAM) |
| [GSE274407](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE274407) | *Danio rerio* | 5 | RAW.tar | Spatiotemporal dynamics of the developing zebrafish enteric nervous system at the whole organ level |
| [GSE159709](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE159709) | *Danio rerio* | 6 | RAW.tar | Spatially resolved transcriptomics reveals the architecture of the tumor-microenvironment interface |
| [GSE294097](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294097) | *Danio rerio* | 4 | RAW.tar (4.9GB) | P301S Mutant Tau-Driven Zebrafish Platform — Pharmacological GSK3β Inhibitors with Anti-Neurodegenerative Efficacy |
| [GSE241156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241156) | *Danio rerio* + *Mus musculus* | 14 | RAW.tar + .xlsx ✓ | Interspecies comparison reveals Hmga1 as driver of cardiac regeneration [TOMOseq] |
| [GSE128350](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128350) | Multi-species incl. *Danio rerio* | 27 | RAW.tar | Multi-species tomo-sequencing — hematopoietic stem cell regulators in the embryonic aorta |
| [GSE66688](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE66688) | *Danio rerio* | 1152 | .txt.gz ✓ | Spatial reconstruction of single-cell gene expression |
| [GSE120509](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE120509) | *Danio rerio* | 72 | .txt.gz ✓ | Multi-dimensional transcriptome analysis of an intact hematopoietic organ (CHT) |
| [GSE104057](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE104057) | *Danio rerio* | 3 | RAW.tar | Spatially resolved RNA-sequencing of the embryonic zebrafish heart |
| [GSE74652](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE74652) | *Danio rerio* | 2 | RAW.tar + .gz ✓ | BMP signaling as essential regulator of zebrafish cardiomyocyte regeneration (tomo-seq) |

---

### Best Matches & Notes

**Top picks for true spatial transcriptomics (sequencing-based):**

- **GSE262578** is the most directly relevant: a dedicated zebrafish spatial transcriptomics atlas ("DreAM") with 53 samples studying axis establishment at three developmental time points, with processed `.rds.gz` files ready for analysis in R.
- **GSE274407** covers the zebrafish enteric nervous system with whole-organ spatial resolution (1.3 GB RAW) — ideal for ENS/gut-neuroscience work.
- **GSE159709** applies spatial transcriptomics to zebrafish tumor-microenvironment biology — unique cancer-focused zebrafish spatial dataset.
- **GSE294097** is notable for applying spatial sequencing to a tau/Alzheimer's-like zebrafish model, bridging neurodegenerative disease and zebrafish spatial methods.

**Tomo-seq (serial sectioning bulk RNA-seq as spatial proxy):**

- **GSE241156**, **GSE128350**, **GSE74652**, **GSE104057**, and **GSE120509** use **tomo-seq** — a zebrafish-developed technique that reconstructs spatial expression via serial transverse sections. This is *not* spot-based spatial transcriptomics (e.g., Visium) but is a well-validated spatial method native to zebrafish.

**Landmark dataset:**
- **GSE66688** (1,152 samples) is the original Achim et al. 2015 *Science* paper on spatial reconstruction of single-cell gene expression in zebrafish — a foundational reference dataset.

### ⚠️ Caveats

1. **Most "spatial" zebrafish datasets use tomo-seq** (serial bulk RNA-seq slices), not commercial platforms like 10x Visium. If you need Visium-style spot-based data specifically, options are very limited for zebrafish.
2. **GSE128350** and **GSE241156** are multi-species — zebrafish data is present but not exclusive.
3. **GSE120509** focuses on the caudal hematopoietic tissue (CHT) organ-level spatial dissection, not whole-embryo.
4. Processed files (`.rds.gz`) are confirmed only for **GSE262578**; most others require processing from RAW tarballs.

### Agentic pipeline
*Tool calls: rnaseq_spatial(zebrafish); multiomics(zebrafish, spatial)*

Here are the zebrafish spatial transcriptomics datasets found across GEO:

| Accession | Organism | Samples | Files | Title |
|---|---|---|---|---|
| [GSE262578](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE262578) | *Danio rerio* | 53 | .rds.gz (processed) | Construction of Danio rerio Asymmetrical Maps (DreAM) |
| [GSE274407](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE274407) | *Danio rerio* | 5 | RAW.tar (1.3 GB) | Spatiotemporal dynamics of the developing zebrafish enteric nervous system at the whole organ level |
| [GSE294097](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE294097) | *Danio rerio* | 4 | RAW.tar (4.9 GB) | P301S Mutant Tau-Driven Zebrafish Platform Enables Systematic Identification of Pharmacological GSK3β Inhibitors with Anti-Neurodegenerative Efficacy |
| [GSE241156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241156) | *Mus musculus*; *Danio rerio* | 14 | RAW.tar + Excel tables | Interspecies comparison reveals Hmga1 as driver of cardiac regeneration [TOMOseq] |
| [GSE128350](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128350) | Multi-species incl. *Danio rerio* | 27 | RAW.tar (15 MB) | Multi-species tomo-sequencing identifies new major hematopoietic stem cell regulators (embryonic aorta) |
| [GSE325620](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325620) | *Danio rerio* | 14 | RAW.tar (1.5 GB) | Comparative single-cell multiomic analysis of natural retinal aging [Zebrafish multiome RNA] |
| [GSE192741](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192741) | Multi-species incl. *Danio rerio* | 15 | RAW.tar + .rds.gz (processed) | Spatial proteogenomics: evolutionarily-conserved hepatic macrophage niches (spatial) |

---

### 🔍 Highlights & Notes

- **Best standalone zebrafish spatial datasets:**
  - **GSE262578 (DreAM)** is the largest purely zebrafish spatial dataset (n=53) and includes processed `.rds.gz` files — ideal for developmental axis/asymmetry studies.
  - **GSE274407** focuses on the **enteric nervous system** development at whole-organ resolution — unique for gut neuroscience.
  - **GSE294097** is notable for applying spatial transcriptomics to a **tauopathy/Alzheimer's model** in zebrafish, useful for neurodegeneration research.

- **Multi-species comparative datasets:**
  - **GSE241156** (TOMOseq, zebrafish + mouse) is well-suited for **cardiac regeneration** studies, with rich supplementary Excel tables.
  - **GSE128350** uses tomo-seq across 4 species including zebrafish for **hematopoietic stem cell** microenvironment studies.
  - **GSE192741/GSE192740** are primarily liver/macrophage multi-species CITE-seq datasets where zebrafish is one of many organisms — zebrafish-specific data may be limited.

- **⚠️ Caveat:** Several datasets use **tomo-seq** (serial sectioning + bulk RNA-seq) rather than spot-based platforms like Visium or MERFISH. GSE294097 is the most likely to use a modern in situ platform given its large RAW file size (4.9 GB).

---
