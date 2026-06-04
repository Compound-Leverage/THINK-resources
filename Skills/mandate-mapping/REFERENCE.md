# Mandate Search Agent - Detailed Reference Guide

This file contains detailed workflow steps, intelligence signals, best practices, and implementation guidance for the Mandate Search Agent Skill.

---

## How This Skill Works (Interactive Web Search)

### Understanding the Search Process

**This is NOT an automated monitoring system.** This is an interactive, on-demand skill where:

1. **You initiate the search** by asking Claude (e.g., "Search for funding opportunities in California")
2. **Claude uses web search tools** to query relevant websites in real-time
3. **Results are analyzed and scored** based on your CONFIG.md
4. **Claude presents findings** with intelligence briefs and recommendations

### Claude's Web Search Capabilities

When you ask Claude to search, it uses these built-in tools:

**WebSearch Tool:**
- Performs web searches across the internet
- Finds recent announcements, press releases, RFPs
- Searches government websites, Grants.gov, agency sites
- Returns current, up-to-date information

**WebFetch Tool:**
- Retrieves content from specific URLs you provide
- Analyzes grant announcements, legislation, agency pages
- Extracts details like funding amounts, deadlines, requirements

**No Background Automation:**
- This skill does NOT run continuously in the background
- It does NOT automatically scrape websites or monitor sources
- It does NOT use actors, bots, or automated data collection
- Each search is interactive and initiated by you

### Typical Search Flow

**User:** "Search for workforce AI funding in Texas"

