---
type: Handoff
title: "First-use packaging teammate report, phase 1b"
description: "Plan, progress and final summary from the first-use packaging work: feedback map, research, decisions, rejected approaches and open product questions."
tags: [handoff, firstuse]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T18:20:00Z }
---

# First-use packaging teammate report, phase 1b

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Status: done. All four files committed on d1-firstuse. Idle, waiting for the lead.
Worktree: `Product-Marketing-final-assignment.d1-firstuse`, branch `d1-firstuse` from `iteration-a` (03aef9a).
Success number: 3 of 3 packaging feedback points answered in docs/packaging/; 0 of 3 on the site yet (the site writers use packaging_summary.md).

## Plan

### Scope and end point
- Packaging here means only what happens between first encountering the product and actually using it. It ends at each audience's first readout. The journey map Stage 6 already hands setup, invitations and the first card to `docs/packaging/` and starts after the first cycle, so there is no overlap. For the fortnightly moments after that, I link to the after-purchase table in `docs/strategy/acquisition_engagement.md` instead of copying it.
- Out of scope in every file: AIDA, price, refunds, the order process, renewal incentives, CAC and persuasion to buy. This rule answers feedback point 2 across all four files.
- Audiences: the head of talent (Kavya), partners and engagement managers (in the product they are the "Manager" role), and consultants (Meera). The managing partner (Vikram) is covered as a partner.
- Timeline is written in cycle numbers (cycle 0 = setup, cycle 1, cycle 2, ...), not in weeks, because the pilot length is still open (3 or 6 cycles, `prior_work/source_conflicts.md` row 11).

### Timing facts I will use, split by evidence
Shown in the prototype (`product/prototype_screens.md` 3.3, 3.1, 3.7):
- Rater, during and after the first card: the "4 of 17" counter and progress bar, "THIS CYCLE 3 Completed / 14 Remaining", the "Submitted · Read only" list, the "Private by design" card ("Individual responses are normalized and grouped before anyone sees them."), the "4-cycle streak · 8 weeks" pill, the comment helper "Your comments and review are always anonymized."
- Person rated, during the cycle (bundle text only, not seen rendered): "Feedback received: You received 4 new items of Anonymized ...".
- Managers: "Participation 96%, 24 of 25 reviews given", Team Insights, Member Insights.
- Reciprocity (true and the main anticipation lever): the same circle you rate this fortnight is rating you (WP p1, `product/product_facts.md` 1.4). The first card is the first half of an exchange, so the cycle-1 payoff does not have to be a chart.

Not stated by any source:
- When Insights first shows numbers to a person, and any minimum number of raters. The prototype Insights is built "from your last six feedback cycles" on demo data.
- Default wording I propose (see question 2): "After your first cycle closes, your Insights page starts filling with what came in. The trend line needs several cycles." Labelled as our assumption to confirm against the product, not as a product fact.

### Files in docs/packaging/

