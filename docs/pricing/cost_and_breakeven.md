---
type: Research Note
title: "Cost to serve, margin floor, fixed cost and break-even"
description: "Every variable cost per seat by line, GST treatment, the margin floor that follows, the monthly fixed cost by named line, contribution and break-even in seats and firms for each candidate price, compared with the size of the segment, plus the model script."
tags: [pricing, costs, break-even, india]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T18:11:26Z }
status: draft
sources:
  - id: ses
    resource: https://aws.amazon.com/ses/pricing/
    title: "Amazon SES pricing, Essentials $0.16 per 1,000 emails (accessed 2026-11-24)"
  - id: ec2
    resource: https://instances.vantage.sh/aws/ec2/t4g.medium
    title: "Vantage, EC2 t4g.medium, $0.034 per hour on demand, starting price (accessed 2026-11-24)"
  - id: rds
    resource: https://instances.vantage.sh/aws/rds/db.t4g.medium
    title: "Vantage, RDS db.t4g.medium, $0.065 per hour on demand, starting price (accessed 2026-11-24)"
  - id: razorpay
    resource: https://razorpay.com/pricing/
    title: "Razorpay pricing, 2% standard platform fee plus GST (accessed 2026-11-24)"
  - id: gst
    resource: https://www.easexpense.com/blogs/gst-saas-subscriptions-india-buyer-guide
    title: "EaseExpense, GST on SaaS India: SAC 998313 and 998314, 18% (accessed 2026-11-24)"
  - id: itc
    resource: https://sekin.in/how-to-claim-gst-input-tax-credit-on-software-subscriptions-in-india-2026-guide/
    title: "Sekin, GST input tax credit on software subscriptions, 2026 guide (accessed 2026-11-24)"
  - id: gm
    resource: https://www.arraycapital.com/insights/saas-operating-benchmarks/
    title: "Array Capital, SaaS operating benchmarks 2026, citing Benchmarkit CY2024: median gross margin 77%, subscription-only 81% (accessed 2026-11-24)"
  - id: ab_fullstack
    resource: https://www.ambitionbox.com/profile/full-stack-developer-salary
    title: "AmbitionBox, Full Stack Developer salary in India: average Rs 9.6 L, top 10% above Rs 13.4 L, 55,000+ salaries (accessed 2026-11-24)"
  - id: ab_csm
    resource: https://www.ambitionbox.com/profile/customer-success-manager-salary
    title: "AmbitionBox, Customer Success Manager salary in India: average Rs 14.7 L, 12,000+ salaries (accessed 2026-11-24)"
  - id: ab_designer
    resource: https://www.ambitionbox.com/profile/product-designer-salary
    title: "AmbitionBox, Product Designer salary in India: average Rs 15 L, 11,000+ salaries (accessed 2026-11-24)"
  - id: ab_sales
    resource: https://www.ambitionbox.com/profile/inside-sales-executive-salary
    title: "AmbitionBox, Inside Sales Executive salary in India: average Rs 4.6 L, 9,600+ salaries (accessed 2026-11-24)"
  - id: channel
    resource: ../strategy/channel_plan.md
    title: "Channel plan, paid layer cap of about Rs 1,50,000 in the first quarter"
  - id: segment
    resource: ../strategy/segment.md
    title: "Segment, guessed 150 to 400 firms and 18,000 to 48,000 seats"
  - id: model
    resource: pricing_model.py
    title: "Pricing model script, sections 3 to 5 and 8"
---

# Cost to serve, margin floor and break-even

Numbers come from [the pricing model](pricing_model.py), sections 3 to 5 and 8, pasted in the appendix with its output. Inputs marked ESTIMATE have no direct source; the reason is given.

## What the graded one-pager got wrong

It showed one lump, "₹30 to serve one employee a month: hosting, AI, support, payments", and "₹8 L fixed costs a month" with no lines. Sphyr has no AI (see [do not claim](../product/do_not_claim.md)), so that line goes. Setup, training and support were "included" in the price, but their labour cost appeared nowhere. GST was not mentioned.

## Variable cost per seat per month

At the 150-person reference firm and a ₹199 price.

| Line | ₹ per seat per month | Basis |
|---|---|---|
| Hosting that grows with seats | 1.00 | ESTIMATE: storage, compute and bandwidth. A fortnightly five-click card is a very light workload. |
| Email (invites, reminders, digests) | 0.12 | ESTIMATE 8 emails per seat per month x Amazon SES $0.16 per 1,000.[^ses] |
| Support | 13.48 | ESTIMATE 0.05 tickets per seat per month x 20 minutes, at ₹809 an hour (customer success manager, ₹14.7 L average CTC[^ab_csm] x 1.1 employer cost / 2,000 hours). |
| Onboarding, paid back over 12 months | 8.98 | ESTIMATE 20 hours per firm (kickoff 1, import and setup 4, training 3, first-cycle support 6, handover 1, preparation 5) x ₹809 / 12 months / 150 seats. Setup, training and support are part of the offer, so their cost sits here. |
| Payment fees | 1.17 | Razorpay 2% plus 18% GST on the fee.[^razorpay] ESTIMATE: a quarter of invoices paid by card or UPI, the rest by bank transfer at no fee. |
| **Total** | **24.75** | |

GST is not a cost. Sphyr charges 18% GST on top of the price (SaaS falls under SAC 998313 and 998314 at 18%).[^gst] A GST-registered firm can usually claim it back as input tax credit.[^itc] GST Sphyr pays on its own inputs, such as AWS and tools, is credited the same way. Tax deducted at source by the buyer affects cash flow, not cost; its rate is not checked here and must be confirmed with a chartered accountant.

## Margin floor

The floor is the lowest price that still gives the target gross margin:

```
floor = per-seat costs that do not depend on price / (1 - target margin - payment fee share)
```

Target gross margin is 80%. The median for private SaaS was 77% in 2024, and 81% for subscription revenue only (Benchmarkit, via Array Capital).[^gm] Sphyr is subscription only, so 80% is the right floor.

| Firm size | Floor at 80% margin | Gross margin at ₹199 |
|---|---|---|
| 40 | ₹249 | 75.1% |
| 150 | ₹121 | 87.6% |
| 400 | ₹93 | 90.4% |

