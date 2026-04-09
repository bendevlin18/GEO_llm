# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Single-script Python tool that fetches GEO (Gene Expression Omnibus) Series metadata from NCBI's Entrez E-Utilities API. It searches for GSE records published within a configurable time window, retrieves document summaries in batches, and outputs structured JSON.

## Running

```bash
# Requires Python 3.10+ (uses X | Y union type syntax)
# No external dependencies — stdlib only (urllib, xml, json, argparse)

python geo_metadata_fetcher.py --email you@example.com
python geo_metadata_fetcher.py --email you@example.com --months 6 --batch-size 300 --add-ftp-urls -o output.json
```

Email is required by NCBI policy. Can be set via `NCBI_EMAIL` env var. Optional `NCBI_API_KEY` env var raises rate limit from 3 to 10 req/sec.

## Architecture

All logic is in `geo_metadata_fetcher.py`. The pipeline is:

1. **eSearch** (`search_geo`) — queries GDS database for GSE records in a date range, returns History server params (query_key, webenv)
2. **eSummary** (`fetch_summaries`) — pages through results in batches using History server, parses XML DocumentSummary elements
3. **Parse** (`parse_doc_summary`) — extracts fields from each summary; filters to GSE-only records
4. **Output** — prints stats, writes JSON

`eutils_get` handles all HTTP requests with retry logic (3 attempts, exponential backoff). Rate limiting is enforced via `REQUEST_DELAY` (0.35s between requests).
