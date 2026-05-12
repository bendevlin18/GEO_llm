# Fetch New GEO Metadata

Fetch a new date range of GEO metadata from the NCBI API.

## Steps

1. **Get the date range** from the user if not already provided. Accepted formats:
   - `YYYY/MM/DD to YYYY/MM/DD` — explicit range
   - `YYYY-QN` shorthand: Q1=01/01–03/31, Q2=04/01–06/30, Q3=07/01–09/30, Q4=10/01–12/31

2. **Determine the output filename** under `data/`:
   - Quarterly → `data/geo_metadata_YYYY-QN.json`
   - Custom → `data/geo_metadata_YYYY-MM-DD.json` (use end date)
   - Check `data/` for existing files covering this range; warn the user before overwriting.

3. **Run**:
   ```bash
   conda run -n GEO_llm python scripts/geo_metadata_fetcher.py \
     --email benjamin.devlin@duke.edu \
     --start-date <YYYY/MM/DD> \
     --end-date <YYYY/MM/DD> \
     -o data/<filename>
   ```

4. **Report** the record count from the script output.

5. **Ask** if the user wants to run the full rebuild pipeline now — if yes, follow `prompts/rebuild.md`.