Onboarding is a cost per firm, so small firms cost more per seat. At 40 people, ₹199 gives 75%, below the target. This is accepted: 40 is the bottom of the segment, and a setup fee would break the flat price that is part of the offer. The 150-person floor of ₹121 is the one used for the price decision.

## Fixed cost per month

| Line | ₹ per month | Basis |
|---|---|---|
| Founder, product and sales (1 FTE) | 1,83,333 | ESTIMATE ₹20 L CTC, paid like a senior customer success manager or designer |
| Founder, engineering (1 FTE) | 1,83,333 | ESTIMATE, same |
| Full-stack engineers (2 FTE) | 2,45,667 | ₹13.4 L each, the top-10% level on AmbitionBox[^ab_fullstack] |
| Product designer (0.5 FTE) | 68,750 | ₹15 L average[^ab_designer] |
| Inside sales, research and outreach (1 FTE) | 42,167 | ₹4.6 L average[^ab_sales] |
| Infrastructure base | 21,678 | 2 app servers at $0.034 an hour[^ec2] and a two-node database at $0.065 an hour each,[^rds] plus $50 for backups and monitoring, plus 20% because the prices read are starting prices, not confirmed for the Mumbai region |
| Software tools | 30,000 | ESTIMATE: workspace email, code hosting, design, CRM, monitoring for about 6 people |
| Sales and marketing, paid layer | 50,000 | The channel plan caps paid spend at about ₹1,50,000 in the first quarter[^channel] |
| Travel for sales and onboarding | 25,000 | ESTIMATE: visits to firms in Mumbai, Delhi NCR and Bengaluru |
| Accounting, legal and compliance | 25,000 | ESTIMATE: chartered accountant for GST, TDS and company filings, contract templates. No security certification is claimed or budgeted. |
| Office | 32,000 | ESTIMATE: 4 co-working seats |
| Support | 0 here | Counted as a variable cost above, at the customer success hourly rate, because it grows with seats. At break-even it is about 1,735 hours a year, 0.87 of a full-time person. Until then the founders do it. |
| **Total** | **9,06,928** | People are ₹7,23,250 of it. Salaries include 10% employer cost on top of CTC (ESTIMATE). |

The old ₹8 L was close in size, but had no lines behind it.

## Contribution and break-even, by candidate price

At the 150-person reference firm. Contribution = price minus every variable cost above.

| Price per seat per month | Variable cost | Contribution | Gross margin | Break-even seats | Firms of 150 | Share of segment seats |
|---|---|---|---|---|---|---|
| ₹149 | ₹24.5 | ₹124.5 | 83.6% | 7,282 | 49 | 15% to 40% |
| ₹199 | ₹24.8 | ₹174.2 | 87.6% | 5,205 | 35 | 11% to 29% |
| ₹249 | ₹25.0 | ₹224.0 | 89.9% | 4,050 | 27 | 8% to 22% |
| ₹299 | ₹25.3 | ₹273.7 | 91.5% | 3,314 | 22 | 7% to 18% |

The share uses the segment's own guess of 18,000 to 48,000 seats in 150 to 400 firms.[^segment] That guess is unverified.

### Break-even by firm size

Onboarding is a cost per firm, so contribution per seat is lower in small firms. If every customer were the same size:

| Price | Firm size | Contribution per seat | Break-even seats | Firms needed |
|---|---|---|---|---|
| ₹149 | 40 | ₹99.8 | 9,084 | 227 |
| ₹149 | 150 | ₹124.5 | 7,282 | 49 |
| ₹149 | 400 | ₹130.2 | 6,968 | 17 |
| ₹199 | 40 | ₹149.5 | 6,065 | 152 |
| ₹199 | 150 | ₹174.2 | 5,205 | 35 |
| ₹199 | 400 | ₹179.9 | 5,042 | 13 |

At ₹199, a business of 40-person firms needs 152 of them, about the whole low end of the segment's guessed 150 to 400 firms. Small firms cannot carry Sphyr alone; it has to win firms of 150 people and more.

### The finding

Break-even needs a large share of a small segment. At ₹199, Sphyr must sign about 35 firms of 150 people, which is 11% to 29% of every professional in the segment. At ₹149 it is 15% to 40%. For a new vendor with no customers, the top of either range is not realistic. Three things follow:

1. The fixed team must stay this lean (two founders, two engineers, half a designer, one researcher) until revenue arrives.
2. If Van Westendorp results allow a higher price, the break-even share falls fastest there (see [validation plan](validation_plan.md)).
3. Selling effort should go first to firms of 150 people and more (see the table above).
4. Long term, Sphyr likely needs adjacent professional-services segments as well. That is a strategy question for the team, not settled here.

## Months to break-even

Run rate, not cash payback. It ignores churn and price changes. Start: 3 to 5 paid pilots before April (from the deliverable map), converting at the 50% threshold in the validation plan. Then a stated number of new 150-person firms a month (ESTIMATE).

| Pilots before April | New firms a month after that | Months to run-rate break-even |
|---|---|---|
| 3 | 1 | about 33 |
| 3 | 2 | about 17 |
| 3 | 3 | about 11 |
| 5 | 1 | about 32 |
| 5 | 2 | about 16 |
| 5 | 3 | about 11 |

Two new firms a month is the planning case, so break-even comes about a year and a half after the first sale.

## Appendix: the model script and its output

The same script is committed as [pricing_model.py](pricing_model.py). Run `python3 docs/pricing/pricing_model.py` from the repo root to reproduce every number in the pricing docs. "Rs" in the output means rupees.

### Output

