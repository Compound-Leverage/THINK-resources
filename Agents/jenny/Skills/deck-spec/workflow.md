# Deck Spec -- Workflow

Produces a full presentation/deck brief, every slide, all copy, layout pattern, and
color assignment, formatted for pasting into whatever builds the deck (a build agent,
a coworking session, a human designer). Jenny specs the whole deck, she doesn't
build the file herself.

## Step 1: Read the brief

Audience, purpose (present / workshop / training / sell), desired outcome, and any
existing content to fold in.

## Step 2: Pull your own deck visual system

Read your own deck color, type, and layout rules (wherever you've defined them,
alongside `brand` in your config if you keep one system for both web and decks, or a
separate deck-specific system if your decks intentionally look different from your
site). Common choices worth deciding once and reusing every time:
- Canvas size and aspect ratio
- Background treatment (light or dark, and whether it differs from your web brand)
- A small, fixed set of accent colors with a role each (e.g. one for primary labels,
  one for a secondary label, one for a tertiary label, one for de-emphasis), don't
  invent new roles per deck
- Section-tag and footer treatment repeated on every slide
- A consistent bullet or marker style for positive versus negative points

## Step 3: Determine slide count and map the act structure

10-18 slides is a reasonable range for most decks. A structure that works across
most persuasive or training decks:

Cover -> Problem/challenge -> Framework or how-it-works -> Core content (repeat as
needed) -> Demo or proof -> Call to action -> Close.

## Step 4: Apply slide layout patterns

These are structural patterns, not brand-specific, adapt the copy and color
assignment to your own system from Step 2:

**Cover slide** -- section tag naming the audience/occasion, large two-line
headline, a subtitle, a tagline or presenter credit, footer.

**Problem/challenge slide** -- section tag "the problem," a headline contrasting
status quo against your alternative, two or three problem cards (label + body),
footer.

**How it works / numbered steps** -- section tag, headline stating the number of
steps and the outcome, one card per step with a number, title, and body, each step
using its own accent color per your fixed role assignment from Step 2.

**Step detail slide** -- section tag naming the step, a question or outcome
headline, two content blocks (what the audience does or sees, plus an example),
footer.

**Comparison slide (before/after)** -- section tag, a contrast headline, two
columns, one for the status quo (de-emphasized styling, negative-marker bullets),
one for the outcome state (full-emphasis styling, positive-marker bullets), footer.

**Demo/live slide** -- section tag marking it as a live moment, a headline stating
what the audience will see, a bullet list of what to watch for, footer.

**Call-to-action slide** -- section tag, a direct headline, one action block (offer,
description, and a single next step), footer stating this is an assessment of fit,
not a hard sell, if that matches your own positioning.

**Closing slide** -- no section tag, one large closing statement in your own voice,
your URL, an optional secondary CTA.

## Step 5: Write every slide

Section tag, headline (aim for two lines, keep total headline word count low),
every content block, and the color/role assignment per slide, using only the roles
fixed in Step 2.

## Step 6: Apply QA

Every slide has a section tag and footer. No slide exceeds a reasonable body-copy
length (80 words is a workable ceiling). The CTA slide has exactly one action. No em
dashes anywhere in the deck's copy.

## Step 7: Output the brief

```
DECK BRIEF -- [Deck Title]
Audience: [who]
Purpose: [present / workshop / training / sell]
Slide count: [n]
Visual system: [pointer to your own deck color/type/layout rules from Step 2]

SLIDES:

[SLIDE 1]
Layout: [pattern name from Step 4]
Section tag: [text]
Headline: [line 1] / [line 2]
Content:
  [LABEL]: [body text]
  [LABEL]: [body text]
Footer: [your standard footer text]

[SLIDE 2]
...
```

Post the brief to your configured notification destination, or hand it directly to
whatever builds the deck.

## Output

A slide-by-slide Markdown brief. No PPTX, PDF, or slide file produced by this skill
itself, that's a separate build step.
