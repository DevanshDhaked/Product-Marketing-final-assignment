---
type: Research Note
title: "Value model: what Sphyr is worth per professional per month"
description: "Value per seat per month for an Indian management consulting firm, from sourced exit costs, a stated change in exits and review hours saved, with the formula, low, mid and high cases, and how a firm saving becomes a per-seat figure."
tags: [pricing, value, consulting, india]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T17:43:57Z }
status: draft
sources:
  - id: aon26
    resource: https://www.aon.com/apac/in-the-press/asia-newsroom/2026/aon-survey-projects-slight-uptick-in-salaries-in-india-2026
    title: "Aon, Annual Salary Increase and Turnover Survey 2025-26 India, press release 24 Feb 2026 (accessed 2026-11-24)"
  - id: aon25
    resource: https://www.deccanchronicle.com/business/economics/india-salaries-to-rise-95-in-2025-1827815
    title: "Deccan Chronicle on Aon 2024-25 India survey, 3 Oct 2024 (accessed 2026-11-24)"
  - id: spi
    resource: https://get.kantata.com/rs/677-LEJ-696/images/2025-ps-maturity-benchmark.pdf
    title: "SPI Research, 2025 Professional Services Maturity Benchmark, Tables 170 and 172 (accessed 2026-11-24)"
  - id: praxis
    resource: https://www.ambitionbox.com/salaries/praxis-global-alliance-salaries
    title: "AmbitionBox, Praxis Global Alliance salaries, 402 salaries, updated 23 Nov 2026 (accessed 2026-11-24)"
  - id: avalon
    resource: https://www.ambitionbox.com/salaries/avalon-consulting-salaries
    title: "AmbitionBox, Avalon Consulting salaries, 273 salaries, updated 24 Nov 2026 (accessed 2026-11-24)"
  - id: hirekey
    resource: https://hirekey.in/blog/recruitment-agency-fee-structure-percentage/
    title: "HireKey, recruitment agency fee structure (accessed 2026-11-24)"
  - id: savannahr
    resource: https://savannahr.com/blog/recruitment-agency-fees-india-how-pricing-works
    title: "SavannaHR, recruitment agency fees in India (accessed 2026-11-24)"
  - id: gallup19
    resource: https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses-trillion.aspx
    title: "Gallup, This Fixable Problem Costs U.S. Businesses $1 Trillion, 13 Mar 2019 (accessed 2026-11-24)"
  - id: gallup24
    resource: https://www.gallup.com/workplace/646538/employee-turnover-preventable-often-ignored.aspx
    title: "Gallup, 42% of Employee Turnover Is Preventable but Often Ignored, 9 Jul 2024, updated 16 Feb 2026 (accessed 2026-11-24)"
  - id: gallup08
    resource: https://news.gallup.com/businessjournal/106912/turning-around-your-turnover-problem.aspx
    title: "Gallup Business Journal, Turning Around Employee Turnover, 8 May 2008 (accessed 2026-11-24)"
  - id: ceb
    resource: https://www.shrm.org/topics-tools/news/employee-relations/annual-performance-review-dead
    title: "SHRM, Is the Annual Performance Review Dead?, 19 Aug 2015, citing CEB (accessed 2026-11-24)"
  - id: hbr
    resource: https://hbr.org/2015/04/reinventing-performance-management
    title: "Buckingham and Goodall, Reinventing Performance Management, HBR April 2015 (accessed 2026-11-24)"
  - id: wp
    resource: "sphyr/Sphyr Overview Whitepaper v0.3.pdf"
    title: "Sphyr Overview Whitepaper v0.3, December 2018 (paper-and-pen pilot)"
  - id: model
    resource: pricing_model.py
    title: "Pricing model script, section 1"
---

# Value model

All numbers below are printed by [the pricing model](pricing_model.py), section 1. Nothing is hand-calculated. Inputs marked ESTIMATE have no direct source; the reason is given next to each.

## What the professor asked

The graded one-pager claimed ₹667 per employee per month: ₹500 from "one fewer resignation a year" and ₹167 from less review preparation. It did not show how one resignation becomes ₹500 for every employee every month. Working backwards: ₹500 x 100 staff x 12 months = ₹6,00,000. So the old number assumed a 100-person firm avoids one exit worth ₹6 L every year. It never said where ₹6 L or "one exit" came from.

