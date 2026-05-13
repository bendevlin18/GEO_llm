"""
Benchmark: App pipeline vs Agentic pipeline on the 10 standard queries.

App pipeline:   Haiku query expansion → grep (×2) → Sonnet answer
                Mirrors the HF Space exactly.

Agentic pipeline: Sonnet with a grep_shard tool, drives its own searches
                  iteratively — mirrors how Claude Code / Gemini CLI behave.

Output: tool_testing/benchmark_results_YYYY-MM-DD.md
Run:    conda run -n GEO_llm python scripts/run_benchmark.py
"""

import os
import re
import sys
import time
from datetime import date

import anthropic

client = anthropic.Anthropic()

# ---------------------------------------------------------------------------
# Shared constants (mirrors spaces/app.py)
# ---------------------------------------------------------------------------

SHARDS = {
    "rnaseq_singlecell": ("wiki/search_index_rnaseq_singlecell.txt", "scRNA-seq"),
    "rnaseq_snrnaseq":   ("wiki/search_index_rnaseq_snrnaseq.txt",   "snRNA-seq"),
    "rnaseq_spatial":    ("wiki/search_index_rnaseq_spatial.txt",    "spatial transcriptomics"),
    "rnaseq_bulk":       ("wiki/search_index_rnaseq.txt",            "bulk RNA-seq"),
    "chipseq":           ("wiki/search_index_chipseq.txt",           "ChIP-seq"),
    "atacseq":           ("wiki/search_index_atacseq.txt",           "ATAC-seq"),
    "cut_run_tag":       ("wiki/search_index_cut_run_tag.txt",       "CUT&RUN/CUT&Tag"),
    "methylation":       ("wiki/search_index_methylation.txt",       "methylation"),
    "multiomics":        ("wiki/search_index_multiomics.txt",        "multiomics"),
}

INDEX_FORMAT = "accession|modality|organism|n_samples|files|topics|title|keywords|flags"

SYSTEM_PROMPT = """You are a genomics dataset discovery assistant for the GEO Multi-omics Wiki,
a structured index of 170,000+ datasets from the Gene Expression Omnibus (GEO), 2015–2026.

When presenting results:
- Format as a markdown table: Accession (linked to GEO), Organism, Samples, Files, Title
- Link accessions as: [GSExxxxxx](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSExxxxxx)
- After the table, briefly explain the best matches and flag important caveats
- For comparison queries ("matched in size", "similar to"), highlight which pairs work well together
- "Processed data available" means files contain .h5, .h5ad, .rds, .RDS, .mtx.gz, or .csv.gz

Apply domain knowledge:
- Alzheimer's mouse models: APP/PS1 (APPswe/PSEN1dE9), 5XFAD, 3xTg-AD, APP-KI, J20
- Parkinson's models: MPTP, 6-OHDA, AAV-α-synuclein, LRRK2
- Common cell lines: HEK293, HeLa, Jurkat, K562, MCF7, A549
- scRNA-seq platforms: 10x Genomics, Drop-seq, Smart-seq2, inDrop
- n_samples is the number of GEO Samples (GSMs) — roughly biological replicates"""

STOP_WORDS = {
    "a", "an", "the", "and", "or", "for", "with", "from", "in", "of",
    "to", "is", "are", "find", "show", "me", "datasets", "data", "samples",
    "studies", "study", "get", "give", "want", "need", "looking", "search",
    "have", "any", "some", "there", "that", "this", "these", "which", "where",
    "what", "how", "many", "more", "than", "least", "most", "please", "can",
    "could", "would", "like", "similar", "size", "large", "small", "also",
    "both", "using", "used", "use",
    "rna", "seq", "rnaseq", "cell", "cells", "gene", "genes", "expression",
    "analysis", "mouse", "human", "mice", "single", "bulk", "sequencing",
    "transcriptom", "genomic", "profil",
}

