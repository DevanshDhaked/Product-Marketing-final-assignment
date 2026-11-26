---
type: Research
title: "v3 design review against v2: visual defects before the user sees it again"
description: "Ranked list of visual defects in the merged iteration-b site (v3 words on the v2 design) on six pages at 1280 light, 1280 dark and 375 light, measured and compared with v2."
tags: [research, design, review, v3, v2, qa]
sources:
  - resource: "http://localhost:8883/ (v3 candidate, merged iteration-b site/, served locally on 2026-11-26)"
  - resource: "http://localhost:8830/ (v2, the design the professor liked, served locally on 2026-11-26)"
  - resource: "docs/design/slop_rules.md (house rules)"
  - resource: "design-taste-frontend skill and design:design-critique skill (local Claude Code skills, not in this repo)"
generated: { by: claude-code/opus-5-5, at: 2026-11-26T15:10:25Z }
---

# v3 design review against v2

## Method

- Pages: index, demo, ad, linkedin, propaganda, deliverables. Each at 1280x800 light, 1280x800 dark and 375x812 light, for v3 (port 8883) and v2 (port 8830). 18 page loads per version.
- Viewport screenshots down the whole page in steps of the viewport height minus 60 px, with reduced motion on so figures show their final frame. Files are in `swarm/tmp/dreview/` as `{v2|v3}_{page}_{1280l|1280d|375l}_{NN}.png`. Contact sheets used for scanning are in `swarm/tmp/dreview/sheets/`.
- Demo stepped through on both versions in all three settings (pick Tara, "Was good", two tags, Submit): `{v2|v3}_demoopen_*`.
- Scripts measured: left and right edge of every section's content, page scroll width, hidden labels, one-word last lines in every text element, button and caption classes, nav items. The ribbon and circle were also run with motion on (`*_motion_*`).
- Not checked, per the brief: copy, WCAG contrast.

## What passed

- No sideways scroll on any page at any width (scroll width equals the viewport on all 36 loads).
- Section content edges match v2 on every page: 104 to 1176 px at 1280, 16 to 359 px at 375.
- Nav is the same on all six pages and the same as v2 apart from the call button label. Phone Menu lists the same four links as v2.
- The logo sphere, the ribbon hero, the circle figure, the product frames on the beige mat and the card styling are all back. The ribbon animation runs on the same timing as v2 (settles in about 8 s), with no console errors.
- Dark theme shows no defect that light does not have, and matches v2 dark section by section.

## Defects

Origin: "new" means v3 introduced it; "inherited" means v2 has it too.

