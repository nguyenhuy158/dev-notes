# Repository Guidelines

## Project Structure & Module Organization

dev-notes is a flat collection of Markdown notes (mostly Vietnamese) to consult
when starting a new project: chosen libraries, shared conventions and short
guides, so the same decisions are not re-made from scratch. There is no app,
no build and no package manager setup.

Folder structure:

```text
README.md                   # Index: one line per note, linked
conventions.md              # Shared conventions (pnpm only, hexagonal layout, ...)
claude-md-guide.md          # How to write CLAUDE.md / agent instructions
claudeignore.md             # .claudeignore convention + Cloudflare Worker example
context-indexing-rag.md     # Context indexing / RAG levels for codebases
avatar-libs.md  cmdk.md  date-fns.md  fonts.md  toast-libs.md  zod.md  zustand.md
                            # Library picks, one topic per file
rag-scripts/                # Illustrative Python for context-indexing-rag.md (level 1)
  index_builder.py          #   Build a naive semantic index (sentence-transformers)
  usage_example.py          #   Query the index
```

## Build, Test, and Development Commands

None. Notes are plain Markdown. `rag-scripts/` are illustrations, not a
maintained tool: they reference helpers you must write yourself; install deps
with `uv add sentence-transformers faiss-cpu` if you run them.

## Coding Style & Naming Conventions

One topic per file, kebab-case file names such as `toast-libs.md`. Start each
note with a single `#` heading, keep sections short, and prefer a concrete
recommendation plus a minimal example over a survey. When adding a note, add a
matching line to the index in `README.md`. Keep the existing language of a note
(Vietnamese unless it already is English).

## Testing Guidelines

No tests. Check that links in `README.md` resolve and code blocks are fenced
with a language where it helps.

## Commit & Pull Request Guidelines

Use concise Conventional Commits, for example `docs: add zod note` or
`docs: update pnpm convention`. Pull requests should include a short summary of
which notes changed and why.

## Ecosystem

See the [huyab.click ecosystem map](https://github.com/nguyenhuy158/kit/blob/main/docs/ECOSYSTEM.md) for how all personal repos connect.

- Kit packages: none (Markdown only). Conventions noted here that became shared
  code live in kit: `@huyab/config` (Biome/TS), `@huyab/sso`, `@huyab/e2e`, and the
  reusable `check.yml` workflow.
- Talks to: no repo at runtime.

## Agent-Specific Instructions

Keep responses short and focused. If a requirement is unclear, ask before making
assumptions.
When a note states a convention (for example "pnpm only" in `conventions.md`),
treat it as the source for other personal repos and keep it consistent with
their `AGENTS.md` files.
