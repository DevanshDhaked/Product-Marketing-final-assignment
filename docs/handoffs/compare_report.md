---
type: Handoff
title: "Old vs new site comparison report"
description: "Rubric-by-rubric comparison of the live old site and iteration-a: verdict mixed, losses in shown reasoning, gains in accuracy and pricing."
tags: [handoff, compare]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T21:49:31Z }
---

# Old vs new site comparison report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Date: 2026-11-25. Read only. No file edited except this report.

Sources checked:
- Old: live site at devanshdhaked.github.io. All 9 pages fetched with curl and byte-compared to `main:site/*.html`. All 9 are identical, so `main` is the live old site.
- New: `iteration-a` worktree `site/*.html`, served at 127.0.0.1:8830 (HTTP 200).
- Page text extracted with a small HTML-to-text script. Word counts: old 7,262 words over 9 pages; new 5,121 words over 6 pages.

Working notes (filled in as I go):

- Home: old segment is "growing companies" (founder plus Head of People, Meera). New segment is consulting firms (head of talent, partners, engagement managers). This is a change of segment, not only of copy.
- Home: old had a 4-card deliverables strip on the home page plus 3 direct footer links. New home has only one "Deliverables" nav link and one footer link.
- Old had 3 extra pages (how-it-works, pricing, trust). New folds them into home sections.
- Segment change is a recorded team decision (`docs/decisions/decision_log.md` line 154: consulting firms of 40 to 400, managing partner buys, head of talent champions).
- Propaganda: old is 2,316 words, 13 sections (summary, audience with non-targets, belief table, message levels, 7 tactics each with "why it fits", channels, sequence, persona table, journey with metrics and retention, positioning statement, expected response, objections, guardrails). New is 787 words, 7 sections that map 1:1 to the brief's 7 asks. New "Why they fit" is 2 sentences. New tactics are 4 one-line bullets with no per-tactic reason.
- Propaganda: old channels include LinkedIn Sponsored Content targeted by title and size, and the ad "retargets site visitors". That is the paid, tracking approach the professor criticised. New channel table has "Cost" and "Tracks anyone?" columns, all free except one standee, "A firm asking consultants to trust a fuller record cannot follow readers around the web."
- Pricing: old had a full pricing page (calculator, ₹15,000 six-week pilot, refund promise, renewal terms with 30-day reminder and one month's credit, first-25 price lock, ₹667 value claim, cost floor, Lattice comparison, flat-rate reason, one-page order form). New has a home section: ₹149, a 150-person example (₹22,350), ₹25,000 12-week pilot for up to 40 people, what the pilot measures, and a "How we set the price" block (pilot covers about 30 hours plus 12 weeks running cost, PerformYard about ₹464, break-even about 49 firms of 150, why six cycles, price survey decides changes).
- Grep: "refund", "renew", "attrition", "Galton", "collu", "minimum" appear in old pages and in no new page.
- LinkedIn: old posts each carry Purpose, Audience, Angle on the message, CTA, "Why it works on LinkedIn" (and Post 3 a pricing-consistency check). New posts carry Job, Journey stage, CTA, plus a short "How the three work together". Old hooks are concrete (Priya story; Galton's 787 guesses). New Post 3 "proof built in the open" (what every pilot measures) answers the professor's no-reviews question; old Post 3 is a price offer.
- Accuracy: old Post 3 and old trust page say "no manager and no HR person ever sees who wrote what". New home FAQ says managers who approve edit requests "can see who asked to edit feedback about whom". New is more careful.
- Ad: old is a LinkedIn Sponsored single image, headline "Promote on merit, not politics.", 9-field rationale (medium, audience targeting, message, benefit, visual, CTA, pricing consistency, journey stage, A/B test and metrics). Audience field includes "Retargeting: site visitors". New is a roll-up standee plus A6 handout, 4-field rationale (medium, audience, journey stage, why it tracks nobody). New lacks benefit, visual, pricing-consistency and measure fields. New medium line: "We pay for the spot because the course treats advertising as the route where money is spent" reads as course meta, not customer reasoning.
- Deliverables page: old had "The thread through all four" (segment, central message, offer) and a journey table (Awareness to Retention) that links every artefact. New has 4 cards with one line each. The thread and journey table are gone; the new journey timeline lives only on the propaganda page (Week 1 to 12 weeks).
- Walkthrough: same 4-step shape in both. New uses the real prototype screen layout (Member Insights, VBA tags) and consulting names; old used an invented 1 to 5 rating card and a 7-parameter table.
- No page on the new site says why consulting firms were chosen or who is not targeted. Old propaganda section 2 had "Who we are not targeting, and why" (under 50 people, large enterprises, buyers who want monitoring, buyers who want to replace the HRMS).
- Screenshots (worktree `.playwright-mcp/`, git-ignored): `compare-old-home-fold.png`, `compare-new-home-fold.png`, `compare-new-ad-fold.png`. Old fold shows audience label ("For growing companies"), promise, price button and the start of the deliverables strip. New fold shows promise, one line of value, one CTA and the ribbon illustration; the audience is named in the copy ("about your consultants", "engagement team") but there is no audience label, no price, and no deliverables except the nav link.
- New internal links: all 6 pages return 200 from 127.0.0.1:8830; anchors #how, #partners, #pricing, #p1-h, #p2-h exist.


## 1. Rubric lines, old vs new

| Rubric line (marks) | Stronger | Evidence |
|---|---|---|
| Customer understanding and strategic alignment (20) | Old, narrowly | Old propaganda names decision maker, champion and amplifiers with "what they need from us", says who is not targeted and why, and has a persona table "What we know about Meera / What we did". New propaganda gives 3 roles with one quoted belief each ("Kavya, 150-person firm", "Vikram", "Meera, senior consultant") and no reason for choosing consulting. New home copy is more specific to the segment's daily pain ("two short project-end forms and a client email someone forwarded"; "One engagement manager has left the firm"). Depth of reasoning goes to old; fit of copy to one segment goes to new. |
| Positioning and central message (15) | Mixed, old on the guideline, new on consistency | Old has a message hierarchy table (promise, core line, proof points, reasons to believe, where each is used, a fallback line). That is the "guideline, not slogan" the professor asked for. New has one line, "The engagement ends. The evidence stays.", used on home, posts 2, ad, propaganda; the "Central message" section is 3 sentences. New adds a vision line at the close: "Careers should be earned in front of the people who saw the work." Old positioning statement is written out in full; new restates it in one sentence. |
| Website and customer journey (15) | Old on journey and deliverable access; new on page focus | Old home has a 4-card deliverables strip plus footer links to each deliverable; old deliverables page has a journey table linking every artefact from Awareness to Retention. New home reaches deliverables only through one nav item; new deliverables page has 4 one-line cards. New home order (problem, how it works, card, partner and consultant views, research, what Sphyr does not do, privacy FAQ, price, after you sign) is logical and complete on one page. Old split it across 5 pages with a Meera Trigger/Search/Evaluate/Act story. |
| Propaganda strategy (15) | Old on reasoning depth; new on channel ethics | Brief: "A list of slogans ... without a clear objective and rationale is not sufficient." Old gives a "why it fits this audience" for each of 7 tactics, plus objections and guardrails. New lists 4 tactics as bare lines and "Why they fit" is 2 sentences. New channel table answers the professor's no-money, no-stalking point directly; old relies on paid LinkedIn targeting and retargeting. |
| Three LinkedIn posts (15) | Roughly even, old on rationale, new on purpose fit | Old posts: strong hooks (Priya, Galton's 787 guesses), each with purpose, audience, angle, CTA and "why it works on LinkedIn". New posts: Job, Journey stage, CTA per post; Post 3 "proof built in the open" is a better answer to the no-reviews problem than old Post 3's price pitch. New lacks the per-post audience and platform reasoning. |
| Advertisement (10) | Old | Old headline "Promote on merit, not politics." reads in 2 seconds; rationale covers 9 fields including benefit, visual reasoning, pricing consistency and an A/B test with metrics. New standee is ethical and consistent, but its rationale has 4 fields, with no benefit field (the standee copy does state one: "so partners calibrate with the whole year in front of them"), no measure, and one line of course meta ("the course treats advertising as the route where money is spent"). Old's retargeting line is a weakness the professor would likely mark. |
| Pricing, packaging, acquisition, engagement (10) | New on pricing and packaging; old on retention | New answers most pricing feedback: pilot amount (covers about 30 hours plus 12 weeks running cost), why 12 weeks (six cycles), non-conversion (firm keeps data as CSV), named competitor plan (PerformYard about ₹464), break-even (about 49 firms of 150), price survey decides changes. New "What happens after you sign" builds anticipation (empty partner screen that fills from the start date; "While you fill in theirs, they are filling in yours"). Old has renewal terms, 30-day reminder, first-renewal credit, first-25 case-study trade, retention metrics; new has none of these after-sale relationship items beyond the fortnight loop. |

## 2. Professor feedback points

| Point | Better | Why |
|---|---|---|
| Pricing: show the ₹667 value assumptions; why capture only ₹149 | Neither fully. Old states ₹667 without proof; new drops value per employee entirely | New avoids the weak number but now never shows customer value in rupees. |
| Pricing: compare like products, name plans | New | PerformYard plan price for firms of a few hundred; old used Lattice Performance $10 with a date but no feature basis. |
| Pricing: ₹150 vs ₹149, margin | Old mentions it, new omits it | Old "₹149 sits on that floor" (not a reason). New silent. |
| Pricing: fixed cost breakdown, break-even | Neither shows the breakdown | New gives about 49 firms, old about 67 customers of 100. |
| Pricing: pilot amount, length, non-conversion | New | Old ₹15,000 six weeks with no derivation. |
| Pricing: Van Westendorp use | New, slightly | "A price survey ... will decide whether ₹149 changes"; old absent on site. |
| Packaging: excitement, not only reassurance | New | Old leans on refund, trust page, "Low risk". New "What happens after you sign" and the consultant "Personal insights" view give something to look forward to. |
| Packaging: first-use reward | New | Consultant sees how work is landing; old card ends on "Nobody ... will ever see that it came from you". |
| Packaging: acquisition material does not belong in packaging | Not applicable to this assignment | Both mix them; fine for a final marketing site. |
| Journey: "can we do anything about it" | Not visible on either site | Neither site shows touchpoints framed as actions. |
| Journey: social proof when there are no reviews | New, slightly | New Post 3 and "What a pilot measures" publish the test in advance. Old offers a first-25 case-study trade. Both valid; new is more concrete. |
| Journey: personal, not distant | Old, slightly | Old Meera story on home and Priya in post 1 and walkthrough. New home uses a second-person scenario, which is personal, but the persona appears only on the propaganda page. |
| Message is a slogan, not a guideline | Old | Old message hierarchy table with where-used and fallback. New has one line and 3 sentences. |
| No money, not creepy channels | New, clearly | New "Tracks anyone? No" column and untracked QR link. Old uses paid targeting and retargeting. |
| Positioning too present-focused, needs vision | New, slightly | New closing line is a vision. Old "Promote on merit, not politics" is a promise, still present. |

## 3. What the old site had that the new one lost or weakened

1. Deliverable access from the home page. Old: 4 cards near the top plus 3 footer links. New: one nav word and one footer link. The brief says the evaluator "should be able to find and open every deliverable without having to search for it". The new site passes, but less obviously.
2. The connective tissue page. Old deliverables page stated segment, central message and offer, and mapped every artefact to a journey stage through Retention. New deliverables page dropped this. Section 8 of the brief ("one connected marketing effort") is graded on exactly this.
3. Propaganda reasoning depth. Lost: per-tactic "why it fits", who is not targeted, belief/attitude/response table, objections, guardrails, a written positioning statement, journey stages with metrics. Kept in short form: audience, belief, message, channels, response.
4. Message guideline. Old's promise / core line / proof points / reasons to believe table is gone. This was the professor's explicit complaint, and the old site had partly fixed it.
5. Retention and relationship after the sale, weakened, not gone. Renewal terms, 30-day reminder, first-renewal credit, case-study trade and the advocacy stage are gone. The refund and the early-customer price lock were dropped on purpose (`docs/decisions/decision_log.md` line 100, "Not adopted (scope)"); the renewal reminder is not addressed in the log. The new site still has "What happens after you sign", "Every two weeks after that" and the missed-cycle FAQ, which cover engagement through the product loop. What is missing is any statement of how the firm-to-Sphyr relationship continues after the pilot. Rubric line 7 asks for "how the customer relationship will be maintained and developed".
6. Ad rationale. Lost benefit, visual reasoning, pricing-consistency note and test-and-measure plan.
7. LinkedIn per-post reasoning. Lost audience, angle and "why it works on LinkedIn".
8. Segment rationale. Nothing on the new site explains why consulting firms. A grader who compares with the team's earlier coursework (growing companies) may read the change as unexplained.
9. Stated customer value. Old said ₹667 per employee (weakly supported). New gives no rupee value at all; the brief asks to "make the value offered understandable".
10. Clarity at first glance. Old fold says who it is for, the promise, and the price. New fold says the promise and one line, with no audience word for a non-consulting reader and no price.
11. Proof points removed: Galton, 0% collusion, minimum-reviewer rule, delayed notes. Not a real loss. `docs/product/do_not_claim.md` line 30 lists minimum response thresholds and "even admins cannot see" as claims the prototype contradicts (managers see who gave feedback to whom in edit approvals), and 0% collusion is a self-reported 2018 paper figure. These were rubric risks on the old site under "Do not invent features". The cost is that new Post 2 and home rest on one study plus Gallup.

## 4. Where the new site is clearly stronger

1. Channel ethics and budget: free channels, one paid standee, no tracking. Direct answer to the professor.
2. Pricing reasoning: pilot amount, length, non-conversion, named competitor plan, break-even, survey use.
3. Packaging excitement and first-use reward ("What happens after you sign", consultant insights view).
4. Accuracy to the prototype: real screen layouts, careful privacy wording (managers see edit requests), "What Sphyr does not do". Fewer claims that could be marked as invented features.
5. One segment, one vocabulary: engagement, calibrate, partner, head of talent appear consistently on all 6 pages and the ad.
6. Propaganda now mirrors the brief's 7 asks in order, which makes it easy to grade.
7. Social proof built in the open (Post 3, "What a pilot measures").
8. A vision line for positioning.

Addendum to section 1, website row: the old walkthrough ends on "Start a ₹15,000 six-week pilot" (order form), "See pricing" and "How anonymity works". The new walkthrough ends on "The engagement ends. The evidence stays.", "Book a 20-minute call" and "Back to home". The new end has a clear next step but no link to the price section, so a reader who wants the cost goes back home.

Addendum to section 4: 9. The old site made anonymity claims the prototype contradicts ("Nobody, not her manager and not HR, will ever see that it came from you"; "Nothing shows until enough reviewers have answered"). `docs/product/do_not_claim.md` line 30 lists these. A grader who opens the prototype could mark them as invented features. The new site removed them.

## 5. Verdict

Tally by rubric marks (my judgement, not a score):

| Line | Marks | Lean |
|---|---|---|
| Customer understanding | 20 | Old (depth of reasoning, non-targets, persona table) |
| Positioning and message | 15 | Mixed (old guideline table; new single line used everywhere, vision line) |
| Website and journey | 15 | Old, slightly (home deliverable links, journey table); new is more accurate and focused |
| Propaganda | 15 | Old on reasoning; new on the channel point the professor raised. Lean old |
| LinkedIn | 15 | Even |
| Advertisement | 10 | Old on rationale; new on ethics. Lean old, slightly |
| Pricing, packaging, acquisition, engagement | 10 | New (pricing and packaging answers), with a retention gap |

Verdict: mixed, with a real downgrade in reasoning shown on the page. The new site is more accurate, answers more of the professor's points, and is one consistent segment. But it cut the written reasoning that the brief grades ("the reasoning behind the choices", "a list ... without a clear objective and rationale is not sufficient") and the cross-artefact thread. Lines worth about 60 of 100 lean old today. The gaps are fixable with content already on the new site or in the decision log.

Top 3 fixes, smallest first, all inside the brief and using only existing content:

1. Home page: add direct links to the propaganda strategy, the three LinkedIn posts and the advertisement (for example in the footer, plus one short line near the top or the end). Restores obvious deliverable access.
2. `deliverables.html`: add "The thread through all four" (segment, central message, offer: ₹149, ₹25,000 12-week pilot) and a short stage-to-artefact table (naming the problem: Post 1 and standee; looking for answers: Post 2, walkthrough, home; seeking validation: Post 3, pilot measures; action: 20-minute call and pilot; after signing: "What happens after you sign" and the fortnight loop). All of it already exists on the propaganda and home pages.
3. `propaganda.html`: add one "why it fits" line per tactic; a short message guideline (promise, core line, proof points, where each is used); and one or two lines on why consulting firms and who is not targeted, taken from `docs/decisions/decision_log.md` line 154.

## Out of scope

- Screenshot location: the brief asked for the main repo root `.playwright-mcp/`. Playwright refused that path, so the 3 screenshots are in the iteration-a worktree `.playwright-mcp/` (git-ignored). Nothing was committed.

## Final

- Verdict: mixed. Not a clean upgrade. The new site is more accurate and answers the professor's channel, pricing and packaging points, but it shows less reasoning and less connection between artefacts. On rubric weight, lines worth about 60 marks lean to the old site as things stand.
- Main losses: home-page deliverable links; the deliverables page thread and journey table; propaganda reasoning depth (per-tactic rationale, non-targets, objections, guardrails, written positioning statement); the message guideline table; the ad's benefit, visual and measurement rationale; LinkedIn per-post audience and platform reasoning; any stated customer value in rupees; a reason for choosing consulting; post-pilot relationship content (refund and price lock were dropped on purpose, line 100 of the decision log).
- Main gains: free, no-tracking channels; pricing reasoning (pilot amount, length, non-conversion, named competitor plan, break-even, survey use); packaging anticipation and first-use reward; claims that match the prototype; one consistent consulting vocabulary; propaganda sections that mirror the brief; social proof built in the open; a vision line.
- Top 3 fixes: (1) home links to all three other deliverables; (2) thread and stage-to-artefact table on `deliverables.html`; (3) per-tactic reasons, message guideline and segment reason on `propaganda.html`.
- Did not check: mobile layouts; dark mode; the old LinkedIn text chunk `.ac` (end of old Post 3 notes); full-page screenshots of either site (only 3 fold screenshots); the old ad image itself; whether the team's earlier graded coursework used the consulting segment (if it did not, the segment change is a larger risk than I scored); external links (Scullen source URL) and the 20-minute call dialog behaviour.