This model fixes that by expressing avoided exits as a change in the attrition rate, not as "one resignation". Then the value does not depend on firm size, which is also why a flat per-seat price is coherent.

## The formula (per seat, per month)

```
value = [ a x s x e x X  +  (h x k - t) x w x r ] / 12
```

| Symbol | Meaning |
|---|---|
| a | annual attrition rate |
| s | share of exits whose reason Sphyr could touch (career advancement, management) |
| e | share of those exits Sphyr prevents |
| X | cost of one exit, in rupees |
| h | review hours per person per year |
| k | share of those hours Sphyr removes |
| t | hours Sphyr adds (filling cards) |
| w | loaded hourly cost of a professional |
| r | share of saved hours that turns into useful work |

`a x s x e` is the number of exits avoided per seat per year. At a firm of N people, avoided exits per year = `N x a x s x e`, and the firm saving divided by N and by 12 gives the same per-seat figure at any size.

## Inputs

| Input | Low | Mid | High | Source or reason |
|---|---|---|---|---|
| a, attrition | 6.9% | 16.2% | 22.1% | Low: SPI voluntary attrition, firms of 101 to 300 (global, 403 firms).[^spi] Mid: Aon India, all industries, 2025 (more than 1,400 organisations).[^aon26] High: Aon India, professional services, 2024.[^aon25] Aon figures may include involuntary exits. |
| Leaver CTC | ₹18 L | ₹24 L | ₹31 L | AmbitionBox: Praxis senior associate consultant ₹17.8 to 19.7 L (38 salaries), management consultant ₹22.7 to 27.2 L, senior consultant ₹29.8 to 32.9 L;[^praxis] Avalon management consultant ₹21.5 to 24.5 L, strategy consultant ₹22.3 to 27.9 L (14 salaries).[^avalon] Self-reported. |
| s, addressable share of exits | 20.4% | 30% | 48% | Low: SPI Table 172, "lack of career advancement" 14.9% + "management dissatisfaction" 5.5%.[^spi] High: Gallup 2008, career advancement 31.5% + management and work environment 16.5%.[^gallup08] Mid: ESTIMATE between them. |
| e, Sphyr effect on those exits | 10% | 20% | 30% | ESTIMATE. No study measures this for Sphyr. Ceiling check: Gallup finds 42% of voluntary leavers (n = 717, US) say the employer could have prevented the exit.[^gallup24] The pilot must measure this. |
| h, review hours per person per year | 30.8 | 40 | 68.3 | Low: Deloitte, close to 2 million hours for 65,000-plus people,[^hbr] a consulting firm with the same project-rating and consensus-meeting process. Mid: CEB, 40 hours per employee.[^ceb] High: CEB 210 hours per manager and 40 per employee, at an ESTIMATED 1 manager per 5 employees. |
| k, hours removed | 15% | 25% | 35% | ESTIMATE. Sphyr replaces project-end forms, chasing and building "the file" before calibration. The calibration meeting stays. |
| t, hours added | 0.93 | 0.93 | 0.93 | 26 cycles x 2 min 09 s per deck, from the 2018 whitepaper pilot.[^wp] That pilot was on paper, so this is a planning figure, not a software result. |
| w, hourly cost | ₹900 | ₹1,200 | ₹1,500 | ESTIMATE: blended firm CTC of ₹15, 20, 25 L (analysts to partners) x 1.2 loading / 2,000 hours. |
| r, time realised | 50% | 75% | 100% | ESTIMATE. Saved time is worth money only if it is used. |

### Cost of one exit (X), built from parts

