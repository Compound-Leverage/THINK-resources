# Template Library -- Rules

- Build every template from your own config's actual brand values, never invent a
  new color, font, or spacing rule at template time
- Version every template file, never overwrite a live template in place, ship the
  next version instead
- Document every template in `Agents/jenny/templates/` before marking it active
- Never mark a new template active without your explicit confirmation
- No em dashes in any output

## What this skill does not do
- Produce a one-off asset, that's `Skills/asset-production/`
- Decide a new brand value belongs in your config, propose that through
  `Skills/style-guide-proposal/` instead
