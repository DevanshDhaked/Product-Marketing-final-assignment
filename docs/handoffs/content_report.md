---
type: Handoff
title: "Six content gaps report"
description: "Segment reason, value line, per-tactic reasons, after the first year, hub thread and a plainer hero lede, each with its source."
tags: [handoff, content]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T22:15:59Z }
---

# Six content gaps report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Worktree `Product-Marketing-final-assignment.d1-content`, branch `d1-content`.

## Plan (one line per fix: draft and source)

1. Audience (propaganda `#audience`, after the first paragraph): "These firms move consultants across engagements all year, so the partner who rates someone has often missed most of the work. We leave out IT consulting and the global firms that run their own review systems." Source: `docs/strategy/segment.md` lines 50, 57, 88, 113.
2. Value (home plan card, appended to the 150-person example line): "By our estimate, replacing one consultant who leaves costs about ₹8.6 lakh, about three years of Sphyr at that size." Source: `docs/pricing/pricing_summary.md` "Three numbers" item 1; `docs/pricing/value_model.md` line 115 (mid case ₹8,63,412 per exit, an estimate).
3. Why they fit (propaganda `#fit`, folded into the paragraph): half a line each for the name (words to take to partners), rotation (accuses no one), one line on every piece (links pieces seen weeks apart); the no-form walkthrough already has its reason (wary of vendors). Source: belief visual in `site/propaganda.html` lines 131 to 134; `docs/strategy/deliverable_map.md` lines 48, 64.
4. After the first year (home "What happens after you sign", new last row): "We review the year with your head of talent and managing partner, and with your consent compare the firm's voluntary exits with the year before. Renewal is decided on those numbers." Source: `docs/strategy/acquisition_engagement.md` lines 87, 96; `docs/pricing/validation_plan.md` line 108. No refund or price lock (decision log 2026-11-24 "Not adopted").
5. Thread (deliverables lede, second sentence): all four carry "The engagement ends. The evidence stays." and follow one buyer journey, linked to `propaganda.html#response`. Source: core line present on all four pages (grep), `docs/strategy/deliverable_map.md`.
6. Hero lede (home): the line from `docs/handoffs/message_report.md`, h1 unchanged.

Baseline: index 1727 words in `<main>`, propaganda 662, deliverables 112. copy_scan 0 unreviewed hits on all three; copy_tells 0 contrast sentences on all three.

Plan revised after review (before any edit): fix 1 now justifies the 40 and 400 edges (rotation is already in Belief); fix 4 ties renewal to the firm's own results, not to the exits check, and says nothing about renewal price.

## Progress

All six fixes applied, one commit each, then one rewording commit (copy_scan word matches) and one trim commit (word budget). Humanizer run on all six strings, and again on the trimmed ones; it removed a clipped "with no lock-in" tail from fix 4.

## New strings and sources (final text)

