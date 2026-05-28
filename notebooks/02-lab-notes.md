# Lab Notes

Experiments, prototypes, and small sparks that might turn into something larger.

## Experiment: Personal Knowledge Radar

Imagine a tiny script that scans your notebooks and returns the ideas you have not touched recently. The goal is not productivity theater; it is resurfacing dormant thoughts before they disappear.

### Inputs

- Markdown files in `notebooks/`.
- Last modified time from Git or the filesystem.
- Optional tags like `#idea`, `#draft`, or `#research`.

### Output

```text
3 notes to revisit this week

1. Field Guide
   Last touched: 18 days ago
   Prompt: Turn the research loop into a reusable checklist.

2. Interface Sketches
   Last touched: 27 days ago
   Prompt: Add screenshots or wireframes.

3. Reading Queue
   Last touched: 42 days ago
   Prompt: Archive links that no longer matter.
```

## Experiment: Friction Log

For one week, write down every moment where a tool, process, or explanation slowed you down. At the end, group the notes into patterns.

| Friction | Possible fix |
|---|---|
| Repeating the same command | Add a script |
| Forgetting project context | Add a README section |
| Unclear folder ownership | Rename the folder |
| Long setup time | Add a bootstrap command |

## Prompts Worth Keeping

- What would make this note useful six months from now?
- What is the smallest example that proves the idea?
- What should be boring, predictable, and automated?
- Where is the sharp edge that future-me will forget?

