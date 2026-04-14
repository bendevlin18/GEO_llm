"""
GEO Multi-omics Search — Hugging Face Spaces app
Natural-language dataset discovery over 170k+ GEO records.

Architecture: user query → grep shard(s) → Claude Haiku → formatted answer
The full search index lives on disk; only grep results (~50-300 lines) ever
reach the LLM context window.
"""

import os
import re
from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# ---------------------------------------------------------------------------
# Shard registry
# ---------------------------------------------------------------------------

SHARDS = {
    "rnaseq_singlecell":  ("wiki/search_index_rnaseq_singlecell.txt",  "scRNA-seq"),
    "rnaseq_snrnaseq":    ("wiki/search_index_rnaseq_snrnaseq.txt",    "snRNA-seq"),
    "rnaseq_spatial":     ("wiki/search_index_rnaseq_spatial.txt",     "spatial transcriptomics"),
    "rnaseq_bulk":        ("wiki/search_index_rnaseq.txt",             "bulk RNA-seq"),
    "chipseq":            ("wiki/search_index_chipseq.txt",            "ChIP-seq"),
    "atacseq":            ("wiki/search_index_atacseq.txt",            "ATAC-seq"),
    "cut_run_tag":        ("wiki/search_index_cut_run_tag.txt",        "CUT&RUN/CUT&Tag"),
    "methylation":        ("wiki/search_index_methylation.txt",        "methylation"),
    "multiomics":         ("wiki/search_index_multiomics.txt",         "multiomics"),
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
  (not just RAW.tar or no_suppl, which means raw reads only)

Apply this domain knowledge — researchers often use shorthand not in structured fields:
- Alzheimer's mouse models: APP/PS1 (APPswe/PSEN1dE9), 5XFAD, 3xTg-AD, APP-KI, J20
- Parkinson's models: MPTP, 6-OHDA, AAV-α-synuclein, LRRK2
- Common cell lines: HEK293, HeLa, Jurkat, K562, MCF7, A549
- scRNA-seq platforms: 10x Genomics, Drop-seq, Smart-seq2, inDrop
- n_samples is the number of GEO Samples (GSMs) — roughly biological replicates or individuals"""


# ---------------------------------------------------------------------------
# Shard detection
# ---------------------------------------------------------------------------

MODALITY_SIGNALS = {
    "rnaseq_singlecell": [
        "single-cell", "scrna", "scrnaseq", "sc rna", "10x", "dropseq",
        "drop-seq", "smart-seq", "inDrop", "single cell rna",
    ],
    "rnaseq_snrnaseq": [
        "single nucleus", "snrna", "snrnaseq", "sn rna", "single-nucleus",
        "nuclear rna", "snuc",
    ],
    "rnaseq_spatial": [
        "spatial", "visium", "merfish", "slide-seq", "slideseq",
        "stereo-seq", "seqfish", "spatial transcriptom",
    ],
    "rnaseq_bulk": [
        "bulk rna", "bulk-rna", "total rna", "rna-seq", "rnaseq",
        "gene expression", "transcriptom",
    ],
    "chipseq": [
        "chip-seq", "chipseq", "chip seq", "histone", "h3k4", "h3k27",
        "h3k36", "h3k9", "transcription factor", "tf binding", "chip",
    ],
    "atacseq": [
        "atac", "chromatin accessibility", "open chromatin", "dnase",
    ],
    "cut_run_tag": [
        "cut&run", "cut and run", "cut&tag", "cut and tag", "cutana",
    ],
    "methylation": [
        "methylation", "wgbs", "rrbs", "bisulfite", "cpg", "5mc", "5hmc",
        "dnmt", "methylom", "em-seq", "medip",
    ],
    "multiomics": [
        "cite-seq", "cite seq", "multiome", "10x multiome", "share-seq",
        "multi-omic", "multiomics", "rna+atac", "protein and rna",
    ],
}


def detect_shards(query: str) -> list[str]:
    """Return ordered list of shard keys to search, based on query signals."""
    q = query.lower()
    scores: dict[str, int] = {k: 0 for k in MODALITY_SIGNALS}
    for shard_key, signals in MODALITY_SIGNALS.items():
        for sig in signals:
            if sig in q:
                scores[shard_key] += 1

    # Pick shards with any signal, sorted by score
    matched = sorted([k for k, v in scores.items() if v > 0], key=lambda k: -scores[k])

    if not matched:
        # No explicit modality signal — default to single-cell (most common complex query)
        # and snRNA + spatial as secondary
        return ["rnaseq_singlecell", "rnaseq_snrnaseq", "rnaseq_spatial"]

    return matched


# ---------------------------------------------------------------------------
# Grep
# ---------------------------------------------------------------------------

STOP_WORDS = {
    # General English
    "a", "an", "the", "and", "or", "for", "with", "from", "in", "of",
    "to", "is", "are", "find", "show", "me", "datasets", "data", "samples",
    "studies", "study", "get", "give", "want", "need", "looking", "search",
    "have", "any", "some", "there", "that", "this", "these", "which", "where",
    "what", "how", "many", "more", "than", "least", "most", "please", "can",
    "could", "would", "like", "similar", "size", "large", "small", "also",
    "both", "using", "used", "use",
    # Genomics-generic — appear in almost every record, useless as grep filters
    "rna", "seq", "rnaseq", "cell", "cells", "gene", "genes", "expression",
    "analysis", "mouse", "human", "mice", "single", "bulk", "sequencing",
    "transcriptom", "genomic", "profil",
}


# Assay/modality terms — handled by shard selection, not useful as grep filters
# (e.g. "single-cell" appears in every record of the singlecell shard)
ASSAY_TERMS = {
    "single-cell", "single-nucleus", "spatial", "scrna", "scrnaseq", "snrna",
    "snrnaseq", "rna-seq", "rnaseq", "chip-seq", "chipseq", "atac-seq",
    "cut&run", "cut&tag", "wgbs", "rrbs", "bisulfite", "cite-seq", "multiome",
    "transcriptomics", "transcriptome",
}


def extract_terms(query: str) -> list[str]:
    """
    Extract specific, grep-useful tokens from a natural language query.
    Compounds (APP/PS1, 5XFAD, H3K27ac) are kept whole and take priority.
    Assay/modality terms are stripped since shard selection handles those.
    """
    # Compound biological terms: APP/PS1, 5XFAD, H3K27ac, Mus musculus → keep whole
    compound = re.findall(r'[A-Za-z0-9]+[/\-][A-Za-z0-9]+', query)

    # Individual word tokens (≥4 chars, not a stop word, not an assay term)
    words = re.findall(r'\b[A-Za-z0-9]{4,}\b', query)
    words = [w for w in words
             if w.lower() not in STOP_WORDS and w.lower() not in ASSAY_TERMS]

    # Deduplicate, compounds first (highest signal)
    seen = set()
    terms = []
    for t in compound + words:
        tl = t.lower()
        if tl not in seen and tl not in ASSAY_TERMS:
            seen.add(tl)
            terms.append(t)

    return terms[:8]


def search_shard(shard_path: str, terms: list[str], modality_filter: str | None = None,
                 max_results: int = 300) -> list[str]:
    """
    Stream through a shard and score lines by how many terms they match.
    Returns up to max_results lines, ranked by match count (highest first).
    Requires at least min_matches terms to hit (tightened if many terms available).
    """
    if not os.path.exists(shard_path):
        return []

    terms_lower = [t.lower() for t in terms]
    # Require all terms to match when we have ≤3 specific terms;
    # require at least half when we have more (handles broad queries gracefully)
    min_matches = len(terms_lower) if len(terms_lower) <= 3 else max(2, len(terms_lower) // 2)

    scored: list[tuple[int, str]] = []

    with open(shard_path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            line = line.rstrip("\n")
            if not line:
                continue

            if modality_filter:
                cols = line.split("|")
                if len(cols) < 2 or cols[1] != modality_filter:
                    continue

            line_lower = line.lower()
            n_matches = sum(1 for t in terms_lower if t in line_lower)
            if n_matches >= min_matches:
                scored.append((n_matches, line))

    # Sort by match count descending, return top results
    scored.sort(key=lambda x: -x[0])
    return [line for _, line in scored[:max_results]]


def run_search(query: str) -> tuple[list[str], list[str]]:
    """
    Detect shards, run scored intersection search, return
    (candidate_lines, search_summary_strings).
    Falls back to a single-term broad search if intersection yields nothing.
    """
    shard_keys = detect_shards(query)
    terms = extract_terms(query)

    all_lines: list[str] = []
    summaries: list[str] = []

    for key in shard_keys:
        path, label = SHARDS[key]
        mod_filter = "bulk" if key == "rnaseq_bulk" else None
        hits = search_shard(path, terms, modality_filter=mod_filter)
        if hits:
            all_lines.extend(hits[:150])
            summaries.append(f"{label}: {len(hits)} match{'es' if len(hits) != 1 else ''}")

    # Fallback: if nothing found, retry with the single longest specific term
    if not all_lines and terms:
        fallback = [max(terms, key=len)]
        for key in shard_keys:
            path, label = SHARDS[key]
            mod_filter = "bulk" if key == "rnaseq_bulk" else None
            hits = search_shard(path, fallback, modality_filter=mod_filter)
            if hits:
                all_lines.extend(hits[:100])
                summaries.append(f"{label} (broad): {len(hits)} matches")

    return all_lines[:300], summaries


# ---------------------------------------------------------------------------
# LLM step
# ---------------------------------------------------------------------------

def build_user_message(query: str, candidates: list[str], summaries: list[str]) -> str:
    if not candidates:
        return (
            f'The user searched for: "{query}"\n\n'
            "No matching records were found in the GEO index. "
            "Please tell them this, suggest alternative search terms, "
            "and note that broader or differently-worded queries may help."
        )

    candidate_block = "\n".join(candidates)
    search_note = ", ".join(summaries) if summaries else "unknown shards"

    return f"""The user is searching the GEO Multi-omics index for: "{query}"

Index format: {INDEX_FORMAT}

Search results ({search_note}):
{candidate_block}

Please identify the most relevant datasets for the user's query and present them clearly."""


def answer_query(query: str, history: list[dict]) -> tuple[list[dict], str]:
    """Gradio handler: run search + LLM, return updated chat history."""
    if not query.strip():
        return history, ""

    candidates, summaries = run_search(query)
    user_msg = build_user_message(query, candidates, summaries)

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
    )

    answer = response.content[0].text

    if summaries:
        answer = f"*Searched: {', '.join(summaries)}*\n\n{answer}"

    history.append({"role": "user", "content": query})
    history.append({"role": "assistant", "content": answer})
    return history, ""


