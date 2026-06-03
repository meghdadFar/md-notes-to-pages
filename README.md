# MD NOTES TO PAGES

Write notes in Markdown, get a published HTML site. You only need to edit `.md`. Allow access to this repo to any AI. On every push to `main`, the notes are rendered and deployed to GitHub Pages automatically.

I created this repo to keep Markdown as the source of truth and treat the website as a generated artifact. If you want the reasoning behind that, the first notebook ([`notebooks/01-why-markdown.md`](notebooks/01-why-markdown.md)) makes the case. Mostly that editing Markdown is faster, cheaper in tokens, and easier for both me and any AI working in the repo. It became an optimized setup to let multiple AI work on notes collaboratively with me.

## How It Works

`scripts/build_site.py` finds every `*.md` file in `notebooks/`, sorted by filename, and renders each one to HTML.

- The first notebook becomes `index.html`. The rest keep their name (`02-your-first-note.md` -> `02-your-first-note.html`).
- The first `# Heading` becomes the page title and sidebar label.
- The first line after it becomes the page description.
- Each `## Heading` becomes a table-of-contents entry.

To reorder pages, rename the files. Numeric prefixes (`01-`, `02-`, ...) work well.

## Requirements

- **Python 3.9 or newer** — runs the build script. (CI uses 3.12.)
- **Git** — for version control and pushing to GitHub.
- **A GitHub account** — only needed to publish. Local builds work without one.
- Python dependencies are pinned in [`requirements.txt`](requirements.txt) (`markdown`, `Pygments`).

## Quick Start

Build and preview locally before publishing anything.

```bash
# 1. Create an isolated environment and install dependencies
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt

# 2. Render notebooks/*.md into _site/
.venv/bin/python scripts/build_site.py

# 3. Serve the result and open http://localhost:8000
python3 -m http.server 8000 -d _site
```

Rerun step 2 whenever you change a note. `_site/` is generated and Git-ignored, so you never commit it.

## Add a Note

Drop a new Markdown file in `notebooks/` and rebuild — the sidebar and pages update on their own. Use a numeric prefix to control ordering.

```markdown
# My Topic

A one-sentence description for the page.

## First Section

Write here.
```

## Publish to GitHub Pages

Publishing is a one-time setup. After it's wired up, every push to `main` redeploys the site automatically.

### 1. Push the repo to GitHub

Create a new repository on GitHub (empty, no README), then from this folder:

```bash
git init                 # skip if the repo is already initialized
git add .
git commit -m "Initial notebooks"
git branch -M main
git remote add origin git@github.com:<your-username>/<your-repo>.git
git push -u origin main
```

### 2. Activate Pages

This is the step most people miss.

1. On GitHub, open **Settings → Pages**.
2. Under **Build and deployment**, set **Source → GitHub Actions**.

> ⚠️ Do **not** choose "Deploy from a branch." That mode runs GitHub's default Jekyll build, which publishes your `README.md` as the homepage and ignores this project's workflow — so you'd see only the README, not your notebooks.

### 3. Let the workflow run

The push from step 1 triggers the **Deploy GitHub Pages** workflow ([`.github/workflows/pages.yml`](.github/workflows/pages.yml)). Open the **Actions** tab and wait for the run to go green. It installs dependencies, runs `scripts/build_site.py`, and deploys `_site/`.

Your site is then live at:

```text
https://<your-username>.github.io/<your-repo>/
```

The URL also appears in **Settings → Pages** and on the workflow's `deploy` job. From now on, just push to `main` to publish updates (or trigger the workflow manually from the Actions tab).

## Add AI Collaborators

Because the source is plain Markdown, you can let AI coding agents read and write notes directly. They work in the repo on your machine, edit only `.md` files, and you commit and push to publish — no one touches HTML.

**Set the ground rules once.** Add a short `AGENTS.md` (and/or `CLAUDE.md`) at the repo root so every agent follows the same conventions:

```markdown
# Working in this repo

- Only edit Markdown files under `notebooks/`. Never edit HTML or `_site/`.
- Start each note with a single `# Title`, then a one-line description, then `##` sections.
- After changes, run `.venv/bin/python scripts/build_site.py` to verify the build succeeds.
- Commit one note per change with a clear message.
```

**Give an agent access to the folder.** Each of the major CLI agents runs inside a working directory and picks up the files there. Install the one you use, `cd` into this repo, and launch it:

| Tool | Install | Launch in the repo |
| --- | --- | --- |
| **Claude** (Claude Code) | `npm install -g @anthropic-ai/claude-code` | `claude` |
| **Gemini** (Gemini CLI) | `npm install -g @google/gemini-cli` | `gemini` |
| **ChatGPT** (Codex CLI) | `npm install -g @openai/codex` | `codex` |

Then prompt it normally — e.g. *"Add a notebook summarizing X"* or *"Tighten the headings in `03-another-example.md`."* The agent edits Markdown, you review the diff, commit, and push. Check each tool's docs for the current install command and how it asks for file-write permission.

**Prefer pull requests?** Connect the GitHub repo through the tool's GitHub integration (the Claude or ChatGPT GitHub app) and have the agent open PRs against `main` instead of editing your local files. Merging a PR runs the same deploy workflow.

## Customize

- Page shell — [`site/templates/page.html`](site/templates/page.html)
- Visual design — [`site/assets/styles.css`](site/assets/styles.css)
- Discovery and rendering — [`scripts/build_site.py`](scripts/build_site.py)
