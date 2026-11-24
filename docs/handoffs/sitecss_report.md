---
type: Handoff
title: "Site CSS teammate report, phase 2"
description: "Shared site files: base CSS, motif, nav, template, favicons and OG image, with browser check results and the page-builder catalogue."
tags: [handoff, sitecss]
generated: { by: claude-code/opus-5-5, at: 2026-11-25T03:00:00Z }
---

# Site CSS teammate report, phase 2

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Worktree: `Product-Marketing-final-assignment.d1-sitecss`, branch `d1-sitecss` from `iteration-a` at 910ca83. Nothing written yet.

## Plan

### Success number
`site/_template.html` renders in both themes at 1280 and 375 with 0 contrast failures, 0 console errors, 0 sideways scroll and 0 idle frames after load.

### What I read
`docs/index.md`, `docs/decisions/decision_log.md` (all), `docs/handoffs/design_report.md` (gate 1b report and Final), all lab CSS and JS, `design-lab/snippets/*`, the hero SVG in `design-lab/home.html`, `contrast.mjs` inputs. Old `site/` pages: 9 HTML files link `site/style.css`; README does not.

### Files

1. `site/css/base.css`. One file, lab load order kept so overrides still win:
   - tokens (`design-lab/tokens.css`, both themes), with `@font-face` paths changed from `fonts/` to `../fonts/` (the only 3 `url()` uses in the lab CSS). Head preloads stay `fonts/...` from the page, so both resolve to the same URL.
   - components (`components.css`): nav, theme toggle, buttons, sections, the 5 layout families, cards, table, quote, stat, chips, notes and `.sample-label`, form, accordion. The lab `.footer` block (old 3-column) is dropped; the canonical `.foot` from `home.css` replaces it.
   - faux UI (`faux-ui.css`) in full, with the prototype palette. Home and walkthrough both need it.
   - shared parts of `home.css`: `.foot`, `.foot-grid`, `.note-pop`, `.linkbtn`, `.go`, `.lede`, `.src-note`, and the price and pilot block (`.terms`, `.term`, `.includes`, `.rows.when`), which I read as the brief's "price block". Also the stat-number style shared by `.proof .v` and `.proof-one .v`, renamed `.bignum` (one rule instead of two copies).
   - stays behind for the home builder (page CSS): `.home section` spacing, `.hero*`, `.duo`, `.back-intro`, `.proof` grid, `.scorecard` grid, `.notdo`, `.faq-head`, `.close .manifesto`. I list these in the Final catalogue.
   - reduced-motion rules (already in tokens) kept.
2. `site/css/motif.css`: `design-lab/motif.css` as is (cool strands), plus `.cv .eng-name` fill from `home.css`, plus a rule for the second label line (see question 1).
3. `site/js/motif.js`: lab file unchanged. Its `fetch("assets/sphyr-mark.svg")` is page-relative, so it works only for pages at the `site/` root. Noted in the catalogue.
4. `site/js/theme.js`: lab file unchanged.
5. `site/fonts/`: `manrope-latin-wght.woff2`, `newsreader-display-normal-500.woff2`, `newsreader-display-italic-400.woff2`, `OFL-manrope.txt`, `OFL-newsreader.txt`. Not the `shortlist/` folder.
6. `site/assets/`: `sphyr-logo.svg`, `sphyr-mark.svg`, `icons.svg`, `LUCIDE-LICENSE.txt`; favicon set from the mono mark: a standalone `favicon.svg` (mono mark, own `prefers-color-scheme` rule so it reads on light and dark tabs; the sprite file may not rasterize, so I make a flat copy first), `favicon.ico` (16, 32, 48 via `rsvg-convert` and `magick`), `apple-touch-icon.png` (180); `og.png` 1200 by 630 regenerated in the new look (warm paper, Newsreader core line, mono mark), rendered from a throwaway HTML card with Playwright.
7. `site/_template.html`: head from `snippets/head.html` with paths to `css/base.css`, the favicon set, OG and Twitter tags (absolute `og:image` at `https://devanshdhaked.github.io/Product-Marketing-final-assignment/assets/og.png`, the old base URL), canonical nav with `aria-current` placeholder comment, an empty `<main id="main">`, footer, `#call-note` popover, `theme.js` deferred. Comments mark: page title and description, page CSS link, page JS, content. Also a skip link to `#main` (accessibility; the lab pages have none).
8. `site/_motif.html`: unlinked specimen of the hero visual (wide 1000 by 370 and compact 360 by 590 compositions from `design-lab/home.html`, the approved ones) and the circle, with the gate 1b labels, `motif.css`, `motif.js` and a replay button. The home builder copies the SVG from here. Labels: "Project 1 · 3 teammates" to "Project 4 · 3 teammates" (each box already carries exactly 3 strands); end label "Promotion round" with "The whole year is in the file" (already so in `home.html`); `aria-label` updated to say projects and teammates; no month names.
9. `site/_shots/`: template and specimen, light and dark, 1280 and 375 (8 PNGs).
10. Docs: a new `docs/design/site_build.md` (file layout, catalogue, do-nots), a `docs/design/log.md` entry, and an index rebuild for `docs/design/` only. See question 4.

