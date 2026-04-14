---
title: GEO Multi-omics Search
emoji: 🧬
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: "5.0.0"
app_file: app.py
pinned: false
license: mit
---

# GEO Multi-omics Search

Natural-language search over 170,000+ genomics datasets from [GEO (Gene Expression Omnibus)](https://www.ncbi.nlm.nih.gov/geo/).

Search using plain English — no command line or grep knowledge required. Covers RNA-seq (bulk, single-cell, snRNA-seq, spatial), ChIP-seq, ATAC-seq, CUT&RUN/Tag, methylation, and multiomics datasets from 2015 through early 2026.

## How it works

1. Your query is matched against the GEO search index shards using keyword grep
2. Matching records (~50–300 lines) are passed to Claude Haiku for ranking and interpretation
3. Results are returned as a formatted table with direct links to NCBI GEO

The full 170k-record index lives on disk — only filtered candidates reach the LLM context window.

## Setup

See the [GEO Multi-omics Wiki repo](https://github.com/bendevlin18/GEO_llm) for the full pipeline and data sources.

Requires `ANTHROPIC_API_KEY` set as a Space secret.
