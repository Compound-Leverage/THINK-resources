---
name: kipp-crm-intake
description: "Enriches incoming org and contact records, classifies each by your ICP profile, and creates or updates CRM entries. Processes new inbound leads, intelligence inbox entries, and prospect lists."
---

## Purpose

Runs a daily (or on-demand) sweep of new inbound and unlinked prospect records, enriches
each one, classifies it against your ICP, and writes clean, scored contacts into your
CRM.

## Setup required

Configure `customization/my-capture-config.json` before first use:
- `icp_profiles` -- your classification criteria
- `routing_flags` -- how classified records get flagged
- `notion.*_db_id` -- your Contacts, Orgs, and Deals Pipeline database IDs
- `enrichment.provider` and `enrichment.api_key_env_var` -- your enrichment tool

## Process

1. Pull new records from your inbound queue (intelligence inbox entries, unlinked
   pipeline prospects, warm inbound leads)
2. Enrich each via your configured provider
3. Classify against `icp_profiles`, apply the matching `routing_flags` value
4. Create or update the Contacts and Orgs records; link to Deals Pipeline where
   applicable
5. Produce an intake report summarizing the sweep

## Output

Contacts and Organizations records in your CRM. Deals Pipeline updated with
decision-maker links. Intake report at the end of each sweep.

## Rules

- Never overwrite an existing manually-edited field with an enrichment guess -- flag
  the conflict instead
- Every record gets a routing flag -- nothing is left unclassified
- No em dashes in any output
