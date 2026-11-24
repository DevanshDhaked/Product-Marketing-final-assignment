---
type: Handoff
title: "Hero alignment report"
description: "The home hero's headline and lede now sit centred on each other at desktop widths."
tags: [handoff, hero]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T22:22:16Z }
---

# Hero alignment report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Progress
- `site/css/home.css` line 14: `.hero-copy` `align-items: end` changed to `align-items: center`. The 900px media query keeps one column on phones, where `align-items` has no visible effect (each item sits in its own auto-height row).
- Checks run against http://127.0.0.1:8837/ (served CSS confirmed to hold the change).

## Final

### Files written, commit SHAs
- `site/css/home.css` (one property), commit `207f8fd` on `d1-hero`.
- `design-lab/shots/site/hero-align-light.png`, `design-lab/shots/site/hero-align-dark.png` (1280 by 900, after 7 s), same commit.

### Key findings
- At 1280 the h1 vertical midpoint and the `.hero-side` midpoint are both at y = 208 px, in light and dark (2 measurements, one per theme).
- Sideways scroll at 375: scrollWidth minus clientWidth = 0.
- Both screenshots looked at by eye: headline and lede plus button read as one row; ribbon visual unaffected.

### Decisions and why
- Changed the existing declaration instead of adding a desktop-only media query. Simplest diff; single-column phone layout is unaffected by `align-items`.

### Rejected approaches
- `align-self` on each column, or a `min-width: 901px` override: more code for the same result.

### Open questions
- None.

### Not verified
- Widths between 901 and 1279 px, and above 1280 (out of scope per addendum).
- Phone screenshot not retaken; only the 375 overflow number was checked.

### Not done (out of scope)
- Nothing else noticed.
