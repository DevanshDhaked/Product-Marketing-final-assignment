---
type: Handoff
title: "v2 baseline auditor report"
description: "Where v2 stands on the three v3 success numbers: first-screen 6 of 9 home and 3 of 9 ad, 8 of 8 professor faults present, about 20 foreign-word entries."
tags: [handoff, baseline]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T09:46:00Z }
---

# v2 baseline auditor report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan
1. Read context (professor feedback addendum, handoff s2-3, product facts, prototype screens, do_not_claim).
2. Read site/index.html, ad.html, linkedin.html, demo.html, deliverables.html, propaganda.html, site/js visible strings.
3. Score first-screen test, check 8 professor faults with file:line, list foreign words, map home sections with AIDA tags.
4. Write docs/research/v2_baseline.md. Finish this report with ## Final.

## Progress
- Context read: professor_feedback.md addendum, handoff sections 2 and 3.
- Product docs read (prototype_screens, product_facts). Segment and persona docs skimmed only by name; not needed for this audit.
- Visible text extracted from site/index, ad, linkedin, demo, deliverables, propaganda and js/*.js with a line-numbered script (swarm/tmp/baseline/vis.py). Outputs in swarm/tmp/baseline/*.txt.
- Live v2 home (firecrawl markdown, 2026-11-26) matches the repo hero and sections. Firecrawl screenshot at 1280x800 failed ("All scraping engines failed"); first-screen content is estimated from home.css instead.
- Home section word counts computed (visible text incl. figure labels).
- Live /v2/ ad and LinkedIn pages (firecrawl markdown) match the repo: ad headline and first line, all three posts (post 3 without price, as in 53081a0).
- Screenshot retried once without maxAge/waitFor; failed again. Stopped retrying (2 failures, under the 3-failure stall rule).
- Residue pass: page words minus product-doc words gave 415 distinct words; read by hand for the foreign-word table.
- Note written: docs/research/v2_baseline.md.

## Not done (out of scope)
- Design-style question (would a consulting firm be impressed by the UI): not in this brief.
- No copy, headlines or fixes written, per the brief.

## Final

### Files written
- `docs/research/v2_baseline.md` (worktree iteration-b). New folder `docs/research/` (it did not exist).
- This report.
- Scratch only (not for commit): `swarm/tmp/baseline/` (vis.py, residue.py, extracted page text).

### Key findings
- First-screen test (one auditor, n=1, rubric 0 to 3 defined in the note): home hero 6 of 9 (what 2, who 1, next 3); ad headline plus first line 3 of 9 (what 1, who 2, next 0). Lowest: home "who" (no firm type, size, country or buyer role in frame) and ad "next" (CTA at ad.html:84 is outside the frame). Source: site/index.html:66-69, site/ad.html:71,81.
- All 8 professor faults are present in v2; none fixed. Professor's "What goes wrong when the team moves on?" is the repo h2 "What goes wrong when the team has moved on" (index.html:95, no question mark).
- "file": 6 visible uses on home in source (5 rendered, one SVG copy shows) and 2 on LinkedIn; product uses "file" only for CSV import. "record": 21 visible uses (18 in page HTML, 3 in js/demo.js; aria-labels not counted); the product calls that view "Insights". Other product mismatches: pooled, evidence, Juniors, Clients, Strongest area, teammates, seat.
- Home section map: weak A, then about 1,150 of 1,810 words of Interest before any Decision content; onboarding assurance (index.html:357-366) and course rationale (346-352) sit after the first Action (334). "See the 2-minute walkthrough" appears 6 times on home.
- All three LinkedIn posts are posted as the Sphyr company page (linkedin.html:69,102,173), not a person.
- Live v2 (home, ad, LinkedIn) matches the repo at b6051be (firecrawl, 2026-11-26).

### Decisions and why
- Defined a written 0 to 3 rubric before scoring, so v3 can be re-scored the same way.
- Scored the ad strictly on headline plus first line, as the brief says; did not credit the QR CTA.
- Counted one SVG copy in the hero (only one of cv-wide/cv-compact renders).
- Used the professor's course AIDA definitions (I = problem plus assurance, D = low friction) for tags.
- Did not flag "landing" (product H1) or "circle" (in the product's My Sphyr subtitle).
- Split aria-label-only words from visible words.

### Approaches rejected and why
- Grep for suspected words only: misses unknown words; replaced with a residue pass against the product docs.
- Further screenshot retries: two failures with the same error; fold estimated from css/home.css instead.

### Open questions for the lead
- "Juniors" and "Clients" differ from product "Subordinates" and "External" but read better for consulting. Keep or match the product?
- Should course pages (Deliverables, propaganda, the "Why this ad" and "Job / Journey stage" blocks) stay on the buyer-facing nav in v3, or move behind a separate course link?
- "calibrate" and "practice" look like real consulting words; wait for the vocabulary teammate to confirm.
- `docs/research/` is a new folder with no `index.md` or log entry, and it is not linked from the docs index. Add the OKF index and log entries when committing (I may not edit existing files).

### What I did not verify
- The exact fold line at 1280 by 800 (no screenshot). Whether "Promotion round" in the SVG is above the fold is an estimate.
- Live versions of demo.html, deliverables.html, propaganda.html (repo only).
- Whether the "to confirm" vocabulary entries are or are not consulting words.
- No reader from the segment was tested; all scores are one auditor's judgment.
