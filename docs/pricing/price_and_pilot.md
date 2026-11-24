---
type: Research Note
title: "Price and pilot: the recommended terms and why"
description: "The recommended list price against the margin floor, the value and the competitor anchors, why it captures only part of the value, what it includes, and the pilot's price, length, timing and what happens when a firm does not convert, with the runner-up for each choice."
tags: [pricing, pilot, consulting, india]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T18:11:26Z }
status: draft
sources:
  - id: share_monetizely
    resource: https://www.getmonetizely.com/blogs/your-market-has-a-high-willingness-to-pay-but-not-for-your-product
    title: "Monetizely, practitioner blog: vendors can capture about 10 to 20% of value (accessed 2026-11-24)"
  - id: share_mistral
    resource: https://mistral.vc/playbooks/pricing-before-pricing-power
    title: "Mistral VC playbook, practitioner rule of thumb: capture 10 to 20% of value (accessed 2026-11-24)"
  - id: share_monolit
    resource: https://monolit.sh/blog/value-based-pricing-for-startups-explained-2026
    title: "Monolit, practitioner blog: price at 10 to 20% of value (accessed 2026-11-24)"
  - id: mckinsey
    resource: https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-net-revenue-retention-advantage-driving-success-in-b2b-tech
    title: "McKinsey, The net revenue retention advantage, 19 Nov 2025, citing its B2B Pulse research: eight in ten B2B decision makers will look for a new vendor if performance guarantees are not offered; no sample size on the page (accessed 2026-11-24)"
  - id: prof
    resource: ../brief/professor_feedback.md
    title: "Professor feedback, pricing and packaging sections"
  - id: conflicts
    resource: ../prior_work/source_conflicts.md
    title: "Source conflicts, rows 11 and 12 (pilot length and risk terms)"
  - id: proto
    resource: ../product/prototype_screens.md
    title: "Prototype screens, including Team and Strategic OKR screens and CSV import"
  - id: model
    resource: pricing_model.py
    title: "Pricing model script, sections 5 to 7"
---

# Price and pilot

Inputs come from the [value model](value_model.md), the [competitor comparison](competitor_comparison.md) and [cost and break-even](cost_and_breakeven.md). Numbers are printed by [the pricing model](pricing_model.py). These are team proposals for approval, not facts from the product sources.

## Recommendation

- **Price: ₹199 per employee per month, billed yearly, plus GST.** The same price for every employee and every firm size.
- **Pilot: 12 weeks (six fortnightly cycles), one or two practices of up to 40 people, ₹25,000 plus GST.** Credited in full to the first annual bill if the firm signs within 60 days of the last cycle. Refunded in full if the firm ran the pilot properly and the partners say the record showed them nothing new; otherwise kept.
- **Early-firm price lock:** the first 10 paying firms keep ₹199 for 24 months, with no case study required.
- **Runner-up price: ₹149.** Van Westendorp results choose between them (rule in the [validation plan](validation_plan.md)).

## How the price was found

The order was fixed in advance, so no price was picked first: cost floor, then value, then competitor anchors, then value share, then price.

| Step | Result |
|---|---|
| 1. Margin floor at 80% gross margin, 150-person firm | ₹121 |
| 2. Value per seat per month | Low ₹209, mid ₹1,249, high ₹6,409 |
| 3. Competitor anchors | Indian: ₹35 to ₹45 (greytHR review add-on), about ₹157 (Keka's whole HRMS with reviews). Global dedicated tools: ₹464 (PerformYard's lowest) to ₹1,486; Peoplebox and Confirm from ₹743 |
| 4. Value share | 10% to 20% of mid value = ₹125 to ₹250 |
| 5. Test | The price must clear the floor, sit inside the anchor band, and be no higher than the low-case value (₹209), so that a firm in the low case does not pay more than it gets |

Of ₹149, ₹199, ₹249 and ₹299, only ₹149 and ₹199 pass. ₹249 and ₹299 clear the floor and sit inside the anchors, but they are above the low-case value. The choice between ₹149 and ₹199 is a trade-off:

| At a 150-person firm | ₹149 | ₹199 |
|---|---|---|
| Gross margin | 83.6% | 87.6% |
| Share of mid value | 11.9% | 15.9% |
| Firm's gain in the low case (value minus price) | ₹60 per seat | ₹10 per seat |
| Against Keka Growth's whole HRMS (₹157) | Below | 27% above |
| Firms of 150 needed to break even | 49 | 35 |
| Share of segment seats needed | 15% to 40% | 11% to 29% |
| Annual bill, 150 seats | ₹2,68,200 plus GST | ₹3,58,200 plus GST |
| Pays for itself if it prevents one exit every | 3.2 years | 2.4 years |

