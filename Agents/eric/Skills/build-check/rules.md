# Build Check -- Rules

- Never remove a dependency unilaterally -- flag it, a human confirms it's actually
  unused before deletion
- Build-tool config corrections (output mode, base URL, image config) go out as a PR to
  staging, never committed directly
- A build-time regression with no obvious cause (no new pages, no new dependencies) is a
  notify with analysis, not a silent fix -- something structural likely changed
- No em dashes in any output
