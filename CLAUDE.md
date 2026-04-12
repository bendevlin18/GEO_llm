# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A periodically-updated, LLM-generated wiki that indexes GEO (Gene Expression Omnibus) RNA-seq datasets by their key features — organism, assay modality, research topic, and data availability — making it easy to discover what data exists and in what form. Inspired by [Karpathy's LLM wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

The wiki and search index (`wiki/search_index.txt`) are designed for easy LLM querying: an LLM can search the index to quickly find relevant GEO datasets by organism, modality, topic, or data format.

## Three-Layer Architecture

### Layer 1: Raw Sources (`data/`)
- JSON snapshots from `geo_metadata_fetcher.py`, timestamped and immutable
- Each scrape covers a date window; new scrapes are additive
- Data files are gitignored (reproducible via the pipeline)

### Layer 2: The Wiki (`wiki/`)
- LLM-generated markdown pages organized by facets:
  - **By organism** — `wiki/organisms/homo_sapiens.md`, etc.
  - **By assay type** — `wiki/assays/bulk_rnaseq.md`, `wiki/assays/scrna_seq.md`, etc.
  - **By research topic** — LLM-inferred from titles/summaries (`wiki/topics/cancer.md`, etc.)
  - **`wiki/index.md`** — master catalog
  - **`wiki/log.md`** — append-only ingest log
- `wiki/search_index.txt` — flat-file search index for LLM queries

### Layer 3: Schema (`CLAUDE.md` + config)
- Wiki conventions, page templates, ingest workflow, tagging taxonomy

## Current Focus: RNA-seq Classification (Phase 1)

Focus exclusively on RNA-sequencing datasets. The ingest pipeline:
1. **Fetch** — pull GEO metadata via NCBI E-Utilities API
2. **Filter & classify** — identify RNA-seq datasets, classify modality (bulk / single-cell / spatial / single-nucleus)
3. **Tag topics** — infer research area from title/summary
4. **Generate wiki pages** — organism pages, modality pages, topic pages, index, and search index

## Pipeline Scripts

All scripts live in `scripts/` and should be run from the project root (e.g., `python scripts/index_ftp.py`).

| Script | Purpose |
|---|---|
| `scripts/geo_metadata_fetcher.py` | Fetches GEO Series metadata from NCBI E-Utilities API |
| `scripts/extract_rnaseq.py` | Filters metadata to RNA-seq datasets and classifies modality |
| `scripts/tag_topics.py` | Infers research topics from titles/summaries |
| `scripts/ftp_probe.py` | Probes GEO FTP for supplementary file details |
| `scripts/index_ftp.py` | Indexes FTP directory listings for data availability |
| `scripts/build_search_index.py` | Builds `wiki/search_index.txt` for LLM querying |
| `scripts/generate_wiki.py` | Generates wiki markdown pages from classified data |
| `scripts/merge_and_rebuild.py` | Merges data snapshots, deduplicates, and rebuilds the wiki |
| `scripts/extract_chipseq.py` | Filters metadata to ChIP-seq/ATAC-seq datasets, classifies modality and target type |
| `scripts/extract_methylation.py` | Filters metadata to methylation datasets, classifies protocol modality |
| `scripts/extract_multiomics.py` | Filters metadata to multiomics datasets (CITE-seq, 10x Multiome, SHARE-seq, TEA-seq), classifies subtype, and back-annotates `rnaseq_classified.json` and `chipseq_classified.json` with `is_multiomics: true` |
| `scripts/generate_plots.py` | Generates PNG charts for the README (`assets/`) from classified data; requires `matplotlib` |
| `scripts/bootstrap.py` | Downloads pre-built data files from the latest GitHub Release |
| `scripts/create_data_release.py` | (Maintainer) Creates a GitHub Release and uploads data assets |

## Running

All scripts require the `GEO_llm` conda environment and should be run from the project root:

