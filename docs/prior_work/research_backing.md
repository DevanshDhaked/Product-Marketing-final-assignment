---
type: Research Note
title: "Research that can back the numbers"
description: "Market size, competitor plans and prices, attrition and review-time figures, and packaging research already gathered, with their sources."
tags: [research, pricing, competitors]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
sources:
  - resource: "tasks/saas/market-analysis/"
  - resource: "tasks/saas/competitor-analysis/"
  - resource: "tasks/saas/packaging/packaging-notes.md"
---

# Research that can back the numbers

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Paths like `tasks/saas/...` and `sphyr/...` are relative to the course folder `sem_3/pm/` on the team's machine, outside this repo. URLs were not re-checked on 2026-11-24.

All items below are as recorded in the repo files; I did not re-verify the URLs this session. Confidence tags are the files' own.

## 5.1 Market size
- Global Employee Performance Management market: USD 3.52 B (2025) to USD 6.33 B (2030), 12.4% CAGR, MarketsandMarkets, Dec 2025, tagged "Use with care" (free teaser page). https://www.marketsandmarkets.com/Market-Reports/employee-performance-management-market-82686564.html. File: `market-analysis/market-analysis.md` §2. Narrower "360-degree feedback software" niche USD 2.6 to 2.7 B by 2032/33 tagged "Directional only".
- Performance Management Systems: USD 3.73 B (2025) to USD 6.40 B (2030), 11.5% CAGR. https://www.researchandmarkets.com/report/performance-management. File: `teammate-contrib/positioning-answers.md` sources.
- Indian SaaS to reach USD 35 B by 2027 (Bain and NASSCOM via Business Standard): https://www.business-standard.com/article/companies/indian-saas-companies-to-reach-35-bn-by-2027-bain-company-report-123012401483_1.html. India software products sector USD 13.3 B FY2022E (NASSCOM, dated, "floor"): https://nasscom.in/knowledge-center/publications/indias-software-product-ecosystem-accelerating-growth. File: `segment/segment-analysis.md`. No company count by employee band found ("not independently verified").
- Revenue per employee benchmarks (for income slab): SaaS Capital 2026 median $141,125, early stage $109,644 https://www.saas-capital.com/blog-posts/revenue-per-employee-benchmarks-for-private-saas-companies/ ; Aleph 2026 $193,000 ARR/employee https://www.getaleph.com/answers/arr-per-employee-saas-2026. File: `segment/segment-analysis.md`.
- SaaSBoomi exists and is active (founder community for channel 2): https://saasboomi.org/. File: `segment/segment-analysis.md`.

## 5.2 Competitor plans and prices
| Vendor | Plan / price | Source as recorded | File |
|---|---|---|---|
| Lattice | Talent Management core $11/user/month; add-ons Engagement $4, Grow $4, Compensation $6, Core AI $6; $4,000/year minimum; annual billing; implementation up to 8 weeks (third-party, Lattice requires demo to see price) | https://peoplemanagingpeople.com/tools/lattice-pricing/ ; also https://lattice.com/pricing , https://www.procr.io/post/lattice-pricing-2026 | `competitor-analysis/research-notes.md` (2026-09-24, confidence medium); `teammate-contrib/positioning-answers.md` |
| 15Five | Engage $4, Perform $11 (reviews, 1-on-1s, check-ins, OKRs), Total Platform $16 per user/month, annual, public on own site FAQ | 15five.com scraped 2026-09-24; also https://www.compono.com/articles/15five-pricing-true-costs-2026 | `competitor-analysis/research-notes.md` (confidence high) |
| Culture Amp | No public price; enterprise line at 1,000+ employees; teammate file cites $5 to 9 | https://www.compono.com/articles/culture-amp-pricing-guide-2026 | `competitor-brief.md`, `teammate-contrib` |
| Leapsome | "publishes no pricing anywhere, sales-led" | leapsome.com (2026-09-24) | `competitor-analysis/competitor-brief.md:71-78` |
| Betterworks | Custom quote; aggregator "from $8/user/month" | https://peoplemanagingpeople.com/tools/lattice-pricing/ (same page) | `competitor-analysis/research-notes.md` |
| Peoplebox | $7 to $15/month (G2); teammate file says $8 | https://www.g2.com/products/peoplebox-ai/pricing ; https://softwarefinder.com/hr/peoplebox-ai | `positioning-statement/alternatives_and_competitors.md`, `teammate-contrib` |
| Confirm | $8/person/month, ONA "hidden talent" | https://www.confirm.com/pricing , https://www.confirm.com/ona | `teammate-contrib` |
| Keka | Growth plan includes continuous feedback, 360 reviews, 9-box, promotions; PSA timesheets | https://www.keka.com/pricing (modified 2026-10-01); https://hrone.cloud/blog/keka-pricing-india/ | `alternatives_and_competitors.md`, `teammate-contrib` |
| Keka / Darwinbox appraisal modules | "₹50–150 per employee per month inside the HRMS" | https://hrone.cloud/blog/keka-pricing-india/ ; https://hrone.cloud/blog/darwinbox-review-india/ | `teammate-contrib/positioning-answers.md` §6 |
| Reflektive | Shut down; raised $81M, $300M peak valuation; acquired by LTG/PeopleFluent; closest analog, bundling risk | https://unicornburn.com/autopsy/reflektive ; https://ltgplc.com/news/expands-performance-management-offering-acquisition-of-reflektive/ | `competitor-analysis/research-notes.md` |