ASSAY_TERMS = {
    "single-cell", "single-nucleus", "spatial", "scrna", "scrnaseq", "snrna",
    "snrnaseq", "rna-seq", "rnaseq", "chip-seq", "chipseq", "atac-seq",
    "cut&run", "cut&tag", "wgbs", "rrbs", "bisulfite", "cite-seq", "multiome",
    "transcriptomics", "transcriptome",
}

MODALITY_SIGNALS = {
    "rnaseq_singlecell": ["single-cell", "scrna", "scrnaseq", "sc rna", "10x", "dropseq",
                          "drop-seq", "smart-seq", "inDrop", "single cell rna"],
    "rnaseq_snrnaseq":   ["single nucleus", "snrna", "snrnaseq", "sn rna", "single-nucleus",
                          "nuclear rna", "snuc"],
    "rnaseq_spatial":    ["spatial", "visium", "merfish", "slide-seq", "slideseq",
                          "stereo-seq", "seqfish", "spatial transcriptom"],
    "rnaseq_bulk":       ["bulk rna", "bulk-rna", "total rna", "rna-seq", "rnaseq",
                          "gene expression", "transcriptom"],
    "chipseq":           ["chip-seq", "chipseq", "chip seq", "histone", "h3k4", "h3k27",
                          "h3k36", "h3k9", "transcription factor", "tf binding", "chip"],
    "atacseq":           ["atac", "chromatin accessibility", "open chromatin", "dnase"],
    "cut_run_tag":       ["cut&run", "cut and run", "cut&tag", "cut and tag", "cutana"],
    "methylation":       ["methylation", "wgbs", "rrbs", "bisulfite", "cpg", "5mc", "5hmc",
                          "dnmt", "methylom", "em-seq", "medip"],
    "multiomics":        ["cite-seq", "cite seq", "multiome", "10x multiome", "share-seq",
                          "multi-omic", "multiomics", "rna+atac", "protein and rna"],
}

QUERIES_FILE = "tool_testing/benchmark_queries.md"


def load_queries(path: str = QUERIES_FILE) -> list[tuple[str, str, str]]:
    queries = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|") or line.startswith("| ID") or line.startswith("|---"):
                continue
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) == 3:
                queries.append((parts[0], parts[1], parts[2]))
    return queries


BENCHMARK_QUERIES = load_queries()

# ---------------------------------------------------------------------------
# App pipeline (mirrors spaces/app.py)
# ---------------------------------------------------------------------------

def detect_shards(query: str) -> list[str]:
    if re.search(r'\bGSE\d+\b', query, re.IGNORECASE):
        return list(SHARDS.keys())
    q = query.lower()
    scores = {k: 0 for k in MODALITY_SIGNALS}
    for shard_key, signals in MODALITY_SIGNALS.items():
        for sig in signals:
            if sig in q:
                scores[shard_key] += 1
    matched = sorted([k for k, v in scores.items() if v > 0], key=lambda k: -scores[k])
    return matched or ["rnaseq_singlecell", "rnaseq_bulk", "rnaseq_snrnaseq", "rnaseq_spatial"]


def extract_terms(query: str) -> list[str]:
    compound = re.findall(r'[A-Za-z0-9]+[/\-][A-Za-z0-9]+', query)
    words = re.findall(r'\b[A-Za-z0-9]{4,}\b', query)
    words = [w for w in words if w.lower() not in STOP_WORDS and w.lower() not in ASSAY_TERMS]
    seen, terms = set(), []
    for t in compound + words:
        if t.lower() not in seen and t.lower() not in ASSAY_TERMS:
            seen.add(t.lower())
            terms.append(t)
    return terms[:8]


def expand_query(query: str) -> list[str]:
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=150,
            messages=[{"role": "user", "content": (
                f"Given this GEO dataset search query, list 5-8 additional specific biological terms "
                f"(synonyms, abbreviations, gene names, mouse model names, cell line names, disease aliases) "
                f"that would appear in relevant dataset titles or summaries.\n"
                f"Query: {query}\n"
                f"Return only a comma-separated list. No explanations. No generic words like 'mouse' or 'RNA'."
            )}],
        )
        raw = response.content[0].text.strip()
        return [t.strip() for t in raw.split(",") if t.strip() and len(t.strip()) >= 3][:8]
    except Exception:
        return []


