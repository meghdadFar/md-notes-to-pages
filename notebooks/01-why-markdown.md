# Why Markdown, Not HTML

Markdown is a great format which is both readable for LLMs and for human. But obviously it's not as easy to read for human, as rendered HTML, especially for longer content, illustrations, images, and content separations via tabs or other separators. On the other hand, it's much easier to edit, move around and maintain. It's much more minimal compared to HTML, which is heavily dependent on HTML tags. 

To have the best of both worlds, I used the following structure which treats the Markdown as a source of truth, but then automate the the rendering and deploying of the content into a nice HTML website, at push trigger. Here is why i think that small decision pays off, especially when you write with AI.

## The Idea

The initial idea of moving away from Markdown and using HTML comes from @trq212. I took it further: keep `.md` as the source in a GitHub repo and auto-generate HTML and publish on every push to `main`.

A small Python render script (a Markdown library + an HTML template + CSS) turns `notebooks/*.md` into `_site/`, and a GitHub Actions workflow deploys it to GitHub Pages on every commit.

You or any AI with access to this repo only ever edit Markdown. But when you commit your changes, the edits will be published into a nicely readable HTML.

## 2x–4x Less Tokens and A Lot Faster

Editing HTML with AI was becoming difficult, time-consuming, and token-heavy. The same edits on `.md` are faster and far more efficient.

Depending on the size of the document, creating and editing the HTML can be 2x–4x the Markdown. For example, this markdown:

```markdown
## Idea
- One useful point
- Another useful point
```

becomes this HTML:

```html
<h2 id="idea">Idea<a class="headerlink" href="#idea" title="Permanent link"></a></h2>
<ul>
<li>One useful point</li>
<li>Another useful point</li>
</ul>
```

This is fine when you generate a little, and do not expect many edits. But when you create a lot of content, that is a lot of tokens you do not need to spend.

## Manual Edits Stay Easy

I frequently edit notes by hand, moving paragraphs around and reordering headings. That is trivial in Markdown and painful maybe near impossible in HTML. The smallest change usually means prompting a model to do it for you. Something that should be a quick manual fix turns into a prompting spree.

## Any Contributions Become Easier

Because the source is Markdown, Claude, Gemini, and others can all edit notes, without stepping on the generated HTML. If they were to edit the HTML, I observed in many cases, they overwrite each other's HTML tags, which usually starts a cycle of prompting and fixing, for issues that were not there in the first place.

I structured the repo in a way that you can add as many `.md` notes as you want, let different models draft them, and drop them in `notebooks/`. Every file is picked up and added to the final site automatically.

## Try It

The next two notebooks are placeholders. Open them, replace the content with your own notes, and run the build. The sidebar and pages update on their own.
