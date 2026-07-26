# THINK Score Schema

Two record types feed THINK Score: an Org Profile and a Cluster / Opportunity Map entry.
Bring your own database (Notion or otherwise) -- these are the fields the workflow and
rubric expect to find, not a specific vendor's schema. Every `[bracket]` is a placeholder
for your own value.

---

## Org Profile Record

One record per org you score. This can live in the same database THINK Foundations users
build their org record in, or a separate one -- whatever you've already set up.

| Field | Type | Description |
|---|---|---|
| `org_name` | text | The org being scored |
| `sector` | text | Industry or mission area |
| `geography` | text | Primary operating region(s) |
| `service_description` | text | What the org does, for whom |
| `headcount` | number | Current staffing level |
| `open_roles` | text | Roles currently unfilled or stretched thin |
| `network_ties` | text | Known relationships to funders, agencies, or decision-makers relevant to their sector |
| `active_pursuits` | text | Capital events the org is already pursuing or has flagged |
| `last_scored_date` | date | Most recent THINK Score run for this org |

---

## Cluster / Opportunity Map Record

One record per capital event being scored against. This is the same record type THINK
Intelligence and THINK Signal read and write -- if you've already set one of those up,
point THINK Score at the same database.

| Field | Type | Description |
|---|---|---|
| `event_name` | text | Name or short label for the capital event |
| `event_type` | select | Grant award / Contract or RFP / Program launch / Policy change / Infrastructure funding |
| `funding_size` | number or range | Known or estimated funding amount |
| `stage` | select | Pre-announcement / Planning / Active solicitation / Awarded |
| `window_close_estimate` | date or text | When the opportunity moves to execution or closes |
| `competition_type` | select | Unsolicited or sole-source / Limited / Set-aside / Open |
| `source_signal` | text or link | Where this event was first identified |
| `linked_org_ids` | relation | Org Profile records already being scored against this event |

---

## Configuration

Point THINK Score at your own database and field names. If you're adapting one of the
other plugins' `customization/*.json` patterns, a comparable config for THINK Score looks
like:

```json
{
  "_instructions": "Configure your own database IDs and field names for THINK Score. Update whenever your org profile or cluster map schema changes.",
  "_last_updated": "[DATE YOU LAST UPDATED THIS FILE]",

  "database": {
    "org_profile_db_id": "[YOUR ORG PROFILE DB ID]",
    "cluster_map_db_id": "[YOUR CLUSTER/OPPORTUNITY MAP DB ID]"
  },

  "field_map": {
    "_instructions": "If your field names differ from schema.md's defaults, map them here.",
    "org_name": "[YOUR FIELD NAME]",
    "headcount": "[YOUR FIELD NAME]",
    "event_name": "[YOUR FIELD NAME]",
    "window_close_estimate": "[YOUR FIELD NAME]"
  },

  "output": {
    "_instructions": "Where the scored readiness report gets written or delivered.",
    "destination": "[e.g. 'Org Profile record, as a linked page' or 'delivered to requesting Strategist']"
  }
}
```

No live database IDs, API keys, or webhook URLs belong in this file or in any record you
commit to version control -- store those in your own environment configuration.
