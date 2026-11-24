---
type: Research Note
title: "Competitor comparison: named plans, read on 2026-11-24"
description: "Named competitor plans with list price, billing basis, minimum and what each plan includes, converted to rupees per seat per month, compared like for like on features Sphyr really has, with the rows that are not comparable and why."
tags: [pricing, competitors, india]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T17:51:30Z }
status: draft
sources:
  - id: lattice
    resource: https://lattice.com/pricing
    title: "Lattice pricing page (accessed 2026-11-24)"
  - id: fifteen
    resource: https://www.15five.com/pricing
    title: "15Five pricing page (accessed 2026-11-24)"
  - id: leapsome
    resource: https://www.leapsome.com/pricing
    title: "Leapsome pricing page (accessed 2026-11-24)"
  - id: peoplebox
    resource: https://www.peoplebox.ai/pricing
    title: "Peoplebox pricing page (accessed 2026-11-24)"
  - id: confirm
    resource: https://www.confirm.com/pricing
    title: "Confirm (now WorkRamp) pricing page (accessed 2026-11-24)"
  - id: py_cost
    resource: https://www.performyard.com/articles/performance-management-software-cost
    title: "PerformYard, How Much Does Performance Management Software Cost? (accessed 2026-11-24)"
  - id: py_pricing
    resource: https://www.performyard.com/pricing
    title: "PerformYard pricing page and FAQ (accessed 2026-11-24)"
  - id: py_consulting
    resource: https://www.performyard.com/performance-management-for-consulting
    title: "PerformYard, Performance Management for Consulting Firms (accessed 2026-11-24, cited in strategy/positioning.md)"
  - id: cultureamp
    resource: https://www.cultureamp.com/pricing
    title: "Culture Amp pricing page (accessed 2026-11-24)"
  - id: keka
    resource: https://www.keka.com/pricing
    title: "Keka pricing page (accessed 2026-11-24)"
  - id: keka_base
    resource: https://www.hr.software/reviews/keka
    title: "hr.software, Keka review, last updated 17 Nov 2026 (third party, accessed 2026-11-24)"
  - id: greythr
    resource: https://www.greythr.com/pricing/
    title: "greytHR pricing page (accessed 2026-11-24)"
  - id: darwinbox
    resource: https://www.indianhrm.com/darwinbox-pricing
    title: "Indian HRM, Darwinbox pricing (third party and a competing vendor, accessed 2026-11-24)"
  - id: fx_usd
    resource: https://www.exchangerates.org.uk/USD-INR-exchange-rate-history.html
    title: "USD/INR close 92.8609 on 23 Nov 2026 (accessed 2026-11-24)"
  - id: fx_eur
    resource: https://www.exchangerates.org.uk/EUR-INR-exchange-rate-history.html
    title: "EUR/INR 102.7462 on 18 Nov 2026 (accessed 2026-11-24)"
  - id: model
    resource: pricing_model.py
    title: "Pricing model script, section 2"
---

# Competitor comparison

All plans were read on 2026-11-24. Rupee figures use $1 = ₹92.86 (23 Nov 2026)[^fx_usd] and €1 = ₹102.75 (18 Nov 2026)[^fx_eur] and come from [the pricing model](pricing_model.py), section 2. List prices only; volume discounts are not public.

## What the graded one-pager got wrong

It said "₹665 to 1,425 per employee a month for Leapsome, Lattice and Peoplebox" with no plan names. That band equals Peoplebox's G2 range of $7 to $15 at ₹95. Leapsome had no public price at the time. "Sphyr is one-fifth or less" was false at the low end: 149 / 665 = 22%. Indian HRMS modules, the alternative a consulting firm already has, were missing.

## Basis of comparison

Price per seat per month, billed annually, for the plan that delivers peer feedback and performance reviews, at a 150-person firm. Sphyr is a feedback layer only. It has no AI and no integrations (see [do not claim](../product/do_not_claim.md)). Where a competitor's plan bundles those, the row is marked.

## Global tools

| Product and plan | List price | Rupees per seat per month | Billing and minimum | What the plan includes (as shown on the page) |
|---|---|---|---|---|
| Lattice, Performance[^lattice] | $10 per seat per month | ₹929 | Billed annually, in USD only. Minimum annual agreement $4,000, which binds below 33 seats | Performance reviews, succession planning, promotions, PIPs, talent reviews, calibration; also meetings, weekly updates, feedback, Q&A boards |
| Lattice, Foundations bundle[^lattice] | $13 per seat per month | ₹1,207 | Same | Performance plus goals and OKRs, analytics, an AI agent and integrations |
| 15Five, Perform[^fifteen] | $11 per user per month | ₹1,021 | Billed annually | AI-assisted reviews, OKRs and goals, 360 feedback, talent matrix, career paths, AI insights |
| Leapsome, Performance Reviews module[^leapsome] | €7 per employee per month | ₹719 | Per employee per month, no setup fee, 14-day trial. Needs the HRIS foundation, shown as free until 31 Dec (€5 to €7 otherwise) | Review templates and automations, cross-cycle analytics, calibration, external reviewers. Goals and OKRs is a separate €4 module |
| Peoplebox, Performance Management[^peoplebox] | $8 per employee per month | ₹743 | Billed annually | OKRs and goals, business reviews, check-ins, anytime feedback |
| Peoplebox, Performance Management + 360 degree[^peoplebox] | $8 + $8 | ₹1,486 | Billed annually | Adds 360 reviews, "anonymous or transparent", with AI-driven reports |
| Confirm, now WorkRamp Perform[^confirm] | From $8 per user per month | ₹743 | Billed annually, quoted for a 200-person company | Performance visibility beyond self-reporting, AI review summaries, pulse surveys, manager coach |
| PerformYard[^py_cost][^py_pricing] | $5 to $15 per employee per month | ₹464 to ₹1,393 | Per seat, billed annually; firms of a few hundred or fewer sit in the upper half | All features included, onboarding, training and a dedicated support manager. Sells to consulting firms with project-based review cycles and client and peer feedback[^py_consulting] |
| Culture Amp[^cultureamp] | Not published | n/a | Quote only | Engage, Perform, AI coach |

