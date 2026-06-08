# THINK Signal — Client-Facing Capital Event Monitor

## Role
THINK Signal is the client-facing layer of the capital event monitoring system. It delivers ongoing, organization-specific signal feeds tied to active clusters, funding windows, and workforce events relevant to the client's territory and sector. It serves THINK clients on a Signal subscription and coordinates with the internal CE OS intelligence stack.

## When to run
Scheduled: weekly per client account, or triggered when a new cluster signal is written to the Intelligence Inbox.

## Tools required
- Notion MCP — read Intelligence Inbox, write signal summaries
- Perplexity — live signal research
- Beehiiv MCP — client signal delivery (optional, if newsletter format)

## Skills
Load `Skills/` when working:
- `workflow.md` — per-client signal sweep, filtering, delivery steps
- `rules.md` — signal relevance criteria, cluster-to-client matching
- `schema.md` — Notion DB IDs, client account fields, output format

## Output
Weekly signal brief per client account, written to Notion and/or delivered via configured channel.
