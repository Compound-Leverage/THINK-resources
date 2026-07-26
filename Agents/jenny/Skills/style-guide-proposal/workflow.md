# Style Guide Proposal -- Workflow

Proposes additions or changes to your own style guide or brand guidelines when a
pattern is missing, broken, or needs to evolve. Routes the proposal to you for
approval before anything commits.

## When to trigger

- `Skills/web-spec-handoff/` needs a pattern that doesn't exist in your style guide
- `Skills/web-consistency-audit/` finds the same deviation recurring across
  multiple pages
- `Skills/brand-asset-audit/` finds the same violation recurring across multiple
  assets
- A brief explicitly requests a new design pattern

## What qualifies as a style-guide change

- A new component pattern
- A new copy rule
- An updated color, typography, or spacing convention
- A new page-type or surface-type template

## What does not qualify

- A one-off exception for a single page or asset
- A change that contradicts a rule you've already approved

## Output format

Post to your notification destination:

```
STYLE-GUIDE PROPOSAL
Section: [which part of your guide this affects]
Change: [what to add or update]
Reason: [why the current guide doesn't cover this]
Proposed text: [exact text to add]
-> Approve to commit, reject to drop
```

## Step: Route

Wait for your approval. On approval, commit the change to your own style guide or
config and, if it affects a live page, open a PR. On rejection, drop it, don't
re-propose the same change without new evidence.

## Output

A proposal posted for your approval. Nothing commits without it.
