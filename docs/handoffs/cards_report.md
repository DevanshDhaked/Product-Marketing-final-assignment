---
type: Handoff
title: "Pricing cards redesign teammate report, phase 3"
description: "Pricing cards redesigned with stageshow rules: plan as hero, shared rows, one action each, aligned toggle."
tags: [handoff, cards]
generated: { by: claude-code/opus-5-5, at: 2026-11-25T07:00:00Z }
---

# Pricing cards redesign teammate report, phase 3

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Design read
1. Reading this as: a pricing block on a calm B2B marketing page for heads of talent and partners; restraint first, no new colours or shadows, so weight comes from size, ground and structure.
2. One hero: the plan card takes 2 of 3 columns on the plain surface with the strong border; the pilot is the supporting tile on the sunk warm ground (existing token) with the light border.
3. One frame: both cards share radius, padding and a subgrid of five rows (label, price, sub line, body, action row), so the numerals, sub lines and action rows sit on the same lines and equal height comes from the shared tracks, not stretched space.
4. Price line: numeral on its own line, unit phrases under it as unbreakable spans ("per employee per month," / "billed yearly, plus GST"); the action row is pinned last with a hairline above it, plan primary "See the 2-minute walkthrough", pilot secondary "Book a 20-minute call" opening #call-note; the scorecard toggle moves into the pilot body.
5. Cards and the "How we set the price" toggle share the full .wrap width with the heading; the toggle's answer text stays at reading measure; phones stack plan first.

## Final

### Files written, with commits (branch d1-cards)
- `site/index.html` (#pricing only) and `site/css/home.css` (pricing rules only): 0e34fab "Redesign pricing cards: plan as hero, shared subgrid rows, one action per card, full-width price toggle".
- Follow-up fix, `site/css/home.css` and retaken shots: b6f532f "Fix pricing open states: restore list and toggle spacing, release shared rows while scorecard is open, centre closed toggle".
- `design-lab/shots/site/pricing-cards-{light,dark}-{1280,375}.png`: dad73b1, retaken in b6f532f. Shot of the whole #pricing section, nav hidden, isolated Playwright contexts, 3200 px tall viewport. Checked by eye: light 1280, dark 1280, light 375. Dark 375 taken the same way, not viewed.

### What changed
- Plan card is the hero: 2fr of a 2fr/1fr grid, plain surface, strong border, primary button "See the 2-minute walkthrough" (demo.html). Pilot is the supporting tile: surface-sunk ground, light border, secondary button "Book a 20-minute call" (popovertarget="call-note").
- Both cards are CSS subgrids over six shared rows: label, price, sub line, main, lower, action. Numerals, sub lines, both hairlines and both buttons sit on the same lines. Fallback for no subgrid: flex column with the action row pushed down.
- Plan lower row: free line and example. Pilot lower row: the "What a pilot measures" toggle (moved out of the card foot into the list area).
- Price line: numeral on its own line; unit under it in unbreakable phrases ("per employee per month," / "billed yearly, plus GST"). Measured: every phrase span renders on 1 line at 1280, 375 and 390.
- Plan inclusions go to two columns at small size from 1100 px up, so the plan's main row matches the pilot's terms.
- Cards and the "How we set the price" toggle share the full .wrap width: left 97, right 1169 at 1280, same as the h2 left edge (97). The toggle answer stays at 68ch.
- No copy changed. No new colours, no shadows.

### Numbers (method: Playwright, lead's server on 8828)
- Empty space under the shorter content per row at 1280 and 1440: main rows 2 px both cards. Lower row: the pilot toggle is centred between its two hairlines (23 px above, 22 px below); plan 2 px. Before: one band of about 84 px in the pilot. At 1100: 30 px under the plan list (list wraps).
- Open states (checked by eye, light 1280): with the scorecard open, the cards drop the shared rows above 760 px and each takes its own height, so the plan card keeps its natural height and the pilot grows (plan 468 px, pilot 778 px). Closing restores equal bottoms (measured). Open lists keep their spacing: 12 px above the price-reason list, 16 px under the scorecard summary, 12 px above "Results stay with your firm".
- Card bottoms equal at 1280 closed (1326 and 1326), and again after open then close.
- Sideways scroll: 0 at 1280, 390 and 375, both themes.
- Smallest text in #pricing: 15 px. Buttons 44 px tall, one line.
- Contrast on the pilot's sunk ground (existing tokens): text-muted 5.66 light, 6.44 dark; text 14.53 and 12.66; on-positive-soft 7.04 and 10.52.
- Links in the section resolve (demo.html, assets/icons.svg, #call-note present). copy_scan: 282 strings, 0 unreviewed hits (re-run after b6f532f). copy_tells: 0 contrast sentences, 4 possible triads, the same 4 as iteration-a before this change (none from this section's new strings).
- Keyboard (1280 and 375): tab order plan button, scorecard toggle, call button, price toggle; Enter opens both toggles and the call note; Escape closes the note and focus returns to the call button; focus ring present on all four.

### Decisions and why
- Mid-run mistake caught by review: my first spacing resets zeroed the global `.incl` margin and the scorecard paragraph margin, so the open lists sat flush. Fixed by scoping the resets to the cards (b6f532f).
- Lead direction mid-run: smoke checks only (copy scans, links, no sideways scroll at 375, one shot per theme at 1280 and 375). The earlier contrast and keyboard numbers stay as recorded; I did not re-run them after b6f532f.
- Subgrid rows instead of stretched flex columns: equal height by structure, per the brief; space can only appear inside a row, never as one band.
- Split body into main and lower rows: with one body row the pilot had an 84 px void; two rows spread the slack and align the hairlines across cards.
- Renamed the lower row class to `.lower` after finding `.foot` is the site footer class in base.css (it added 49 px padding and removed the scorecard bullets).
- Pilot uses the stronger hairline (border-strong) because the light border is faint on the sunk ground.

### Rejected
- Keeping the subgrid while the scorecard is open: the open list pushed a void of about 270 px into the plan card.
- 7:5 split: pilot terms wrap to 2 lines and the void stayed near 80 px.
- Unit beside the numeral: the pilot's unit fits beside, the plan's does not, so the price rows would differ between cards.
- Example line in the plan's action row: two items in the action row, against "one action each".

### Open questions for the lead
1. Two primary buttons are in view on desktop: the sticky nav's "See the 2-minute walkthrough" (btn-primary, line 52) and the plan card's primary. Same label and target. The brief asks for the plan's primary; the nav is outside my section. Options: make the nav button secondary on scroll, or accept.
2. "Book a 20-minute call" now appears in the pilot card and again as the text link at the end of #pricing (`.call`, unchanged) and in the footer. Same label and intent. I kept the end link because the content is approved; removing it is one line if you want.
3. Resolved: the pilot toggle is centred in its lower row, so the slack is split above and below it instead of sitting under it as one band.

### Not verified
- Dark 375 shot not viewed by eye. Open state at 375 not viewed (stacked cards, same spacing rules). Safari and Firefox not tested (subgrid is supported in both; the fallback path not rendered).
- Reduced motion and idle frames not re-run: this change adds no motion.
- Widths between 761 and 1099 px only checked at 1024 (rows aligned, no sideways scroll), not by eye.
