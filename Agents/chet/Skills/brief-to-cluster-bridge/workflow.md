# Brief-to-Cluster Bridge -- Workflow

Use this when you already have an intelligence brief, market scan, or research report
sitting around and want cluster candidates out of it, instead of starting
`Skills/cluster-discovery/`'s scan from scratch. It's a bridge, not a duplicate scan --
it mines existing narrative content for the same kind of structured output
cluster-discovery produces.

## When to use
After receiving any brief-style document -- a funding or policy intelligence brief, a
sector scan, a weekly digest -- that might contain a named group carrying a capacity gap
your capability map covers.

## Process
1. Read the brief or scan output in full
2. Identify every named, bounded group mentioned -- a consortium, cohort, membership
   body, or similar -- filtering for groups where the brief states or clearly implies:
   - A shared capacity gap matching one of your capabilities
     (`core/config.template.json`)
   - Enough member entities to plausibly clear your `gap_volume_threshold`
3. Do not extract individual organizations or one-off entities from the brief -- if the
   brief only names single orgs with no bounded group structure, that's not a cluster
   candidate; leave it out rather than forcing a fit
4. For each qualifying group, mine what the brief provides directly: member entities (or
   a stated estimate), buyer identity, budget confirmation, and window estimate. Note
   explicitly what came directly from the brief versus what still needs confirming
5. Write each qualifying group as a Cluster Candidate Record (see
   `templates/brief-sourced-candidate.md` in this repo's `Agents/chet/templates/`),
   tagged with the source brief so it's traceable
6. Anything in the brief that looks promising but doesn't resolve to a named, bounded
   group: don't force it into a cluster record -- note it as worth a fresh
   `cluster-discovery` scan instead

## Output
Cluster Candidate Records, same base fields as `Skills/cluster-discovery/`, each
carrying a "sourced from: [brief name/date]" reference for traceability. No
individual-entity placement leads -- if the brief's content doesn't resolve to a bounded
group, this skill produces nothing for it.
