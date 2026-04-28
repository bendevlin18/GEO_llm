# GEO Wiki Query Benchmark: Claude Code vs. Gemini CLI

## Setup

Both tools run from the repo root with full access to the file structure. Claude Code reads `CLAUDE.md` as project instructions; Gemini CLI reads `GEMINI.md` (mirror of `CLAUDE.md`). Queries are issued cold — no preamble or hints about the index format.

## Evaluation Criteria (score each 1–3)

| Criterion | 1 — Poor | 2 — OK | 3 — Good |
|---|---|---|---|
| **Accuracy** | Returns wrong datasets | Mostly right, some errors | All returned datasets match query |
| **Completeness** | Misses obvious results | Finds most relevant | Finds all clearly relevant results |
| **Constraint adherence** | Ignores filters (n_samples, file type) | Partially applies | Correctly applies all constraints |
| **Domain interpretation** | Misses domain terms | Partially understands | Correctly resolves domain knowledge |
| **Explanation quality** | No justification | Brief justification | Clear reasoning per result |
| **Hallucination** | Invents accessions or details | Minor inaccuracies | No fabrication |
| **Tool efficiency** | Wrong shard or redundant calls | Minor inefficiency | Picks right shard, minimal calls |

---

## Queries

### Tier 1 — Simple

**Q1:** `Find zebrafish spatial transcriptomics datasets`
- Shard: `wiki/search_index_rnaseq.txt`
- Tests: basic organism + modality match on large shard
- Verifiable: yes — grep for `Danio rerio` + `spatial`

**Q2:** `How many CITE-seq datasets profile human PBMCs?`
- Shard: `wiki/search_index_multiomics.txt`
- Tests: counting task on small shard
- Verifiable: yes — grep for `cite_seq` + `Homo sapiens` + `PBMC`

---

### Tier 2 — Multi-constraint

**Q3:** `Mouse kidney snRNA-seq with at least 5 samples and H5 files available`
- Shard: `wiki/search_index_rnaseq.txt`
- Tests: three simultaneous constraints (organism, modality, file type, sample count)
- Verifiable: yes

**Q4:** `Human bulk RNA-seq cancer datasets with processed count matrices (CSV or TSV files)`
- Shard: `wiki/search_index_rnaseq.txt`
- Tests: file format filter on large shard
- Verifiable: yes

**Q5:** `H3K27ac ChIP-seq datasets in mouse embryonic stem cells`
- Shard: `wiki/search_index_chipseq.txt`
- Tests: histone mark recognition (domain term in keywords/title)
- Verifiable: yes

---

### Tier 3 — Domain knowledge

**Q6:** `Find single-cell RNA-seq from APP/PS1 or 5XFAD mice`
- Shard: `wiki/search_index_rnaseq.txt`
- Tests: Alzheimer's mouse model names — these appear in titles, not as organism field values
- Watch for: hallucination if the model "knows" these models but can't find them in the index

**Q7:** `Find datasets from the Tabula Muris project`
- Shard: `wiki/search_index_rnaseq.txt`
- Tests: landmark atlas recognition — should search for "Tabula Muris" in title/keywords
- Watch for: confidently wrong results or fabricated accessions

---

### Tier 4 — Comparison and reasoning

**Q8:** `Find two comparable snRNA-seq datasets of human kidney that I could use to replicate an analysis — similar sample counts preferred`
- Shard: `wiki/search_index_rnaseq.txt`
- Tests: evaluate and rank multiple results, not just list them
- Watch for: whether it compares n_samples across candidates

**Q9:** `I want to study chromatin accessibility in mouse brain development — what datasets are available?`
- Shards: `wiki/search_index_rnaseq.txt`, `wiki/search_index_atacseq.txt`
- Tests: does the tool search multiple shards without being told to? ("chromatin accessibility" = ATAC-seq, not mentioned explicitly)
- Watch for: whether it stays in one shard or crosses to ATAC-seq

---

### Tier 5 — Open-ended

**Q10:** `I'm studying liver fibrosis — what's the best dataset to start with?`
- Shards: multiple (RNA-seq, ChIP-seq, ATAC-seq all relevant)
- Tests: judgment — file format ease, sample count, modality, cross-assay awareness
- No single right answer; score on reasoning quality

---

## Results

| Query | Claude Code Score | Gemini CLI Score | Notes |
|---|---|---|---|
| Q1 | | | |
| Q2 | | | |
| Q3 | | | |
| Q4 | | | |
| Q5 | | | |
| Q6 | | | |
| Q7 | | | |
| Q8 | | | |
| Q9 | | | |
| Q10 | | | |

## Observations

_Fill in after running._
