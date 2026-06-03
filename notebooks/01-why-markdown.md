# Why Markdown, Not HTML

Keep Markdown as the source of truth and treat the website as a generated artifact — here is why that small decision pays off, especially when you write with AI.

## The Idea

Loved Tariq's idea and took it further: keep `.md` as the source in a GitHub repo and auto-generate HTML on every push to `main`.

A small Python render script (a Markdown library + an HTML template + CSS) turns `notebooks/*.md` into `_site/`, and a GitHub Actions workflow deploys it to GitHub Pages on every commit.

You — or any AI with access to this repo — only ever edit Markdown. Nobody touches HTML.

## AI Edits Are Cheaper on Markdown

Editing HTML with AI was becoming difficult, time-consuming, and token-heavy. The same edits on `.md` are faster and far more efficient.

Depending on the size of the document, creating and editing the HTML can be 2x–4x the Markdown. For example, this:

```markdown
## Idea
- One useful point
- Another useful point
```

becomes this:

```html
<h2 id="idea">Idea<a class="headerlink" href="#idea" title="Permanent link"></a></h2>
<ul>
<li>One useful point</li>
<li>Another useful point</li>
</ul>
```

Generating a little is fine. But when you create a lot of content, that is a lot of tokens you do not need to spend.

## Manual Edits Stay Easy

I frequently edit notes by hand — moving paragraphs around and reordering headings. That is trivial in Markdown and painful in HTML, where the same change usually means prompting a model to do it for you. Something that should be a quick manual fix turns into a prompting spree.

## Any Model Can Contribute

Because the source is Markdown, Claude, Gemini, and others can all edit the same repo without stepping on the generated HTML.

Add as many `.md` notes as you want, let different models draft them, and drop them in `notebooks/`. Every file is picked up and added to the final site automatically.

## Try It

The next two notebooks are placeholders. Open them, replace the content with your own notes, and run the build — the sidebar and pages update on their own.
