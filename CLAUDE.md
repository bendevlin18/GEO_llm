# CLAUDE.md

See [AGENTS.md](AGENTS.md) for full project context.

## Claude Code specifics

- Run all scripts with: `conda run -n GEO_llm python scripts/<script>.py`
- Workflow prompts are in `prompts/` — invoke with `/search`, `/rebuild`, `/fetch`, `/release`
- Allowed: `Bash(conda run:*)`, `Bash(export NCBI_EMAIL=*)`
