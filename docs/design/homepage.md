---
type: Design Note
title: "Homepage mockup"
description: "The home page mockup in design-lab/home.html: sections and their message steps, where each piece of copy came from, the copy rules applied, and the measured checks with their method."
tags: [design, homepage, copy, checks]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T19:01:57Z }
status: draft
sources:
  - resource: "docs/strategy/message_guideline.md"
  - resource: "docs/strategy/deliverable_map.md"
  - resource: "docs/pricing/pricing_summary.md"
  - resource: "docs/packaging/packaging_summary.md"
  - resource: "docs/strategy/acquisition_engagement.md"
  - resource: "design-lab/home.html"
---

# Homepage mockup

Files: `design-lab/home.html` and `home.css`, with the canonical snippets in `design-lab/snippets/` (`head.html`, `nav.html`, `footer.html`, `theme-toggle.html`). Screenshots: `design-lab/shots/home-*.png` and `home-first-screen-*.png`, both themes, 1280 and 375. Style rules: [design system](design_system.md), [slop rules](slop_rules.md), [ribbon motif](ribbon_motif.md), [faux UI placement](faux_ui.md), [references](references.md).

## Page map

Six pages in the site: home, the 2-minute walkthrough, a deliverables hub and three deliverable pages. The home page links to two of them (walkthrough, deliverables hub) plus a "Book a 20-minute call" note. Nav: logo, Deliverables, theme switch, walkthrough button. Footer: walkthrough, deliverables, the call note, course credit.

| Section | Message step | What carries it | Copy source |
|---|---|---|---|
| Hero | 1 and 5 | Core line, one sentence, walkthrough button, the ribbon core visual ending at "Promotion round" | Core line verbatim; the rest rewritten from guideline sections 1 and 7 |
| Two minutes every two weeks | 1 and 2 | Interactive feedback card frame; the circle of 14 with group buttons | Guideline section 2; packaging step 3 and 4 copy |
| The whole year (for consultants, for partners) | 3 | Member insights frame, team-level manager frame | Guideline sections 2 and 7 |
| Most of a rating comes from the person giving it | 3 (proof and trust) | Two cited numbers, what Sphyr does not do, what stays private | Guideline sections 3 and 4; packaging FAQ |
| Try it with up to 40 people first | 5 (second step) | Scorecard, the 2018 pilot number, pilot and price blocks, what the price includes, how the price was set, what happens after signing, "Book a 20-minute call" | Acquisition and engagement (scorecard), pricing summary, packaging summary |
| Close | 4 | The vision as one large sentence, walkthrough button | Guideline section 1 (vision) |

The interactive walkthrough stays prominent: the nav button, the hero button, a link in "Two minutes every two weeks", and the closing button.

## Copy rules applied

- Every visible string was rewritten with the humanizer rules except the core line "The engagement ends. The evidence stays." Facts, numbers and conditions were kept; the pricing terms keep their exact figures and conditions.
- One "X, not Y" contrast on the page: the section 3 headline ("At promotion time, partners look at the whole year, not just the last engagement."). No triads used as rhythm, no staged openers or one-line closers, no bold labels before sentences, no dashes.
- No month names (guideline section 5, timing words). The promotion moment appears twice in public copy: the hero visual label and the section 3 headline. The scorecard's "by calibration" names a measure, not the timing.
- No line announces that Sphyr has no customers (guideline section 4, rule from 2026-11-24). The pilot section leads with the scorecard and the 2018 paper pilot, labelled exactly.
- No persona names (gate 1a). Faux UI frames keep the prototype's sample data under a sample label.

Before and after the humanizer pass (`python3 design-lab/copy_tells.py`, then confirmed by eye; product frames excluded):

| Measure | Before | After |
|---|---|---|
| "X, not Y" contrasts | 2 (plus the footer disclaimer, flagged by the script) | 1 |
| Triads as rhythm | 5 | 0 (the script still lists the citation "Scullen, Mount and Goff", the four team names, and two-item lists) |
| Month names in copy | 18 occurrences of April | 0 (prototype sample dates inside product frames remain; see open points) |

## Checks (2026-11-24)

Copy: `python3 design-lab/copy_scan.py design-lab/home.html` reads every text node, aria-label, alt, title and meta content. Result: 236 strings, 0 unreviewed hits, 10 reviewed strings (denials such as "No AI writes or scores anything", the no-refund term, the cited Gallup fact, "review" as an engagement type or competitor category, and prototype microcopy and sample dates).

Page checks follow the untemplated skill's check list, run with the Playwright MCP Chromium (not playwright-core with installed Chrome; no touch emulation or device scale on the phone profile). Profiles in order: reduced motion then motion on; desktop 1440 by 900 then phone 390 by 844; dark then light. 8 runs; the 15 px classic scrollbar guard held in all 8, 0 discarded.

| Check | Limit | Result | Method |
|---|---|---|---|
| Sideways scroll, phone | none | 0 (scrollX 0 at top and end; scrollWidth 375 equals clientWidth) | 4 phone runs |
| Smallest text, phone | 11 px | 11 px | computed size; SVG text from its rendered box |
| First-screen words | 25 (a target here) | 50 desktop, 37 phone | visible painted text in the first viewport, nav and the visual's labels included |
| Idle frames | 0 in 2 s | 0 requestAnimationFrame frames in every run | wrapped rAF, distinct frame times |
| Running animations at rest | 0 | reduced motion: 0 at 2 s and later. Motion on: 34 during the intro at 2 s, 0 at 8.5 s | `document.getAnimations()` |
| Changed share per interaction | 5% | sphere hover 0.49%, circle group 1.13%, feedback answer 4.99%, price disclosure 4.42%, call note 0.49% | screenshot at rest against during, grey difference over 24, scrollbar cut, 1440 by 900 light |
| Time to rest after leave | 2 s | sphere hover 160 ms | screenshots every 100 ms until equal to rest |
| Boxed at rest | only frames and price blocks | faux UI frames (panels, KPI tiles, cards) and the two term blocks; nothing else | computed borders on 3 or more sides, outline, box shadow |
| Modes | right first frame | system dark loads dark; stored light loads light on the first frame; toggling back to the system value clears the stored choice | init script samples the first frame |
| Contrast | 4.5:1 below 24 px, 3:1 above | 0 failures in 201 desktop and 177 phone text nodes, both themes | computed colours against the nearest solid background |
| Fonts and hosts | licensed, 0 foreign | Manrope and Newsreader (roman and italic) loaded, licence files beside them; 0 requests to other hosts | `document.fonts`, request log |
| Clean load | 0 | 0 page console errors, 0 failed requests | console and request log |

Notes, not failures:
- The first screen holds 50 words at 1440 because the core visual carries the engagement names and the promotion label. The nav, the core line, one sentence and the button come to 33 words (6 plus 6 plus 17 plus 4, counted by hand).
- The core visual plays once on load (about 7 seconds), as agreed, then rests. Under reduced motion it shows the finished picture.
- The feedback answer change (4.99%) sits at the limit: the card swaps its second step, as the product does.
- The call note's 0.49% counts only text and border pixels, because the note's surface and the page differ by less than the 24-level grey threshold. By area the note covers about 5% of the viewport.
- The earlier scroll-linked draw on the circle was removed; it now draws once when it enters the view.

## Open points

- Prototype sample dates (chart axis May 05 to Jun 30, comment dates Jul 22 and Jul 25) still show inside the product frames. They are the product's sample data; replacing them would change the real screen. Decide whether the no-month rule covers them.
- Engagement names in the core visual (pricing review, market entry, cost programme, due diligence) are examples of engagement types, not clients.
