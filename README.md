# md-notes-to-pages

Write notes in Markdown, get a published HTML site. You only need to edit `.md`. On every push to `main`, the notes are rendered and deployed to GitHub Pages automatically.

I created this repo to keep Markdown as the source of truth and treat the website as a generated artifact. If you want the reasoning behind that, the first notebook ([`notebooks/01-why-markdown.md`](notebooks/01-why-markdown.md)) makes the case. Mostly that editing Markdown is faster, cheaper in tokens, and easier for both me and any AI working in the repo. It became an optimized setup to let multiple AI work on notes collaboratively with me.

## How It Works

`scripts/build_site.py` finds every `*.md` file in `notebooks/`, sorted by filename, and renders each one to HTML.

- The first notebook becomes `index.html`. The rest keep their name (`02-your-first-note.md` -> `02-your-first-note.html`).
- The first `# Heading` becomes the page title and sidebar label.
- The first line after it becomes the page description.
- Each `## Heading` becomes a table-of-contents entry.

To reorder pages, rename the files. Numeric prefixes (`01-`, `02-`, ...) work well.

## Quick Start

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build_site.py
```

Then preview at `http://localhost:8000`:

```bash
python3 -m http.server 8000 -d _site
```

## Add a Note

Drop a new Markdown file in `notebooks/` and build again — the sidebar and pages update on their own.

```markdown
# My Topic

A one-sentence description for the page.

## First Section

Write here.
```

## Publish

1. Push the repo to GitHub.
2. In `Settings -> Pages`, set `Source` to `GitHub Actions`.
3. Push to `main`.

The workflow installs dependencies, runs the build, and deploys `_site/` to Pages. It runs on every push to `main` (and manually).

## Customize

- Page shell — [`site/templates/page.html`](site/templates/page.html)
- Visual design — [`site/assets/styles.css`](site/assets/styles.css)
- Discovery and rendering — [`scripts/build_site.py`](scripts/build_site.py)

`_site/` is generated and ignored by Git.
