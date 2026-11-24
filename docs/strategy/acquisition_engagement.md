---
type: Plan
title: "Acquisition and engagement"
description: "How consulting firms are reached, the single next step at each point (the 2-minute walkthrough, then a 20-minute call, then a paid pilot), the public pilot scorecard that replaces reviews, and how the relationship stays useful after the first touch and after purchase using only real product moments."
tags: [strategy, acquisition, engagement, retention]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:55:19Z }
status: draft
sources:
  - id: proto
    resource: https://sphyr-prototype.raviwarrier.com/
    title: "Sphyr prototype, screens in docs/product/prototype_screens.md (captured 2026-11-24)"
  - id: doc
    resource: "sphyr/Sphyr.io Product Documentation.pdf"
    title: "Product Guide: Sphyr"
  - id: wp
    resource: "sphyr/Sphyr Overview Whitepaper v0.3.pdf"
    title: "Sphyr Overview Whitepaper v0.3, December 2018, p6 to p7"
  - id: conflicts
    resource: ../prior_work/source_conflicts.md
    title: "Source conflicts, row 11 (pilot length)"
---

# Acquisition and engagement

Scope: how a firm is reached and decides, and how the relationship stays useful afterwards. What happens between buying and the first card (setup, invitations, the first-use experience) is in the first-use plan in `docs/packaging/` and is not repeated here. Pilot price and length come from the pricing work in `docs/pricing/`.

## How firms are reached

Three entry paths, all from the [channel plan](channel_plan.md):

1. **An introduction.** Someone Kavya or Vikram knows sends one personal note with the walkthrough link.
2. **A post she recognises.** A LinkedIn post or article in consulting words, reshared by someone in her network.
3. **A room she is in.** A community session or event where Sphyr's team speaks or attends.

All three lead to the same place: our site and the 2-minute walkthrough.

## One next step at a time

Each touch asks for one step only, the smallest that moves her forward.

| Where she is | The one step we ask for | What she gets | What we never ask for here |
|---|---|---|---|
| She has just heard of Sphyr | **Take the 2-minute walkthrough** on our site | She sees the card, the circle and the record without talking to anyone | Her email, her firm's name, a meeting |
| She has seen the walkthrough | **Book a 20-minute call** | A conversation about her firm's April round, including what Sphyr does not do | A demo of features she did not ask about |
| She is convinced and needs the partners | **Share the partner page** with Vikram | A short page in partner words, and an offer to join the call | A "decision timeline" |
| The partners agree | **Start a paid pilot** with one or two practices | A pilot with a success test agreed in writing before it starts | A firm-wide contract |
| The pilot is done | **Review the scorecard together**, then decide | An honest report, good or bad | Pressure to renew before the report |

Kavya can stop at any step. If she does, she keeps what she already got and hears from us only if she asked to.

## The pilot scorecard (proof without reviews)

Sphyr has no customers and no reviews. The pilot scorecard is how proof gets built in public.

- **Before the pilot starts**, we publish on our site what every pilot measures and how. The firm agrees the targets.
- **What is measured** (to be confirmed with the pricing and first-use work):
  1. Participation per cycle (the prototype's manager view shows it, for example "Participation 96%, 24 of 25 reviews given").[^proto]
  2. Average number of different people giving feedback to each consultant (the member view shows "From 12 collaborators").[^proto]
  3. Share of senior consultants with feedback from people on three or more engagements by calibration. If the product does not show this directly, the firm counts it from team rosters.
  4. A two-question partner survey after calibration: "Did the record show you something you did not know?" and "Did it change any discussion?"
  5. A two-question consultant survey: "Did you see something useful in your own record?" and "Would you keep doing it?"
- **After the pilot**, results are published only with the firm's consent, unnamed unless the firm agrees. Bad results are published the same way as good ones, or not at all.

Pilot terms, decided at gate 1b ([price and pilot](../pricing/price_and_pilot.md)): 12 weeks, six fortnightly cycles, up to 40 people, ₹25,000 plus GST, credited against the first annual bill if the firm signs. If it does not sign, the firm gets its data as a CSV file and the rest is deleted; there is no refund. This settles [source conflicts, row 11](../prior_work/source_conflicts.md): the graded six weeks gave only three cycles. The scorecard is measured over the six cycles.

## After the first touch (before any purchase)

The relationship stays useful without chasing:

- **She asked for nothing:** we send nothing. The site stays open.
- **She took the walkthrough and signed up for the monthly note:** one email or LinkedIn note a month about calibration and rotation in consulting firms, with one link. One-click unsubscribe.
- **She had the 20-minute call:** one follow-up with what we discussed and the partner page. After that, only what she asks for.
- **She said "not now":** we ask if she wants a note in October before the next round, and do only that.

## After purchase: real product moments

Only product moments that exist in the product guide or the prototype are used.

| When | Product moment | Why it keeps the relationship useful |
|---|---|---|
| Every fortnight | The cycle opens; each person sees a short deck of cards for the people in their circle (prototype "FEEDBACK THIS FORTNIGHT")[^proto] | Two minutes, then done. The rhythm is the habit |
| During each cycle | Notification copy such as "Feedback reminder: 3 reviews remaining for this fortnight cycle" (prototype bundle text)[^proto] | A light nudge from the product, not from HR |
| After a few cycles | Each consultant's own "Insights": trend over cycles, strongest signal, areas to improve, anonymized comments, "Current cycle progress"[^proto] | The consultant's reason to return: they see their own record grow |
| Any time | "My Sphyr": a consultant adds people they now work with, including client counterparts invited by email when the partner agrees (product guide p5)[^doc] | The circle follows the person as engagements change |
| Each cycle, for managers | "Team Insights": team score, participation, rating distribution, anonymized team feedback, feedback edit approvals[^proto] | Engagement managers see how their team is landing while the engagement still runs |
| Before calibration | "Member Insights": each member's trend and assessment across cycles[^proto] | Partners come to calibration with the whole year |
| After calibration | Review of the pilot scorecard with Kavya and Vikram | Renewal is decided on the firm's own results |

What our team provides alongside the product: the whitepaper describes the license as including "business support, training and training materials, set up and configuration support and flexible billing".[^wp] We use that for one short guide for partners on reading a record before calibration.

Never promise: an org-wide HR dashboard, a promotion recommendation screen, integrations, Slack or Teams reminders, coaching, a reflection journal, pulse surveys, or AI features. These are roadmap items or are not in the prototype.

## What makes a firm stay (and what does not)

- **Stays:** consultants keep filling cards because they see their own record; partners use the record in calibration; Kavya spends less time chasing forms.
- **Does not make a firm stay:** discounts, lock-in, renewal pressure, or feature promises. We do not use them.

[^proto]: Sphyr prototype
[^doc]: Product Guide: Sphyr
[^wp]: Sphyr Overview Whitepaper v0.3
