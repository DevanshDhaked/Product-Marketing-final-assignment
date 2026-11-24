---
type: Guideline
title: "Site build: shared files and page contract"
description: "How the shared site files in site/ (base CSS, motif, theme and nav scripts, fonts, assets, page template) are laid out, which classes page builders use, the canonical nav, and what pages must not do."
tags: [design, site, css, template, nav]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T19:41:03Z }
status: draft
commit: e6a615c
sources:
  - id: lab
    resource: "design-lab/"
    title: "Approved design lab: tokens.css, components.css, faux-ui.css, motif.css, home.css, theme.js, motif.js, snippets/"
  - id: decisions
    resource: "docs/decisions/decision_log.md"
    title: "Gate 1b decisions: ribbon labels, no month names, humanized copy"
  - id: popover
    resource: "https://developer.mozilla.org/en-US/docs/Web/API/Popover_API"
    title: "MDN: Popover API (light dismiss, Escape, focus return to the invoker) (accessed 2026-11-24)"
---

# Site build: shared files and page contract

The approved design in `design-lab/` is ported into shared files under `site/`. Pages add only their content, one page CSS file and one page JS file. This note is the contract between the shared files and the pages. It extends [the design system](design_system.md), [the slop rules](slop_rules.md), [faux UI placement](faux_ui.md) and [the ribbon motif](ribbon_motif.md), and does not replace them.

## Files

| Path | What it holds | Source |
|---|---|---|
| `site/css/base.css` | Tokens for both themes, base type, layout primitives, components, faux UI frames, the logo mark, shared page parts | `tokens.css`, `components.css`, `faux-ui.css`, mark rules of `motif.css`, shared parts of `home.css`, in that order |
| `site/css/motif.css` | Strand palette, mark motion and strand variants, the core visual, the circle | `motif.css` plus the two-line box label |
| `site/js/theme.js` | Theme switch: system default, stored choice, other tabs | `theme.js`, unchanged |
| `site/js/nav.js` | Keeps `aria-expanded` on the Menu button in step; closes the menu when a link is followed | new |
| `site/js/motif.js` | Inlines the mark for hover, replay, the circle playing once, circle groups | `motif.js`, unchanged |
| `site/fonts/` | Manrope variable, Newsreader display 500 and italic 400, both OFL licence files | `design-lab/fonts/` |
| `site/assets/` | `sphyr-logo.svg`, `sphyr-mark.svg` (sprite, `#mark`), `icons.svg` (Lucide) with `LUCIDE-LICENSE.txt`, `favicon.svg`, `favicon.ico` (16, 32, 48), `apple-touch-icon.png` (180), `og.png` (1200 by 630) | lab assets; favicons and OG image are new |
| `site/_template.html` | Blank page: head, nav, empty `main`, footer, call note, scripts | `design-lab/snippets/` |
| `site/_motif.html` | Unlinked specimen of the core visual and the circle with the gate 1b labels | `design-lab/home.html` compositions |
| `site/_shots/` | Screenshots of the two files above, both themes, 1280 and 375, plus the open menu at 375 | not linked from any page |

The `@font-face` paths in `base.css` are `../fonts/`; the head preloads are `fonts/` from the page. Both resolve to the same URL, so each font loads once.

The old `site/style.css`, `site/main.js`, `site/og.png`, `site/sphere.svg` and `site/one.svg` stay until no page links them, then they are removed.

## Page contract

- Copy `site/_template.html` to `site/<page>.html`. Every page sits at the `site/` root. Do not put pages in subfolders, because `motif.js` fetches `assets/sphyr-mark.svg` relative to the page.
- Do not edit the shared files. Put page styles in `site/css/<page>.css` and page scripts in `site/js/<page>.js`.
- Load order: `css/base.css`, then `css/motif.css` (only with the motif), then the page CSS. Scripts, all with `defer`: `js/theme.js`, `js/nav.js`, `js/motif.js` (only with the motif), then the page script.
- Keep the head order: the colour-scheme meta and the inline theme script come before any stylesheet, so a stored theme applies on the first frame.
- Replace the title, the description and the three `og:` text fields. Keep the favicon lines and `og:image`.
- Use tokens (`var(--text)`, `--text-muted`, `--bg`, `--surface`, `--action`, `--link`, `--border` and the rest), never raw colours. If a page adds colour pairs, check them with `node design-lab/contrast.mjs site/css/<page>.css`.

## Nav (replaces the three-item nav)

- From 1000 px: the logo, then How it works (`index.html#how`), For partners (`index.html#partners`), Pricing (`index.html#pricing`) and Deliverables, then the walkthrough button and the theme switch.
- Below 1000 px, the first three links move into a Menu popover (`#nav-menu`, all four links). Deliverables stays in the bar beside the Menu button.
- Below 760 px, the walkthrough button hides as well, so every page must carry its own link to `demo.html`.
- Below 400 px, the switch drops its moon icon and the gaps tighten. Below 340 px, the Menu chevron goes as well.
- The `popover` attribute gives open, close, Escape, outside click and focus return without script. `nav.js` only syncs `aria-expanded` and closes the menu after a link.
- For the current page, add `aria-current="page"` to its link in both the bar and the menu. That is the brand link on `index.html`; Deliverables on `deliverables.html` and the three deliverable pages; the button on `demo.html`.
- The home page must give its sections `id="how"`, `id="partners"` and `id="pricing"`.

