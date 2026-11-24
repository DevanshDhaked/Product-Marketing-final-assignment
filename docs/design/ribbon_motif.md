---
type: Guideline
title: "Ribbon motif"
description: "How the Sphyr ribbon-sphere logo becomes the site's one visual idea: the core visual, the circle of 14, the logo variants, the two strand palettes, and the motion and reduced-motion rules."
tags: [design, motif, logo, motion]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T18:18:40Z }
status: draft
sources:
  - id: msg
    resource: "docs/strategy/message_guideline.md"
    title: "Message guideline, section 9: the core visual and never-show list"
  - id: mdn
    resource: "https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timeline"
    title: "MDN: animation-timeline, Baseline 2026 newly available since October 2026 (accessed 2026-11-24)"
  - resource: "design-lab/motif.html"
  - resource: "design-lab/assets/sphyr-mark.svg"
---

# Ribbon motif

**The ribbons are the people who saw the work.** One idea, used at most three times on a page. Specimens: `design-lab/motif.html`; code: `design-lab/motif.css`, `design-lab/motif.js`, `design-lab/assets/sphyr-mark.svg`.

## Uses

1. **The core visual (home hero).** The message guideline's core visual (section 9)[^msg]: four engagements across the year, April to March. Each one sends three coloured strands (its people) into one record line. Each engagement ends and fades to a dashed outline; its strands stay. At April the record runs into the sphere. Below 600px a second, vertical composition replaces the wide one; it is not scaled down.
2. **The circle (How it works).** Fourteen strands for the average circle of 14 in the 2018 paper-and-pen pilot run by Sphyr's founder, in four groups: peers, seniors, juniors, clients. Every strand turns the same way, like the ribbons in the logo. Buttons show one group at a time. Clients join when the consultant invites them by email from My Sphyr, with the partner's agreement; captions must say that, never "when the partner adds them".
3. **The mark.** The logo in the nav and footer, and once large at the end of the core visual. On hover or keyboard focus its ribbons part slightly and come back.

Do not use ribbons as dividers, backgrounds, bullets or decoration, and never inside a product frame.

## Logo variants

All variants keep the sphere and its 15 separate ribbons. `sphyr-mark.svg` is the original artwork with 2 near-white slivers and 10 sub-pixel artefacts removed; every ribbon reads a custom property (`rib-1` to `rib-15`) that falls back to its original colour, and a gap colour outlines each ribbon so one-colour versions stay readable.

| Variant | How | Where | Why |
|---|---|---|---|
| Full colour | `assets/sphyr-logo.svg`, unchanged | Large uses only, such as the ad standee | The rainbow is the brand; at small sizes it turns to noise |
| Mono, follows the theme | `.mark--mono`: ink on light, near-white on dark, gaps in the page colour | Nav, footer, favicon, every small use | Calm, legible at 16 to 28px, never clashes with status colours |
| White on green | `.mark--white` on the fixed print green #007652 | The ad standee, any green field, photographs | One colour for print; the green does not change with the theme |
| Strand colours | `.mark--strands`: ribbons take the active strand palette | The end of the core visual, where strands become the sphere | The strands visibly become the ribbons |

## Strand palettes (decision at gate 1b)

Neither palette uses orange or red, which mean "could improve" and "destructive" in the product.

- **Cool logo colours:** teal, cerulean, royal blue, navy, green, olive, plum and orchid from the logo, each with a lighter step for dark theme. Livelier, closest to the brand.
- **Tonal green:** eight steps of the product green. Calmer and more corporate; reads as one brand colour.

## Motion

- The default, non-animated state is the finished picture, so reduced-motion readers, no-JS readers and screenshots get the whole story.
- Only opacity, transform and stroke-dashoffset animate. No scroll listeners, no WebGL, no animation library.
- Core visual: plays once on load (about 7 seconds), with a "Play again" button. Each engagement takes 1.5 seconds.
- Circle: draws in as it scrolls into view with `animation-timeline: view()` where supported (Baseline 2026, newly available since October 2026)[^mdn]; elsewhere an IntersectionObserver plays it once.
- Under `prefers-reduced-motion: reduce` nothing animates and the hover parting is off.
- Size: `motif.css` 7.9 KB, `motif.js` 3.3 KB, `sphyr-mark.svg` 13.7 KB uncompressed (9.4 KB gzipped for all three), plus about 9 KB of inline SVG per page for the two compositions. Measured 2026-11-24.

## Known limits

- Engagement names and months in the core visual are examples and are labelled as such.
- Strand colours in dark theme were checked by eye, not by a contrast script; they are decorative and every meaning is also in text.
- The hover parting needs JavaScript (it inlines the mark); without it the mark shows but does not move.

[^msg]: Message guideline, section 9: the core visual and never-show list
[^mdn]: MDN: animation-timeline, Baseline 2026 newly available since October 2026 (accessed 2026-11-24)
