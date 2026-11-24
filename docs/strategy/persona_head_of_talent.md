---
type: Persona
title: "Persona: Kavya, head of talent (champion)"
description: "The primary persona: Kavya, head of talent at a 150-person homegrown consulting firm, who finds Sphyr, runs the pilot and takes the case to the managing partner; her week, goals, fears, words and stakes."
tags: [strategy, persona, champion, consulting]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:55:19Z }
status: draft
sources:
  - id: segment
    resource: segment.md
    title: "Segment note (this folder)"
  - id: pain
    resource: "tasks/saas/positioning-statement/consulting_pain.md"
    title: "Team research note on consulting pain, 2026-10-05"
  - id: proto
    resource: https://sphyr-prototype.raviwarrier.com/
    title: "Sphyr prototype, screens recorded in docs/product/prototype_screens.md (captured 2026-11-24)"
  - id: foundit
    resource: https://www.ptinews.com/press-release/appraisal-season-half-of-india-s-professionals-are-already-job-hunting-foundit-appraisal-survey-finds/3893922
    title: "foundit Appraisal Survey press release, 2026-07-24 (accessed 2026-11-24)"
---

# Persona: Kavya, head of talent

> **Read this first.** Kavya, the firm, Meera and every quote in this file are an illustrative composite built from research on the segment. They are not real people or interviews. Never present any of it as a testimonial, a customer or a review. No head of talent has been interviewed yet, so her words are a hypothesis to test.

## Who she is

Kavya is 38. She is head of talent at a homegrown management consulting firm of about 150 professionals, headquartered in Gurugram, with offices in Mumbai and Bengaluru. The firm has four practices and eleven partners. She has been there three years. She was hired as its first head of talent after the managing partner lost two engagement managers in one quarter.

Before this she spent six years in HR at a Big 4 firm. She knows what a large firm's review machinery looks like, and she knows her firm will never have it. Her team is two people: an HR executive and a recruiter. She reports to the managing partner.

She runs campus and lateral hiring, onboarding, the project-end feedback forms, the April appraisal and promotion round, and exit interviews. The last two are the ones she thinks about at night.

## Her week in late November

**Monday.** She opens the tracker of project-end forms. Thirty-one engagements closed since April. Nineteen forms are in. Most say "good work, strong team player". Four engagement managers have not replied to three reminders. One has left the firm, so his three forms will never come.

**Tuesday.** A partner asks her for "the file" on two senior consultants he will rate in April. He led neither of their big engagements this year. She sends what she has: two short forms and a note from a client email someone forwarded in August.

**Wednesday.** She re-reads last June's exit interview with Siddharth, a senior consultant who left for a Big 4 firm. He told her: *"Nobody who saw my pricing work was in the calibration room. The partner who rated me saw three weeks of me."* She agreed with him. She could not say so.

**Thursday.** She looks at Meera, a senior consultant in Bengaluru. Meera has had four engagements this year, three different engagement managers and one client CFO who praised her model to the partner. Kavya can see Siddharth's year happening again.

**Friday.** The managing partner asks her to "make April less painful this time". She has heard this every year.

## What she wants

- **One honest record per consultant at calibration**, built from the people who worked with them across the year, not the last engagement.
- **To stop chasing.** Less time spent hunting forms from busy engagement managers.
- **To keep people like Meera.** Fewer exits that say "partiality" or "nobody saw my work".
- **To be the person who fixed April.** Her standing with the partners depends on promotion rounds that feel fair and finish on time.
- **Something consultants do not hate.** Anything that feels like a long form or like being watched will be ignored in a 60-hour client week.

## What she fears

- **Buying another tool nobody uses.** If participation drops in the busy weeks, she owns the failure.
- **Partners saying she is taking away their judgement.** Partners decide promotions. A tool that looks like it decides for them will be killed in the first partners' meeting.
- **Consultants feeling surveilled.** If the first message reads as "HR is tracking you", trust is gone and so is she.
- **Clients being bothered.** The client relationship belongs to the partner. One annoyed client and the whole idea is dead.
- **Being wrong in front of the managing partner.** She gets one ask a year for a new budget line. If she spends it on something that does not show results by April, she will not get another.

