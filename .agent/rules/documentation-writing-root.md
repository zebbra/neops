---
trigger: always_on
---

### Handling tasks

- When prompted with a task, first determine if it belongs to this repository or a submodule of this repository.
- Then, document according to the conventions of the submodule and the rules in this file.
- You can validate your documentation by running `make doc-build`, in the root repository (test overall documentation) and submodules (test specific documentation)
- Always validate your documentations using `make doc-build` after every change!!

### Tools

- `make scan_docs`: Runs a script to scan all markdown files for compliance with the rules (no `../` links that go outside of the `docs` folder, no inlined code blocks). Use this to check your work.