---
type: Research Note
title: "Site technical notes"
description: "Stack, deployment to gh-pages, JS behaviour, bugs, mobile overflow and accessibility issues on the site."
tags: [site, technical, bugs]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
commit: fc85cac
sources:
  - resource: "site/"
  - resource: "README.md"
---

# Site technical notes

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Paths are relative to `site/`. Audit of commit fc85cac on 2026-11-24.

## Stack and deployment
- Plain static HTML/CSS/JS, no build, no framework, no analytics (README.md:48). 9 pages, one stylesheet (174 lines), main.js (45 lines), inline script in demo.html:92-113, two hand-written SVGs, og.png 1200x630.
- Deploy: GitHub Pages serves branch `gh-pages`; after committing `site/` run `git subtree push --prefix site origin gh-pages` (README.md:60-64). Verified: `git diff origin/gh-pages HEAD:site` is empty, so live = HEAD (gh-pages last commit 2026-11-24 11:15 +0530). `main` and `iteration-a` point at the same commit fc85cac. Subtree push deploys whatever branch is checked out, so a push from iteration-a goes live immediately.
- Live check (curl, 24 Nov): HTTP 200 for /, all 9 pages, style.css. main.js/og.png/svgs not reached before the slow check was stopped; same tree as HEAD so expected present.
- OG/Twitter tags on every page, one shared og.png; favicon = sphere.svg.

## JS behaviour
- main.js:1-20: any `.fcard` is playable; counts clicks on stars and tags; send requires a rating (shake animation otherwise), then swaps to the done state and dispatches a bubbling `sent` event.
- demo.html:93-112: `go(n)` toggles steps and progress, smooth-scrolls to top; candidate pick -> step 2; `sent` -> 900 ms -> step 3 with pick-dependent line; bars rendered from a hard-coded 7-row array.
- main.js:22-35: calculator = n x 149 x 12, GST 18%, first bill = annual x 1.18 - 15,000.
- main.js:37-45: order form prevents submit and prints a prototype confirmation; nothing is sent. Uses innerHTML but only interpolates a number, so no injection risk.

## Bugs
- Calculator shows a negative first bill at 7 or fewer employees: verified ₹-4,451 at 5 employees (main.js:31). Also credits the pilot against the GST-inclusive total, while main.js:43 prices the pilot as "₹15,000 + GST". Clamp at 0 and credit pre-GST.
- Calculator accepts decimals (pricing.html:51 has no `step`).

## Mobile (Playwright, 375px window, 360px layout width)
Horizontal page scroll on 3 of 9 pages:
- how-it-works.html: scrollWidth 430. Root cause: inline `style="grid-template-columns:repeat(3,1fr)"` on `.loop` (how-it-works.html:66 and :92) overrides the 800px media query (style.css:99). Five steps in 3 columns also leaves a ragged row on desktop (:92-98).
- pricing.html: scrollWidth 371. Root cause: `.g2` is `minmax(320px,1fr)` (style.css:52) inside the order form card with 26px padding (pricing.html:89-90), so the track cannot fit.
- propaganda.html: scrollWidth 413. Root cause: `.doc-layout` single track is `1fr` (style.css:143), and grid items keep min-content width, so wide tables push the track out. Fix: `minmax(0,1fr)`. The TOC is also hidden under 900px (style.css:143), so the 13-section doc has no navigation on phones.
- Others (index, demo, trust, deliverables, linkedin, ad): no overflow.
- Sticky nav wraps to 100px tall on mobile (style.css:33), about 12% of an 800px viewport.

## Accessibility
- Unlabelled textareas (placeholder only): index.html:40, demo.html:58.
- Rating and tag buttons are toggles without `aria-pressed`; rating buttons are named only "1" to "5" (index.html:36-38; demo.html:54-56; state only via `.on` class in main.js:7, 10).
- `aria-label` on a plain `div` with no role (index.html:32) is ignored by most screen readers.
- Demo step changes do not move focus or announce anything (demo.html:93-97); the hidden steps use `display:none`, so focus is lost to body.
- Block `<div>`s inside `<button>` (demo.html:41-42): invalid content model.
- No skip link; no `prefers-reduced-motion` guard for `scroll-behavior: smooth` (style.css:17), the demo smooth scroll (demo.html:96), card hover lift (style.css:120) or the shake (main.js:13).
- Contrast: `.paper a` #0e7c66 on #f6f5f1 is about 4.7:1 (passes AA for body text, narrowly). Muted #9aa5ae on dark backgrounds is fine.
- Good: `:focus-visible` outline (style.css:170), `aria-current` on nav, labelled form inputs on pricing, alt text on informative images, `alt=""` on decorative ones, `aria-live` on the order result (pricing.html:97).

## Housekeeping
- Google Fonts via CSS `@import` (style.css:1) delays first paint; a `<link rel=preconnect>` + `<link>` in head is faster.
- "(Offer pending faculty confirmation.)" is shipped copy (pricing.html:71). Resolve before 27 Nov.
- README.md:6 has an emoji; README.md:65-67 disclaimer is good.
