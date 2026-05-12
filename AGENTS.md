# AGENTS.md

Shared project context for all AI coding assistants (Claude Code, Gemini CLI, Codex, etc.).
Workflow prompts live in `prompts/` — see each tool's config file for how to invoke them.

## Project Overview

A periodically-updated, LLM-generated wiki that indexes GEO (Gene Expression Omnibus) datasets by organism, assay modality, research topic, and data availability. Inspired by [Karpathy's LLM wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

The search index shards (`wiki/search_index_*.txt`) are designed for LLM querying: grep to a candidate set, then pass to an LLM for interpretation and ranking. Primary access pattern: **grep → LLM**, not **grep → human**.

## Architecture

**Layer 1 — Raw Sources (`data/`):** JSON snapshots from `geo_metadata_fetcher.py`, named `geo_metadata_YYYY-QN.json`. Gitignored; reproducible via pipeline.

**Layer 2 — Wiki (`wiki/`):** LLM-generated markdown pages by organism, assay type, and research topic. Includes `wiki/index.md` (master catalog), `wiki/log.md` (ingest log), and per-assay search index shards (checked in).

**Layer 3 — Schema (`AGENTS.md` + `prompts/`):** Project instructions, tagging taxonomy, and workflow prompts.

## Pipeline Scripts

All scripts live in `scripts/` and run from the project root via `conda run -n GEO_llm python scripts/<script>.py`.

| Script | Purpose |
|---|---|
| `geo_metadata_fetcher.py` | Fetch GEO Series metadata from NCBI E-Utilities API |
| `extract_rnaseq.py` | Filter to RNA-seq, classify modality |
| `extract_chipseq.py` | Filter to ChIP-seq/ATAC-seq, classify modality and target type |
| `extract_methylation.py` | Filter to methylation datasets, classify protocol |
| `extract_multiomics.py` | Filter to multiomics (CITE-seq, 10x Multiome, etc.); back-annotates RNA-seq + ChIP-seq with `is_multiomics: true` |
| `tag_topics.py` | Infer research topics from titles/summaries |
| `index_ftp.py` | Bulk FTP indexing (~1.6 rec/sec, ~18 hr for full run; incremental) |
| `build_search_index.py` | Build per-assay `wiki/search_index_*.txt` shards |
| `generate_wiki.py` | Generate wiki markdown pages from classified data |
| `generate_plots.py` | Generate PNG charts for README (`assets/`); requires matplotlib |
| `bootstrap.py` | Download pre-built data files from latest GitHub Release |
| `create_data_release.py` | (Maintainer) Create a GitHub Release and upload data assets |
| `merge_and_rebuild.py` | Merge snapshots, deduplicate, rebuild wiki end-to-end |

**Environment:** `conda run -n GEO_llm python scripts/<script>.py` (Python 3.10+, mostly stdlib)
**NCBI email:** `benjamin.devlin@duke.edu` (required by policy; also via `NCBI_EMAIL` env var)
**NCBI API key:** optional `NCBI_API_KEY` env var raises rate limit from 3 → 10 req/sec

**Bootstrap** (skip the ~18 hr pipeline): `conda run -n GEO_llm python scripts/bootstrap.py`

See `prompts/rebuild.md`, `prompts/fetch.md`, and `prompts/release.md` for full workflow steps.

## Answering Dataset Queries

When asked about datasets, use these sources in order:

1. **Per-assay search index shards** — first stop. Grep for organism, modality, topic. Format: `accession|modality|organism|n_samples|files|topics|title|keywords|flags`
   - `wiki/search_index_rnaseq.txt` — bulk, single-cell, single-nucleus, spatial (~130k records)
   - `wiki/search_index_chipseq.txt` — chip_seq, chip_exo (~26.6k records)
   - `wiki/search_index_atacseq.txt` — atac_seq (~6.6k records)
   - `wiki/search_index_cut_run_tag.txt` — cut_and_run, cut_and_tag (~1.4k records)
   - `wiki/search_index_methylation.txt` — wgbs, rrbs, em_seq, oxbs_seq, hmc_seq, medip_seq, methylation_array (~5.2k records)
   - `wiki/search_index_multiomics.txt` — cite_seq, multiome, spatial_multiomics (~926 records)
   - `flags` field (9th column): `multiomics` = paired multi-assay data exists for this record
2. **`wiki/` pages** — curated summaries + 50 most recent datasets per facet (not full listings)
3. **`data/*.json`** — raw GEO metadata with full abstracts, platform info, pub dates; use for specific dataset lookups
4. **`ftp_index.json`** — actual supplementary filenames and sizes from GEO FTP

**Protocol guidance** — if the user asks how to analyze a dataset, match file extensions to:

| Extensions | Protocol |
|---|---|
| `.csv.gz`, `.tsv.gz`, `.txt.gz` (bulk) | `wiki/protocols/csv_tsv_counts.md` |
| `.rds.gz`, `.RData.gz`, `.rda.gz` | `wiki/protocols/rds_seurat.md` |
| `.h5ad.gz` | `wiki/protocols/h5ad_anndata.md` |
| `.h5` (CellRanger output) | `wiki/protocols/h5_cellranger.md` |
| `.mtx.gz` + barcodes + features | `wiki/protocols/mtx_10x.md` |
| `no_suppl`, `RAW.tar`, or SRA | `wiki/protocols/fastq_alignment.md` |

See `wiki/protocols/index.md` for a decision table with effort tiers.

## Key Data Files

**`*_classified.json`** — one record per dataset; fields: `accession`, `title`, `summary`, `organism`, `n_samples`, `platform_id`, `suppfile`, `pub_date`, `modality`, `topics`, `is_multiomics`
- ChIP-seq adds `target_type`; multiomics overlaps intentionally with RNA-seq and ChIP-seq sets

**Search index shards** — denormalized, grep-friendly projections of the classified JSON enriched with FTP data. `flags=multiomics` propagated from `extract_multiomics.py` back-annotation.

**`wiki/search_index.txt`** — combined shard (all assay types, gitignored); reconstructable via `build_search_index.py`

## Current Data Coverage

- **Date range:** 2015-Q1 through April 2026 (45 quarterly snapshots)
- **RNA-seq:** ~130,000 datasets — Bulk: ~104k | scRNA: ~23k | snRNA: ~2k | Spatial: ~1k
- **ChIP-seq/chromatin:** ~45,000 — ChIP-seq: ~35.5k | ATAC-seq: ~8k | CUT&RUN: ~720 | CUT&Tag: ~710
- **Methylation:** ~7,258 — WGBS: ~1.2k | RRBS: ~516 | Array: ~1.3k | other: ~3.8k
- **Multiomics:** ~926 — CITE-seq: ~376 | 10x Multiome/SHARE-seq: ~86 | Spatial: ~75
- **FTP index:** 100% complete (130,059 / 130,059 RNA-seq records)
- **Wiki:** 155 organism pages, 28 topic pages, 18 assay pages
- **Data release:** `data-v1.0.0` on GitHub Releases (~29.5 MB bootstrap bundle)

## Topic Taxonomy (28 topics)

| Category | Topics |
|---|---|
| **Disease/Clinical** | cancer, infectious_disease, cardiovascular, kidney, lung_respiratory, gut_intestine, liver, eye_vision, skin |
| **Biology** | development, immunology, neuroscience, metabolism, hematopoiesis, reproduction, aging, cell_cycle, cell_stress |
| **Molecular** | epigenetics, rna_biology, gene_regulation, signal_transduction |
| **Methods/Tools** | crispr_gene_editing, drug_response |
| **Other** | microbiology, plant_biology, fibrosis_wound, skeletal_muscle |

Assigned by `tag_topics.py` (keyword-based, multi-label). ~4,500 ENCODE records untagged due to boilerplate summaries.

## Known Limitations

- **~4,500 untagged records** — ENCODE datasets with boilerplate summaries lack enough text for keyword matching
- **Wiki pages show max 50 datasets** — by design; use search index shards or `*_classified.json` for full listings
- **FTP indexing is slow** — ~18 hr full run; incremental saves every 100 records, safe to interrupt and resume
- **Rule-based classification** — `extract_*.py` uses keyword heuristics; may misclassify edge cases

## Key Design Decisions

- **Multiomics cross-listing** — a CITE-seq study appears in both `rnaseq_classified.json` and `multiomics_classified.json` by design; each shard answers queries about its primary assay type
- **Back-annotation** — `extract_multiomics.py` patches `rnaseq_classified.json` and `chipseq_classified.json` in-place to set `is_multiomics: true`; `build_search_index.py` propagates this to the `flags` column
- **Incremental updates** — date windows are merged without duplicates (keyed on GSE accession; latest snapshot wins)
- **LLM-first** — index and wiki pages are structured for LLM consumption; complex queries require domain knowledge and reasoning that simple search UIs cannot provide
