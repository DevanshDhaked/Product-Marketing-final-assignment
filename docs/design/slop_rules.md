---
type: Guideline
title: "Slop rules for page builders"
description: "Concrete do and do-not rules so Sphyr pages stop reading as AI-made, drawn from the site design audit and the design-taste rules that fit a static B2B site."
tags: [design, copy, guideline]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T17:04:27Z }
status: draft
commit: fc85cac
sources:
  - resource: "docs/site_audit/design_audit.md"
  - resource: "design-taste-frontend skill (local Claude Code skill, not in this repo)"
  - resource: "stageshow skill, references/craft.md (local Claude Code skill, not in this repo)"
---

# Slop rules for page builders

Use these with the [design system](design_system.md) and the [faux UI placement](faux_ui.md). Each rule says what to do. Where a rule comes from the [design audit](../site_audit/design_audit.md), the audit line is named so you can see the old pattern. Check a finished page against the list at the end.

## Visual

Do:
- Use the tokens in `design-lab/tokens.css` only. No raw hex values in page CSS.
- Keep one accent family: the product green. Orange means "could improve" and appears only on chips, marks and caution cards.
- Give site cards a hairline and no shadow. Save shadows for product view frames.
- Use the ribbon-sphere SVG for the logo. It is the only multicolour element outside product views.
- Show a real product view (see [faux UI placement](faux_ui.md)) where a page needs a visual.

Do not:
- Put a radial glow or gradient blob behind a hero (audit: `style.css:171-172`).
- Add glow shadows or gradient washes to cards (audit: feedback card `style.css:73`, price card `style.css:108`).
- Use the dark developer-tool palette (near-black and teal) as the default look. The site is light-first with a full dark theme that follows the reader's choice.
- Draw icons by hand. Use the Lucide sprite in `design-lab/assets/icons.svg`, one size and one stroke per view.
- Use a sparkle, wand or star icon anywhere. It reads as "AI", and Sphyr has no AI features today (see the [do-not-claim list](../product/do_not_claim.md), item 2).
- Use emoji in page copy or headings.
- Add decorative status dots, hairline grids, rotated text or scroll cues.

## Layout

Do:
- Use at least four different section layouts on a page: split hero, document column, labelled rows, unequal pair, wide figure.
- Keep the hero to four text elements at most: an optional kicker, a headline of at most two lines, subtext of at most 20 words, and one primary plus one secondary button.
- Put every number that needs a source in a stat or a table with the source in the same block.
- Stack every multi-column layout to one column under 900px and check the page at 375px.

Do not:
- Build a row of three identical bordered cards (audit: `index.html:65-69`, `108-112` and five other pages). Use an unequal pair, labelled rows or a table.
- Repeat "kicker, H2, three cards" for every section (audit: "every section is eyebrow + H2 + 3 cards").
- Center a closing hero with two buttons (audit: `index.html:129-132`). End with one plain call to action in a split or a document column.
- Use giant monospace stat numerals (audit: `style.css:69`). One number per stat, Manrope, 40px.
- Use inline styles for layout. Use the component classes.

## Type

Do:
- Use Manrope for everything. Numbers use tabular figures, not a monospace font.
- Write headings in sentence case. Make hierarchy from size and one weight step.
- Keep body lines under 68 characters.

Do not:
- Put an uppercase, letter-spaced monospace label above headings (audit: `style.css:40` and nearly every heading). This is the most recognisable AI-landing-page tell.
- Use more than one kicker per three sections. A kicker is sentence case, 15px, green text (`.kicker`), never uppercase mono.
- The exception: the uppercase green eyebrow inside a product view frame stays, because it is the product's real page header.

## Copy

Do:
- Write plain, short sentences with specific numbers and their sources.
- Keep the honest labels the audit praised: "illustrative, not a customer case", "Sample data, fictional people", the 2018 pen-and-paper pilot wording.
- Say what is true about privacy: ratings are pooled and comments are anonymized to the person rated. A manager approving an edit request sees who gave that feedback.
- Use one label per intent across a page. If the walkthrough button says "Try the walkthrough", every walkthrough link says that.

Do not:
- Write staccato triads ("Three posts. Three jobs. One promise.", audit: `linkedin.html:26`, `ad.html:26`, `index.html:118`, `index.html:56`).
- Close sections with a reflexive "X, not Y" line (audit counted 60 occurrences, for example `trust.html:51`, `pricing.html:71`). Keep the brand line if the message guideline keeps it, and use the pattern nowhere else.
- Use stock LinkedIn moves ("Nobody here is a villain.", "That's the real problem.", "Here's why ...", audit: `linkedin.html:49-51`, `121`).
- Use em dashes, en dashes as separators, or double hyphens. Use a full stop, a comma, a colon or "to" for ranges.
- Use hype words: seamless, empower, unlock, revolutionary, cutting-edge, leverage, robust, world-class, elevate.
- Say "anonymous to everyone", "fully anonymous" or "bias-free".
- Invent customers, logos, testimonials, integrations, AI features or certifications.

## Product views

Do:
- Use only screens that exist in the prototype, with its labels and microcopy.
- Put "Prototype screen. Sample data, fictional people." under every frame.
- Crop to the part that carries the point, and keep every real word whole.

Do not:
- Crop the manager view in a way that hides the edit approvals and so suggests full anonymity.
- Show the "Members Needing Support" list, any screen that names a low performer, or scores next to people (message guideline, section 9).
- Use the prototype's demo names (John Smith, Maya Chen and others) or present any sample name as a real person or client.
- Build fake dashboards or screens the prototype does not have.

## Pre-publish check

Run on every page before it ships:
1. Count kickers: at most one per three sections.
2. Count layout families: at least four on a page with five or more sections; no row of three equal cards.
3. Search the file for the em dash (U+2014), the en dash (U+2013) and the double hyphen in copy: zero.
4. Search for the hype words above: zero.
5. Every number has a source or a sample label in the same block.
6. Every product view has the sample label.
7. Toggle both themes and look at the whole page in each.
8. Load at 375px: no sideways scroll, no button label wraps, nav on one line at desktop.
9. `node design-lab/contrast.mjs` still reports 0 failures if any token changed.
