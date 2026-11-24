---
type: Research Note
title: "Validation plan: how survey and pilot results set the real price"
description: "The Van Westendorp study for consulting buyers (who, how many, how recruited without scraped lists), the decision rule fixed before data that turns the curves into a list price, and the pilot-to-paid conversion and margin checks with thresholds and the action each one triggers."
tags: [pricing, validation, van-westendorp, pilot]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T18:05:15Z }
status: draft
sources:
  - id: psm_cran
    resource: https://cran.r-project.org/web/packages/pricesensitivitymeter/refman/pricesensitivitymeter.html
    title: "pricesensitivitymeter R package reference: PMC, PME, OPP, IDP and the Newton-Miller-Smith extension (accessed 2026-11-24)"
  - id: quirks
    resource: https://www.quirks.com/articles/a-look-at-three-survey-based-methods-for-pricing-research
    title: "Quirk's, A look at three survey-based methods for pricing research (accessed 2026-11-24)"
  - id: sawtooth
    resource: https://sawtoothsoftware.com/resources/blog/posts/van-westendorp-pricing-sensitivity-meter
    title: "Sawtooth Software, Van Westendorp pricing sensitivity meter (accessed 2026-11-24)"
  - id: advergize
    resource: https://www.advergize.com/glossary/price-sensitivity-meter/
    title: "Advergize, Price Sensitivity Meter glossary: sample size guidance (accessed 2026-11-24)"
  - id: rocklane
    resource: https://www.rocklanestrategy.com/insight-hub/pricing-b2b-saas-pilots-to-convert-to-full-contracts
    title: "Rocklane Strategy, pricing B2B SaaS pilots to convert (practitioner, accessed 2026-11-24)"
  - id: tlab
    resource: https://tlab.fun/knowledge/what_are_realistic_b2b_pilot-to-contract_conversion_benchmarks_in_2026.php
    title: "tlab.fun, realistic B2B pilot-to-contract conversion benchmarks in 2026 (practitioner, accessed 2026-11-24)"
  - id: segment
    resource: ../strategy/segment.md
    title: "Segment, guessed 150 to 400 firms; how to find firms without scraping"
  - id: channel
    resource: ../strategy/channel_plan.md
    title: "Channel plan, consent-based channels and bans"
  - id: acq
    resource: ../strategy/acquisition_engagement.md
    title: "Acquisition and engagement, the pilot scorecard"
---

# Validation plan

The graded one-pager said "Van Westendorp price survey with 40 to 60 HR buyers, pilot-to-paid conversion, and a quarterly margin review". It did not say how a result would change the price. This plan fixes the decision rule before any data comes in, so the survey cannot be read to fit a number we already like.

## 1. Van Westendorp study

### The method in one paragraph

Each respondent names four prices: too cheap to trust, a bargain, getting expensive, and too expensive to consider.[^sawtooth] Plotting the share of respondents at each price gives four curves. Their crossings give the point of marginal cheapness (PMC, lower edge of the acceptable range), the point of marginal expensiveness (PME, upper edge), the optimal price point (OPP) and the indifference price point (IDP).[^psm_cran] Plain Van Westendorp measures how a price is perceived, not whether people would buy. So we add the Newton-Miller-Smith extension: two five-point purchase-likelihood questions asked at the respondent's own "bargain" and "getting expensive" prices.[^quirks] Likelihood at the "too cheap" and "too expensive" prices is set to zero.[^psm_cran] This gives an expected take-up and revenue at each price.

### Who

- **Managing partners** (the buyer) and **heads of talent or HR leads** (the champion) at homegrown Indian management and strategy consulting firms of 40 to 400 professionals. IT consulting is out, as in the [segment](../strategy/segment.md).
- Not "HR buyers" in general, which is the gap the graded version had.
- At most two respondents per firm (one partner, one talent lead), so a single firm cannot dominate.

### How many

- The segment is guessed at 150 to 400 firms.[^segment] B2B price studies usually run 50 to 200 respondents and need wider confidence intervals; consumer studies want 100 or more.[^advergize]
- **Target: 40 completed responses from at least 25 firms.** That is below the usual B2B range, so the results are **directional**. Roles are analysed separately only if a role has 15 or more responses.

### How we recruit, without scraped lists

Following the [channel plan](../strategy/channel_plan.md) bans:

1. People who finish the website walkthrough or a 20-minute call and tick a box to take part.
2. The team's own and alumni networks, by personal message.
3. HR and consulting community events, in person, with a printed link.
4. A LinkedIn company search for Indian management consulting firms of 51 to 500 employees, read by a person, with one personal message per firm. No scraping, no bought lists, no automated messages.

