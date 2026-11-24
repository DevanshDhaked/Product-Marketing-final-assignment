---
type: Handoff
title: "Pricing teammate report, phase 1b"
description: "Plan, progress and final summary from the pricing work: recommended terms, six feedback points answered, insights, decisions, rejected approaches, required follow-up edits and unverified items."
tags: [handoff, pricing]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T19:10:00Z }
---

# Pricing teammate report, phase 1b

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Worktree: `Product-Marketing-final-assignment.d1-pricing`, branch `d1-pricing` from `iteration-a` (03aef9a).

Status: done, waiting for team approval at gate 1b. Recommended: Rs 199 per employee per month billed yearly plus GST; pilot 12 weeks, up to 40 people, Rs 25,000 plus GST, credited on conversion, refunded only if the firm took part properly and the partners say the record showed nothing new. Details and alternatives in `## Final`.

## Plan

**Success number: 6 of 6 professor pricing points answered with shown working.**

### File to feedback point map

| File | Answers | Purpose |
|---|---|---|
| `docs/pricing/value_model.md` | 1 Value | Value per employee per month for a consulting firm, low, mid, high |
| `docs/pricing/competitor_comparison.md` | 2 Competitors | Named plans, like-for-like feature map, non-comparable rows flagged |
| `docs/pricing/cost_and_breakeven.md` | 4 Break-even (and the floor for 3) | Cost to serve by line, margin floor, fixed cost by line, contribution, break-even, script appendix |
| `docs/pricing/price_and_pilot.md` | 3 Rationale, 5 Pilot | Final price against floor, value and anchors; pilot price, length, non-conversion terms |
| `docs/pricing/validation_plan.md` | 6 Validation | Van Westendorp design with a fixed decision rule, pilot-to-paid and margin checks with thresholds |
| `docs/pricing/pricing_summary.md` | writer-facing | One page in plain words: price, what is included, the pilot, three numbers that justify it |
| `docs/pricing/index.md`, `docs/pricing/log.md` | OKF | Built with `build_index.py` for this subfolder only |

### Derivation order (no price is chosen in advance)

1. Cost floor (cost to serve per seat, then floor at the target gross margin).
2. Value per seat (low, mid, high).
3. Competitor anchors (Indian HRMS modules low anchor, global tools high anchor).
4. Value share (what part of value a new vendor can capture, sourced).
5. List price = the point that clears the floor, sits inside the anchors, and captures a defensible share of mid value.

Test for keeping ₹149: it stays only if it clears the new floor and sits inside the anchor band. Otherwise it changes. Same test for the ₹15,000 pilot.

### 1. value_model.md (point 1)

- Formula independent of firm size, so it answers "how one resignation becomes ₹500 per employee per month" and shows why a flat per-seat price is coherent:
  `value per seat per month = (attrition rate x relative reduction x cost per exit + review hours saved per seat per year x loaded hourly cost) / 12`
- Then a worked firm example (reference firm size from segment.md, about 120 professionals, a guess) that shows the firm-level rupee saving and divides it back down.
- Inputs to source: voluntary attrition in professional services (SPI 2025 Table 170 already in segment.md, plus Indian sources such as Aon or Mercer India salary and attrition surveys); salary bands for analyst, consultant, senior consultant, manager in Indian management consulting (AmbitionBox, Glassdoor); cost per exit lines: recruiter fee (Indian agency fee as a share of CTC), ramp time to full billability, lost billable time while the seat is empty (utilization and bill rate), partner and HR time, client impact (estimate, labelled).
- Attribution: share of exits linked to unfair or opaque appraisal (foundit 2026 job-hunting figure, exit-reason surveys); relative reduction Sphyr could cause is an estimate in all three cases, stated as such.
- Review prep: hours per seat per year on project-end forms, chasing, calibration meetings, partner time, at a stated loaded hourly cost. The 2018 whitepaper figures (US$63 vs US$85, 1,000 manager-minutes for 20 reports) come from a paper-and-pen pilot (do_not_claim 9): used only as a caveated cross-check, never as a Sphyr software result.
- Output: low, mid, high table, plus the old ₹667 shown against it.

### 2. competitor_comparison.md (point 2)