## 5.3 Numbers that can back the value calc and pain
- Replacement cost 0.5 to 2x annual salary (Gallup): https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses-trillion.aspx. Teammate applied it to ₹25 L CTC = ₹12 to 50 L per regretted exit (`teammate-contrib/positioning-answers.md` §5).
- Rater effect: 53 to 62% of rating variance reflects the rater, actual performance 21 to 25% (Scullen, Mount & Goff, 2000, J. Applied Psychology 85(6)). https://www.researchgate.net/publication/12202559_Understanding_the_Latent_Structure_of_Job_Performance_Ratings
- Gallup: 29% strongly agree reviews are fair; 14% say reviews inspire improvement. https://www.gallup.com/workplace/249332/harm-good-truth-performance-reviews.aspx
- India: 36% call appraisal process effective; 52% job-hunting during appraisal season (foundit 2026). https://aninews.in/news/business/appraisal-season-half-of-indias-professionals-are-already-job-hunting-foundit-appraisal-survey-finds20260724110024/
- Remote workers 24% less likely to be promoted; 60% of managers say reduced visibility makes reviews harder. https://www.legaldive.com/news/remote-workers-face-bias-for-raises-promotions-american-staffing-association/641114/
- 71% of companies run annual reviews; 58% track performance on spreadsheets ("Use with care", aggregator). https://www.selectsoftwarereviews.com/blog/performance-management-statistics (`persona/research-notes.md`)
- Sphyr 2018 pilot (whitepaper, first-party, small sample, no control): card time 2 min 09 s per fortnight (sphere about 14); fairness acceptance up 57% to about 94%; appeals down 92% (discussion 25 to 3.5 min); HR collation effort down 76%; ease test 3.4 min vs 45 to 56 min for existing forms; cost per employee US$63 vs US$85; manager time 1,000 min for 20 reports vs 0; appeals 40% vs 3.2%. Do not use the "0% collusion" and "88%" figures. File: `positioning-statement/product_evidence.md`; source `documents-shared-class/Sphyr Overview Whitepaper v0.3.pdf`.
- Peer-rank wisdom-of-crowds appraisal validated at a 1,000+ employee company over three years: Dokuka et al. (2019) arXiv:1912.12861 https://arxiv.org/abs/1912.12861 (`persona/persona.md`).
- Deloitte redesign around per-project snapshots: https://hbr.org/2015/04/reinventing-performance-management

## 5.4 Packaging, demo and proof research (`packaging/packaging-notes.md`, Exa, 2026-11-09, vendor self-reported)
- Interactive demos convert 12% better than product videos: https://www.navattic.com/report/state-of-the-interactive-product-demo-2026
- Form conversion 1.1% to 1.8% with interactive demo, 24 B2B SaaS companies: https://www.hockeystack.com/lab-blog-posts/do-interactive-demos-work
- 73% of top interactive demos ungated: https://www.navattic.com/report/state-of-the-interactive-product-demo-2024
- 8 in 10 B2B decision-makers look for a new vendor if performance guarantees are not offered (McKinsey 2025): https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-net-revenue-retention-advantage-driving-success-in-b2b-tech
- Signeasy: 0.04% used its 100-day refund: https://signeasy.com/blog/company/100-day-money-back-guarantee
- Mid-market go-live typically 2 to 4 weeks (HubSpot 2026): https://blog.hubspot.com/service/b2b-customer-onboarding-best-practices
- HR SaaS case: guided path to first task beat more tutorials: https://www.christophercorte.it/en/projects/onboarding-saas-hr/
- Peer influence (adjacent, "Use with care"): 54% of buyers talked to existing users before purchase (TrustRadius 2025 via reechee); 65% of CMOs start vendor search in peer communities (Wynter 2026, n=101). https://reechee.io/blog/state-of-b2b-software-buying/ (`customer-journey/research-notes.md`)

## 5.5 Professor context (`positioning-statement/professor_lens.md`)
- Grader is Ravi Warrier, who wrote the Sphyr whitepaper (2018) and hosts the prototype (sphyr-prototype.raviwarrier.com). His vision words: "decentralizing performance reviews", "truly democratic", career progression as "an apolitical recognition of value" not "a political favor", promote "quiet, reliable executioners" over "loud bullshitters"; employees gain "a voice in the assessment of peers", "insights into their blind spots", "an opportunity to improve their bonds with their fellow team members"; core belief "employee delight is at the heart of any organization's long-term success."
- Earlier professor critiques recorded in `positioning-statement/task.md` (the 63/100 combined feedback, carried forward) and `positioning-statement/log.md` (positioning "too focused on the present").

Status: COMPLETE (all 5 sections written).
