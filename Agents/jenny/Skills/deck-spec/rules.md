# Deck Spec -- Rules

- Output is a brief only, never a built PPTX, PDF, or slide file, that's a separate
  build step
- Use only the accent-color roles you fixed for yourself in Step 2 of `workflow.md`,
  don't introduce a new role per deck
- Every slide needs a section tag and footer, no exceptions
- Keep headlines short, two lines is a reasonable ceiling, and keep body copy under
  your own per-slide word ceiling
- Exactly one call to action, on the CTA slide only, never scattered across multiple
  slides
- No em dashes in any output

## What this skill does not do
- Build the actual deck file, a separate build step (a coworking session, a build
  agent, a human) takes the brief from here
- Decide a new visual system for decks on the fly, pick your system once in your own
  reference and reuse it every time, propose changes through
  `Skills/style-guide-proposal/` if it needs to evolve