def search_shard(shard_path: str, terms: list[str], modality_filter: str | None = None,
                 max_results: int = 300, min_matches_override: int | None = None) -> list[str]:
    if not os.path.exists(shard_path):
        return []
    terms_lower = [t.lower() for t in terms]
    if min_matches_override is not None:
        min_matches = min_matches_override
    else:
        min_matches = len(terms_lower) if len(terms_lower) <= 3 else max(2, len(terms_lower) // 2)
    scored = []
    with open(shard_path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            line = line.rstrip("\n")
            if modality_filter:
                cols = line.split("|")
                if len(cols) < 2 or cols[1] != modality_filter:
                    continue
            line_lower = line.lower()
            n = sum(1 for t in terms_lower if t in line_lower)
            if n >= min_matches:
                scored.append((n, line))
    scored.sort(key=lambda x: -x[0])
    return [l for _, l in scored[:max_results]]


def run_app_pipeline(query: str) -> dict:
    shard_keys = detect_shards(query)
    terms = extract_terms(query)
    expanded = expand_query(query)

    all_lines, seen, summaries = [], set(), []

    for key in shard_keys:
        path, label = SHARDS[key]
        mod_filter = "bulk" if key == "rnaseq_bulk" else None
        hits = search_shard(path, terms, modality_filter=mod_filter)
        primary_count = sum(1 for h in hits[:150] if h.split("|")[0] not in seen)
        for h in hits[:150]:
            acc = h.split("|")[0]
            if acc not in seen:
                all_lines.append(h)
                seen.add(acc)

        exp_count = 0
        if expanded:
            for h in search_shard(path, expanded, modality_filter=mod_filter,
                                  max_results=100, min_matches_override=1):
                acc = h.split("|")[0]
                if acc not in seen:
                    all_lines.append(h)
                    seen.add(acc)
                    exp_count += 1

        total = primary_count + exp_count
        if total:
            note = f" (+{exp_count} via synonyms)" if exp_count and primary_count else " (via synonyms)" if exp_count else ""
            summaries.append(f"{label}: {total}{note}")

    candidates = all_lines[:300]
    search_note = ", ".join(summaries) if summaries else "no results"
    expansion_note = f"\nExpanded search terms: {', '.join(expanded)}" if expanded else ""

    if not candidates:
        user_msg = (f'The user searched for: "{query}"\n\nNo matching records found. '
                    'Suggest alternative search terms.')
    else:
        user_msg = (f'The user is searching the GEO Multi-omics index for: "{query}"\n\n'
                    f'Index format: {INDEX_FORMAT}\n\n'
                    f'Search results ({search_note}){expansion_note}:\n'
                    + "\n".join(candidates)
                    + '\n\nIdentify the most relevant datasets and present them clearly.')

    response = api_create_with_backoff(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
    )
    return {
        "answer": response.content[0].text,
        "shards_searched": shard_keys,
        "terms": terms,
        "expanded": expanded,
        "n_candidates": len(candidates),
        "summary": search_note,
    }


# ---------------------------------------------------------------------------
# Agentic pipeline (Claude drives its own grep searches)
# ---------------------------------------------------------------------------

GREP_TOOL = {
    "name": "grep_shard",
    "description": (
        "Search a GEO dataset index shard. Returns pipe-delimited lines: "
        "accession|modality|organism|n_samples|files|topics|title|keywords|flags. "
        "Run multiple searches with different terms or shards to find the best candidates."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "shard": {
                "type": "string",
                "enum": list(SHARDS.keys()),
                "description": "Which index shard to search.",
            },
            "terms": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Search terms (case-insensitive). All terms must appear in a matching line.",
            },
            "require_any": {
                "type": "boolean",
                "description": "If true, any single term matching is enough (OR logic). Default false (AND).",
            },
        },
        "required": ["shard", "terms"],
    },
}

