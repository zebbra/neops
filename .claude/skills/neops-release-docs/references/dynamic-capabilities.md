# Dynamic capability contracts

Use this guide when user configuration looks open-ended in the client but another repository controls which values actually work.
Common examples are sorting keys, entity fields, provider names, feature identifiers, route targets, and plugin capabilities.

## Trace the complete contract

Start from the user-facing configuration field and follow it across every boundary that constrains it:

1. Find the client or dashboard schema that accepts the value.
2. Find the SDK code that sends, validates, transforms, or disables it.
3. Find the API query or endpoint that exposes capabilities, when one exists.
4. Find the backend registry, enum, mapping, validator, or dispatch table that defines the accepted values.
5. Compare the previous and target release tags to identify added, removed, renamed, or newly advertised values.

Do not conclude that any string is valid merely because the frontend type is `string`.
Do not stop at examples when the accepted set is finite.

## Separate canonical values from compatibility spellings

Identify which names users should put in new configuration.
Keep these separate from legacy aliases, index-prefixed forms, internal storage paths, and compatibility spellings.

- Publish the complete canonical public set.
- Mention legacy aliases only when operators need them to understand existing saved configuration.
- Recommend canonical values for new configuration.
- Never expose internal field paths as public configuration unless the implementation explicitly accepts them as part of the public contract.

## Document version support and live availability

A release-level registry and a live deployment can answer different questions.

- The registry at the target tag defines what that software version can support.
- A capability query may filter the registry against migrations, installed modules, index mappings, permissions, or runtime configuration.

Document both when both exist:

1. Add a complete table of canonical values grouped by the context that selects them, such as entity type or provider.
2. Include the capability query or endpoint with the smallest useful request example.
3. State that the live response is authoritative for the current deployment.
4. Explain what operational action populates or changes availability, such as an index rebuild or migration.

The release story should lead with the added user capability.
Capability discovery and rejection of unsupported values explain safe behavior but normally remain supporting details.

## Prefer deterministic generation

When the registry is machine-readable, generate the versioned reference table rather than transcribing it manually.
Pin generation to the exact backend or SDK tag included by the client release.

Choose the least fragile extraction method that preserves the public contract:

- import a side-effect-free registry;
- call a build fixture or schema command;
- parse a static enum or registry definition;
- query an isolated exact-version service.

If importing application code requires services or settings, prefer a small parser or an existing schema-generation command over booting production configuration.

For a durable configuration reference, add a drift check that compares the documented or generated values with the target registry.
The check should fail or produce an actionable review item when canonical values change.

## Validate before preview

Confirm all of the following:

- every relevant context, entity type, or provider is represented;
- every documented canonical value exists in the target registry;
- no target canonical value is missing from the reference;
- configuration examples use canonical values;
- the discovery query or endpoint matches the target schema;
- runtime filtering and required migrations or rebuilds are stated;
- the release page links to the durable reference instead of becoming the only complete list.