```bash
# Requires Python 3.10+ (uses X | Y union type syntax)
# Core pipeline: stdlib only (urllib, xml, json, argparse)
# generate_plots.py also requires: conda install -n GEO_llm matplotlib
# Always use: conda run -n GEO_llm python scripts/<script>.py

# Fetch metadata for a date range
conda run -n GEO_llm python scripts/geo_metadata_fetcher.py --email benjamin.devlin@duke.edu --start-date 2024/01/01 --end-date 2024/03/31 -o data/geo_metadata_2024-Q1.json

# Full merge/classify/tag/rebuild pipeline (runs all steps end-to-end)
conda run -n GEO_llm python scripts/merge_and_rebuild.py

# FTP indexing (slow — ~1.6 records/sec, ~18 hours for 100k records; saves incrementally)
conda run -n GEO_llm python scripts/index_ftp.py

# Bootstrap pre-built data from GitHub Releases (skips the ~18 hr pipeline)
conda run -n GEO_llm python scripts/bootstrap.py

# (Maintainer) Publish a new data release to GitHub
GITHUB_TOKEN=ghp_... conda run -n GEO_llm python scripts/create_data_release.py --tag data-v1.0.0
```

Email is required by NCBI policy (`benjamin.devlin@duke.edu`). Can also be set via `NCBI_EMAIL` env var. Optional `NCBI_API_KEY` env var raises rate limit from 3 to 10 req/sec.

## Full Rebuild Checklist

Run these steps in order after fetching new GEO metadata. Each step depends on the previous.

```bash
# 1. Classify all assay types (each reads data/*.json, writes *_classified.json)
conda run -n GEO_llm python scripts/extract_rnaseq.py
conda run -n GEO_llm python scripts/extract_chipseq.py
conda run -n GEO_llm python scripts/extract_methylation.py
conda run -n GEO_llm python scripts/extract_multiomics.py   # also back-annotates rnaseq + chipseq

# 2. Index FTP supplementary files (slow, incremental — skip if ftp_index.json is current)
conda run -n GEO_llm python scripts/index_ftp.py

# 3. Rebuild search index shards (reads all *_classified.json + ftp_index.json)
conda run -n GEO_llm python scripts/build_search_index.py

# 4. Regenerate wiki pages
conda run -n GEO_llm python scripts/generate_wiki.py

# 5. Regenerate README charts — run this every rebuild so assets/ stays in sync
conda run -n GEO_llm python scripts/generate_plots.py

# 6. Commit wiki/ and assets/ to git, then push
git add wiki/ assets/
git commit -m "Rebuild wiki and plots — <date>"
git push
```

**Note:** `generate_plots.py` reads the classified JSON files directly (`rnaseq_classified.json`, `chipseq_classified.json`, `methylation_classified.json`, `multiomics_classified.json`). It must be run after step 1 (classify) and should always be re-run before committing, so the charts in `assets/` reflect the current data and not a stale snapshot.

## Repository Structure

```
GEO_llm/
├── data/                          # Layer 1: Raw sources (gitignored)
│   ├── geo_metadata_2015-Q1.json      # Quarterly scrapes from 2015 to present
│   ├── geo_metadata_2015-Q2.json      # Named as geo_metadata_YYYY-QN.json
│   ├── ...                            # Coverage: 2015-Q1 through 2024-Q4
│   ├── geo_metadata_2025-Q1.json      # plus 2025 quarters
│   └── geo_metadata_2026-04-09.json   # Latest scrape (Jan–Apr 2026)
│
├── wiki/                          # Layer 2: LLM-generated wiki (checked in)
│   ├── index.md                       # Master catalog
│   ├── log.md                         # Append-only ingest log
│   ├── search_index.txt               # Flat-file index for LLM querying
│   ├── organisms/                     # One page per organism (~155 species)
│   │   ├── homo_sapiens.md
│   │   ├── mus_musculus.md
│   │   └── ...
│   ├── assays/                        # One page per RNA-seq modality
│   │   ├── bulk_rnaseq.md
│   │   ├── scrna_seq.md
│   │   ├── snrna_seq.md
│   │   └── spatial.md
│   └── topics/                        # One page per research area (28 topics)
│       ├── cancer.md
│       ├── neuroscience.md
│       ├── microbiology.md
│       └── ...
│
├── scripts/                       # Pipeline scripts (run from project root)
│   ├── geo_metadata_fetcher.py        # Fetch raw GEO metadata from NCBI API
│   ├── extract_rnaseq.py              # Filter to RNA-seq, classify modality
│   ├── tag_topics.py                  # Infer research topics from titles/summaries
│   ├── ftp_probe.py                   # Probe individual GEO FTP dirs for file details
│   ├── index_ftp.py                   # Bulk FTP indexing across all classified datasets
│   ├── build_search_index.py          # Build wiki/search_index.txt for LLM querying
│   ├── generate_wiki.py              # Generate wiki markdown pages from classified data
│   └── merge_and_rebuild.py           # Merge snapshots, deduplicate, rebuild wiki
│
├── rnaseq_classified.json         # Intermediate: classified RNA-seq records (gitignored)
├── chipseq_classified.json        # Intermediate: classified ChIP-seq/ATAC-seq records (gitignored)
├── methylation_classified.json    # Intermediate: classified methylation records (gitignored)
├── multiomics_classified.json     # Intermediate: classified multiomics records (gitignored)
├── ftp_index.json                 # Intermediate: FTP file listings (gitignored)
├── ftp_probe_results.json         # Intermediate: FTP probe results (gitignored)
│
├── CLAUDE.md                      # Layer 3: Schema and project instructions
└── plans.md                       # Project roadmap and architecture notes
```