## Indian HRMS review modules

| Product and plan | List price | Rupees per seat per month | Billing and minimum | What it includes |
|---|---|---|---|---|
| greytHR, Performance Management System add-on[^greythr] | ₹35 to ₹45 per user per month | ₹35 to ₹45 for the module; ₹127 with the plan it needs, at 150 staff | Add-on only on the Growth plan, ₹4,495 a month for 50 employees plus ₹85 per extra employee | Goals, reviews, appraisals |
| Keka, Growth plan[^keka][^keka_base] | ₹15,999 a month for up to 100 employees, then ₹150 per extra employee | ₹157 at 150 staff; ₹400 at 40; ₹152 at 400 | Monthly price; base from a third-party review, per-extra price from Keka's own page | Full HRMS and payroll, plus 360 reviews, continuous feedback, 9-box and bell-curve calibration, promotions, PIPs |
| Darwinbox[^darwinbox] | Not published | Reported ₹200 to ₹600, from a competing vendor's site | Quote only, by headcount and modules | Full HRMS suite |
| Zoho People | Not read | n/a | The pricing page refused automated access on 2026-11-24 | Not used |

## Like-for-like feature check

Only features Sphyr has today are compared. "Shown" means the competitor's pricing or product page names it; a blank means the page we read did not show it, not that the product lacks it.

| Feature Sphyr has | Lattice Perf. | 15Five Perform | Leapsome Reviews | Peoplebox + 360 | PerformYard | Keka Growth | greytHR PMS |
|---|---|---|---|---|---|---|---|
| Feedback from many colleagues, not only the manager | Shown (feedback) | Shown (360) | Shown | Shown (360) | Shown (peers, clients) | Shown (360, continuous feedback) | |
| A fixed light rhythm by default (Sphyr: every two weeks) | | | | | Any cadence, set by HR | | |
| Raters outside the firm (Sphyr: email invites) | | | Shown (external reviewers) | | Shown (clients) | | |
| Goals and OKR cascade | Separate $8 product | Shown | Separate €4 module | Shown | | | Shown (goals) |
| Trends across cycles for the employee and manager | | | Shown (cross-cycle analytics) | | Shown (running record) | Shown (insights) | |
| AI features (Sphyr: none) | In Foundations | Shown | | Shown | | | |
| Integrations (Sphyr: none, CSV import only) | Shown | Shown | Shown | Shown | | Part of HRMS | Part of HRMS |

## Which rows are comparable

- **Comparable:** Lattice Performance, 15Five Perform, Leapsome Performance Reviews, Peoplebox (with 360), Confirm Perform and PerformYard. Each sells a per-seat review and feedback module on its own. At list price they sit between ₹464 (PerformYard's low end, for firms of several hundred) and ₹1,486 per seat per month. Five of the six pages show AI features, integrations or both, which Sphyr does not have (Lattice, 15Five, Leapsome, Peoplebox, Confirm). PerformYard's pages we read showed neither. So these prices are a ceiling, not a target.
- **Partly comparable:** greytHR PMS at ₹35 to ₹45 is a real Indian review module, but it can only be bought on top of greytHR's Growth HRMS plan, and it runs reviews and appraisals, not frequent peer feedback.
- **Not comparable on price, but the real alternative:** Keka Growth at about ₹157 per seat buys a whole HRMS with payroll, and reviews come inside it. A firm that already pays this will ask why it should pay for reviews again. This is the anchor the managing partner will use.
- **Not comparable:** Darwinbox and Culture Amp (no list price), Zoho People (not read), Lattice Foundations (bundles AI and integrations).

## Anchors used for the price

| Anchor | Value | Why |
|---|---|---|
| Low, Indian | ₹35 to ₹157 per seat | What a firm pays today for review features inside or on top of its HRMS |
| High, global like-for-like | ₹719 to ₹1,021 per seat (Leapsome, Peoplebox, Confirm, Lattice, 15Five single modules) | What a dedicated review and feedback tool costs, with features Sphyr lacks |

The price decision is in [price and pilot](price_and_pilot.md).

[^lattice]: Lattice pricing
[^fifteen]: 15Five pricing
[^leapsome]: Leapsome pricing
[^peoplebox]: Peoplebox pricing
[^confirm]: Confirm / WorkRamp pricing
[^py_cost]: PerformYard cost article
[^py_pricing]: PerformYard pricing FAQ
[^py_consulting]: PerformYard consulting page
[^cultureamp]: Culture Amp pricing
[^keka]: Keka pricing
[^keka_base]: hr.software Keka review
[^greythr]: greytHR pricing
[^darwinbox]: Indian HRM on Darwinbox
[^fx_usd]: USD/INR rate
[^fx_eur]: EUR/INR rate
