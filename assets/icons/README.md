# THINK School icon assets

`think-school.png` is the approved THINK School mark (dark background `#0D0C11`,
purple glyph `#673FBA`), copied here as the single shared visual identity for every
plugin's `interface.composerIcon` / `interface.logo` fields (see each
`Plugins/*/.codex-plugin/plugin.json`). Source: 1254x1254 PNG, square, no
transparency -- resolution is production-ready for the OpenAI submission portal.
Confirm exact size/format requirements in the portal at submit time; resize down
if it asks for something smaller, don't re-export from a lower-res source.

## Structure

Each plugin keeps its own copy under `Plugins/<name>/assets/think-school.png` so
plugin manifests can reference a plugin-relative path (matching the existing
`"skills": "./skills"` convention) without depending on a shared repo-root path
that may not resolve the same way across hosts.

Future per-team icons (once approved) drop in the same way, no manifest
restructuring needed:

```
assets/icons/
  think-school.png       (shared identity -- in place)
  capture-team.png        (not yet supplied)
  proposal-team.png       (not yet supplied)
  content-team.png        (not yet supplied)
  sales-bd-team.png       (not yet supplied)
  sales-enablement.png    (not yet supplied)
  lead-discovery.png      (not yet supplied)
  fulfillment.png         (not yet supplied)
  proposal-generator.png  (not yet supplied)
```

When a per-team icon is supplied, copy it into that plugin's own `assets/`
folder and repoint that plugin's `interface.composerIcon`/`logo` at it -- every
other plugin keeps using the shared `think-school.png` until its turn comes.