AGENTIC_SYSTEM = SYSTEM_PROMPT + f"""

You have access to a grep_shard tool that searches GEO index shards.
Available shards: {', '.join(SHARDS.keys())}
Index format: {INDEX_FORMAT}

Strategy:
- Pick the right shard(s) based on assay type
- Use specific biological terms, not generic ones
- Run follow-up searches if initial results are sparse or miss domain synonyms
- For ambiguous queries, search multiple shards
"""


def run_grep_tool(shard: str, terms: list[str], require_any: bool = False) -> str:
    path, label = SHARDS[shard]
    mod_filter = "bulk" if shard == "rnaseq_bulk" else None
    min_override = 1 if require_any else None
    hits = search_shard(path, terms, modality_filter=mod_filter,
                        max_results=150, min_matches_override=min_override)
    if not hits:
        return f"No results found in {label} for terms: {terms}"
    return f"# {label} — {len(hits)} results\n" + "\n".join(hits[:100])


def api_create_with_backoff(**kwargs):
    for attempt in range(6):
        try:
            return client.messages.create(**kwargs)
        except anthropic.RateLimitError:
            wait = 30 * (2 ** attempt)
            print(f"    rate limited — waiting {wait}s…", flush=True)
            time.sleep(wait)
    return client.messages.create(**kwargs)


def run_agentic_pipeline(query: str) -> dict:
    messages = [{"role": "user", "content": query}]
    tool_calls = []

    while True:
        response = api_create_with_backoff(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            system=AGENTIC_SYSTEM,
            tools=[GREP_TOOL],
            messages=messages,
        )

        if response.stop_reason == "end_turn":
            answer = next((b.text for b in response.content if hasattr(b, "text")), "")
            return {"answer": answer, "tool_calls": tool_calls}

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    args = block.input
                    result = run_grep_tool(
                        shard=args["shard"],
                        terms=args["terms"],
                        require_any=args.get("require_any", False),
                    )
                    tool_calls.append({"shard": args["shard"], "terms": args["terms"]})
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
        else:
            break

    return {"answer": "(pipeline error)", "tool_calls": tool_calls}


# ---------------------------------------------------------------------------
# Runner and output
# ---------------------------------------------------------------------------

def run_benchmark(queries: list | None = None, out_dir: str = "tool_testing") -> None:
    queries = queries or BENCHMARK_QUERIES
    today = date.today().isoformat()

    for qid, tier, query in queries:
        out_path = f"{out_dir}/{today}_{qid}.md"
        print(f"Running {qid} ({tier})…", flush=True)

        print(f"  app pipeline…", flush=True)
        app = run_app_pipeline(query)

        print(f"  agentic pipeline…", flush=True)
        agentic = run_agentic_pipeline(query)

        tool_summary = "; ".join(
            f"{c['shard']}({', '.join(c['terms'])})" for c in agentic["tool_calls"]
        ) or "none"

        block = "\n".join([
            f"# {qid} ({tier}) — {today}",
            f"**Query:** {query}",
            "",
            "## App pipeline",
            f"*Shards: {', '.join(app['shards_searched'])} | "
            f"Terms: {', '.join(app['terms'])} | "
            f"Expanded: {', '.join(app['expanded'])} | "
            f"Candidates: {app['n_candidates']} | {app['summary']}*",
            "",
            app["answer"],
            "",
            "## Agentic pipeline",
            f"*Tool calls: {tool_summary}*",
            "",
            agentic["answer"],
            "",
        ])

        with open(out_path, "w") as f:
            f.write(block)

        print(f"  done. Written to {out_path}", flush=True)


if __name__ == "__main__":
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not set.")
        print("Run as: ANTHROPIC_API_KEY=sk-ant-... conda run -n GEO_llm python scripts/run_benchmark.py")
        sys.exit(1)

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--queries", nargs="+", help="Run specific query IDs only, e.g. Q1 Q6")
    parser.add_argument("--out-dir", default="tool_testing", help="Output directory")
    args = parser.parse_args()

    subset = [q for q in BENCHMARK_QUERIES if q[0] in args.queries] if args.queries else None
    run_benchmark(subset, out_dir=args.out_dir)
