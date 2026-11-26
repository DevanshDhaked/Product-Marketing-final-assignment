---
type: Handoff
title: "Home polish report"
description: "Design-review fixes on home: hero fits the first screen with a 2-line H1 at full size, labelled problem rows, primary pilot button, phone fixes, anchored call popover and the call in the phone menu."
tags: [handoff, phome]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T15:50:00Z }
---

# Home polish report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Skills loaded before any markup: `design-taste-frontend`, `stageshow` (no new faux UI here, so stageshow only informed the frame trims in item 5).

## Plan

Files: `site/index.html`, `site/css/home.css`, `site/css/base.css`. Nothing else.

1. Hero (blocker): H1 `em` back to its own line (v2 `display: block`), size from the v2 cqi clamp, tuned so both lines fit the left column at 1280. Pilot line shortened to the brief's one-line wording. Measure the right column; if it still pushes the figure below y 345, put the button and walkthrough link in one row and keep the pilot line under the button group.
2. Pilot card button `btn-secondary` to `btn-primary`. Both cards' `.lower` and `.act` dividers on `--border`.
3. `.manifesto`: `text-wrap: balance`.
4. Problem: `ul.rows.lines` back to `dl.rows` (base labelled-row grid), labels Staffing, Recency, Rolled off, Chasing forms, Attrition; the five sentences verbatim. Body colour `--text` as v2 `.scenes dd`.
5. 375: feedback frame shows only the active step on one-column layouts (shared cell kept at desktop); Team Insights third KPI full width under the two (base.css); circle `core-label` shown at a smaller size on phones, side labels pulled inside the viewBox (home.css override of motif.css, which I do not own).
6. `.groups` max-width removed; `#how .duo` top-aligned; captions `text-wrap: pretty`.
7. `.note-pop` anchored under the nav call button: fixed, top right below the 64 px header, right edge on the wrap's content edge; phones full width minus gutters near the top.
8. Menu: last item a `button` with `popovertarget="call-note"`, styled like the menu links.

Open questions: none blocking. Item 4 uses bold labels before sentences, which the common copy rules ban; the brief asks for it explicitly, so the brief wins.

## Progress

- Hero, 1280x800: figure top 340 px, caption and Play again bottom 797 px (v2: 342 and 798). H1 two lines at 38.6 px. Sample: one load each at 1280 light and dark, one dev check at 1000 (H1 still two lines at 34.3 px; button, pilot line and link stack in source order there).
- Feedback frame at 375: 19 px from the last item to the frame cut for each of the three answers (was 146 px for "Was good"; all three steps shared one 388 px cell).
- Circle at 375: "Consultant" at 24 units (about 9 px) sits inside the core (x 162 to 213 inside 160 to 215). Side labels: Peers x 27, Juniors right edge x 359.
- Call note on demo at 1280: x 756 to 1176, y 72 to 233, under the nav button (927 to 1110, bottom 50).
- Phone Menu: five items, each 44 px tall, 17 px / 500, same colour.

## Menu markup

Last `<li>` of `#nav-menu > ul`, after Deliverables:

```html
      <li><button type="button" popovertarget="call-note">Book a 20-minute call</button></li>
```

The styling and the "hide the Menu while the note is open" rule are in `base.css`, so other pages need only this markup.

## Compared with v2

- **Hero** (`v2_hero_1280l.png` vs `phome_hero_1280l.png`): the fold now matches v2, figure 340 vs 342 and caption bottom 797 vs 798. The H1 is smaller than v2's (38.6 px vs 58 px).
- **Calibration rows** (`dreview/v2_index_1280l_01.png`): the same `.rows` grid, with the label column on the left and the answer at x 388. The v2 labels wrapped to two lines; the new 1 to 3 word labels fit on one line, so each row is a single line at 1280. v2's lead paragraph is not restored (not in the brief).
- **Feedback frame at 375** (`dreview/v2_index_375l_05.png`): v2 left about 90 px of empty card under "Resilient". Mine leaves 19 px, then the frame cut.
- **Team Insights at 375** (`dreview/v2_index_375l_08.png`): v2 showed only Team score and Participation. Mine adds Edit requests as a full-width third card.

