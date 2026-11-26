---
type: Handoff
title: "Final nits report"
description: "Five nits from the final check fixed: hyphen breaks and project wording on propaganda, the LinkedIn comment URL, the colour mark on og.png, and the Strongest signal card on phones."
tags: [handoff, nits3]
generated: { by: claude-code/opus-5-5, at: 2026-11-27T00:30:00Z }
---

# Final nits report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Success number: 5 of 5 items fixed and committed on `d1-nits3`. No sideways scroll on 12 of 12 loads (3 pages, 375 and 1280, light and dark).

## Final

### Files and commits
- `a998b44` `site/propaganda.html`: items 1 and 2 (same file, one group).
  - Item 1: "2-minute" and "20-minute" in the core card "Expected response" use U+2011.
  - Item 2: "Nobody remembers all of a consultant's projects." (core card "Belief today" and the Belief section quote); "Partners still decide, now with every project in the cycle in front of them." (managing partner); "so partners decide with every project in the cycle in view." (positioning paragraph). 0 hits for "whole year" left on the page.
- `a5cadce` `site/linkedin.html`, `site/css/posts.css`: item 3. The URL now reads `devanshdhaked.github.io/<wbr><span class="nw">Product-Marketing-final-assignment/</span><wbr>v3/<wbr>demo.html`. A new rule `.li-bubble .nw { white-space: nowrap; }` keeps the hyphenated segment whole. At 375 the segment ends at x=329, inside the bubble edge at x=342.
- `5feefcf` `design-lab/og/og.html`, `site/assets/og.png`: item 4. I removed `mark--mono` from the brand mark and re-rendered at 1200 by 630 with Playwright (`page.screenshot`, clip, `scale: 'css'`). A pixel diff against the old image changes only the box (81,124)-(125,167), which is the mark.
- `720af12` `site/css/base.css`: item 5. In the Insights `@container (max-width: 600px)` block, the third KPI changed from `display: none` to `grid-column: 1 / -1`. This is the same pattern as the Edit requests fix. At 375 the frame is 343 by 699, with two cards side by side and "Strongest signal" full width below them.

### Key decisions
- Item 5 is in `base.css`, not `home.css`. The hiding rule and the Edit requests fix both live in `base.css`. `.fx-insights` is only used on `index.html`, so no other page changes.
- Items 1 and 2 share one commit because both edit `propaganda.html`. Splitting them would need interactive staging.
- Item 2 wording uses phrases that already appear on the site ("Every project, in one view", "appraisal cycle"). It adds no new claim and no "X, not Y". The page still has 1 contrast sentence (the sign-off).

### Rejected
- Using U+2011 inside the LinkedIn URL text in place of a span. A pasted URL would then contain non-ASCII hyphens. The span keeps the ad cards' pattern.

### Checks
- copy_scan and copy_tells: propaganda has 0 unreviewed hits and 1 contrast. index has 0 unreviewed hits. linkedin has 1 unreviewed hit ("social proof", the post 1 story line). That hit is pre-existing: the same hit shows on the HEAD copy before my change, and it is out of scope.
- Humanizer review of the 3 new lines flagged nothing.
- Playwright console: only a favicon 404 when rendering og.html.

### Not verified
- How LinkedIn or WhatsApp show the new og.png (not pushed).
- Pages other than propaganda, linkedin and index were not reloaded. No other page shares the changed rules: `.li-bubble` is in posts.css (linkedin only) and `.fx-insights` is on index only.
- At 375 the Insights satellite card covers the lower chart. I measured this on the live page with the old rule injected, then without it. Before: frame 591 px, with 58 px of chart visible above the satellite. After: frame 699 px, with 58 px of chart visible above the satellite. The visible chart height did not change. No height, aspect-ratio or overflow rule in `home.css` targets the Insights stage.

### Open questions
- None. `grep "whole year"` finds 0 hits in `site/` and `docs/`, so no source doc quotes the old wording.

### Screenshots
`Product-Marketing-final-assignment.swarm/tmp/nits3/`:
- propaganda_{core,aud,shift,pos}_{375,1280}{l,d}.png
- linkedin_comment_{375,1280}{l,d}.png
- index_insights_{375,1280}{l,d}.png
- og_before.png (the old image). The new image is `site/assets/og.png`, and I looked at it.

### Not done (out of scope)
- In the propaganda timeline, "The 2-minute walkthrough" (line 222) still uses a plain hyphen. The brief scoped item 1 to the core card only.
- The pre-existing copy_scan hit on linkedin post 1.

Browser closed. Idle.