**Claude:**
1. Reads your CONFIG.md (knows you're in Texas, your keywords, thresholds)
2. Uses WebSearch to query:
   - "Texas workforce development AI grants 2025"
   - "Texas economic development automation funding"
   - "Grants.gov Texas workforce AI"
3. Fetches top results using WebFetch to get details
4. Filters results by your configured criteria
5. Scores each opportunity (0-100)
6. Presents findings with routing tags and intelligence briefs

**This happens in real-time during your conversation with Claude.**

---

## Detailed Workflow Steps

### Step 1: User-Initiated Search Execution

**When you request a search:**
1. Claude reads your CONFIG.md to understand preferences
2. Constructs web search queries using your keywords + geography
3. Uses WebSearch tool to find opportunities
4. Captures URLs, titles, descriptions, dates from search results
5. Uses WebFetch to retrieve full details from promising results

### Step 2: Initial Filtering

**Include if:**
- Mentions workforce, training, skills, or economic development
- Contains AI, automation, digital transformation, or technology keywords
- Has funding component or appropriation language
- Located in or applicable to target regions

**Exclude if:**
- Pure research grants (no training/workforce component)
- Healthcare-specific (unless workforce training)
- K-12 education only (unless workforce pipeline)
- Infrastructure-only (no human capital component)
- Completely out of region with no federal/regional option

### Step 3: Opportunity Scoring (Detailed)

For each qualifying opportunity:
1. **Assign funding size points (0-40)**
   - $100,000 or more → 40 points
   - $50,000 - $99,999 → 30 points
   - $25,000 - $49,999 → 20 points
   - Under $25,000 → 10 points

2. **Calculate timeline points (0-20)**
   - 6-12 months to deadline → 20 points (optimal positioning window)
   - 3-6 months → 15 points (still actionable)
   - Under 3 months → 10 points (rushed timeline)
   - Over 12 months → 5 points (too early, monitor only)

3. **Assess competition level (0-20)**
   - Unsolicited opportunity (no formal RFP) → 20 points
   - Limited competition/invitation only → 15 points
   - Set-aside or preference program → 10 points
   - Open competition RFP → 5 points

4. **Evaluate geography match (0-20)**
   - Target region (DE, PA, MD, VA, DC) → 20 points
   - Adjacent region with spillover potential → 10 points
   - Federal program available in target regions → 5 points
   - Out of region with no local component → 0 points

5. Generate total score (0-100)
6. Document score breakdown in JSON format

### Step 4: Routing Tag Assignment (Detailed)

**white-paper-ready (Score 80+, Pre-funding stage)**
- **Characteristics:** Legislative signal or agency planning stage, no formal RFP yet, funding appropriated or in budget proposal
- **Action Required:** Draft thought leadership white paper
- **Timeline:** Position within 30 days
- **Goal:** Establish thought leadership before competition emerges
- **Deliverable:** White paper with specific angle addressing opportunity

**proposal-ready (Score 70+, Active RFP)**
- **Characteristics:** Formal solicitation published, clear submission requirements, deadline within 3-6 months
- **Action Required:** Develop full proposal response
- **Timeline:** Respond within RFP timeline
- **Goal:** Submit competitive proposal by deadline
- **Deliverable:** Complete proposal package per RFP requirements

**nurture-needed (Score 50-69)**
- **Characteristics:** Moderate potential but barriers exist, may need partnerships or capacity building, timeline unclear or funding uncertain
- **Action Required:** Relationship building, information gathering
- **Timeline:** Quarterly check-ins
- **Goal:** Build relationships and capacity for future pursuit
- **Deliverable:** Stakeholder engagement plan and partnership development

**monitor-only (Score <50)**
- **Characteristics:** Low priority or poor fit, funding too small or timeline problematic
- **Action Required:** Save to database, no active follow-up
- **Timeline:** Passive monitoring only
- **Goal:** Maintain awareness in case circumstances change
- **Deliverable:** Archive record in database

### Step 5: Intelligence Brief Generation (Detailed)

**Trigger Intelligence Brief for:**
- Any opportunity scoring 70 or higher
- Funding amount exceeds $500,000
- Unsolicited opportunity (pre-RFP stage)
- Multi-year program potential
- Strategic regional initiative (multi-state or flagship program)

**Intelligence Brief Must Include:**
1. **Opportunity Summary:** 2-3 sentences covering what, who, when, how much
2. **Score Breakdown:** Table showing points awarded in each category with rationale
3. **White Paper Angle or Proposal Strategy:** Specific positioning recommendation
4. **Target Organizations:** Agencies, workforce boards, decision makers
5. **Similar Past Awards:** Precedents if known
6. **Recommended Next Actions:** Specific tasks with owners and deadlines
7. **Partnership Opportunities:** Required or recommended partners
8. **Risk Factors:** Barriers, challenges, or red flags

### Step 6: Reporting Formats

**Daily Alert (If Applicable):**
- Trigger: Score 85+ or urgent deadline
- Content: Opportunity ID, title, score, routing tag, quick-hit action items
- Format: Brief text alert with link to full intelligence brief
- Delivery: Immediate notification

**Weekly Digest:**
- Content: All opportunities found that week, sorted by score
- Includes: Summary statistics, top 5 opportunities with descriptions, status updates
- Format: Structured markdown report
- Delivery: End of week (Friday)

**Monthly Intelligence Report:**
- Content: Trend analysis, regional comparison, success tracking, recommendations
- Includes: Charts/tables showing patterns over time
- Format: Comprehensive markdown report
- Delivery: First week of following month

---

## Key Intelligence Signals (Detailed)

### Pre-Funding Legislative Signals

**High Priority:**
- **Bill introduced with appropriation language:** New legislation allocating specific funding amounts
- **Budget proposal with new line item:** Governor or legislature proposes new funding category
- **Committee hearing on workforce/AI topic:** Legislative attention to relevant issues
- **Agency testimony requesting new program funding:** State agencies advocating for resources
- **Legislative study commission findings:** Research recommendations for new programs
- **Governor's budget address mentions:** Executive priority statements

**What to Look For:**
- Language like "appropriates $X for," "establishes program," "directs agency to"
- Bill status: Introduced, in committee, passed committee (increasing likelihood)
- Sponsors: Bipartisan, leadership, committee chairs (increasing probability)
- Timing: Budget cycle season, election year considerations

**How to Track:**
- Daily checks of state legislature bill trackers
- Weekly review of committee calendars
- Subscribe to bill status alerts for relevant committees
- Monitor fiscal notes showing funding estimates

### Agency Planning Signals

**High Priority:**
- **Strategic plan released with unfunded priorities:** Agency roadmaps awaiting resources
- **RFI (Request for Information) published:** Pre-solicitation market research
- **Listening sessions or stakeholder meetings announced:** Pre-program design engagement
- **New office or division created:** Organizational capacity for new initiatives
- **Federal grant awarded to state agency:** Sub-grant opportunities forthcoming
- **Workforce board priority area designation:** Policy direction for future funding

**What to Look For:**
- Plans with specific initiatives but "pending funding" or "subject to appropriation"
- RFIs that signal upcoming RFP but requirements not yet set
- Meeting announcements seeking input on program design
- Press releases about new agency structure or leadership
- Federal awards requiring state match or sub-awards
- Board resolutions designating priority industries or populations

**How to Track:**
- Weekly review of agency websites and announcements
- Attend or monitor workforce board meetings
- Subscribe to federal grant award RSS feeds
- Review agency strategic plans and annual reports
- Follow agency leadership on social media for policy signals

### Expiring Appropriation Signals

**High Priority:**
- **Auditor reports on unspent funds:** Appropriations not fully utilized
- **End-of-fiscal-year spending authority:** "Use it or lose it" deadlines
- **Grant programs with low application rates:** Undersubscribed opportunities
- **Pilot programs being evaluated for continuation:** Expansion possibilities
- **Reversion of funds warnings:** Agencies rushing to obligate before deadline

**What to Look For:**
- Comptroller or auditor reports showing lapsed appropriations
- Agency announcements of expedited timelines or rolling deadlines
- Legislative oversight hearings on underutilized programs
- Program evaluations with positive findings and expansion recommendations
- End of fiscal year (June 30 for most states) timing

**How to Track:**
- Quarterly review of auditor/comptroller reports
- Monitor end-of-fiscal-year (April-June) agency behavior
- Check program websites for application rate data
- Subscribe to evaluation report releases
- Track multi-year appropriation spend-down schedules

---

## Search Sources (Detailed)

### Primary Sources (Check Daily)

**1. Grants.gov**
- URL: grants.gov
- Search filters: Workforce development, AI training, economic development keywords
- Agency filters: DOL, EDA, NSF, DOE, DOC, SBA
- Geographic filters: State eligibility requirements
- Best practice: Set up saved searches with email alerts

**2. State Legislature Trackers**
- Delaware: legis.delaware.gov
- Maryland: mgaleg.maryland.gov
- Pennsylvania: legis.state.pa.us
- Virginia: lis.virginia.gov
- DC: dccouncil.gov/legislative-information
- Search terms: Workforce, training, economic development, appropriation, AI, automation

**3. Governor/State Executive Offices**
- Search press release pages daily
- Focus on: Budget proposals, executive orders, policy initiatives
- Subscribe to press release email lists
- Monitor State of the State addresses (January typically)

**4. State Workforce Boards**
- Check meeting calendars and agendas
- Review posted minutes for funding discussions
- Monitor strategic plan updates
- Track performance reports for priority areas

**5. Regional Economic Development Authorities**
- EDA regional office announcements
- State commerce/economic development departments
- Regional planning councils
- Local economic development organizations

### Secondary Sources (Check Weekly)

**State Budget Hearings**
- Legislative calendar for appropriations committee hearings
- Agency budget testimony (usually posted online)
- Fiscal notes on pending legislation
- Budget analysis documents from legislative services

**Agency Testimony Documents**
- Department of Labor testimony to legislatures
- Economic development agency reports
- Workforce board recommendations
- Education agency workforce initiatives

**Comptroller/Auditor Reports**
- Quarterly revenue reports
- Annual audits of agencies
- Performance audits of programs
- Reports on lapsed or unused appropriations

**Federal Register**
- New regulations impacting workforce programs
- Agency notices of upcoming funding opportunities
- Program evaluation requirements
- State plan approval notices

**Congressional Delegation Announcements**
- Senators' and Representatives' press releases about federal grants
- Announcements of earmarks or directed funding
- Regional economic development initiatives
- Letters to federal agencies supporting state/local projects

---

## Strategic Priorities

### White Paper Development Focus

When opportunity is tagged "white-paper-ready," recommend specific angles:

**1. Skills-to-Jobs Gap**
- **Theme:** Bridging disconnect between training and employer needs
- **Audience:** Workforce boards, economic development agencies
- **Key points:** Demand-driven training, employer partnerships, credential alignment
- **Data to include:** Regional labor market analysis, skills gap studies

**2. AI Displacement Response**
- **Theme:** Proactive retraining before job loss occurs
- **Audience:** State labor departments, legislative committees
- **Key points:** Early warning systems, rapid response, incumbent worker training
- **Data to include:** Automation risk analysis, occupational trends

**3. Regional Industry Focus**
- **Theme:** Sector-specific workforce strategies (manufacturing, healthcare, tech)
- **Audience:** Industry associations, sector partnerships
- **Key points:** Customized curriculum, stackable credentials, career pathways
- **Data to include:** Industry growth projections, hiring trends

**4. Equity and Access**
- **Theme:** Serving underrepresented populations effectively
- **Audience:** Workforce boards, community organizations
- **Key points:** Barrier reduction, wraparound services, culturally responsive programs
- **Data to include:** Demographic gaps, success stories

**5. Public-Private Partnership Models**
- **Theme:** Innovative funding and delivery approaches
- **Audience:** Economic development, business community
- **Key points:** Shared investment, employer engagement, sustainability
- **Data to include:** ROI studies, partnership examples

**6. Metrics and Accountability**
- **Theme:** Proven evaluation frameworks for workforce programs
- **Audience:** Legislative committees, funding agencies
- **Key points:** Outcome measurement, continuous improvement, data-driven decisions
- **Data to include:** Performance metrics, evaluation methodologies

### Relationship Building Priorities

Identify and cultivate relationships with:

**Executive Leadership:**
- Workforce board executive directors
- State labor secretaries and deputies
- Economic development agency directors
- Community college system chancellors
- Governor's policy advisors (workforce, economic development)

**Legislative Contacts:**
- Appropriations/finance committee staff
- Labor and workforce committee staff
- Economic development committee staff
- Key legislators (chairs, vice-chairs, champions of workforce issues)
- Legislative budget analysts

**Regional/Local:**
- One-stop operator managers
- Local workforce area directors
- Regional planning council staff
- Economic development directors (city/county/regional)
- Chamber of commerce executives

**Employer Community:**
- Industry association executives
- Sector partnership conveners
- Large employer HR/training directors
- Manufacturing extension partnership staff

### Competitive Intelligence

When analyzing opportunities, research and note:

**Active Organizations:**
- Community colleges and training providers active in the region
- Workforce development nonprofits (Goodwill, Urban League, etc.)
- Consulting firms specializing in workforce grants
- Technology training providers
- Industry associations with training programs

**Past Awardees:**
- Review previous awards if this is a recurring program
- Identify organizations with proven track record
- Note partnership patterns (who teams with whom)
- Understand successful proposal strategies

**Required Qualifications:**
- Licensure or accreditation requirements
- Track record or experience requirements
- Geographic presence requirements
- Minimum organizational capacity or budget
- Specific subject matter expertise

**Political Considerations:**
- Election year dynamics
- Governor's priorities and initiatives
- Legislative champions or opponents
- Agency leadership changes
- Regional equity considerations
- Economic development zone preferences

**Timing Factors:**
- Fiscal year cycles (state and federal)
- Budget hearing schedules
- Legislative session calendars
- Election cycles (state and federal)
- Agency planning timeframes

---

## Quality Control Procedures

### Accuracy Checks

**Before Generating Intelligence Brief:**
1. **Verify funding amounts:** Cross-reference source documents, check if minimum/maximum or total program amount
2. **Confirm deadlines:** Check official posting, note if pre-proposal vs. final deadline
3. **Cross-reference geography eligibility:** Read fine print on state/local restrictions
4. **Validate agency contact information:** Check current organizational structure, verify names/titles
5. **Check for updates:** Look for amendments, FAQs, webinar announcements

**During Scoring:**
1. Apply scoring rubric consistently
2. Document rationale for each score component
3. Flag borderline cases for review
4. Note when new opportunity type doesn't fit existing criteria

**After Intelligence Brief:**
1. Proofread for clarity and accuracy
2. Ensure all URLs work
3. Verify recommended actions are realistic
4. Check that timeline recommendations are feasible

### False Positive Reduction

**Common False Positives to Filter:**

**Job Postings vs. Funding Opportunities:**
- "Position available" or "now hiring" = NOT a funding opportunity
- "Applications sought for grant program" = IS a funding opportunity

**Award Announcements vs. Active Opportunities:**
- "[Organization] receives $X grant" = NOT active (already awarded)
- "Applications due [future date]" = IS active

**Goods/Services RFP vs. Grant:**
- "Purchase [equipment/software/services]" = NOT relevant
- "Operate [training program] for participants" = MAY be relevant if training focus

**Out-of-Scope Training:**
- Medical continuing education (CME) = NOT relevant unless workforce development
- Teacher professional development = NOT relevant unless workforce pipeline
- Law enforcement training = NOT relevant unless transferable skills

**International Programs:**
- "International development" = NOT relevant
- "Federal program available in all 50 states including [target states]" = RELEVANT

### Score Validation

**Review scoring logic when:**
- Opportunity score feels misaligned with intuition about value
- Multiple borderline opportunities in same week (may need criteria adjustment)
- User feedback indicates scoring didn't match their assessment
- New funding mechanism emerges that doesn't fit existing model

**Scoring Edge Cases:**
- **Unknown funding amount:** Score conservatively (estimate based on similar programs) and flag uncertainty
- **Rolling deadline:** Treat as "good" timeline (15 pts) unless funds running out
- **Planning grant leading to implementation:** Score the full potential value, note multi-phase
- **Federal grant to state (pass-through coming):** Score based on anticipated sub-grant value
- **Legislative bill (uncertain if will pass):** Include probability discount in competition/timeline scoring

---

## Continuous Improvement Process

### Weekly Review (Every Friday)

**Review Questions:**
1. Did we miss any opportunities that should have been captured? (Check industry newsletters, colleague intel)
2. Are score distributions appropriate? (Not all high, not all low - looking for spread)
3. Are routing tags leading to correct actions? (White-paper-ready truly actionable within 30 days?)
4. Is geographic coverage balanced? (Some states consistently underrepresented?)
5. Are any sources consistently low-value? (High false positive rate from certain sources?)

**Actions:**
- Add missed keywords to search-criteria.md
- Adjust scoring weights if systematic misalignment
- Refine routing tag thresholds if needed
- Investigate underrepresented states (add sources?)
- Reduce frequency or remove low-value sources

### Monthly Optimization (First Friday of Month)

**Keyword Review:**
- Analyze which keywords triggered valuable opportunities
- Add new terminology that has emerged
- Remove keywords generating excessive false positives
- Update Boolean search strings

**Source Review:**
- Rank sources by true positive rate
- Add new sources discovered or recommended
- Adjust check frequency (daily vs. weekly) based on productivity
- Note any source access issues (paywall, broken link, restructured website)

**Scoring Analysis:**
- Calculate average score (ideally 60-70 range)
- Review distribution across routing tags (balanced?)
- Identify if any scoring criteria need weight adjustment
- Note patterns in high-scoring vs. low-scoring opportunities

**Geographic Coverage:**
- Confirm balanced representation across 5 target states
- Review federal opportunities for state relevance
- Consider if adjacent states warrant closer monitoring
- Update agency contact lists in target-regions.md

**Threshold Adjustment:**
- Review alert threshold (currently 85+) - too many or too few?
- Review intelligence brief threshold (currently 70+) - appropriate?
- Review minimum funding capture (currently $10K) - right level?

### Quarterly Strategic Assessment (End of Quarter)

**Effectiveness Analysis:**
1. **White-paper-ready identification:** How many pre-RFP signals captured? How many materialized into actual opportunities?
2. **Success rate when pursuing:** Win rate on proposals submitted? Quality of opportunities pursued?
3. **ROI on time spent:** Which opportunity types yielded best results relative to effort?
4. **Emerging trends:** What themes are growing? What's declining?
5. **Competitor analysis:** Who's winning? What strategies are they using?

**Strategic Questions:**
- Are we focusing on the right geography? (Expand? Narrow?)
- Are we focusing on the right sectors? (Manufacturing vs. healthcare vs. IT?)
- Are we focusing on the right opportunity types? (Pre-RFP vs. active RFP balance?)
- Do our capabilities match opportunity requirements? (Build new capabilities?)
- Should scoring weights shift based on organizational priorities?

**System Updates:**
- Major updates to Skill.md if workflow changed significantly
- Refresh REFERENCE.md with new best practices learned
- Update scoring-examples.md with real opportunities from quarter
- Revise target-regions.md with new agencies or contact changes
- Update output-templates.md if new report types needed

---

## Integration with Business Development

### Handoff to Proposal Team (Detailed)

When opportunity moves to proposal-ready status, provide complete handoff package:

**1. Intelligence Brief**
- Full opportunity analysis with score breakdown
- Strategic positioning recommendations
- Competitive landscape assessment

**2. Source Documents**
- RFP/solicitation PDF
- Q&A documents if available
- Past award information
- Agency strategic plans or relevant policy documents

**3. Informal Intelligence**
- Notes from any stakeholder conversations
- Insights from pre-proposal conference (if attended)
- Observations from similar opportunities
- Network intelligence about competition

**4. Technical Requirements**
- Subject matter expert needs identified
- Technical approach recommendations
- Evaluation criteria analysis
- Compliance checklist

**5. Partnership Recommendations**
- Required partners (if mandatory teaming)
- Suggested partners (if advantageous)
- Partner roles and contributions
- Letters of commitment needed

**6. Resource Estimation**
- Level of effort estimate for proposal development
- Budget range based on requirements
- Timeline for proposal development
- Staff/consultant needs

**7. Risk Assessment**
- Barriers to successful proposal
- Gaps in qualifications or experience
- Competition risk factors
- Go/no-go recommendation with rationale

### White Paper Production Trigger (Detailed)

When opportunity tagged white-paper-ready, generate detailed white paper brief:

**1. Positioning Strategy**
- Specific angle/topic for white paper
- Target audience (agency, committee, board)
- Key messages to convey
- Call-to-action or engagement ask

**2. Content Recommendations**
- Outline structure (executive summary, problem, solution, recommendations)
- Data points to include (labor market, best practices, case studies)
- Research sources to cite
- Length and format (typically 8-12 pages, executive summary + full paper)

**3. Distribution Plan**
- Primary recipients (names and titles)
- Secondary distribution (associations, networks)
- Delivery method (email, meeting, webinar)
- Follow-up engagement strategy

**4. Timing Analysis**
- Optimal release date (before key decision points)
- Follow-up milestones (meetings, presentations)
- Opportunity timeline alignment
- Legislative or budget calendar considerations

**5. Supporting Materials**
- One-pager summary for quick reference
- Presentation deck for in-person briefings
- Talking points for conversations
- FAQ for potential questions

**6. Success Metrics**
- Measures of engagement (downloads, meetings secured)
- Influence indicators (cited in documents, invited to testify)
- Relationship milestones (access to decision makers)
- Opportunity outcome (RFP released, positioned well)

---

## Best Practices for Users

### When to Run the Skill

**Daily (Recommended):**
- Morning scan for new opportunities across all sources
- Review any high-priority alerts from overnight
- Quick check of state legislative trackers during session

**On-Demand:**
- Deep dive into specific state when following up on lead
- Topic-specific search when researching particular industry/population
- Re-scan when major policy announcement occurs (Governor's budget, new federal program)

**Active Pursuit:**
- Monitor tracked opportunities for amendments or Q&A
- Check for similar opportunities in other states
- Track deadline countdowns for active proposals

### Customization Recommendations

**Scoring Weights:**
- Default: Funding 40, Timeline 20, Competition 20, Geography 20
- **If capacity-constrained:** Increase competition weight (favor easier wins)
- **If seeking visibility:** Increase funding weight (favor larger, high-profile opportunities)
- **If regional focus:** Increase geography weight to favor specific states
- **If relationship-building mode:** Increase timeline weight (favor longer lead times)

**Geography Expansion:**
- Consider adding adjacent states (WV, NC, NJ, NY) if opportunities spill over
- Weight adjacent states lower (5-10 pts) to maintain target state focus
- Monitor for regional/multi-state programs that include target states

**Funding Thresholds:**
- Default minimum: $10,000 (balance opportunity size with search volume)
- **If pursuing only major opportunities:** Raise minimum to $50K or $100K
- **If exploring all options:** Lower to $5K but expect higher volume

**Routing Tag Customization:**
- Default thresholds: 80/70/50/<50 for four tags
- **If aggressive growth mode:** Lower white-paper-ready to 75+ to capture more
- **If selective/quality mode:** Raise proposal-ready to 75+ to focus only on best
- Can add custom tags (e.g., "partnership-required", "quick-turnaround")

**Sector Focus:**
- Default: Broad across multiple industries
- **If industry-specific:** Adjust keywords to favor manufacturing, healthcare, IT, etc.
- **If population-specific:** Boost keywords for veterans, youth, re-entry, etc.
- Update scoring to bonus points for strategic priority matches

### Common Pitfalls to Avoid

**1. Chasing Every Opportunity**
- **Pitfall:** Pursuing too many moderate opportunities, spreading resources thin
- **Solution:** Set minimum score threshold (e.g., only pursue 75+) and stick to it

**2. Ignoring Pre-RFP Signals**
- **Pitfall:** Only responding to active RFPs when competition is highest
- **Solution:** Prioritize white-paper-ready opportunities for strategic positioning

**3. Neglecting Relationship Building**
- **Pitfall:** Viewing this as purely automated search, missing human intelligence
- **Solution:** Use findings to guide relationship strategy, attend stakeholder meetings

**4. One-Size-Fits-All Approach**
- **Pitfall:** Same white paper or proposal strategy for every opportunity
- **Solution:** Customize positioning to specific opportunity context and audience

**5. No Follow-Through**
- **Pitfall:** Identifying opportunities but not acting on white papers or proposals
- **Solution:** Assign owners and deadlines for every high-priority opportunity

**6. Ignoring Negative Signals**
- **Pitfall:** Pursuing despite risk factors (short timeline, poor fit, strong competition)
- **Solution:** Respect go/no-go recommendations, focus on winnable opportunities

**7. Static Approach**
- **Pitfall:** Never updating keywords, sources, or scoring as environment changes
- **Solution:** Follow monthly and quarterly review process religiously

---

## Limitations and Caveats

### Known Limitations

**Access Limitations:**
- Some opportunities require subscription services or insider access (e.g., paywalled news, membership-only portals)
- Local/county opportunities may not be visible in online state sources
- Relationship-based opportunities may not be publicly posted ("invitation only" with no announcement)

**Timing Uncertainty:**
- Legislative signals may not materialize into actual funding (bill doesn't pass, budget cut)
- Pre-RFP signals have inherently uncertain timelines (could be 3 months or 18 months)
- Agency planning can change with leadership transitions or political shifts

**Competitive Intelligence Gaps:**
- Difficult to know all competitors pursuing same opportunity
- Hard to assess quality/capacity of competition without insider knowledge
- Past performance data may not be publicly available

**False Negatives:**
- Opportunities announced in non-traditional venues may be missed
- Programs with different terminology than our keywords
- Very new/innovative programs that don't fit existing categories

**Scoring Subjectivity:**
- Scoring rubric provides structure but some judgment calls remain
- Different users might weight factors differently based on risk tolerance
- Changing organizational priorities may make historical scores less relevant

### When to Combine with Other Intelligence

**Human Relationship Intelligence:**
- Attend workforce board meetings to hear about upcoming opportunities
- Build relationships with agency program officers who share early signals
- Network with peers in the field who may hear of opportunities first
- Engage with employer community to understand their workforce needs

**Subscription Services:**
- Federal grant monitoring services (e.g., GrantWatch)
- State policy tracking services (e.g., LegiScan premium)
- Industry association newsletters and alerts
- Economic development listservs and networks

**Direct Outreach:**
- Call or email agencies to ask about anticipated funding
- Request to be added to interested parties lists for upcoming RFPs
- Ask about timing for next funding cycle if past opportunities closed
- Inquire about sub-grant opportunities from federal pass-through awards

**Market Research:**
- Review agency strategic plans and annual reports directly
- Attend conferences where agency leaders present priorities
- Monitor workforce board performance reports for underserved areas
- Analyze industry trends to anticipate workforce needs driving future funding

---

**Version:** 1.0.0
**Last Updated:** 2025-10-25
**This reference guide supplements Skill.md with detailed implementation guidance**
