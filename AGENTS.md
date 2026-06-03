# AGENTS.md — Guidelines for AI Collaborators

This repository publishes a folder of Markdown notes as an HTML website. If you are an AI agent working here, follow these conventions.

## What you may edit freely

- **Markdown (`.md`) files in `notebooks/`** — this is the source of truth. Add new notes, edit existing ones, and reorder them. No need to ask.
- Ordering comes from the filename. Use numeric prefixes (`01-`, `02-`, ...) and rename files to reorder pages.

## Edit only when explicitly asked

These shape the site itself rather than its content. Change them only when the user specifically requests it — then keep the change minimal, and rebuild afterward to confirm the notebook → HTML pipeline still works:

- `site/templates/` — the page shell (the HTML wrapped around each note).
- `site/assets/styles.css` — the visual design.
- `scripts/build_site.py` — how notes are discovered and rendered.
- `.github/workflows/pages.yml` — the build-and-deploy (GitHub Pages) workflow.
- `requirements.txt` — Python dependencies.

## Never edit

- **The generated HTML or anything in `_site/`.** It is produced by the build and overwritten on every run, so changes there are pointless and will be lost.

## Note format

- Start each note with a single `# Title` — it becomes the page title and the sidebar label.
- Follow the title with a one-line description.
- Use `## Headings` for sections; they become the table-of-contents entries.

## Before you finish

- Run `python scripts/build_site.py` (or `.venv/bin/python scripts/build_site.py`) and confirm the build succeeds.
- Commit one note per change with a clear message.

## Updating these guidelines

You may edit this file when the conventions actually change — a new folder, a new note format, a new build command — but keep it short and concrete. [`CLAUDE.md`](CLAUDE.md) points here, so this file is the single source; no need to duplicate the rules elsewhere.
