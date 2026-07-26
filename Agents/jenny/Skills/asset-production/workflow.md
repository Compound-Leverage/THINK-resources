# Asset Production -- Workflow

Brief intake through delivery for any recurring visual asset type: thumbnails,
social graphics, one-pagers, lead magnets, proposal visuals, or anything else you've
defined in `surfaces.types` in your own filled-in copy of
`core/config.template.json`.

Load your filled-in config before running any step below.

## Step 1: Intake and classify

Parse the brief for:
- **Surface**: match it against `surfaces.types` in your config. If it doesn't match
  any existing surface, that's a signal for `Skills/template-library/`, not a reason
  to invent a one-off spec here.
- **Content**: headline, subhead, body copy, CTA, key stat or number.
- **Deadline**: if none given, treat it as due the same session.

If the brief is missing surface or content, ask once. If it's still unclear, make a
reasonable assumption, flag it plainly in the delivery note, and ship rather than
stalling.

## Step 2: Pull the matching spec

Once the surface is classified, pull its dimensions, format, and notes straight from
`surfaces.types` in your config. Don't re-derive a spec that's already defined
there.

## Step 3: Apply brand constraints

Every asset gets checked against `brand` in your config before it goes anywhere:
- Accent color usage stays within `colors.accent_max_percent`, used only where your
  own config designates (headlines, stats, CTAs, whatever you've defined, never as a
  full background wash)
- Body copy and backgrounds use your configured `text_primary` and
  `neutral_backgrounds`
- Typography uses `typography.heading_font` / `typography.body_font` only, nothing
  from `typography.disallowed_fonts`
- Imagery follows your `imagery_policy` exactly (no stock photography is a common
  choice, but this is your call, not a fixed rule)
- Logo placement respects `logo.min_size_px` and `logo.clear_space_px`
- Copy inside the asset follows every rule in `voice_rules`, including no em dashes

## Step 4: Produce

Hand off to whatever actually renders the asset, your design tool (Canva or
equivalent, via MCP) or an HTML-to-image render pipeline, with a production brief
that states: surface, dimensions, format, exact copy to apply (don't paraphrase or
improve copy at this step), and the file name per `file_naming_convention` in your
config.

If you're running a multi-agent setup, Jenny writes the production brief and QAs
the result; whichever tool or sub-agent executes the render is not Jenny's job to
also be.

## Step 5: QA

Before delivery, confirm every item below. Do not deliver if any box is unchecked,
fix first:
- [ ] Accent color at or under `colors.accent_max_percent`, used only where
      designated
- [ ] Body copy and backgrounds match your configured colors
- [ ] Correct dimensions and format for the classified surface
- [ ] One CTA, benefit-led copy
- [ ] Copy follows every `voice_rules` entry, including no em dashes
- [ ] Logo sized and placed per `logo.min_size_px` / `logo.clear_space_px`
- [ ] Imagery matches your `imagery_policy`
- [ ] Typography uses only your configured fonts
- [ ] File named per `file_naming_convention`

## Step 6: Deliver

Save to your configured `tools.delivery_destination`. Post a delivery note to your
`notifications.destination` with: asset name and surface, file link, any assumptions
flagged in Step 1, and confirmation the QA checklist passed in full.

## Output

The produced asset at your delivery destination, plus a short delivery note. No raw
production log needed beyond that, the asset and its QA pass/fail is the record.
