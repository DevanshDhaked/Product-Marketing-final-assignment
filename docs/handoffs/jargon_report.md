---
type: Handoff
title: "Plain words on walkthrough and LinkedIn report"
description: "Walkthrough and LinkedIn post 2 prototype screens now use the same plain words as the home page."
tags: [handoff, jargon]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T22:12:14Z }
---

# Plain words on walkthrough and LinkedIn report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Status: done. Plan stop skipped as the brief says (user approved the fix).

## Changed strings (old, then new)

`site/demo.html`:
- `:124` and `:133` chip: "Engagement team VBAs" to "Engagement team values".
- `:132` Could improve step: "Choose the clearest signals. Your name is not shown with your response." to "Pick the ones that fit best. Your name is not shown with your response."
- `:157` private note: "Individual responses are normalized and grouped before anyone sees them." to "Each answer is grouped with the others before anyone sees it."
- `:180` Member Insights sub: "Review individual performance signals, comparisons, feedback, and improvement areas." to "See what colleagues said about each consultant, side by side."
- `:189` and `:213` card sub: "Most frequent positive anonymized signals" to "Tags picked most often with "Was good"" (written as `&quot;Was good&quot;`).
- `:198` and `:222` card sub: "Recurring constructive signals to coach" to "Tags that keep coming up with "Could improve"" (written as `&quot;Could improve&quot;`).

`site/linkedin.html` (post 2 faux screen only; post texts untouched):
- `:133` chip: "Engagement team VBAs" to "Engagement team values".
- `:144` private note: "Individual responses are normalized and grouped before anyone sees them." to "Each answer is grouped with the others before anyone sees it."

`site/js/demo.js`: no change. It holds none of the listed strings and no code reads them.

Rating words: neither page had "Positive" as a rating label. The two tag-card subs now name the card's own labels, "Was good" and "Could improve".

## Checks (smoke only, per the lead's rule)
- copy_scan demo: 189 strings, 1 unreviewed hit ("Review period", prototype label, false positive on `\breviews?\b`). Before this work it was 2 hits; the old sub line "Review individual performance signals..." was the other one. linkedin: 148 strings, 0 unreviewed hits.
- copy_tells: same results as before the change on both pages. demo: 1 contrast ("Tara and Nikhil are an example, not real consultants."), 1 triad (team names). linkedin: 0 contrast, 3 possible triads (all inside the post texts or credits, all present before). No new hits.
- Humanize: the 6 new distinct strings were checked by hand against the humanizer patterns (no dashes, no triads, no contrast, plain words). Three of them are copied byte for byte from the home page.
- Links: every relative href/src resolves (demo 25, linkedin 26 unique).
- Sideways scroll at 375: scrollWidth equals clientWidth (360/360) on both pages, both themes.
- Walkthrough: run end to end for Tara and Nikhil, light and dark (4 runs). After the pick and submit, `#card-done` shows, `#yours` is visible, and `#compare` and `#turn` hold the picked person's text. 0 page errors.
- Screenshots at 1280, light and dark, checked by eye, in `design-lab/shots/site/`: `jargon-demo-card-good-*`, `jargon-demo-card-improve-*` (Could improve tile clicked), `jargon-demo-insights-*` (taken after a Nikhil run, so his count shows 75; the nav was hidden for the capture only), `jargon-linkedin-post2-*`. The longer tag-card subs fit on one line at 1280.
- 375, light, checked by eye: `jargon-demo-card-improve-light-375.png`, `jargon-demo-insights-light-375.png`. "Tags that keep coming up with "Could improve"" wraps to two clean lines; the private note shows in full; the manager sub wraps to two lines.

## Not done (out of scope)
- "Anonymized Feedback" (demo.html `:205`, `:206`, `:228`, `:229`, demo.js `:92`): home kept it, the brief does not list it.
- "cycle" wording on demo ("Last Cycle / All Cycles", "6 cycles", "Repeated across N cycles", "Cycle 5/6"): not listed.
- "Review period" copy_scan hit: needs an allowlist entry in `design-lab/copy_scan.py`, outside my file scope.

## Final

### Files written, with commits (branch `d1-jargon`)
- `0cfa6cf` `site/demo.html`, `design-lab/shots/site/jargon-demo-{card-good,card-improve,insights}-{light,dark}-1280.png` (6).
- `6e1c553` `site/linkedin.html`, `design-lab/shots/site/jargon-linkedin-post2-{light,dark}-1280.png` (2).
- `210ade9` `design-lab/shots/site/jargon-demo-{card-improve,insights}-light-375.png` (2).
- This report (outside the repo, not committed).

### Key insights and findings
- No "Positive" rating label existed on demo or linkedin; the only "positive" was inside the "signals" line.
- demo.js has no selector or text dependency on any changed string, so the walkthrough logic was not affected.
- The tag cards in the prototype show tags from the "What stood out?" step (Was good) and the friction step (Could improve). `docs/product/product_facts.md:86` describes the second as "top recurring constructive tags". The new subs say the same in plain words.

### Decisions and why
- Copied the three home strings exactly so all pages match (`docs/handoffs/clarity_report.md`, "Changed strings").
- Quoted the rating labels in running text (`&quot;Was good&quot;`), following the home FAQ (`index.html:301`, `Choose &quot;No interaction&quot;`), so the label does not read as a typo.
- Manager sub "See what colleagues said about each consultant, side by side." describes what the two-column screen shows. It drops the old four-item list.

### Rejected approaches
- Editing demo.js "Anonymized Feedback": not listed and home kept it.
- Adding "Review period" to the copy_scan allowlist: shared file outside scope.

### Open questions
- Should "Anonymized Feedback" and the "cycle" labels get the same plain-word pass on all pages, home included?

### What I did not verify
- 375 screenshots in dark, and the LinkedIn post 2 screen at 375 (only the chip and private note changed there; sideways scroll is 0).
- The home strings themselves were not rechecked.