## Class catalogue

- Base: `.wrap`, `.measure`, `.muted`, `.num`, `.visually-hidden`, `.skip`. `h1` and `h2` use Newsreader; `em` inside them is the italic.
- Buttons and links:
  - `.btn` plus `.btn-primary` (one per view), `.btn-secondary` or `.btn-text`, grouped in `.btn-row`.
  - `.linkbtn` is a button that looks like a link. `.go` is a link with an arrow `.icon`.
- Icons: `<svg class="icon"><use href="assets/icons.svg#i-..."/></svg>`, with `.icon-sm` for the small size.
- Sections: `<section class="section"><div class="wrap">`. Also `.kicker`, `.lede`, `.stack` and `.stack-lg`.
- Layout families:
  - `.split`: copy beside a figure.
  - `.doc`: a reading column.
  - `.rows`: a `dl` of labelled rows; `.rows.when` for timed steps.
  - `.pair`: an unequal 7 to 5 pair.
  - `.figure`: a wide figure with a caption.
- Content:
  - Cards: `.card`, `.card-positive`, `.card-caution`.
  - Tables: a `table` inside `.table-wrap`.
  - Quotes: `.quote` with `.q-label`.
  - Numbers: `.stat` with `.v`, `.l` and `.src`; `.bignum` for one large display number.
  - Tags: `.chips` holding `.chip`, `.chip-positive` or `.chip-constructive`.
  - Notes: `.callout`, `.sample-label`, `.src-note`.
  - Forms: `.field` with `.help` and `.err`.
  - FAQ: `.faq`, an accordion of `details` elements.
- Price and pilot: `.terms` holding two `.term` blocks (`.what`, `.big`, `.sub`), plus `.includes`, `.more`, `.after` and `.call`.
- Call note: `#call-note.note-pop[popover]`, opened with `popovertarget="call-note"`. It is in the template, once per page.
- Faux UI: `.figure` then `.stage` then the `.fx-*` classes, in the prototype palette (`--p-*`). The compositions are `.fx-feedback` with `.fx-hero-card`, `.fx-insights`, `.fx-team`, `.fx-benchmark`, `.fx-approvals`, `.fx-window` and `.fx-sat`. The markup source is `design-lab/faux-ui.html` and `design-lab/home.html`.
- Logo: `<svg class="mark mark--mono" viewBox="0 0 1254 1254"><use href="assets/sphyr-mark.svg#mark"/></svg>`. Use `.mark--white` on green and `.mark--strands` (motif CSS) for the colour version.
- Motif:
  - Copy the `figure` blocks from `site/_motif.html`.
  - Core visual: `#cv1` wide and `#cv1c` phone, with the replay button `data-replay="cv1"`. Box labels are "Project 1" over "3 teammates", up to "Project 4". The end label is "Promotion round" with "The whole year is in the file".
  - Circle: `#circle1` with the `.groups` buttons (`data-circle`, `data-group`). Its viewBox is `50 6 924 488`, so the "Juniors" label is not cut on phones.

Home-only layout stays in the home page's CSS. That covers `.hero` and its parts, `.duo`, `.text-col`, `.back-intro`, the `.proof` grid, `.scorecard`, `.proof-one`, `.notdo`, `.faq-head` and `.close .manifesto`. The source is `design-lab/home.css`.

## Do not

- Do not box sections or use a hero over three equal cards. Only product frames and the price and pilot blocks are boxed.
- Do not put a second primary button in one view.
- Do not add looping or scroll-linked motion, glow, shadows on site cards, or dithering.
- Do not use eyebrow labels outside product frames.
- Do not write month names anywhere, including inside frames. Use cycles and relative times.
- Do not link `style.css` or `main.js`.

## Checks on the shared files (2026-11-25, Chromium through Playwright, served over HTTP)

- Contrast: `node design-lab/contrast.mjs site/css/base.css` gave 116 token checks and 0 failures. A DOM pass gave 0 failures in 8 runs (two files, both themes, 1280 and 375; 11 to 38 text nodes per run).
- Theme:
  - Both system themes render on the first load.
  - The toggle stores the opposite theme. Toggling back to the system value clears storage.
  - A stored choice wins over a later system change.
  - `data-theme` is set before `base.css` arrives, tested with the stylesheet held back 800 ms.
- Menu at 375: Enter opens it, Tab moves into it, and Escape closes it with focus back on the Menu button. A click outside closes it, and following a link navigates. The Menu button is hidden at 1280.
- Motion:
  - Reduced motion: 0 running animations and every strand and label visible.
  - With motion: 44 animations at load, then 0 running animations and 0 animation frames after 8.5 s.
  - The circle plays once when scrolled into view and rests within 3 s.
- Phone:
  - Sideways scroll is 0 at 320, 360, 375 and 390.
  - The smallest text is 11.7 px at 375. That is the circle group label, 11.2 px at 360.
  - The box labels fit: "Project 1" is 63 units and "3 teammates" 79 units wide, inside 148 and 160 unit boxes.
- Console and hosts: 0 console errors. The only host is the local server.
- Copy: `copy_scan.py` and `copy_tells.py` give 0 unreviewed hits and 0 contrasts. The single "possible triad" is the footer list of four team names.

Not checked: Safari and Firefox, touch emulation, screen readers. At 320 px the circle group labels fall below 11 px (about 9.7 px).
