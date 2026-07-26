# Template Library -- Workflow

When a recurring asset type is identified, build a master template, version it,
document it, and add it to your own template library. Future production runs for
that surface use the template instead of being built from scratch each time.

## When to trigger

- A surface is being produced for the second time with no existing template for it
- You explicitly request a template for a new recurring asset
- `Skills/brand-asset-audit/` surfaces a pattern that should be standardized

## Step 1: Build the template

Apply your full brand spec from `core/config.template.json`. The template should
include:
- Correct dimensions for the surface, per `surfaces.types` in your config
- Color token references, not hardcoded values
- Font token references
- Grid and margin guides
- Placeholder copy following your `voice_rules`
- A CTA placeholder noting its intended destination
- Locked logo placement, sized and spaced per `logo` in your config

## Step 2: Version

File name per your own `file_naming_convention`, with a version suffix (`_v1`,
`_v2`, and so on).

## Step 3: Document

Create `Agents/jenny/templates/[template-name].md` (see
`templates/template-documentation.md` in this repo's `Agents/jenny/templates/` for
the format) describing the surface, its dimensions, when to use it and when not to,
which zones are editable, and which zones are locked.

## Step 4: Save and confirm

1. Save the template file itself to your configured design tool or delivery
   destination
2. Save the documentation file to `Agents/jenny/templates/`
3. Post to your notification destination: `TEMPLATE DROP -- [surface name] -- v1
   ready for review`, with a link
4. Wait for your confirmation before marking it active in the library, don't mark it
   active unilaterally

## Output

A versioned template file plus a documentation file in `Agents/jenny/templates/`.
Not active until you confirm it.
