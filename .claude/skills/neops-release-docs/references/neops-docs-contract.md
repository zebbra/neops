# Neops release documentation contract

## Publishing topology

`docs.neops.io` is built by the `zebbra/neops` repository.
That repository registers `neops-web-client` under `docs/neops-web-client` as a Git submodule and refreshes submodules from `develop` in its scheduled Pages workflow.

The one-time central navigation entry is:

```yaml
- "Web Client Releases": "!include ./docs/neops-web-client/mkdocs_release_notes.yml"
```

The release-only include avoids presenting the unfinished web client user guide as complete.

The skill publishes release entries directly from a temporary detached worktree to `neops-web-client:develop` after explicit preview approval. The central include is published once to `zebbra/neops:main`. Later releases never modify the central repository because its scheduled or manually dispatched Pages workflow refreshes the client submodule from `develop`.

## Files owned by neops-web-client

```text
docs/
  releases/
    index.md
    vX.Y.Z.md
    assets/
      vX.Y.Z/
        descriptive-screenshot.png
mkdocs_release_notes.yml
```

`mkdocs_custom.yml` includes `mkdocs_release_notes.yml` so the release section is also validated by the client repository's local documentation build.

## Release page shape

Use only sections that contain useful information:

```markdown
# Neops Web Client X.Y.Z

Released YYYY-MM-DD

One short paragraph describing the release in user terms.

## At a glance

| Area | What changed | Why it matters |
|---|---|---|
| Recognizable screen or workflow | Visible behavior | Concrete user outcome |

## Highlights

### Outcome-oriented feature title

Explain what the user can now do, where they encounter it, and any important limit.

Give a concrete scenario, short workflow, or before-and-after comparison.

![Specific, useful alt text](assets/vX.Y.Z/descriptive-screenshot.png)

*Short caption explaining what is shown.*

## Fixes and improvements

- Describe observable behavior, not implementation details.

## Upgrade notes

Include only required configuration, migration, compatibility, or operational action.

## Technical details

- [Full client changelog](https://github.com/zebbra/neops-web-client/compare/vPREVIOUS...vCURRENT)
- [Included SDK release](https://github.com/zebbra/neops-web-sdk/releases/tag/vSDK)
```

Do not add empty sections. A dependency-only release can be short.

## Index and navigation

`docs/releases/index.md` gives a short explanation followed by newest-first release links with one-sentence summaries.

`mkdocs_release_notes.yml` contains only portable navigation information:

```yaml
docs_dir: docs

nav:
  - Overview: releases/index.md
  - vX.Y.Z: releases/vX.Y.Z.md
```

Insert new stable releases immediately after Overview. Do not add preview or beta releases unless the user explicitly asks to document them.

## Writing rules

- Address Neops users and operators, not package maintainers.
- Optimize the opening summary and At a glance table for an everyday user who has not read the underlying pull requests.
- Lead with tasks, behavior, and operational consequences.
- Prefer concrete verbs such as "archive", "compare", "configure", and "restore".
- Explain unfamiliar terms at first use.
- Keep most releases to two to five highlights.
- Give every major highlight a concrete example, workflow, before-and-after explanation, configuration sample, or exact-version screenshot.
- Group small related fixes instead of listing every pull request.
- Mention breaking changes and required action before optional improvements.
- Use sentence case for headings.
- Do not use an em dash.
- Do not include confidential deployment details or private data.

## SDK package boundary

The SDK currently publishes these client-consumed packages:

- `@zebbra/ngx-jsonforms-carbon`
- `@zebbra/ngx-neops-app-components`
- `@zebbra/ngx-neops-app-services`
- `@zebbra/ngx-neops-client`
- `@zebbra/ngx-neops-icons`
- `@zebbra/ngx-neops-sdk-artifacts`
- `@zebbra/ngx-neops-storage-client`

Discover the authoritative package set from a sibling `neops-web-sdk` checkout when available. Do not assume other `@zebbra` packages come from that repository.

## Screenshot decision

A screenshot is appropriate when all of these are true:

1. The change is visible and materially affects a workflow.
2. The exact target release can be verified in the running UI.
3. The required screen can be reached with demo or sanitized data.
4. The image explains something that prose alone does not convey as quickly.

Prefer one screenshot that shows the completed state. Use a short sequence only when the interaction itself is the important change.
