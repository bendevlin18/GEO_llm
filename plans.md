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

## Search Index Sharding (near-term)

`wiki/search_index.txt` is already at 69 MB and growing with each new assay type added. GitHub's soft limit is 50 MB and hard limit is 100 MB — adding methylation and ChIP-seq alone will push past the hard limit.

### Plan: one index file per assay family

Split `wiki/search_index.txt` into per-assay files:

```
wiki/search_index_rnaseq.txt       # ~130k records, ~52 MB
wiki/search_index_chipseq.txt      # ~35k records, ~14 MB
wiki/search_index_atacseq.txt      # ~8k records, ~3 MB
wiki/search_index_cut_run_tag.txt  # ~1.4k records, ~0.5 MB
wiki/search_index_methylation.txt  # (future)
wiki/search_index_other.txt        # catch-all for smaller assay types
```

Keep `wiki/search_index.txt` as a **combined index** but move it out of git (gitignore it) — it's too large for GitHub and can be reconstructed by concatenating the per-assay files. The per-assay files stay in git since each is well under 50 MB.

### Changes required

- `scripts/build_search_index.py` — write per-assay files in addition to (or instead of) the combined file
- `wiki/` — add the new per-assay index files, remove or gitignore the combined one
- `CLAUDE.md` — update querying instructions to name the per-assay files
- `README.md` — update grep examples to reference per-assay files

### LLM querying impact

Per-assay files are actually better for LLM use: an LLM asked about ChIP-seq data only needs to load `search_index_chipseq.txt`, not wade through 130k RNA-seq records. The combined index remains useful for cross-assay queries and can be generated locally.

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

### Data sharing

Data files are gitignored because they're large and reproducible via the pipeline — but re-running from scratch takes ~18 hours (FTP indexing alone). For others to bootstrap without that cost, the repo needs a data distribution strategy.

#### What needs sharing

| File | Size | Compressed estimate | Notes |
|---|---|---|---|
| `rnaseq_classified.json` | 103 MB | ~12 MB | Intermediate — skip extract+tag steps |
| `ftp_index.json` | 46 MB | ~5 MB | Intermediate — skip FTP indexing (~18 hrs) |
| `data/` (45 quarterly JSONs) | 315 MB | ~50 MB | Raw source — needed to re-run from scratch |
| `wiki/search_index.txt` | 52 MB | — | Already in git |

The two intermediates (`rnaseq_classified.json` + `ftp_index.json`) are the highest-value files to share — they let a new user skip the entire pipeline and go straight to querying or rebuilding the wiki.

#### Option A: GitHub Releases (recommended — simplest)

Attach compressed archives to a versioned GitHub Release (e.g., `data-v1.0`):
- `bootstrap_data.tar.gz` — intermediates only (`rnaseq_classified.json` + `ftp_index.json`, ~17 MB compressed)
- `raw_data.tar.gz` (optional) — all quarterly `data/` snapshots (~50 MB compressed)

A `scripts/bootstrap.py` script fetches and extracts the latest release assets using the GitHub API (no auth needed for public repos). Users run one command after cloning:

```bash
conda run -n GEO_llm python scripts/bootstrap.py
```

Pros: zero infrastructure, versioned alongside code, free, 2 GB/asset limit is not a concern here.
Cons: manual step to cut a new release when data updates; assets don't auto-update between releases.

#### Option B: Hugging Face Datasets

Host the intermediates as a dataset on the HF Hub (`bendevlin18/geo-rnaseq-index` or similar). The HF `datasets` library makes loading trivial for the target audience:

```python
from datasets import load_dataset
ds = load_dataset("bendevlin18/geo-rnaseq-index", split="train")
```

The `huggingface_hub` Python API supports programmatic uploads, so the pipeline can push updated data after each rebuild. Dataset cards provide searchable documentation.

Pros: excellent discoverability for ML/bioinformatics users, no infra, free, supports streaming large files.
Cons: requires HF account and API token in the pipeline; slightly awkward for non-Python consumers; format conversion (JSON → Parquet or Arrow) adds a step.

#### Option C: Git LFS

Un-gitignore the intermediate files and track them with Git LFS. Transparent to users — `git clone` fetches everything.

Free tier: 1 GB storage, 1 GB/month bandwidth.

With ~150 MB of intermediates, the storage limit is fine — but the 1 GB/month bandwidth cap would be hit quickly if the repo gets any real usage (~7 clones/month). Paid LFS bandwidth is $5/50 GB.