```text
== 1. Value per seat per month ==

[low] exit cost parts (leaver CTC Rs 1,800,000):
  recruiter fee                Rs    149,940
  vacancy lost margin          Rs     55,923
  ramp lost revenue            Rs    260,088
  partner and HR hiring time   Rs     40,500
  client and knowledge loss    Rs          0
  total per exit               Rs    506,451  (0.28 x CTC)
  relative reduction in exits  2.0%
  exits avoided per seat/year  0.00141
  attrition value / seat / mo  Rs 59
  net review hours saved/yr    3.7 h at Rs 900/h
  staff time / mo              Rs 138
  partner time / mo            Rs 11
  review value / seat / mo     Rs 149 (incl. partner time)
  TOTAL value / seat / mo      Rs 209

[mid] exit cost parts (leaver CTC Rs 2,400,000):
  recruiter fee                Rs    300,000
  vacancy lost margin          Rs    149,129
  ramp lost revenue            Rs    346,784
  partner and HR hiring time   Rs     67,500
  client and knowledge loss    Rs          0
  total per exit               Rs    863,412  (0.36 x CTC)
  relative reduction in exits  6.0%
  exits avoided per seat/year  0.00720
  attrition value / seat / mo  Rs 518
  net review hours saved/yr    9.1 h at Rs 1,200/h
  staff time / mo              Rs 680
  partner time / mo            Rs 51
  review value / seat / mo     Rs 731 (incl. partner time)
  TOTAL value / seat / mo      Rs 1,249

[high] exit cost parts (leaver CTC Rs 3,100,000):
  recruiter fee                Rs    516,770
  vacancy lost margin          Rs    288,937
  ramp lost revenue            Rs    447,929
  partner and HR hiring time   Rs    108,000
  client and knowledge loss    Rs    310,000
  total per exit               Rs  1,671,636  (0.54 x CTC)
  relative reduction in exits  14.4%
  exits avoided per seat/year  0.02409
  attrition value / seat / mo  Rs 3,356
  net review hours saved/yr    23.0 h at Rs 1,500/h
  staff time / mo              Rs 2,873
  partner time / mo            Rs 180
  review value / seat / mo     Rs 3,053 (incl. partner time)
  TOTAL value / seat / mo      Rs 6,409

Firm view (same per-seat value at any size; shows how a firm saving becomes per seat):
   40 staff [low ] exits/yr   2.8, avoided/yr 0.06 (one every 17.8 yr), firm value/yr Rs     100,222 -> / 40 / 12 = Rs 209
   40 staff [mid ] exits/yr   4.8, avoided/yr 0.29 (one every  3.5 yr), firm value/yr Rs     599,423 -> / 40 / 12 = Rs 1,249
   40 staff [high] exits/yr   6.7, avoided/yr 0.96 (one every  1.0 yr), firm value/yr Rs   3,076,472 -> / 40 / 12 = Rs 6,409
  150 staff [low ] exits/yr  10.4, avoided/yr 0.21 (one every  4.7 yr), firm value/yr Rs     375,833 -> / 150 / 12 = Rs 209
  150 staff [mid ] exits/yr  18.0, avoided/yr 1.08 (one every  0.9 yr), firm value/yr Rs   2,247,835 -> / 150 / 12 = Rs 1,249
  150 staff [high] exits/yr  25.1, avoided/yr 3.61 (one every  0.3 yr), firm value/yr Rs  11,536,769 -> / 150 / 12 = Rs 6,409
  400 staff [low ] exits/yr  27.6, avoided/yr 0.56 (one every  1.8 yr), firm value/yr Rs   1,002,221 -> / 400 / 12 = Rs 209
  400 staff [mid ] exits/yr  48.0, avoided/yr 2.88 (one every  0.3 yr), firm value/yr Rs   5,994,228 -> / 400 / 12 = Rs 1,249
  400 staff [high] exits/yr  66.9, avoided/yr 9.64 (one every  0.1 yr), firm value/yr Rs  30,764,718 -> / 400 / 12 = Rs 6,409

Old one-pager check: Rs 500/seat/mo at 100 staff = Rs 600,000 per avoided exit per year

== 2. Competitor anchors (Rs per seat per month) ==
USD/INR 92.86, EUR/INR 102.75
  Lattice                      Performance                            USD    10 = Rs    929  (min $4,000/yr binds below 33 seats)
  Lattice                      Foundations bundle                     USD    13 = Rs  1,207  (min $4,000/yr binds below 26 seats)
  15Five                       Perform                                USD    11 = Rs  1,021
  Leapsome                     Performance Reviews module, promo to 31 Dec EUR     7 = Rs    719
  Leapsome                     Reviews + foundation after promo, low  EUR    12 = Rs  1,233
  Leapsome                     Reviews + foundation after promo, high EUR    14 = Rs  1,438
  Peoplebox                    Performance Management                 USD     8 = Rs    743
  Peoplebox                    Performance Management + 360 degree    USD    16 = Rs  1,486
  Confirm (WorkRamp Perform)   Perform, from                          USD     8 = Rs    743
  PerformYard                  per-seat, low end                      USD     5 = Rs    464
  PerformYard                  per-seat, high end                     USD    15 = Rs  1,393
  Keka Growth (full HRMS incl. reviews) at  40 staff: Rs 400 per seat
  greytHR Growth + PMS add-on (Rs 40)   at  40 staff: Rs 152 per seat (PMS alone Rs 35 to 45)
  Keka Growth (full HRMS incl. reviews) at 150 staff: Rs 157 per seat
  greytHR Growth + PMS add-on (Rs 40)   at 150 staff: Rs 127 per seat (PMS alone Rs 35 to 45)
  Keka Growth (full HRMS incl. reviews) at 400 staff: Rs 152 per seat
  greytHR Growth + PMS add-on (Rs 40)   at 400 staff: Rs 126 per seat (PMS alone Rs 35 to 45)
  Old one-pager check: 149 / 665 = 22%, 149 / 1425 = 10%

== 3. Cost to serve per seat per month (at the 150-person reference firm) ==
  CS hourly cost Rs 809
  hosting per seat                         Rs   1.00
  email per seat                           Rs   0.12
  support per seat                         Rs  13.48
  onboarding, paid back over 12 months     Rs   8.98
  payment fees                             Rs   1.17
  total at price Rs 199                    Rs  24.75
  margin floor at 80% gross margin,  40-person firm: Rs 249; gross margin at Rs 199: 75.1%
  margin floor at 80% gross margin, 150-person firm: Rs 121; gross margin at Rs 199: 87.6%
  margin floor at 80% gross margin, 400-person firm: Rs 93; gross margin at Rs 199: 90.4%

== 4. Fixed cost per month ==
  Founder, product and sales (1 FTE)            Rs   183,333
  Founder, engineering (1 FTE)                  Rs   183,333
  Full-stack engineer (2 FTE)                   Rs   245,667
  Product designer (0.5 FTE)                    Rs    68,750
  Inside sales, research and outreach (1 FTE)   Rs    42,167
  infrastructure base                           Rs    21,678
  software tools                                Rs    30,000
  sales and marketing (paid layer)              Rs    50,000
  travel for sales and onboarding               Rs    25,000
  accounting, legal and compliance              Rs    25,000
  office (co-working)                           Rs    32,000
  TOTAL                                         Rs   906,928   (people Rs 723,250)

== 5. Price candidates (150-person firm) ==
  Rs 149: variable Rs  24.5, contribution Rs 124.5, GM 83.6%, share of mid value 11.9%, low-case value minus price Rs +60, break-even 7,282 seats = 49 firms of 150, 15% to 40% of segment seats
  Rs 199: variable Rs  24.8, contribution Rs 174.2, GM 87.6%, share of mid value 15.9%, low-case value minus price Rs +10, break-even 5,205 seats = 35 firms of 150, 11% to 29% of segment seats
  Rs 249: variable Rs  25.0, contribution Rs 224.0, GM 89.9%, share of mid value 19.9%, low-case value minus price Rs -40, break-even 4,050 seats = 27 firms of 150, 8% to 22% of segment seats
  Rs 299: variable Rs  25.3, contribution Rs 273.7, GM 91.5%, share of mid value 23.9%, low-case value minus price Rs -90, break-even 3,314 seats = 22 firms of 150, 7% to 18% of segment seats
  Rs 149 at 150 seats: Rs 268,200 a year plus GST = 0.31 mid-case exits; pays for itself if it prevents one exit every 3.2 years
  Rs 199 at 150 seats: Rs 358,200 a year plus GST = 0.41 mid-case exits; pays for itself if it prevents one exit every 2.4 years
  Rs 199 vs lowest dedicated-tool list price (PerformYard low end) Rs 464: 43%; vs Peoplebox and Confirm Rs 743: 27%; vs Leapsome promo Rs 719: 28%; vs Keka Growth at 150: 127%
  Price rule: floor Rs 121 <= price <= low-case value Rs 209; passes: 149, 199

== 5b. Break-even by firm size at Rs 149 and Rs 199 ==
  Rs 149, all firms of  40: contribution Rs  99.8, 9,084 seats = 227 firms (segment guess: 150 to 400 firms)
  Rs 149, all firms of 150: contribution Rs 124.5, 7,282 seats = 49 firms (segment guess: 150 to 400 firms)
  Rs 149, all firms of 400: contribution Rs 130.2, 6,968 seats = 17 firms (segment guess: 150 to 400 firms)
  Rs 199, all firms of  40: contribution Rs 149.5, 6,065 seats = 152 firms (segment guess: 150 to 400 firms)
  Rs 199, all firms of 150: contribution Rs 174.2, 5,205 seats = 35 firms (segment guess: 150 to 400 firms)
  Rs 199, all firms of 400: contribution Rs 179.9, 5,042 seats = 13 firms (segment guess: 150 to 400 firms)

== 6. Pilot ==
  25 seats, 12 weeks (2.76 months): cost to serve Rs 25,344, list price for same seats and time Rs 13,747
  40 seats, 12 weeks (2.76 months): cost to serve Rs 25,998, list price for same seats and time Rs 21,995
  Proposed fee Rs 25,000: per seat-month at 40 seats Rs 226, at 25 seats Rs 362
  4 pilots, 50% convert, every non-converting pilot refunded (worst case): Rs 50,000 = 5.5% of one month's fixed cost
  5 pilots, 50% convert, every non-converting pilot refunded (worst case): Rs 62,500 = 6.9% of one month's fixed cost
  Firm's exposure in a pilot Rs 25,000 vs a first year at 150 seats Rs 358,200
  Fee as credit against a first annual bill at 150 seats: 7.0% of Rs 358,200
  Latest start for 6 cycles before 2027-04-01: 2027-01-07 (44 days after 2026-11-24)

== 7. Price lock for early firms ==
  10 firms of 150 locked at Rs 199, if list rises by Rs 50: Rs 900,000 a year of forgone revenue
  25 firms of 150 locked at Rs 199, if list rises by Rs 50: Rs 2,250,000 a year of forgone revenue
  10 firms of 150 locked at Rs 199, if list rises by Rs 100: Rs 1,800,000 a year of forgone revenue
  Break-even needs 35 firms of 150; 10 locked firms = 29%, 25 = 72%

== 8. Months to break-even (ESTIMATE ramp) ==
  Customer success hours a year at break-even: 1,735 h = 0.87 FTE (paid as variable cost at Rs 809/h)
  3 pilots x 50% = 1.5 firms, then 1 new firms a month: run-rate break-even after about 33 months
  3 pilots x 50% = 1.5 firms, then 2 new firms a month: run-rate break-even after about 17 months
  3 pilots x 50% = 1.5 firms, then 3 new firms a month: run-rate break-even after about 11 months
  5 pilots x 50% = 2.5 firms, then 1 new firms a month: run-rate break-even after about 32 months
  5 pilots x 50% = 2.5 firms, then 2 new firms a month: run-rate break-even after about 16 months
  5 pilots x 50% = 2.5 firms, then 3 new firms a month: run-rate break-even after about 11 months
```