- Each row: product, plan name, list price, billing basis, minimum, what the plan includes, date read (2026-11-24), URL.
- Global: Lattice (Performance plan, $4,000/yr minimum), 15Five (Perform), Leapsome (no public price, say so), Culture Amp (no public price), PerformYard (sells to consulting firms), Peoplebox, Confirm.
- Indian HRMS: read Keka, Darwinbox, Zoho People, greytHR pages directly. The ₹50 to 150 figure comes from hrone.cloud, a competing vendor's blog, so it is used only if confirmed or clearly labelled.
- Like-for-like matrix on features Sphyr really has (fortnightly peer cards, sphere of influence, pooled ratings, anonymized comments to the person rated, manager approval of edits, VBAs, OKR cascade, CSV import, external raters by email invite). No AI, no integrations on the Sphyr side.
- Mark non-comparable rows and why (HRMS bundle with no standalone review price, annual-review tools with no fortnightly cadence, engagement-survey tools).
- Exchange rate fetched and cited for 2026-11-24.

### 3. cost_and_breakeven.md (point 4, and the floor for point 3)

- Variable cost per seat per month, line by line: hosting (AWS Mumbai or similar list prices, stated usage per seat), email and notifications (fortnightly reminders, invites; SES or similar list price), payment fees (gateway vs bank transfer for annual invoices), support per seat (tickets per seat x minutes x support cost), onboarding labour amortized over a year (setup, training and support are included in the price), GST treatment (18% charged on top, pass-through for GST-registered buyers, not a cost; confirm rate and SAC code). AI removed from the cost lines.
- Margin floor = cost per seat / (1 minus target gross margin), with the target margin sourced from B2B SaaS benchmarks.
- Fixed cost per month by named line: people (roles and Indian salary sources), infra base, tools, sales and marketing, support base, compliance and legal (accounting, GST filing, contracts; no security certification claimed). Assumptions stated per line.
- Contribution per seat, break-even in seats and in firms of the reference size, months to break-even under a stated ramp.
- Break-even seats compared to the segment's guessed 18,000 to 48,000 seats. The implied penetration share is reported as a finding, plainly, even if it is uncomfortable.
- Appendix: the Python script source as a fenced block plus its pasted output (scratchpad can be wiped). See open question 4.

### 4. price_and_pilot.md (points 3 and 5)

- Final price against floor, value and anchors, with the reason for the exact number (no charm pricing below the floor).
- Why the price captures only part of the value: value share norms in B2B SaaS (sourced), new-vendor risk with no customers, buyer budget authority (head of talent gets one budget ask a year, managing partner signs), the Indian HRMS anchor.
- What is included, with AI and integrations removed. OKRs are listed only as the prototype shows them (Team and Strategic OKR screens exist).
- Pilot: length set by signal need. Six fortnightly cycles is 12 weeks. To finish before the April calibration, a pilot must start by early January; the doc states this constraint. Pilot price derived from cost to serve plus onboarding labour for the pilot group, and compared to list price for the same seats and weeks.
- Non-conversion terms: credit against the first annual bill if they convert; what happens to the fee if they do not (see open question 2); data handed back as a CSV sent by us (the product has no self-serve export screen in the prototype, so it is written as a manual service); deletion within a stated number of days, written as an operational promise, not a compliance claim (do_not_claim 5).
- Required changes for the lead to apply (I do not edit outside `docs/pricing/`): pilot length and scorecard timing in `docs/strategy/acquisition_engagement.md`; the conflict with packaging's full-refund offer (source_conflicts row 12).

### 5. validation_plan.md (point 6)

- Respondents: managing partners and heads of talent at firms in the segment, not generic "HR buyers".
- Population is about 150 to 400 firms (segment guess), so n = 40 to 60 is not realistic. Plan a smaller n (target to be set from sourced guidance) and treat results as directional.
- Recruitment without scraped lists: team and alumni networks, a manually read LinkedIn search, consulting associations and events, walkthrough visitors who opt in.
- Van Westendorp four questions plus Newton-Miller-Smith purchase-likelihood questions, because plain Van Westendorp measures price perception, not intent to buy.
- Decision rule fixed before data: how the four curves and the acceptable range (point of marginal cheapness to point of marginal expensiveness) set the list price; what happens if the range excludes the proposed price; what result changes it.
- Pilot-to-paid conversion threshold and gross margin review threshold, each with a trigger and the action it causes.

