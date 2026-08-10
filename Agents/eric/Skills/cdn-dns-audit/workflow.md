# CDN/DNS Audit -- Workflow

Reviews your CDN/hosting account config: hosting project settings, edge
functions/Workers, edge storage (KV/object storage equivalents), caching rules, and DNS
state, checking for drift from what your config expects.

## Step 1: Hosting project config

Use your provider's CLI/MCP to inspect your hosting project (`hosting` in your config):
- Production branch matches `branches.production_branch`
- Preview branches include your staging branch plus feature branches
- Build command and output directory match `build` in your config
- Environment variables: verify staging vs. production scoping
- Custom domains match `hosting.custom_domains`

## Step 2: Edge functions/Workers

Enumerate deployed edge functions/Workers on the account.

For each one:
- Name and purpose (infer from code if undocumented)
- Route assignment (which URLs it intercepts)
- Last modified date
- Is it referenced anywhere in your site repo or automation repo?

Flag: any edge function with no documented purpose, or last modified a long time ago
(90+ days is a reasonable default) with no active route.

## Step 3: Edge storage

List any KV namespaces, object storage buckets, or equivalents. For each:
- Is it actively used by an edge function or the site?
- Is it documented anywhere?

Flag anything undocumented or apparently unused.

## Step 4: Caching rules

Check cache rules configured at the account level (separate from your headers file):
- Are static assets (JS, CSS, images) getting edge-cached?
- Are HTML pages getting appropriate cache settings (short TTL or no-cache for dynamic
  content)?
- Any account-level rule overriding your headers file incorrectly?

## Step 5: DNS state

- Correct records pointing at your hosting provider (CNAME/A records as your provider
  requires)
- SSL/TLS certificate validity
- No dangling records pointing at a decommissioned target

## Step 6: Route findings

| Finding | Action |
|---|---|
| Wrong production branch | Notify -- requires a hosting-dashboard change only a human can make |
| Orphaned edge function (no route, no docs) | Notify -- confirm before anyone deletes it |
| Missing environment variable in production | Notify -- may break functionality, and env var changes always require a human |
| Cache misconfiguration fixable in your headers file | PR to staging |
| DNS record issue | Notify -- DNS changes always require a human |
| Structural CDN config issue | Notify with full analysis |

## Output
See `Templates/infrastructure-eric.md`'s Infra/Deploy Audit Report for the combined
output format this and the other audit skills share.
