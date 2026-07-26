# Findings Routing -- Workflow

The approval gate every other Jason skill routes through. Receives raw findings,
formats them, and posts them to wherever you want them reviewed. This is the only skill
that writes to an external destination, and the only skill that decides whether a fix
can go straight to a PR or has to wait for you.

## Step 1: Collect raw findings
Every other skill (`content-qa`, `site-audit`, `security-audit`, `agent-fleet-audit`,
`docs-maintenance`) returns a list of findings, each tagged PASS, FLAG, or RECOMMEND.
Findings-routing consumes that list -- it doesn't generate its own.

## Step 2: Sort by lane
For every FLAG or RECOMMEND, check whether it matches an entry in your
`routing.rule_based` or `routing.judgment_call` list (`core/config.template.json`):
- Matches `rule_based`: mechanical, deterministic fix -- hand off to your own PR-opening
  tooling (a `gh pr create` step, or equivalent) against your staging branch. Include the
  PR URL in the report.
- Matches `judgment_call`, or matches neither list: hold for review. Never guess.
- PASSes are dropped from the detail view and rolled into a single count.

## Step 3: Format
Use `Templates/jason-qa-reviewer.md`'s Post-Deploy Audit Report as the base format for
routine site-audit and content-qa runs. Use `templates/agent-fleet-audit-report.md` in
this repo's `Agents/jason/templates/` for agent-fleet-audit runs, and
`templates/docs-update-proposal.md` or `templates/changelog-entry.md` for
docs-maintenance output. Every finding cites the exact page, section, or file it came
from -- no finding ships without a citation.

## Step 4: Post
Post the formatted report to your configured `notifications.destination`
(`core/config.template.json`). If nothing was found this run, post a short "nothing to
flag" message instead of the full report -- don't burn a review cycle on an empty run.

## Step 5: Stop
Findings-routing does not take further action once posted. Reviewing the report and
deciding what happens to each judgment call is your job, not Jason's.

## Output
- A formatted findings report, posted to your configured destination
- PR URLs for any rule-based fix opened this run
- A running count of PASSes, not itemized