Not touched: old HTML pages, `site/style.css`, `site/main.js`, `site/og.png`, `site/sphere.svg`, `site/one.svg` (see question 2).

### Steps, in order
1. Copy fonts and assets. Commit.
2. Write `base.css`, `motif.css`, copy the two JS files. Commit.
3. Favicon set and OG image. Commit.
4. `_template.html` and `_motif.html`. Measure the new labels with `getBBox` in the browser. Commit.
5. Checks (below), shots. Commit shots.
6. Doc and report Final. Commit.

### Checks (method)
Serve the worktree root on port 8821 with `python3 -m http.server`; Playwright Chromium (I am the only phase 2 teammate running).
- `copy_scan.py` and `copy_tells.py` on `_template.html` and `_motif.html`: 0 unreviewed hits, 0 triads, at most one "X, not Y".
- Contrast: run `node design-lab/contrast.mjs` and prove the token block in `base.css` matches `design-lab/tokens.css` with a `diff` of the token section (see question 3). Plus a DOM text-contrast pass in both themes.
- Toggle: system light, system dark, stored choice wins on reload, toggling back to the system value clears storage. No flash: first-frame screenshot after reload with a stored choice.
- 0 idle `requestAnimationFrame` frames after load; reduced motion shows the finished picture; the motif plays once and rests.
- 390 px: sideways scroll 0; smallest text 11 px or more, including the motif labels.
- All relative links on both files resolve (pages that do not exist yet, such as `demo.html`, are listed, not fixed).
- 0 console errors, 0 foreign hosts.

### Open questions for the lead
1. Label fit. "Project 1 · 3 teammates" is about 23 characters; at the box's 15 px bold it is about 190 px wide, and the boxes are 148 px (wide) and 160 px (phone). Options:
   - (a, recommended) two lines in the box, "Project 1" in 15 px bold and "3 teammates" in 13 px muted. The box grows upward, so the strand start points and paths stay as they are. The middle dot is dropped because the line break does its job.
   - (b) one line with the dot, set at 13 px and boxes widened to about 176 px, which means redrawing all 12 strand paths in both compositions.
2. `site/style.css` and `site/main.js`. The 9 old pages link them, and the brief says to leave those pages alone, so the condition for removal is not met. I propose not deleting them now; the last page teammate (or the reviewer) removes them once no page links them. Same for `site/og.png`, `site/sphere.svg`, `site/one.svg` (old favicon and OG). Agree?
3. Contrast proof. `contrast.mjs` reads `design-lab/tokens.css` by a fixed path, not the site. Either (a) I keep the token block identical and show the `diff`, or (b) you let me add an optional path argument to `contrast.mjs` (one line; the script is not in my owned list) so `node design-lab/contrast.mjs site/css/base.css` checks the shipped file. I recommend (b), since page builders run it later.
4. Docs. May I add `docs/design/site_build.md` as a new file (not an edit to `design_system.md`), plus a `docs/design/log.md` entry and a `docs/design/` index rebuild? If you prefer a dated addendum inside `design_system.md`, say so.
5. Time. How long do I have? The steps above are roughly 2 to 3 hours of agent time (a guess). If it is less, I would cut the OG regeneration first and keep the old image.