| Rank | Page | Width, theme | Where | What | Origin | Screenshot | One-line fix |
|---|---|---|---|---|---|---|---|
| Blocker | index | 1280 light and dark | Hero | The hero grew from 765 to 861 px. The ribbon starts about 95 px lower than in v2, so "Appraisal cycle" sits on the fold (y 780 of 800). The caption's second line and Play again fall below the first screen. In v2 the whole figure, its caption and Play again fit. Cause: the H1 now runs 3 lines (house rule: 2), and the right column stacks lede, button, pilot line and walkthrough link. | new | v3_index_1280l_00.png, v2_index_1280l_00.png | Bring the H1 back to 2 lines (smaller size or shorter line) and take one item out of the right column, so the figure starts near y 345 as in v2. |
| Visible | index | 1280 all | Price and pilot, pilot card | "Book a 20-minute call" is the outlined `btn-secondary` here. Nav, hero and close show the same action as the green primary. In v2 the outline was right, because the primary action was the walkthrough. | new | v3_index_1280l_08.png | Make the pilot card button `btn-primary`. Keep the plan card's text link. |
| Visible | demo, linkedin | all | Figure captions | Two caption systems now exist. Demo and linkedin use a new `exhibit-cap`: "Exhibit N." with a 1 px green rule, a Source line and a bold note, so three type treatments under one frame. Index, ad and propaganda keep the plain grey caption with the info icon, which v2 used on every page. Inside the LinkedIn post mock, an "Exhibit 1" caption reads as out of place. | new | v3_demoopen_1280l_04.png, v3_linkedin_1280l_02.png, v2_linkedin_1280l_02.png | Use the index caption (icon and one grey line) on demo and linkedin. Keep the bold "Tara's column" note as in v2. |
| Visible | demo (same native popover on every page; captured on demo only) | 1280 light | Call popover | The nav "Book a 20-minute call" opens a popover centred in the viewport. It covers the intro's sample-data line and steps 3 and 4 of the step list, and it is far from the button that opened it. | new | v3_callnote_1280l.png | Anchor it under the nav button (fixed, top right, below the header), or give it a backdrop so it reads as a dialog. |
| Visible | index | 375 light | How it works, Fortnightly Feedback frame | A white strip of about 140 px sits empty inside the frame below the last tag ("Resilient"). Frame bottom minus last tag: 222 px in v3, 118 px in v2. | inherited, worse | v3_index_375l_04.png, v2_index_375l_05.png | Let the frame height follow its content on phones. |
| Visible | index | 375 light | Team Insights frame | The "Edit requests" stat card is hidden on phones, so only Team score and Participation show. This breaks the slop rule "do not crop the manager view in a way that hides the edit approvals". The "Strongest signal" card in Insights is hidden too. | inherited | v3_index_375l_06.png | Show Edit requests on phones (third card full width under the two). |
| Visible | index | 1280 all | Closing line | The 3-line display heading ends with one word: "memory." | new | v3_index_1280l_09.png | Add `text-wrap: balance` to `.manifesto`, or widen it so "not one manager's memory." stays together. |
| Visible | index | 1280 all | What happens at calibration | Five single sentences sit in full-width rows (1072 px) with a hairline on every row. The text ends near x 820, so the right third of every row is empty. v2 used labelled rows (bold label and sentence) under a lead paragraph. | new | v3_index_1280l_01.png, v2_index_1280l_01.png | Restore the v2 labelled-row layout, or cap the rows to the text column width. |
| Visible | demo | 1280 all | Step 4, What this changes | The CTA group floats in the middle of its column (button top about 130 px below the H2 top, paragraph about 60 px below, read from the screenshot). The paragraph ends on the widow "a time." v2 put the buttons in one row under the text. | new | v3_demoopen_1280l_04.png, v2_demoopen_1280l_04.png | Top-align the CTA column with the paragraph, or stack it under the text as in v2. |
| Visible | linkedin, ad, index | all | Text links after the main button | Four classes serve two link intents: `.go` (green, underlined, arrow), `.btn-text` ("Next: the advertisement", no arrow), `.linkbtn` and plain links. On linkedin, two links in two different styles sit one under the other. v2 used an outlined button for "Next". | new | v3_linkedin_1280l_05.png | Use one text-link style (`.go` with arrow) for both, or bring back the v2 button row. |
| Visible | deliverables | 1280 all | How we set the price, What happens after a firm signs | The two new sections start at x 104, while the deliverable titles above sit at about x 200 after the 01 to 04 numbers, so the page has two left edges. The term "Every two weeks after that" wraps and leaves "that" alone. | new | v3_deliverables_1280l_02.png, v3_deliverables_1280l_03.png | Indent the new sections to the title column, or set them off with their own section rule. Widen the term column or stop it wrapping. |
| Visible | index | 375 light | Who gets a say, circle | The centre circle is empty on phones: the "Consultant" label is hidden. The "Juniors" label reaches x 367, 8 px inside the screen edge instead of the 16 px gutter. | inherited | v3_index_375l_08.png | Show the centre label at a smaller size, and pull the side labels inside the gutter. |
| Nit | ad | 1280 and 375 | Standee | The standee stacks a 5-line body, QR code, URL, pilot line and brand line under the ribbon, and reads crowded next to v2. | new | v3_ad_1280l_01.png, v2_ad_1280l_01.png | Shorten the standee body or drop the pilot line from the standee (it is on the card back). |
| Nit | propaganda | 1280 all | Expected response timeline | The step label breaks at the hyphen: "Book a 20- / minute call". | new | v3_propaganda_1280l_04.png | Use a non-breaking hyphen (U+2011) in "20-minute". |
| Nit | ad | 1280 and 375 | Handout card URLs | The printed URL breaks as "Product / -Marketing-final-assignment/v3/", so a line starts with a hyphen. v2 broke it mid-word. | inherited | v3_ad_1280l_01.png | Add `<wbr>` after each "/" so it breaks at slashes only. |
| Nit | index | 1280 all | Price cards | The divider in the pilot card is dark grey, and the one in the plan card is light. | new | v3_index_1280l_08.png | Use the same hairline token in both cards. |
| Nit | index | 1280 all | Who gets a say | The counts table ends at x 1076, while the paragraph above runs to 1176. | inherited | v3_index_1280l_06.png | Match the table width to the text column. |
| Nit | index | 1280 all | How it works | The H2 starts 110 px below the frame top (v2: 79 px), so the text column looks loose next to the frame. | new | v3_index_1280l_02.png | Align the text column to the top of the frame. |
| Nit | index | 1280 all | Insights caption | The caption wraps with "cards." alone on its last line. | new | v3_index_1280l_04.png | Shorten the caption or let it run full width. |
| Nit | demo | all | Step 1, selected consultant | The checked radio shows a grey dot on the green card, so it looks disabled. | inherited | v3_demoopen_1280l_01.png | Colour the checked radio green. |
| Nit | all | 375 light | Header and Menu | The phone header and Menu have no "Book a 20-minute call", although it is now the main action. | inherited | v3_menu_375l.png | Add the call as the last Menu item. |

