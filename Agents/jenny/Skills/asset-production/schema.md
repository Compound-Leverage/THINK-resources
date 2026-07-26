# Asset Production -- Schema

Bring your own design tool and file storage. These are the fields the workflow and
rules expect to find, not a specific vendor's schema. Every `[bracket]` in
`core/config.template.json` is a placeholder for your own value.

## Config

See `core/config.template.json` for the brand, surface, tool, and naming config this
skill reads. Key sections:
- `brand.colors`, `brand.typography`, `brand.imagery_policy`, `brand.logo`,
  `brand.voice_rules`
- `surfaces.types[]` -- `surface_id`, `dimensions`, `format`, `notes`
- `tools.design_tool`, `tools.render_pipeline`, `tools.delivery_destination`
- `file_naming_convention`
- `notifications.destination`

## Production Brief (internal handoff, not a deliverable record)

If you're routing production to a separate tool or sub-agent, the handoff brief
carries:

| Field | Description |
|---|---|
| `surface_id` | Matches an entry in `surfaces.types` |
| `dimensions` / `format` | Pulled from the matched surface entry |
| `copy` | Exact headline, body, CTA, and key stat text, applied as given |
| `file_name` | Per `file_naming_convention` |
| `delivery_destination` | Per `tools.delivery_destination`, or an override stated in the brief |

## Delivery Note (what actually gets posted)

| Field | Description |
|---|---|
| `asset_name` | Name and surface type |
| `file_link` | Link at the delivery destination |
| `assumptions` | Anything assumed in Step 1 of `workflow.md`, or "none" |
| `qa_result` | Pass, listing the checklist in full, or not delivered |

No live API keys, webhook URLs, or other credentials belong in this file,
`core/config.template.json`, or any record you commit to version control, store
those in your own environment configuration.
