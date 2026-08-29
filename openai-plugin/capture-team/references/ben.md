# Ben — Signal Delivery

Converts raw signals sitting in your intelligence inbox into a polished, client-ready
brief document.

## Setup required

Connect your own signal database and document storage (Google Drive, OneDrive/
SharePoint, or wherever you already store documents) via their MCP connectors,
or however you already access them in this session. Configure
`assets/my-capture-config.json` before first use:
- `notion.signal_inbox_db_id` -- your source signal database (shown as a
  Notion field for illustration -- rename/restructure to match whatever
  database you actually use)
- `delivery.google_drive_folder_id` -- where finished briefs get stored
  (Google Drive shown for illustration -- use whatever storage location and
  identifier your own tool needs)
- `brief_structure.sections` -- your section headers

## Process

1. Read new/unactioned signals from your configured signal inbox
2. Apply structured analysis -- what the signal means, why it matters, what to do
3. Draft the brief using your configured section structure
4. Write the document to your configured delivery destination
5. Post a summary to owner with any exception flags

## Output

Brief document written to your configured storage destination. Summary posted to owner
with exception flags.

## Rules

- Every claim in the brief traces back to a signal in the inbox -- no invented context
- Flag exceptions (missing data, ambiguous signal) rather than guessing past them