Pros: seamless for git users, no separate download step.
Cons: bandwidth costs at scale; slows down `git clone`; doesn't help with the 315 MB `data/` archive (would push storage over limit).

**Verdict: not recommended unless usage stays very low.**

#### Option D: DVC (Data Version Control)

Add DVC to the repo and point it at a cloud storage backend (S3, GCS, Backblaze B2, or Cloudflare R2 — R2 has no egress fees). Users run `dvc pull` after `git clone`.

```bash
git clone https://github.com/bendevlin18/GEO_llm
cd GEO_llm
dvc pull  # fetches data/ + intermediates from remote
```

DVC tracks data versions alongside code commits, so each git tag has a corresponding data snapshot.

Pros: proper data versioning, CI/CD friendly, supports all major cloud backends.
Cons: adds `dvc` as a dependency; requires provisioning and paying for cloud storage; more ops overhead than the project currently needs.

**Verdict: best long-term option if the project grows to multiple contributors or needs automated CI data updates.**

#### Recommended path

1. **Now:** implement Option A (GitHub Releases + bootstrap script). Low effort, unblocks external users immediately.
2. **If HF discoverability matters:** add Option B alongside A — push to HF Hub after each pipeline rebuild.
3. **If the project gets automated CI or multiple contributors:** migrate to Option D (DVC + R2).

## README Visualizations (`assets/`)

Static PNG charts embedded in the GitHub README to communicate dataset scope at a glance.
Generated by `scripts/generate_plots.py` from the classified JSON files — no external data needed beyond what's already in the repo (after bootstrapping).

### Charts to build

| File | Chart | Data source |
|---|---|---|
| `assets/plot_assay_overview.png` | Horizontal bar: total datasets by assay family | All classified JSONs |
| `assets/plot_rnaseq_modalities.png` | Horizontal bar: RNA-seq breakdown by modality | `rnaseq_classified.json` |
| `assets/plot_growth_over_time.png` | Line chart: datasets added per year, by assay family | All classified JSONs (pub_date) |
| `assets/plot_top_organisms.png` | Horizontal bar: top 15 organisms (RNA-seq) | `rnaseq_classified.json` |
| `assets/plot_topics.png` | Horizontal bar: top research topics (RNA-seq) | `rnaseq_classified.json` |

### Design constraints

- Output at 150 DPI, ~900px wide — renders cleanly in GitHub README at default width
- Consistent color palette across charts (one color per assay family)
- Clean style with minimal chrome — no heavy gridlines or chartjunk
- Requires `matplotlib` (add to conda env; not in stdlib but universal in bioinformatics)
- Script gracefully exits with a helpful message if matplotlib is not installed

### README embedding

Embed 3–4 charts directly in the README (overview, growth over time, top organisms, RNA-seq modalities). Link to the others from a "More plots" line. The `assets/` folder is checked into git so charts render on GitHub without any setup.

### Regeneration

Run after any pipeline rebuild to keep charts in sync with data:

```bash
conda run -n GEO_llm python scripts/generate_plots.py
```

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

## Free-Tier Access: Using the Wiki Without an LLM Subscription

The wiki and search index are designed for LLM querying, but many researchers won't have Claude Code, a paid API key, or any LLM subscription. This section tracks ways to make the resource useful to those users.

### The core problem

The search index shards are grep-friendly but large (the RNA-seq shard is 52 MB, 130k lines). The wiki pages are human-readable but don't support full-text search across all 170k records. Neither is convenient for a biologist who just wants to ask "do you have mouse kidney snRNA-seq data with processed H5 files?"

### Access tier 1: No tools required — browser + GitHub

The wiki pages are already readable on GitHub at `wiki/assays/`, `wiki/organisms/`, `wiki/topics/`. For simple browsing ("what mouse datasets exist?", "what scRNA-seq files does this modality have?"), the wiki pages are sufficient. GitHub's built-in file browser and search (Ctrl+F on any page) covers basic use cases.

**Improvements to support this tier:**
- Ensure wiki pages are well-organized and skimmable (already good)
- Add a `wiki/README.md` or improve `wiki/index.md` with a browsing guide so users who land on the wiki directory know where to start

### Access tier 2: Grep / Python — free, offline, no LLM needed

The pipe-delimited search index is explicitly designed for grep. Any user with Python or bash can run powerful queries with zero cost.