### Source

```python
"""Sphyr pricing model for Indian management consulting firms (40 to 400 professionals).

Run: python3 docs/pricing/pricing_model.py
Every input carries a source key (see the pricing docs' `sources` frontmatter) or the word
ESTIMATE with its reason. Money is in Indian rupees. L = lakh = 100,000.
"""

L = 100_000
CASES = ("low", "mid", "high")

# == 1. value per seat ==
VALUE = {
    # annual VOLUNTARY attrition rate (the exit-reason shares below are shares of voluntary leavers)
    # low: SPI 2025 Table 170, voluntary, 101 to 300 staff (global PS firms)
    # mid: Aon India 2025, voluntary 12.0% of 16.2% total (Business Today, 2 Mar 2026)
    # high: Aon India 2024 professional services 22.1% total x voluntary share in 2024
    #       (13.4% of 17.7% all-industry); the share applied to one sector is an ESTIMATE
    "attrition": {"low": 0.069, "mid": 0.120, "high": 0.221 * 13.4 / 17.7},
    # annual CTC of the person who leaves (consultant band)
    # low: Praxis senior associate consultant 17.8 to 19.7 L; mid: management consultant at
    # Avalon 21.5 to 24.5 L and Praxis 22.7 to 27.2 L; high: Praxis senior consultant 29.8 to 32.9 L
    "leaver_ctc": {"low": 18 * L, "mid": 24 * L, "high": 31 * L},
    # recruiter fee as share of first-year CTC (hirekey, savannahr)
    "recruiter_fee": {"low": 0.0833, "mid": 0.125, "high": 0.1667},
    # days to recruit and days to become productive (SPI 2025 Table 170, 101 to 300)
    "vacancy_days": {"low": 75.6, "mid": 75.6, "high": 75.6},
    "ramp_days": {"low": 58.6, "mid": 58.6, "high": 58.6},
    # ESTIMATE: share of vacancy days whose work is lost rather than covered by others
    "vacancy_uncovered": {"low": 0.25, "mid": 0.50, "high": 0.75},
    # ESTIMATE: average output during ramp
    "ramp_productivity": {"low": 0.5, "mid": 0.5, "high": 0.5},
    # ESTIMATE: loaded cost = CTC x 1.2 (office, tools, benefits not in CTC)
    "loading": {"low": 1.2, "mid": 1.2, "high": 1.2},
    # revenue per billable consultant / fully loaded cost (SPI 2025: $204k / $136k, 101 to 300)
    "revenue_to_cost": {"low": 1.5, "mid": 1.5, "high": 1.5},
    # ESTIMATE: partner and manager hours to interview and onboard one replacement
    "hiring_hours": {"low": 15, "mid": 25, "high": 40},
    # ESTIMATE: hourly loaded cost of that senior time (about 45 L CTC x 1.2 / 2,000 h)
    "senior_hourly": {"low": 2700, "mid": 2700, "high": 2700},
    # ESTIMATE: client and knowledge loss as share of leaver CTC, only in the high case
    "client_loss": {"low": 0.0, "mid": 0.0, "high": 0.10},
    # share of exits whose stated reason Sphyr could touch
    # low: SPI 2025 Table 172, lack of career advancement 14.9% + management dissatisfaction 5.5%
    # high: Gallup 2008, career advancement 31.5% + management and work environment 16.5%
    # mid: ESTIMATE between the two
    "exit_share_addressable": {"low": 0.204, "mid": 0.30, "high": 0.48},
    # ESTIMATE (no study exists for Sphyr): share of those exits Sphyr prevents
    "sphyr_effect": {"low": 0.10, "mid": 0.20, "high": 0.30},
    # review hours per person per year, firm-wide
    # low: Deloitte, about 2 million hours / 65,000 people (HBR 2015)
    # mid: CEB, 40 hours per employee (SHRM 2015)
    # high: CEB blend, 1 manager (210 h) per 5 employees (40 h each), span is an ESTIMATE
    "review_hours": {"low": 2_000_000 / 65_000, "mid": 40.0, "high": (5 * 40 + 210) / 6},
    # ESTIMATE: share of those hours Sphyr removes (project-end forms, chasing, building "the
    # file" before calibration). The calibration meeting itself stays.
    "hours_saved_share": {"low": 0.15, "mid": 0.25, "high": 0.35},
    # time Sphyr adds: 26 fortnightly cycles x 2 min 09 s per deck (whitepaper 2018 paper pilot)
    "sphyr_hours_added": {c: 26 * (2 + 9 / 60) / 60 for c in CASES},
    # ESTIMATE: blended firm-wide CTC per professional (pyramid of analysts to partners)
    "blended_ctc": {"low": 15 * L, "mid": 20 * L, "high": 25 * L},
    # ESTIMATE: share of saved hours that turns into billable or other useful work
    "time_realization": {"low": 0.5, "mid": 0.75, "high": 1.0},
    "work_hours_year": {c: 2000 for c in CASES},
    # ESTIMATE: partner hours per professional per year spent building and debating the record
    # before calibration (asking for "the file", reading forms, discussing each consultant)
    "partner_hours": {"low": 0.5, "mid": 1.0, "high": 2.0},
    # ESTIMATE: share of that partner time Sphyr removes (the record is already there)
    "partner_saved_share": {"low": 0.2, "mid": 0.3, "high": 0.4},
}


def exit_cost(c, v=VALUE):
    ctc = v["leaver_ctc"][c]
    loaded = ctc * v["loading"][c]
    revenue = loaded * v["revenue_to_cost"][c]
    parts = {
        "recruiter fee": ctc * v["recruiter_fee"][c],
        # seat empty: revenue lost minus cost saved, only for uncovered days
        "vacancy lost margin": (revenue - loaded) * v["vacancy_days"][c] / 365 * v["vacancy_uncovered"][c],
        # new hire paid in full, produces part of the revenue
        "ramp lost revenue": revenue * v["ramp_days"][c] / 365 * (1 - v["ramp_productivity"][c]),
        "partner and HR hiring time": v["hiring_hours"][c] * v["senior_hourly"][c],
        "client and knowledge loss": ctc * v["client_loss"][c],
    }
    return parts


def value_per_seat(c, v=VALUE):
    cost = sum(exit_cost(c, v).values())
    reduction = v["exit_share_addressable"][c] * v["sphyr_effect"][c]
    exits_avoided_per_seat = v["attrition"][c] * reduction
    attrition_year = exits_avoided_per_seat * cost
    hourly = v["blended_ctc"][c] * v["loading"][c] / v["work_hours_year"][c]
    net_hours = v["review_hours"][c] * v["hours_saved_share"][c] - v["sphyr_hours_added"][c]
    review_year = net_hours * hourly * v["time_realization"][c]
    partner_year = (v["partner_hours"][c] * v["partner_saved_share"][c] * v["senior_hourly"][c]
                    * v["time_realization"][c])
    review_year += partner_year
    return {
        "partner_month": partner_year / 12,
        "exit_cost": cost,
        "exit_cost_x_ctc": cost / v["leaver_ctc"][c],
        "relative_reduction": reduction,
        "exits_avoided_per_seat_year": exits_avoided_per_seat,
        "attrition_month": attrition_year / 12,
        "net_hours_saved": net_hours,
        "hourly": hourly,
        "review_month": review_year / 12,
        "total_month": (attrition_year + review_year) / 12,
    }


def print_value():
    print("== 1. Value per seat per month ==")
    for c in CASES:
        parts = exit_cost(c)
        print(f"\n[{c}] exit cost parts (leaver CTC Rs {VALUE['leaver_ctc'][c]:,.0f}):")
        for k, x in parts.items():
            print(f"  {k:28s} Rs {x:>10,.0f}")
        r = value_per_seat(c)
        print(f"  {'total per exit':28s} Rs {r['exit_cost']:>10,.0f}  ({r['exit_cost_x_ctc']:.2f} x CTC)")
        print(f"  relative reduction in exits  {r['relative_reduction']:.1%}")
        print(f"  exits avoided per seat/year  {r['exits_avoided_per_seat_year']:.5f}")
        print(f"  attrition value / seat / mo  Rs {r['attrition_month']:,.0f}")
        print(f"  net review hours saved/yr    {r['net_hours_saved']:.1f} h at Rs {r['hourly']:,.0f}/h")
        print(f"  staff time / mo              Rs {r['review_month'] - r['partner_month']:,.0f}")
        print(f"  partner time / mo            Rs {r['partner_month']:,.0f}")
        print(f"  review value / seat / mo     Rs {r['review_month']:,.0f} (incl. partner time)")
        print(f"  TOTAL value / seat / mo      Rs {r['total_month']:,.0f}")
    print("\nFirm view (same per-seat value at any size; shows how a firm saving becomes per seat):")
    for n in (40, 150, 400):
        for c in CASES:
            r = value_per_seat(c)
            avoided = n * r["exits_avoided_per_seat_year"]
            firm_year = r["total_month"] * 12 * n
            yrs = 1 / avoided if avoided else float("inf")
            print(f"  {n:3d} staff [{c:4s}] exits/yr {n * VALUE['attrition'][c]:5.1f}, avoided/yr {avoided:4.2f}"
                  f" (one every {yrs:4.1f} yr), firm value/yr Rs {firm_year:>11,.0f}"
                  f" -> / {n} / 12 = Rs {firm_year / n / 12:,.0f}")
    # the graded one-pager's implied number: Rs 500 x 100 staff x 12 = Rs 6 L for one exit
    print(f"\nOld one-pager check: Rs 500/seat/mo at 100 staff = Rs {500 * 100 * 12:,} per avoided exit per year")


# == 2. competitor anchors ==
USD_INR = 92.86  # exchangerates.org.uk close 23 Nov 2026
EUR_INR = 102.75  # exchangerates.org.uk 18 Nov 2026
REF_FIRM = 150  # reference firm size (head of talent persona)

# (name, plan, price per seat per month in source currency, currency, minimum annual USD or None)
COMPETITORS = [
    ("Lattice", "Performance", 10, "USD", 4000),
    ("Lattice", "Foundations bundle", 13, "USD", 4000),
    ("15Five", "Perform", 11, "USD", None),
    # needs the HRIS foundation, free only until 31 Dec 2026 (shown as EUR 5 to 7 otherwise)
    ("Leapsome", "Performance Reviews module, promo to 31 Dec", 7, "EUR", None),
    ("Leapsome", "Reviews + foundation after promo, low", 12, "EUR", None),
    ("Leapsome", "Reviews + foundation after promo, high", 14, "EUR", None),
    ("Peoplebox", "Performance Management", 8, "USD", None),
    ("Peoplebox", "Performance Management + 360 degree", 16, "USD", None),
    ("Confirm (WorkRamp Perform)", "Perform, from", 8, "USD", None),
    ("PerformYard", "per-seat, low end", 5, "USD", None),
    ("PerformYard", "per-seat, high end", 15, "USD", None),
]


def inr(price, cur):
    return price * (USD_INR if cur == "USD" else EUR_INR if cur == "EUR" else 1)


def keka_growth_per_seat(n):
    # Rs 15,999 a month for up to 100 employees, then Rs 150 per extra employee
    return (15999 + max(0, n - 100) * 150) / n


def greythr_growth_plus_pms_per_seat(n, pms=40):
    # Growth Rs 4,495 a month with 50 employees, Rs 85 per extra; PMS add-on Rs 35 to 45
    return (4495 + max(0, n - 50) * 85) / n + pms


def print_competitors():
    print("\n== 2. Competitor anchors (Rs per seat per month) ==")
    print(f"USD/INR {USD_INR}, EUR/INR {EUR_INR}")
    for name, plan, p, cur, minimum in COMPETITORS:
        line = f"  {name:28s} {plan:38s} {cur} {p:>5} = Rs {inr(p, cur):>6,.0f}"
        if minimum:
            seats = minimum / 12 / p
            line += f"  (min ${minimum:,}/yr binds below {seats:.0f} seats)"
        print(line)
    for n in (40, REF_FIRM, 400):
        print(f"  Keka Growth (full HRMS incl. reviews) at {n:3d} staff: Rs {keka_growth_per_seat(n):,.0f} per seat")
        print(f"  greytHR Growth + PMS add-on (Rs 40)   at {n:3d} staff: Rs {greythr_growth_plus_pms_per_seat(n):,.0f} per seat"
              f" (PMS alone Rs 35 to 45)")
    old_low, old_high = 665, 1425
    print(f"  Old one-pager check: 149 / {old_low} = {149 / old_low:.0%}, 149 / {old_high} = {149 / old_high:.0%}")


# == 3. cost to serve and margin floor ==
# ESTIMATE: employer cost on top of CTC (insurance, laptop, leave cover)
EMPLOYER_LOADING = 1.10
# customer success hourly cost: AmbitionBox average CSM CTC Rs 14.7 L x loading / 2,000 h
CS_HOURLY = 14.7 * L * EMPLOYER_LOADING / 2000

VARIABLE = {
    # ESTIMATE: storage, compute and bandwidth that grow with seats, Rs per seat per month
    "hosting per seat": 1.0,
    # ESTIMATE 8 emails per seat per month (invites, reminders, digests) x SES $0.16 per 1,000
    "email per seat": 8 * 0.16 / 1000 * USD_INR,
    # ESTIMATE: 0.05 support tickets per seat per month x 20 min at CS hourly cost
    "support per seat": 0.05 * 20 / 60 * CS_HOURLY,
}
# ESTIMATE: onboarding hours per firm (kickoff 1, import and setup 4, training 3,
# first-cycle support 6, handover 1, preparation 5), paid back over 12 months
ONBOARDING_HOURS = 20
# Razorpay 2% + 18% GST on the fee; ESTIMATE share of invoices paid by card or UPI
# (the rest by bank transfer at no fee)
GATEWAY_FEE = 0.02 * 1.18
GATEWAY_SHARE = 0.25
TARGET_GM = 0.80  # Benchmarkit CY2024 median 77%, subscription-only 81%


def variable_cost_per_seat(price, firm=REF_FIRM):
    parts = dict(VARIABLE)
    parts["onboarding, paid back over 12 months"] = ONBOARDING_HOURS * CS_HOURLY / 12 / firm
    parts["payment fees"] = price * GATEWAY_FEE * GATEWAY_SHARE
    return parts


def floor_price(firm=REF_FIRM):
    # solve p = cost(p) / (1 - GM), where cost has a part proportional to p
    fixed_part = sum(v for k, v in variable_cost_per_seat(0, firm).items())
    share = GATEWAY_FEE * GATEWAY_SHARE
    return fixed_part / (1 - TARGET_GM - share)


# == 4. fixed cost and break-even ==
# monthly fixed cost by line, Rs. People are CTC per year from AmbitionBox unless ESTIMATE.
PEOPLE = [
    # (role, FTE, CTC per year, basis)
    ("Founder, product and sales", 1, 20 * L, "ESTIMATE, paid like a senior CSM or designer"),
    ("Founder, engineering", 1, 20 * L, "ESTIMATE, same"),
    ("Full-stack engineer", 2, 13.4 * L, "AmbitionBox top-10% full-stack Rs 13.4 L"),
    ("Product designer", 0.5, 15.0 * L, "AmbitionBox average Rs 15 L"),
    ("Inside sales, research and outreach", 1, 4.6 * L, "AmbitionBox average Rs 4.6 L"),
]
OTHER_FIXED = {
    # ESTIMATE from AWS list prices: 2 x t4g.medium ($0.034/h), RDS db.t4g.medium Multi-AZ
    # (2 x $0.065/h), backups, monitoring; +20% for Mumbai region and headroom
    "infrastructure base": ((2 * 0.034 + 2 * 0.065) * 730 + 50) * 1.2 * USD_INR,
    # ESTIMATE: workspace email, code hosting, design, CRM, monitoring for about 6 people
    "software tools": 30_000,
    # channel plan cap: about Rs 1,50,000 per quarter for the paid layer
    "sales and marketing (paid layer)": 150_000 / 3,
    # ESTIMATE: events, travel to firms in Mumbai, Delhi NCR, Bengaluru
    "travel for sales and onboarding": 25_000,
    # ESTIMATE: chartered accountant for GST, TDS and ROC filings; contract templates;
    # no security certification is claimed or budgeted
    "accounting, legal and compliance": 25_000,
    # ESTIMATE: 4 co-working seats
    "office (co-working)": 32_000,
}


def fixed_monthly():
    people = {f"{r} ({fte} FTE)": fte * ctc * EMPLOYER_LOADING / 12 for r, fte, ctc, _ in PEOPLE}
    return people, OTHER_FIXED


SEGMENT_SEATS = (18_000, 48_000)  # segment.md guess: 150 to 400 firms x about 120 professionals
CANDIDATES = (149, 199, 249, 299)


def print_costs_and_breakeven():
    print("\n== 3. Cost to serve per seat per month (at the 150-person reference firm) ==")
    print(f"  CS hourly cost Rs {CS_HOURLY:,.0f}")
    for price in (199,):
        parts = variable_cost_per_seat(price)
        for k, x in parts.items():
            print(f"  {k:40s} Rs {x:6.2f}")
        print(f"  {'total at price Rs ' + str(price):40s} Rs {sum(parts.values()):6.2f}")
    for n in (40, REF_FIRM, 400):
        var = sum(variable_cost_per_seat(199, n).values())
        print(f"  margin floor at {TARGET_GM:.0%} gross margin, {n:3d}-person firm: Rs {floor_price(n):,.0f};"
              f" gross margin at Rs 199: {(199 - var) / 199:.1%}")

    print("\n== 4. Fixed cost per month ==")
    people, other = fixed_monthly()
    for k, x in {**people, **other}.items():
        print(f"  {k:45s} Rs {x:>9,.0f}")
    fixed = sum(people.values()) + sum(other.values())
    print(f"  {'TOTAL':45s} Rs {fixed:>9,.0f}   (people Rs {sum(people.values()):,.0f})")

    print("\n== 5. Price candidates (150-person firm) ==")
    mid = value_per_seat("mid")["total_month"]
    low = value_per_seat("low")["total_month"]
    for p in CANDIDATES:
        var = sum(variable_cost_per_seat(p).values())
        contrib = p - var
        gm = contrib / p
        seats = fixed / contrib
        firms = seats / REF_FIRM
        pen = (seats / SEGMENT_SEATS[1], seats / SEGMENT_SEATS[0])
        print(f"  Rs {p}: variable Rs {var:5.1f}, contribution Rs {contrib:5.1f}, GM {gm:.1%}, "
              f"share of mid value {p / mid:.1%}, low-case value minus price Rs {low - p:+.0f}, "
              f"break-even {seats:,.0f} seats = {firms:.0f} firms of 150, "
              f"{pen[0]:.0%} to {pen[1]:.0%} of segment seats")
    mid_exit = value_per_seat("mid")["exit_cost"]
    for p in (149, 199):
        bill = p * REF_FIRM * 12
        print(f"  Rs {p} at {REF_FIRM} seats: Rs {bill:,} a year plus GST = {bill / mid_exit:.2f} mid-case exits;"
              f" pays for itself if it prevents one exit every {mid_exit / bill:.1f} years")
    print(f"  Rs 199 vs lowest dedicated-tool list price (PerformYard low end) Rs {inr(5, 'USD'):,.0f}:"
          f" {199 / inr(5, 'USD'):.0%}; vs Peoplebox and Confirm Rs {inr(8, 'USD'):,.0f}: {199 / inr(8, 'USD'):.0%};"
          f" vs Leapsome promo Rs {inr(7, 'EUR'):,.0f}: {199 / inr(7, 'EUR'):.0%};"
          f" vs Keka Growth at {REF_FIRM}: {199 / keka_growth_per_seat(REF_FIRM):.0%}")
    # rule in price_and_pilot.md: floor <= price <= low-case value, and inside the anchors
    print(f"  Price rule: floor Rs {floor_price():,.0f} <= price <= low-case value Rs {low:,.0f}; passes: "
          + ", ".join(str(p) for p in CANDIDATES if floor_price() <= p <= low))

    print("\n== 5b. Break-even by firm size at Rs 149 and Rs 199 ==")
    for p in (149, 199):
        for n in (40, REF_FIRM, 400):
            c = p - sum(variable_cost_per_seat(p, n).values())
            seats = fixed / c
            print(f"  Rs {p}, all firms of {n:3d}: contribution Rs {c:5.1f}, {seats:,.0f} seats = {seats / n:,.0f} firms"
                  f" (segment guess: 150 to 400 firms)")
    return fixed


# == 6. pilot ==
PRICE = 199  # recommended list price, see price_and_pilot.md
PILOT_WEEKS = 12  # 6 fortnightly cycles
PILOT_MAX_SEATS = 40
# ESTIMATE: extra hours for a pilot beyond normal onboarding: success test agreed in writing (2),
# mid-pilot check (2), scorecard report and review meeting (6)
PILOT_EXTRA_HOURS = 10


def print_pilot(fixed):
    print("\n== 6. Pilot ==")
    months = PILOT_WEEKS * 7 / 30.4
    for seats in (25, PILOT_MAX_SEATS):
        var = sum(v for k, v in variable_cost_per_seat(PRICE, seats).items()
                  if not k.startswith("onboarding"))
        cost = (ONBOARDING_HOURS + PILOT_EXTRA_HOURS) * CS_HOURLY + var * seats * months
        at_list = PRICE * seats * months
        print(f"  {seats} seats, {PILOT_WEEKS} weeks ({months:.2f} months): cost to serve Rs {cost:,.0f}, "
              f"list price for same seats and time Rs {at_list:,.0f}")
    fee = 25_000
    print(f"  Proposed fee Rs {fee:,}: per seat-month at 40 seats Rs {fee / (40 * months):,.0f}, "
          f"at 25 seats Rs {fee / (25 * months):,.0f}")
    # refund exposure under the recommended conditional refund (price_and_pilot.md)
    for pilots in (4, 5):
        worst = pilots * 0.5 * fee
        print(f"  {pilots} pilots, 50% convert, every non-converting pilot refunded (worst case): Rs {worst:,.0f}"
              f" = {worst / fixed:.1%} of one month's fixed cost")
    print(f"  Firm's exposure in a pilot Rs {fee:,} vs a first year at {REF_FIRM} seats Rs {PRICE * REF_FIRM * 12:,}")
    print(f"  Fee as credit against a first annual bill at 150 seats: "
          f"{fee / (PRICE * REF_FIRM * 12):.1%} of Rs {PRICE * REF_FIRM * 12:,}")
    # time check: 6 cycles before an April calibration round
    import datetime as dt
    april = dt.date(2027, 4, 1)
    start = april - dt.timedelta(weeks=PILOT_WEEKS)
    today = dt.date(2026, 11, 24)
    print(f"  Latest start for {PILOT_WEEKS // 2} cycles before {april}: {start} "
          f"({(start - today).days} days after {today})")

    print("\n== 7. Price lock for early firms ==")
    for n_firms, rise in ((10, 50), (25, 50), (10, 100)):
        cost = n_firms * REF_FIRM * rise * 12
        print(f"  {n_firms} firms of {REF_FIRM} locked at Rs {PRICE}, if list rises by Rs {rise}: "
              f"Rs {cost:,.0f} a year of forgone revenue")
    seats = fixed / (PRICE - sum(variable_cost_per_seat(PRICE).values()))
    print(f"  Break-even needs {seats / REF_FIRM:.0f} firms of {REF_FIRM}; 10 locked firms = "
          f"{10 / (seats / REF_FIRM):.0%}, 25 = {25 / (seats / REF_FIRM):.0%}")

    print("\n== 8. Months to break-even (ESTIMATE ramp) ==")
    contrib = PRICE - sum(variable_cost_per_seat(PRICE).values())
    firms = fixed / (contrib * REF_FIRM)
    cs_hours = firms * ONBOARDING_HOURS + firms * REF_FIRM * 0.05 * 20 / 60 * 12
    print(f"  Customer success hours a year at break-even: {cs_hours:,.0f} h = {cs_hours / 2000:.2f} FTE"
          f" (paid as variable cost at Rs {CS_HOURLY:,.0f}/h)")
    # run-rate break-even, not cash payback; ignores churn and price rises
    # start: 3 to 5 pilots before April (deliverable map), converting at the 50% threshold
    # in validation_plan.md; then ESTIMATED new firms a month
    for pilots in (3, 5):
        start_firms = pilots * 0.5
        for adds in (1, 2, 3):
            months = max(0.0, (firms - start_firms) / adds)
            print(f"  {pilots} pilots x 50% = {start_firms:.1f} firms, then {adds} new firms a month: "
                  f"run-rate break-even after about {months:.0f} months")


if __name__ == "__main__":
    print_value()
    print_competitors()
    fixed = print_costs_and_breakeven()
    print_pilot(fixed)
```

[^ses]: Amazon SES pricing
[^ec2]: Vantage EC2 t4g.medium
[^rds]: Vantage RDS db.t4g.medium
[^razorpay]: Razorpay pricing
[^gst]: EaseExpense on GST for SaaS
[^itc]: Sekin on input tax credit
[^gm]: Array Capital citing Benchmarkit
[^ab_fullstack]: AmbitionBox full-stack developer
[^ab_csm]: AmbitionBox customer success manager
[^ab_designer]: AmbitionBox product designer
[^ab_sales]: AmbitionBox inside sales executive
[^channel]: Channel plan
[^segment]: Segment
