---
type: Handoff
title: "Pricing trim teammate report, phase 3"
description: "The trimmed pricing section: equal cards, scorecard toggle, price reasons, moved 02:09 stat, checks."
tags: [handoff, trim]
generated: { by: claude-code/opus-5-5, at: 2026-11-25T06:00:00Z }
---

# Pricing trim teammate report, phase 3

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Success number: pricing cards hold 12 lines of copy in place of the old 30-plus; the plan card's price numeral went from up to 76 px to 40 px at 1280.

## Progress

- Worktree `../Product-Marketing-final-assignment.d1-trim`, branch `d1-trim` from `iteration-a` (f7f3f1b).
- Rebuilt `#pricing` to the approved content. Moved the 02:09 stat into `#check` as a third proof number.
- Applied the two lead fixes received mid-task: pilot label and consulting text in the faux UI feedback.

## Final

### Files written, with commits
- `site/index.html`, `site/css/home.css`, `design-lab/shots/site/home-pricing-{light,dark}-{1280,375}.png`: 7f0d774 "Trim home pricing section and move 02:09 stat to proof".
- `site/index.html` (faux UI feedback quotes only): 8d0c7ae "Use consulting examples in home faux UI feedback".

### What changed
- Plan card: label "The plan", ₹149, "per employee per month, billed yearly, plus GST", "Same rate for every employee and firm size.", the four approved bullets, "Clients you invite to give feedback: free", "A 150-person firm pays ₹22,350 a month, plus GST." (150 x 149 = 22,350, checked).
- Pilot card: label "Start with a pilot" (lead fix 1; I did not use "Start with a 12-week pilot" because the next line already says "12 weeks, up to 40 people"), ₹25,000, "one time, plus GST", "12 weeks, up to 40 people", "Comes off your first annual bill if you sign. If not, you keep your data."
- Under the pilot card: a closed `<details>` "What a pilot measures" with the four scorecard items and "Results stay with your firm unless you agree to share them." The old line "Your firm agrees the targets before the pilot starts." was dropped to match the brief exactly.
- Removed: bills table, OKRs, spreadsheet import, new-joiner billing, the refund paragraph, the 2-col 7fr/5fr wall.
- "How we set the price" toggle cut from two paragraphs to three sentences: pilot cost (about 30 hours plus 12 weeks of running costs), plan rate for 40 people over 12 weeks is about ₹16,500 which is below that, and ₹149 is above cost to serve and below estimated value in the cautious case. The ₹8.6 lakh exit-cost figure and its caveat are gone from the page (still in `docs/pricing/`).
- Cards: equal 1fr 1fr pair, max width 880 px, padding 24 px (was 32), price numerals Newsreader 32 to 40 px for both, stacked below 760 px.
- Proof section: 02:09 with its exact qualifier and source line ("From a 2018 paper-and-pen pilot run by Sphyr's founder in four companies, self-reported (Sphyr whitepaper v0.3).") is now the third number. Grid is 1.15fr 1fr 1fr above 1100 px so "62% and 53%" stays on one line, 2 columns with 02:09 on its own row from 760 to 1100 px, 1 column below. Numeral size lowered from max 64 px to max 56 px to fit three across.
- Faux UI feedback (lead fix 2): member satellite "Your interview notes were clear and easy to build on. Tell us sooner when a client interview moves, so we can plan around it."; team feedback "The team stayed calm when the client changed the scope, and the final deck still went out on time." and "Flag gaps in the data earlier, especially when the client's team owns the numbers." I also replaced the member satellite quote because it used "handoff" and "research dependency", the same software tone.

### Checks (method: lead's server on 8826, Playwright isolated context)
- copy_scan: 275 strings, 0 unreviewed hits. copy_tells: 0 contrast sentences, 4 possible triads. Three are old (citation names, team names, "no hours or screen activity"); the new one is the approved bullet "Setup, training and support by our team", a real list of three services, kept verbatim.
- Sideways scroll: 0 at 390 and 375 in both themes (scrollWidth equals clientWidth; no element in the page past the right edge). Also 0 at 1000 and 1280.
- Smallest text in `#pricing`, `#check` and the edited faux UI: 12 px (fx label), all open toggles included.
- Links: 7 unique hrefs on the page, all relative, all resolve, anchors exist. 0 bad.
- Screenshots of `#pricing` in light and dark at 1280 and 375 in `design-lab/shots/site/` (nav hidden while shooting so it does not cover the section). Checked by eye: light 1280, dark 1280, dark 375 and an extra open-toggle shot at 375.
- Humanizer pass on all new strings; one edit (the price reasoning now says the plan amount "is less than that").

