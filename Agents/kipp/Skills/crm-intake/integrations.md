# CRM Intake -- Integrations

Bring your own enrichment provider. Hunter.io is used below as a worked example
because it's a common, affordable choice for domain-to-contact lookup -- swap in
whatever provider you've set in `enrichment.provider`.

## Standard enrichment (every record)

**Domain search** -- given an org domain, return likely contacts:
```
GET https://api.hunter.io/v2/domain-search
Params:
  domain:   org website domain (strip https/www)
  api_key:  [your enrichment.api_key_env_var value]
  limit:    5
```
Seniority priority when more than one contact returns: Executive Director >
President > CEO > Chief [any] > VP [any] > Director [any] -- adjust this order to
whatever seniority signals matter for your own ICP profiles.

**Email verifier** -- confirm a candidate email is live:
```
GET https://api.hunter.io/v2/email-verifier
Params:
  email:    candidate email from domain search
  api_key:  [your enrichment.api_key_env_var value]
```
Accept: status = "valid" or "accept_all". Reject: status = "invalid" -> treat as
not found.

**Email finder (fallback)** -- when domain search returns no usable contact but you
have a name from a web search:
```
GET https://api.hunter.io/v2/email-finder
Params:
  domain:       org website domain
  first_name:   from web search
  last_name:    from web search
  api_key:      [your enrichment.api_key_env_var value]
```

**Rate limit:** on HTTP 429, wait 60 seconds and retry once. If the retry fails: log
the error and skip contact creation for that record rather than blocking the rest of
the sweep. Note on the record: "[Provider] rate limit hit -- retry manually."

## Deep enrichment (only for profiles marked `enrichment_tier: deep`)

Run your configured `deep_enrichment_provider` (Clay is a common choice) only for
records classified into a profile your config marks for it. Pull whatever fields
matter for your own ICP -- common ones:
- Company size, headcount, LinkedIn URL
- Funding stage or recent funding events, if available
- Recent activity signals (hiring, expansion, new leadership)
- Any tool-stack or systems signal relevant to your own qualifying criteria

Write whatever fields you pull into the Organizations record's
`deep_enrichment_fields` (see `schema.md`). Log provider credits used if your
provider meters usage, so you can catch a low-balance condition before a sweep
silently comes back empty.

## CRM writes

See `schema.md` for the full field list. The write pattern is the same regardless of
provider or database -- create the Contacts record, create or update the
Organizations record, and (for a scored-prospect-list source) link the contact as
decision-maker on the pipeline record.
