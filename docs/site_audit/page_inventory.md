---
type: Research Note
title: "Current site page inventory"
description: "Each page of the site at commit fc85cac with its sections, headline, calls to action, and the strategy it states."
tags: [site, audit]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
commit: fc85cac
sources:
  - resource: "site/"
---

# Current site page inventory

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Paths are relative to `site/`. Audit of commit fc85cac on 2026-11-24.

Shared chrome on every page: sticky dark nav (logo, How it works, Walkthrough, Pricing, Trust, green "Deliverables (4)" pill) and footer with team credit, "Not a live commercial offer", and links to all three non-site deliverables plus the hub (e.g. index.html:21, index.html:135). So every deliverable is at most one click from any page.

## index.html (Home). Serves: Website (01), hub.
Purpose: problem-led landing for founders and Heads of People, plus a visible deliverables strip for the grader.
Sections in order:
1. Hero, split (index.html:24-49). Eyebrow "For growing companies". H1 "Promote on merit, not politics." (27). Lede "Your company grew faster than anyone's line of sight..." (28). CTAs: "Try the 2-minute walkthrough" -> demo.html, "One price: ₹149" -> pricing.html (29). Right: playable five-click feedback card for "Priya R." (32-48); after send: "See what the founder sees ->" demo.html (46).
2. Deliverables strip (51-59), eyebrow "Course submission · Team 03 · all four deliverables", 4 cards -> index, propaganda, linkedin, ad.
3. The problem (61-70). H2 "At 40 people you saw everyone's work. At 200, you see whoever reaches you." Three cards: loudest voice, recency, quiet contributor leaves.
4. One view vs everyone (72-79). H2 "One rater is a guess. Fourteen, every fortnight, is evidence." one.svg vs sphere.svg; Scullen, Mount & Goff 2000 stat (76).
5. Meera's story (81-90), labelled "illustrative, not a customer case". 4 cards Trigger / Search / Evaluate / Act.
6. Fortnight loop (92-102). H2 "Two minutes, every two weeks". 4 steps. CTA "How it works in detail ->".
7. Evidence (104-113). Eyebrow "2018 pen-and-paper pilot of the method, not today's software". Stats: 2m 9s, 0% collusion, 787 (Galton 1906, which is not part of the 2018 pilot; mislabelled grouping).
8. Pricing teaser (115-127). H2 "One price. No tiers. No surprise when you hire." Card: pilot, refund, CSV/XLSX. CTA "See pricing and the pilot".
9. Closing (129-132), centered. H2 core line "Built from everyone who actually worked with them, not one manager's memory. That's Sphyr." CTAs walkthrough, "How anonymity works".
Links out: demo, pricing, how-it-works, trust, propaganda, linkedin, ad, deliverables.

## how-it-works.html. Serves: Website (Interest stage).
Hero H1 "Many honest views, pooled over time." (26). Sections:
1. The Sphere (30-38): who is in it; clients and vendors free.
2. The card (40-50): 3 cards (rating, tags, note); seven parameters listed (48); 2m 9s pilot note (49).
3. Pooling and anonymity (52-61): H2 "Nobody sees who wrote what. Not the manager, not HR." 3 cards. CTA "Full trust and data page ->".
4. Values cascade (63-71): 3 steps.
5. Decisions stay human (73-87): "Managers still decide. Now they have evidence." Table CSV/XLSX Available, HRMS connectors Planned.
6. Getting started (89-100): H2 "Guided setup, not a login and good luck". 5 steps (kickoff, import, training, first-cycle, handover + 30-day renewal reminder). CTAs walkthrough, pricing.

