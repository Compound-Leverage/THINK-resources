# Cluster Discovery -- Schema

Bring your own database (Notion, Airtable, a spreadsheet). These are the fields the
workflow and rules expect to find, not a specific vendor's schema. Every `[bracket]` in
`core/config.template.json` is a placeholder for your own value.

## Config
See `core/config.template.json` for the capability map, scanning sources, and threshold
config this skill reads. Key sections:
- `capability_map.capabilities[]` -- `capability_id`, `capacity_solved`,
  `signal_keywords`, `known_groups`
- `scanning.sources`, `scanning.gap_volume_threshold`, `scanning.cadence`
- `thresholds.saturating_window_days`
- `unmatched_signal_routing.destination`

## Cluster Candidate Record
One record per qualifying group -- matches `Templates/cluster-discovery-chet.md`,
with the field list spelled out:

| Field | Type | Description |
|---|---|---|
| `group_name` | text | The named, bounded group (consortium, cohort, membership body) |
| `capability_matched` | text | `capability_id` / `capacity_solved` from your config |
| `member_entities` | number + list/link | Count and roster of member entities |
| `buyer_identity` | text | Who holds hiring or contracting authority |
| `budget_confirmation` | select | Confirmed line item / Inferred -- cite source |
| `gap_volume` | number | Count of member entities showing the signal pattern |
| `window_estimate` | date or text | Estimate until the gap goes public or gets staffed elsewhere |
| `status` | select | Forming / Confirmed / Active / Saturating / Closed |
| `source` | text or link | Where this group was found |

## Suggested status transitions
- New group found in Step 2 of `workflow.md`: **Forming**
- Steps 3-4 confirm dependency and gap volume clears your threshold: **Forming ->
  Confirmed** (safe to automate -- the bar is mechanical)
- Window estimate drops under your `thresholds.saturating_window_days`: **-> Saturating**
- Window passes without conversion: **-> Closed**

Adjust the statuses and thresholds to whatever your own pipeline actually uses -- these
are starting points, not fixed values.

No live database IDs, API keys, or webhook URLs belong in this file, `core/config.template.json`,
or any record you commit to version control -- store those in your own environment
configuration.
