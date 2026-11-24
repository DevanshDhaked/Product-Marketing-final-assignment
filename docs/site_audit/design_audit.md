---
type: Research Note
title: "Design and AI-slop audit"
description: "Visual and copy patterns on the site that read as generic or AI-made, the current design system, and what to keep."
tags: [site, design, audit]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
commit: fc85cac
sources:
  - resource: "site/style.css"
  - resource: "site/"
---

# Design and AI-slop audit

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Paths are relative to `site/`. Audit of commit fc85cac on 2026-11-24.

## Scan results (scripted over all html, css, js, README)
- Em dashes in copy: 0.
- En dashes: only in numeric ranges ("50–300", "51–200", "1–2" weeks), e.g. deliverables.html:40, propaganda.html:104-106, ad.html:63. Acceptable; could be swapped for "to" if the "no dashes" rule is applied strictly.
- `--`: only in CSS custom properties (style.css:4-14 and uses). Not copy.
- Hype words (seamless, empower, unlock, revolutionary, cutting-edge, leverage, robust, world-class, etc.): 0.
- Emoji: 👇 in Post 1 copy (linkedin.html:53), ✅ x3 in Post 3 copy (linkedin.html:130-132), 🔗 in README.md:6. The 👍💬↗✉ reaction bars (linkedin.html:56, 102, 145; ad.html:56) are LinkedIn chrome and fine.
- ", not " contrast construction: 60 occurrences across the html. Part of it is the brand line itself ("merit, not politics"), but it is overused enough to read as a tic.

## Visual patterns that read as template / AI default
- Radial gradient glow blob behind every hero (style.css:171-172, applied via `.hero`).
- Glow drop shadow on the feedback card (style.css:73) and gradient wash on the price card (style.css:108).
- Uppercase letter-spaced mono "eyebrow" above nearly every heading (style.css:40; index.html:26, 52, 62, 73, 82, 93, 105, 117; same on every page). The single most recognisable AI-landing-page tell.
- Identical bordered-card grids, mostly in threes: index.html:65-69, 108-112; how-it-works.html:43-47, 55-59; trust.html:42-46; pricing.html:66-70; deliverables.html:39-43. Every section is eyebrow + H2 + 3 cards.
- Giant mono stat numerals (style.css:69; index.html:109-111).
- Centered closing hero with two buttons (index.html:129-132).
- Dark "dev-tool" palette (near-black + teal, Linear/Vercel look) for an HR buyer the site itself describes as plain-speaking and wary of tech jargon (propaganda.html:119). Brief says looks only "make an impression", so this is a fit question, not a score item. A warmer, paper-first look (the `.paper` style already used on deliverable pages) would fit the persona better.
- Heavy inline styles (e.g. index.html:51, 65, 77; linkedin.html:98, 140-143; ad.html:36-54) instead of components.

## Copy patterns that read as AI
- Staccato triads in headlines: "Three posts. Three jobs. One promise." (linkedin.html:26), "One image. One promise. Two seconds." (ad.html:26), "One price. No tiers. No surprise when you hire." (index.html:118), "Problem, belief shift, offer. Three jobs, one message." (index.html:56).
- Stock LinkedIn moves: "Nobody here is a villain." / "That's the real problem." (linkedin.html:49, 51), "Here's why we didn't make it tiered." (linkedin.html:121), "(Illustrative, but you've probably lived it.)" (linkedin.html:39), arrow lists (linkedin.html:82-84).
- Reflexive "X, not Y" closers: "Guided setup, not a login and good luck" (how-it-works.html:91), "This is a trade, not a discount" (pricing.html:71), "Feedback, not surveillance" (trust.html:51), "We blame the structure, not the people" (propaganda.html:65, also 162).
- "Fairness is the product, so the pricing should be fair too." (pricing.html:29): tidy aphorism, fine once.

## Design system (style.css)
- Fonts: Inter 400/500/600/700/800 for everything; JetBrains Mono 400/600 for eyebrows, labels, stats, prices, table headers (style.css:1, 14, 18). Loaded via CSS `@import` from Google Fonts (render-blocking chain).
- Type scale: h1 clamp(38px, 6vw, 68px) weight 800, tracking -.035em (36); h2 clamp(28px, 3.6vw, 40px) (37); h3 20px (38); body 17px/1.6 (18); lede 20px muted (39); small 14px (43); eyebrow 13px mono uppercase .12em (40); label 11px mono pill (44).
- Colour tokens (3-15): bg #0b0d0f, bg2 #12161a, card #161b20, line #262d34, text #e8ecef, muted #9aa5ae, accent #0e7c66 (buttons, borders), accent-hi #2fd3a9 (links, highlights), paper #f6f5f1, ink #15191c. LinkedIn mock uses #0a66c2 and #f3f2ef. No light/dark theme switch; site is dark-only, deliverable docs use `.paper` light.
- Spacing and layout: container 1120px, narrow 760px, side padding 24px (21-22); section padding 88px, tight 56px, hero 72/88 (46-48); grid gap 20px; split 1.1fr/.9fr gap 56px, stacks under 900px (55-56).
- Radii: cards 14px, fcard/price 18px, buttons 10px, inputs 8px, labels 6px.
- Components: sticky blurred nav with pill CTA (25-33); `.btn-p` filled teal and `.btn-g` ghost (61-66); `.card`; `.stat`; `.fcard` interactive feedback card (73-88); `.vs` one-vs-many (91-93); `.loop` numbered timeline with CSS counters (96-99); tables + `.tbl` scroll wrapper (102-105); `.price` card (108-111); `details` accordions (112-113); form inputs (114-115); `.deliv` hub cards with hover lift (118-124); `.paper` long-form doc with sticky TOC (127-143); `.li` LinkedIn post mock (146-156); `.ad` 1:1 creative (159); `.note` dashed disclaimer (164).

## Genuinely good, keep
- Honest labelling everywhere: "illustrative, not a customer case" (index.html:82), "2018 pen-and-paper pilot of the method, not today's software" (index.html:105), "Sample data · fictional people" (demo.html:33), no unsupported security claims (trust.html:68), prototype note on the form (pricing.html:98). This is the strongest credibility asset and matches the brief's "do not invent" rule.
- The walkthrough as self-persuasion: pick a candidate before seeing pooled data (demo.html:36-44, 65-83; rationale propaganda.html:85). The professor already praised the demo.
- The one-dot vs ring visual used on home, Post 2 and the ad (index.html:76-77; linkedin.html:98-101; ad.html:43-46). A real, repeatable brand device.
- Structural framing that avoids blaming managers: "Your company grew faster than anyone's line of sight" (index.html:28) and the reasoning for it (propaganda.html:64-65).
- Hub ergonomics: every deliverable one click from every page (nav pill + footer).
- Plain, short sentences; specific numbers; FAQ-style H2 "Can my manager see who wrote what? No." (trust.html:31).
- Propaganda doc structure: belief/attitude/response table (propaganda.html:58-63), tactic-with-reason table (79-89), anti-segment (50-55), guardrails (157-165).
- Transparent price reasoning section as a concept (pricing.html:74-83); it needs real numbers, not removal.
- Paper style for the deliverable documents, visually separating "course artefact" from "product site".

---
