---
type: Handoff
title: "Link-preview image report"
description: "og.png remade at 1200 by 630 with the v3 headline, the India line and the full-colour logo sphere, rendered from HTML."
tags: [handoff, og3]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T16:40:00Z }
---

# Link-preview image report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Plan approval skipped: the og3 brief is the approved plan and says to do it now.

## Final

Image: `site/assets/og.png` (1200 x 630, 8-bit RGB PNG, 68,283 bytes, under the 300 KB cap).

### Files and commits
- `design-lab/og/og.html` (new): HTML source for the image. Links `site/css/base.css` for the real fonts and tokens. Commit `5b1f4ba`.
- `site/assets/og.png` (replaced). Commit `5b1f4ba`.
One commit, because the image and its source are one logical group.

### Key decisions
- Text is verbatim from the brief. Display line: "Peer feedback for / appraisals / at consulting firms" in three explicit lines (Newsreader 500, 70 px). "at consulting firms" is the italic 400 accent in `--link` (#007652), the same as `home.css:59`. Small line: "For firms of 40 to 400 people in India." (Manrope 500, 28 px, `--text-muted`). 28 px keeps it legible when LinkedIn and WhatsApp scale the card to about 40 to 50%. The strings were not run through humanizer, because they come verbatim from the brief and the home H1/lede.
- Line breaks are explicit `<br>` rather than `text-wrap: balance`, so a re-render gives the same result.
- Top-left: mono mark plus "Sphyr" (`.mark--mono`), as in the old image. The live site header uses the full-colour mark. Changing this one class is the lead's call.
- Right sphere: the `sphyr-mark.svg#mark` symbol with paper gaps (`--rib-gap: var(--bg); --rib-gap-w: 8`), the same treatment as the home hero `.mark--strands`. The symbol's colours on this branch are the current logo palette (orange, yellow, red, greens, blues), so the sphere no longer looks like the old OG's blue and olive version. It now matches the site. Commit `4a994f8` ("Ribbon visual: original logo colours for strands and sphere in both themes") made that change, and no site CSS overrides `--rib-N` with a colour.
- Green rule at the foot: 10 px, `--brand` (#009163), full bleed. It is the one element meant to touch the edges.

### Checks (measured in the page with getBoundingClientRect, viewport 1200 x 630, devicePixelRatio 1)
- Fonts loaded before capture: `document.fonts.check` returned true for Newsreader 500, Newsreader italic 400 and Manrope 500.
- Brand row top 121. H1 text box x 80 to 616, y 206 to 422. Small line x 80 to 559, y 457 to 495. Sphere x 760 to 1120, y 125 to 485. Rule y 620 to 630.
- Safe margin: every element except the foot rule is at least 80 px from each edge (brief asks for 64 px). The gap between text and sphere is 144 px.
- I opened the PNG and looked at it. The text is sharp and nothing is clipped.
- The only console error is the favicon 404 at the server root (`/favicon.ico`). This is a property of the design-lab page and does not affect the image.

### Approaches rejected
- `sphyr-logo.svg` as an `<img>`: rendered the sphere without the paper gaps the site uses. Replaced with the mark symbol. The first render was overwritten and not committed.
- Two lines for the display text: "Peer feedback for appraisals" at 70 px is about 800 px wide and would run into the sphere.
- `browser_take_screenshot`: saves to the MCP output folder. I used `page.screenshot` with an explicit path, `clip` and `scale: 'css'` instead.

### Not verified
- How LinkedIn and WhatsApp actually render the card. Not tested live (no push).

### Screenshots
- The deliverable itself: `site/assets/og.png`. The common brief's per-theme 1280 and 375 screenshots do not apply to a fixed 1200 x 630 image, which has no theme and no responsive layout.

## Not done (out of scope)
- The file name `og.png` is unchanged, and every page's `og:image` points at `.../v3/assets/og.png`. LinkedIn and WhatsApp cache previews by URL. Links already shared may keep showing the old image until someone re-scrapes the URL in LinkedIn Post Inspector, or until the meta tags get a cache-busting query such as `og.png?v=3`. Meta tags are outside my scope. This is the lead's call.
- No `og:image:alt` tags exist on any page, so no alt text describes the old image.
