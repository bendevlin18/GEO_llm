# Publish Data Release

Publish a new data release to GitHub Releases.

## Steps

1. **Verify prerequisites** — confirm these files exist and are non-empty:
   - `rnaseq_classified.json`, `chipseq_classified.json`, `methylation_classified.json`, `multiomics_classified.json`, `ftp_index.json`
   - Report record counts for each.

2. **Show existing tags**: `git tag -l "data-v*" | sort -V | tail -5`

3. **Determine the tag** — if not provided, suggest the next version:
   - MAJOR — schema-breaking changes (new/removed fields, format changes)
   - MINOR — new data coverage (more date ranges, more records)
   - PATCH — re-run with fixes, same coverage
   - Confirm with the user before proceeding.

4. **Draft release notes**: coverage date range (from `data/` filenames), record counts per assay, FTP index status, notable changes since last release.

5. **Get the GitHub token** — ask the user if `GITHUB_TOKEN` is not set. This step uploads ~30 MB publicly.

6. **Run**:
   ```bash
   GITHUB_TOKEN=<token> conda run -n GEO_llm python scripts/create_data_release.py \
     --tag <tag> \
     --notes "<notes>"
   ```

7. **Report** the release URL.

## Version scheme

`data-vMAJOR.MINOR.PATCH` — current: `data-v1.0.0`
