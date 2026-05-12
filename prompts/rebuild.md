# Full Pipeline Rebuild

Run all steps in order. Each step depends on the previous. All commands use `conda run -n GEO_llm python scripts/<script>.py`.

## Steps

**1. Classify all assay types** (each reads `data/*.json`, writes `*_classified.json`):
```bash
conda run -n GEO_llm python scripts/extract_rnaseq.py
conda run -n GEO_llm python scripts/extract_chipseq.py
conda run -n GEO_llm python scripts/extract_methylation.py
conda run -n GEO_llm python scripts/extract_multiomics.py   # also back-annotates rnaseq + chipseq
```
Report record counts after each step.

**2. FTP indexing** (slow — ~18 hours for a full run; saves incrementally every 100 records):
```bash
conda run -n GEO_llm python scripts/index_ftp.py
```
Ask the user if they want to skip this step if `ftp_index.json` is already current. Safe to interrupt and resume.

**3. Build search index shards**:
```bash
conda run -n GEO_llm python scripts/build_search_index.py
```

**4. Regenerate wiki pages**:
```bash
conda run -n GEO_llm python scripts/generate_wiki.py
```

**5. Regenerate README charts** (must run after step 1; reads `*_classified.json` directly):
```bash
conda run -n GEO_llm python scripts/generate_plots.py
```

**6. Commit**:
```bash
git add wiki/ assets/
git commit -m "Rebuild wiki and plots — <date>"
git push
```

## After completion

Report: RNA-seq, ChIP-seq, methylation, multiomics record counts; any steps skipped; reminder to push if not done.