## Approval (2026-11-25)
Approved with answers: 1a (two-line label, no middle dot), 2 keep old files for the lead to remove, 3b path argument in `contrast.mjs`, 4 new `docs/design/site_build.md` (second pass), 5 speed first: pass 1 is fonts, assets, CSS, JS, template, specimen; pass 2 (favicon, OG, full shots, doc) waits for the lead.

## Progress, pass 1 (2026-11-25)

Commits on `d1-sitecss`, oldest first:
- 20d4018 fonts and assets
- f1772fd `js/theme.js`, `js/motif.js` (lab files, unchanged)
- c67a332 `css/base.css`, `css/motif.css`
- 3bf8f6b `design-lab/contrast.mjs` takes an optional CSS path
- e065b63 `_template.html`, `_motif.html`

Changes from the plan:
- `.mark`, `.mark--mono` and `.mark--white` moved from `motif.css` into `base.css`. The nav and footer logo use them on every page, and pages without the motif do not load `motif.css`. A static class check found this.
- The specimen's phone composition viewBox is now `0 -4 360 594`, because the first box grew upward past y=0.

### Checks run (static only)
- `node design-lab/contrast.mjs site/css/base.css`: 116 checks, 0 failures. The default run on the lab tokens also gives 116 checks and 0 failures.
- `copy_scan.py`: `_template.html` 24 strings, 0 unreviewed hits; `_motif.html` 66 strings, 0 unreviewed hits.
- `copy_tells.py`: 0 contrasts in both files. The 1 "possible triad" in each file is the team name list in the footer, which has four names and is not a rhythm triad. It is the approved lab footer.
- Links: all 12 relative refs in each file resolve, including the SVG fragment ids (`#mark`, `#i-moon`). There are 0 duplicate ids. `demo.html`, `deliverables.html` and `index.html` resolve to the old pages for now.
- CSS braces balance in both files. Every class used in the two pages exists in the CSS, except `circle-fig`, a hook with no rule in the lab either.

### Not run: blocked
I could not run the browser checks. The Claude Code permission classifier denied starting `python3 -m http.server 8821`, both as a background process and with `run_in_background`, as "Undermining Oversight". Playwright blocks `file:` URLs.

So these are not verified: rendering in both themes at 1280 and 375, toggle and no-flash, idle frames, reduced motion, 390 px overflow, smallest text size, the label fit measured with `getBBox`, console errors.

Two fixes would unblock it: the lead or user allows the server command for this pane, or the lead serves the worktree on 8821. Then I run the full browser pass before merge, or in pass 2 if you prefer to merge now.

The label fit is by arithmetic only. "3 teammates" at 13 px is about 80 units, and "Project 1" at 15 px bold is about 70 units, in boxes 148 and 160 wide. The risk is low, but it is not measured.

## Ready for page builders

Files are in `site/`, and every page sits at the `site/` root. Copy `_template.html` to `site/<page>.html`. Do not edit `css/base.css`, `css/motif.css`, `js/theme.js`, `js/nav.js`, `js/motif.js`, `fonts/`, `assets/` or `_template.html`. Ask the lead for any shared change.

Load order: `css/base.css`, then `css/motif.css` (motif pages only), then `css/<page>.css`. Scripts with `defer`: `js/theme.js`, `js/nav.js`, then `js/motif.js` (motif pages only), then `js/<page>.js`.

