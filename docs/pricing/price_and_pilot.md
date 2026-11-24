---
type: Research Note
title: "Price and pilot: the decided terms and why"
description: "The decided list price (Rs 149) against the margin floor, the value and the competitor anchors, why it captures only part of the value, what it includes, the decided pilot terms, and the alternatives considered and not adopted (Rs 199, refund options, price lock)."
tags: [pricing, pilot, consulting, india]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T18:18:08Z }
status: draft
sources:
  - id: decision
    resource: ../decisions/decision_log.md
    title: "Decision log, 2026-11-24: Price and pilot (gate 1b)"
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
    title: "Pricing model script, sections 5 to 8"
---

# Price and pilot

Inputs come from the [value model](value_model.md), the [competitor comparison](competitor_comparison.md) and [cost and break-even](cost_and_breakeven.md). Numbers are printed by [the pricing model](pricing_model.py). The terms below were decided by the team at gate 1b.[^decision] They are our pricing, not facts from the product sources.

## Decided terms

- **Price: ₹149 per employee per month, billed yearly, plus GST.** The same price for every employee and every firm size.
- **Pilot: 12 weeks (six fortnightly cycles), up to 40 people, ₹25,000 plus GST.** Credited against the first annual bill if the firm signs.
- **If the firm does not sign:** it gets its data as a CSV file, and the rest is deleted. There is no refund.

## How the price was found

The order was fixed in advance, so no price was picked first: cost floor, then value, then competitor anchors, then value share, then price.

| Step | Result |
|---|---|
| 1. Margin floor at 80% gross margin, 150-person firm | ₹121 |
| 2. Value per seat per month | Low ₹209, mid ₹1,249, high ₹6,409 |
| 3. Competitor anchors | Indian: ₹35 to ₹45 (greytHR review add-on), about ₹157 (Keka's whole HRMS with reviews). Global dedicated tools: ₹464 (PerformYard's lowest) to ₹1,486; Peoplebox and Confirm from ₹743 |
| 4. Value share | 10% to 20% of mid value = ₹125 to ₹250 |
| 5. Rule | The price must clear the floor, sit inside the anchor band, and be no higher than the low-case value (₹209), so that a firm in the low case does not pay more than it gets |

Of ₹149, ₹199, ₹249 and ₹299, only ₹149 and ₹199 pass. ₹249 and ₹299 clear the floor and sit inside the anchors, but they are above the low-case value. The team chose ₹149.

| At a 150-person firm | ₹149 (decided) | ₹199 (considered) |
|---|---|---|
| Gross margin | 83.6% | 87.6% |
| Share of mid value | 11.9% | 15.9% |
| Firm's gain in the low case (value minus price) | ₹60 per seat | ₹10 per seat |
| Against Keka Growth's whole HRMS (₹157) | 95%, below it | 127%, above it |
| Against the lowest dedicated-tool price (₹464) | 32% | 43% |
| Firms of 150 needed to break even | 49 | 35 |
| Share of segment seats needed | 15% to 40% | 11% to 29% |
| Annual bill, 150 seats | ₹2,68,200 plus GST | ₹3,58,200 plus GST |
| Pays for itself if it prevents one exit every | 3.2 years | 2.4 years |

### Why ₹149

1. **It passes the rule with room in the low case.** A firm in the low case still gains ₹60 a seat a month. At ₹199 that gain would be only ₹10.
2. **It answers the HRMS comparison.** ₹149 is just below what Keka charges per seat for its whole HR system at 150 people. The managing partner does not have to accept that reviews cost more than the HR system.
3. **It clears the floor.** The graded ₹149 sat below its own ₹150 floor. With costs itemised and AI removed, the floor is ₹121, and ₹149 clears it by ₹28 at 83.6% gross margin.
4. **It stays inside the value-share norm.** ₹149 is 11.9% of mid value. The usual rule of thumb is 10% to 20%, from three practitioner sources, not from a study.[^share_monetizely][^share_mistral][^share_monolit]
5. **It is easy to say to a managing partner.** At 150 people, ₹2.68 L a year pays for itself if Sphyr prevents one voluntary exit every 3.2 years, against about 18 such exits a year in a firm that size (mid case).
6. **It keeps the price the professor already graded.** Only the reasoning behind it changes.

### The cost of ₹149, said plainly

- **It needs more firms.** Break-even takes about 49 firms of 150 people, against 35 at ₹199. That is 15% to 40% of every professional in the segment, and about two years at two new firms a month (see [cost and break-even](cost_and_breakeven.md)).
- **Small firms run at a low margin.** At 40 people, gross margin is 67%, below the 80% target.

### Why exactly 149

