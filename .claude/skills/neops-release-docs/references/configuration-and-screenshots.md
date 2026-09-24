# Configuration and screenshot evidence

Use this procedure for every release, not only network-diagram changes.

## Find configuration users can control

Start from each user-visible release highlight and trace the implementation at the exact target tag.

Use this evidence order:

1. Dashboard card registrations and their JSON form schemas.
2. Saved configuration DTOs, interfaces, and public model types.
3. Migration functions and version numbers for saved configuration.
4. Default constants and runtime fallback behavior.
5. Shipped sample configurations and demo fixtures.
6. Tests that establish valid values, precedence, and boundary behavior.
7. Implementation code only when the public contract remains unclear.

Compare the previous and target release tags. Record settings that are new, removed, renamed, migrated, or behaviorally different. Distinguish among:

- visible form settings available to dashboard editors;
- expert-mode JSON or JMESPath settings;
- deployment environment variables;
- internal component inputs that users cannot configure.

Only the first three belong in user-facing release documentation.

## Write configuration examples

Copy the smallest useful shape from a shipped sample configuration, then remove unrelated data. Verify every property and enum value against the target tag.

For each example:

- identify the card, feature, or deployment surface it configures;
- explain the settings that materially change behavior;
- state defaults when omitting a setting changes the meaning;
- state whether existing saved configurations are migrated automatically;
- state required manual action before optional tuning;
- keep identifiers and sample data generic and non-sensitive.

Prefer one cohesive JSON or environment example over several disconnected fragments. Do not copy a large fixture merely to prove that a field exists.

## Capture screenshots

Use this source priority:

1. A first-party demo route and fixture shipped at the exact SDK or client tag.
2. An exact local client build with seeded or sanitized data.
3. A configured staging deployment whose displayed version matches the target tag.
4. No screenshot when none of the above is trustworthy.

For a first-party demo:

1. Create a detached worktree at the exact tag.
2. Install from its lockfile, or reuse dependencies only after confirming the dependency files match that tag.
3. Start the demo without modifying the source fixture.
4. Navigate to the documented demo route and select the shipped sample configuration.
5. Verify the visible feature state and inspect browser errors.
6. Capture a consistent light-theme viewport with no private data.
7. Store the image under `docs/releases/assets/<tag>/` and add descriptive alt text and a factual caption.

For a configuration-heavy visual change, prefer:

- one screenshot of the configured result;
- one screenshot of the relevant editor controls or configuration view, when that surface exists and is legible;
- a Markdown JSON example instead of a screenshot when text is clearer.

Never screenshot source code, terminal output, or a demo that does not faithfully exercise the documented configuration.
