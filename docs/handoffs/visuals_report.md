---
type: Handoff
title: "Visuals teammate report"
description: "Four HTML and CSS visuals on the propaganda page: audience map, belief shift, channel table and campaign flow."
tags: [handoff, visuals]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T20:59:07Z }
---

# Visuals teammate report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Branch `d1-visuals` from `iteration-a` (bd7a7f3). Worktree `Product-Marketing-final-assignment.d1-visuals`.

## Design read

Baseline: 705 words inside `<main>` (summary card, contents and body; script in scratchpad strips tags). Budget: at or below 705 after the change. copy_scan 0 unreviewed hits; copy_tells 0 contrasts, 8 possible triads (most are lists of names or channels).

Approach: all four visuals are semantic HTML and CSS, not SVG. Reason: three of them hold links or table data that must stay readable and keyboard reachable, and HTML reflows to a phone column without shrinking text. Arrows come from the existing `assets/icons.svg` (`i-arrow-right`), turned down on phones. Tokens only from `base.css`; brand green is the one accent (the "belief we want" side, the primary person, the path through the flow). No boxes inside boxes: each figure is one hairline-ruled surface or none, rows split by hairlines.

1. Audience map (`#audience`): three columns (one per person), each with role, what they do in the sale (proposes, signs, decides if it works), an illustrative persona name and what each must believe, as a short quote. Head of talent column gets the brand rule as primary. The paragraph shrinks to one sentence.
2. Belief shift (`#belief`): today (muted) on the left, the belief we want (brand) on the right, the four tactics as a numbered column between them with arrows. Phones: stacked top to bottom with down arrows. The Scullen citation sentence stays in prose.
3. Channel table (`#tactics`): a real `<table>`: channel, cost, tracks anyone, journey stage, what it carries. Six rows, five free and the one paid standee. Caption answers the "no money, not creepy" challenge. Phones: each row becomes a stacked block with labels from `data-label`, so nothing scrolls sideways.
4. Campaign flow (`#response`): an `<ol>` strip, left to right on desktop, top to bottom on phones. Nodes: week 1 post 1 and the standee, week 3 post 2, the walkthrough, week 5 post 3, the 20-minute call, the 12-week pilot. Each node links (linkedin.html#p1-h and so on, ad.html, demo.html, the call-note popover, index.html#pricing). Stage word above each node.

Checks per the lead's reduced list: copy_scan, copy_tells, links resolve, no sideways scroll at 375, one shot per theme at 1280 and one at 375 per visual.

## Final

### Files written, with commits (branch d1-visuals)
- `site/propaganda.html`, `site/css/deliverables.css` (propaganda.js unchanged; the sticky contents still work).
- 1fbdb03 audience map; ecf2384 belief shift; bf1dd80 channel table; 21268b6 campaign flow; cc0fcc5 prose trims; 6bcd9c1 phone fix for the table note; 4cfb96c screenshots; 4e10f6f summary card belief wording matches the visual, curly quotes across the page.
- `design-lab/shots/site/propaganda-visual-{audience,belief,channels,flow}-{light-1280,dark-1280,light-375}.png` (12 files).

### Checks (lead's reduced list)
- Words inside `<main>`: 705 before, 703 after (tag-stripped count, includes the summary card and contents list).
- copy_scan: 1 unreviewed hit, `Tracks anyone?` (surveillance rule). It is the column header the brief asked for and is a denial. Lead: add it to ALLOWED in `design-lab/copy_scan.py` (shared file, I did not edit it) or tell me to rename the column.
- copy_tells: 0 contrasts, 4 possible triads, all false positives (citation authors, team names, a two-item list, text joined across table cells). "never partners" appears once (summary card).
- Links: every relative href and anchor on the page resolves (script check, 0 bad).
- Sideways scroll at 375: scrollWidth 360 (no overflow). Smallest text in the visuals 13 px.
- Screenshots checked by eye in both themes at 1280 and light at 375.

### Key insights and findings
- Playwright MCP writes screenshots only under the main repo root (`.playwright-mcp/`). Save there, then move into the worktree.
- The lead's server on 8829 serves stale CSS after edits. Run `fetch(url, {cache: 'reload'})` for the CSS and page, then reload.
- copy_scan's surveillance rule matches any form of "track", including denials.
- `base.css` has `.doc li + li` and `.doc p + p` margins that leak into figures inside `.doc`. Figure CSS needs selectors of equal specificity (for example `.aud li + li`).
- Container queries cannot style the container itself. A grid that must reflow by figure width needs an inner wrapper (`.shift-grid`).
- Facts used: posts two weeks apart and the standee in the same weeks as post 1 (`site/linkedin.html`); journey stage names (`docs/strategy/journey_map.md`); channel list and no-tracking rules (`docs/strategy/channel_plan.md`); persona roles (`docs/strategy/deliverable_map.md`, Meera is the senior consultant).

### Key decisions
- All four visuals are semantic HTML and CSS (lists, a real table, an ordered list of links), not SVG, so links stay keyboard reachable and text reflows on phones. Layout switches by container queries on each figure, so the 901 to 1100 px range (narrow body column) also gets the stacked layout.
- Figures run wider than the 68ch text measure; paragraphs keep the measure.
- Brand green marks the subject of each visual: the head of talent, the belief we want, the path in the flow. Cost and tracking answers are small tags (green free/no, warm paid).
- To hold the word budget, prose the visuals now carry was cut: audience personas moved into the map, the belief from/to and tactics moved into the shift, the channel list moved into the table, the sequence and pilot terms moved into the flow. The summary card rows stay (decision log) but are shorter.
- Flow uses weeks only (post 1 week 1, post 2 week 3, post 3 week 5, two weeks apart per linkedin.html); the call node opens the existing `#call-note` popover; the pilot links to `index.html#pricing`.

### Rejected
- Inline SVG diagrams: would need role="img" and hide the flow links from keyboard users.
- Ellipsis on long flow time labels: replaced with short labels ("From week 3", "When ready").

### Open questions
- Copy_scan ALLOWED entry for `Tracks anyone?` (above).
- The table "Carries" column for HR meets and articles says "The core line" and "The rater research" because those channels carry no graded deliverable. Confirm wording.
- Optional: the table caption could name the course challenge outright; skipped for lack of word budget (2 words of slack).

### Not verified
- Contrast scripts, reduced motion, idle frames, 390 px (skipped per lead).
- Widths between 641 and 900 px by eye.
- Keyboard pass through the flow links (they are plain links and one button, not tested by hand).
- Humanizer pass done by me on the new strings (two fixes: "Blame the gap on rotation and fading memory", "Try it alone"); no second reader.