## Not done (out of scope)
- The close section's pilot line wording (see open questions).
- The desktop feedback frame strip under "Resilient" at 1280 (visible in `phome_how_1280l/d.png`) and the Insights "Strongest signal" card on phones.
- Other review items (demo, linkedin, ad, deliverables, propaganda) belong to other teammates.

## Final

Score: 8 of 8 review items done. Hero figure top is at 340 px against a 345 target.

Files written, all on `d1-phome`:
- `788e4f4` Hero (`site/index.html`, `site/css/home.css`).
- `ddb11fa` Price cards: pilot button is `btn-primary`, and both cards use `--border` for `.lower` and `.act` (`index.html`, `home.css`).
- `7f53bfb` Closing line: `text-wrap: balance`. The last line is now "manager's memory." (`home.css`).
- `d434eec` Calibration rows: `dl.rows.scenes` with the labels Staffing, Recency, Rolled off, Chasing forms and Attrition. The sentences are verbatim, each runs the full answer column, and `pretty` wrapping applies on phones (`index.html`, `home.css`).
- `a65457e` Team Insights: the third KPI card is full width on phones instead of hidden (`base.css`).
- `c48157a` Phone frames and layout nits (`home.css`).
- `2f95dc6` Menu item (`index.html`, `base.css`).
- `6f70d74` `.note-pop` anchored under the nav (`base.css`).

Key decisions and why:
- **Hero columns are now `1fr 1fr` with a 48 px gap (v2 used `1.45fr 1fr` with 64 px).** Lede, button, pilot line and link only fit v2's 181 px column height if the button and link share a row. That row needs about 482 px, and the one-line pilot line needs 497 px at 13 px. The H1 size still uses v2's cqi clamp form; the floor is lowered to 1.875rem so it stays at two lines down to the 900 px breakpoint.
- **The hero pilot line is 13 px (`--fs-caption`).** At 15 px it wraps and pushes Play again below 800 px.
- **A container query on `.hero-side` stacks the hero buttons when the column is under 500 px.** It falls back to source order (button, pilot line, link), so on narrow columns the pilot line sits right under the main button.
- **The one-step feedback card applies at 900 px and below (the one-column breakpoint).** Desktop keeps the shared cell so the text beside the card never moves.
- **The circle labels are overridden in `home.css` with attribute selectors (`[text-anchor]`).** `motif.css` is not mine, and no markup change was needed.
- **The call note uses fixed `inset` with `%` values, not anchor positioning.** The nav button is hidden under 760 px, and `%` ignores scrollbar width.
- **`body:has(#call-note:popover-open) .nav-menu { visibility: hidden }`.** The note opens as a nested popover, so the Menu stays open under it and showed through. When the note closes, the Menu reappears. `nav.js` only closes the Menu on link clicks, and I do not own it.
- **`#how .text-col h2` is trimmed to cap height,** so the heading glyphs, not the line box, meet the frame top.

Approaches rejected:
- Keep the 1.45:1 hero and only shrink the H1. The right column alone (4-line lede plus button) is already about 180 px, so the pilot line and link could not fit.
- `text-wrap: pretty` on captions. It left "cards." alone in Chrome; `balance` fixed it.
- Splitting `home.css` hunks for items 5 and 6. They are in one commit, and `base.css` (Team KPI) is in its own.