**Data flow:** `data/` (raw snapshots) → pipeline scripts → `wiki/` (LLM-queryable output)

Gitignored files (`data/`, `rnaseq_classified.json`, `ftp_index.json`, `ftp_probe_results.json`) are all reproducible via the pipeline scripts. Pre-built versions of the two intermediates are available via GitHub Releases — see the **Data Releases** section below.

## Data Releases

Pre-built data is distributed via GitHub Releases so users can skip the full pipeline (~18 hours). The current release is **`data-v1.0.0`**.

### Bootstrapping (new users)

```bash
# After cloning, fetch rnaseq_classified.json + ftp_index.json (~30 MB download)
conda run -n GEO_llm python scripts/bootstrap.py

# Optionally also fetch raw quarterly GEO metadata snapshots (~50 MB)
conda run -n GEO_llm python scripts/bootstrap.py --include-raw
```

### Publishing a new release (maintainers)

Run this after a pipeline rebuild to make the updated data available:

```bash
GITHUB_TOKEN=ghp_... conda run -n GEO_llm python scripts/create_data_release.py \
    --tag data-v2.0.0 \
    --notes "Coverage: 2015-Q1 through <date> | <N> RNA-seq datasets | 100% FTP indexed"
```

This packages `rnaseq_classified.json` + `ftp_index.json` into `bootstrap_data.tar.gz` and uploads it to a new GitHub Release. Use `--include-raw` to also bundle the `data/` quarterly snapshots.

Release tags follow the pattern `data-vMAJOR.MINOR.PATCH`. Increment MAJOR for schema-breaking changes, MINOR for new data coverage, PATCH for re-runs or fixes.

## Answering Dataset Queries

When the user asks about datasets (e.g., "find mouse kidney snRNA-seq datasets"), use these sources in order:

1. **Per-assay search index shards** — first stop for discovery. Choose the relevant shard and grep for organism, modality, topic. Each line is pipe-delimited: `accession|modality|organism|n_samples|files|topics|title|keywords|flags`.
   - `wiki/search_index_rnaseq.txt` — bulk, single-cell, single-nucleus, spatial (~130k records, 52.9 MB)
   - `wiki/search_index_chipseq.txt` — chip_seq, chip_exo (~26.6k records, 13.9 MB)
   - `wiki/search_index_atacseq.txt` — atac_seq (~6.6k records, 3.2 MB)
   - `wiki/search_index_cut_run_tag.txt` — cut_and_run, cut_and_tag (~1.4k records, 671 KB)
   - `wiki/search_index_methylation.txt` — wgbs, rrbs, em_seq, oxbs_seq, hmc_seq, medip_seq, methylation_array, other_methylation (~5.2k records, 1.9 MB)
   - `wiki/search_index_multiomics.txt` — cite_seq, multiome, spatial_multiomics, other_multiomics (~926 records, 546 KB)
   - `wiki/search_index.txt` — combined (all assay types); **gitignored**, reconstructable by concatenating the per-assay files
   - **`flags` field (9th column):** empty for most records; `multiomics` for records that also appear in `search_index_multiomics.txt`. Use this to filter for datasets where paired/joint multiomics data is available alongside the primary assay.