## demo.html (Walkthrough). Serves: Website (Consideration), the packaging "good demo" the professor liked.
Label "Sample data · fictional people and company" (33), 4-step progress bar.
1. Step 1 (36-44) "Promotion round next week. One senior engineer slot." 180-person company. Pick Karan (visible) or Priya (quiet).
2. Step 2 (46-63) fill one feedback card.
3. Step 3 (65-78) "Six fortnights. Fourteen people each. One picture." Pooled bar table of the 7 parameters, Priya vs Karan (data at 108-109), most-used tags.
4. Step 4 (80-87) "Same two people. Now you can see the work." Core line (84). CTAs "Start a ₹15,000 six-week pilot" -> pricing.html#order, "See pricing", "How anonymity works", "Restart".

## pricing.html. Serves: Website (Consideration/Action), pricing + packaging rubric line.
1. Hero split (24-45): H1 "One price. ₹149." Lede no tiers / no free plan / no volume discounts. Line "Fairness is the product, so the pricing should be fair too." (29). Price card with inclusions; CTAs "Start the ₹15,000 pilot" -> #order, "Try the walkthrough first".
2. Calculator (47-61) "Do the maths": headcount -> monthly, annual, GST 18%, first bill after pilot credit.
3. Start / Commit / Renew (63-72): pilot (3 cycles), refund after 6 cycles on annual plan, renewal terms + 30-day reminder + one month credit. First-25 price lock card with "(Offer pending faculty confirmation.)" (71).
4. Why ₹149 (74-83): 4 `<details>`: cost ₹30 -> ₹150 floor (79), value ₹667 with no arithmetic (80), market = Lattice $10/seat at ₹93/USD checked 24 Nov 2026 (81), why flat (82).
5. Order (85-100): H2 "Start your pilot", 4-field form, submit "Request the ₹15,000 pilot", note "Course prototype: this form doesn't send any data." (98).

## trust.html. Serves: Website (Consideration), trust/anonymity objection.
H1 "Honest feedback needs real anonymity." (26). Sections: who-sees-what table (31-37), three rules (40-47), "Feedback, not surveillance" + collusion card (49-60), Your data `<details>` x4 + honest note that hosting/encryption/certs are not claimed (62-70). CTA "See the anonymized view in the walkthrough".

## deliverables.html. Serves: hub for the grader.
H1 "All four deliverables" (26), 4 cards (28-33). "The thread through all four" (36-51): Segment / Central message / Offer cards, then a journey-stage table mapping each artefact to Awareness, Interest, Consideration, Action, Retention.

## propaganda.html. Serves: Propaganda strategy (02).
Hero H1 "Shift the belief before the pitch." (26). Sticky TOC (32-34, hidden under 900px). 13 numbered sections: 1 Summary (37-40), 2 Audience incl. anti-segment (42-55), 3 Belief to shift: belief/attitude/response table (57-65), 4 Central message hierarchy + fallback "merit, not memory" (67-76), 5 Tactics table x8 (78-89), 6 Channels x5 (91-99), 7 Campaign sequence weeks 1 to 7+ (101-108), 8 Persona in action (110-120), 9 Journey and retention with metrics (122-132), 10 Positioning statement (134-136), 11 Expected response (138-145), 12 Objections (147-155), 13 Guardrails (157-165). Footer nav to LinkedIn and ad (166).

## linkedin.html. Serves: Three LinkedIn posts (03).
Hero H1 "Three posts. Three jobs. One promise." (26), jump buttons. Each post = LinkedIn mock left + rationale table right (Purpose, Audience, Angle, CTA, Why on LinkedIn).
- Post 1 (33-70) Week 1: "She unblocked three teams last quarter. Her name came up in zero promotion discussions." Story of Priya; CTA comment question; link in first comment -> index.html.
- Post 2 (72-116) Week 3: Galton ox hook, Scullen 2000, core line, image one vs Sphere; CTA walkthrough in comments -> demo.html.
- Post 3 (118-159) Week 5: "₹149. One price. Here's why we didn't make it tiered." Offer, pilot, refund, first-25 trade; image price card; CTA -> pricing.html.
- "How the three work together" table (161-172).

