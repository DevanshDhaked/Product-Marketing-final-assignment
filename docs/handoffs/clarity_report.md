---
type: Handoff
title: "Home clarity fixes report"
description: "Readable hero payoff label, a line on where sample scores come from, and plain words on the home sample screens."
tags: [handoff, clarity]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T21:59:07Z }
---

# Home clarity fixes report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Worktree `Product-Marketing-final-assignment.d1-clarity`, branch `d1-clarity`. Scope: three approved fixes on `site/index.html` and the CSS they need.

## Diagnosis (written before edits)

### Fix 1: hero payoff label
Measured at 1280 after the animation settled (7.6 s), served page on 8834:
- `.round-label` "Promotion round": 14px, 700, fill `--text`.
- `.round-sub` "The whole year is in the file": 13px, weight 400, fill `--text-muted`.
- Other text in the picture: `.eng-name` 15px 700, `.eng-sub` 13px 500 (both `--text-muted` at rest).
Root cause: the payoff line is the only text in the picture at weight 400, it is the smallest size, and it sits in the muted colour, so it reads as the faintest text in the picture. The label above it is also 1px smaller than the project names. The layman capture also caught the round mid fade-in (it fades in at 6.4 to 7.0 s), which made it look lighter still; the animation is not changed.
The rules live in `site/css/motif.css`, a shared file owned by site-css. Plan: override in `site/css/home.css`, scoped to `.hero-visual`, so the shared file stays untouched. Label to 15px (same as the project names); payoff line to 14px, weight 500, fill `--text` in both themes. No change to timing or keyframes.

### Fix 2: "No AI writes or scores anything" vs scores 78 and 82
The denial says nothing scores, then two sample screens show scores with no source. Sources:
- `docs/product/product_facts.md:71`: "Input scale is not numeric: 3-way experience (... PROTO: Was good / Could improve / No interaction) plus factor tags."
- `docs/product/product_facts.md:72`: "Output: normalized scores. PROTO and DOC p7 screenshot show scores out of 100 (e.g. "93 out of 100"), chart axes 50 to 100."
- `docs/product/product_facts.md:73`: "No source states the formula that converts taps to a 0-100 score. Do not describe the algorithm."
- `docs/product/do_not_claim.md:26`: AI is not a current feature.
Plan: adjust the denial in "What Sphyr does not do" so it stays true: no AI writes anything, and the scores out of 100 on the sample screens are worked out from the card answers. No formula, no weighting.

