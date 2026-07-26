# CRM Intake -- Schema

Bring your own database (Notion, Airtable, a spreadsheet). These are the fields the
workflow and rules expect to find, not a specific vendor's schema. Every `[bracket]`
in `core/config.template.json` is a placeholder for your own value.

## Config
See `core/config.template.json` for the ICP profiles, routing flags, intake sources,
and enrichment config this skill reads. Key sections:
- `icp_profiles.profiles[]` -- `profile_id`, `label`, `org_types`, `size_range`,
  `qualifying_signals`, `enrichment_tier`
- `routing_flags` -- `qualified_flag`, `unqualified_flag`, `escalation_flag`,
  `unresolved_flag`
- `intake_sources.sources`, `intake_sources.cadence`
- `enrichment.provider`, `enrichment.api_key_env_var`,
  `enrichment.confidence_threshold`, `enrichment.deep_enrichment_provider`
- `audit.stalled_after_days`

## Contacts record
| Field | Type | Description |
|---|---|---|
| `name` | text | Contact's full name |
| `title` | text | Job title, from enrichment |
| `organization` | link | Link to the Organizations record |
| `email` | email | Verified email, or blank if none found |
| `email_status` | select | Verified / Unverified -- confirm before send / Not found |
| `icp_profile` | select | `profile_id` matched, or `unresolved_flag` |
| `routing_flag` | select | Value from `routing_flags` |
| `source` | text | Which intake source this record came from |
| `date_enriched` | date | When this record was last processed |

## Organizations record
| Field | Type | Description |
|---|---|---|
| `name` | text | Org name |
| `website` | text | Domain used for lookup |
| `org_type` | select | One of your `icp_profiles.*.org_types` |
| `icp_profile` | select | `profile_id` matched |
| `routing_flag` | select | Value from `routing_flags` |
| `deep_enrichment_fields` | varies | Whatever your `deep_enrichment_provider` returns, only for `enrichment_tier: deep` profiles |
| `notes` | text | Conflicts flagged, manual review notes |

## Pipeline record update (when the source is a scored prospect list)
| Field | Type | Description |
|---|---|---|
| `decision_maker` | link | Link to the Contacts record |
| `notes` | text | "Contact enriched via [provider] -- [date]" |

## Expected output
- Every intake record processed within your `intake_sources.cadence` window
- Every record ICP-classified before advancing -- no unclassified records
- A verified contact on every routed record, or an explicit "no email found" flag
- No duplicate contacts
- Every pipeline record has a decision-maker linked before advancing, or is flagged
  by the periodic audit if it's been stalled past `audit.stalled_after_days`

No live database IDs, API keys, or webhook URLs belong in this file,
`core/config.template.json`, or any record you commit to version control -- store
those in your own environment configuration.
