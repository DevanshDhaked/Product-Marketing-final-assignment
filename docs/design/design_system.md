---
type: Design System
title: "Sphyr site design system"
description: "Direction, light and dark colour roles with checked contrast, type, spacing, radius, elevation, components, motion and the theme toggle for the Sphyr site."
tags: [design, tokens, theme, accessibility]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T17:04:27Z }
status: draft
commit: e3e82ae
sources:
  - id: proto
    resource: "https://sphyr-prototype.raviwarrier.com/"
    title: "Sphyr prototype, CSS custom properties read in a browser"
    last_modified: 2026-11-24T00:00:00Z
  - id: toggle
    resource: "https://developer.chrome.com/docs/modern-web-guidance/guides/ui-components/dark-mode-toggle"
    title: "Chrome for Developers: Dark mode toggles (accessed 2026-11-24)"
  - id: lightdark
    resource: "https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark"
    title: "MDN: light-dark(), Baseline widely available since May 2024 (accessed 2026-11-24)"
  - id: wcag
    resource: "https://www.w3.org/TR/WCAG22/"
    title: "WCAG 2.2: 1.4.3 contrast minimum 4.5:1, 1.4.11 non-text contrast 3:1"
  - resource: "design-lab/tokens.css"
  - resource: "design-lab/contrast.mjs"
---

# Sphyr site design system

The code is the source of truth: [`design-lab/tokens.css`](../../design-lab/tokens.css), [`components.css`](../../design-lab/components.css), [`faux-ui.css`](../../design-lab/faux-ui.css) and [`theme.js`](../../design-lab/theme.js). This note explains the choices and the rules that the code cannot show. See it working in `design-lab/components.html` and `design-lab/faux-ui.html` (serve the repo root with `python3 -m http.server`).

## Direction

The site should look like the documentation of the product it sells: calm, light-first, set in the product's own typeface and colours, with a full dark theme. The reader is the head of talent at a 40 to 400 person Indian consulting firm. That reader is wary of tech jargon and judges credibility, so the page avoids the dark developer-tool look, glows and decorative effects. The only strong colour moments are the ribbon-sphere logo and the product views. Real prototype screens do the showing, with an honest sample-data label under each. Grading is on message and reasoning, so the look aims to be credible and to get out of the way.

## Colour roles

Every colour token is defined once with `light-dark(light, dark)`. Values come from the prototype's CSS[^proto] unless the table says "changed". Contrast is checked against WCAG 2.2[^wcag] by `node design-lab/contrast.mjs`, which parses `tokens.css` and exits non-zero on any failure. Current result: 70 checks (35 pairs in two themes), 0 failures.

| Role | Token | Light | Dark | Key check (light / dark) |
|---|---|---|---|---|
| Page | `--bg` | #F6FAFD | #040A16 | |
| Card, panel | `--surface` | #FFFFFF | #0D1826 | |
| Raised (satellite, popover) | `--surface-raised` | #FFFFFF | #121C2B | |
| Sunk (callout, bars) | `--surface-sunk` | #EAF1F8 | #182230 | |
| Frame well | `--stage-ground` | #E4EDF6 (new) | #08111F (new) | 4.65 / 8.84 muted text on it |
| Body text | `--text` | #0D1828 | #F4F7FB | 16.98 / 18.43 on page |
| Secondary text | `--text-muted` | #5E6A7A | #A5B3C1 | 4.83 / 7.49 on sunk (lowest) |
| Hairline | `--border` | #DAE2EA | #2C394A | decorative, no requirement |
| Control outline | `--border-strong` | #7B8799 (new role) | #5B6B80 (new) | 3.47 / 3.64 on page, 3:1 needed |
| Button fill, link | `--action`, `--link` | #007652 (changed) | #34C696 | 5.66 / 9.12 with button text |
| Button text | `--on-action` | #FFFFFF | #040A16 | |
| Brand green, non-text | `--brand`, `--focus` | #009163 | #34C696 | 3.83 / 9.12 focus ring on page |
| Strength surface and text | `--positive-soft`, `--on-positive-soft` | #DBF8EB, #005B38 | #043123, #A4E9CB | 7.30 / 10.28 |
| Could-improve mark | `--constructive` | #E1712D | #F7A224 | 3.18 / 8.63 as a mark, never text on light |
| Could-improve surface and text | `--constructive-soft`, `--on-constructive-soft` | #FFEED2, #4C1E01 | #3D1D00, #FFD69A | 12.33 / 11.16 |
| Destructive, form error | `--destructive` | #C62B29 (changed) | #FF655A | 5.30 / 6.85 on page |