| Part | Low | Mid | High | Basis |
|---|---|---|---|---|
| Recruiter fee | ₹1,49,940 | ₹3,00,000 | ₹5,16,770 | 8.33%, 12.5%, 16.67% of CTC (contingency fees for mid and senior roles in India).[^hirekey][^savannahr] |
| Lost margin while the seat is empty | ₹55,923 | ₹1,49,129 | ₹2,88,937 | 75.6 days to hire (SPI, 101 to 300 staff).[^spi] Lost revenue minus saved cost. Revenue / loaded cost = 1.5 (SPI, about $204k revenue per billable consultant, $136k loaded cost).[^spi] ESTIMATE: 25%, 50%, 75% of that time is not covered by others. |
| Lost revenue during ramp | ₹2,60,088 | ₹3,46,784 | ₹4,47,929 | 58.6 days to become productive (SPI).[^spi] ESTIMATE: 50% output during ramp. |
| Partner and HR hiring time | ₹40,500 | ₹67,500 | ₹1,08,000 | ESTIMATE: 15, 25, 40 hours at ₹2,700 an hour (about ₹45 L CTC x 1.2 / 2,000 h). |
| Client and knowledge loss | 0 | 0 | ₹3,10,000 | ESTIMATE: 10% of CTC, high case only. |
| **Total per exit** | **₹5,06,451** | **₹8,63,412** | **₹16,71,636** | |
| As a multiple of CTC | 0.28x | 0.36x | 0.54x | |

Cross-check: Gallup puts replacement at 0.5 to 2x salary,[^gallup19] and at about 80% of salary for professionals in technical roles.[^gallup24] Our build-up is lower in the low and mid cases on purpose: it counts only costs we can name. The model does not borrow Gallup's higher figures.

## Results

| Per seat per month | Low | Mid | High |
|---|---|---|---|
| Relative reduction in exits (s x e) | 2.0% | 6.0% | 14.4% |
| Exits avoided per seat per year | 0.0014 | 0.0097 | 0.0318 |
| Attrition value | ₹59 | ₹699 | ₹4,433 |
| Net review hours saved per year | 3.7 | 9.1 | 23.0 |
| Review time value | ₹138 | ₹680 | ₹2,873 |
| **Total value** | **₹198** | **₹1,379** | **₹7,306** |

The high case multiplies every favourable input together. It shows the upside, not a planning number. Pricing decisions use the low and mid cases.

## How a firm saving becomes a per-seat figure

| Firm size | Case | Exits a year | Avoided a year | One avoided exit every | Firm value a year | Divided by staff and 12 |
|---|---|---|---|---|---|---|
| 40 | low | 2.8 | 0.06 | 17.8 years | ₹94,822 | ₹198 |
| 40 | mid | 6.5 | 0.39 | 2.6 years | ₹6,62,155 | ₹1,379 |
| 150 | low | 10.4 | 0.21 | 4.7 years | ₹3,55,583 | ₹198 |
| 150 | mid | 24.3 | 1.46 | 0.7 years | ₹24,83,080 | ₹1,379 |
| 400 | low | 27.6 | 0.56 | 1.8 years | ₹9,48,221 | ₹198 |
| 400 | mid | 64.8 | 3.89 | 0.3 years | ₹66,21,547 | ₹1,379 |

Reading the 150-person mid row: the firm loses about 24 people a year. Sphyr prevents 6% of them, about 1.5 exits a year, each worth about ₹8.6 L. Adding the review hours saved, the firm gains about ₹24.8 L a year. ₹24.8 L / 150 / 12 = ₹1,379 per seat per month.

The old ₹500 sits inside this range. Our mid attrition value alone is ₹699, and it rests on a named exit cost and a named rate.

## What this model does not claim

- No source shows Sphyr reduces exits. The effect `e` is our estimate, and the pilot scorecard must test it. Until then, public copy must not state a rupee saving as a Sphyr result.
- The 2018 whitepaper results came from a paper-and-pen pilot with four unnamed companies. We use only its card time, as a planning input.
- SPI and Gallup data are mostly from outside India. Aon and AmbitionBox are Indian. AmbitionBox salaries are self-reported.
- Time saved is not cash. The low case counts only half of it.

[^aon26]: Aon, India survey 2025-26
[^aon25]: Aon, India survey 2024-25, via Deccan Chronicle
[^spi]: SPI Research 2025 benchmark
[^praxis]: AmbitionBox, Praxis Global Alliance
[^avalon]: AmbitionBox, Avalon Consulting
[^hirekey]: HireKey fee guide
[^savannahr]: SavannaHR fee guide
[^gallup19]: Gallup 2019
[^gallup24]: Gallup 2024
[^gallup08]: Gallup 2008
[^ceb]: SHRM citing CEB
[^hbr]: HBR 2015, Deloitte
[^wp]: Sphyr whitepaper 2018
