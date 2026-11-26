---
type: Handoff
title: "Sign-off swap report"
description: "The graded-message sign-off placed on the ad, propaganda and hub; propaganda reworded to match it and keep one contrast per page."
tags: [handoff, signoff]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T14:20:00Z }
---

# Sign-off swap report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Not done (out of scope)
- `site/index.html:263` still has `<p class="signoff">The project ends. The feedback stays.</p>`. Its owner needs to make the same swap.
- `site/linkedin.html` and `site/demo.html` do not carry the new line. The hub lede now says all four deliverables close on it, so the lede is only true once those two pages carry it.

## Final

Commit `e23fbb6` on `d1-signoff`. It is one commit, amended once to reword the propaganda sentence, and it is not pushed. It changes 3 files.

### Files written
- `site/ad.html`: the standee strapline `.sd-strap` now reads "Built from everyone on the project, not one manager’s memory."
- `site/propaganda.html`: `.core-line` now carries the new line, and the TODO comment is gone. The Central message section gets one added sentence: "The core line puts the team’s graded central message into consulting words."
- `site/deliverables.html`: the TODO comment is gone. The hub lede gets one more clause: "...mapped in the campaign flow, and close on one line: “Built from everyone on the project, not one manager’s memory.”"

### Checks
- copy_scan: ad 92 strings, 0 unreviewed hits (4 reviewed denials). Propaganda 155 strings, 0 unreviewed hits (1 reviewed denial). Deliverables 77 strings, 0 unreviewed hits.
- copy_tells: each page has exactly 1 CONTRAST sentence, and on each page it is the new line. Possible triads: ad 2, propaganda 5, deliverables 1. All of them were there before this change (names, citations, setup lines). This edit added none.
- No TODO is left in the 3 pages.
- I ran the humanizer over the new strings. The only contrast is the quoted line the user approved.
- `grep "not one manager" site/*.html` finds the line only in ad, propaganda and deliverables.

### Key decisions
- In propaganda, the origin sentence does not quote the full graded message ("...not one manager's memory."). A quote would put a second "X, not Y" on the page and break the one-per-page rule.
- The brief makes the origin sentence conditional on the page already explaining where the core line came from. I counted the Central message paragraph as meeting that condition. Strictly, that paragraph explains the reason for the line rather than its origin. Remove the sentence if you read the condition more strictly.
- "Carry one line on every piece" (tactic list) and "One line on every piece links posts seen weeks apart" describe the line and do not quote it. I left both as they were, because writing the line into them would repeat the contrast on the page.
- I used curly apostrophes and quotes to match the nearby copy on these pages.

### For the lead (decisions needed)
1. Propaganda Central message contradicts the new line. The paragraph still says "The line blames how work rotates, so partners can hear it without getting defensive." That described the old line. The new line points at "one manager's memory", not at rotation. The paragraph is now inaccurate next to the line it explains, and it needs a reword. The hard scope stopped me from changing it.
2. The hub lede claim is not yet true. LinkedIn and the walkthrough (`linkedin.html`, `demo.html`) do not carry the line. Have their owners add it, or drop the clause from the lede.
3. Propaganda line 73 (Tactics dd) reads "Name the problem and blame rotation, never partners." This is a clipped "X, not Y" form that copy_tells does not flag. With the new core line, the page arguably has two. I did not change it.
4. `index.html` still has the old sign-off. See "Not done" above.

### Not verified
- I took no screenshots, which the brief allows unless a line wraps. I did not check how the longer strapline wraps on the standee mockup at 375 or 1280. That is the most likely place for a bad wrap.
- I did not re-check links. No hrefs changed.

### Approaches rejected
- I did not quote the graded message on the propaganda page, for the one-contrast-per-page reason above.

### Follow-up from the lead (scope extended to findings 1 to 3, plus a wrap check)
Commit `ae0cab1` on `d1-signoff`, after `e23fbb6`. It changes 2 files, `site/propaganda.html` and `site/deliverables.html`.
- Finding 1, Central message: the rotation sentence now reads "The line places the gap where one manager’s memory carries the rating and offers everyone on the project as the fix, so a partner hears a better way to rate." It has no contrast.
- Finding 2, hub lede: I dropped the clause saying all four deliverables close on one line. The lede is back to "...mapped in the campaign flow." The point about linkedin.html and demo.html in "Not done" no longer applies.
- Finding 3, Tactics row: it now reads "Name the problem as how ratings are made, and leave partners out of the blame."
- Checks after the edits:
  - copy_scan: propaganda 155 strings, 0 unreviewed hits. Deliverables 77 strings, 0 unreviewed hits.
  - copy_tells: propaganda has 1 contrast, the core line. Deliverables has 0.
- Strapline wrap on ad.html (http://localhost:8875/site/ad.html):
  - At 1280 and at 375 the line sits on 2 lines and breaks after "project,". There is no orphan and no sideways scroll; scrollWidth equals the viewport at both widths.
  - No fix was needed. I closed the browser afterwards.
- Screenshots: `Product-Marketing-final-assignment.swarm/tmp/signoff/ad_strap_1280.png` and `ad_strap_375.png` in the same folder. I checked both in the light theme only.
- Still open: the tactic list item "Blame the gap on rotation and fading memory" (propaganda shift diagram) still points at rotation. It has no contrast, and I left it because it was not in this scope.