## v2 parity

Verified present in v3: the logo sphere in nav and footer, the ribbon hero and its animation, the circle figure, the product frames on the beige mat with the "Private by design" note, the price card pair, the standee and handout cards, the propaganda layout, and both themes.

What v2 had that v3 no longer has. Some of these may be intentional under the v3 order; the lead should confirm each.

- The "Today / With Sphyr" pull-quote pair under the problem section.
- The row of three green stat numerals (62% and 53%, 29%, 02:09) with sources.
- The "What stays private" FAQ accordion (five disclosures).
- Labelled problem rows (bold label plus paragraph), now plain sentences.
- The plan card's two-column feature list and the "Clients you invite to give feedback: free" line, plus the "What a pilot measures" and "How we set the price" disclosures.
- The "What happens after you sign" timeline on the home page (now on deliverables).
- The "Back to home" button at the end of the demo.
- End button rows on ad and linkedin (walkthrough, next page, all deliverables). The ad page lost its links to the LinkedIn posts and to all deliverables.
- The pull-quote band "The engagement ends. The evidence stays." inside LinkedIn post 2.
- The icon caption on demo and linkedin frames.

## What this means for v3

- Fix the index hero first: 2-line H1 and one fewer item in the right column, so the ribbon, its caption and Play again fit in 1280x800 as in v2.
- Make every "Book a 20-minute call" button the green primary, including the pilot card.
- Use one caption style site-wide: the v2 icon caption. Drop "Exhibit N." from demo and the LinkedIn mock.
- Anchor the call popover to the nav button.
- On phones, show the Edit requests card and the circle's centre label, and trim the empty strip in the feedback frame.
- Pick one text-link style for secondary actions, and top-align the demo step 4 CTA.
- Put the two new deliverables sections on the title column and fix the "that" and "20- / minute" breaks.
- Ask the lead which dropped v2 pieces (stats row, FAQ, Today/With Sphyr, end button rows) were cut on purpose.
