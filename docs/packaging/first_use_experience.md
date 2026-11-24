---
type: Journey Map
title: "First-use experience: from first encounter to first readout"
description: "The receiving journey for the head of talent, partners and engagement managers, and consultants, from first encounter to each one's first readout, with the intended effect of every element and the product fact or team service behind it."
tags: [packaging, first-use, onboarding, consulting]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T17:40:07Z }
status: draft
sources:
  - id: proto
    resource: ../product/prototype_screens.md
    title: "Prototype screen inventory, sections 3.1 to 3.13 (captured 2026-11-24)"
  - id: facts
    resource: ../product/product_facts.md
    title: "Product facts, sections 1.4 to 1.11"
  - id: dnc
    resource: ../product/do_not_claim.md
    title: "Do-not-claim list"
  - id: wp
    resource: "sphyr/Sphyr Overview Whitepaper v0.3.pdf"
    title: "Sphyr Overview Whitepaper v0.3, December 2018, p1 to p7"
  - id: journey
    resource: ../strategy/journey_map.md
    title: "Journey map, Stage 6 onward (this journey ends where Stage 6 starts)"
---

# First-use experience: from first encounter to first readout

> Kavya, Vikram and Meera are illustrative composites from [the head of talent persona](../strategy/persona_head_of_talent.md). They are not customers.

## Scope

This file covers only what happens between a person first encountering Sphyr and actually using it. It ends at each audience's first readout. What happens every fortnight after that is in [acquisition and engagement](../strategy/acquisition_engagement.md), and the pilot from cycle 2 onward is Stage 6 of [the journey map](../strategy/journey_map.md).

Out of scope: price, the order, refunds, renewal, acquisition cost and any persuasion to buy.

Time is counted in cycles because the pilot length is still open ([source conflicts, row 11](../prior_work/source_conflicts.md)). Cycle 0 is setup, before the first cards. Cycles are fortnightly, the default in the product.[^proto]

## How to read the tables

Each element has one intended effect. Effects are the four the professor asked about:

- **Anticipation**: the person looks forward to something specific, and knows when it arrives.
- **Contribution matters**: the person sees that what they gave went somewhere and counted.
- **Discovery**: the person learns something useful they did not know.
- **Reason to return**: the person has a concrete reason to open Sphyr next cycle.

The last column says whether the element is a **Product** fact (it exists in the prototype or product guide) or a **Team service** (something our team does around the product). Team services are not product features and must never be described as such.

## The head of talent (Kavya)

Her first encounter is the walkthrough, before signing. Every other step happens after signing.

| Element | When | What it is | Intended effect | Product or team service |
|---|---|---|---|---|
| The 2-minute walkthrough | Before signing | She fills one card on labelled sample data, then sees a pooled record | Anticipation: she has already seen what April could look like | Team service (built from prototype screens). Price and order are not part of this element |
| Kickoff session | Cycle 0 | 45 minutes with our team: she leaves with the date cycle 1 opens and a cycle-by-cycle list of what she will see and when ([anticipation plan, moment A](anticipation_plan.md)) | Anticipation | Team service |
| Her firm's words on the card | Cycle 0 | She types the firm's own values into "Organization VBAs" and presses "Save & cascade". The next card any consultant opens shows those words | Contribution matters: the card speaks her firm's language, not a vendor's | Product: Admin, Organization VBAs[^proto] |
| The schedule preview | Cycle 0 | She picks "Fortnightly" and sees "Current cycle starts / ends" and "Next starts" dates | Anticipation: a real date, not "soon" | Product: Admin, Feedback Frequency[^proto] |
| Member import | Cycle 0 | Upload a CSV, XLS or XLSX file; approve domain signups | (Setup, no effect claimed) | Product: Admin, Member Directory. Our team may do the upload with her as a team service |
| The invitations go out | End of cycle 0 | The partner note and the consultant invite, sent in her name or the managing partner's ([moments B and C](anticipation_plan.md)) | Anticipation, for everyone else | Team service (we draft, she sends) |
| First participation number | End of cycle 1 | Each team's manager view shows "Participation", for example "24 of 25 reviews given" | Discovery: proof in week two that she is not chasing forms | Product: Manager views[^proto]. See the gap below |
| First readout session | End of cycle 1 | 30 minutes where she and the engagement managers open their own Team Insights while our team explains how to read a first cycle | Discovery and reason to return | Team service. Our team never sees or prepares the firm's ratings |

Gap: the prototype shows participation per team in the manager views. It shows no organization-wide participation view for an admin.[^proto] Kavya either holds a manager role for the pilot teams or asks each engagement manager. Do not promise her an HR-wide dashboard ([do-not-claim](../product/do_not_claim.md)).

## Partners and engagement managers

In the product they are the "Manager" role. They are also rated by their own circle: in Sphyr "a manager is considered as just another employee" (whitepaper p5).[^wp]

