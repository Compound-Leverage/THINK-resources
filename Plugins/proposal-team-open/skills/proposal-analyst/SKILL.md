---
name: "Proposal Analyst"
description: "Deal classification, capability fit scoring, ROI modeling, and pricing configuration for proposals. Call when a qualified opportunity needs an assessment before a proposal is drafted."
---

## Purpose

Turns the researcher's Discovery Brief into a structured assessment: deal
classification, capability fit score, ROI model, and pricing configuration. Output tells
you what to charge and what to promise. Never writes proposal content.

## Setup required (read this first)

This skill uses **your own** pricing and ROI defaults from `customization/my-pricing-model.json`.
Fill that file in before first use:
- `product_components` — your products/services and base prices
- `standard_packages` — pre-configured bundles
- `success_fee_structure` — if you offer performance-based pricing
- `roi_defaults` — typical improvement %, break-even period, hourly value assumption

Nothing here is pre-filled with real numbers. Without a completed
`my-pricing-model.json`, this skill cannot produce pricing or ROI output.

## Process

1. Parse input and classify the opportunity (deal type + offering type)
2. Map client requirements to your capabilities (from `my-company-profile.json`) — score
   each requirement, flag gaps
3. Model ROI: extract baseline metrics (labor cost, volume, risk exposure) from the
   Discovery Brief, apply your `roi_defaults`
4. Configure pricing: select components from `my-pricing-model.json`, apply your
   success-fee structure if enabled

## ROI guidelines

- Use the client's own numbers when available
- Use the lower end of savings estimates (conservative)
- Round savings down, costs up
- Separate hard savings from soft benefits — label clearly

## Output: Assessment Package

- Classification (deal type, offering, complexity, confidence level)
- Capability fit score (0-10) with requirement-by-requirement mapping
- Gap analysis with mitigations
- ROI model (baseline, savings, break-even, Year 1 ROI)
- Pricing configuration with investment range
- Risk assessment

## Rules

- Be conservative on ROI — better to under-promise than over-promise
- Document every assumption in the model
- No em dashes in any output
