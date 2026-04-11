# GEO LLM Wiki — Project Plan

## Vision

Build a periodically-updated, LLM-generated wiki that indexes GEO datasets by their key features, making it easy to discover what data is available and in what form. Inspired by [Karpathy's LLM wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Three-Layer Architecture

### Layer 1: Raw Sources (`data/`)
- JSON snapshots from `scripts/geo_metadata_fetcher.py`, timestamped and immutable
- Each scrape covers a date window; new scrapes are additive

### Layer 2: The Wiki (`wiki/`)
- LLM-generated markdown pages, organized by facets:
  - **By organism** — `wiki/organisms/homo_sapiens.md`, etc.
  - **By assay type** — `wiki/assays/rna_seq.md`, `wiki/assays/chip_seq.md`, etc.
  - **By sequencing modality** (within RNA-seq):
    - Bulk RNA-seq
    - Single-cell RNA-seq (scRNA-seq)
    - Spatial transcriptomics (Visium, MERFISH, Slide-seq, etc.)
    - Single-nucleus RNA-seq (snRNA-seq)
  - **By research topic** — LLM-inferred from titles/summaries (cancer, immunology, neuroscience, etc.)
  - **`wiki/index.md`** — master catalog
  - **`wiki/log.md`** — append-only ingest log
  - **Notable dataset pages** — `wiki/datasets/GSExxxxxx.md` for high-value entries

### Layer 3: Schema (`CLAUDE.md` + config)
- Wiki conventions, page templates, ingest workflow, tagging taxonomy

## Phase 1: RNA-seq Classification (current)

Focus exclusively on RNA-sequencing datasets. The ingest pipeline will:

1. **Filter** — identify RNA-seq datasets from the full GEO metadata
2. **Classify modality** — bulk vs. single-cell vs. spatial vs. single-nucleus (using LLM on title + summary + platform + supplementary file info)
3. **Tag topics** — infer research area from title/summary
4. **Generate wiki pages** — organism pages, modality pages, topic pages, index

## Data Availability Indexing (future phases)

A key goal is understanding not just *what* a dataset is, but *what files are available* and how usable they are. Categories to track:

- **Raw data** — FASTQ files (assumed to always exist on SRA)
- **Preprocessed data** — what's in the supplementary files:
  - Count matrices (CSV, TSV, TXT)
  - R/RData/RDS objects (Seurat, SingleCellExperiment, DESeq2 results)
  - H5/H5AD files (AnnData for scanpy)
  - MTX files (10x Genomics sparse matrices)
  - BED/BEDGraph/BigWig files (for ChIP/ATAC)
- **Metadata quality** — does the dataset include:
  - Sample-level metadata (conditions, treatments, timepoints)
  - Cell-type annotations (for single-cell)
  - Clinical metadata (for human studies)
- **Processing status** — is the data:
  - Raw counts only
  - Normalized
  - Fully analyzed (with DE results, clustering, etc.)

The `suppFile` field in GEO metadata gives a starting signal (e.g., "CSV", "RDS", "H5AD"), and FTP directory listings can reveal more detail.

## Incremental Update Strategy

The pipeline should support pulling new date windows and merging them into the existing index without duplicates or data loss.

### Update workflow

1. **Fetch** — run `scripts/geo_metadata_fetcher.py` for a new date window, save to `data/geo_metadata_YYYY-MM-DD.json`
2. **Merge** — load all data snapshots, deduplicate by accession (latest snapshot wins if a record appears in multiple fetches)
3. **Classify** — run `scripts/extract_rnaseq.py` and `scripts/tag_topics.py` on the merged set
4. **Rebuild** — regenerate `search_index.txt`, wiki pages, and update `log.md`

### Deduplication

GEO records can be updated after initial publication. The merge step should:
- Key on accession (GSE ID)
- If a record appears in multiple snapshots, keep the most recent version
- Track total unique records and new-vs-updated counts in the log

### Scheduling (future)

- Monthly or weekly cron fetching the latest window
- Could use Claude Code scheduled triggers or a simple cron + shell script
- Each run appends to `log.md` with date, window, counts

### Data sharing (future)

Data files (raw JSON snapshots, classified records, FTP index) are gitignored since they're reproducible via the pipeline. For others to use the repo with pre-built data without re-running the full pipeline:
- GitHub Releases with attached data archives
- Or a bootstrap script that fetches a compressed data bundle from a hosted location
- Or Git LFS if the data stabilizes in size

## Batch Processing Approach

- First pass: lightweight LLM classification (title + summary → modality + topic tags)
- Second pass: deeper pages for notable/high-value datasets
- Process in batches to manage LLM API costs

## LLM Backend Strategy

**Phase 1 (current):** Use Claude Code interactively to classify records and generate wiki pages. This lets us iterate on prompts, taxonomy, and page structure without needing API infrastructure.

**Phase 2 (future):** Move to Anthropic API calls (via Python SDK) for automated batch classification. This enables:
- Periodic unattended scrape → classify → update-wiki pipeline
- Structured output (JSON mode) for reliable parsing
- Cost-efficient batching with Haiku for classification, Sonnet/Opus for deeper pages
- Caching of prompts to reduce cost on re-runs

Requires `ANTHROPIC_API_KEY` env var. The classification prompt and taxonomy developed in Phase 1 will carry over directly.

## Phase 2.5: Analysis Protocols (`wiki/protocols/`)

Add a `wiki/protocols/` folder with step-by-step analysis guides for each data format a user might encounter when downloading a GEO dataset. Each protocol page should explain what the data format is, what tools are needed, and walk through a standard analysis workflow.

### Difficulty / time tiers

| Tier | Data Starting Point | Estimated Time | Difficulty | Example Formats |
|---|---|---|---|---|
| **1 — Ready to use** | Processed count matrices, DE results, annotated objects | Minutes to hours | Easy | CSV, TSV, XLSX with counts or DE tables |
| **2 — Needs loading** | Serialized analysis objects | Hours | Easy–Medium | RDS (Seurat), H5AD (AnnData), RData |
| **3 — Needs processing** | Raw count matrices (unfiltered) | Hours to a day | Medium | MTX + barcodes + features (10x), H5 (CellRanger) |
| **4 — Needs alignment** | Raw sequencing reads only | Days | Hard | FASTQ (from SRA), no supplementary files |

### Protocol pages to create

- `protocols/csv_tsv_counts.md` — loading pre-made count matrices, basic QC, DE analysis
- `protocols/rds_seurat.md` — loading Seurat objects, exploring existing annotations, extending analysis
- `protocols/h5ad_anndata.md` — loading AnnData/scanpy objects, similar to RDS tier
- `protocols/mtx_10x.md` — loading sparse matrices from CellRanger output, filtering, clustering
- `protocols/h5_cellranger.md` — loading HDF5 from CellRanger, converting to Seurat/AnnData
- `protocols/fastq_alignment.md` — obtaining FASTQ from SRA, alignment with STAR/CellRanger/STARsolo, generating count matrices
- `protocols/index.md` — overview page with the tier table and decision flowchart ("I have X format, what do I do?")

### Integration with the wiki

- Search index and dataset pages already track file formats via FTP indexing. Protocol pages can be linked from dataset entries so users go directly from "this dataset has MTX files" to "here's how to analyze MTX files."
- The difficulty/time tier for each dataset could eventually be added as a field in the search index, letting users filter by analysis effort (e.g., "show me scRNA-seq mouse brain datasets where processed data is available").

## Phase 3: Beyond RNA-seq

Phase 1 focuses on RNA-seq because it's the largest and most consistently structured slice of GEO. Once the RNA-seq pipeline is mature, the wiki should expand to cover all major GEO assay types. The same three-layer architecture (raw sources → classified data → wiki pages) applies; the main work is building assay-specific classifiers and extending the taxonomy.

### Assay types to add

| Assay Family | Subtypes / Modalities | Key File Types |
|---|---|---|
| **ChIP-seq / CUT&RUN / CUT&Tag** | Histone marks, TF binding, broad vs. narrow peaks | BED, BigWig, narrowPeak, broadPeak |
| **ATAC-seq** | Bulk ATAC, single-cell ATAC (scATAC) | BED, BigWig, fragments.tsv |
| **Methylation** | WGBS, RRBS, Infinium arrays (450K, EPIC) | BED, IDAT, beta-value matrices |
| **Hi-C / 3D Genome** | Hi-C, Micro-C, HiChIP, capture Hi-C | .hic, .cool, .mcool, contact matrices |
| **Proteomics** | Mass spec, CITE-seq protein | CSV, TSV, mzML |
| **Multiomics** | 10x Multiome (RNA+ATAC), SHARE-seq, TEA-seq, CITE-seq | H5, MTX, fragments.tsv |
| **Microarray** | Expression arrays, SNP arrays | CEL, CHP, TXT |
| **Other sequencing** | WGS, WES, amplicon-seq, long-read (PacBio, ONT) | BAM, VCF, FASTQ |

### What changes per assay

- **`extract_rnaseq.py`** → generalized `classify_assay.py` that routes records to assay-specific classifiers. The RNA-seq classifier becomes one module.
- **Modality classification** — each assay family has its own subtypes (e.g., ChIP-seq: histone vs. TF; methylation: WGBS vs. array). These need assay-specific keyword rules or LLM classification.
- **Topic taxonomy** — the existing 28 topics are largely assay-agnostic and should carry over. May need additions for assay-specific research areas (e.g., "chromatin architecture" for Hi-C).
- **Wiki structure** — `wiki/assays/` expands with new pages per assay type. Organism and topic pages become cross-assay, showing what data is available across modalities for a given organism or research area.
- **Search index** — same pipe-delimited format, just more records and a wider set of modality values.
- **FTP indexing** — already assay-agnostic; works for any GEO dataset.

### Suggested rollout order

1. **ChIP-seq / CUT&RUN** — second-largest assay type on GEO, well-structured, complements RNA-seq for gene regulation studies
2. **ATAC-seq** — growing fast, especially scATAC alongside scRNA-seq
3. **Methylation** — large existing body of data, distinct file types
4. **Multiomics** — increasingly common, links to existing RNA-seq entries
5. **Hi-C / 3D genome** — smaller but high-value, specialized file formats
6. **Microarray** — legacy data but massive archive, simpler to classify

### Cross-assay features (longer term)

- **Multi-assay dataset pages** — many GEO SuperSeries bundle RNA-seq + ChIP-seq + ATAC-seq from the same study. Link these together so a user can find all data from a single experiment.
- **Assay co-occurrence index** — for a given organism + topic, show which assay types are available (e.g., "for mouse kidney, there are 88 snRNA-seq, 12 ATAC-seq, and 5 ChIP-seq datasets").
- **Data integration readiness** — flag datasets where multiple assays share the same samples, enabling multi-omic integration.
