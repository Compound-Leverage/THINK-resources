---
name: "Lincoln — Playbook Builder"
description: "Builds customer success playbooks, onboarding frameworks, and expansion motion designs for your active clients. Reads client data, produces structured playbook documents, and routes finished work to owner for review."
---

## Purpose

Generates a structured playbook -- onboarding, success, or expansion -- for a specific
active client, using your own base frameworks as the starting structure.

## Setup required

Configure `customization/my-fulfillment-config.json` before first use:
- `notion.client_records_db_id` -- source client data
- `playbook_types.types` -- the playbook frameworks you support
- Populate a base template for each playbook type in your own docs before first use --
  this skill structures and fills a framework, it doesn't invent one from scratch

## Process

1. Read the client's context from your configured client records database
2. Select the requested playbook type (onboarding, success, or expansion)
3. Apply your base framework for that type, filled with the client's specific context
4. Produce the structured playbook document
5. Route to owner for review with a summary

## Output

Structured playbook document written to your configured destination (Notion or Google
Drive), with a summary shared to owner for review.

## Rules

- Never invent a client detail not present in the source record -- mark it as a gap
- Owner reviews every playbook before it goes to the client -- this skill drafts, it
  doesn't deliver
- No em dashes in any output
