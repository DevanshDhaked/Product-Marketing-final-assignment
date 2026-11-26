---
type: Handoff
title: "v3 adversarial reviewer report"
description: "v3 scored on the three numbers: first screen home 9 and ad 9 of 9, professor's faults 2 of 8 partial, foreign words 8 minor entries, with a ranked fix list."
tags: [handoff, review3]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T14:40:00Z }
---

# v3 adversarial reviewer report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan
- Read research_common.md, review3.md, v2_baseline.md, professor addendum, decision log "v3 plan gate".
- Read site/*.html (index, ad, linkedin, demo, deliverables, propaganda) and js visible strings.
- Screenshots of home at 1280x800 and 375x667, ad page, via Playwright on localhost:8876 only.
- Score: first-screen rubric, 8 faults, word residue, smoke checks, section map.
- Write docs/research/v3_review.md, then ## Final here.

## Progress
- 2026-11-26: briefs and baseline read. Server at localhost:8876 returns 200.
- Screenshots taken (home 1280x800, 375x667; ad standee element). QR decoded in browser. Scan script at swarm/tmp/review3/scan.py. Browser closed.
- Note written: docs/research/v3_review.md.
- Advisor pass: ad (c) re-scored to the v2 frame rule, Member Insights row added, link check run (curl + id grep), Admin screens and managing-partner persona read.

## Not done (out of scope)
- Did not judge the professor's design point ("would consulting firms be impressed") beyond the 8 faults; not in the baseline list.
- Did not re-check pricing arithmetic sources in docs/pricing/ (spot-checked: 149 x 150 = 22,350; pilot at plan rate about 16,500 holds).
- Playwright saved its screenshots and snapshots under `.playwright-mcp/` in the worktree (gitignored; the tool would not write elsewhere).

## Final

### Files written
- `docs/research/v3_review.md` (worktree iteration-b)
- this report
- helper script `swarm/tmp/review3/scan.py` and `swarm/tmp/review3/residue.txt` (scratch)

### Key findings (n=1 reviewer, no segment readers)
- First-screen: home 9 of 9 (v2 6), measured from real screenshots at 1280 and 375. Ad 9 of 9 (v2 3) under the v2 frame rule (headline and first line only; QR block out of frame). It would be 8 if the QR block counted: no printed way to book the call, and the QR opens v2.
- Faults: 2 of 8 still present, both partial (6 fixed) (4: no line on home for the managing partner's first fear, good juniors leaving, per persona_managing_partner.md:35; 8: company-page posts, Galton ox paragraph kept at linkedin.html:107, post 3 opens on "the pilot"). Target 0 not met.
- Words: 8 entries (v2 about 20), including "Member Insights" in body copy (demo.html:63, 168, 169; deliverables.html:118; js/demo.js:14, 79, 81), a banned word unless the lead exempts the screen name. 0 hits for file, record, evidence, pooled, teammates, subordinates, VBAs, resources. Left: course labels on ad.html:133 and linkedin post notes; "circle" (demo, deliverables, js/demo.js); "turnout" index.html:226; "landing" deliverables.html:121; "the whole year" on propaganda; label "The 20-minute call" propaganda.html:223.
- Smoke FAILs: (1) ad QR decodes to `.../v2/demo.html`; printed address /v2/ at ad.html:73, 105, 118; og meta /v2/ at ad.html:22-23. (2) deliverables.html:121 gives the head of talent (Admin) a participation view that only Manager has (prototype_screens.md:87; Admin screens 118 to 140 show no counts; Frequency subtitle says "submission tracking" but shows only the schedule). Marked FAIL (likely).
- Passes: no partner role, no "anonymous", one "X, not Y" per page, no months, no customers, no dashes, all internal links resolve (6 pages 200 on localhost, 15 of 15 #id targets found), no sideways scroll at 375 on all 6 pages.
- Section map: A, I, I, I, D, A; 617 words of Interest before Decision (v2 about 1,150); section 2 is 46 percent of the page.

### Decisions and why
- Home (b) scored 3 though head of talent is not in frame: the rubric reader is the managing partner, who sees firm type, size and country.
- Ad (c) scored 3 to keep the v2 frame rule (v2 scored the same frame 0 because the QR was out of frame); the booking gap and v2 QR are reported as smoke FAIL and fix 1 and 2, not in the score.
- Product role names in body text (index.html:170, 207) not counted as foreign words: they are product truth disclosures the plan gate asks for.
- Course labels on ad and LinkedIn pages counted, since the brief allows course words only on propaganda and hub; flagged as a lead decision because the grader may want them.

### Approaches rejected
- Estimating the fold from CSS as v2 did: real screenshots were available, so measured instead.
- Reading builders' self-scores: not used, per brief.

### Open questions for the lead
- Exempt "Member Insights" (real screen name) in body copy, or rewrite as "a consultant's Insights screen"?
- Keep course labels ("Job", "Journey stage", "Call to action") on ad and LinkedIn pages as grader annotations, or rename?
- How should the standee let a reader book the call: QR to the v3 home call section, or a printed booking address?
- Post author: stay on the company page or move to a named founder or partner profile?

### Not verified
- Live /v3/ deployment (only localhost checked).
- Dark theme rendering.
- QR decode used Chrome's BarcodeDetector on the SVG rendered at 500 px; one decode, consistent with the printed /v2/ address.
- Fault 4 and 8 statuses are judgment calls.
- External link (peopleanalyst.com Scullen page) not fetched.
- Hero word count includes about 46 words of hidden exhibit steps; noted as a caveat in the section map.
