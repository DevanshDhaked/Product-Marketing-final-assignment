---
type: Research Note
title: "Source inventory"
description: "Every earlier Sphyr coursework file, whether it was graded or a draft, and its date."
tags: [sources, inventory]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
sources:
  - resource: "tasks/saas/"
---

# Source inventory

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Paths like `tasks/saas/...` and `sphyr/...` are relative to the course folder `sem_3/pm/` on the team's machine, outside this repo.

## Graded PDFs (source of truth)

| File | What | Graded? | Date |
|---|---|---|---|
| `saas/submissions/team-03.pdf` | 3 pages: Segment Analysis + Customer Journey (Rohan, founder, 120 people, 20 touchpoints) + Channel Messaging Plan (founder-led, 4 channels) | Graded (Combined 63/100) | 29 Sep 2026 01:42 |
| `saas/segment/team-03-original.pdf` | Byte-identical copy of `submissions/team-03.pdf` (same md5 4763a7ee...) | Same as above | 29 Sep 2026 |
| `saas/Sphyr_Pricing_OnePager.pdf` | Pricing one-pager, Rs 149 flat | Graded (Pricing 70/100; feedback cites this exact path) | 2 Nov 2026 17:30 |
| `saas/packaging/packaging-team03.pdf` | Packaging one-pager (website, demo with "Meera", guided setup, support, AIDA) | Graded (Packaging 69/100) | 9 Nov 2026 23:08 |
| `saas/packaging/packaging-onepager.pdf` | Byte-identical copy of packaging-team03.pdf (md5 5ed6440a...) | Same | 9 Nov 2026 |
| `saas/positioning-statement/positioning-onepager.pdf` | Positioning statement, domain = Consulting firms 40 to 400 | On-disk draft. Submitted text differs per `positioning-statement/log.md` 2026-10-15; submitted version not in repo. No grade in feedback.md | 6 Oct 2026 00:55 |
| `saas/communication-objectives/communication-objectives.pdf` | Classroom exercise answers Q1 to Q13 (Propaganda/Advertising/PR classification) | Likely submitted (no grade in feedback.md) | 26 Oct 2026 11:34 |
| `saas/customer-journey/journey-onepager.pdf` | EARLIER journey draft: "Priya", HRBP, 400-person company, 19 touchpoints | Draft, superseded by team-03.pdf p2 | 24 Sep 2026 22:24 |
| `saas/channel-messaging/channel-messaging-onepager.pdf` | EARLIER channel draft: HR leaders, HR communities, Phase 1/2 incl. review sites | Draft, superseded by team-03.pdf p3 | 24 Sep 2026 22:29 |

Note: feedback.md quotes "Rohan" and "120 employees", which matches `team-03.pdf`, not the Priya journey one-pager. So team-03.pdf is the graded combined submission.

## Markdown / HTML drafts (not graded)

| File | What | Segment it assumes | Date |
|---|---|---|---|
| `saas/index.md`, `saas/log.md` | Bundle index and history. Open flag 2026-09-29: persona/journey/channel/competitor/market not rebuilt for founder segment | n/a | 2026-09-24 to 2026-10-06 |
| `saas/segment/segment-analysis.md` (+ index, log, task) | Reproduces team-03.pdf segment table, ADDS industry (6 product verticals, HR tech strongest), geography (Bengaluru, Hyderabad, Pune, NCR, Chennai), income slab (Rs 31.5 to 675 cr revenue; 100 to 250 band Rs 105 to 337.5 cr). Additions were NOT in the graded PDF | Founder-led, 30 to 500, product IT | 2026-09-29 |
| `saas/persona/persona.md` (+ research-notes, task, log) | "The Bias Referee", HRBP / People Ops champion, core ICP 200 to 1,000, stretch 100 to 200; no personal name in this file | HRBP-led 200 to 1,000 | 2026-09-24 |
| `saas/customer-journey/journey-map.md` (+ html, research-notes, task, log) | Priya, HRBP at 400-person hybrid product/professional-services firm; 6 stages, 19 steps | HRBP-led | 2026-09-24 |
| `saas/channel-messaging/channel-messaging-plan.md` (+ html, research-notes, task, log) | North Star "Whole Sphere + Holds Up"; 5 channels in 2 phases; employee launch message | HRBP-led | 2026-09-24 |
| `saas/positioning-statement/*` (12 md + html/pdf) | Consulting-domain positioning (course assigned Team 3 = consulting). Holds copywriter guideline, social-proof plan, Meera story, professor_lens.md, v3 vision options | Consulting firms 40 to 400 | 2026-10-05 to 2026-10-15 |
| `saas/communication-objectives/answers.md` (+ html, index, log) | Reasoning for the 13-message classification exercise | n/a | 2026-10-26 |
| `saas/packaging/packaging-notes.md` (+ html, index, log) | Decisions, checked facts, Exa research, open risks behind packaging PDF | Founders | 2026-11-09 |
| `saas/teammate-contrib/positioning-answers.md` | 22-question positioning checklist answered for the founder-led product-IT segment; tagline "Promote on evidence from everyone, not one manager's memory." | Founder-led, 30 to 500 (ICP 80 to 250) | undated (after 29 Sep, before 5 Oct) |
| `saas/teammate-contrib/questions-to-ask.md` | The 22-question checklist itself | n/a | undated |
| `saas/market-analysis/*` | Category naming, market size, trends, buyer landscape | HRBP-era (200 to 2,000 then reconciled) | 2026-09-24 |
| `saas/competitor-analysis/*` | Lattice, 15Five, Culture Amp, Leapsome, Betterworks, Reflektive; pricing | HRBP-era | 2026-09-24 |
| `saas/advisor-review/opus-review.md` | 13-finding Opus critique of the HRBP-era bundles | HRBP-era | 2026-09-24 |

No markdown source exists for the pricing one-pager. Grep for 149, 667, 15,000, Westendorp, lakh across all md/html returns nothing; `Sphyr_Pricing_OnePager.pdf` is the only pricing source.
