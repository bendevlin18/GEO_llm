"""
Build a compact, grep-friendly search index from classified datasets.
Combines RNA-seq, ChIP-seq, methylation, and multiomics classified records.
Incorporates FTP file listings when available.

One line per dataset:
  accession|modality|organism|n_samples|files_summary|topics|title|keywords|flags

files_summary format: "filename1(size),filename2(size)" from actual FTP listing,
or falls back to GEO's archive_contents field if FTP data unavailable.

flags (9th field): "multiomics" if accession also appears in multiomics_classified.json;
empty string otherwise.
"""
import json
import os
import re
from collections import Counter

with open("rnaseq_classified.json") as f:
    data = json.load(f)

# Include ChIP-seq / ATAC-seq classified records if available
if os.path.exists("chipseq_classified.json"):
    with open("chipseq_classified.json") as f:
        chipseq_data = json.load(f)
    rna_accessions = {r["accession"] for r in data}
    new_records = [r for r in chipseq_data if r["accession"] not in rna_accessions]
    data = data + new_records
    print(f"Loaded ChIP-seq index: {len(chipseq_data)} entries ({len(new_records)} unique to ChIP-seq)")
else:
    print("No chipseq_classified.json found, building RNA-seq only index")

# Include methylation classified records if available
if os.path.exists("methylation_classified.json"):
    with open("methylation_classified.json") as f:
        meth_data = json.load(f)
    existing_accessions = {r["accession"] for r in data}
    new_records = [r for r in meth_data if r["accession"] not in existing_accessions]
    data = data + new_records
    print(f"Loaded methylation index: {len(meth_data)} entries ({len(new_records)} unique to methylation)")
else:
    print("No methylation_classified.json found, skipping methylation records")

# Load multiomics classified records — used for the multiomics shard and flags
multiomics_data = []
multiomics_accessions: set[str] = set()
if os.path.exists("multiomics_classified.json"):
    with open("multiomics_classified.json") as f:
        multiomics_data = json.load(f)
    multiomics_accessions = {r["accession"] for r in multiomics_data}
    print(f"Loaded multiomics index: {len(multiomics_data)} entries")
else:
    print("No multiomics_classified.json found, skipping multiomics shard and flags")

# Load FTP index if available
ftp_index = {}
if os.path.exists("ftp_index.json"):
    with open("ftp_index.json") as f:
        ftp_index = json.load(f)
    print(f"Loaded FTP index: {len(ftp_index)} entries")
else:
    print("No FTP index found, using GEO suppFile field only")


def format_size(size_bytes):
    """Compact human-readable size."""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes/1024:.0f}KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes/(1024*1024):.0f}MB"
    else:
        return f"{size_bytes/(1024*1024*1024):.1f}GB"


def files_summary(accession, suppfile_fallback):
    """Build a compact files summary string from FTP data or fallback."""
    if accession in ftp_index:
        ftp = ftp_index[accession]
        files = ftp.get("files", [])
        if not files:
            return "no_suppl"
        parts = []
        for f in files:
            name = f["name"]
            if name == "filelist.txt":
                continue
            parts.append(f"{name}({format_size(f['size'])})")
        return ", ".join(parts) if parts else "no_suppl"
    else:
        return f"[GEO:{suppfile_fallback}]" if suppfile_fallback else "unknown"


def compress_summary(title, summary, max_len=200):
    """Extract key terms from title+summary, deduplicating against title."""
    title_lower = title.lower()
    stop = {
        "the", "a", "an", "and", "or", "of", "in", "to", "for", "by", "with",
        "from", "on", "at", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "shall", "can", "that", "this", "these",
        "those", "it", "its", "we", "our", "they", "their", "here", "there",
        "how", "what", "which", "who", "whom", "when", "where", "why",
        "also", "than", "then", "not", "but", "yet", "so", "if", "as",
        "into", "through", "during", "before", "after", "above", "below",
        "between", "both", "each", "all", "any", "some", "such", "no",
        "nor", "only", "own", "same", "very", "just", "about", "up",
        "out", "upon", "using", "used", "based", "however", "whether",
        "show", "showed", "shown", "found", "find", "study", "studies",
        "result", "results", "data", "analysis", "performed", "identified",
        "revealed", "demonstrate", "investigated", "examined", "suggest",
        "suggests", "provide", "provides", "compared", "associated",
        "respectively", "significant", "significantly", "observed",
        "including", "involved", "known", "well", "thus", "moreover",
        "furthermore", "although", "whereas", "therefore", "underlying",
        "remains", "remain", "unclear", "role", "roles", "function",
        "functions", "mechanism", "mechanisms",
    }

    words = re.findall(r'[A-Za-z0-9][\w\-/]*[A-Za-z0-9]|[A-Za-z0-9]', summary)
    terms = []
    seen = set()
    for w in words:
        wl = w.lower()
        if wl in stop or len(wl) < 3:
            continue
        if wl in title_lower:
            continue
        if wl in seen:
            continue
        seen.add(wl)
        terms.append(w)

    result = " ".join(terms)
    if len(result) > max_len:
        result = result[:max_len].rsplit(" ", 1)[0]
    return result


