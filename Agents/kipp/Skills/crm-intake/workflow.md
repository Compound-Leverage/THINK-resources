# CRM Intake -- Workflow

Enrichment and ICP classification for every record entering your intake queues.
Load your filled-in config (`core/config.template.json`, copied) before running any
step below -- it defines your intake sources, ICP profiles, routing flags, and
enrichment provider.

## Step 1: Pull new records from each configured source

Run this against every source listed in `intake_sources.sources`. The shape is the
same regardless of source -- only where the record came from differs:

- **Signal inbox** -- new entries flagged for intake in whatever intelligence or
  signal-tracking database you run upstream of Kipp
- **Scored prospect list** -- records your own scoring process has already
  qualified and dropped into your pipeline with no linked contact yet
- **Warm inbound leads** -- referrals, conference contacts, or re-engagement records
  with no existing CRM record at all

## Step 2: Resolve the org domain

- Pull the website field from the source record if present
- Strip `https://`, `www.`, and trailing slashes
- If no website field: web search "[org name] official website" to find the domain

## Step 3: Check for an existing contact first

Query your Contacts database for a name + org match before doing any enrichment
lookup.
- Match found: skip enrichment, link the existing contact to the source record
- No match: proceed to Step 4

## Step 4: Enrichment lookup

Run your configured enrichment provider (see `integrations.md` for the lookup
pattern and fallback order):
- Domain lookup -> select best contact by seniority -> verify the email
- Confidence below `enrichment.confidence_threshold`: flag "Unverified -- confirm
  before send"
- Provider returns nothing: record name/title only if you have it from a web search,
  and note "No email found -- manual outreach needed"
- Rate limited: wait, retry once per `integrations.md`, then log and skip rather than
  blocking the rest of the sweep

## Step 5: Write CRM records and classify

- Create or update the Contacts record with the verified (or flagged) contact
- Create or update the linked Organizations record
- If the source was a pipeline/prospect record: link the contact as decision-maker
  and note the enrichment date
- Run ICP classification (see `rules.md`) against your `icp_profiles`
- Apply the routing flag your config maps to the matched profile
- If the matched profile's `enrichment_tier` is `deep`: run your configured
  `deep_enrichment_provider` and write the additional fields it returns (see
  `integrations.md`)

## Step 6: Unclassifiable records

If a record's signals don't clearly match any profile, don't leave it unflagged and
don't force the closest guess silently -- assign the closest match and apply your
`routing_flags.unresolved_flag`, then note which signals conflicted.

## Step 7: Periodic audit (stalled records)

On your `intake_sources.cadence` or a separate weekly pass -- whichever you prefer --
sweep your pipeline for any record that:
- Has been in your pipeline longer than `audit.stalled_after_days`, and
- Is still missing either a linked decision-maker contact or an ICP classification

Flag each one for manual review rather than re-running enrichment against it blind --
a record stalled this long usually means the enrichment lookup came back empty and
needs a human to find the contact another way, not another automated retry.

## Output
Contacts and Organizations records in your CRM, per the field list in `schema.md`.
Pipeline records updated with a linked decision-maker where applicable. An intake
report at the end of each sweep (base format in `Templates/kipp-crm-intake.md`; the
periodic audit produces its own log, extended format in `Agents/kipp/templates/`).
