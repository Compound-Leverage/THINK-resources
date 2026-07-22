# Ops Team (ops-team-open) — Example Prompts

Paste these into Claude after installing this plugin from the THINK School marketplace. Swap in your own systems, data, and files wherever you see a placeholder like "our CRM" or [prospect name].

Open-source 3-role site ops team: QA Reviewer audits deploys, Design Lead handles brand-consistent visual assets and web specs, Infra Lead owns the build pipeline, DNS, and CDN.

### Eric — Infra Lead
- "Audit our latest deploy against our performance thresholds and caching rules, and open a PR to staging for any config-only fixes you find."
- "Check our GitHub Actions for failures or drift, and tell me what needs my sign-off before it touches production."

### Jason — QA Reviewer
- "Run a post-deploy audit of our site — H1 consistency, SEO, our copy terminology table, and broken links — then open PRs for anything rule-based and flag judgment calls to me."
- "Cite the exact page and section for every finding, and give me a changelog of what you fixed."

### Jenny — Design Lead
- "Here's the brief: I need a social graphic for [campaign name], sized for LinkedIn and Instagram. Use our brand guidelines and deliver it to our Drive folder with a share link."
- "Audit our last 5 marketing assets against our brand guidelines and flag anything off-brand instead of silently fixing it."

