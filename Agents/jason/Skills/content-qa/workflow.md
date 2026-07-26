# Content QA -- Workflow

Checks what your pages say: page type, headline standard, and terminology consistency.
Load your filled-in site standards file (`standards.site_standards_path` in
`core/config.template.json`) before running any step below -- every check here tests
against your own rules, not a fixed one this skill invents.

## Step 1: Classify every page
Tag each page as one of two types, using `page_types.product_patterns` and
`page_types.utility_patterns` in your config:
- **Product** -- a product, lead-gen, or offer page. The visitor is being moved toward
  an action or outcome.
- **Utility** -- a reference, tool, onboarding, or resource page. The visitor is being
  served a function they already decided to use.

When ambiguous, ask: is this page trying to get the visitor to do something, or is it
helping a visitor who already decided to do something? Former is product, latter is
utility. Skip anything matching `page_types.excluded_patterns` (privacy, terms, error
pages, editorial content where a word-count or headline convention doesn't apply).

This classification feeds every other step below -- run it first.

## Step 2: H1 audit
Read each page's H1 and test it against your site standards' H1 rule, applying the rule
for its page type from Step 1:
- **Product pages** -- outcome-driven. The H1 states the outcome or consequence the
  visitor cares about. Flag if it describes a process ("Discover," "Learn," "Get
  started"), asks a question, or names a thing without saying why it matters to the
  visitor.
- **Utility pages** -- descriptive label. The H1 accurately names the page. Flag if it
  uses filler ("Here is where to," "What is a"), asks a question when a label would
  serve, or uses process language instead of naming the thing directly.

## Step 3: Propose replacements for every H1 flag
For each flagged page, read its subhead (or first supporting line under the H1) and its
page type from Step 1, then propose replacement H1 options:
- **Product pages** -- propose 2 options
- **Utility pages** -- propose 1 option (there is usually one right answer)

Do not rewrite the page's value proposition, tone, audience, or offer -- work with the
existing direction. Do not propose copy that contradicts the subhead.

## Step 4: Copy consistency
Scan page copy against your site standards' terminology table and any documented brand
voice rules (CTA text and destination, banned words or phrasing, no em dashes). Flag
copy that contradicts an approved line without an intentional, documented change. This
step does not judge whether new copy (with no approved equivalent to compare against) is
good -- that's a brand decision, not this skill's call.

## Output
Findings per page: classification, H1 verdict, proposed replacement options (if
flagged), and copy-consistency flags. Pass everything to `Skills/findings-routing/`.
