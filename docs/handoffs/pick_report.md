---
type: Handoff
title: "Walkthrough pick teammate report"
description: "The walkthrough card, partner view and ending now follow the visitor's pick of Tara or Nikhil."
tags: [handoff, pick]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T21:10:23Z }
---

# Walkthrough pick teammate report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Design read (2026-11-25)

Pick sets one person (Tara or Nikhil). Everything after step 1 names that person. No new steps, no new numbers; only numbers already on the page are reused (Tara 65 responses from 10 of 14, Nikhil 74 from 13 of 14, six cycles).

- Step 1: unchanged. Reply "You picked X. We'll come back to that at the end." already follows the pick.
- Step 2: heading, intro line, card name, avatar (initials and colour), question legend, comment label and the submitted row all show the picked person. Reply after submit names the picked person. Drop "this cycle" from "joins the other 13 from Nikhil's circle this cycle": 13 is the six-cycle count, so it was a wrong claim. New line names the person's own count (10 or 13 people).
- Step 3: same two-column view. The visitor's card lands in the picked column (count, tag bars, improvement areas, comment). Tara's list items get data-tag hooks so her bars bump too. Intro paragraph leads with the picked person's numbers and top tags, then the other's count. Caption names the picked column.
- Step 4: ending text per pick. Tara path: the record backs what you saw of Tara, and shows 13 colleagues saw Nikhil's work you never saw. Nikhil path: as today. Both end on partners still deciding with what colleagues saw.
- Without JS the page stays as now (Nikhil default in the HTML).
- Template comments: none left in site/demo.html. Step indicator fix (li + li margin) already in demo.css; recheck by eye.

## Final

Status: done. Both paths (Tara, Nikhil) walk to the end with the card, partner view and ending matching the pick.

### Files written, with commits (branch d1-pick)
- `site/demo.html`, `site/js/demo.js`: ee0f15c "Walkthrough card, partner view and ending follow the pick".
- `design-lab/shots/site/demo-pick-{tara,nikhil}-step{3,4}-{light,dark}-1280.png` and `demo-pick-tara-step3-light-375.png`: 6bb482b.
- `site/js/demo.js`, `site/css/demo.css`: 5e0c315 "Trim step 2 reply to old length; default cursor on locked pick".

### Key findings
- Old step 2 reply said the card "joins the other 13 from Nikhil's circle this cycle". 13 is the six-cycle collaborator count, so "this cycle" was wrong. New line, same length as the old one (22 words for Nikhil): "Your card joins those from {10|13} other colleagues in {name}'s record, and {name} sees what you said without your name on it."
- If the visitor changed the pick after submitting, the labels would switch while the counts sat in the other column. Pick radios are now disabled after submit.
- Dated template comments: none were left in `site/demo.html` (0 `<!--`).
- Step indicator: the `li + li` fix was already in `demo.css`; at 1280 all four marks sit at the same top (396 px).

### Decisions
- One `people` map in `demo.js` holds name, initials, avatar colour, collaborator count, step 3 sentence and step 4 ending for each person. The HTML marks the parts to fill with `data-first`, `data-full`, `data-av`, `#compare`, and `data-col` on each column. Tara's tag and area items got `data-tag` so her bars count the card.
- Kept the HTML default as Nikhil, so the no JS page reads as before.
- Reused only numbers already on the page (10 and 13 of 14, six cycles, the top tags). No new claims.
- New strings went through the humanizer. Final Tara ending: "You picked Tara, and Tara's record backs what you saw in client meetings. It also shows 13 colleagues who saw Nikhil's work over six cycles, and very little of that work reached you. Partners still decide, now with both records open." Nikhil ending is unchanged.

### Rejected
- Reordering the columns or adding a "your pick" badge in step 3: it would be a new feature, and the caption and intro sentence already name the pick.
- Keeping pick changes live after submit: it would need the card moved between columns. Locking is smaller and honest.

### Checks
- copy_scan on demo.html: 2 hits, both existing prototype UI text ("Review ..."), not new. copy_tells: 1 contrast (the existing "an example, not real consultants"), 1 triad flag on the footer team names (a real list).
- Links: all relative href/src targets exist.
- 375: scrollWidth 360 equals clientWidth 360, so no sideways scroll.
- copy_scan and copy_tells on the rendered `main` text after each path (Tara and Nikhil): 0 hits; 1 contrast (the existing one); 1 triad flag on the existing prototype subtitle "comparisons, feedback, and improvement areas".
- Keyboard, full path: arrow keys switch the pick before submit and the card relabels; Tab into the card, Space ticks a tag, Tab 10 times reaches Submit, Enter submits, focus lands on `#card-done`, next Tabs reach "Book a 20-minute call" and "Back to home". After submit the pick radios are disabled (skipped by Tab); the picked row keeps its green fill and reads as locked.
- All 9 screenshots checked by eye. The first element shots had the sticky nav over the content (a capture artifact). Those were retaken with the nav set static for the capture only.

### Open questions
- None blocking. The brief says "over the year", but the page says six cycles (about 12 weeks). I kept the page numbers.

### Not verified
- Screen reader output of the changed names (the live regions are unchanged).
- Dark theme at 375.