```bash
# Mouse kidney snRNA-seq with H5 files
grep "single-nucleus" wiki/search_index_rnaseq.txt | grep -i "mus musculus" | grep -i "kidney" | grep "H5"

# Human cancer scRNA-seq with processed Seurat objects
grep "single-cell" wiki/search_index_rnaseq.txt | grep -i "homo sapiens" | grep -i "cancer" | grep "RDS"
```

**Planned additions to support this tier:**
- `scripts/query.py` — a simple CLI wrapper around grep with named flags (`--modality`, `--organism`, `--topic`, `--files`, `--min-samples`). Returns formatted results. Zero dependencies beyond stdlib.
- Example query recipes in the README so users know the grep patterns without having to figure out the index format
- Potentially a short `QUERYING.md` guide in the wiki

### Access tier 3: Free cloud LLMs with file upload

Several free-tier cloud tools can ingest files and answer questions about them. These let a biologist describe what they want in plain English without knowing grep syntax.

**Google NotebookLM (best option for this use case)**
- Free with a Google account; no subscription needed
- Accepts uploaded documents as "sources" — users can upload one or more search index shards (or the smaller wiki pages) as source material
- Designed exactly for "chat with your documents" queries: "find mouse kidney snRNA-seq datasets that have RDS files and at least 10 samples"
- The 52 MB RNA-seq shard is large but the wiki assay pages (a few KB each) are a perfect fit
- **Plan:** add a section to the README explaining how to use NotebookLM with the wiki pages — which files to upload, example queries

**Google Gemini (gemini.google.com) — free tier**
- 1M token context window on free tier (as of 2025) — large enough to paste an entire shard
- Users can paste the contents of a search index shard directly into the chat and ask natural-language questions
- More friction than NotebookLM (manual copy-paste) but no setup required

**Claude.ai free tier**
- Smaller context window than Gemini but well-suited to pasting individual wiki pages (assay pages, organism pages) and asking follow-up questions
- Best for "I already found the assay page, tell me more / help me choose between these datasets"

**ChatGPT free tier**
- Similar to Claude.ai free — small context, works well for wiki page sections
- GPT-4o mini is available free and handles tabular markdown well

**Plan:** write a short guide ("Using the wiki with free AI tools") covering NotebookLM, Gemini, and Claude.ai free with concrete examples of what to upload and what to ask.

### Access tier 4: Local LLMs — free, private, no internet required

For users who can run local inference (researchers at institutions without cloud access, or those with privacy constraints):

**Ollama + llama3.1 / Mistral / Gemma**
- Free, runs on a laptop with 8+ GB RAM
- User installs Ollama, downloads a model, and pipes search index chunks into the model
- Works best with models that have 8k+ context windows; 128k-context models (like llama3.1) can handle entire wiki pages
- `scripts/query.py` (planned above) could have an `--llm` flag to pipe results through a local Ollama endpoint

**LM Studio**
- GUI for running local models; easier for non-technical users than Ollama CLI
- Same approach: load wiki pages or search index chunks as context

**Plan:** add an "offline / local LLM" note to the querying guide, with an Ollama one-liner example.

### Access tier 5: Hosted web interface — no install, no LLM needed

A lightweight static search interface that runs entirely in the browser, no server or LLM required.

**Option A: GitHub Pages + lunr.js or Fuse.js**
- Pre-build a JSON search index at wiki generation time (`scripts/generate_wiki.py` emits a `search_index.json` alongside the text shards)
- Deploy a static HTML/JS page to GitHub Pages that loads the JSON and supports faceted search (organism, modality, topic, file type, min samples)
- Zero hosting cost; updates automatically on each push
- Covers the "I want to search without any tools" use case entirely

**Option B: Hugging Face Spaces (Gradio app)**
- A small Gradio app that loads the search index shards and supports natural-language or faceted queries
- Free on HF Spaces for public repos; no user account required to use the demo
- Could integrate a free HF-hosted model (e.g., Mistral-7B via the Inference API) for natural-language querying on top of grep results
- More capable than the static option but requires Python runtime

**Recommended path:**
1. **Near-term:** add `scripts/query.py` CLI + grep recipe examples in the README (tier 2) — highest value, lowest effort
2. **Near-term:** add a NotebookLM / free LLM guide to the README (tier 3) — no code required, high discoverability
3. **Medium-term:** GitHub Pages static search (tier 5A) — covers users who won't touch a command line
4. **Later:** HF Spaces Gradio app (tier 5B) — richer experience, natural-language queries