### Why ₹199

1. **₹149 does not build a business in this segment.** It needs 49 firms, up to 40% of every professional in the segment. ₹199 needs 35. Both are hard (see the finding in [cost and break-even](cost_and_breakeven.md)), but ₹149 is harder by 14 firms.
2. **It stays inside the value-share norm.** ₹199 is 15.9% of mid value. The usual rule of thumb is 10% to 20%. That rule comes from three practitioner sources, not from a study.[^share_monetizely][^share_mistral][^share_monolit]
3. **It meets the low-case rule, but only just.** At ₹209 of low-case value, the gain is ₹10 a seat. That is close to zero. The pilot exists to find out which case a firm is in before it pays for a year.
4. **It is far below dedicated tools.** ₹199 is 43% of the lowest list price we found for a dedicated tool (PerformYard's $5, ₹464, which applies to firms of several hundred) and 27% of Peoplebox's and Confirm's starting price (₹743).
5. **It is easy to say to a managing partner.** At 150 people, ₹3.58 L a year pays for itself if Sphyr prevents one voluntary exit every 2.4 years, against about 18 such exits a year in a firm that size (mid case).

### The cost of ₹199, said plainly

- **It is above Keka's whole HRMS (₹157 a seat at 150 people).** The managing partner will ask why reviews cost more than the HR system. The answer: Sphyr does not replace the HRMS or its annual review module. It adds a record that the HRMS does not keep: feedback from everyone a consultant worked with, every two weeks, across engagements. The right comparison is a dedicated feedback tool (₹719 and up) and the value of one kept consultant.
- **The low case is thin.** If a firm is in the low case, ₹199 roughly equals what it gets. The pilot and its success test are the protection.

### Why exactly 199, not 200

The old ₹149 sat below its own ₹150 floor with no reason given. ₹199 sits ₹78 above the ₹121 floor, so its ending does not cut into the margin. Indian HR software list prices often end in 9 or 5, for example Keka's ₹15,999 and greytHR's ₹2,495 and ₹4,495 (see the [competitor comparison](competitor_comparison.md)). ₹199 follows that habit. Nothing more rests on it.

## Why the price captures only part of the value

- **The value is our estimate.** No study shows Sphyr reduces exits. The firm carries the risk that the estimate is wrong, so it keeps most of the gain.
- **A new vendor with no customers.** Sphyr has no reviews or references. McKinsey reports that eight in ten B2B decision makers will look for another vendor if performance guarantees, such as a refund when milestones are not met, are not offered.[^mckinsey] A low price, a short paid pilot with a written success test, and the conditional refund below lower that risk.
- **Budget authority.** The head of talent gets one new budget ask a year (see the [head of talent persona](../strategy/persona_head_of_talent.md)), and the managing partner signs. A bill of about ₹3.6 L a year for 150 people is a size we expect a managing partner can approve without a long process. That is an ESTIMATE to test in the pilot calls.
- **Competitor anchors.** The firm already pays for an HRMS. Pricing far above the Indian anchor would make the comparison about price, not about the record.

## What the price includes

From the product sources and the prototype only:[^proto]

- Fortnightly five-click feedback cards for everyone in a person's circle of colleagues.
- Ratings pooled across seven parameters. Comments are anonymized to the person rated. Managers approve edit requests, and the approval queue shows who gave feedback to whom, so we never say "anonymous to everyone".
- Values, behaviors and attitudes as card options. Team and company OKRs, as in the prototype.
- Each employee's own insights over cycles, and manager views of team and member trends.
- Member import by CSV, XLS or XLSX. Raters outside the firm, such as clients, invited by email, free.
- Setup, training and support.
- New joiners billed from the month they join.

Not included, because the product does not have them: AI features, integrations with HRMS, payroll, Slack, Teams or SSO, mobile apps.

## The pilot

### Length: 12 weeks, six cycles

The graded six-week pilot had only three fortnightly cycles. Team sources say about six cycles (about 12 weeks) are needed for a usable record.[^conflicts] Over six cycles, a consultant is more likely to collect feedback from people on more than one engagement, which is what partners need at calibration. That is our reasoning, not a measured result. So the pilot is 12 weeks.

### Timing

To finish six cycles before 1 April 2027, a pilot must start by **7 January 2027**, 44 days from today (2026-11-24). Those 44 days include the year-end holidays. Signing 3 to 5 pilots in that window is the main schedule risk.

- After the last cycle, the firm keeps **read-only access** to all records and dashboards for **60 days**, with no new cycles, so partners can use the record in their April calibration.
- A firm that starts after 7 January runs the same six cycles. Its pilot ends after April, so the calibration questions in the scorecard are asked at its next review round instead, and the decision meeting uses the other scorecard items at week 12.

### Fee: ₹25,000 plus GST, up to 40 people

| | 25 people | 40 people |
|---|---|---|
| Cost to serve for 12 weeks | ₹25,344 | ₹25,998 |
| List price for the same seats and weeks | ₹13,747 | ₹21,995 |

Cost to serve is 30 hours of customer success time (20 hours of onboarding plus 10 for the pilot: the written success test, a mid-pilot check and the scorecard report and review) at ₹809 an hour, plus variable costs for 2.76 months. The fee is set to recover that cost, so Sphyr earns nothing on a pilot. At 40 people it is ₹226 per seat-month, close to list price. The old ₹15,000 was below the cost of a 12-week pilot.

### If the firm converts

The full ₹25,000 is credited to the first annual bill if the firm signs within 60 days of the last cycle. At 150 seats that is 7% of a ₹3,58,200 first year.

### If the firm does not convert

Data terms are the same in every option. Within 7 days of a request we send all ratings and comments as CSV files; the prototype has no self-serve export screen, so we do it by hand. After the 60-day read-only window, we delete the firm's account and data within 30 days and confirm it in writing. Only invoices are kept, because tax law needs them.

| Option | Fee if the firm does not convert | Verdict |
|---|---|---|
| **A. Conditional refund (recommended)** | Refunded in full if the firm did its part (participation of 80% or more in at least 5 of the 6 cycles) and fewer than half of the partners answer yes to "Did the record show you something you did not know?". Otherwise kept. | Buyers want a guarantee of this kind: McKinsey's example of a performance guarantee is "a refund if certain milestones can't be met".[^mckinsey] Both conditions are counted, not argued: participation comes from the product, the partner answer from a two-question survey agreed before the pilot. The firm cannot fail the test by not taking part. Worst case for Sphyr: if every non-converting pilot is refunded, 4 pilots at 50% conversion cost ₹50,000, 5.5% of one month's fixed cost. |
| B. Fee kept, credit only if converting (runner-up) | Kept. | Covers our cost and selects committed firms. But it offers no guarantee, which most buyers look for, and the firm alone carries the risk. |
| C. Full refund for any firm that does not convert | Refunded. | Rejected: pays for firms that change their mind for reasons unrelated to the result, and removes the commitment the fee is meant to create. |
| D. Partial refund | Part refunded. | Rejected: adds an argument about the amount without solving either problem. |

What the firm risks in any option: ₹25,000 and 12 weeks, against ₹3,58,200 for a first year at 150 seats. That cap, plus the conditional refund, is what stands in for the reviews and references Sphyr does not have yet.

The professor wrote that "refund promises" belong to "sales and marketing strategy" and are "not central to the packaging experience".[^prof] So these terms live here and in the acquisition plan, not on the first-use or packaging pages. The deletion promise is an operational commitment; it is not a compliance claim.

## Price lock for early firms

| Option | Cost if list later rises by ₹50 | Verdict |
|---|---|---|
| **First 10 paying firms keep ₹199 for 24 months, no conditions (recommended)** | ₹9 L a year forgone (10 firms x 150 seats) | Lowers the new-vendor price risk. 10 firms are 29% of the 35 needed to break even, a limited exposure. |
| First 10 firms locked in exchange for a case study (runner-up) | Same | A price tied to publication pressures firms to agree, and they would only agree when results are good. That breaks the acquisition rule that "bad results are published the same way as good ones, or not at all". |
| The old offer: first 25 firms, 2 years, for a case study | ₹22.5 L a year | Locks 72% of the break-even base at an early price, and has the same consent problem. Rejected. |

Publishing is a separate question for every firm, paying or not: at the end of the pilot we ask whether its scorecard may be published, named or unnamed. The firm decides, and no price depends on the answer.

[^share_monetizely]: Monetizely
[^share_mistral]: Mistral VC
[^share_monolit]: Monolit
[^mckinsey]: McKinsey 2025
[^prof]: Professor feedback
[^conflicts]: Source conflicts rows 11 and 12
[^proto]: Prototype screens
