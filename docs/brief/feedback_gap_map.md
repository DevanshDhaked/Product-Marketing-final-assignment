---
type: Research Note
title: "Feedback gap map"
description: "For each professor feedback point, what the graded submission said and what was missing."
tags: [feedback, gaps]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
sources:
  - resource: "brief/professor_feedback.md"
---

# Feedback gap map

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Paths like `tasks/saas/...` and `sphyr/...` are relative to the course folder `sem_3/pm/` on the team's machine, outside this repo.

Source of feedback: [professor feedback](professor_feedback.md). "Prior work in repo" lists drafts that already touch the point (not fixes, only pointers).

## 4.1 Pricing (70/100), `Sphyr_Pricing_OnePager.pdf`

| Feedback point | What the submission said (verbatim) | What is missing |
|---|---|---|
| Value calc: show how one resignation a year becomes ₹500 per employee per month | "₹667 Per employee a month: one fewer resignation a year (₹500) + less review prep (₹167)." "Costs and value are team estimates." | No replacement-cost figure, no salary assumption, no company size behind "one fewer resignation", no attribution logic (why Sphyr causes it), no source for ₹167 review prep (hours x rate). Prior work in repo: `teammate-contrib/positioning-answers.md` §5 Gallup 0.5 to 2x salary, ₹25 L CTC, ₹12 to 50 L per exit; foundit 2026 "52% were job-hunting during appraisal season"; whitepaper cost study US$85 vs US$63 per employee and 1,000 manager-minutes for 20 reports (`positioning-statement/product_evidence.md`) |
| Competitive comparison: like-for-like products, name plans, basis of comparison | "₹665–1,425 Per employee a month for Leapsome, Lattice and Peoplebox." "Competitor list prices read 2 Nov 2026 at $1 ≈ ₹95." | No plan names, no feature mapping, no note on minimums (Lattice $4,000/yr), Leapsome has no public price per `competitor-brief.md:77`, the range equals Peoplebox's G2 band $7 to $15 alone (inference), Lattice $11 and 15Five Perform $11 not shown as plans, and Indian HRMS modules (Keka, Darwinbox, ₹50 to 150) are absent although they are the real alternative named in `teammate-contrib/positioning-answers.md` §8 |
| 150 vs 149, and why capture only ₹149 of ₹667 | "₹30 ÷ (1 − 80% margin) = ₹150 floor"; "Customer keeps 78% of the value"; "Sphyr is one-fifth or less" | No reason for dropping below own floor (charm pricing or not), no argument for leaving 78% with the customer (new-brand risk, adoption, competitor anchor, Indian HRMS anchor), no statement of where in the value-cost-market band 149 sits and why |
| Break-even: break down ₹8 L fixed cost; show ₹119 includes all variable costs | "₹119 earned per employee after costs ₹8 L fixed costs a month ÷ ₹119 ≈ 6,700 employees, about 67 companies of 100"; "₹30 To serve one employee a month: hosting, AI, support, payments." | No line items for ₹8 L (team, salaries, office, tools, marketing). ₹30 is one lump; onboarding labour for "Setup, training and support" (included in price) and GST/payment fees not shown separately; no time-to-break-even |
| Pilot: how ₹15,000 was set, why six weeks, what if no conversion | "6-week pilot, one team of up to 25: ₹15,000, adjusted against the first yearly bill" | No derivation (it is about ₹435 per employee-month, 2.9x list, my arithmetic); six weeks is 3 cycles while other team docs say about 6 cycles / 12 weeks are needed for a signal; no non-conversion rule (refund? keep data? export?) |
| Van Westendorp: how results drive an actual decision | "Van Westendorp price survey with 40–60 HR buyers, pilot-to-paid conversion, and a quarterly margin review" | No decision rule (e.g. what happens if acceptable range excludes 149), no target respondent consistent with founder buyer (it says HR buyers), no threshold for pilot-to-paid conversion, no trigger tied to the margin review |
| Overall: show how assumptions were reached and why to trust them | "Costs and value are team estimates." | Every key number (₹30, ₹8 L, ₹500, ₹167, ₹15,000) is stated without a source or a worked calculation |

## 4.2 Packaging (69/100), `packaging/packaging-team03.pdf`