1. `first_use_experience.md` (Journey Map type)
   - Purpose: the receiving journey from first encounter to first readout, per audience.
   - Outline: how to read it; one table per audience with columns Element, When (cycle), What it is, Intended effect (anticipation / contribution matters / discovery / reason to return), Product fact or team service (with source); what each audience has by the end of cycle 1 and by the first readout; what we do not promise.
   - Head of talent: one bridging row for the walkthrough (first encounter) with no price, order or persuasion content; then admin setup (file import, firm's own values as card options, frequency), kickoff, invitations, first cycle, first Team Insights view.
   - Partners and engagement managers: the partner note, the April preview, their own first cards (they are rated too), first Team Insights and participation.
   - Consultants: the invite, building My Sphyr, first card, first "feedback received", first own Insights.
   - Answers the overall comment ("be more precise about what each element is intended to achieve") through the intended-effect column.

2. `anticipation_plan.md` (Plan type)
   - Purpose: the specific moments before first use that build anticipation, with draft copy.
   - Outline: why reassurance is not enough (the feedback, one line); the anticipation moments in order, each with who, when, what they are told they will get back and when, and the draft copy:
     a. Kavya's kickoff session (team service): she leaves with a cycle-by-cycle picture of what she will see and when.
     b. The partner note and "April preview" (team service): what the record will look like at calibration, shown on labelled sample data, so partners know what they will open in April. Anticipation device only, not the calibration.
     c. The consultant invite from Kavya or the managing partner (team service, drafted by us): "the people who saw your work get a say", reciprocity, what you get back after the first cycle and after several.
     d. Building My Sphyr before cycle 1 (product): choosing who will see and rate your work.
     e. The first cycle opening (product): "FEEDBACK THIS FORTNIGHT".
   - Every element is labelled Product or Team service. Draft copy is run through `humanizer:humanizer`.
   - Answers feedback point 1.

3. `first_card_reward.md` (Concept type)
   - Purpose: what happens on and right after the first card, for the rater and the person rated, and the reason to return each fortnight.
   - Outline: what the rater gets on screen during and after the card (prototype facts above); contribution matters (the firm's own values on the card, the comment goes to the person by name, anonymized to them; the progress counter; the circle is rating you back); discovery (first "feedback received", first comments, first strongest signal once Insights fills, with the timing caveat); reason to return (the record grows, the trend needs several cycles, the streak pill, April); what the person rated sees and when; what we must not say.
   - Answers feedback point 3.

4. `packaging_summary.md` (Concept type)
   - Purpose: one page the website writers can lift for a "what happens after you sign" section.
   - Outline: a 4 to 5 step sequence per audience in plain words, each step with what the reader can look forward to; a short "what you see after your first card" block; honest timing line; claims to avoid. Humanized.

Plus `docs/packaging/index.md` (built by the tool for this subfolder only) and `docs/packaging/log.md`.

### Feedback map (filled in at the end with section anchors)
| Feedback point | File | Section |
|---|---|---|
| 1. Create excitement, build anticipation before first use | `anticipation_plan.md` | anticipation moments a to e |
| 2. Keep out acquisition (AIDA, refunds, order, renewal, CAC) | all four files | scope rule in each file's opening; `first_use_experience.md` scope section |
| 3. First use must be rewarding | `first_card_reward.md` | contribution matters, discovery, reason to return |
| Overall: state what each element is meant to achieve | `first_use_experience.md` | intended-effect column |

### Not carried over from the graded PDF
- The FAQ "Can my manager see who wrote what? No." The prototype's feedback edit approvals show managers who gave feedback to whom.
- The founder and IT-firm framing. The segment is now consulting.
- "Direct HRMS connectors come later." Roadmap claim.
- "Sphyr imports the employee list" as a product act. The admin's file import is the product; our team doing it for the firm is a team service.
- The refund, renewal reminder, one-month credit and AIDA block (feedback point 2).

### Process
- Load `hack-kit:okf-docs` before writing. Own `log.md` in `docs/packaging/`. Run `build_index.py` for `docs/packaging` only and the validator; fix errors. Never touch root `docs/index.md` or `docs/log.md`.
- Research (after approval, small): firecrawl or exa only, cited with URL and access date 2026-11-24. Two questions: (a) evidence that anticipation and pre-use expectations shape how a first experience is judged; (b) evidence that showing people their input was used ("closing the loop") raises later response rates in feedback or survey programs. If nothing solid turns up, I say so and the files stand on product facts alone. No studies named from memory.
- Humanizer on draft copy in `anticipation_plan.md` and `packaging_summary.md` before commit.
- One commit per file, explicit paths, short message. No push, no merge.

### Questions for the lead (each has a default; "approved" accepts all defaults)
1. First encounter scope. The professor's definition starts at "first encountering the product" and he praised the walkthrough; the brief says "from signed". Default: for consultants and most partners, first encounter comes after signing (invite or kickoff). For the head of talent it is the walkthrough, which gets one bridging row with no price, order or persuasion content.
2. First own result. Default: the wording in "Not stated by any source" above, marked as an assumption to confirm.
3. Team services do not read firm ratings. Default: any "first readout" is a session where Kavya and the partners open their own Team Insights and Member Insights while our team explains how to read them. Our team never prepares a readout from the firm's data.
4. Pilot length. Default: cycle numbers only, no weeks, until the pricing work decides.
5. Clients in the first cycle. Default: no client counterparts in cycle 1; a partner may add one from cycle 2 onward, once per engagement phase at most (matches the journey map).
6. Small engagement teams. Teams of 3 to 5 make first-cycle comments easy to attribute, and no source gives a pooling threshold. Default: copy promises only "ratings are pooled and comments are anonymized to the person rated", and the kickoff tells Kavya this risk plainly. Does not block the plan.
7. Time budget. How long do I have for phase 1b? Default: aim to finish all four files in one pass, research capped small.

## Progress

- 2026-11-24: Plan approved by the lead, all seven defaults accepted. No hard time limit, quality first, research capped small. Extra instruction: anticipation copy must feel exciting, not only clear. Starting work.
- 2026-11-24: Research done (3 sources, below). Four files written, humanizer pass on all draft copy, OKF validator 0 errors (4 warnings, all pre-existing outside docs/packaging/). Advisor review found 3 accuracy problems; fixed in e969c01.

## Final

### Files written, with commit SHAs (branch d1-firstuse)
| File | Commit |
|---|---|
| `docs/packaging/first_use_experience.md` | 9e59571, fixed in e969c01 |
| `docs/packaging/anticipation_plan.md` | 925954e, fixed in e969c01 |
| `docs/packaging/first_card_reward.md` | 6aed9ea |
| `docs/packaging/packaging_summary.md` | 0b939c2, fixed in e969c01 |
| `docs/packaging/index.md`, `docs/packaging/log.md` | 6f4807e, log updated in e969c01 |

Action for the lead on merge: the root `docs/index.md` needs the line `* [packaging](packaging/index.md) - ...`. `build_index.py` added it; I reverted it because the brief forbids editing the root index.

### Feedback map
| Feedback point | File | Section |
|---|---|---|
| 1. Create excitement; build anticipation before first use | `anticipation_plan.md` | "The five moments" (table) and sections A to E, each with draft copy; "Three rules for every moment" |
| 2. Keep out acquisition (AIDA, refunds, order, renewal, CAC) | all four files | Scope line near the top of each file; `first_use_experience.md` "Scope"; `packaging_summary.md` "Rules for this section" |
| 3. First use must be rewarding | `first_card_reward.md` | "The core idea: the first card is half of an exchange", "The rater: on the card", "The rater: right after the card", "The person rated: during and after the first cycle", "The reason to return each fortnight" |
| Overall: state what each element is meant to achieve | `first_use_experience.md` | "How to read the tables" and the "Intended effect" column in every audience table |

### Key insights and findings
- Reciprocity is the strongest true anticipation lever: the circle you rate this fortnight rates you (whitepaper p1). The first card is half of an exchange, so the cycle-1 reward can be words from colleagues, not a chart.
- The comment prompt is addressed to the person by name ("Let [name] know what's on your mind?"). That is the product's own "your contribution reaches someone" signal.
- The admin's "Save & cascade" puts the firm's own words on every card. This gives the head of talent a concrete pre-use moment.
- The empty Member Insights screen for the partners' own practice, shown next to a labelled sample, makes the April record something to look forward to.
- The prototype demo cycle starts on a Monday (14 Sep 2026) and the reminder text says "Due Friday". There is no start-date control, only frequency and a preview.
- The product guide p5 says external members are invited by email from My Sphyr. A partner does not add them. `docs/strategy/journey_map.md` (Stage 5 client row, Stage 6) says "partner adds" or "partner opts the client in". This mismatch is outside my folder; the strategy owner should fix it.
- The graded PDF's FAQ "Can my manager see who wrote what? No." is contradicted by the prototype edit approval queue. It was not carried over.
- Research (all accessed 2026-11-24, used as analogy only, sample sizes not retrieved):
  - Kumar, Killingsworth, Gilovich, Psychological Science 2014, https://doi.org/10.1177/0956797614546556: waiting for experiences is more pleasant and exciting than waiting for objects (4 studies, incl. a large experience-sampling study).
  - Chun, Diehl, MacInnis, Journal of Marketing 2017, https://doi.org/10.1509/jm.150267: savoring an upcoming experience raises enjoyment during it and as it is remembered (5 studies).
  - McKinsey Organization Blog, 10 May 2021, https://www.mckinsey.com/capabilities/people-and-organization/our-insights/the-organization-blog/survey-fatigue-blame-the-leader-not-the-question: a review of more than 20 academic articles found the main driver of survey fatigue is the belief that results will not be acted on; sharing and acting on results raised later participation. Direct fetch returned 403; text read via exa.

### Decisions and why
- Timeline in cycle numbers, not weeks: the pilot length is still open (source_conflicts row 11).
- No individual score or trend promised for the first fortnight. The first thing a consultant sees should be colleagues' words, and a score from few ratings would mislead.
- Our team never reads or prepares firm ratings. The "first readout" is a session where the firm opens its own views.
- Clients are not in cycle 1. From cycle 2, the consultant invites them by email with the partner's agreement. This is a firm rule, not a product setting.
- Reassurance lines moved to the FAQ and side notes. Openings lead with what each person gets.

### Approaches rejected and why
- Added badges, points or leaderboards: the product has a streak pill and counters only (do_not_claim item 15), and it would read as a game about rating colleagues.
- A team-written first-cycle readout of individuals: privacy, and it would need our team to see ratings.
- Copy saying "every second Friday" or "pick the Friday": there is no evidence the product starts cycles on Friday or lets the admin pick a date.
- Reusing the graded PDF's refund, renewal credit, AIDA block, HRMS-connector line and "Sphyr imports the employee list" as a product claim.

### Open questions
1. When does a person's Insights page, or a team's Team Insights, first show results, and with how many ratings? All cycle-1 promises are marked as assumptions until this is confirmed.
2. Is the strategy owner fixing the "partner adds the client" wording in `journey_map.md`?
3. Pilot length (3 or 6 cycles) from the pricing work. It decides how many cycles exist before the April preview becomes a real record.

### What I did not verify
- The "Feedback received" notification text comes from the code bundle only. Nobody has seen it on screen.
- How reciprocity works on screen: whether adding someone to your circle puts you on their deck. Moments C and E depend on it.
- The prototype shows no organization-wide participation view for an admin. Kavya needs a manager role or the engagement managers' numbers.
- Whether a partner can open Member Insights for consultants outside the teams they manage, which calibration needs.
- The research sample sizes, and the full papers (abstracts only).
- The timings I proposed for the kickoff (45 minutes), readout session (30 minutes) and April preview (10 minutes). They are proposals, not tested.
