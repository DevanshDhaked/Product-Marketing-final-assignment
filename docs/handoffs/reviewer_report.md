---
type: Handoff
title: "Final review report, phase 3"
description: "Read-only review of the six pages against the brief, rubric, the 15 feedback points and the copy rules: findings, checks passed and rubric estimates."
tags: [handoff, reviewer]
generated: { by: claude-code/opus-5-5, at: 2026-11-25T05:30:00Z }
---

# Final review report, phase 3

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Status: done.

## Plan
Read-only review of `site/` on `iteration-a` (worktree `.claude/worktrees/iteration-a`, served at http://127.0.0.1:8830/). No repo edits, no worktree, no server.

1. Read the brief docs: assignment_brief, professor_feedback, feedback_gap_map, decision_log, message_guideline, do_not_claim, pricing_summary, packaging_summary.
2. Read every page source (index, demo, deliverables, propaganda, linkedin, ad). Map each of the 15 professor points to page and exact text. Score answered / partly / not.
3. Consistency grep across six pages: central message, ₹149, ₹25,000, 12 weeks, 40 people, credit, data return, segment 40 to 400, CTA wording, deliverable numbering, QR URL.
4. Run `design-lab/copy_scan.py` and `design-lab/copy_tells.py` on each page. Read copy for rule breaks (month names, customers, anonymity, invented features, AI, pronouns, persona names outside propaganda, X not Y count, triads, dashes, emojis).
5. Technical via private headless Chrome (playwright-core from npx cache): link and anchor check, nav and phone menu, Escape and focus, both themes, 375 and 390 px overflow, smallest font size, walkthrough and FAQ keyboard, reduced motion, console errors, external requests, logo colour in nav and footer.
6. Write findings ranked worst first, must-fix vs nice-to-have, then `## Final`.

Findings are appended below in parts as they land.

## Progress part 1 (copy read, scans run; browser checks next)

Interim findings from reading all six pages and running `copy_scan.py` and `copy_tells.py` on each (n = 6 pages):
- Propaganda misquotes the 2018 pilot as per card. Source (`docs/product/evidence_and_claims.md:39`): "The average time to fill up the feedback cards (for an average sphere size of 14 members) was a little over two minutes (02:09 mins)". Propaganda section 3 says "a card took a little over two minutes (02:09)" and section 9 says "A card takes about two minutes ... it took 02:09 for a circle of 14". Index and posts say the whole set of cards. Must fix.
- Ad timing conflict: propaganda section 8 puts the standee in "Weeks 3 to 4" with post 2. `ad.html` (Journey stage) and `linkedin.html` (How the three work together) say it runs with the first post (week 1). Must fix one side.
- Pricing feedback is mostly not on the site. Only the pilot derivation and a cost-floor/value line are there, and both are inside a closed `<details>` "How we set the price". Competitor comparison, break-even and Van Westendorp are absent.
- Copy scan hits on demo, propaganda and ad read as false positives (sentences that state what Sphyr does not do), except demo faux UI line "Your comments and review are always anonymized." which overstates privacy. Detail in the final list.

## Result

**Success number: 6 of 15 professor feedback points fully answered on the site, 6 partly, 3 not (12 of 15 at least partly).**
**Must-fix findings: 4** (plus 1 decision the lead must take on pricing).

Method: read all six pages as rendered text, ran `copy_scan.py` and `copy_tells.py` on each page (n = 6), grepped for months, dashes, emojis, persona names and pronouns, and ran three headless Chrome scripts (playwright-core 1.66 alpha with system Chrome) against http://127.0.0.1:8830/.

## The 15 feedback points

| # | Point | Status | Where and exact text |
|---|---|---|---|
| P1 | Value calc (₹500 per employee from one resignation) | Partly | index, closed `<details>` "How we set the price": "losing a consultant costs a firm about ₹8.6 lakh in recruiter fees and the months before a replacement is up to speed. Sphyr for 150 people costs ₹2.68 lakh a year, so keeping one consultant pays for about three years of it." No breakdown of ₹8.6 lakh on the site. |
| P2 | Competitor comparison on named plans | Not | Nothing on any page. |
| P3 | ₹150 floor vs ₹149, why capture only part of value | Partly | Same details: "The ₹149 rate sits above what it costs us to serve each person, and below the value we estimate for a firm even in our most cautious case." Says where it sits, not why there. |
| P4 | Break-even: fixed cost breakdown, full variable cost | Not | Nothing on any page. |
| P5 | Pilot: how the amount was set, why the length, what if no conversion | Partly (2 of 3) | Amount: "The pilot fee covers what a pilot costs us to run: roughly 30 hours ... about ₹9,500 less than that cost". No conversion: "you get your data as a spreadsheet (CSV) and we delete the rest. The fee isn't refunded." Why 12 weeks: not stated anywhere. |
| P6 | Van Westendorp: how results set the price | Not | Nothing on any page. |
| K1 | Packaging creates excitement, anticipation before first use | Answered | index "What happens after you sign": "We show your partners a sample record built from people on four engagements, then the same screen for their own practice, still empty. It starts filling from the date you picked". |
| K2 | Packaging strayed into acquisition | Answered | Packaging on index starts at "after you sign"; acquisition lives in propaganda sections 4, 7, 8. |
| K3 | First-use reward | Partly | index: "The first cycle ... While you fill in theirs, they are filling in yours." The payoff comes only "After a few cycles: Consultants start to see what their colleagues noticed". Nothing the user gets from the first card itself. |
| J1 | "Can we do anything about it?" instead of "Relevant" | Partly | propaganda "How Kavya shaped each choice", columns "What we know about Kavya / What we did about it". This is the actionability idea, but there is no journey map that a grader would recognise as the fix. |
| J2 | Social proof when there are no reviews | Answered | index "What every pilot measures" and 02:09 pilot; linkedin Post 3 (job: "Seeking validation"); propaganda objection "Who else has tried this?". |
| J3 | Journey not personal | Answered | index scene: "A partner asks you for the file on a senior consultant ... this is all you have to send."; propaganda Kavya story; demo puts the reader in the partner seat. |
| M1 | Message is a slogan, not a guideline | Partly | propaganda section 6: "Every piece follows the same order: the moment the engagement ends, the two-minute mechanism, what partners see, the vision, then one next step." The full guideline (`docs/strategy/message_guideline.md`, never-say list, proof per claim, visual rules) is not on the site. |
| M2 | No money, no creepy marketing: channel list | Answered | propaganda section 4: "All of them are free except the one advertisement ... people choose to hear from us, and we track nobody." plus "What we never do" and section 5. |
| V1 | Positioning too present-focused, needs vision | Answered | propaganda section 6 Vision line; index closing line "Careers should be earned in front of the people who saw the work." |

## Must fix before submission (worst first)

1. **Pilot statistic misquoted as per card.** propaganda section 3 "The method takes about two minutes": "a card took a little over two minutes (02:09) for an average circle of 14 people"; section 9 objection: "A card takes about two minutes, every two weeks, for the people in their circle." Source (`docs/product/evidence_and_claims.md:39`): "The average time to fill up the feedback cards (for an average sphere size of 14 members) was a little over two minutes". Index and posts 2 and 3 say the whole set. Breaks the claims rule (message guideline section 3) and cross-page consistency. Fix: "the cards for an average circle of 14 people took a little over two minutes (02:09)" and "The whole set of cards takes about two minutes, every two weeks."
2. **Ad timing contradicts itself.** propaganda section 8 "Show how it works, Weeks 3 to 4: The second post goes out, and the standee goes up". ad.html Journey stage: "It runs in the same weeks as the first LinkedIn post." linkedin.html: "The standee ad runs at an HR event in the same weeks as the first post". Breaks the checklist line "deliverables consistent with one another". Fix: pick one. The ad's stated stage is "the trigger", which matches week 1, so move the standee sentence in propaganda to "Name the problem, Weeks 1 to 2".
3. **Pronoun instead of role.** propaganda "How Kavya shaped each choice": "Kavya gets one new budget line a year, and her name is on it." Breaks "roles over pronouns" (everywhere else the page uses "they"/the role). Fix: "and Kavya's name is on it."
4. **Faux UI overstates privacy.** demo step 2 card: "Your comments and review are always anonymized." The site itself says managers who approve edit requests can see who gave feedback to whom. Breaks the anonymity rule (do_not_claim item 6). Fix: "Your comment is shown to the person without your name." (If this is verbatim prototype copy, keep the meaning honest anyway; the page is ours.)

## Decision for the lead (pricing feedback vs scope decision)
The 2026-11-24 decision log keeps the pricing reasoning internal. That costs 4 of the 15 points (P2, P4, P6 not answered; P5 partly). The data already exists in `docs/pricing/pricing_summary.md`. Cheapest fix, inside the existing "How we set the price" details on index, four plain sentences:
- Competitors: "₹149 is about a third of the lowest list price we found for a dedicated review tool (PerformYard, $5 a seat, about ₹464) and about a fifth of Peoplebox's and Confirm's starting price (about ₹743)." Recheck prices first; summary says read 24 November 2026.
- Break-even: "At this rate we need about 49 firms of 150 people to cover our fixed costs."
- Pilot length: "Six fortnightly cycles is the fewest that give partners a usable pattern; three were too few."
- Test: one sentence on what a Van Westendorp result would change.
Also consider opening this `<details>` by default or giving it a visible heading: a grader skimming may never click it. Needs the user's approval because it reverses a logged decision.

## Nice to have
1. index pricing card label "Getting started" never says "pilot", while every other page calls it a pilot. Fix: "12-week pilot".
2. index faux UI team feedback: "protected quality through a difficult release" and "another team owns the handoff" read as software team language. Swap for consulting text, as demo already does ("rebuilt the cost model after the scope change").
3. K3 first-use reward: add one line on what a consultant sees after the first cycle, once the timing is confirmed against the prototype (packaging summary flags it as unverified).
4. demo step 3: Nikhil's "Responses received" goes 74 to 75 after your card, but "From 13 collaborators" stays 13 while the intro says 13 of 14. Either count the reader as the 14th or leave it; small.
5. ad standee: the headline sits tight under the logo with no gap (see screenshot `ad-full.png`).
6. Post 1 says the file is "the consultant's self-appraisal and one form", index scene says "two short project-end forms and a client email". Not wrong, slightly different pictures of the same file.
7. Smallest rendered text is 11px (faux UI tag headers "Values", ad URL under the QR). Acceptable inside product frames; the ad URL at 11px is hard to read on the page.

## What passed (verified)
- Links: every internal link and anchor resolves on all 6 pages; 4 external source links on propaganda only. No console errors, no failed requests, no 4xx, no external requests on load (n = 6 pages).
- Phone: scrollWidth equals viewport at 375 and 390 on all 6 pages. Menu opens, Escape closes it, aria-expanded flips, focus returns to the Menu button.
- Themes: toggle sets `data-theme=dark` and `aria-pressed=true` on all pages. Logo uses full-colour `class="mark"` in nav and footer on all pages; checked visually on index light and dark.
- Motion: with reduced motion, 0 animations; without it, 0 running animations after the hero settles (12 s).
- Walkthrough: fully keyboard operable (Space on radio unlocks step 2, tags, Submit, steps 3 and 4 open, focus moves to the "Submitted" state). Call popover opens and closes with Escape.
- QR decodes (Chrome BarcodeDetector) to `https://devanshdhaked.github.io/Product-Marketing-final-assignment/demo.html`, the same as the printed address and the posts' first comment.
- Copy: no month names, no dashes, no emojis on any page. Persona names only on propaganda (8 lines, audience section). Contrast sentences: demo 1, propaganda 1, others 0. Triad flags were name lists or four-item lists, not rhythm. Copy scan hits on propaganda and ad are sentences about what Sphyr does not do.
- Price, pilot terms, segment, CTA wording and deliverable numbering (website 1, propaganda 2, posts 3, ad 4) match across pages.

## Rubric read (estimates, mine, not a grader's)
Customer understanding 20: about 16 (segment, exclusions and persona table are strong; persona shaping is visible). Positioning and message 15: about 13. Website and journey 15: about 11 (no explicit journey view; journey lives in propaganda and the after-sign steps). Propaganda 15: about 13. Posts 15: about 12 (three clear jobs and stages). Ad 10: about 8. Pricing, packaging, acquisition, engagement 10: about 7 (pricing shown clearly, reasoning thin; relationship after the pilot is one line). These are guesses.

## Final
**Files written:** only this report, `Product-Marketing-final-assignment.swarm/reports/reviewer.md`. No repo changes, no commits (read-only brief). Scratch files (text extracts, scripts, screenshots) in `/private/tmp/claude-501/-Users-borah-resources-IIITH-PDM-sem-3-pm-Product-Marketing-final-assignment/86511671-9824-48f7-8ea7-aa5ef15d50e4/scratchpad/`.

**Key insights:** 6 of 15 feedback points fully answered, 12 of 15 at least partly. The three pricing points not answered were left out by a logged team decision, and the data to answer them already exists in `docs/pricing/pricing_summary.md`. Four copy defects must be fixed: the 02:09 per-card misquote, the ad timing conflict, one pronoun, one privacy overstatement in the demo UI. The technical build is clean on every check run.

**Decisions I made:** counted a point "answered" only when the site text addresses every part of the professor's question; counted the Kavya action table as only a partial answer to J1 because no journey map exists on the site.

**Approaches rejected:** did not use the shared Playwright MCP browser (used a private headless Chrome instead, as the brief allows); did not open external source links.

**Open questions:** (1) Will the team add the four pricing sentences, which reverses the 2026-11-24 scope decision? (2) Is "Your comments and review are always anonymized." verbatim prototype copy? (3) Which ad timing is intended, week 1 or weeks 3 to 4?

**Not verified:** the live gh-pages deploy content (the QR target returns HTTP 200, but I did not confirm it serves the iteration-a walkthrough; it must be redeployed before submission); the professor's source PDFs (checked quotes against repo digests only); dark-theme screenshots for pages other than index (checked by computed background and toggle state); contrast ratios; screen reader output.
