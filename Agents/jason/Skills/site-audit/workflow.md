# Site Audit -- Workflow

The technical half of Jason's audit surface: is the site discoverable, does it resolve
correctly, and is it up. Covers SEO hygiene, LLM/AI discoverability, redirects, broken
links, uptime, code-level performance patterns, a secondary-property audit (a newsletter
or blog platform, if you have one), and search console monitoring. Run the sections that
match your trigger -- see `hooks/hook-map.md` for which sections fire on which cadence.

## 1. SEO hygiene
Read-only pass across content pages. Check:
- `<title>` present and unique per page
- Meta description present and under `thresholds.meta_description_max_chars`
  (`core/config.template.json`)
- H1 present and unique per page (one per page, no more) -- coordinate with
  `Skills/content-qa/` rather than re-deriving H1 content rules here; this check is
  presence/uniqueness only
- No duplicate page titles across the site
- Canonical tags present where pages have query parameters

Does not judge whether title/description copy is good (a brand decision) or check
external backlinks.

## 2. LLM/AI discoverability
Static file checks, no network calls needed:
- `llms.txt` present at your site root
- `robots.txt` present and does not block known AI crawlers you want indexing you
- Meta description present and non-empty on content pages
- Structured data (`application/ld+json`) present on at least one block per content page
- OpenGraph tags (`og:title`, `og:description`, `og:url`) present on content pages
- Semantic heading structure -- single H1 per page, logical H2/H3 hierarchy
- No content locked behind JS-only render (H1 and meta present in static HTML, not
  injected client-side only)

## 3. Redirects
Read your redirects file (or hosting platform's redirect config) and verify each source
path resolves to an active destination. Flag:
- Source paths that no longer exist (redirect is unnecessary now)
- Destination paths that return 404 (dead destination)
- Redirect chains (A to B to C instead of A to C)

**Propose the fix per type, per your `routing` config:**
- Chain collapse, or removing an unnecessary entry: rule-based, hand off to
  `Skills/findings-routing/` for a PR
- Conflict (the source page's file still exists -- may have unique content) or dead
  destination (correct target may be ambiguous): judgment call, flag with your proposed
  best guess but do not act

## 4. Broken links
After your build/deploy completes, crawl the built site and check every internal link
and asset reference for 404s. Internal only -- external URL rot is out of scope for this
step (add it as a separate cadence if you want it).

## 5. Uptime
Parallel HTTP HEAD requests (not GET -- no need to download page bodies) against every
route derived from your site's page structure, excluding known non-200 utility pages
(error pages, legal pages) and API routes. Flag anything returning 4xx or 5xx; treat
3xx as informational, not a flag.

## 6. Performance patterns
Weekly read-only pass for known code-level Core Web Vitals risks -- this does not run a
Lighthouse audit, it flags patterns a developer can act on directly:
- Images missing `width`/`height` attributes (layout shift risk)
- Images not using your framework's optimized image component, if it has one
- Render-blocking `<script>` tags in `<head>` without `defer` or `async`
- Large inline `<style>` blocks that could be extracted
- Fonts loaded without `font-display: swap`

## 7. Secondary property audit
If you configured a `site.secondary_properties` entry (a newsletter or blog platform),
run a lighter version of sections 1-2 against it:
- Site-level: accessible (200), `robots.txt` doesn't block AI crawlers, sitemap present,
  custom domain active (not defaulting to the platform's own subdomain)
- Post-level, sampled per `thresholds.secondary_property_sample_size` and
  `secondary_property_sample_days` (default: 10 most recent posts, plus anything
  published in the last 7 days -- don't re-audit the full archive every run): title
  present, preview/subtitle text present, title follows your H1 standard, no em dashes,
  thumbnail/OG image set, canonical URL correct

## 8. Search console monitor
Read your search console's notification emails (or check its dashboard/API directly).
For each new issue:

| Issue type | Route to |
|---|---|
| Redirect errors or chains | Section 3 above |
| Pages not indexed / coverage issues | Coverage check (below) |
| Crawl anomalies | Coverage check (below) |
| Core Web Vitals | Section 6 above |
| Mobile usability | Flag for manual review -- cannot be auto-resolved |
| Manual action | Flag for manual review -- cannot be auto-resolved |
| Enhancement / structured data | Section 2 above |

**Coverage check:** for not-indexed and coverage issues, search console notifications
typically list issue types but not every affected URL. Check each content page for a
`noindex` tag that shouldn't be there, a canonical tag pointing somewhere unexpected, or
exclusion from your sitemap that shouldn't apply -- flag any of the three.

## Output
Findings per section, each citing the exact page, path, or file. Pass everything to
`Skills/findings-routing/`, which sorts rule-based fixes into PRs and everything else
into flags for your review.
