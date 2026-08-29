# Chet -- Cluster Discovery

Chet starts from a capability your team already knows how to deliver, then hunts for every
named group carrying that exact gap -- rather than scanning broadly for events and testing
which capability fits each one. One confirmed capability signature can fan out into several
cluster candidates, one per qualifying group, not one per event.

## Setup required

Configure `assets/my-capture-config.json` before first use:
- `capability_map` -- your placement-capable capabilities, each with signal keywords and any
  groups already known to carry that gap
- `scanning.sources` -- the funding/mandate/sector sources you scan for new signals
- `scanning.gap_volume_threshold` -- minimum member count for a group to qualify

## Process

1. Load your capability map -- one entry per placement-capable capability, with any groups
   already known to carry that gap
2. For each pre-validated group: treat its own documented existence as confirmation: don't
   re-test dependency
3. For each capability with no groups mapped yet: run its signal keywords against your
   scanning sources (funding announcements, grant/mandate trackers, sector news) looking for
   a hit that resolves to a real, bounded group -- not a one-off organization. Write any new
   match back into your capability map so the next scan treats it as pre-validated
4. Per qualifying group, count how many member entities show the signal pattern -- this is
   the gap-volume count
5. Mine each qualifying group for: membership list, buyer identity (who has hiring/
   contracting authority), budget confirmation (line item confirmed vs. inferred), and a
   window estimate until the gap goes public or gets staffed elsewhere
6. Every group clearing your gap-volume threshold gets its own candidate record -- don't
   collapse multiple groups into one
7. A signal that doesn't match any mapped capability, seen more than once, isn't forced into
   a cluster -- log it as a build candidate instead
8. On a recurring cadence, refresh existing groups: update membership, budget, and window
   estimates, and archive any candidate whose window has closed without conversion

## Output

Cluster candidate records (group name, member entities, buyer identity, budget confirmation,
gap volume, window, status) ready for manual triage. No 0-100 fit score at this stage -- fit
is implied by starting from a confirmed capability.

## Rules

- Never score or contact individual entities within a group -- Chet writes clusters, not
  individual leads or events
- Don't re-derive dependency for a group whose existence is already documented
- Skip a paused or closed group entirely -- no re-mining, no discovery expansion
- Mine per qualifying group, not per individual event
