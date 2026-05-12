# Search Architecture

This project supports two distinct search modes. They share the same underlying data (the search index shards) but differ fundamentally in how the LLM is positioned relative to the grep step.

---

## Mode 1: CLI LLM (Claude Code, Gemini CLI, Codex)

```
User query
    │
    ▼
LLM reasons about query
    │
    ├─ "kidney" → grep wiki/search_index_rnaseq.txt for "kidney"
    ├─ "snRNA-seq" → already selected the right shard
    ├─ notices no H5 results → re-grep filtering on ".h5"
    └─ recognizes "APP/PS1" as Alzheimer's model → also greps "5XFAD", "amyloid"
    │
    ▼
LLM interprets, re-ranks, explains results
    │
    ▼
Response to user
```

The LLM **drives** the grep. It decides which shards to search, which terms to use, whether to refine or broaden, and when to stop. If the first grep misses something, the LLM can run another one. Domain knowledge (knowing that APP/PS1 and 5XFAD are both Alzheimer's mouse models, that "renal" and "kidney" are synonyms) is applied *before* the grep, not after.

This is the most capable search mode. It's also the most expensive in API calls and requires a running LLM with file access.

**Access pattern:** `LLM → grep → (re-grep if needed) → LLM → response`

---

## Mode 2: HF Spaces App

```
User query
    │
    ▼
Haiku expands query into biological synonyms
(e.g. "Alzheimer's" → ["APP/PS1", "5XFAD", "amyloid", "tau", "APOE", "neurodegeneration"])
    │
    ▼
Pass 1 grep: primary keyword terms (high precision)
Pass 2 grep: expanded synonym terms, any single match qualifies (higher recall)
    │
    ▼
Combined candidate set (~50–300 lines) passed to Sonnet
    │
    ▼
Sonnet ranks and explains results
    │
    ▼
Response to user
```

The app's grep runs **before** the main LLM (Sonnet) sees anything. Sonnet only receives the grep output — it cannot go back and run additional searches. This means any relevant records missed by both grep passes are permanently lost from that query's results.

To compensate, a lightweight pre-processing step uses Haiku to expand the query into biological synonyms before grepping. This is a one-shot inference call (cheap, ~100ms) that improves recall without adding latency to the main response.

The expanded terms are also included in the prompt to Sonnet so it can appropriately weight primary matches (exact keyword hits) versus expansion matches (synonym hits).

**Access pattern:** `Haiku expansion → grep (×2) → Sonnet → response`

---

## Why the two modes differ

| | CLI LLM | HF Space |
|---|---|---|
| LLM controls grep | Yes — iterative | No — grep runs first |
| Can re-search on miss | Yes | No |
| Domain knowledge applied | Before grep | Before grep (via expansion) + after (via Sonnet) |
| Cost per query | Higher (multiple LLM calls) | Lower (one Haiku + one Sonnet call) |
| Requires local file access | Yes | No — runs on HF infrastructure |
| Best for | Complex, iterative discovery | Quick lookup, no setup |

The CLI mode is inherently more capable because the LLM can observe partial results and adapt — tightening, broadening, or pivoting to a different shard mid-search. The app trades that flexibility for accessibility: anyone with credentials can use it from a browser with no local setup.

---

## The grep → LLM pattern

Both modes implement the same fundamental design: grep the index to a manageable candidate set, then pass that set to an LLM for interpretation.

The search index shards are structured specifically for this pattern — pipe-delimited, one record per line, with keywords extracted from titles and summaries. A single `grep -i "kidney" wiki/search_index_rnaseq.txt` returns a few hundred lines in milliseconds; passing those lines to an LLM takes seconds and produces a ranked, explained answer.

This contrasts with embedding-based semantic search, which would require a vector database, embedding API calls at query time, and infrastructure to host ~170k embeddings. The grep approach is simpler, faster to query, and requires no additional infrastructure — at the cost of relying on term overlap rather than semantic similarity. The LLM's domain knowledge bridges the gap for most queries.

---

## Query expansion in detail

Expansion is only used in the HF Space because it solves a problem specific to that mode (the LLM can't re-grep). The expansion prompt asks Haiku to generate:

- **Synonyms**: "kidney" → "renal", "nephro"
- **Abbreviations**: "Alzheimer's disease" → "AD"
- **Mouse model names**: "Alzheimer's" → "APP/PS1", "5XFAD", "3xTg-AD"
- **Gene/protein names**: "histone acetylation" → "H3K27ac", "CBP", "p300"
- **Disease aliases**: "ALS" → "amyotrophic lateral sclerosis", "motor neuron disease"

Expanded terms use `min_matches=1` (any single hit qualifies) rather than the primary search's intersection logic. This prevents the expansion from being too restrictive while still adding relevant results the primary pass missed. Results from the expansion pass are appended after primary results and capped at 100 per shard to keep the candidate set manageable.