Changes from the prototype and why:
- **Action green #009163 to #007652.** White text on #009163 is 4.02:1 and #009163 as link text on the page is 3.83:1. Both fail AA for normal text. #007652 gives 5.66:1 and 5.39:1. #009163 stays for non-text use (chart lines, focus ring, the radar), where 3:1 is enough.
- **Destructive #DF312F to #C62B29.** #DF312F is 4.33:1 on the page background.
- **Small green text inside faux UI** (the product's uppercase eyebrow) uses `--link`, not #009163, for the same reason.
- **New `--border-strong`** so input and button outlines meet 3:1. The prototype's #CED9E3 input border is about 1.4:1.
- **New `--stage-ground`** for the well that frames product views.

Colour meaning follows the product: green is strength or positive, orange is "could improve" and never "bad", red only for errors and destructive actions. One accent family (green) across the whole site.

## Type

Manrope only, the prototype's typeface. It is self-hosted as one latin variable woff2 (weights 200 to 800, 24 KB) with `font-display: swap` and a preload; the SIL OFL licence sits next to it in `design-lab/fonts/`. This replaces Inter and JetBrains Mono and the render-blocking Google Fonts `@import`. No monospace: numbers use `font-variant-numeric: tabular-nums`.

| Step | Size | Line height | Use |
|---|---|---|---|
| Display | 36 to 56px fluid; 34 to 44px beside a figure | 1.12 | Page H1, at most two lines |
| H2 | 26 to 34px fluid | 1.25 | Section headings |
| H3 | 20px | 1.25 | Card and sub-headings |
| Lede | 19px | 1.6 | One paragraph under a heading |
| Body | 17px | 1.6 | Copy, at most 68 characters per line |
| Small | 15px | 1.5 | Nav, buttons, table cells |
| Caption | 13px | 1.45 | Sources, sample labels, table headers |

Weights: 400 body, 500 nav, 600 buttons and labels, 700 headings. Sentence case everywhere outside product views.

## Space, radius, elevation

- Space: 4px base (4, 8, 12, 16, 24, 32, 48, 64, 96). Sections 64 to 96px tall padding. Content width 1120px, gutters 24px (16px under 640px).
- Radius rule: surfaces (cards, tables, frames) 12px, the prototype's value. Controls (buttons, inputs) 8px. Status chips and the toggle track are full pills. Nothing else.
- Elevation: site cards have a hairline and no shadow. Shadows exist only on faux UI frames (`--shadow-frame`) and their satellites (`--shadow-satellite`), ported from the stageshow kit and tinted to the page. In dark theme depth comes from lighter surfaces and a light hairline.

## Components

All in `design-lab/components.html`, in both themes:
- **Nav:** logo, four links, theme toggle, Deliverables button. 64px, one line on desktop. Under 760px the links move to a second scrollable row and the Deliverables button hides; the footer keeps every deliverable one click away.
- **Theme toggle:** a labelled switch, "Dark theme", with `aria-pressed`. Rules below.
- **Buttons:** primary (filled), secondary (outlined), text link with arrow. Labels one to three words, never wrapping on desktop.
- **Section layouts (five families):** split hero, document column, labelled rows, unequal pair (7 to 5), wide figure with caption. A page uses at least four different families and never three equal cards.
- **Cards:** plain, strength (green tint), caution (amber tint).
- **Table:** sentence-case header, tabular right-aligned numbers, one rule per row, source in the caption, sideways scroll on phones.
- **Quote:** the product's own "Anonymized feedback" item. At most three lines.
- **Stat:** one number, its label, its source. A number without a source is not shown.
- **Chips:** VBA tags in the product's positive and could-improve colours.
- **Sample label and callout:** honest labels under every product view and illustrative number.
- **Form field:** label above, helper and error below.
- **Questions:** native `details` and `summary`.
- **Footer:** course disclaimer, product links, deliverable links.
- **Faux UI frame:** see [faux UI placement](faux_ui.md).

## Motion

Motion is feedback only: hover colour, the 0.98 press on buttons, the toggle knob, the accordion chevron, the feedback card's selected tile. 160ms, one ease curve. No entrance animations, no scroll effects, no loops. Under `prefers-reduced-motion: reduce` every transition and animation is off.

## Theme toggle

Behaviour, following Chrome for Developers' guidance on dark mode toggles[^toggle]:
1. CSS works without JavaScript. `:root { color-scheme: light dark }` and `light-dark()` colours[^lightdark] follow the system setting when nothing is stored.
2. A tiny inline script in `<head>`, before the stylesheets and never deferred, reads `localStorage["sphyr-theme"]` and sets `data-theme` on `<html>`, which pins `color-scheme`. `localStorage` is wrapped in try/catch.
3. The toggle switches to the opposite of what is on screen. If that equals the system setting, the stored value is removed instead of saved, so the page goes back to following the system.
4. A later system change never clears a stored choice. Other tabs follow through the `storage` event.
5. Two states are shown, as the guidance recommends for a toggle in site chrome.

Verified on 2026-11-24 with a Playwright script on `components.html` (7 scenarios, all correct): with a stored choice, the first animation frame after reload already has the stored theme's background, so there is no flash.

Copy this into every page `<head>`:

```html
<meta name="color-scheme" content="light dark">
<script>try{var t=localStorage.getItem("sphyr-theme");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}catch(e){}</script>
```

## Known limits

- `light-dark()` needs a browser from May 2024 or later. Older browsers drop those colour declarations.
- The Manrope file is the latin subset. A canvas width test (2026-11-24) suggests it renders the rupee sign itself: "Manrope, serif" measured differently from plain serif. The font file was not inspected. If the glyph is missing, the browser falls back to the system font for that one character.
- The ribbon logo's near-white highlight paths (#F8F9F9, #F0F6F6) were checked by eye on the dark nav at 28px only.

[^proto]: Sphyr prototype, CSS custom properties read in a browser
[^wcag]: WCAG 2.2: 1.4.3 contrast minimum 4.5:1, 1.4.11 non-text contrast 3:1
[^toggle]: Chrome for Developers: Dark mode toggles (accessed 2026-11-24)
[^lightdark]: MDN: light-dark(), Baseline widely available since May 2024 (accessed 2026-11-24)
