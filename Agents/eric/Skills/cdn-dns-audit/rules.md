# CDN/DNS Audit -- Rules

- DNS record changes always route to a human -- never applied automatically, no
  exceptions
- Edge function/Worker create, modify, or delete always routes to a human for approval
  first
- Environment variable changes always route to a human -- never applied automatically
- Never delete an edge function or storage resource, even an apparently orphaned one --
  flag it, a human confirms and removes it
- Cache-header fixes that live in your own headers file (not the account-level CDN
  config) go out as a PR to staging
- No em dashes in any output