### Catalogue (`base.css`)
- Base: `.wrap` (page width and gutter), `.measure`, `.muted`, `.num` (tabular figures), `.visually-hidden`, `.skip` (skip link, already in the template). `h1` and `h2` are Newsreader. `h3` and everything else is Manrope. `h1 em` and `h2 em` are the italic.
- Nav, toggle and footer: `.nav`, `.brand`, `.nav-links` (with `.nav-wide` on the three home links), `.nav-menu-btn`, `#nav-menu.nav-menu[popover]`, `.theme-toggle[data-theme-toggle]`, `.foot`, `.foot-grid`. Copy them from the template unchanged; only add `aria-current="page"` (see Nav below).
- Buttons: `.btn` plus `.btn-primary` (one per view), `.btn-secondary`, `.btn-text`. Group them in `.btn-row`. `.linkbtn` is a button that looks like a link. `.go` is an arrow link with `.icon`.
- Icons: `<svg class="icon"><use href="assets/icons.svg#i-..."/></svg>` (Lucide), with `.icon-sm` for the small size.
- Sections: `<section class="section"><div class="wrap">`. Sections are parted by a hairline. Also `.kicker`, `.lede`, `.stack`, `.stack-lg`.
- Layout families: `.split` (copy plus figure), `.doc` (reading column), `.rows` (a `dl` of labelled rows; `.rows.when` for timed steps), `.pair` (7 to 5 unequal pair), `.figure` (wide figure plus caption).
- Content: `.card` (`.card-positive`, `.card-caution`), `.table-wrap` around a `table`, `.quote` with `.q-label`, `.stat` with `.v`, `.l`, `.src`, `.bignum` (large display number), `.chips` and `.chip` (`.chip-positive`, `.chip-constructive`), `.callout`, `.sample-label` (under every product frame and illustrative number), `.src-note`, `.field` with `.help` and `.err`, `.faq` (a `details` accordion).
- Price and pilot: `.terms` holding two `.term` blocks (`.what`, `.big`, `.sub`, `p`), plus `.includes` (two-column list), `.more`, `.after`, `.call`.
- Call note: `#call-note.note-pop[popover]`, opened by `popovertarget="call-note"`. It is already in the template, once per page.
- Faux UI (product frames): `.figure` then `.stage` then `.fx-*`, in the prototype's own palette (`--p-*` tokens). Compositions: `.fx-feedback`/`.fx-hero-card`, `.fx-insights`, `.fx-team`, `.fx-benchmark`, `.fx-approvals`, `.fx-window`, `.fx-sat`. The markup source is `design-lab/faux-ui.html` and `design-lab/home.html`. Dates inside frames are cycles ("Cycle 1" to "Cycle 6") and relative times.
- Logo: `<svg class="mark mark--mono" viewBox="0 0 1254 1254"><use href="assets/sphyr-mark.svg#mark"/></svg>`. Use `.mark--white` on green.

### Nav (2026-11-25 change, commit fa8498e; replaces the 3-item nav)
- Desktop (1000 px and up): logo, How it works (`index.html#how`), For partners (`index.html#partners`), Pricing (`index.html#pricing`), Deliverables, the walkthrough button, the theme switch.
- Below 1000 px: the three home links move into a Menu popover (`#nav-menu`, all four links), and Deliverables stays in the bar beside the Menu button. Below 760 px the walkthrough button hides too, so every page must carry its own link to `demo.html`. The 1000 px breakpoint is my estimate of where the full bar stops fitting (about 930 px wide); not measured.
- Behaviour: the `popover` attribute gives open, close, Escape, outside click and focus return to the Menu button, and works without JS. `js/nav.js` keeps `aria-expanded` in step and closes the menu when a link is followed.
- Current page: add `aria-current="page"` to the link in both the bar and the menu.
- Home builder: `index.html` must have `id="how"`, `id="partners"` and `id="pricing"` on its sections. The old `index.html` on this branch has none of them, so these anchors do not resolve until the new home page lands.

### Motif (`motif.css` and `motif.js`)
Copy the `<figure>` blocks from `site/_motif.html`:
- Core visual: wide and phone SVGs, ids `cv1` and `cv1c`, the replay button `data-replay="cv1"`, labels "Project 1" over "3 teammates" through "Project 4", end label "Promotion round" with "The whole year is in the file".
- Circle: `#circle1` and the `.groups` buttons with `data-circle`.
- Other classes: `.mark--strands`, `.mark-play` (ribbons part on hover; needs `data-mark` on the svg so `motif.js` inlines it), `.mark-tile`.
- The core visual plays once. Under reduced motion it shows the finished picture.

### Left for the home builder (page CSS, not in base)
These come from `design-lab/home.css`, lines 5 to 62 and 87 to 90: `.home section` spacing, `.hero`, `.hero-copy`, `.hero-side`, `.hero-visual`, `.duo` and `.duo.flip`, `.text-col`, `.back-intro`, `.proof` (grid; use `.bignum` for the number), `.notdo`, `.faq-head`, `.scorecard`, `.proof-one`, `.close .manifesto` and `.accent`.

