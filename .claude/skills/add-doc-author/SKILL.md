---
name: add-doc-author
description: Add or update an author profile (avatar, role, links, email, mailmap) in the neops docs so they render correctly in the per-page footer. Use when a new person joins and starts committing to the docs, when an existing committer is missing their photo/role in the footer, or whenever the user asks to "add an author", "onboard <name> to the docs", "fix <name>'s avatar", or "fill out author info". Pulls headshots and roles from the neops.io team roster.
---

# Add / update a docs author

The docs footer (the `mkdocs-document-dates` plugin) shows each page's git
authors with an avatar, name, role and profile link. That metadata lives in
`docs/authors.yml`, keyed by the author's **canonical git name**. This skill
fills out a person's entry end to end: resolve their canonical name, grab their
headshot + role from neops.io, store a resized avatar, and write the YAML.

## Key files
- `docs/authors.yml` — the author profiles (keyed by canonical `%aN`).
- `docs/assets/authors/` — local avatar images (kebab-case, e.g. `jane-doe.png`).
- `.mailmap` (repo root) — folds a person's alias names/emails into one canonical identity.

## Inputs to gather
Ask the user only for what you can't derive: the person's **full name** (as it
should display). Everything else (email, photo, role, profile URL) you fetch or
infer. If they commit under odd names/emails, also get those aliases for the
mailmap.

## Steps

1. **Find the canonical git name.** The `authors.yml` key MUST match what
   `git log --use-mailmap` emits. List current canonical names across the docs
   (main repo + submodules):
   ```bash
   { git -c log.showSignature=false -c mailmap.file=.mailmap log --use-mailmap --format='%aN';
     git submodule --quiet foreach 'git -c log.showSignature=false -c mailmap.file="$toplevel/.mailmap" log --use-mailmap --format="%aN"' 2>/dev/null; } \
     | grep -viE 'gpg:|signature' | sort -u
   ```
   If the person appears under several spellings/emails, add a `.mailmap` line so
   they collapse to one identity (format `Canonical Name <canonical@email> <alias@email>`),
   then re-check. Their canonical name is the `authors.yml` key.

2. **Fetch their headshot + role from neops.io.** The team roster lives at
   `https://www.neops.io/about#team`, with per-person pages at
   `https://www.neops.io/team/<first-name-last-name>` (lowercase, hyphenated).
   Use WebFetch on `https://neops.io` (or `/about`) to read the roster — it lists
   each member's name, role, and a headshot image URL on the Webflow CDN
   (`https://cdn.prod.website-files.com/.../<Name>.png`). Match by name and note:
   - the **photo URL**,
   - their **role** (becomes the tooltip `description`, e.g. "Software Solutioneer"),
   - the **team-page URL** `https://www.neops.io/team/<slug>` (becomes `url`).

   If the person isn't on neops.io, check zebbra.ch; if still nothing, leave
   `avatar` unset (the plugin falls back to a Gravatar from `email`) and tell the
   user. For external contributors, a `https://github.com/<handle>.png` avatar +
   GitHub `url` is the right fallback (that's how Tim Zurbuchen is configured).

3. **Download and resize the avatar** into `docs/assets/authors/<slug>.png`
   (slug = kebab-case of the name). Keep avatars small — resize to 256×256:
   ```bash
   cd docs/assets/authors
   curl -fsSL "<photo-url>" -o <slug>.png
   file <slug>.png   # confirm it's a real PNG/JPEG, not an HTML error page
   if command -v magick >/dev/null; then RS=magick; elif command -v convert >/dev/null; then RS=convert; fi
   [ -n "$RS" ] && $RS <slug>.png -resize 256x256^ -gravity center -extent 256x256 -strip <slug>.png
   ```
   The CDN filenames often contain spaces — URL-encode them (`%20`) in `curl`.

4. **Write the `docs/authors.yml` entry.** Email convention is
   `<first>.<last>@zebbra.ch`. Avatar path is relative to `docs_dir`
   (`assets/authors/<slug>.png`). Example:
   ```yaml
     "Jane Doe":
       name: Jane Doe
       email: jane.doe@zebbra.ch
       avatar: assets/authors/jane-doe.png
       url: https://www.neops.io/team/jane-doe
       description: Network Automation Engineer
   ```
   Match the formatting/2-space indentation of the existing entries; add the new
   block in author order, don't reformat the rest.

5. **Verify it renders.** Start the docs and check the footer:
   ```bash
   make doc-serve   # serves at http://127.0.0.1:8000/<site-path>/
   ```
   With the Playwright MCP, open a page the person authored (find one via
   `git log --author='<Name>' --name-only -- '*.md'` in the relevant repo) and
   confirm their avatar is an `<img>` (not initials) and the tooltip shows the
   role + link. If they have **no `.md` commits yet**, the entry won't appear
   anywhere yet — that's fine, say so. Stop the server (`pkill -f doc_serve_watch`;
   kill any leftover `mkdocs serve`) and remove any screenshots / `.playwright-mcp`
   you created when done.

## Notes
- `docs/authors.yml`, `.mailmap`, and `docs/assets/authors/*` are **content in the
  neops repo**, not the mkdocs-documentation template — commit them here when done.
- Avatars and `authors.yml` are the only things to touch; the plugin, hook, and
  styling already ship from the template.
