# md-notes-to-pages

A small template for publishing a folder of Markdown notebooks as a clean GitHub Pages site.

Write notes in `notebooks/`. Run one script. Get a static HTML site in `_site/`.

```text
notebooks/*.md -> Python render script -> _site/ HTML -> GitHub Pages
```

## Why

Markdown is pleasant to write, easy to diff, and friendly to AI-assisted editing.

HTML is better for reading, navigation, styling, and sharing.

This repo keeps Markdown as the source of truth and treats the website as a generated artifact.

## Project Shape

```text
.
├── notebooks/
│   ├── 01-field-guide.md
│   ├── 02-lab-notes.md
│   └── 03-reading-room.md
├── scripts/
│   └── build_site.py
├── site/
│   ├── assets/
│   │   └── styles.css
│   └── templates/
│       └── page.html
├── .github/
│   └── workflows/
│       └── pages.yml
├── requirements.txt
└── _site/
```

## How It Works

`scripts/build_site.py` automatically finds every `*.md` file in `notebooks/`, sorted by filename.

- The first notebook becomes `index.html`.
- Every other notebook becomes a page named from its filename, such as `02-lab-notes.md` -> `02-lab-notes.html`.
- The first `# Heading` in each file becomes the page title and sidebar label.
- The first non-heading line becomes the page description.
- Second-level headings become the table of contents.

To reorder pages, rename the Markdown files. Numeric prefixes like `01-`, `02-`, and `03-` work well.

## Quick Start

Install dependencies:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Build the site:

```bash
.venv/bin/python scripts/build_site.py
```

Preview locally:

```bash
python3 -m http.server 8000 -d _site
```

Open:

```text
http://localhost:8000
```

## Add a Notebook

Create a new Markdown file in `notebooks/`:

```text
notebooks/04-my-topic.md
```

Start it with a title:

```markdown
# My Topic

A one-sentence description for the page metadata.

## First Section

Write here.
```

Run the build again. The sidebar and page output update automatically.

## Customize

- Change the site shell in `site/templates/page.html`.
- Change the visual design in `site/assets/styles.css`.
- Change notebook discovery or rendering behavior in `scripts/build_site.py`.
- Replace the sample notebooks with your own notes.

## Publish With GitHub Pages

1. Push the repo to GitHub.
2. Open `Settings -> Pages`.
3. Set `Build and deployment -> Source -> GitHub Actions`.
4. Push to `main`.

The workflow installs dependencies, runs `scripts/build_site.py`, uploads `_site/`, and deploys it to GitHub Pages.

## Notes

- `_site/` is generated and ignored by Git.
- Add pages by adding Markdown files to `notebooks/`.
- The GitHub Actions workflow runs on pushes to `main` and manual runs.
