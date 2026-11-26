---
type: Handoff
title: "v3 design reviewer report"
description: "All six pages checked against v2 at 1280 light and dark and 375: one blocker (hero past the fold), visible defects and nits, and the v2 parity list."
tags: [handoff, dreview]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T15:20:00Z }
---

# v3 design reviewer report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan
- Load design-taste-frontend and design:design-critique skills.
- Read docs/design/slop_rules.md and design_system.md.
- For 6 pages x (1280 light, 1280 dark, 375 light), v3 (8883) and v2 (8830): viewport screenshots down the page, edge measurement script, overflow check.
- Write docs/research/v3_design_review.md with ranked defect table and v2 parity list.

## Progress
- Loaded skills: design-taste-frontend and design:design-critique. Read docs/design/slop_rules.md.
- Screenshots taken: v3 and v2, 6 pages x 1280 light, 1280 dark, 375 light, viewport steps of (h-60)px, reducedMotion=reduce. Files `{v2|v3}_{page}_{1280l|1280d|375l}_{NN}.png` in swarm/tmp/dreview/.
- No sideways scroll on any page at any width (scrollWidth equals viewport on all 36 loads).
- Section edge measurement (script, 6 pages x 1280 and 375, v2 and v3): outer content edges match v2 everywhere (L104/R1176 at 1280, L16/R359 at 375). Only overshoot: index #say at 375 reaches x=367 (Juniors label), inside the viewport. Raw data: swarm/tmp/dreview/_edges.txt.
- Demo stepped through (pick Tara, Was good, two tags, Submit) on both versions and all 3 configs; files `{v2|v3}_demoopen_*`. Call popover captured: `v3_callnote_1280l.png`.
- Done so far: index, demo, ad. Findings held for the note.
- Interim findings (persisted before more checks):
  - Index hero 1280x800: hero 861px tall (v2 765). Figure caption on the fold, Play again below. H1 3 lines. Regression.
  - Index pricing: pilot card uses outline btn-secondary for "Book a 20-minute call"; same label is green primary in nav, hero, close.
  - Captions: demo and linkedin use new "Exhibit N." caption (exhibit-cap, green rule, Source line, bold note); index, ad, propaganda keep the plain caption. v2 used the icon caption on demo and linkedin.
  - Call popover (v3 only) opens centred over the demo intro, covering the sample-data line and steps 3 to 4.
  - Index 375: Team Insights hides the Edit requests card (v2 same). Circle centre label "Consultant" hidden (v2 same).
  - Propaganda timeline wraps "Book a 20- / minute call". Ad URLs break as "Product / -Marketing".
  - Hero animation timing identical to v2 (settles about 8 s); not a defect.
- Coverage gaps closed: dark sheets for demo, ad, propaganda, deliverables and v2 dark viewed; stepped demo at 375 and dark viewed; phone Menu opened on both; widow scan rerun over all leaf text elements; #how frame gap and H2 offset measured. Browser closed.

## Final

### Files written
- `docs/research/v3_design_review.md` (worktree iteration-b): ranked defect table (1 blocker, 11 visible, 9 nits), v2 parity list, 8 action bullets.
- This report.
- Screenshots and data, not for commit: `swarm/tmp/dreview/` (about 270 PNGs, `sheets/`, `_edges.txt`, `_ctas.txt`).

### Key findings (source: local pages 8883 and 8830, measured 2026-11-26)
1. Blocker, new: the index hero at 1280x800 is 861 px tall (v2 765). The ribbon caption sits on the fold, and Play again falls below it. The H1 runs 3 lines. Shots: v3_index_1280l_00.png against v2_index_1280l_00.png.
2. Visible, new: the pilot card renders "Book a 20-minute call" as an outline secondary button, while it is the green primary everywhere else.
3. Visible, new: there are two caption systems. Demo and linkedin use "Exhibit N." with a green rule and Source line; everything else, including v2, uses the icon caption.
4. Visible, new: the call popover opens centred over the demo intro instead of near the nav button.
5. Visible on phones, inherited: Edit requests is hidden in Team Insights, which breaks a slop rule. The circle centre label is hidden. The feedback frame has an empty strip of 222 px from the last tag to the frame bottom (v2 118).
6. Visible, new:
   - The close heading ends on the widow "memory."
   - The problem rows use full width with a hairline on each row and the right third empty.
   - The demo step 4 CTA floats mid-column.
   - Text-link CTAs use mixed styles.
   - The deliverables page has two left edges (104 and about 200).
7. Passed:
   - No sideways scroll on any of the 36 loads.
   - outer content edges (104/1176 at 1280, 16/359 at 375) match v2.
   - Nav is identical across pages.
   - Logo, ribbon, circle, frames and cards are present.
   - Animation timing matches v2, with no console errors.
   - Dark mode matches v2.

### Decisions and why
- Ran the screenshots with reduced motion so figures show their final frame. Motion was then checked separately at 0.7, 3, 5.7, 8, 12 and 18 s. Without the reduced run, mid-animation frames would read as false defects.
- Ranked the hero as the only blocker. It is the first screen and a clear regression from the v2 composition the user asked to keep. The other items need a careful look to notice.
- Tagged each defect new or inherited, so the lead can separate regressions from v2 debt.
- Wrote the dropped v2 blocks as a parity list for the lead to confirm. I did not rank them as defects, because the v3 order may have cut them on purpose.

### Approaches rejected and why
- One full-page screenshot per page: the brief forbids it, and it hides fold problems.
- Treating the sphere drawing late as "not rendering": at 5.7 s it looked missing, but the 3/8/12/18 s run showed identical timing in v2. Not a defect.
- Contrast or WCAG checks: out of scope (smoke level).

### Open questions for the lead
- Were these v2 pieces cut on purpose: the stats row, the FAQ accordion, Today/With Sphyr, the home timeline (now on deliverables), and the end button rows on ad and linkedin?
- Should the "Exhibit N." caption stay on demo and linkedin as a deliberate deliverable-style label, or go back to the v2 icon caption?
- Should the phone header or Menu carry "Book a 20-minute call", now that it is the main action?

### Not verified
- v2 at 375 was viewed in full only for index and demo. For ad, linkedin, propaganda and deliverables, the inherited tags at 375 come from 1280 comparisons and the widow scan.
- Dark mode at 375 was not captured (not in the brief's matrix).
- Two values were read from screenshots, not measured: the step 4 CTA offset and the about-200 px title column on deliverables.
- Copy issues seen but out of scope: the demo intro says "Member Insights view" while step chip 3 says "See the Manager view".
- Browsers other than Playwright Chromium were not tested.

### Not done (out of scope)
- Copy review (one label mismatch noted above).
- WCAG and contrast audits.
- `docs/research/index.md` and `log.md` need an entry for `v3_design_review.md`; I am read-only, so the lead adds it.
