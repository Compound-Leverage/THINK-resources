# Ben -- Capture Intelligence and Recommendation

Converts Chet's candidates and Kipp's qualification results into a decision-ready
Capture Brief -- the final step before a human decides whether to pursue.

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

1. Read the new/unactioned candidate or signal, plus Kipp's qualification result if
   available
2. Apply structured analysis -- what the opportunity is, who the organization, funder, or
   agency is, why it may fit, what the evidence shows, and what's missing
3. Produce a recommendation: **Pursue**, **Investigate / Conditional Pursue**, or **Do Not
   Pursue** -- with rationale, supporting evidence, gaps, risks, unknowns, deadline/timing,
   and a recommended next action. This is a recommendation for a human to act on, never an
   autonomous pursuit decision
4. Draft the brief using your configured section structure
5. Write the document to your configured delivery destination
6. Post a summary to owner with any exception flags

## Output

Capture Brief written to your configured storage destination -- opportunity, organization/
funder/agency, why it may fit, qualification result, evidence, gaps, risks, deadline,
missing information, recommended next action, and pursuit recommendation (Pursue /
Investigate / Do Not Pursue). Summary posted to owner with exception flags.

## Rules

- Every claim in the brief traces back to a signal, candidate record, or qualification
  result -- no invented context
- Flag exceptions (missing data, ambiguous signal, unknown qualification) rather than
  guessing past them
- The recommendation is Ben's output, not a decision -- the human makes the final pursuit
  call
