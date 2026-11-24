---
type: Handoff
title: "Favicon and row heights report"
description: "Full-colour favicon on every page and equal row heights where answers are close; long lists keep natural height."
tags: [handoff, polish]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T21:55:49Z }
---

# Favicon and row heights report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Diagnosis

### Job 1: favicon shows the old grey sphere
- Root cause: `site/assets/favicon.svg`, `favicon.ico` and `apple-touch-icon.png` were built from the mono mark (near-white ribbons on a #1F1C18 ink tile) in commit ef8a34c. That was a documented choice: `docs/design/design_system.md:172` and `docs/design/ribbon_motif.md:39` say "mono ... favicon".
- `index`, `demo`, `_template` and `_motif` link that mono set. `ad`, `deliverables`, `linkedin` and `propaganda` link `assets/sphyr-logo.svg` (full colour) only, with no .ico and no apple-touch icon.
- There is no `site/favicon.ico`, so the browser's default `/favicon.ico` request returns 404.
- Same filenames on change means a cached mono icon survives; hrefs need a version query.

### Job 2: uneven row heights
- Root cause: `.rows > div` (base.css:254) is a grid per row with `padding-block` only, so each row is as tall as its longest cell. Answers run 2 to 4 lines (dd capped at 60ch = 622 px at 1280), so rows differ.
- Measured at 1280 (row heights, px): home scenes 102,131,131,131; home "after you sign" 130,131,103,103,158,103; ad "Why this ad" 184,158,103,131; hub index 174,174,174,201; LinkedIn notes dl 79,79,52 / 79,52,79 / 79,79,52; propaganda channel table rows 50,50,50,50,50,74; propaganda shift bridge 48,48,24,48.
- A text-width fix only holds at one viewport width; a shared row track (grid-auto-rows: 1fr) holds at every desktop width.

### Baseline copy_scan (before)
index 0 unreviewed / 5 denials; demo 2 unreviewed / 1; deliverables 0 / 0; propaganda 0 / 1; linkedin 0 / 1; ad 0 / 3.

## Job 1: favicon (done, ca4cb95)
- `favicon.svg` is now a copy of `sphyr-logo.svg` (full colour, transparent). `favicon.ico` (16, 32, 48) and `apple-touch-icon.png` (180) regenerated from the logo with rsvg-convert and ImageMagick. The apple icon sits on the light paper colour #FAF8F4 because iOS fills transparent pixels with black.
- New `site/favicon.ico` (copy) for the browser's default request.
- All six pages plus `_template.html` and `_motif.html` now carry the same three lines: ico, svg, apple-touch, each with `?v=2` so cached mono icons are not reused.
- Checked: on each of the six pages, read the icon `<link>` hrefs and fetched each with `cache: 'reload'`: all 200 with the right content type; the SVG has no #1F1C18 ink tile. `/favicon.ico` returns 200 (15086 bytes). I did not see a rendered browser tab (headless Chromium does not show one).
- There is no web manifest in `site/` (no `<link rel="manifest">`, no manifest file), so nothing to update there.
- The user may need a hard refresh (or to close and reopen the tab) because browsers cache favicons hard.

## Job 2: row heights (done, 6fbdb63)
Rules added (CSS only, no words changed):
- `base.css`: `@media (min-width: 641px) { .rows { display: grid; grid-auto-rows: 1fr; } }`. Covers home scenes, home "What happens after you sign" and the ad page "Why this ad" rows.
- `deliverables.css`: same pattern for `.hub-index` at 641 px and up, plus `.doc .hub-index > li + li { margin-top: 0 }` against the `.doc li + li` trap (measured margin 0 on every entry).
- `posts.css`: same pattern for `.post-note dl` at 521 px and up (matches its existing phone breakpoint).
- `deliverables.css`: audience map columns share four subgrid rows (title, job, belief, name) when the figure is wider than 560 px, so the names line up.

Row heights, px, before then after (1280):
| List | Before | After |
|---|---|---|
| Home scenes | 102,131,131,131 | 131 x4 |
| Home after you sign | 130,131,103,103,158,103 | 158 x6 |
| Ad "Why this ad" | 184,158,103,131 | 184 x4 |
| Hub index | 174,174,174,201 | 201 x4 |
| LinkedIn notes (3 lists) | 79,79,52 / 79,52,79 / 79,79,52 | 79 x3 each |
| Audience map name line top (y, px) | 1115,1115,1142 | 1142,1142,1142 |

Also equal at 1024 and 800. Phones (375) keep natural heights. Sideways scroll 0 at 375, 800, 1024 and 1280 on index, ad, deliverables, linkedin and propaganda, and at 375 and 1280 on demo.
Screenshots, dark, 1280 (each looked at): `design-lab/shots/site/polish-home-scenes-dark-1280.png`, `polish-home-after-dark-1280.png`, `polish-ad-rows-dark-1280.png`, `polish-hub-dark-1280.png`, `polish-linkedin-note-dark-1280.png`, `polish-prop-audience-dark-1280.png`. Light theme checked on home scenes (131 x4, looks right); the change is layout only, with no colours.

Checked and left alone, with reasons:
- Propaganda channel table (50 x5, 74): the last row is taller only because "Plain QR link" sits under its tag. That is a note, not wrapping; forcing every row to 74 would look emptier.
- Propaganda shift bridge (48,48,24,48): a numbered list with no row lines, so it does not read as uneven rows.
- Propaganda summary card: already a shared two-column grid; rows line up.
- Price cards: already share rows through subgrid.
- `ul.incl` bullets and the faux-UI `fx-*` lists: plain bullet lists and product mockups, not row lists.
- Demo step 1 choices (`wt-pick-body` 42, 82): two choices whose descriptions differ in length inside one control; not a row list with dividers.
- copy_scan after: identical to the baseline on all six pages.

## Final
1. Files written, with commits
   - ca4cb95: `site/assets/favicon.svg`, `site/assets/favicon.ico`, `site/assets/apple-touch-icon.png`, new `site/favicon.ico`, icon links in `site/index.html`, `demo.html`, `deliverables.html`, `propaganda.html`, `linkedin.html`, `ad.html`, `_template.html`, `_motif.html`.
   - 6fbdb63: `site/css/base.css`, `site/css/deliverables.css`, `site/css/posts.css`, six `design-lab/shots/site/polish-*.png`.
2. Key findings
   - The grey icon was the documented mono favicon (`docs/design/design_system.md:172`, `docs/design/ribbon_motif.md:39`, commit ef8a34c), linked on index and demo. The other four pages already used the colour logo but had no .ico, and there was no root `/favicon.ico`.
   - Uneven rows came from each `.rows > div` sizing to its own text (dd capped at 60ch). A shared `grid-auto-rows: 1fr` track holds at every desktop width; matching line counts by text width would only hold at one width.
3. Decisions and why
   - Kept the asset filenames and added `?v=2` so every reference updates and caches break.
   - Kept the 60ch answer width. Lifting it to the full column would cut the shared height (home "after you sign" 158 to 131) but makes lines about 80 characters long.
   - Applied equal heights only at 641 px and up (521 px for LinkedIn notes, matching their existing breakpoints). Phones keep natural heights, as the brief allows.
4. Rejected approaches
   - Matching line counts by text width: it breaks at other widths, and the "after you sign" list stays uneven anyway.
   - A fixed `tr` height on the channel table: hides the reason the row is taller.
   - `min-height` in px: it breaks as soon as copy changes.
5. Open questions
   - Docs: `design_system.md:172` and `ribbon_motif.md:39` still say the favicon uses the mono mark. The lead should add a dated addendum (full-colour favicon, user decision 2026-11-25). I did not edit docs (outside the brief's `site/` scope).
   - Equal heights leave clear space under short answers in three lists: home "What happens after you sign" (158 px rows, shortest answer 2 lines, 1280), ad "Why this ad" (184 px rows; "Journey stage" is 2 lines with about 100 px empty below, 1280), LinkedIn notes at 1024 (134 px rows; "Looking for answers." is one line). If the user finds this too airy, one option for all three is to lift the 60ch answer cap (home list would drop to 131 px at 1280). I did not change it: the brief asked for equal heights.
6. Not verified
   - The rendered favicon in a real browser tab (headless); checked by link hrefs and fetches only.
   - Safari and Firefox (Chromium only). The audience-map subgrid has an `@supports` guard; without subgrid it falls back to the old layout.
   - Light theme screenshots for every changed list (looked at one; the change has no colour).

## Not done (out of scope)
- Docs addendum for the favicon change (see open questions).
- Home hero label, "No AI scores" line and sample-screen words: not touched (the clarity teammate owns them).

### Final addendum (2026-11-25, user decision on Job 2)
- Commit 84592ce: `site/css/base.css`, `site/css/home.css`, retaken `design-lab/shots/site/polish-home-after-dark-1280.png` and `polish-ad-rows-dark-1280.png`.
- User decision: equal row heights stay only where answers differ by about one line: home "What goes wrong" scenes, hub index, LinkedIn notes, audience map. The ad page "Why this ad" rows and the home "What happens after you sign" list go back to natural height.
- Change: removed the shared `.rows` equal-height rule from `base.css` and added the same rule to `home.css` scoped to `.scenes`. `.scenes` was the only other `.rows` list on the site, so an opt-in page rule is simpler than excluding two lists in shared CSS. No word changes.
- Measured at 1280: ad rows 184,158,103,131 (natural, same as before Job 2); "after you sign" 130,131,103,103,158,103 (natural); scenes still 131 x4. At 375 nothing changed and sideways scroll is 0 on both pages. copy_scan on index and ad matches the baseline.
- Both retaken screenshots looked at: natural heights, dividers and alignment intact.
- This replaces the earlier open question about airy rows. Hub index, LinkedIn notes and audience map are unchanged from 6fbdb63.