### Do not
- Do not edit the shared files or use raw colours. Use tokens (`var(--text)`, `--bg`, `--surface`, `--action`, `--link`, `--border` and the others). If you add colour pairs, run `node design-lab/contrast.mjs site/css/<page>.css`.
- Do not box sections or build hero-plus-three-equal-cards layouts. Only product frames and the price and pilot blocks are boxed.
- Do not add a second primary button in one view, motion that loops or follows scroll, glow, shadows on site cards, or dithering.
- Do not use eyebrow labels outside product frames. Do not use month names anywhere, including in frames.
- Do not use pages in subfolders: `motif.js` fetches `assets/sphyr-mark.svg` relative to the page.
- Do not link `style.css` or `main.js`. The lead removes them at the end.
- The favicon is `assets/sphyr-logo.svg` for now. `og:image` already points at `assets/og.png`, which pass 2 creates. Keep those head lines as they are.

### Nav change checks (static, 2026-11-25)
`copy_scan.py`: `_template.html` 33 strings, `_motif.html` 75, 0 unreviewed hits. `copy_tells.py`: 0 contrasts, the same footer-names triad flag. `contrast.mjs site/css/base.css`: 116 checks, 0 failures. `node --check site/js/nav.js`: ok. 17 relative refs per file resolve, including `#i-chevron-down`; 0 duplicate ids. The browser checks are still blocked, as above: the menu open and close, Escape, focus return, phone bar width at 375 and the desktop fit at 1000 are not verified.

Stopped. Waiting for the lead: merge, and the server permission for the browser checks.

## Pass 2 (2026-11-25)

Success number: `_template.html` and `_motif.html` render in both themes at 1280 and 375 with 0 contrast failures (116 token checks; 8 DOM runs with 11 to 38 text nodes each), 0 console errors, 0 sideways scroll (320, 360, 375, 390) and 0 running animations or animation frames after the intro. Served by the lead at `http://127.0.0.1:8821/`; Chromium through Playwright MCP.

### Browser checks and fixes
- Phone nav: at 360 px the bar had 0 px slack, and with a 15 px scrollbar it overflowed. Fixed (commit 65cd333): under 400 px the switch drops its moon icon and the gaps tighten; under 340 px the Menu chevron goes. After the fix, free space between the logo and the links is 32 px at 360 and 47 px at 375, with nothing past the edge at 320.
- Circle labels: the "Juniors" label ran 16 units past the circle's viewBox and was cut on phones. Fixed (commit e6a615c): the specimen viewBox is now `50 6 924 488`, and the phone label size is 33 px, which gives 12.3 px at 390, 11.7 at 375 and 11.2 at 360. The specimen h1 also got space above the project boxes.
- Theme: both system themes render on the first load; the toggle stores the opposite theme; toggling back clears storage; a stored choice wins over a later system change. With `base.css` held back 800 ms, `data-theme` was already set (no flash).
- Menu at 375: Enter opens it, Tab moves into "How it works", Escape closes it with focus back on the Menu button, an outside click closes it, and following a link navigates to `deliverables.html`. `aria-expanded` follows open and close. The menu box is 79 to 359 by 64 to 261 at 375. The Menu button is hidden at 1280.
- Motion: under reduced motion, 0 running animations and every strand and label visible. With motion, 44 animations at load, then 0 running animations and 0 animation frames in 1 s after 8.5 s. The circle plays once on scroll and rests within 3 s. Replay and the circle groups work. 2 of 2 `data-mark` svgs were inlined.
- Labels (`getBBox`): "Project 1" is 63 units wide and "3 teammates" 79, inside the 148 (wide) and 160 (phone) boxes. All 8 labels are inside their boxes.
- Smallest text: 15 px on the template; 11.7 px on the specimen at 375 (circle group label).
- Hosts: only `127.0.0.1:8821`. Fonts: Manrope and Newsreader loaded.

## Final

### Files written with commit SHAs (branch `d1-sitecss`)
Pass 1 (merged into `iteration-a` as c705c3e):
- 20d4018: `site/fonts/*` (Manrope, Newsreader display 500 and italic 400, OFL files) and `site/assets/` (logo, mark sprite, icons, Lucide licence).
- f1772fd: `site/js/theme.js`, `site/js/motif.js`.
- c67a332: `site/css/base.css`, `site/css/motif.css`.
- 3bf8f6b: `design-lab/contrast.mjs` takes an optional CSS path.
- e065b63: `site/_template.html`, `site/_motif.html`.
- fa8498e: the four-link nav, the phone menu, `site/js/nav.js`.