### 6. pricing_summary.md (writer-facing)

- Plain words: price, what it includes, the pilot, the three numbers that justify it. Run through `humanizer:humanizer` only if it becomes public copy; it is an internal doc for writers.

### Method

- Research with firecrawl and exa; every external fact gets URL and access date 2026-11-24 in `sources` frontmatter. Estimates and guesses labelled with their reason. Sample sizes given with any claim.
- Numbers computed by a Python script in the scratchpad; outputs pasted, not hand-calculated.
- OKF v0.2 via `hack-kit:okf-docs`; index only for `docs/pricing`; validator at 0 errors.
- Commits on `d1-pricing`, one per logical group (research docs, cost and price docs, validation and summary, index and log). No push, no merge.

### Open questions for the lead

1. Time budget: how long do I have? This decides research depth per competitor and salary source.
2. Pilot fee if the firm does not convert: credit-only (kept by Sphyr), partly refundable, or fully refundable? Packaging's graded work offered a full refund after about 12 weeks.
3. The old "first 25 customers: price locked for 2 years in exchange for a case study": keep, drop, or change? It may conflict with the consent-only publishing rule in acquisition_engagement.md.
4. Script persistence: may I paste the script source as a fenced appendix in `cost_and_breakeven.md`, or commit it as a file under `docs/pricing/`?
5. Reference firm size for the worked example: use the segment's 120-professional guess?

## Progress

- 2026-11-24: Plan approved by lead. Answers: no hard time limit, finish each file before deepening the next; I recommend pilot non-conversion terms and the case-study price lock (opt-in, consent-based) with a runner-up; script pasted as appendix in cost_and_breakeven.md and committed as docs/pricing/pricing_model.py; reference firm 150 professionals, with 40 and 400 ends shown; outside-folder changes listed in the final report only.
- 2026-11-24: value_model.md and competitor_comparison.md written, commit 8e96aef. Value per seat per month: low Rs 198, mid Rs 1,379, high Rs 7,306. Global like-for-like modules Rs 719 to 1,021 (Leapsome, Peoplebox, Confirm, Lattice, 15Five); Indian anchors greytHR PMS Rs 35 to 45, Keka Growth whole HRMS about Rs 157 per seat at 150 staff. Next: cost_and_breakeven.md.
- 2026-11-24: all six files written, validator 0 errors (1 expected warning: cost_and_breakeven.md is 691 lines because the lead asked for the script and its output as an appendix). Commits 37805cd, 407e32d, c92d972, efa0b04, 4a07d30.

## Final

### Recommended terms for team approval (gate 1b)

