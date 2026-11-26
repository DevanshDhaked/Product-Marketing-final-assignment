---
type: Handoff
title: "Home restored to the v2 design report"
description: "Home rebuilt on the v2 design (ribbon hero with the logo sphere, circle figure, v2 cards and grid, edges 104 to 1176 as v2) with the v3 words and A-I-D-A order."
tags: [handoff, rhome]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T14:50:00Z }
---

# Home restored to the v2 design report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Teammate rhome, Depth 1, worktree `Product-Marketing-final-assignment.d1-rhome`, branch `d1-rhome` from 25c15bf. 2026-11-26.

Skills loaded before markup: `design-taste-frontend`, `stageshow`. Rules read: `docs/design/slop_rules.md`, decision log entries of 2026-11-26.

## Plan

Files: `site/index.html`, `site/css/home.css` (both rebuilt from 729e109, the v2 site). `site/css/base.css` is not touched: the v3 changes to it were additive only (ink token, report grid, exhibit, pilot-line, keynums), so every v2 class still resolves. `motif.css` and `motif.js` are linked again (unchanged since v2).

Section order (A, I, D, A), each in v2's own component:
1. Hero (A). v2 split hero: h1 left, lede right, ribbon figure full width below with "Play again". h1 "Peer feedback for appraisals at Indian consulting firms", second half in v2's green italic line ("at Indian consulting firms"), size retuned so each half stays on one line. Right column: v3 lede, "Book a 20-minute call" (primary, opens #call-note), pilot line, "See the 2-minute walkthrough" link. Ribbon labels: "Project N" / "3 colleagues", end label "Appraisal cycle" / "Every project, in one view". Animation unchanged.
2. Problem (I). v2 stacked section: h2 "What happens at calibration today", then the five v3 lines as hairline rows (v2's rows rhythm, one column because the lines have no labels). v2's trigger paragraph and before/after block are dropped: v3 has no words for them and they used "file".
3. How it works (I). v2 `.duo` (text left, feedback card right): h2 "Two minutes every two weeks", h3 + text for the project team giving feedback, h3 "The head of talent sets it up" + the Admin role line (the firm-wide tag set). Card: v3 sample (Ananya Rao, consulting tags). Then v2 `.back-intro` over each full-width frame: Insights (Member role), Team Insights (Manager role, `#partners`). Captions in v2's sample-label style, each naming the screen and its real role.
4. Who gets a say (I). v2 `.duo.flip` with the circle figure and the four group buttons (Peers, Seniors, Juniors, Clients). Text in consulting words.
5. Assurance (D). h2 "What you get and what stays private", v3's four rows in v2 `.rows`.
6. Price and pilot (D). v2 `.price-pair` subgrid cards, pilot first as the wide card, plan second on the sunk ground. Pilot: price, terms, credit line, what happens if the firm does not sign, "Book a 20-minute call" (secondary style, so the only primary buttons are hero and close). Plan: per-employee price, seat and joiner line, 150-person example, walkthrough link in the action row so both cards end on one line.
7. Call (A). v2 `.close`: the sign-off "Built from everyone on the project, not one manager's memory." as the large line (accent on the second half), then "Book a 20-minute call", pilot line, walkthrough link. Nothing after it but the footer.

Dropped from home: key-numbers row (v2 has no four-column grid; its 3-column `.proof` would need a new set of numbers, and 2 minutes, 2 weeks and 14 are already in the h2, the lede and the circle caption), v3's h2 "Talk to us before your next appraisal cycle" (v2's close is one large line and a button; a second heading would crowd it). Both are noted as decisions for the lead.

Open questions (proceeding with the defaults above): pilot as the wide card; dropping the close h2. (Superseded during the build: pilot and plan at equal width, accent on the first half of the sign-off; see Build notes.)

## Build notes