Pass 2 (not merged yet):
- 65cd333: phone nav fit at 320 to 375 px.
- ef8a34c: `site/assets/favicon.svg`, `favicon.ico` (16, 32, 48), `apple-touch-icon.png` (180), linked in both pages.
- cc941c1: `site/assets/og.png` (1200 by 630, 49 KB, the core line in Newsreader beside the mark in strand colours, light theme).
- e6a615c: circle labels fit on phones; specimen heading spacing.
- 38bb0f9: `site/_shots/`, 10 PNGs: template and motif, light and dark, 1280 and 375, plus the open menu at 375 in both themes.
- 9ea2e2c: `docs/design/site_build.md`, `docs/design/log.md`, `docs/design/index.md`. The validator gives 0 errors; its 6 warnings are outside `docs/design/`.

### Key insights and findings
- The motif labels live in page SVG markup, not in the shared CSS or JS. `_motif.html` is the source the home builder must copy. `design-lab/home.html` still has the old engagement names and the old circle viewBox.
- Logo classes (`.mark`, `.mark--mono`) belong in `base.css`. Every page's nav and footer use them, and pages without the motif do not load `motif.css`.
- The phone bar has almost no slack: logo, Deliverables, Menu and the switch take about 300 px of 343 at 375.
- Native popover covers Escape, outside click and focus return. Only `aria-expanded` needs script; the toggle event fires asynchronously, so tests must wait a tick.
- The `sphyr-mark.svg` sprite uses CSS variables. For the favicons I made a flat copy (fills fixed to warm paper on a warm ink tile, gap stroke 28) before rasterizing with `rsvg-convert` and `magick`.

### Decisions and why
- One `base.css` in the lab's order (tokens, components, faux UI, mark, shared parts), so the lab's override order holds. The lab's old `.footer` block was dropped for the canonical `.foot`.
- `.terms` and `.term` count as the brief's price block and are in base. `.bignum` replaces the two duplicated big-number rules.
- The two-line box label grows the box upward by 14 units, so no strand path changed (lead's option a).
- Nav breakpoint at 1000 px: the measured full bar fits from 1000 with 131 px to spare.
- The favicon is a tile (ink square, paper ribbons), so it reads on light and dark tabs without a media query.
- The OG image puts the core line on two lines at 62 px; the first render at 76 px broke "ends. The" mid-phrase.
- `nav.js` is a new shared file. Theme and nav behaviour stay in separate files.

### Rejected approaches and why
- One-line label with wider boxes: all 12 strand paths would need redrawing (lead chose a).
- Deleting `style.css`, `main.js`, `og.png`, `sphere.svg`, `one.svg`: the old pages still link them (lead removes them at the end).
- A hand-written JS disclosure for the menu: popover gives the same behaviour natively with less code and works without JS.
- A favicon that follows `prefers-color-scheme`: tab colours vary by browser, and the ICO and PNG files cannot switch.
- `file:` URLs for checks: blocked by Playwright. Starting my own server was denied by the permission classifier; the lead served it.

### Open questions
- The home builder must add `id="how"`, `id="partners"`, `id="pricing"`, and must copy the motif SVG from `_motif.html`, not from `design-lab/home.html`.
- At 320 px the circle group labels are about 9.7 px, under the 11 px floor (the checks target 375 and 390). Accept, or hide the circle labels below 340 px?
- `docs/design/design_system.md` still describes the 3-item nav in its phase 1b addendum. `site_build.md` says it replaces it, but the canonical doc has no dated addendum. Should one be added?
- `docs/decisions/decision_log.md` has no entry for the nav change yet (lead's call).

### Not verified
- Safari and Firefox, touch emulation, screen readers (only the DOM state was checked).
- The favicon in a real browser tab and the OG image in a real link preview: the image's absolute URL resolves only after deploy.
- The 360 and 320 checks ran with Chromium's viewport set, not on devices.
- Copy on the specimen page (h1 "Ribbon motif", the figure caption) was not run through the humanizer skill; the page is unlinked and `noindex`. Template copy is the approved lab copy.