2. **`wiki/` pages** — organism, assay, and topic pages provide curated summaries grouped by facet. Note: these pages show summary stats (modality breakdown, organism distribution, related topics, file types) plus the **50 most recent datasets** in a table. They are not full listings — for comprehensive results, use the search index or `rnaseq_classified.json`.
3. **`data/*.json`** — raw GEO metadata with full summaries, platform info, pub dates, FTP links. **Use this when the user asks about a specific dataset or wants additional details** beyond what the search index provides (e.g., full abstract, platform, publication date, sample details). Grep for the accession (e.g., `GSE312968`) across the data files.
4. **`ftp_index.json`** — actual supplementary filenames and sizes from the GEO FTP server. Shows what preprocessed data is available (RDS, H5, MTX, CSV, etc.) and how large the files are.

## Key Data Files

**`rnaseq_classified.json`** — canonical classified dataset (JSON)
- One object per RNA-seq dataset with structured fields: `accession`, `title`, `summary` (first 500 chars), `organism`, `n_samples`, `platform_id`, `suppfile`, `pub_date`, `modality`, `topics` (array), `is_multiomics` (bool, added by `extract_multiomics.py`)
- Use for programmatic access and detailed lookups

**`chipseq_classified.json`** — canonical classified ChIP-seq/ATAC-seq dataset (JSON)
- Fields: `accession`, `title`, `summary`, `organism`, `n_samples`, `platform_id`, `suppfile`, `pub_date`, `modality`, `target_type`, `topics`, `is_multiomics` (bool, added by `extract_multiomics.py`)

**`multiomics_classified.json`** — canonical classified multiomics dataset (JSON)
- Fields: `accession`, `title`, `summary`, `organism`, `n_samples`, `platform_id`, `suppfile`, `pub_date`, `modality`, `topics`
- Overlaps intentionally with `rnaseq_classified.json` and `chipseq_classified.json` — a CITE-seq study will appear in both RNA-seq and multiomics sets

**`wiki/search_index_rnaseq.txt`**, **`search_index_chipseq.txt`**, **`search_index_atacseq.txt`**, **`search_index_cut_run_tag.txt`**, **`search_index_methylation.txt`**, **`search_index_multiomics.txt`** — grep-optimized search index shards (pipe-delimited text, checked into git)
- Format: `accession|modality|organism|n_samples|files|topics|title|keywords|flags`
- Summary replaced with extracted keywords (stop words removed, compressed)
- Includes FTP file info when available from `ftp_index.json` (actual filenames + sizes), falls back to `[GEO:types]` from suppfile field
- `flags` (9th column): `multiomics` if the record also appears in the multiomics shard; empty otherwise
- No `platform_id` or `pub_date`
- Use for fast grep-based discovery; pick the shard matching the assay type of interest

**`wiki/search_index.txt`** — combined index (all assay types, gitignored)
- Concatenation of all per-assay shards; too large for git (~70 MB) but reconstructable by re-running `build_search_index.py`
- Use for cross-assay queries when running locally

The search index is a denormalized, grep-friendly projection of the classified JSON enriched with FTP data. Both contain the same set of records.

## Current Data Coverage

- **Date range:** 2015-Q1 through April 2026 (45 quarterly snapshots)
- **Total unique GEO records:** ~227,000
- **RNA-seq datasets classified:** ~130,000
  - Bulk: ~104,000 | Single-cell: ~23,000 | Single-nucleus: ~2,000 | Spatial: ~1,000
- **Topic tagging:** ~96.6% tagged (~4,500 untagged — see Known Limitations)
- **FTP index:** Complete — 130,059 / 130,059 RNA-seq records indexed (100%)
- **ChIP-seq / chromatin datasets classified:** ~45,000
  - ChIP-seq: ~35,500 | ATAC-seq: ~8,000 | CUT&RUN: ~720 | CUT&Tag: ~710 | ChIP-exo: ~87