- v2 edge baseline at 1280 (http://localhost:8830/index.html), measured before any edit: every section's `.wrap` content box 104 to 1176; children 104 to 1176 except the close (104 to 798). v2 h1 58px.
- Hero: v2's "one sentence per line" h1 rule would have dropped the new headline to 45px with a large blank under it beside a five-line lede. Changed to 6cqi (64px at 1280) with `text-wrap: balance`, three lines, green italic on "at Indian consulting firms" inline; lede measure 34ch to 38ch. Left column now ends about 90px above the right column's last line, and the call button sits at y about 294 at 1280 by 800, above the fold.
- Problem rows: first try capped the text at 60ch and every line wrapped with a lone last word. Now each line is one row at desktop, `text-wrap: pretty` on phones.
- Captions: v2 capped figure captions at 70ch, so they were narrower than their frames. Now they run the frame width (checked: each caption box equals its figure's box).
- Pricing: started at `1fr 1fr` (advisor note: the pilot has too little text for v2's 2fr card). Numerals, sub lines and both hairlines align across the two cards.
- Humanizer pass on the new strings: rewrote the circle sentence (plainer) and the ribbon aria-label (three "Each..." openings in a row). Captions and ribbon labels unchanged.
- Words check: no file, record, evidence, pooled, teammate, promotion, subordinate, exhibit, em or en dash in visible text. "Member" appears only as the product role in two captions ("Member role").

## Not done (out of scope)

- Nothing outside the home page was changed. Other pages that still use "Exhibit" captions or direction A rules were not checked against this restore.
- Decision log: the 2026-11-26 "v3 plan gate" Design point (no autoplay ribbon in the first screen, exhibits, numbered sections) and the direction A addendum in `docs/design/design_system.md` now contradict the shipped home page. I did not edit canonical docs. Lead: please append a dated decision recording the user's v2-design restore for the home page.

## Final

Files and commits (branch `d1-rhome`):
- `site/index.html`, `site/css/home.css`: 0f630e0 "Home: restore the v2 design (ribbon hero, circle, cards) with v3 words and order".
- `site/css/home.css`: cfc9267 "Home: keep the Juniors label whole on phones (circle SVG overflow, inherited from v2)". At 375 v2 and this page both clipped "Juniors" (label 322 to 367, SVG ends at 359); the SVG now shows overflow into the 16px gutter, scrollWidth still 375.
- `site/css/base.css` not touched: the v3 changes to it were additive, every v2 class still resolves. `motif.css` and `motif.js` linked again.
- Assembly script (not committed): `.swarm/tmp/rhome/build.py`. Two strings were edited after it ran, so `site/index.html` is the source of truth.

Edge numbers at 1280 (the success number): all 8 section boxes 104 to 1176, the same as v2. Children: hero copy, hero figure, problem, how, say, assurance, pricing 104 to 1176; call 104 to 798 (v2 close 104 to 798). No sideways scroll at 1280 or 375 (scrollWidth 1280 and 375; no element outside the viewport at 375 except inside product frames, which clip).

Checks: copy_scan 233 strings, 0 unreviewed hits. copy_tells: 1 contrast (the approved sign-off, the page's one "X, not Y"); 2 possible triads, both real lists (the four circle groups, the team names in the footer). All local links and icon ids resolve.

Key decisions and why:
- Order hero, problem, how it works (card, Insights, Team Insights), who gets a say, assurance, price and pilot, call, as the brief lists it. v2 had the circle inside "how"; it is its own section now (`#say`).
- Key-numbers row dropped: v2 has no grid for four figures, and 2 minutes, 2 weeks and 14 already appear in the h2, the lede and the circle caption.
- v3 close h2 "Talk to us before your next appraisal cycle" dropped: v2's close is one large line and the button. The section keeps `id="call"` and an aria-label. No inbound links to `#call` found.
- Pilot first, on the plain surface with the strong border; the plan sits beside it on the sunk ground. Pilot button is "Book a 20-minute call" in secondary style, so the only primary buttons are nav, hero and close, each with the pilot line under the in-page ones. Plan action row holds the walkthrough link so both cards end on one line.
- Sign-off accent on "everyone on the project," (the positive half), not on the negation.
- Problem: v2's trigger paragraph and today/with-Sphyr block dropped; v3 has no words for them and both used "file".

Approaches rejected: v2 h1 sizing (too small, blank column); pilot as v2's 2fr wide card (half-empty card).

Open questions for the lead: (1) pilot and plan at equal width, against v2's unequal pair; (2) dropping the close h2; (3) h1 at three balanced lines, not v2's two-sentence split.

Screenshots (`.swarm/tmp/rhome/`), all looked at: v2 references v2_1280_light_full.png, v2_375_circle.png. Taken on the final markup: v3r_1280_light_full.png, v3r_1280_dark_full.png, v3r_1280_dark_hero.png, v3r_1280_how.png, v3r_1280_say.png, v3r_375_how.png, v3r_375_say.png, v3r_375_circle.png, v3r_375_pricing.png, v3r_375_call.png. Taken before the caption-width fix or the two humanizer edits, so not on the final markup: v3r_1280_hero.png, v3r_1280_ribbon.png, v3r_1280_problem.png, v3r_1280_assurance.png, v3r_1280_pricing.png, v3r_1280_call.png (none of these sections changed after the shot except caption width, which they do not have), v3r_375_light_full.png, v3r_375_hero.png, v3r_375_ribbon.png. Full-page captures show the ribbon blank because it plays when it comes into view; the viewport shots (light and dark) show it drawn. Element shots at 375 show the sticky nav over part of a section; that is the capture, not the layout.

Inherited from v2 and left as is: no "Consultant" label in the circle's core at 375 (v2 hides it too); a 61px white strip under the chips in the feedback card, measured the same on v2 (the height reserved for the "Could improve" step).

What I did not verify: dark section close-ups beyond the hero (the dark full page only); 375 dark; the circle group buttons, the card's radio states, "Play again" and the call popover by click (markup and CSS unchanged from v2 and v3); widths between 375 and 1280.
