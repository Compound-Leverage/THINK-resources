# CRM Intake -- Rules

## ICP classification

Classify every record before it advances -- no record skips this step. The
qualification question is whatever your own `icp_profiles.qualifying_signals`
define for each profile; Kipp doesn't invent criteria beyond what your config states.

- A record matching a profile's `qualifying_signals`: classify into that profile,
  apply the matching `routing_flags` value
- Signals conflicting or insufficient to confidently pick one profile: assign the
  closest match and apply `routing_flags.unresolved_flag`, noting which signals
  conflicted
- Never leave a record unclassified -- the closest-match-plus-flag path always
  applies when a clean match isn't available

## Constraints

1. No cold outreach -- Kipp enriches and classifies records only; whoever owns
   outreach in your own process approves and sends, not Kipp
2. No guessed emails -- only provider-verified addresses, or an explicit "no email
   found" flag
3. Confidence threshold -- flag any contact below `enrichment.confidence_threshold`
   as "Unverified -- confirm before send"
4. No duplicate contacts -- check name + org before every create
5. Enrichment provider API keys from environment only -- never hardcode credentials
   or paste a live key into any file you commit
6. Your CRM is the source of truth -- if a contact already exists, link and move on,
   don't re-enrich or overwrite a manually-edited field with an enrichment guess;
   flag the conflict instead
7. Every record gets a routing flag -- nothing advances without one
8. Deeper enrichment (your `deep_enrichment_provider`) only runs for profiles marked
   `enrichment_tier: deep` in your config -- don't run it against every record by
   default, it's there for the profiles that need it
9. No em dashes in any output

## What this skill does not do
- Score capital events, clusters, or signals -- that happens upstream, before a
  record reaches Kipp's intake queues (your own scoring process, or
  `Skills/mandate-mapping` / `Skills/community-grant-radar` if you're using those
  for signal sourcing)
- Send anything, to anyone, at any point
- Decide what a qualified record's outreach should say -- that's a downstream job
