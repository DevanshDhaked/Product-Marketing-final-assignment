---
type: Handoff
title: "v3 final check report"
description: "Final scores: home and ad 9 of 9, professor's faults 1 of 8 partial (company-page posts), foreign words 1 to 2 on course pages; both themes at both widths with no blocker or visible defect."
tags: [handoff, final3]
generated: { by: claude-code/opus-5-5, at: 2026-11-27T00:00:00Z }
---

# v3 final check report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan
1. Read v3_review.md, v2_baseline.md, v3_design_review.md, professor_feedback addendum, decision_log 2026-11-26 entries.
2. Re-score three numbers on final site (localhost:8889) with v3_review methods.
3. Screenshot every page at 1280/375 x light/dark; list defects.
4. Check og tags and site/assets/og.png.
5. Smoke checks.
6. Write docs/research/v3_final_check.md, then ## Final here.

## Progress
- Read method docs (v3_review, v2_baseline rubric, v3_design_review, professor addendum, decision log 2026-11-26).
- 182 viewport screenshots taken on localhost:8889 (6 pages x 1280x800 and 375x667 x light and dark, reduced motion, theme from prefers-color-scheme, no pinned theme). Files: swarm/tmp/final3/{page}_{1280|375}{l|d}_NN.png; contact sheets swarm/tmp/final3/sheets/.
- scrollWidth = clientWidth on all 24 loads (no sideways scroll).
- Demo stepped through in 4 settings; phone Menu and nav popover opened in both themes; dark via toggle pixel-diffed (0 px difference, 8 frames).
- og tags, QR, links, label, dash, month and "X, not Y" checks run. Note written.

## Final

### Files written
- `docs/research/v3_final_check.md` (iteration-b worktree, uncommitted).
- This report.
- Scratch only (not for commit): `swarm/tmp/final3/` screenshots, sheets, scripts.

### Key findings
- First-screen: home 9 of 9 at 1280x800 and 375x667 (H1 now 2 lines; ribbon, caption and Play again fit, Play again at y 750 to 794). Ad standee 9 of 9; QR decodes to `.../v3/` (3 of 3), 0 "/v2/" hits in site/.
- Faults: 1 of 8 left, partial and a judgment: fault 8 (all posts from the Sphyr company page, `linkedin.html:63`; post 3 opens on "the pilot", 193). Fault 4 closed by the Attrition row (`index.html:106`). Ox paragraph gone.
- Foreign words: strict 2, lenient 1. "the whole year" on `propaganda.html:71`, 109, 128, 213 (no exemption). AIDA words used as values or body text on ad 128 to 129 and LinkedIn 100 to 104, 180 to 181, 233 to 234 (exemption names only Job, Journey stage, Call to action). Buyer copy on home and ad: 0.
- Design: 18 rows from v3_design_review checked: 17 fixed, 1 still present ("Strongest signal" card hidden on phones, inherited). 3 new nits: propaganda 375 "2- / minute" break (`propaganda.html:70`), post 2 comment URL hyphen breaks at 375 (`linkedin.html:173`), og.png mono logo mark vs full-colour header. No blocker, no visible-rank defect. Dark at 375: no defect beyond light.
- Link previews: og:image and og:url correct on 6 of 6 pages; og.png shows the v3 headline and lede. No twitter:image tag (fallback to og).
- Smoke: no sideways scroll (24 of 24 loads plus 4 opened demos), links resolve (6 of 6 pages 200, 16 of 16 ids), main label exact, at most one "X, not Y" per page, 0 dashes, 0 month names.

### Decisions I made and why
- Counted foreign words twice (strict and lenient) because the exemption text names three labels while the pages use more AIDA words; the lead owns that call.
- Marked fault 8 "partly present" rather than fixed: copy is better, but the author is still the company page, which the team's own research shows gets 1.6 percent reach.
- Did not log the ad's dark-mode lack of a beige mat: v2 dark is the same.
- Did not log the dark band in `standee_el.png`: it is the sticky header over the element in a dark-emulated run.

### Approaches rejected and why
- Reading all 182 screenshots one by one: used light/dark side-by-side contact sheets instead, and opened single frames where needed.
- Counting `.btn-primary` only for the label check: extended to footer, menu and text mentions after review.

### Open questions for the lead
1. LinkedIn author: company page with staff reshares, or a named person? Last open fault.
2. Extend the course-label exemption to AIDA stage words as values (ad, LinkedIn), or relabel?
3. Replace "the whole year" on the propaganda page to reach 0 residue?
4. og.png: switch to the full-colour logo mark?

### What I did not verify
- Live GitHub Pages /v3/ (only localhost:8889).
- How real link previews render on LinkedIn or WhatsApp (tags checked only).
- The external link peopleanalyst.com.
- Four old nits not re-checked one by one (price card divider, counts table width, How it works H2 offset, Insights caption widow); none stood out in the sheets.
- Motion-on ribbon and circle animations (reduced motion was on).
- No reader from the segment; all scores n=1.