def make_line(r: dict) -> str:
    """Build a pipe-delimited search index line for a record."""
    topics = ",".join(r.get("topics", []))
    keywords = compress_summary(r.get("title", ""), r.get("summary", ""))
    fs = files_summary(r["accession"], r.get("suppfile", ""))
    flags = "multiomics" if r["accession"] in multiomics_accessions else ""
    return "|".join([
        r["accession"],
        r.get("modality", ""),
        r.get("organism", ""),
        str(r.get("n_samples", "")),
        fs,
        topics,
        r.get("title", ""),
        keywords,
        flags,
    ])


# Shard routing: which modality values belong to each per-assay index file
SHARD_MAP = {
    "search_index_rnaseq.txt":        {"bulk", "single-cell", "single-nucleus", "spatial"},
    "search_index_chipseq.txt":       {"chip_seq", "chip_exo"},
    "search_index_atacseq.txt":       {"atac_seq"},
    "search_index_cut_run_tag.txt":   {"cut_and_run", "cut_and_tag"},
    "search_index_methylation.txt":   {
        "wgbs", "rrbs", "em_seq", "oxbs_seq", "hmc_seq",
        "medip_seq", "methylation_array", "other_methylation",
    },
    "search_index_multiomics.txt":    {
        "cite_seq", "multiome", "spatial_multiomics", "other_multiomics",
    },
}
# Build reverse lookup: modality -> shard filename
MODALITY_TO_SHARD = {}
for shard_file, modalities in SHARD_MAP.items():
    for m in modalities:
        MODALITY_TO_SHARD[m] = shard_file

HEADER = (
    "# accession|modality|organism|n_samples|files|topics|title|keywords|flags\n"
    "# files: actual FTP filenames+sizes when available, or [GEO:types] as fallback\n"
    "# flags: 'multiomics' if record also appears in search_index_multiomics.txt; empty otherwise\n"
)

lines = []
ftp_hits = 0
shard_lines: dict[str, list[str]] = {f: [] for f in SHARD_MAP}
unrouted = []

# Main loop: rnaseq + chipseq + methylation records
for r in data:
    if r["accession"] in ftp_index:
        ftp_hits += 1
    line = make_line(r)
    lines.append(line)
    shard = MODALITY_TO_SHARD.get(r.get("modality", ""))
    if shard:
        shard_lines[shard].append(line)
    else:
        unrouted.append(line)

# Multiomics shard: built from multiomics_classified.json directly
for r in multiomics_data:
    line = make_line(r)
    shard_lines["search_index_multiomics.txt"].append(line)
    lines.append(line)

# Write combined index (gitignored — reconstructable from shards)
combined_path = "wiki/search_index.txt"
with open(combined_path, "w") as f:
    f.write(HEADER)
    for line in lines:
        f.write(line + "\n")

size_kb = os.path.getsize(combined_path) / 1024
print(f"Wrote {len(lines)} records to {combined_path} ({size_kb:.0f} KB)")
print(f"FTP data available for {ftp_hits}/{len(data)} non-multiomics records ({100*ftp_hits/len(data):.0f}%)")

# Write per-assay shard files (checked into git — each is well under 50 MB)
print("\nPer-assay shard files:")
for shard_file, shard in shard_lines.items():
    path = f"wiki/{shard_file}"
    with open(path, "w") as f:
        f.write(HEADER)
        for line in shard:
            f.write(line + "\n")
    size_kb = os.path.getsize(path) / 1024
    print(f"  {path}: {len(shard)} records ({size_kb:.0f} KB)")

if unrouted:
    print(f"\nWarning: {len(unrouted)} records with unrecognized modality not written to any shard")
    modalities = Counter(line.split("|")[1] for line in unrouted)
    for m, n in modalities.most_common():
        print(f"  {m}: {n}")

# Show some example lines
print("\nExample lines (rnaseq, multiomics-flagged, multiomics):")
flagged = [l for l in lines if l.split("|")[-1] == "multiomics" and "bulk" in l.split("|")[1]]
if flagged:
    print(f"  {flagged[0][:200]}...")
multi_examples = shard_lines["search_index_multiomics.txt"][:2]
for ex in multi_examples:
    print(f"  {ex[:200]}...")