## ad.html. Serves: Advertisement (04).
Hero H1 "One image. One promise. Two seconds." (26). LinkedIn Sponsored Content mock (32-57): intro text, 1:1 dark creative "Promote on merit, not politics." with one-vs-Sphere, proof line, "₹149 / employee / mo billed annually", CTA strip "See the pooled view in 2 minutes" + "Learn more" -> demo.html. Rationale table (59-72): medium, audience/targeting, message, benefit, visual, CTA, pricing consistency, journey stage, A/B test.

---

## 2. Strategy as the site states it

- Segment: "Founders of growing companies (50–300 people) who sign off on promotions but can't see who did what" (deliverables.html:40; propaganda.html:38, 45). Core geography/vertical: "Mid-size IT services and digital engineering firms in Bengaluru, Hyderabad, Pune, Delhi NCR and Chennai" (propaganda.html:45). Public copy uses only "growing companies" (index.html:26).
- Anti-segment: under ~50, large enterprises with mature HR suites, buyers who want monitoring, buyers replacing HRMS (propaganda.html:50-55). This closes devansh_notes.md open item 4 partly.
- Persona: "Meera, Head of People" as champion (deliverables.html:40); "Head of People at a 350-person IT services company, the kind of firm that has just outgrown our core 50–300 band" (propaganda.html:111). Home calls it only "a growing IT services company" (index.html:85). Decision maker = founder; amplifiers = quiet contributors (propaganda.html:45-47).
- Central message: promise "Promote on merit, not politics." + core line "Built from everyone who actually worked with them, not one manager's memory. That's Sphyr." (propaganda.html:40, 70-71; index.html:27, 130; demo.html:84). Proof words "two-minute, anonymous, everyone" (propaganda.html:75). Reframe "the company grew faster than anyone's line of sight" (propaganda.html:65; index.html:28; ad.html:34). Fallback "merit, not memory" (propaganda.html:76).
- Belief shift: "my managers know who deserves a promotion" -> "one person's view is a guess; everyone's view over time is evidence" (propaganda.html:38, 60).
- Positioning statement: propaganda.html:135 (same as devansh_notes.md:70).
- Price: ₹149 per employee per month, billed annually, + GST, no tiers / free plan / volume discounts, clients and vendors free (pricing.html:27-28, 41). Calculator at pricing.html:47-61, main.js:22-35.
- Pilot: ₹15,000, six weeks, three fortnightly cycles, one team, credited to first annual bill (pricing.html:67). Refund: full refund on the annual plan if first six cycles (about 12 weeks) show nothing new (pricing.html:68; trust.html:67). Renewal: terms upfront, 30-day reminder, one month credit at first renewal (pricing.html:69). First 25: two-year price lock for a case study (pricing.html:71).
- Channels: LinkedIn organic, LinkedIn Sponsored Content (titles Founder/CEO/Head of HR/People, size 51–200 and 201–500, India, IT services/software), website + walkthrough, founder/HR communities (planned phase 4), email after walkthrough (propaganda.html:94-98; ad.html:63). Retargeting of site visitors and Post 1-2 engagers (propaganda.html:106; linkedin.html:170; ad.html:63).
- Sequence: wk 1-2 Unsettle (Post 1), 3-4 Reframe (Post 2 + ad), 5-6 Prove (Post 3 + retarget), 7+ Reinforce (propaganda.html:104-107).
- Journey: Awareness -> Interest -> Consideration -> Action -> Retention -> Advocacy with metrics (propaganda.html:124-130; deliverables.html:45-50). Narrative journey for Meera on home: Trigger, Search, Evaluate, Act (index.html:85-88).
- Engagement after first interaction: "Retention is built into the product. Every fortnight, each employee gets new cards" (propaganda.html:132); guided setup, handover (how-it-works.html:93-97).
- Business context: break-even ~67 customers of 100 employees (propaganda.html:145). No fixed-cost breakdown anywhere on the site.

---
