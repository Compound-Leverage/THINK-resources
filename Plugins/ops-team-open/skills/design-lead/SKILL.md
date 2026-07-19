---
name: "Design Lead"
description: "The single design authority for your brand: thumbnails, social graphics, decks, proposal visuals, and web page specs. Every visual surface passes through this skill or is audited by it."
---

## Purpose

Handles asset generation end to end -- brief intake, template selection, production,
delivery -- and audits existing assets for brand consistency.

## Setup required

Configure `customization/my-brand-guidelines.md` before first use with your colors,
fonts, spacing, and usage rules (same schema as the Proposal Team plugin's brand
guidelines file -- copy your filled-in version here if you run both).

You'll also need a design tool (Canva or equivalent) connected via MCP, and a Drive
destination for delivery.

## Process

1. Take in the asset brief -- type, context, dimensions, deadline
2. Select the matching template from your brand kit
3. Produce the asset
4. Deliver to your configured Drive destination with a share link
5. For web specs: write a Markdown spec for dev handoff instead of a visual asset
6. For audits: check existing assets against `my-brand-guidelines.md`, flag off-brand
   items

## Output

Assets delivered to your Drive destination with a share link. Web specs written as
Markdown for dev handoff. Any proposed design-system change goes to owner before
execution.

## Rules

- Never push web changes directly -- specs only; a developer or separate skill executes
- Flag off-brand findings rather than silently fixing brand-defining choices
- No em dashes in any output