Open questions for the lead:
- **The page now has two pilot-line wordings.** The hero uses the brief's short one. The close section keeps "Start with a 12-week pilot for up to 40 people. ₹25,000 plus GST, taken off your first annual bill if you sign." Should the close match? It was out of scope, so I left it.
- **The H1 is 38.6 px at 1280, against 58 px in v2.** That was the price of two lines plus the four right-column items in the first screen.
- **On phones the H1 is 4 lines, because the `em` is on its own line again (v2 behaviour).** The brief only set the line count for 1280.
- **The labelled rows use bold labels before sentences, which the common copy rules ban.** I followed the brief. `copy_tells` did not flag them.
- **The centre "Consultant" label renders at about 9 px on phones (24 viewBox units at a scale of 0.38).** A `home.css` comment treats 11 px as the floor for figure labels. At 11 px (29 units) the word is wider than the 55 px core and would run onto the strands. Smaller and inside the core is my reading of the brief. Lead to decide.

What I did not verify:
- Safari and Firefox (Chromium only). `text-box` and `:has()` need recent engines; without `text-box`, the hero and How it works headings sit a few px lower.
- The circle with motion on at 375 (screenshots used reduced motion).
- The desktop feedback frame's empty strip under "Resilient" at 1280. It was not in the brief, and it is unchanged.
- The Insights "Strongest signal" card is still hidden on phones. The review mentioned it, but the brief lists only Edit requests.

Checks: `copy_scan` found 0 unreviewed hits in 239 strings. `copy_tells` found 1 contrast (the page's existing closing line) and 2 triads that are real lists (both existing). All local links resolve. Scroll width equals the viewport at 1280 light, 1280 dark and 375 on index, and at 375 on demo and linkedin. Humanizer pass on the new strings found no changes.

Screenshots in `.swarm/tmp/phome/`:
- `phome_{hero,problem,how,say,pricing,call}_{1280l,1280d,375l}.png`
- `v2_hero_1280l.png`
- `callnote_demo_1280l.png`
- `menu_375l.png`, `menu_callnote_375l.png`
- `insights_cap_1280l.png`
- `fb_375l.png`, `team_375l.png`

I opened all 25 and found no defect from these changes. The section screenshots of 375 How it works, Who gets a say, Pricing and Problem show the sticky nav over the section top. That comes from element screenshots, not from the page. Browser closed. Idle.

### Addendum to Final: second hero pass (lead request)

Score: H1 is 50.4 px on 2 lines at 1280 (was 38.6). The fold still holds: figure top 337 px and caption bottom 794 px at 1280x800 (v2: 342 and 798).

- Commit `5668801` (`site/index.html`, `site/css/home.css`).
- **Layout.** Grid `7fr 4fr` with areas `"h1 side" "lede side"`. The lede moved out of `.hero-side` in the markup and now sits under the H1 in the wide left column (662 px). The actions (button, pilot line, walkthrough link) stack in the right column (378 px), bottom-aligned with the lede's last line. The H1 size uses the same cqi clamp form (`4.7cqi`). At 1000 px it is 44.7 px, still on 2 lines.
- **Spacing.** The fold needed about 28 px back, so the hero top padding and the gap above the figure each drop one step: `--s-7` (48) to `--s-6` (32). That is a spacing change, not a type change. The H1 now starts 32 px below the header, against 48 before.
- **Rejected options:**
  - 7 of 12 columns with the lede in the right column: a 5-line lede plus the actions in about 380 px is about 280 px tall, so the fold breaks.
  - H1 on its own full-width row above a lede-plus-actions row: about 290 px of copy, so the fold breaks by about 100 px.
- **Phones (375).** Order is H1, lede, button, pilot line, link. The H1 is 36 px on 4 lines, as before this pass. No sideways scroll at 375, 1000 or 1280.
- **New screenshots:** `phome2_hero_1280l.png`, `phome2_hero_1280d.png`, `phome2_hero_375l.png`, all opened and checked.
- **Not verified:** the motion-on ribbon at the new figure position (screenshots used reduced motion), and Safari and Firefox.
- **Open question for the lead:** the right-hand actions now sit lower than the H1, level with the lede, so the button is about 170 px below the H1 top. If the lead prefers the button level with the H1 top, change `align-self: end` to `start` on `.hero-side` in `home.css`. The height and the fold do not change.

Browser closed. Idle.
