---
type: Plan
title: "First card reward: what the first card gives the rater and the person rated"
description: "What happens on and right after the first Sphyr card for the person filling it and the person rated, how it shows their contribution matters, what they discover, and the reason to return each fortnight, with product facts and timing gaps marked."
tags: [packaging, first-use, reward, retention]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T17:40:07Z }
status: draft
sources:
  - id: proto
    resource: ../product/prototype_screens.md
    title: "Prototype screen inventory, sections 3.1, 3.3, 3.7 (captured 2026-11-24)"
  - id: facts
    resource: ../product/product_facts.md
    title: "Product facts, sections 1.4, 1.6, 1.9, 1.10"
  - id: dnc
    resource: ../product/do_not_claim.md
    title: "Do-not-claim list, method notes (notification copy from the bundle)"
  - id: wp
    resource: "sphyr/Sphyr Overview Whitepaper v0.3.pdf"
    title: "Sphyr Overview Whitepaper v0.3, December 2018, p1 to p3"
  - id: mck
    resource: https://www.mckinsey.com/capabilities/people-and-organization/our-insights/the-organization-blog/survey-fatigue-blame-the-leader-not-the-question
    title: "McKinsey Organization Blog, Survey fatigue? Blame the leader, not the question, 10 May 2021 (accessed 2026-11-24 via exa; direct fetch returned 403)"
---

# First card reward: what the first card gives the rater and the person rated

> The professor's question: completing a five-click card may be simple, but what does the user get out of that first interaction? This file answers it for the two people every card touches: the one filling it and the one it is about. In the first cycle every consultant is both.

Out of scope here: price, renewal and anything about buying.

## The core idea: the first card is half of an exchange

In Sphyr, ratings are reciprocal. The people in your circle rate you as you rate them (whitepaper p1).[^wp] So the first card is not a form that goes into a drawer. It is the first half of an exchange that completes in the same fortnight. That is why the cycle-1 reward does not have to be a chart. The chart comes later. In cycle 1 the reward is that the people who saw your work are saying something back, and you can read it.

## Why closing the loop matters

A McKinsey review of more than 20 academic articles found that the main driver of survey fatigue was employees believing the organization would not act on the results, not the number or length of surveys. When organizations shared and acted on results, employees were more likely to take part in later surveys.[^mck] Sphyr is not a survey, so this is an analogy. The design rule it gives us: every person must see, within the first cycle, that what they gave went somewhere.

## The rater: on the card

All of this is in the prototype's "Provide Feedback" screen.[^proto]

| What they see | What it does for them | Effect |
|---|---|---|
| The person's name, role and how they know them ("UX Researcher · Peers") | The card is about a colleague, not a form field | Contribution matters |
| "How was your experience with [name] this fortnight?" with three answers, including "No interaction" | An honest answer is always available; nobody has to invent a rating | Contribution matters |
| Tags in the firm's own words, set by the admin ("Sphyr UI / UX VBAs" in the demo) | The words they tap are the firm's values, so the choice means something here | Contribution matters |
| "Let [name] know what's on your mind?" with "Your comments and review are always anonymized." | The note is addressed to the person, by name. It reaches them, not a file | Contribution matters |
| "Private by design: Individual responses are normalized and grouped before anyone sees them." | They can be honest | (Reassurance, kept in the side rail where the product puts it) |

## The rater: right after the card

| What they see | What it does for them | Effect |
|---|---|---|
| The counter moves ("4 of 17") and the progress bar fills | Visible progress; the deck is short and finite | Contribution matters |
| "THIS CYCLE: 3 Completed, 14 Remaining" | They know exactly what is left | Reason to return (within the cycle) |
| The card appears under "Completed Feedback This Fortnight" as "Submitted · Read only" | What they gave is recorded and stays as given | Contribution matters |
| The streak pill (demo: "4-cycle streak · 8 weeks") | From cycle 2, a small reason not to break the run. It is the only game-like element in the product; we add none | Reason to return |

What happens to the card afterwards: the person rated receives the tags in pooled form and the note without the rater's name. Managers see team participation, and through the edit approval queue they can see who gave feedback to whom.[^proto] So copy says "anonymized to the person you rated", never "anonymous to everyone".

## The person rated: during and after the first cycle

| When | What they see | Effect | Evidence |
|---|---|---|---|
| During cycle 1 | A notification that new anonymized feedback has arrived ("Feedback received: You received 4 new items of Anonymized ...") | Discovery: people are saying something about their work, now | Product, but from bundle text only; not seen rendered[^dnc] |
| After cycle 1 closes | Their Insights page starts with what came in: the most frequent tags ("Top feedback received"), anonymized notes in a feed, and progress on their own cards | Discovery: what landed, in their colleagues' words | Screen is Product.[^proto] **When it first shows anything, and with how many raters, is our assumption.** No source states a threshold |
| After a few cycles | "Overall trajectory", the seven dimensions with cycle change, "Areas to improve" with "Repeated across N cycles", matched peer comparison | Discovery: patterns, not single remarks | Product.[^proto] The demo page is built "from your last six feedback cycles" |

What the first cycle can honestly give a consultant: tags and short notes from people in her circle, in their words. What it cannot give yet: a trend, a meaningful peer comparison, or "areas repeated across cycles". Copy for the first weeks promises the voice, not the chart.

## What a person discovers in cycle 1 (examples on demo data)

These are the kinds of lines the demo shows, used only to show what "discovery" means. They are prototype demo data, not real feedback.

- A strength they did not know others noticed: a "Was helpful" or "Took initiative" tag from three people on two different teams.
- A note that names a specific moment: "Your handoff was clear and thoughtful. An earlier signal on the research dependency would have helped us plan around it."[^proto]
- A friction they can still fix this engagement: "Resolve dependencies sooner" tapped by people on the current team.

## The reason to return each fortnight

| Reason | For whom | Product fact |
|---|---|---|
| The next deck opens on a known date, and their circle is filling cards for them again | Everyone | Fortnightly cycle and schedule[^proto] |
| Each cycle adds to their own record; after a few, the line appears | Consultants | Insights: "Overall trajectory", "Fortnightly trend"[^proto] |
| Engagements change, so the circle changes: they add the new team | Consultants | My Sphyr: "You can update it at any time."[^proto] |
| How their current team is landing, while the engagement still runs | Engagement managers | Team Insights[^proto] |
| April: the partners read the whole year | Consultants, partners | Member Insights across cycles[^proto] |
| Not breaking the streak | Everyone, from cycle 2 | The streak pill, nothing more |

The fortnightly moments after cycle 1 are listed in [acquisition and engagement](../strategy/acquisition_engagement.md).

## Design choices and what we rejected

- **No first-cycle score shown as a headline.** A score from a few ratings in two weeks would mislead and would make the first thing a consultant sees a number about her. The first thing she sees should be words from people she worked with.
- **No added badges, points or leaderboards.** The product has a streak pill and counters only ([do-not-claim](../product/do_not_claim.md), item 15). Adding more would read as a game about rating colleagues.
- **No team-written "first-cycle readout" of individuals.** Our team does not read the firm's ratings. The first readout is a session where engagement managers open their own Team Insights ([first-use experience](first_use_experience.md)).

[^wp]: Sphyr Overview Whitepaper v0.3
[^mck]: McKinsey Organization Blog, 2021
[^proto]: Prototype screen inventory
[^dnc]: Do-not-claim list, method notes