- **Methylation datasets classified:** ~7,258
  - Other/unclassified: ~3,750 | Array (450K/EPIC): ~1,347 | WGBS: ~1,240 | RRBS: ~516 | MeDIP-seq: ~196 | 5hmC-seq: ~110 | EM-seq: ~59 | oxBS-seq: ~40
- **Multiomics datasets classified:** ~926
  - CITE-seq: ~376 | Other multiomics: ~389 | 10x Multiome/SHARE-seq: ~86 | Spatial multiomics: ~75
  - 749 RNA-seq records and 353 ChIP-seq/ATAC-seq records back-annotated with `is_multiomics: true`
- **Wiki:** 155 organism pages, 28 topic pages, 18 assay pages (4 RNA-seq + 5 ChIP-seq/chromatin + 9 methylation)
- **Search index:** 170,741 total records (RNA-seq + ChIP-seq/ATAC-seq + methylation + multiomics combined)
- **Data release:** `data-v1.0.0` published on GitHub Releases (bootstrap bundle: 29.5 MB)

## Topic Taxonomy (28 topics)

The keyword-based tagger (`scripts/tag_topics.py`) assigns multi-label tags. A dataset can match multiple topics.

| Category | Topics |
|---|---|
| **Disease/Clinical** | cancer, infectious_disease, cardiovascular, kidney, lung_respiratory, gut_intestine, liver, eye_vision, skin |
| **Biology** | development, immunology, neuroscience, metabolism, hematopoiesis, reproduction, aging, cell_cycle, cell_stress |
| **Molecular** | epigenetics, rna_biology, gene_regulation, signal_transduction |
| **Methods/Tools** | crispr_gene_editing, drug_response |
| **Other** | microbiology, plant_biology, fibrosis_wound, skeletal_muscle |

## Known Limitations

- **~4,500 untagged records** — mostly ENCODE datasets with boilerplate summaries ("For data usage terms and conditions...") and records with very sparse metadata. These lack enough text for keyword matching.
- **Wiki pages show max 50 recent datasets** — by design in `generate_wiki.py` (`dataset_table(max_rows=50)`). Use `search_index.txt` or `rnaseq_classified.json` for full listings.
- **FTP indexing is slow** — ~1.6 records/sec due to NCBI rate limits. A full 130k-record run takes ~18 hours. The script saves incrementally (every 100 records) and can be resumed if interrupted.
- **Classification is rule-based** — `extract_rnaseq.py` uses keyword heuristics, not LLM classification. May misclassify edge cases. Phase 2 plans to use Anthropic API for more accurate batch classification.
- **RNA-seq only (Phase 1)** — ChIP-seq, ATAC-seq, methylation, and other assay types are not yet indexed. See `plans.md` Phase 3 for expansion roadmap.

## Key Design Decisions

- **LLM-first querying** — the search index and wiki pages are structured for LLM consumption, not just human browsing
- **Incremental updates** — new date windows are fetched and merged without duplicates (keyed on GSE accession, latest snapshot wins)
- **Phase 1 uses Claude Code interactively** for classification; Phase 2 will move to Anthropic API calls for automated batch processing
- **Conda environment** — all scripts run under the `GEO_llm` conda env via `conda run -n GEO_llm`
- **Multiomics cross-listing** — the same GSE accession intentionally appears in multiple classified sets (e.g., a 10x Multiome study is in both `rnaseq_classified.json` and `multiomics_classified.json`). This is by design: each shard answers queries about its primary assay type. The `is_multiomics` flag on RNA-seq and ChIP-seq records, and the `flags` column in the search index, let users discover that additional paired data exists for a given dataset.
- **Back-annotation pattern** — `extract_multiomics.py` is authoritative for the multiomics set. After running it, it patches `rnaseq_classified.json` and `chipseq_classified.json` in-place to set `is_multiomics: true` on overlapping accessions. `build_search_index.py` reads these flags and propagates them to the `flags` column of the per-assay search index shards.
