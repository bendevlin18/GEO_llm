"""
Parse per-query benchmark files and produce a combined benchmark.md summary.

Each query file: tool_testing/YYYY-MM-DD_QN.md
Output:          tool_testing/benchmark.md

Usage: conda run -n GEO_llm python scripts/analyze_benchmark.py [--dir tool_testing]
"""

import re
import sys
import argparse
from pathlib import Path
from datetime import date


def extract_accessions(text: str) -> set[str]:
    return set(re.findall(r'GSE\d+', text))


def parse_query_file(path: Path) -> dict | None:
    text = path.read_text()
    m = re.match(r'# (Q\d+) \((T\d+)\) — .+\n\*\*Query:\*\* (.+)', text)
    if not m:
        return None
    qid, tier, query = m.group(1), m.group(2), m.group(3).strip()

    app_m = re.search(r'## App pipeline\n(.+?)(?=\n## Agentic pipeline)', text, re.DOTALL)
    agt_m = re.search(r'## Agentic pipeline\n(.+)', text, re.DOTALL)

    app_acc = extract_accessions(app_m.group(1)) if app_m else set()
    agt_acc = extract_accessions(agt_m.group(1)) if agt_m else set()

    overlap  = app_acc & agt_acc
    app_only = app_acc - agt_acc
    agt_only = agt_acc - app_acc
    union    = app_acc | agt_acc
    jaccard  = len(overlap) / len(union) if union else 0.0

    return {
        "qid": qid,
        "tier": tier,
        "query": query,
        "file": path.name,
        "app": sorted(app_acc),
        "agentic": sorted(agt_acc),
        "overlap": sorted(overlap),
        "app_only": sorted(app_only),
        "agentic_only": sorted(agt_only),
        "jaccard": jaccard,
        "app_text": app_m.group(1).strip() if app_m else "",
        "agt_text": agt_m.group(1).strip() if agt_m else "",
    }


def build_summary(results: list[dict]) -> str:
    today = date.today().isoformat()
    lines = [
        f"# Benchmark Summary — {today}",
        "",
        "Scoring rubric (1–3 each): Accuracy · Completeness · Constraint adherence · "
        "Domain interpretation · Explanation quality · Hallucination · Tool efficiency",
        "",
        "## Overlap statistics",
        "",
        f"| Query | Tier | App | Agentic | Overlap | Jaccard | Query |",
        f"|---|---|---|---|---|---|---|",
    ]
    for r in results:
        lines.append(
            f"| {r['qid']} | {r['tier']} | {len(r['app'])} | {len(r['agentic'])} "
            f"| {len(r['overlap'])} | {r['jaccard']:.2f} | {r['query'][:55]} |"
        )

    lines += ["", "## Scoring", "", "| Query | App Score | Agentic Score | Notes |", "|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['qid']} | | | |")

    lines += ["", "---", ""]

    for r in results:
        n_ol = len(r["overlap"])
        n_app_only = len(r["app_only"])
        n_agt_only = len(r["agentic_only"])
        lines += [
            f"## {r['qid']} ({r['tier']})",
            f"**Query:** {r['query']}  ",
            f"**Source file:** `{r['file']}`",
            "",
            f"**Overlap ({n_ol}):** {', '.join(r['overlap']) or 'none'}  ",
            f"**App only ({n_app_only}):** {', '.join(r['app_only']) or 'none'}  ",
            f"**Agentic only ({n_agt_only}):** {', '.join(r['agentic_only']) or 'none'}",
            "",
            "### App pipeline",
            r["app_text"],
            "",
            "### Agentic pipeline",
            r["agt_text"],
            "",
            "---",
            "",
        ]

    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default="tool_testing")
    args = parser.parse_args()

    d = Path(args.dir)
    files = sorted(d.glob("????-??-??_Q*.md"))
    if not files:
        print(f"No per-query files found in {d}/")
        sys.exit(1)

    results = []
    for f in files:
        r = parse_query_file(f)
        if r:
            results.append(r)
        else:
            print(f"  skipped (parse failed): {f.name}")

    results.sort(key=lambda r: int(r["qid"][1:]))

    # Print console summary
    print(f"{'Query':<5} {'App':>4} {'Agt':>4} {'Overlap':>7} {'Jaccard':>7}  Query")
    print("-" * 80)
    for r in results:
        print(f"{r['qid']:<5} {len(r['app']):>4} {len(r['agentic']):>4} "
              f"{len(r['overlap']):>7} {r['jaccard']:>7.2f}  {r['query'][:60]}")

    out_path = d / "benchmark.md"
    out_path.write_text(build_summary(results))
    print(f"\nWrote {out_path}")
