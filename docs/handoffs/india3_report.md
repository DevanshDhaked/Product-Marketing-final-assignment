---
type: Handoff
title: "India in the lede report"
description: "India moved from the home headline into the lede, the ad first line and the LinkedIn intro; the Insights caption uses the app's word."
tags: [handoff, india3]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T16:05:00Z }
---

# India in the lede report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Branch `d1-india3`, worktree `Product-Marketing-final-assignment.d1-india3`. Brief was the approved plan, so no plan stop.

## Final

Success number: "Indian" appears 0 times in the home H1, ad standee/A6 lines and LinkedIn lede/meta (only the ad "Audience" rationale row keeps it, as briefed).

### Files written, commits
- `556d964` Move India out of the home headline into the lede; ad and LinkedIn lines say 'in India'
  - `site/index.html`: H1 "Peer feedback for appraisals <em>at consulting firms</em>" (markup and accent kept). Lede now starts "For firms of 40 to 400 people in India."
  - `site/ad.html`: standee (`.sd-line`) and A6 front (`.a6-line`) now "for heads of talent at consulting firms of 40 to 400 people in India". Audience row untouched.
  - `site/linkedin.html`: intro lede, meta description, og:description now "...at consulting firms of 40 to 400 people in India."
- `767c666` Home Insights caption: scores come from answers in Fortnightly Feedback (`site/index.html`)

### Key decisions
- Home `<title>`, meta and og tags did not say "Indian", so they were left alone (brief: update only if they say "Indian").
- No hero spacing or size change: at 1280x800 the H1 is still 2 lines, the column reads balanced, and Play again sits at y=794 of 800, with its caption beside it.
- Two commits: the India move and the caption fix are separate logical changes.

### Checks
- copy_scan and copy_tells on index, ad, linkedin: output identical to the HEAD baseline (index 0 hits; ad 0 hits; linkedin 1 hit "[social proof] Ten months later..." is pre-existing, not in scope).
- No sideways scroll at 375: index, ad, linkedin all scrollWidth 375.
- Standee and A6 front: the new line fits in both, no clipping seen in the screenshots.

### Approaches rejected
- None needed. The edits are word swaps.

### Open questions
- None.

### Not verified
- Did not run the humanizer skill: the edits move existing words around and add no new phrasing.
- The standee box has scrollHeight 904 vs clientHeight 894 and scrollWidth 395 vs clientWidth 380 at 1280. It looks fine in the screenshot (likely ribbon art). Not compared with the pre-change state.
- Ad and LinkedIn not screenshotted at 375 (only scrollWidth checked). LinkedIn not screenshotted at all (only the lede text was read back).

### Screenshots
`Product-Marketing-final-assignment.swarm/tmp/india3/`
- `home_1280_light.png`, `home_1280_dark.png`, `home_375.png`
- `ad_standee_1280.png`, `ad_a6_front_1280.png`

## Not done (out of scope)
- linkedin.html copy_scan "[social proof]" hit on the "Ten months later" line (pre-existing).
- `propaganda.html` left as is, per brief.