- **Price: Rs 199 per employee per month, billed yearly, plus GST.** Same for every employee and firm size. Runner-up Rs 149. Price rule: floor (Rs 121) <= price <= low-case value (Rs 209), inside the anchors; only Rs 149 and Rs 199 pass. Van Westendorp picks between them by the rule in validation_plan.md; Rs 249 is tested only if pilot data raise the low-case value above Rs 249.
- **Pilot: 12 weeks (6 fortnightly cycles), one or two practices up to 40 people, Rs 25,000 plus GST.** Must start by 7 Jan 2027 to finish before 1 Apr 2027. 60-day read-only access after the last cycle. Full fee credited to the first annual bill if the firm signs within 60 days of the last cycle.
- **Non-conversion (recommended A, conditional refund):** fee refunded in full if the firm had 80%+ participation in at least 5 of 6 cycles AND fewer than half its partners say the record showed something new; otherwise kept. Worst-case refund exposure: Rs 50,000 for 4 pilots at 50% conversion (5.5% of one month's fixed cost). Fee equals cost to serve (Rs 25,344 to 25,998). Data terms in all options: CSV sent within 7 days of request (manual, the prototype has no export screen); account and data deleted within 30 days after the 60-day read-only window, confirmed in writing; invoices kept for tax. **Runner-up B:** fee kept, credit only on conversion. I first recommended B, then switched after reading the McKinsey source (19 Nov 2025): eight in ten B2B decision makers look for a new vendor without performance guarantees, its example being a refund when milestones are not met.
- **Price lock (recommended):** first 10 paying firms keep Rs 199 for 24 months, no case study required. Publishing a scorecard is a separate, consent-only question with no price attached. **Runner-up:** lock for 10 firms in exchange for an opt-in case study. The old 25-firm, case-study lock is rejected.

### The six feedback points, answered (6 of 6)

1. Value: formula per seat independent of firm size, low Rs 209 / mid Rs 1,249 / high Rs 6,409 per seat per month (value_model.md).
2. Competitors: 9 global plans and 4 Indian HRMS rows named with price, billing, minimum, features, URL, date; comparable and non-comparable rows marked (competitor_comparison.md).
3. Rationale: floor Rs 121 at 80% gross margin; Rs 199 is 15.9% of mid value; Rs 149 vs Rs 199 trade-off shown; ending-in-9 explained (price_and_pilot.md).
4. Break-even: variable cost Rs 24.75 per seat by line, GST pass-through, fixed Rs 9,06,928 a month by line, break-even 5,205 seats = 35 firms of 150 at Rs 199; 152 firms of 40 or 13 firms of 400 (cost_and_breakeven.md).
5. Pilot: price, length, timing, non-conversion terms with options (price_and_pilot.md).
6. Validation: Van Westendorp plus Newton-Miller-Smith, who/how many/how recruited, decision rule fixed before data, conversion threshold 50% with a check after 4 pilots, quarterly margin triggers (validation_plan.md).

### Files written, with commit SHAs (branch d1-pricing)

- 8e96aef: value_model.md, competitor_comparison.md, pricing_model.py (first version).
- 37805cd: pricing_model.py, value_model.md, competitor_comparison.md (voluntary attrition, partner time, cost, price, pilot sections; AI and integrations sentence fixed).
- 407e32d: cost_and_breakeven.md (with script and output appendix), price_and_pilot.md.
- c92d972: validation_plan.md, pricing_summary.md.
- efa0b04: index.md, log.md for docs/pricing.
- 4a07d30: low-case price rule, conditional pilot refund, Leapsome post-promotion price and stale_after, break-even by firm size, summary claims fixed, appendix regenerated (cost_and_breakeven.md is now 742 lines; validator warning only).

### Key insights and findings (sources in each doc's frontmatter, accessed 2026-11-24)

- Break-even needs a large share of a small segment: at Rs 199, 35 firms of 150 = 11% to 29% of the segment's guessed 18,000 to 48,000 seats; at Rs 149, 49 firms = 15% to 40%. Run-rate break-even about 16 to 17 months after the first sale at 2 new firms a month (estimate). The team should discuss the lean team and adjacent segments.
- Firm size decides break-even: at Rs 199 it takes 152 firms of 40 (about the whole low-end firm count of the segment), 35 of 150 or 13 of 400. Selling should go first to firms of 150 and more.
- Leapsome's EUR 7 review module needs an HRIS foundation that is free only until 31 Dec 2026; after that the like-for-like price is EUR 12 to 14 (Rs 1,233 to 1,438). The cheapest dedicated-tool list price is PerformYard's $5 (Rs 464); Rs 199 is 43% of it. competitor_comparison.md has stale_after 2026-12-31.
- Rs 199 is above Keka Growth's whole-HRMS cost (about Rs 157 per seat at 150 staff; base price from a third-party review). Positioning answer: Sphyr sits next to the HRMS, it does not replace it.
- Leapsome now publishes prices (Performance Reviews EUR 7). The graded claim "Leapsome, Lattice and Peoplebox Rs 665 to 1,425" was really one Peoplebox G2 band.
- Voluntary attrition: Aon India 2025 voluntary 12.0% of 16.2% total (Business Today, 2 Mar 2026); SPI 2025 voluntary 6.9% for 101 to 300 staff (403 firms, global).
- Exit reasons Sphyr can touch: SPI 2025 Table 172 lack of career advancement 14.9% + management dissatisfaction 5.5%; Gallup 2008 31.5% + 16.5%.
- Review time: Deloitte about 2 million hours for 65,000-plus people (HBR 2015); CEB 210 h per manager, 40 h per employee (SHRM 2015).
- Exit cost build-up is 0.28x to 0.54x CTC, deliberately below Gallup's 0.5x to 2x and 80% for technical professionals.
- Small firms cost more per seat: gross margin at Rs 199 is 75.1% at 40 people (below the 80% target), 87.6% at 150, 90.4% at 400.

### Decisions I made and why

- Voluntary attrition only, because the exit-reason shares are shares of voluntary leavers.
- Partner time costed separately at Rs 2,700 an hour, because the brief asked for it.
- Support and onboarding counted as variable cost at the CSM hourly rate (0.87 FTE at break-even), not as a fixed CSM salary, so contribution includes them.
- 80% gross margin target (Benchmarkit CY2024 median 77%, subscription-only 81%).
- Pilot fee set at cost to serve, so Sphyr makes no profit on pilots and a refund would be a pure loss.
- No setup fee for small firms: it would break the flat price that is part of the offer.

### Approaches I rejected and why

- Keeping Rs 149: passes the floor and anchor test, but needs 49 firms to break even.
- Rs 249 and Rs 299: above the low-case value (Rs 209), so a firm in the low case would pay more than it gets; excluded by the stated price rule.
- Six-week pilot: only 3 cycles.
- Partial refund: adds a dispute about the amount and solves nothing.
- Fee kept with no refund (my first choice): rejected after the McKinsey source showed buyers look for exactly this guarantee.
- Unconditional refund: pays for firms that change their mind for unrelated reasons.
- 25-firm lock for a case study: locks 72% of the break-even base and pressures firms to publish only good results.
- Using Gallup's 0.5x to 2x salary directly as exit cost: not India, not consulting, and higher than costs we can name.

### Required changes outside docs/pricing/ (lead to apply; I did not edit them)

1. `docs/index.md`: add the line `* [pricing](pricing/index.md) - Sphyr pricing for Indian consulting firms: value per seat, named competitor plans, cost to serve and break-even, the proposed price and pilot, the validation rule, and a one-page summary for writers.` (build_index.py would add it; I built on a temp copy to avoid touching the root).
2. `docs/strategy/acquisition_engagement.md`: replace the open pilot-length conflict (line 64) with: pilot 12 weeks, 6 cycles, up to 40 people, Rs 25,000 plus GST, start by 7 Jan 2027 for the April round, 60-day read-only window, credit within 60 days; add the success-test targets from validation_plan.md section 5; non-conversion terms per the approved option.
3. `docs/packaging/first_use_experience.md` line 36 on iteration-a says the pilot length is still open (source conflicts row 11): set it to 12 weeks, 6 cycles once approved. The packaging docs on iteration-a already keep price and refunds out of scope, which matches the professor's note. Source conflicts rows 11 and 12 are resolved by price_and_pilot.md once approved.
4. `docs/strategy/persona_managing_partner.md` line 68 ("What does it cost?"): once approved, point to pricing_summary.md and add the Keka objection and answer.
5. Site, LinkedIn post 3 and ad: wait for gate 1b; use pricing_summary.md wording; run through the humanizer.

### Open questions

- Which price does the team approve, Rs 199 or Rs 149, and which non-conversion option, A (conditional refund) or B (fee kept)?
- Is a 7 Jan 2027 latest start realistic for 3 to 5 pilots over the holidays, or should the pilot be sold against the firms' mid-year review instead?
- Does the team accept the break-even finding, or should the fixed team or segment change?
- TDS treatment of SaaS invoices was not checked; needs a chartered accountant.

### What I did not verify

- Zoho People pricing page refused automated access; not used.
- Keka Growth base price (Rs 15,999 for up to 100) is from hr.software, a third party; only the Rs 150 per extra employee is on Keka's page. Darwinbox price is from a competing vendor's site.
- AWS prices read are Vantage "starting at" prices, not confirmed for the Mumbai region (20% buffer added).
- Practitioner sources only (no studies) for the 10 to 20% value share and for pilot conversion benchmarks; none give sample sizes. The McKinsey B2B Pulse figure was read at source but the page gives no sample size.
- The Sphyr effect on exits (e), the share of hours removed (k, q), partner hours (p), onboarding and support hours, founder pay and all "ESTIMATE" lines are guesses with reasons, not data.
- foundit's 86% figure was read but not used; Gallup and SPI are mostly non-Indian.
- Feature columns in the competitor table only show what the pages I read showed; a blank is not proof the feature is missing.
- I did not run the humanizer: these are internal docs; pricing_summary.md must be humanized before any line goes public.
