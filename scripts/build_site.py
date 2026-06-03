#!/usr/bin/env python3
from __future__ import annotations

import html
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

import markdown
from markdown.extensions.toc import TocExtension


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"
OUTPUT_DIR = ROOT / "_site"
ASSET_DIR = ROOT / "site" / "assets"
TEMPLATE_PATH = ROOT / "site" / "templates" / "page.html"


@dataclass(frozen=True)
class Page:
    source: Path
    output_name: str
    nav_title: str
    description: str


def page_title(markdown_text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", markdown_text, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def page_description(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return stripped
    return fallback


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "notebook"


def discover_pages() -> list[Page]:
    markdown_files = sorted(NOTEBOOK_DIR.glob("*.md"))
    if not markdown_files:
        raise FileNotFoundError(
            f"No Markdown notebooks found in {NOTEBOOK_DIR.relative_to(ROOT)}"
        )

    pages = []
    used_outputs = set()
    for index, source in enumerate(markdown_files):
        markdown_text = source.read_text(encoding="utf-8")
        fallback_title = source.stem.replace("-", " ").replace("_", " ").title()
        title = page_title(markdown_text, fallback_title)
        output_name = "index.html" if index == 0 else f"{slugify(source.stem)}.html"

        counter = 2
        unique_output_name = output_name
        while unique_output_name in used_outputs:
            unique_output_name = f"{Path(output_name).stem}-{counter}.html"
            counter += 1

        used_outputs.add(unique_output_name)
        pages.append(
            Page(
                source=source,
                output_name=unique_output_name,
                nav_title=title,
                description=page_description(markdown_text, f"{title} notebook."),
            )
        )

    return pages


def render_markdown(markdown_text: str) -> tuple[str, str]:
    renderer = markdown.Markdown(
        extensions=[
            "extra",
            "sane_lists",
            "codehilite",
            TocExtension(permalink="", toc_depth="2-3"),
        ],
        extension_configs={
            "codehilite": {
                "guess_lang": False,
                "noclasses": True,
            }
        },
        output_format="html5",
    )
    body = renderer.convert(markdown_text)
    toc = renderer.toc
    return body, toc


def render_nav(pages: list[Page], current_output: str) -> str:
    links = []
    for page in pages:
        active = ' aria-current="page"' if page.output_name == current_output else ""
        links.append(
            f'<a href="{page.output_name}"{active}>{html.escape(page.nav_title)}</a>'
        )
    return "\n".join(links)


def build_page(template: str, pages: list[Page], page: Page) -> str:
    markdown_text = page.source.read_text(encoding="utf-8")
    title = page_title(markdown_text, page.nav_title)
    content, toc = render_markdown(markdown_text)
    return (
        template.replace("{{ title }}", html.escape(title))
        .replace("{{ description }}", html.escape(page.description))
        .replace("{{ nav }}", render_nav(pages, page.output_name))
        .replace("{{ toc }}", toc)
        .replace("{{ content }}", content)
    )


def copy_assets() -> None:
    target = OUTPUT_DIR / "assets"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(ASSET_DIR, target)


def main() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(exist_ok=True)
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    pages = discover_pages()

    for page in pages:
        output = build_page(template, pages, page)
        (OUTPUT_DIR / page.output_name).write_text(output, encoding="utf-8")

    copy_assets()
    (OUTPUT_DIR / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(pages)} notebook page(s) from {NOTEBOOK_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