### Decisions and why
- Kept "What happens after you sign" and "Book a 20-minute call" in `#pricing`. The brief's remove list did not name them and they come from the packaging work. If "exactly this" meant they should go too, it is a two-line delete.
- Plan label "The plan" in place of "Sphyr, everything included": four bullets no longer list everything.
- No new colours, so contrast.mjs was not rerun.

### Rejected
- Leaving 02:09 as a 2x2 grid with a hole at 1280: looked unfinished.
- Equal three columns: "62% and 53%" wrapped to two lines (needs 335 px, column was 325 px).

### Open questions for the lead
- Should "What happens after you sign" stay inside the pricing section, move, or go?

### Not verified
- Idle frames and reduced motion: no animation added, not re-measured.
- No-flash theme load not retested (head untouched).
- Light 375 final shot not viewed after the retake (the dark 375 retake was, and they share layout).

## Addendum: round 2 (equal cards, price reasoning lines)

Success number: plan and pilot cards are both 402 px tall at 1280 (533 px each with the scorecard open).

### Commits
- ae685e0 "Make plan and pilot cards equal height, scorecard toggle inside pilot card": `site/index.html`, `site/css/home.css`, 6 shots in `design-lab/shots/site/` (`home-pricing-{light,dark}-{1280,375}.png`, `home-pricing-cards-{light,dark}-1280.png`).
- 171db5a "Add price reasoning lines to How we set the price": `site/index.html`.

### What changed
- `.price-pair` uses `align-items: stretch`. Each `.term` is a flex column. The plan card's bottom block (free line and example) and the pilot card's bottom block (the "What a pilot measures" toggle) are pushed down with `margin-top: auto`. The toggle moved inside the pilot card so the cards can match, and the `.side` wrapper is gone. Cards stack below 760 px as before.
- I did not shorten the plan card. The pilot card has about 100 px of space above its toggle at 1280. All plan card lines are approved copy, and the bottom hairlines sit within about 35 px of each other, so it looks balanced (see `home-pricing-cards-light-1280.png`). If the lead wants less space, the only cut left is the "Same rate for every employee and firm size." line.
- "How we set the price" now holds one short paragraph on the pilot fee and four lines:
  1. "₹149 is about a third of the cheapest standalone appraisal software we found. That is PerformYard, whose published price for firms of a few hundred people is about ₹464 a seat a month." (docs: ₹149 is 32% of ₹464, PerformYard $5 for firms of several hundred people. The date was dropped.)
  2. "At this rate, about 49 firms of 150 people cover our fixed costs." (docs: break-even 49 firms of 150 at ₹149.)
  3. "We think six fortnightly cycles is about the fewest that show partners a pattern they can use, so the pilot runs 12 weeks." ("We think" because the docs call it team reasoning, not a measured result.)
  4. "A price survey of heads of talent and partners will decide whether ₹149 changes. A change would apply only to firms that sign after it." (docs: validation_plan.md; changes apply to new firms only.)
- I dropped the earlier sentence "₹149 is above our cost to serve and below what Sphyr is worth" to keep the toggle short. The four new lines carry the reasoning.
- I wrote "appraisal software" instead of "review tool" because copy_scan flags `\breviews?\b` as social proof. That avoided editing the shared scanner.

### Checks
- copy_scan: 279 strings, 0 unreviewed hits. copy_tells: 0 contrast sentences, the same 4 possible triads as before, none new.
- Sideways scroll 0 at 375 and 390, both themes, toggles open and closed. Smallest text in `#pricing` is 15 px.
- Card heights: 402/402 closed and 533/533 open at 1280. At 375 they stack at their own heights (586 and 597 with the toggle open).
- Shots checked by eye: cards light 1280, section open light 1280, light 375. Dark 1280 and dark 375 were taken the same way.
- Tooling note: element screenshots at a short viewport came out offset on the long page, so the 375 shots use a 3200 px tall viewport.

### Access-date rule (lead, round 2)
- Searched `site/index.html` for "accessed", "read on", "we read", ISO dates, day-month-year dates, "as of" and "checked on". No visible text matches. The PerformYard line has no date. The citations read "Scullen, Mount and Goff, 2000.", "Gallup, across industries worldwide." and the 02:09 source "From a 2018 paper-and-pen pilot ... (Sphyr whitepaper v0.3)". The years there are when the research was done, not access dates.
- One match is not visible text: the HTML comment on line 36, `<!-- Canonical nav (2026-11-25, replaces the 3-item nav) ... -->`, from the shared nav block. It shows only in page source. I left it alone because the block is canonical across pages. Sitecss or the lead should decide whether to strip that date from every page.
