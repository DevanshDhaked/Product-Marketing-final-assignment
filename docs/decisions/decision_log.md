---
type: Decision Log
title: "Iteration A decisions"
description: "Decisions the team made for the final-assignment website iteration, newest first, each with its reason and what it changes."
tags: [decisions, iteration-a]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
---

# Iteration A decisions

Append new decisions on top. Do not edit an old decision; add a new one that replaces it and say which.

## 2026-11-24: Ad placement chosen

- **Decision:** the one advertisement is a paid sponsor standee (portrait roll-up) with matching A6 handout cards, placed at an HR community event of the kind run by NHRD Network chapters, in the December to January window before the April round. It tracks nobody: no pixel, no badge scan, no form; a QR code opens a plain URL for the 2-minute walkthrough.
- **Naming:** the ad page does not name the specific real event (research found HR Showcase 2026, NHRD Bangalore, 4 to 5 Dec 2026). It describes the placement generically and says "planned", not "booked". No endorsement by any body is implied.
- **Why:** advertising means money is involved ([class notes](../brief/communication_objectives_notes.md)); the event standee was the best verified paid option that reaches heads of talent among peers without tracking. Both newsletters measure clicks per subscriber ([research](../handoffs/admedium_report.md)).
- **Replaces:** the LinkedIn Sponsored Content ad with retargeting on `main` (`site/ad.html`). Its reasoning layout (medium, audience, message, benefit, visual, call to action, journey stage) is kept as a content pattern only.
- **Fix needed:** the channel plan lists SHRM India's 2026 conference (26 to 27 Nov 2026), which falls before the selling window; drop or move that row.

## 2026-11-24: Simple site, new information architecture

- **Decision:** the current site on `main` is a content reference only, not a design or navigation reference. The team finds it confusing and hard to navigate, with too many links.
- **Direction:** simple and clear, yet pleasing and opinionated to look at, not a generalized average website. Use the fewest pages and links that still meet the brief: the website as hub with clear links to the propaganda strategy, the three LinkedIn posts and the ad, plus the 2-minute walkthrough.
- **Replaces:** the phase 2 page split in [the plan](../plan/iteration_a_plan.md) (nine existing pages) until the new page list is approved at gate 1b.

## 2026-11-24: Design direction for phase 1b

- **References:** study Awwwards and similar galleries for comparable products (HR tech, people analytics, feedback tools, editorial B2B SaaS) and borrow named patterns.
- **Logo:** use the ribbon-sphere logo in a playful way (motif, assembly, ribbons as the people around a consultant). It may be recoloured (all white, dark, mono) if the sphere stays recognisable and its ribbon sections stay distinct.
- **Type:** not limited to Google Fonts, not excluding them. The font must be free to self-host on a public site, with its licence recorded.
- **Skills:** use `design-taste-frontend` and `stageshow`. The prototype's UI language stays inside faux UI frames. Light and dark themes with the toggle stay.
- **Replaces:** the phase 1a choice of Manrope as the only font is open again.

## 2026-11-24: Gate 1a results

- **Central message and positioning approved:** "The engagement ends. The evidence stays." with the vision and product lines in [positioning](../strategy/positioning.md). Condition: all copy must read as written by people. Run every piece of public copy through the `humanizer:humanizer` skill before it ships.
- **Persona use approved:** the brief grades persona use, not a persona deliverable (brief lines 66, 129, 170, 330, 351). Kavya, Vikram and Meera stay an internal base that shapes copy, channel and call to action. They are named only in the propaganda strategy's audience section, not on a site page.
- **Three LinkedIn posts approved** as mapped in [the deliverable map](../strategy/deliverable_map.md).
- **Ad medium reopened:** the professor's class notes ([communication objectives](../brief/communication_objectives_notes.md)) define advertising as the push route where "money is involved". A free event poster would be word of mouth or PR, not an advertisement. The ad should be a small, paid, non-invasive placement. The exact placement is open until specific events or slots are verified with dates and prices.

## 2026-11-24: Segment definition confirmed, persona, ad medium, plan approved

- **Segment:** the consulting definition below is confirmed by the team. It replaces the "proposed" status.
- **Primary persona:** the head of talent (champion), who finds Sphyr, runs the pilot and takes the case to the managing partner. The managing partner is the secondary buyer persona. Meera, a senior consultant, is the person being rated.
- **Ad medium:** the brief asks for "one advertisement designed for an appropriate medium and audience", not a LinkedIn ad. Only the three LinkedIn posts must be on LinkedIn. The strategy work proposes the ad medium with its reasoning, and the team approves it at gate 1a.
- **Plan:** [the iteration A plan](../plan/iteration_a_plan.md) is approved. Phase 1a starts.

## 2026-11-24: Segment is consulting (exact definition proposed, awaiting confirmation)

- **Status:** the team chose consulting. The exact definition below is a proposal until the team confirms it.
- **Decision:** the canonical segment is homegrown, partner-led Indian management and strategy consulting firms of about 40 to 400 professionals. The managing partner is the buyer, the head of talent is the champion, and Meera, a senior consultant, is the person being rated. IT and tech consulting are out.
- **Why:** the course assigned Team 3 the consulting domain (`tasks/saas/positioning-statement/task.md`, 5 Oct). The professor's feedback asks for a personal journey and a message a junior copywriter can use, and a narrow, concrete segment serves both. The definition comes from `tasks/saas/positioning-statement/positioning-onepager.pdf`.
- **Replaces:** the live site's segment (founders of 50 to 300 person IT services firms, Meera as Head of People) and the graded 29 Sep segment (founder-led product IT, 30 to 500, Rohan).
- **Changes:** the website copy, persona, journey, propaganda strategy, all three LinkedIn posts, the ad and the pricing inputs.

## 2026-11-24: Pricing follows the feedback and the math

- **Decision:** keep a flat per-employee model. Re-derive every number for consulting: the value per employee, the competitor comparison on named plans, the margin floor, fixed costs, contribution, break-even, the pilot amount, its length and what happens if the firm does not convert, and how Van Westendorp results set the final price. If the math no longer supports ₹149 or the ₹15,000 six-week pilot, the number changes.
- **Why:** pricing scored 70/100 because the key numbers had no supporting logic ([feedback](../brief/professor_feedback.md)).
- **Gate:** the re-derived numbers are shown to the team before any site change.

## 2026-11-24: Visual direction is light and dark with a toggle

- **Decision:** the site supports a light and a dark theme with a visible toggle. It should stop reading as AI-made. Grading is on message and reasoning; looks only make an impression (brief line 12).

## 2026-11-24: Source PDFs stay out of the repo

- **Decision:** `docs/` holds markdown digests that quote and cite sources. It does not copy the professor's whitepaper, the product documentation or the graded PDFs. The repo is public.

## 2026-11-24: Working branch and deploy

- **Decision:** all iteration work happens on the `iteration-a` branch. Commits are made per logical group. A person on the team pushes and redeploys `gh-pages`; agents do not push.
