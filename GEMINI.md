# GEMINI.md

See [AGENTS.md](AGENTS.md) for full project context.

## Gemini CLI specifics

- Run all scripts with: `conda run -n GEO_llm python scripts/<script>.py`
- Workflow prompts are in `prompts/` — include them with `@prompts/<name>.md`
  - Dataset search: `@prompts/search.md <your query>`
  - Full rebuild: `@prompts/rebuild.md`
  - Fetch new data: `@prompts/fetch.md <date range>`
  - Publish release: `@prompts/release.md`