| Feedback point | What the submission said (verbatim) | What is missing |
|---|---|---|
| 1. Reduces hesitation more than it creates excitement; build anticipation before first use | Assurance language throughout: "No form to read any of it, and no need to call sales."; "full refund if the first six fortnightly cycles ... show the founder nothing new"; "Runs alongside the current HR system, so nothing is replaced."; "Can my manager see who wrote what? No." | No element names what the buyer or employee looks forward to, or what they anticipate before first use. Prior work in repo: professor's own vision words in `positioning-statement/professor_lens.md` ("a voice in the assessment of peers", "insights into their blind spots", "an opportunity to improve their bonds"), and employee value line in `teammate-contrib`: "Credit from everyone you helped, not just whoever your manager noticed." |
| 2. Too much acquisition (AIDA, refunds, order process, renewal incentives, CAC) | Whole "HOW IT SUPPORTS ACQUISITION (AIDA)" block: Awareness, Interest/Decision (refund, renewal reminder, export), Action ("One-page online order ... one month's credit on the first renewal"), CAC row | About one third of the page is outside scope (encounter to first use). The packaging brief in `packaging-notes.md` itself asked for AIDA and CAC ("It must support AIDA", "CAC is the money spent to convert 1 customer"), so the class notes and the grader disagree; flag for the team |
| 3. First-use experience: what does the user get from the five-click card? | Guided setup step 5: "support stays on until everyone can finish a real five-click card"; video "Your first card in 2 minutes."; invite "It takes two minutes every two weeks." | No payoff after the first card: no feedback received back, no "your contribution counted" signal, no first insight, no reason to return in two weeks. Journey already had partial ideas, not carried into packaging: team-03.pdf #16 "Keep each employee's own dashboard useful to them personally: a trend line built from people they actually work with" and #17 "A short, personal nudge built from someone's own results". Note: the first trend line needs several cycles, so cycle 1 payoff must be something else |
| Overall: state what each element is meant to achieve | Table columns are "Element / What it includes / Sample content" | No "intended feeling or outcome" column per element |

## 4.3 Combined: Segmentation, Persona, Journey, Messages, Channels (63/100), `submissions/team-03.pdf`

| Feedback point | What the submission said (verbatim) | What is missing |
|---|---|---|
| Wrong column: "Relevant" should be "Can we do anything about it?" | Column header "Relevant", 19 of 20 rows "Y". Touchpoint 1: "The company grows to around 120 employees and starts operating across multiple teams or offices, so Rohan can no longer personally see everything anymore." Y, "Show that growth changes visibility ..." | No actionability test per touchpoint. Several touchpoints are conditions Sphyr cannot change (growth itself, #1; managers disagreeing, #4), and the table does not separate those from moments Sphyr can act on. Prior work in repo: `positioning-statement/consulting_pain.md` "Can we do anything about it?" table (Yes / Partly / No per pain), written for consulting |
| Social proof when there are no reviews: what could make validation-seeking better? | #8 "Before booking a demo, they check review sites for what other buyers said." N, "Sphyr is new and has no reviews yet. This step matters more once real customers exist, not on day one." | Any substitute proof on day one. Prior work in repo: `positioning_drafts.md` "Social proof when no reviews exist" (design-partner cohort 3 to 5, publish pilot numbers, peer references, borrowed research credibility); `product_evidence.md` 2018 pilot "2 min 09 s", fairness acceptance "about 94%" with caveats; `teammate-contrib` §17 pilot targets; Scullen et al. 53 to 62% rater variance |
| Journey is detailed but not personal; distant, no empathy | Buyer description is about "The buyer company"; Rohan named once in #1, then "the founder", "they", "his COO"; no feelings, quotes, or stakes | Rohan's thoughts and feelings per stage, his words, what is at risk for him, a concrete story (named employee who left). Prior work: Meera story in `consulting_pain.md` (consulting); quiet-engineer sales story in `teammate-contrib` §19 ("the quiet engineer who unblocked three teams and resigned after being passed over") |
| Message is a slogan, not a guideline for a junior copywriter and designer | "Built from everyone who actually worked with them, not one manager's memory. That's Sphyr." | Always-say order, proof per claim, never-say list, tone, vocabulary, visual rule, per-audience variants. Prior work: `positioning_drafts.md` "Guideline for a copywriter or designer" (consulting); `teammate-contrib` §3 per-role value messages and §14 founder language and words to avoid; `channel-messaging-plan.md` per-channel taglines (HRBP era) |
| No money, no creepy or privacy-invading marketing: how does the channel list change? | Channels 1 "cold emails", 3 "LinkedIn ads / Google SEO" (paid targeting) | No zero-budget or consent-based channel option; two of four channels depend on cold outreach or paid targeting; no privacy stance on how prospects are found. Prior work: `positioning_drafts.md` "works with no paid budget and no tracking or targeting"; `channel-messaging-onepager.pdf` Phase 1 (personal intros, communities, own-site content) |
| Segmentation and persona | No specific comment in feedback.md | Combined grade covers them; persona has no standalone page in the graded PDF (see 2.2) |