### Fix 3: jargon on the card and sample screens
Plan, words only, structure unchanged:
- Card: "Engagement team VBAs" (two chips) to "Engagement team values". "Choose the clearest signals." to plain wording. "normalized and grouped" in the private note to plain wording.
- Consultant screen: sub line drops "normalized" and explains "cycle" as every two weeks once; "Mixed signals this cycle" to "Up 3 points this cycle" (matches the manager screen's "Up 2 points this cycle"); "Strongest signal" to "Strongest area"; "Composite score across all seven dimensions" to a plain line. Aria-label updated to match.
- Manager screen: "Positive" to "Was good" so the rating words match the card. Aria-label updated.
- Chart axis "Cycle 1..6" stays (explained by the sub line).

### Change to the Fix 2 plan (before editing)
`design-lab/copy_scan.py:38` allowlists the whole "What Sphyr does not do" paragraph verbatim. Rewording the denial would create an unreviewed hit in a file outside my scope. So the denial stays as is, and the true line goes in the figcaption under the first sample screen that shows a score.

## Progress

All three fixes done, one commit each. No change to layout, sections, animation, row heights or favicons.

### Changed strings (old, then new)

Fix 1, `site/css/home.css` (new block after `.hero-visual .cv-compact`; `motif.css` untouched):
- `.round-label` "Promotion round": 14px, 700, `--text`. New: 15px in both compositions, so it matches the project names.
- `.round-sub` "The whole year is in the file": 13px wide / 15px phone, weight 400, `--text-muted`. New: 14px wide / 15px phone (kept), weight 500, `--text` in both themes.

Fix 2, `site/index.html`, figcaption under the consultant screen:
- Old: "Prototype screen. Sample data, fictional people."
- New: "Prototype screen. Sample data, fictional people. Scores are out of 100 and come from colleagues' answers on the cards."
- Source lines: `docs/product/product_facts.md:71` "Input scale is not numeric: 3-way experience (... PROTO: Was good / Could improve / No interaction) plus factor tags."; `:72` "Output: normalized scores. PROTO and DOC p7 screenshot show scores out of 100"; `:73` "No source states the formula that converts taps to a 0-100 score. Do not describe the algorithm." The line names input and output only, no method.

Fix 3, `site/index.html`:
- Card chip, twice: "Engagement team VBAs" to "Engagement team values".
- Card, "Could improve" step: "Choose the clearest signals. Your name is not shown with your response." to "Pick the ones that fit best. Your name is not shown with your response."
- Card private note: "Individual responses are normalized and grouped before anyone sees them." to "Each answer is grouped with the others before anyone sees it." (Same claim as the safe line in `do_not_claim.md:30`, no stronger.)
- Consultant screen sub: "A normalized, anonymized view built from your last six feedback cycles." to "What colleagues said over your last six cycles, one every two weeks, with names removed."
- Consultant KPI: "Mixed signals this cycle" to "Up 3 points this cycle" (matches the manager screen's "Up 2 points this cycle").
- Consultant KPI label: "Strongest signal" to "Strongest area".
- Consultant chart: "Composite score across all seven dimensions" to "Your overall score, cycle by cycle".
- Consultant aria-label: "strongest signal Quality of Work" to "strongest area Quality of Work".
- Manager screen: "Positive" to "Was good" (now the same rating words as the card).
- Manager aria-label: "68 percent positive" to "68 percent was good".

### Checks
- copy_scan `site/index.html`: 284 strings, 0 unreviewed hits, 5 reviewed denials.
- copy_tells: 0 contrast sentences, 5 possible triads. All 5 were there before this work (Scullen/Mount/Goff, the denial paragraph, the FAQ pooling answer, the plan list, the team names). None come from new strings.
- Humanize: the new strings (one Fix 2 line, seven distinct Fix 3 strings) were checked by hand against the humanizer patterns; copy_tells shows 0 contrast sentences and no new triads.
- Links: every relative href/src in index.html resolves.
- Sideways scroll at 375: scrollWidth equals clientWidth (360/360) in both themes. 1280: 1265/1265.
- Screenshots, checked by eye, in `design-lab/shots/site/`: `clarity-hero-{light,dark}-{1280,375}.png` (taken 7.8 s after load, animation settled), `clarity-card-good-*`, `clarity-card-improve-*` (Could improve tile clicked), `clarity-consultant-*`, `clarity-manager-*`, each in light and dark at 1280 and 375. At 375, "Up 3 points this cycle" and the new sub line and chart line wrap cleanly; the "Strongest area" tile is hidden in the compact stage, so it does not render there.

## Not done (out of scope)
- Same jargon on other pages (not fixed):
  - `site/demo.html:124`, `:133` "Engagement team VBAs"; `:132` "Choose the clearest signals."; `:157` "Individual responses are normalized and grouped before anyone sees them."; `:180` "Review individual performance signals, comparisons, feedback, and improvement areas."; `:189`, `:213` "Most frequent positive anonymized signals"; `:198`, `:222` "Recurring constructive signals to coach". demo.html and `site/js/demo.js` also use "cycle" many times.
  - `site/linkedin.html:131` "Engagement team VBAs"; `:142` the "normalized and grouped" line.
- Home page, not in the three fixes: "Edit requests, 3, Awaiting your decision" stays unexplained on the manager screen. The manager sub line "Compare team health, spot coaching priorities, and decide feedback edit requests." is a triad (allowlisted as prototype microcopy). "Aggregated last-cycle responses" and "Anonymized Feedback" labels are still jargon-ish. The first "cycle" on the page is in "Who gets a say" ("From the second cycle"), before the screens explain it. "02:09" stat, "pooled", "evidence" and the "per employee" question from the layman report are untouched.
- Possible bug, unverified: if the theme is toggled after the hero animation ends, `.eng-name` keeps the light-theme muted fill (rgb 98,92,84) in dark, because the keyframe end value holds. Seen only when I switched `data-theme` by script after load; a fresh load in dark looks correct.

## Final

### Files written, with commits (branch `d1-clarity`)
- `53d86c3` Fix 1: `site/css/home.css`, `design-lab/shots/site/clarity-hero-*.png` (4).
- `c4ddd6d` Fix 2: `site/index.html`.
- `b9e0250` Fix 3: `site/index.html`, `design-lab/shots/site/clarity-card-*`, `clarity-consultant-*`, `clarity-manager-*` (16).
- `9f906e9` follow-up: `site/css/home.css` comment wording only.
- This report.

### Key insights and findings
- The hero payoff text was not low contrast by token: the label is `--text` 14px bold. The sub line was the only weight 400 text in the picture, in the muted colour, at the smallest size. The layman capture also caught it mid fade-in (6.4 to 7.0 s). Measured in the served page, both themes.
- The docs support only "scores out of 100, made from the 3-way rating plus tags; no formula is given" (`product_facts.md:71-73`).
- The "No AI writes or scores anything" paragraph is allowlisted verbatim in `copy_scan.py:38`, so any rewording needs a person to update that allowlist.

### Decisions and why
- Fix 1 override goes in `home.css`, scoped to `.hero-visual`, because `motif.css` belongs to site-css. The phone sub line keeps its 15px from `motif.css`, so the override does not shrink it.
- Fix 2 line sits in the consultant screen figcaption, the first place a score appears, so the denial keeps its reviewed wording and copy_scan stays clean.
- "Engagement team values" follows the brief's example and the section heading "Your firm's values on every card".
- "cycle" is kept on the screens (FAQ and timeline use it) and explained once in the consultant sub line as "one every two weeks".
- "Up 3 points this cycle" mirrors the manager screen wording and agrees with the +3 chip and "Improving".

### Rejected approaches
- Rewording the denial paragraph: it would fail copy_scan, and the allowlist sits outside my file scope.
- Editing `motif.css`: shared file.
- Renaming "cycle" to "round" on the screens: it would clash with the FAQ and timeline, which still say "cycle".

### Open questions
- Should the lead also move the score line next to the denial (needs a copy_scan allowlist update), or is the figcaption enough?
- Fix the same jargon on `demo.html` and `linkedin.html` in a follow-up?

### Not verified
- No reduced-motion run and no contrast script (cut from the checks on 2026-11-25).
- The theme-toggle `.eng-name` fill issue above was not reproduced through the real toggle button.
- Screenshots were taken with the shared Playwright MCP browser against the lead's server on 8834. No other session was using it at that time, as far as I could tell.
