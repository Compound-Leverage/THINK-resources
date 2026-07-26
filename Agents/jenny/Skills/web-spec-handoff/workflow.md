# Web Spec Handoff -- Workflow

Produces a design spec for a page or component on your own site. Jenny reads the
brief and your own codebase, then outputs a spec for whatever builds it, Claude
Code, a developer, or another agent. Jenny never writes the code herself and never
pushes to your site's repo.

## Step 1: Read before speccing

Before writing anything:
1. Read your own site's style guide or design-system file
   (`web.style_guide_path` in your config)
2. Read two or three existing pages of the same type, for pattern and tone
3. Read your own token/config file (Tailwind config, CSS variables, whatever you
   use) for available classes and values
4. Read your own components folder (`web.component_library_path` in your config) for
   existing reusable components

## Step 2: Spec output format

```
PAGE SPEC -- [page slug]
Date: [date]
Brief: [one-line summary of what this page is]

FILE PATH
[path in your repo]

PAGE TYPE
[product / utility / landing / component]

DIMENSIONS / LAYOUT
[viewport behavior, max-width, grid, padding]

SECTIONS
1. [Section name]
   - Component: [existing component name, or "new pattern -- see below"]
   - Copy: [headline / body / CTA text as it should appear]
   - Color tokens: [from your own config]
   - Typography tokens: [from your own config]
   - Notes: [anything non-obvious]

2. [repeat per section]

CTA
- Text: [exact button text]
- Destination: [path]
- Style: [existing class reference]

COMPONENTS TO REUSE
- [component name] -- used for [section]

NEW PATTERNS NEEDED
- [Only list if nothing equivalent exists. Propose the pattern and flag it for
  approval via Skills/style-guide-proposal/ before anyone builds it.]

QA CHECKLIST FOR THE RESULTING PR
- [ ] Accent color usage matches your config's max-percent rule
- [ ] Body copy and backgrounds match your configured colors
- [ ] No inline styles outside your own design system's documented exceptions
- [ ] One CTA on the page, correct destination
- [ ] No em dashes in copy
- [ ] Imagery matches your imagery policy
- [ ] Logo placement and sizing correct, if applicable
```

## Step 3: Handoff

Post the spec to your configured notification destination, labeled `WEB SPEC --
[page slug] -- ready to build`.

After the build step opens a PR: run `Skills/web-consistency-audit/` on the diff
before merge, and post the result to your notification destination.

## Output

A Markdown spec, handed off for someone or something else to implement. No code,
ever, from this skill.
