"""
Build a compact, grep-friendly search index from classified RNA-seq data.
Incorporates FTP file listings when available.

One line per dataset:
  accession|modality|organism|n_samples|files_summary|topics|title|keywords

files_summary format: "filename1(size),filename2(size)" from actual FTP listing,
or falls back to GEO's archive_contents field if FTP data unavailable.
"""
import json
import os
import re
from collections import Counter

with open("rnaseq_classified.json") as f:
    data = json.load(f)

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
        # Compact: filename(size) for each file, skip filelist.txt
        parts = []
        for f in files:
            name = f["name"]
            if name == "filelist.txt":
                continue
            parts.append(f"{name}({format_size(f['size'])})")
        return ", ".join(parts) if parts else "no_suppl"
    else:
        # Fallback to GEO's suppFile field
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


lines = []
ftp_hits = 0
for r in data:
    topics = ",".join(r.get("topics", []))
    keywords = compress_summary(r["title"], r["summary"])
    fs = files_summary(r["accession"], r["suppfile"])
    if r["accession"] in ftp_index:
        ftp_hits += 1

    line = "|".join([
        r["accession"],
        r["modality"],
        r["organism"],
        r["n_samples"],
        fs,
        topics,
        r["title"],
        keywords,
    ])
    lines.append(line)

# Write index
index_path = "wiki/search_index.txt"
with open(index_path, "w") as f:
    f.write("# accession|modality|organism|n_samples|files|topics|title|keywords\n")
    f.write("# files: actual FTP filenames+sizes when available, or [GEO:types] as fallback\n")
    for line in lines:
        f.write(line + "\n")

size_kb = os.path.getsize(index_path) / 1024
print(f"Wrote {len(lines)} records to {index_path} ({size_kb:.0f} KB)")
print(f"FTP data available for {ftp_hits}/{len(lines)} records ({100*ftp_hits/len(lines):.0f}%)")

# Show some example lines
print("\nExample lines:")
for line in lines[:3]:
    print(f"  {line[:250]}...")
