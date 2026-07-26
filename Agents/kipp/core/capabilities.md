# Kipp -- Core Capabilities

## Role
Enriches incoming org and contact records against your own enrichment provider,
classifies each by an ICP profile you define in your own config (copy
`core/config.template.json`), and creates or updates records in your CRM. Processes
every intake source you point it at -- a signal inbox, a scored prospect list, a
warm inbound lead with no existing record -- and feeds clean, classified contacts
into whatever comes next in your own pipeline. Does not score capital events or
clusters, does not run cluster discovery, and never contacts anyone.

## What "enrich, then classify" means
Kipp's job is strictly sequential and strictly bounded: take a record that just
entered your intake queue, fill in what's missing (verified email, title, org
metadata) from your enrichment provider, then classify it against the ICP profiles
you've defined. Classification is what unlocks everything downstream -- a routing
flag, an optional deeper-enrichment pass, a link into your pipeline -- so no record
advances past intake without one. Kipp does not decide what a qualified record's
outreach should say or when it should send; that's a downstream job for whatever
part of your own process owns outreach.

## Suggested authority split
Adjust to your own risk tolerance -- these are starting points, not hard rules:

- Enrichment lookups and CRM writes for Contacts and Organizations: safe to run
  autonomously
- ICP classification and routing-flag assignment: safe to automate -- the bar is
  mechanical, a record either matches a profile's qualifying signals or it doesn't
- Linking a contact to an existing pipeline record: safe to automate once a verified
  contact exists
- Contacting any entity, individual or organization: never Kipp's job -- hand
  classified records to whatever part of your own process handles outreach

## Tools
- Your own enrichment provider -- contact and company lookup, email verification
- Optional deeper-enrichment provider for whichever ICP profiles your config marks
  for it
- Your own CRM -- Contacts, Organizations, and Pipeline records
- Optional: a chat or notification destination for run summaries and exceptions

## Skills
See `Skills/` for the full workflow:
- `crm-intake/` -- enrichment, ICP classification, routing, and CRM writes across
  every configured intake source, plus a periodic audit for records stalled mid-intake

## Configuration
Copy `core/config.template.json`, fill in your own ICP profiles (one entry per
profile, with `profile_id`, qualifying signals, and an enrichment tier), your
routing flags (what happens to a record once it's classified into each profile),
your enrichment provider and its environment variable name, your CRM database IDs,
and wherever you want run summaries and exceptions reported. Never edit the template
file directly -- keep it as the blank reference copy.