1. `site/propaganda.html` `#audience`, appended to the first paragraph: "Below about 40 people, partners still see everyone's work, and above about 400, firms buy large HR software. We leave out IT consulting and global firms." Source: `docs/strategy/segment.md` lines 57, 72, 80, 88 ("Above this, firms build HR functions and buy suites; the Big 4 and MBB run global systems"), 113.
2. `site/index.html` plan card, appended to the `.example` line ("A 150-person firm pays ₹22,350 a month, plus GST."): "By our estimate, one consultant leaving costs about ₹8.6 lakh, roughly three years of Sphyr at that size." Source: `docs/pricing/pricing_summary.md` "Three numbers" item 1; `docs/pricing/value_model.md` line 115 (mid case ₹8,63,412 per exit, an estimate). ₹8.63 L / ₹2.68 L a year = 3.2 years.
3. `site/propaganda.html` `#fit`, inserted between the two existing sentences: "A short name gives them words for partners, and blaming rotation accuses no one. One line on every piece links posts seen weeks apart." The fourth tactic (no form) already had its reason in the existing first sentence ("wary of vendors ... the walkthrough asks for nothing"). Source: belief visual `site/propaganda.html` lines 131 to 134; `docs/strategy/deliverable_map.md` lines 48, 64.
4. `site/index.html` "What happens after you sign", new last row. dt "After the first year", dd: "Our team goes through the year with you, including voluntary exits against the year before if you agree. You decide on renewal from your own results." Source: `docs/strategy/acquisition_engagement.md` line 87 (renewal decided on the firm's own results); `docs/pricing/validation_plan.md` line 108 (exits checked after the first year, with consent). No refund, price lock or renewal price (decision log 2026-11-24 "Not adopted").
5. `site/deliverables.html` lede, second sentence: "All four repeat “The engagement ends. The evidence stays.” and follow one buyer journey, mapped in the campaign flow." "campaign flow" links `propaganda.html#response`. Verified the line is in the work itself: `linkedin.html:117` (post media line), `ad.html:71` (standee head), `ad.html:95` (A6 card head), home h1, propaganda summary card. Dependency: `linkedin.html` and `ad.html` belong to another agent; if they drop the line, this sentence must change.
6. `site/index.html` hero lede: "Every two weeks, the people who saw a consultant's work give two minutes of feedback, and Sphyr keeps it all in one record." Source: `docs/handoffs/message_report.md`. h1 unchanged.

`docs/product/do_not_claim.md` checked: fix 2 and fix 4 touch none of its 17 items (item 4 covers prices taken from the sources, items 8 and 9 cover customers and pilot results as software results). Fix 2 is marked as our estimate and claims no Sphyr result.

## Checks

- copy_scan: 0 unreviewed hits on all three pages. The first pass flagged "reviews" (social proof pattern), "HR teams" (`\bTeams\b`) and "review systems"; reworded in 63db6f1.
- copy_tells: 0 contrast sentences on all three pages. Triad flags: index 5 (baseline 5), propaganda 5 (baseline 4), deliverables 1 (baseline 1). The new propaganda flag ("Below about 40 people, partners still see everyone's work, and above about 400, firms...") reads by eye as two clauses, not a triad (the heuristic counts commas).
- No dashes in the three pages (grep 0).
- Links: all relative links resolve; `propaganda.html#response` exists.
- Sideways scroll at 375 (Playwright on :8835): index, propaganda, deliverables all scrollWidth = clientWidth (360 + 15 scrollbar).
- Screenshots, each looked at: `design-lab/shots/site/content-hero-dark.png` (1280), `content-hero-375-dark.png` (button still on the first phone screen), `content-value-dark.png`, `content-value-light.png` (taken before the trim; the line was longer then), `content-renewal-dark.png`, `content-segment-dark.png`, `content-fit-dark.png`, `content-hub-dark.png`. Plan and pilot cards stay equal height; the pilot foot row shows more empty space under "Results stay with your firm" because the shared subgrid row grew by one line.
- Word count in `<main>`, before to after: index 1727 to 1786 (+59), propaganda 662 to 712 (+50), deliverables 112 to 132 (+20). Total +129. Fixed by the brief: +9 from the supplied hero line and 7 words of the quoted core line in fix 5.

## Final

### Files written, commit SHAs (branch d1-content)
- dd3b6fd `site/index.html` hero lede (fix 6)
- 15a0e5f `site/index.html` value line in plan card (fix 2)
- 4594e50 `site/index.html` after-first-year row (fix 4)
- 12fa02d `site/propaganda.html` audience segment line (fix 1)
- b5d3c28 `site/propaganda.html` why they fit (fix 3)
- 728dc9a `site/deliverables.html` thread line and campaign flow link (fix 5)
- 63db6f1 `site/index.html`, `site/propaganda.html` reword to clear copy_scan matches
- b0017b3 `site/index.html`, `site/propaganda.html` trim toward the word budget
- 637d675, dba8f19 `design-lab/shots/site/content-*.png` (8 screenshots)
No CSS changed.

### Key insights and findings
- Rotation as the "why consulting" reason was already on the propaganda page (Belief section), so the segment line uses the size edges instead (`segment.md` lines 72, 80, 88).
- `validation_plan.md` line 116 (price rise at renewal with 60 days' notice) and home "How we set the price" (a change applies only to firms that sign after it) can read as conflicting. The new renewal row avoids price entirely. The lead may want to reconcile the doc.
- copy_scan matches plain words ("reviews", "Teams") as claim patterns; the new lines were reworded instead of touching the allowlist, which is outside scope.

### Decisions and why
- Value line sits in the plan card after the 150-person example, so "that size" has a referent and the value sits beside the price. Marked "By our estimate".
- Renewal row ends on the firm deciding from its own results, with no lock-in clause: the humanizer flagged "with no lock-in" as a clipped negative tail, and the home page keeps its "X, not Y" count at 0.
- Renewal row says "with you" instead of naming the head of talent and managing partner, to fit the word budget.
- The no-form tactic kept its existing reason in the fit paragraph instead of a new half-line.

### Rejected approaches
- Rotation sentence for fix 1: duplicated the Belief section.
- "Renewal is decided on those numbers": tied renewal to the exits check, which the source does not say.
- Value line inside the closed "How we set the price" toggle: hidden by default.

### Open questions
- Hero first screen is now about 33 words (lede 13 to 22) against the gate 1b "about 30". The line was supplied by the brief.
- Word budget: +129 against "about 100"; 16 of those are fixed by the brief. Further cuts would drop a tactic or the exclusion line.

### Not verified
- Light theme checked by screenshot only for the pricing cards (before the trim). Other light spots not shot.
- 375 shots only for the home hero.

### Not done (out of scope)
- `docs/` addenda for these copy changes (canonical docs need the lead's approval).
- Reconciling `validation_plan.md` line 116 with the home price-change line.