The incentive is a short summary of the anonymised results, so firms see what peers think a fair price is. Answers are kept without names in the analysis.

### How the questions are framed

- The respondent first sees the 2-minute walkthrough and one paragraph on what is included (see [price and pilot](price_and_pilot.md)).
- Prices are asked per employee per month, with the annual bill for 150 people shown next to each answer, because B2B buyers judge price against the contract value.[^advergize]
- No price of ours is shown before the questions.

### When

December 2026 to January 2027, alongside the first pilot conversations. The list price can change until the first annual contract is signed. Firms that already hold a lock pay the lower of the locked and the new price.

## 2. The decision rule (fixed before data)

Candidate prices: **₹149, ₹199, ₹249**. ₹299 is excluded unless pilot data raise the mid value, because it is above 20% of mid value today.

1. Drop any candidate below the ₹121 margin floor (none today) or outside the acceptable range [PMC, PME].
2. Among the remaining candidates, pick the one with the highest expected revenue per respondent from the Newton-Miller-Smith curve (take-up x price).
3. If two candidates are within 10% of each other on expected revenue, pick the lower one. A new vendor should trade a little revenue for less risk.
4. If managing partners and talent leads disagree and both groups have 15 or more answers, the managing partners' range wins. They sign.
5. **If fewer than 30 responses arrive**, Van Westendorp alone does not move the price. It moves only if the pilot calls point the same way: price raised as an objection in at least half of the calls.

### What would change ₹199

| Result | Action |
|---|---|
| PME below ₹199 | Move to ₹149 |
| PME below ₹149 | Do not go below the floor. Stop and rework the value message and the offer, then re-test |
| ₹249 inside the range and its expected revenue at least 10% above ₹199 | Move to ₹249 |
| PMC above ₹249 | Run a second round with higher prices |
| ₹199 inside the range, no rule above applies | Keep ₹199 |

## 3. Pilot-to-paid conversion

Practitioner benchmarks put pilot-to-paid conversion at 30% to 45% for a median B2B SaaS company and above 70% for well-run pilots;[^rocklane] another gives 25% to 35% as a planning range for qualified paid pilots.[^tlab] Neither states a sample size.

- **Target: 50% or more.** Paid pilots with a written success test should beat the median. The break-even model in [cost and break-even](cost_and_breakeven.md) uses 50%.
- **Check after the first 4 pilots.** If fewer than 2 convert, review the pilot design, the offer and the price before signing more. Record the stated reason for every firm that does not convert.
- **If 3 or more of the first 4 convert and price is rarely raised**, test ₹249 with new firms. Locked firms are not affected.

The pilot shows whether the record is used. It cannot show the effect on exits in 12 weeks. That effect, `e` in the [value model](value_model.md), is checked after the first year: each paying firm's voluntary exits against its own previous year, with the firm's consent.

## 4. Margin checks

Reviewed every quarter, against the plan in [cost and break-even](cost_and_breakeven.md).

| Check | Plan | Trigger | Action |
|---|---|---|---|
| Gross margin across all firms | 80% or more | Below 80% for two quarters running | Find the cost line first: support hours, onboarding hours or hosting. Fix it before touching price. Any price rise applies at renewal only, with 60 days' notice, and never to locked firms |
| Support | 0.05 tickets per seat per month | Above 0.10 | Improve the help pages and the first-use flow |
| Onboarding hours per firm | 20 | Above 30 | Build templates for import and setup |
| Variable cost per seat | ₹24.75 at 150 seats | Above ₹40 | Same as the gross margin action |
| New firms a month | 2 | Below 1 for two quarters | The break-even date moves out past 30 months; revisit the fixed team and the segment |

## 5. Pilot scorecard targets

The pilot measures what [acquisition and engagement](../strategy/acquisition_engagement.md) lists.[^acq] With a 12-week pilot, these are the success-test targets we propose the firm agrees to in writing. They are starting points for that conversation, not sourced benchmarks:

1. Participation of 80% or more in each of the six cycles.
2. At least 6 different colleagues giving feedback to each consultant by cycle 6.
3. At least half of senior consultants with feedback from people on 3 or more engagements by calibration.
4. At least half of the partners answer yes to "Did the record show you something you did not know?"
5. At least half of the consultants answer yes to "Would you keep doing it?"

[^psm_cran]: pricesensitivitymeter reference
[^quirks]: Quirk's on pricing methods
[^sawtooth]: Sawtooth on Van Westendorp
[^advergize]: Advergize on sample size
[^rocklane]: Rocklane Strategy
[^tlab]: tlab.fun
[^segment]: Segment
[^acq]: Acquisition and engagement