# ---------------------------------------------------------------------------
# Gradio UI
# ---------------------------------------------------------------------------

import gradio as gr

DESCRIPTION = """
## GEO Multi-omics Dataset Search

Search 170,000+ genomics datasets from [GEO](https://www.ncbi.nlm.nih.gov/geo/) using plain English.
Covers RNA-seq (bulk, single-cell, snRNA-seq, spatial), ChIP-seq, ATAC-seq, CUT&RUN/Tag, methylation, and multiomics — 2015 through early 2026.

**Example queries:**
- *Find single-cell RNA-seq from APP/PS1 mice, and a matched-size dataset from 5XFAD mice*
- *Mouse kidney development bulk RNA-seq with processed count matrices*
- *Human PBMC CITE-seq datasets with H5 or RDS files, at least 10 samples*
- *Arabidopsis drought stress RNA-seq*

Powered by the [GEO Multi-omics Wiki](https://github.com/bendevlin18/GEO_llm) · Results link to NCBI GEO.
"""

with gr.Blocks(title="GEO Multi-omics Search", theme=gr.themes.Soft()) as demo:
    gr.Markdown(DESCRIPTION)

    chatbot = gr.Chatbot(
        label="Results",
        height=540,
        show_copy_button=True,
        render_markdown=True,
        type="messages",
    )

    with gr.Row():
        query_box = gr.Textbox(
            placeholder="Describe the datasets you're looking for…",
            label="Query",
            scale=5,
            autofocus=True,
        )
        submit_btn = gr.Button("Search", variant="primary", scale=1)

    gr.Examples(
        examples=[
            "Single-cell RNA-seq from APP/PS1 mice, and a similar-sized dataset from 5XFAD mice",
            "Mouse kidney development bulk RNA-seq with processed count matrices",
            "Human PBMC CITE-seq with at least 10 samples and H5 or RDS files",
            "snRNA-seq from human Alzheimer's disease brain, preferably with processed data",
            "Arabidopsis thaliana drought stress bulk RNA-seq",
            "Mouse H3K27ac ChIP-seq in microglia",
            "WGBS methylation data from human cancer cell lines",
        ],
        inputs=query_box,
    )

    state = gr.State([])

    submit_btn.click(
        fn=answer_query,
        inputs=[query_box, state],
        outputs=[state, query_box],
    ).then(
        fn=lambda h: h,
        inputs=state,
        outputs=chatbot,
    )

    query_box.submit(
        fn=answer_query,
        inputs=[query_box, state],
        outputs=[state, query_box],
    ).then(
        fn=lambda h: h,
        inputs=state,
        outputs=chatbot,
    )

if __name__ == "__main__":
    demo.launch()