| Element | When | What it is | Intended effect | Product or team service |
|---|---|---|---|---|
| The partner note | End of cycle 0 | A short note from Kavya or the managing partner: what partners will open in April, in partner words ([moment B](anticipation_plan.md)) | Anticipation | Team service (we draft) |
| The April preview | Cycle 0, at the partners' meeting | Ten minutes showing one sample consultant's record across four engagements, labelled as sample data, then the same screen empty for their own people | Anticipation: they see the record they will have, and that it starts filling now | Team service, using the prototype's Member Insights screen[^proto] |
| Their own first cards | Cycle 1 | The same two-minute deck as everyone else | Contribution matters: their view goes into the record like anyone else's | Product: Provide Feedback[^proto] |
| First Team Insights | End of cycle 1 | Team score, participation, rating distribution, anonymized team feedback, for the engagement team they run now | Discovery: how the team is landing while the engagement still runs | Product: Manager, Team Insights.[^proto] **Timing is our assumption**: no source says how soon this view fills |
| Feedback edit approvals | Any time from cycle 1 | They approve or reject requests to reopen submitted feedback. This queue shows who gave feedback to whom | (Governance, no effect claimed) | Product. This is why no copy may say "anonymous to everyone" |

## Consultants (Meera)

Her first encounter is the invite. She did not choose to buy Sphyr, so the first thing she hears decides whether she reads it as "a voice" or as "being watched".

| Element | When | What it is | Intended effect | Product or team service |
|---|---|---|---|---|
| The invite | End of cycle 0 | From the managing partner: the people who saw your work get a say, they rate you as you rate them, and what you get back and when ([moment C](anticipation_plan.md)) | Anticipation | Team service (we draft, the firm sends) |
| Building her circle | Before cycle 1 opens | In "My Sphyr" she adds peers, seniors and juniors she works with. From cycle 2 she may invite a client counterpart by email, only with the partner's agreement | Anticipation: she is choosing who gets a say in her year | Product: My Sphyr and email invites for external members (product guide p5).[^proto] The partner-agreement rule is the firm's rule, not a product setting |
| The cycle opens | Cycle 1, day 1 | "FEEDBACK THIS FORTNIGHT": a short deck, one card per person in her circle | Anticipation turns into use | Product: Provide Feedback[^proto] |
| Her first card | Cycle 1 | Was good / Could improve / No interaction, then tags in her firm's words, then an optional note to the person by name | Contribution matters ([first card reward](first_card_reward.md)) | Product |
| Feedback arrives for her | During cycle 1 | A notification that new anonymized feedback has been received | Discovery and reason to return | Product, from bundle text only: "Feedback received: You received 4 new items of Anonymized ..."; not seen rendered[^dnc] |
| Her first own Insights | After cycle 1 closes | Her Insights page starts filling with what came in. The trend line needs several cycles | Discovery and reason to return | Product screen exists. **Timing is our assumption**: no source says when Insights first shows numbers or how many raters it needs |

## What each audience has at the first readout

| Audience | First readout | What they have | What they do not have yet |
|---|---|---|---|
| Head of talent | End of cycle 1 | A participation number per team; the firm's own words on every card; a date for each next cycle | Any trend; any April record |
| Engagement managers | End of cycle 1 | A first Team Insights view for the team they run now | A trend across cycles |
| Partners | End of cycle 1, and in April | Their own cards done; their teams' first views | The full-year record, which builds every cycle until April |
| Consultants | After cycle 1 closes | Tags and anonymized notes from people in their circle | A trend line or peer comparison that means much; both need several cycles |

## Edge cases built into the design

- **No interaction is a real answer.** A consultant on the bench taps "No interaction" and is done. The card does not force a rating.
- **Small engagement teams.** In a team of three to five, a first-cycle note can be easy to attribute. No source gives a pooling threshold. The kickoff tells Kavya this plainly, and copy promises only that ratings are pooled and comments are anonymized to the person rated.
- **A thin circle.** A consultant with three people in her circle gets three cards and few ratings. The invite asks her to add everyone she worked with this year who is still at the firm.
- **Cycle 1 in a deadline week.** The go-live date is agreed at the kickoff and read from the schedule preview, which shows cycle dates "based on the current organization calendar". The prototype shows no control for picking a start date (its demo cycle starts on a Monday). The kickoff checks the date against known client deadlines.
- **A missed first cycle.** The Insights page counts missed cycles ("Missed Fortnightly Cycle"). Nobody is chased; the next cycle opens in two weeks.
- **A partner who will not fill cards.** His view is simply missing from the record. Kavya raises it in the readout session; the product does not enforce it.

## What we do not promise in first use

An HR-wide dashboard, a promotion screen, integrations, Slack or Teams reminders, AI, or "anonymous to everyone". Full list: [do-not-claim](../product/do_not_claim.md).

[^proto]: Prototype screen inventory
[^wp]: Sphyr Overview Whitepaper v0.3
[^dnc]: Do-not-claim list, method notes