## In her own words (composite, not quotes)

- *"By April, the people who saw someone's best work are on three other engagements, or gone."*
- *"I don't need more data. I need the right people's view, before they forget."*
- *"Every year a partner rates someone he barely worked with, and every year I'm the one who explains it in the exit interview."*
- *"If it takes more than two minutes on a Friday evening, my consultants won't do it."*
- *"I can't take this to the partners as 'HR wants a tool'. It has to be about their calibration."*
- *"Show me someone like us who tried it. Not a logo. Someone I can call."*

Context that supports her view: in a July 2026 foundit survey of Indian professionals, 52% of respondents said they were actively looking for a job during appraisal season, and among people who felt well represented in their appraisal, 37% said their manager actively advocated for them.[^foundit] The release does not state the sample size, and it covers all sectors, not consulting.

## How she wins internally

Kavya cannot buy Sphyr herself. The managing partner signs. Her path:

1. **Make it a partner problem, not an HR problem.** The pitch is "calibration on the whole year, not the last engagement", in partner words. See [the managing partner persona](persona_managing_partner.md).
2. **Ask for a small, time-boxed paid pilot**, not a firm-wide rollout. One or two practices, before the April round. The amount and length come from the pricing work.
3. **Bring proof a partner accepts:** the method in plain language, a 2-minute walkthrough he can click himself, the honest 2018 pilot, and a peer reference from another firm once one exists.
4. **Pre-empt the vetoes.** For partners: Sphyr feeds calibration, it does not rate anyone for them. For consultants: two minutes every two weeks, comments are anonymized to the person rated. For clients: only when the partner opts the client in.
5. **Agree the success test before starting.** For example: participation by the fourth cycle, and how many senior consultants have feedback from three or more engagements by calibration. Then report it honestly, even if it is bad.

## What she gets from Sphyr (only what the product does)

- **A personal sphere for each consultant.** Each person keeps a circle of the people they work with: peers, seniors, juniors and external people such as client counterparts, invited by email (prototype "My Sphyr"; product guide p5).[^proto] The record follows the person, not the engagement.
- **A fortnightly rhythm on by default.** Admin sets one organization-wide frequency; fortnightly is the default (prototype "Feedback Frequency").[^proto]
- **Two-minute cards.** Each card asks how the past two weeks went (was good, could improve, no interaction), then a few tags, then an optional note.
- **What partners and engagement managers see.** Manager views show member trends across cycles, the seven core parameters, recurring constructive signals and anonymized comments, plus team participation (prototype "Member Insights" and "Team Insights").[^proto]
- **What the consultant sees.** Her own trend over cycles, her strongest signals, areas to improve and anonymized comments (prototype "Insights").[^proto]
- **Her own admin.** Member import by file, the firm's own values list, the cycle rhythm.

Not available, so never promise it to Kavya: an org-wide talent dashboard for HR, a "who should we promote" screen, integrations with an HR system, reminders by Slack or Teams, or anything described as AI. Ratings are pooled and comments are anonymized to the person rated; managers can see who asked to edit feedback given to whom, so never say "anonymous to everyone".

## Her stakes at each stage

Detail per stage is in [the journey map](journey_map.md).

| Stage | What is at stake for Kavya |
|---|---|
| Trigger | Another April like the last one, and another Siddharth |
| Naming the problem | Whether she can describe it in partner words, not HR words |
| Looking for answers | Her time; she will not sit through suite demos built for 2,000-person companies |
| Seeking validation | Her credibility: backing a product with no reviews |
| Making the case | Her one budget ask of the year |
| Paid pilot | Participation in client-heavy weeks; her name is on it |
| First calibration on Sphyr | Whether partners see something they did not already know |
| Renewal | Whether she is the person who fixed April |

## What she must never hear from us

- "Track your consultants" or anything that sounds like monitoring.
- "Replaces partner judgement" or "the system decides".
- "Anonymous" without qualification, "unbiased", "eliminates politics".
- HR software jargon: "VBA", "sphere score", "ONA", "talent suite".
- Pressure tactics, countdown offers, or follow-ups she did not ask for.

[^foundit]: foundit Appraisal Survey, 2026-07-24
[^proto]: Sphyr prototype
