# Release story quality

Use this guide to turn release evidence into a page that an everyday Neops user can scan and act on.

## Establish the previous-release baseline

Compare the target release with the previous stable release before deciding what is new or important.
Pull requests and commits often describe a large implementation even when users already had a simpler version of the same workflow.

For each candidate highlight, answer:

- What could the user already do in the previous stable release?
- What additional task, field coverage, workflow step, or control does the target release add?
- Is the change new behavior, an extension of existing behavior, a guardrail, or internal support?
- Which part belongs in the headline, and which part explains reliability or compatibility?

Use comparative language when a feature already existed.
For example, say that an existing link now opens an authenticated in-app page instead of presenting the whole integration as new.

## Build a coverage map before writing

For every meaningful client or included SDK change, record:

| Field | Question to answer |
|---|---|
| Reader | Is this primarily for an everyday user, dashboard author, task author, or operator? |
| Surface | Which page, card, dialog, table, or deployment setting changed? |
| Previous-release baseline | What could the reader already do before this release? |
| Previous friction | What was difficult, missing, or unclear before this release? |
| New outcome | What can the reader now do or understand? |
| Change class | Is this a new workflow, an extension, expanded coverage, a guardrail, or internal support? |
| Story role | Is this a headline outcome, supporting behavior, upgrade note, or technical detail? |
| Concrete example | What realistic task, data shape, schedule, filter, or login choice demonstrates it? |
| Configuration | Did a user-controlled field, default, valid value, or migration change? |
| Accepted-value contract | Is a string, key, path, or identifier constrained by a registry, enum, schema, validator, or capability API in another repository? |
| Visual evidence | Can an exact-version screenshot show the result or interaction? |
| Required action | Must anyone change configuration, rebuild an extension, or coordinate versions? |

Use this map to group related changes into two to five coherent highlights.
Do not omit a major visible or conceptual change merely because the client commit only updates package versions.

## Separate the feature from its guardrails

Lead with what readers can now do.
If a release makes more fields sortable, name the added field groups and the tables that gain them.
Capability discovery and rejection of unsupported keys explain why the feature behaves safely, but they are not the headline unless preventing those failures is the main user outcome.

Use this test for each proposed heading:

1. Could a reader describe the new or expanded task after reading only the heading and first sentence?
2. Does the wording name the affected records, fields, screen, or workflow?
3. Would removing the validation or fallback details leave the core user capability intact?

If the third answer is yes, keep those details as supporting behavior.
Avoid abstract headlines such as "backend-aware behavior" when the evidence supports a concrete description.

## Make the page understandable at a glance

After the release date and short summary, add an **At a glance** table with three columns:

| Area | What changed | Why it matters |
|---|---|---|

Use concrete area names that readers recognize, such as **Task cockpit**, **Executions**, **Entity tables**, or **Dashboard editor**.
Keep each cell to one or two direct sentences.
Mention required upgrade action in this table when it is important enough that a reader should not miss it.
Order rows by user significance, not commit order, implementation size, or which repository supplied the change.

## Turn each highlight into a small user story

For each major highlight:

1. Name the screen or workflow and the previous problem.
2. Explain what changed in visible terms.
3. Give a realistic example or a short **How it works** sequence when an interaction has multiple steps.
4. Show a screenshot when it communicates the change faster than prose.
5. Include the smallest verified configuration example when the user controls the behavior.
6. State defaults, limits, compatibility, and migration behavior close to the relevant feature.

Prefer text such as "Select the devices, start the task, then follow progress in the executions panel" over abstractions such as "task launch behavior was centralized."
Replace generic benefits such as "improves usability" with the observable result.

## Choose concrete evidence

Each major highlight should have at least one useful concrete element:

- an exact-version UI screenshot;
- a verified configuration example;
- a short before-and-after behavior comparison;
- a numbered workflow walkthrough;
- a realistic example showing input and result.

Screenshots should show a meaningful state, not an empty shell.
When authentication or backend data prevents a trustworthy screenshot, prefer a specific walkthrough or example rather than vague prose.

## Review from the reader's perspective

Before previewing, verify that a reader who has not seen the pull requests can answer:

- What will look or behave differently after the upgrade?
- Where do I find it?
- What task is easier or newly possible?
- Do I need to configure or migrate anything?
- Is there an example I can adapt?
- If configuration accepts a finite set of values, where is the complete current list and how can a live deployment report its available subset?
- Which behavior is genuinely new, and which behavior extends something from the previous release?
- What is the primary capability, and what merely validates or protects it?

If any answer requires reading the technical links, enrich the main page first.
