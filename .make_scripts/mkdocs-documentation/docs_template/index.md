# Your project documentation

This is the seed `index.md` for a new project. Replace it with a real overview, then add pages under `docs/` following the [Neops writing conventions](https://zebbra.github.io/mkdocs-documentation/conventions/).

A useful landing page tells the reader, in this order:

1. What this project *is*, in one sentence.
2. Who uses it (operators? developers? both?).
3. Where to go next.

The grid-card pattern below is the standard way to surface "where to go next". The placeholder links point at the template's hosted writing-conventions guide so a fresh build doesn't fail — replace each `Read more` href with a real section path once you create those pages (e.g. `getting-started/index.md`, `10-concepts/index.md`).

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } __Getting started__

    ---

    A short tutorial that takes a new reader from zero to a working hello-world.

    [:octicons-arrow-right-24: How we structure pages](https://zebbra.github.io/mkdocs-documentation/conventions/#page-structure)

-   :material-book-open-page-variant:{ .lg .middle } __Concepts__

    ---

    The mental model — what the moving parts are and how they fit together.

    [:octicons-arrow-right-24: How we structure pages](https://zebbra.github.io/mkdocs-documentation/conventions/#page-structure)

</div>

## Including this site in the aggregated build

If this project is one component of a larger Neops site, add a line to the **parent** repo's `mkdocs_custom.yml`:

```yaml
nav:
  - Your component: "!include ./docs/your-repo-name/mkdocs_custom.yml"
```

Then add this repo as a submodule of the parent under `docs/your-repo-name`. The aggregated build pulls each submodule's nav and pages into a single site.

## Next steps for this template

- Open [Writing Conventions](https://zebbra.github.io/mkdocs-documentation/conventions/) and skim the snippet, admonition and status-warning patterns before you write much.
- Set `site_url`, `repo_url`, and `nav` in `mkdocs_custom.yml` (next to this file).
- Optional: add `.mailmap` at the repo root and `docs/authors.yml` here if you want author profiles in the per-page footer.