₹149 sits ₹28 above the ₹121 floor, so its ending does not cut into the margin. Indian HR software list prices often end in 9 or 5, for example Keka's ₹15,999 and greytHR's ₹2,495 and ₹4,495 (see the [competitor comparison](competitor_comparison.md)). ₹149 follows that habit. Nothing more rests on it.

## Why the price captures only part of the value

- **The value is our estimate.** No study shows Sphyr reduces exits. The firm carries the risk that the estimate is wrong, so it keeps most of the gain.
- **A new vendor with no customers.** Sphyr has no reviews or references. McKinsey reports that eight in ten B2B decision makers will look for another vendor if performance guarantees, such as a refund when milestones are not met, are not offered.[^mckinsey] Sphyr offers no refund, so a low price and a short pilot carry that risk instead: the firm puts ₹25,000 and 12 weeks at stake, not ₹2,68,200 for a year.
- **Budget authority.** The head of talent gets one new budget ask a year (see the [head of talent persona](../strategy/persona_head_of_talent.md)), and the managing partner signs. A bill of about ₹2.7 L a year for 150 people is a size we expect a managing partner can approve without a long process. That is an ESTIMATE to test in the pilot calls.
- **Competitor anchors.** The firm already pays for an HRMS. A price above the Indian anchor would make the comparison about price, not about the record.

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

### Fee: ₹25,000 plus GST, up to 40 people

| | 25 people | 40 people |
|---|---|---|
| Cost to serve for 12 weeks | ₹25,324 | ₹25,965 |
| List price for the same seats and weeks | ₹10,293 | ₹16,468 |

Cost to serve is 30 hours of customer success time (20 hours of onboarding plus 10 for the pilot: the written success test, a mid-pilot check and the scorecard report and review) at ₹809 an hour, plus variable costs for 2.76 months. The fee is set at that cost, so Sphyr earns nothing on a pilot. It is above list price for the same seats because onboarding is the same work for 25 people as for 150. The graded ₹15,000 was below the cost of a 12-week pilot.

### If the firm signs

The ₹25,000 is credited against the first annual bill. At 150 seats that is 9.3% of a ₹2,68,200 first year.

### If the firm does not sign

The firm gets all its ratings and comments as a CSV file, and the rest of its data is deleted. The prototype has no self-serve export screen, so the CSV is prepared by hand. The fee is not refunded. The deletion is an operational commitment, not a compliance claim. Invoices are kept, because tax law needs them.

Not yet set by the decision: how long after the last cycle the credit stays open, and how many days the CSV and the deletion take. We suggest 60 days for the credit, 7 days for the CSV and 30 days for deletion, for the team to confirm.

The professor wrote that "refund promises" belong to "sales and marketing strategy" and are "not central to the packaging experience".[^prof] So these terms live here and in the acquisition plan, not on the first-use or packaging pages.

## Considered, not adopted

These were analysed and left out at gate 1b to keep the scope to what the final brief asks.[^decision] They stay here as backing in case the team revisits them.

| Option | What it was | Why it was considered | Status |
|---|---|---|---|
| ₹199 list price | The analysis above | 35 firms to break even instead of 49 | Not adopted: thin low-case gain (₹10), above Keka's whole HRMS |
| Conditional refund | Refund the fee if the firm had 80% participation in at least 5 of 6 cycles and fewer than half its partners said the record showed something new | Buyers look for performance guarantees.[^mckinsey] Worst-case cost ₹50,000 for 4 pilots at 50% conversion, 5.5% of one month's fixed cost | Not adopted |
| Full refund for any firm that does not sign | Refund on request | Strongest risk reversal | Not adopted: pays for firms that change their mind for unrelated reasons |
| Partial refund | Part of the fee back | A middle way | Not adopted: adds an argument about the amount |
| Price lock for the first 10 firms, 24 months | Keep the launch price if the list rises | Lowers new-vendor price risk. If the list rose by ₹50, ₹9 L a year forgone; 10 firms are 21% of the 49 needed | Not adopted |
| Price lock in exchange for a case study (the graded offer: 25 firms, 2 years) | Lock tied to publication | Builds proof | Not adopted: pressures firms to publish only good results, and 25 firms are 51% of the break-even base |
| Start by 7 January 2027 | Six cycles before a 1 April 2027 appraisal round need a start 44 days from 2026-11-24 | Lets the record feed the April calibration | Not adopted as a sales push. The calendar fact stands: a pilot that starts later ends after April |

Publishing results stays a separate, consent-only question for every firm: at the end of the pilot we ask whether its scorecard may be published, named or unnamed. No price depends on the answer.

[^decision]: Decision log, gate 1b
[^share_monetizely]: Monetizely
[^share_mistral]: Mistral VC
[^share_monolit]: Monolit
[^mckinsey]: McKinsey 2025
[^prof]: Professor feedback
[^conflicts]: Source conflicts rows 11 and 12
[^proto]: Prototype screens
