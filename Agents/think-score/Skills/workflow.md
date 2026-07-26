# THINK Score Workflow

The scoring process THINK Score runs when a Strategist asks "Score [Org Name]." Two inputs
come in, one report goes out: an org profile, a cluster or opportunity map, a scored
readiness report with gap analysis.

---

## Step 1: Gather the Org Profile

Pull the requesting org's profile record from your own database (Notion or otherwise --
see `schema.md` for the field list). At minimum you need:

- Sector and geography the org operates in
- Mission or service description (what they actually do, for whom)
- Current staffing capacity: headcount, open roles, and where the team is already
  stretched thin
- Existing relationships or network ties to funders, agencies, or decision-makers in
  their sector
- Any capital events they are already pursuing or have flagged as relevant

If the org profile is missing a field the rubric needs, do not guess a value. Note the
gap and either ask the Strategist for it or flag it in the report's Exceptions line.

## Step 2: Gather the Cluster / Opportunity Map

Pull the capital event(s) being scored against from your cluster or opportunity map
(the record type THINK Intelligence and THINK Signal both read and write). At minimum
you need, per event:

- What the event is (grant award, program launch, policy change, infrastructure funding)
- Funding size, if known or estimated
- Stage: pre-announcement/planning, active solicitation, or already awarded
- Window: how much time is left before the opportunity moves to execution or closes
- Competition type: unsolicited/sole-source, limited, set-aside, or open
- Source signal(s) this event traces back to

If the org is being scored against more than one event, score each one separately.
Do not average across events -- a report covers one org against one event (or produces
one section per event if the Strategist asked for a multi-event view).

## Step 3: Score Each Dimension

Apply the rubric in `rules.md`: four dimensions, 0-10 each, summing to a 0-40 total.
Score every dimension independently before totaling -- don't work backward from a
target score.

For any dimension scoring below a 3, record the specific reason it was capped (not just
the number). This is what makes the gap analysis in Step 4 legible instead of a bare
score.

## Step 4: Classify the Primary Gap

Identify the lowest-scoring dimension(s) and classify the primary gap using the mapping
in `rules.md` (Detection / Packaging / Timing / Capacity). If two dimensions are tied for
lowest, name both and let the Strategist prioritize -- don't invent a tiebreaker.

Capacity gaps are the ones a Digital Employee placement typically closes. If Capacity to
Act is the primary or a tied-primary gap, say so plainly in the report -- that's the
finding that leads to a placement conversation, not just a score.

## Step 5: Self-Check Before Assembly

Before writing the report, verify:

- The total equals the sum of the four dimension scores
- The Position label matches the band the total falls into (see `rules.md`)
- Every dimension below a 3 has a recorded cap reason
- The primary gap classification traces back to an actual low score, not an assumption

If any check fails, fix the scoring before moving on. Don't ship a report with a Position
label that doesn't match its total.

## Step 6: Assemble the Report

Fill out `templates/readiness-report.md` with the scored dimensions, total, Position
label, gap analysis, and a recommended next step ranked by urgency. Note any missing
input data in the Exceptions line at the bottom -- don't silently fill a gap with a guess.

## Step 7: Deliver

Hand the completed report to the requesting Strategist, or write it to the org's record
in your own database if that's the delivery pattern you've set up. Either way, the report
should stand on its own -- someone who wasn't in the room should be able to read it and
understand the org's position without asking follow-up questions.
