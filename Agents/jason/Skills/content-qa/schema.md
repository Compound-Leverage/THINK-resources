# Content QA -- Schema

Bring your own site standards file (see
`Plugins/ops-team-open/customization/my-site-standards.md` for the format this repo
ships). These are the fields the workflow and rules expect to find, not a specific
vendor's schema.

## Page classification record

| Field | Type | Description |
|---|---|---|
| `path` | text | The page's route or file path |
| `page_type` | select | Product / Utility |
| `excluded` | boolean | True if matched `page_types.excluded_patterns` -- skip all checks |

## H1 finding record

| Field | Type | Description |
|---|---|---|
| `page` | text | Path from the classification record |
| `current_h1` | text | The H1 as currently written |
| `verdict` | select | PASS / FLAG |
| `reason` | text | Why it was flagged, citing the specific rule violated |
| `proposed` | list | 1 option (utility) or 2 options (product), present only on FLAG |

## Copy consistency finding record

| Field | Type | Description |
|---|---|---|
| `page` | text | Path where the divergence was found |
| `issue` | text | What was found (e.g. CTA destination mismatch, banned term used) |
| `expected` | text | The approved line or rule from your site standards |
| `verdict` | select | FLAG |

## Suggested config fields this skill reads
See `core/config.template.json`:
- `page_types.product_patterns`, `page_types.utility_patterns`,
  `page_types.excluded_patterns`
- `standards.site_standards_path`

No live database IDs, API keys, or webhook URLs belong in this file, `core/config.template.json`,
or any record you commit to version control -- store those in your own environment
configuration.
