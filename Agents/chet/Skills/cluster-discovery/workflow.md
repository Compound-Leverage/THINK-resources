# Cluster Discovery -- Workflow

Capability-first cluster finding. Instead of scanning broadly for events and testing
which capability fits each one, start from a capability you already know how to deliver
(your own filled-in copy of `core/config.template.json`), then hunt for every named
group carrying that exact gap.

Load your filled-in config before running any step below.

## Step 1: Load pre-validated groups
For each capability with `known_groups` populated, treat every listed group as
pre-validated. Its dependency is already confirmed by the group's own documented
existence -- don't re-test or re-derive it.

Before doing per-group work in Steps 3-4, check two gates. Either one alone is enough to
skip a group entirely this run:
- **Manual pause:** you've marked this specific group paused, without archiving or
  deleting it
- **Automatic stop:** the group's status is Saturating or Closed -- its window is ending
  or already over, so continuing to research it is wasted work

## Step 2: Discover new groups for unmapped capabilities
For each capability with no `known_groups` yet, run its `signal_keywords` against your
scanning sources (`scanning.sources` in your config). A hit that resolves to a named,
bounded recipient group -- a real consortium, cohort, or membership body, not a one-off
organization -- becomes a new `known_groups` entry. Write it back into your config
immediately so the next scan treats it as pre-validated (Step 1).

**Watch for cascade siblings.** One underlying event -- a law, mandate, or policy change
-- can produce more than one distinct group response, not just one. A single policy can
create a tight, highly-qualified consortium on one side of an affected network and a
much larger, more loosely organized cohort with a different (often more foundational)
version of the same gap on the other side. When you find the first matching group from a
policy-driven signal, explicitly check whether a second, different group formed in
response to the same root event before treating the search as done. Mine each sibling's
gap volume, membership, and budget confirmation independently -- don't assume one
sibling's profile applies to another. Each real sibling is its own `known_groups` entry,
not a duplicate of the first one found.

Not every qualifying signal is a direct funding announcement -- a new compliance
requirement can create the same capacity-deficit pattern without a dollar allocation
attached.

## Step 3: Capacity gap volume test
Per group (existing or newly found in Step 2): count the member entities that show the
`signal_keywords` pattern. This is the gap-volume count. Fit against your capability is
already implied by starting the scan from that capability -- don't re-score it.

## Step 4: Mine per group
For each qualifying group, mine:
- Member entities -- the group's membership list
- Buyer identity -- who holds hiring or contracting authority, per entity
- Budget confirmation -- line item confirmed vs. inferred, citing the source
- Window estimate -- how long until the gap goes public or gets staffed elsewhere
- Gap volume -- the count from Step 3

Mine per qualifying group, not per individual event or entity -- a group with 15 members
showing the signal is one candidate record covering all 15, not 15 separate records.

## Step 5: Fan-out rule
One capability can produce multiple cluster candidates -- one per qualifying group.
Don't collapse multiple groups into a single record. Every group clearing your
`gap_volume_threshold` (default 3, set in your config) gets its own candidate record.

## Step 6: Unmatched signal routing
A signal that doesn't match any capability in your config, seen more than once across
scans, is not forced into a cluster. Log it per your `unmatched_signal_routing` config
(e.g. a product/build backlog) instead of reporting it as a cluster candidate.

## Step 7: Ongoing maintenance
On your scanning cadence (weekly is typical), re-run Steps 3-4 against existing
`known_groups` to keep membership, budget confirmation, and window estimates current,
correcting or removing stale entries as you go. Skip any group caught by either gate in
Step 1.

**Archive on closed window:** when a candidate's window estimate has passed without
conversion, archive that record (status -> Closed) rather than leaving it stale as
active.

## Output
Write each qualifying group as a Cluster Candidate Record -- see
`Templates/capture-team-open.md` for the base format, or `schema.md` in this folder for
the full field list and status transitions. No 0-100 fit score and no separate fit
field -- both are implied by starting the scan from a confirmed capability.
