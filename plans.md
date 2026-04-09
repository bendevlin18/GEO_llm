# GEO LLM Wiki — Project Plan

## Vision

Build a periodically-updated, LLM-generated wiki that indexes GEO datasets by their key features, making it easy to discover what data is available and in what form. Inspired by [Karpathy's LLM wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Three-Layer Architecture

### Layer 1: Raw Sources (`data/`)
- JSON snapshots from `geo_metadata_fetcher.py`, timestamped and immutable
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

1. **Fetch** — run `geo_metadata_fetcher.py` for a new date window, save to `data/geo_metadata_YYYY-MM-DD.json`
2. **Merge** — load all data snapshots, deduplicate by accession (latest snapshot wins if a record appears in multiple fetches)
3. **Classify** — run `extract_rnaseq.py` and `tag_topics.py` on the merged set
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
