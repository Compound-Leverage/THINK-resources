# Sales BD Team (sales-bd-team) — Example Prompts

Paste these into Claude after installing this plugin from the THINK School marketplace. Swap in your own systems, data, and files wherever you see a placeholder like "our CRM" or [prospect name].

Open-source 3-role BD team: Lead Scout sources intent signals, BD Research enriches and labels them, BD Execution scores and sends outreach.

### Lori — Lead Scout
- "Scan our configured signal sources (forums, event registrations, newsletter clicks) for people showing active demand signals that match our ICP, and give me the qualified leads with an intent score."
- "Apply our auto-exclude disqualifiers to this list of candidates and tell me which ones survive."
- "Write today's qualified leads to a CSV with name, org, signal source, and routing flag, the way we configured it."

### Alex — BD Research
- "Here are the raw candidates Lori sourced this week — enrich each one with company and contact data and label them against our ICP profiles."
- "Flag any record where you're missing a required field instead of guessing it, and write the completed ones to our pipeline and contacts databases."

### Sarah — BD Execution
- "Score these enriched leads against our ICP scoring dimensions, then draft an HTML outreach email for the top 5 using our company differentiators."
- "This is a new segment for us — hold the drafts for my approval before sending, per our approval gate."
- "Log the outreach activity from this batch into our CRM and apply our standard follow-up cadence."

