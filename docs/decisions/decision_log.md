---
type: Decision Log
title: "Iteration A decisions"
description: "Decisions the team made for the final-assignment website iteration, newest first, each with its reason and what it changes."
tags: [decisions, iteration-a]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
---

# Iteration A decisions

Append new decisions on top. Do not edit an old decision; add a new one that replaces it and say which.

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
