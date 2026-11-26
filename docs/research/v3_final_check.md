---
type: Research
title: "v3 final check: three numbers, both themes at both widths, link previews, smoke"
description: "A read-only final check of the iteration-b site on the three v3 success numbers, a defect pass at 1280 and 375 in light and dark, the link-preview tags and the smoke rules, scored with the method of v3_review.md."
tags: [research, audit, review, v3, qa, dark-mode]
sources:
  - resource: "http://localhost:8889/ (final iteration-b site/, served by the lead), Playwright, 2026-11-26"
  - resource: "http://localhost:8830/ (v2, for comparison of the ad in dark), 2026-11-26"
  - resource: "site/index.html, site/ad.html, site/linkedin.html, site/demo.html, site/deliverables.html, site/propaganda.html, site/js/demo.js, site/js/theme.js, site/assets/og.png, site/assets/ad/walkthrough-qr.svg (iteration-b working tree)"
  - resource: "docs/research/v3_review.md, docs/research/v2_baseline.md, docs/research/v3_design_review.md (methods and earlier scores)"
  - resource: "docs/brief/professor_feedback.md (addendum 2026-11-26)"
  - resource: "docs/decisions/decision_log.md (entries of 2026-11-26)"
  - resource: "docs/product/prototype_screens.md, docs/product/product_facts.md"
generated: { by: claude-code/opus-5-5, at: 2026-11-26T18:30:00Z }
---

# v3 final check

## The three numbers

| Number | v2 | v3 review | Now | Target |
|---|---|---|---|---|
| First-screen test, home (1280x800 and 375x667) | 6 of 9 | 9 of 9 | 9 of 9 at both widths | 9 of 9 |
| First-screen test, ad standee | 3 of 9 | 9 of 9 (8 if the QR target counted) | 9 of 9 (QR now opens /v3/, so no caveat) | 9 of 9 |
| Professor's faults still present | 8 of 8 | 2 of 8 (4 and 8, partial) | 1 of 8, partial (8, judgment); 4 closed | 0 of 8 |
| Foreign-word entries on public pages | about 20 | 8 | strict 2, lenient 1 (see section 3) | 0 |

All scores are one reviewer's judgment (n=1), read as a managing partner of a 40 to 400 person Indian consulting firm. No reader from the segment was tested.

## Method
- Same rubric as `v2_baseline.md` section 1 (0 to 3 for what, who, next) and the same fault and residue methods as `v3_review.md`.
- 182 viewport screenshots: six pages at 1280x800 and 375x667, light and dark, reduced motion, theme from the system setting with no stored choice. Steps of viewport height minus 60 px. Files in `swarm/tmp/final3/` as `{page}_{1280|375}{l|d}_NN.png`; light and dark side by side in `swarm/tmp/final3/sheets/`.
- Demo stepped through in all four settings (pick Tara, Was good, two tags, Submit): `demoopen_*`. Phone Menu (`menu_375{l|d}.png`) and the nav call popover (`callnote_1280{l|d}.png`) opened in both themes.
- Dark through the toggle: index and ad at both widths with a light system setting and `sphyr-theme=dark` stored, pixel-diffed against the system-dark shots: 0 differing pixels in 8 of 8 frames.
- Visible text: tags, head, scripts, styles and comments stripped per source line; a watch list grepped; words not in `prototype_screens.md` or `product_facts.md` listed per page (index 117, ad 101, demo 75, linkedin 136, deliverables 102, propaganda 147 distinct words) and read by hand.
- QR decoded in the browser with BarcodeDetector. Links collected in the browser; pages fetched (6 of 6 return 200, `assets/og.png` 200); every `#id` grepped (16 of 16 found).

## 1. First-screen test

### Home (1280x800 and 375x667, both themes, screenshots looked at)
In frame at 1280: H1 "Peer feedback for appraisals at consulting firms" (`index.html:67`, 2 lines, 101 px), lede (68), call button, pilot line, walkthrough link, and the full ribbon with its caption and Play again (button at y 750 to 794 of 800). At 375: H1, lede, button, pilot line and walkthrough link all above 667 (walkthrough link bottom at y 531).

| Question | Score | Text judged | Why |
|---|---|---|---|
| (a) What | 3 | H1 (67), lede (68) | Peer feedback, for appraisals, every two weeks, two minutes, read by partners and engagement managers before calibration. |
| (b) Who | 3 | H1 (67), lede (68) | Consulting firms, 40 to 400 people, India. |
| (c) Next | 3 | button, pilot line, link | One main action with its terms under it. |
| Total | 9 of 9 | | |

### Ad standee (`ad.html`, headline and first line)
Headline: "Calibration is on Monday. Half the project feedback forms are still blank." First line: "Sphyr collects peer feedback for appraisals every two weeks, for heads of talent at consulting firms of 40 to 400 people in India. Scan to book a 20-minute call or see the 2-minute walkthrough."

| Question | Score | Why |
|---|---|---|
| (a) What | 3 | Product and job in segment words. |
| (b) Who | 3 | Buyer role, firm type, size, country. |
| (c) Next | 3 | Names the step. The QR now decodes to `https://devanshdhaked.github.io/Product-Marketing-final-assignment/v3/`, whose first button is the call, as the decision log entry "v3 returns to the v2 design" asks. |
| Total | 9 of 9 | |

## 2. Professor's faults (numbering as in `v3_review.md`)

| # | Fault | Now | Evidence |
|---|---|---|---|
| 1 | No Attention at the top of home | Fixed | `index.html:67` to 68. |
| 2 | Vague lines | Fixed | Problem h2 "What happens at calibration today" (100) with five labelled scenes. "The engagement ends. The evidence stays." 0 hits on public pages. |
| 3 | Statements that need long explanation | Fixed | One sentence per problem row; no footnoted statistic on home. |
| 4 | Not written from inside the reader's life | Fixed (was partial) | New row "Attrition: A strong consultant misses a designation and leaves after the hike letters go out." (`index.html:106`) names the managing partner's first fear. |
| 5 | "file" and other non-product words | Fixed | 0 visible hits for file, record, evidence, pooled, member (outside "Member Insights" and "Member role"), subordinates, VBA, resources, teammates, turnout. |
| 6 | No AIDA order across home | Fixed | Section order: hero (A), calibration today (I), two minutes every two weeks and who gets a say (I), what you get and what stays private (I, assurance), price and pilot (D), close (A). Nothing after the Action. |
| 7 | Ad headline is not an Attention line | Fixed | Standee and card headline as above. |
| 8 | LinkedIn posts do not stop a doomscroller | Partly present (judgment) | Better: the 1906 ox paragraph is gone; post 1 opens "Four people saw the workshop. None were in calibration." (`linkedin.html:73`) with a type card of that hook (83); post 2 opens "One manager writes the rating for four projects." (116); post 3 gives a checklist to save or forward (193). "How the three work together" adds that team members reshare each post in their own words. Still present: all three posts come from the Sphyr company page (`linkedin.html:63` and each author block), and post 3 opens on "the pilot" (193) for a reader who has not met Sphyr yet. The `linkedin3` report's own source puts company-page reach at 1.6 percent of followers. Lead decision, already open in `review3_report.md`: company page or a named person. |

## 3. Foreign words (residue)
Exempt (decision log 2026-11-26): "Deliverables" in the nav; "Member Insights" in body copy; "circle"; the course labels Job, Journey stage, Call to action on the ad and LinkedIn pages; course words on `propaganda.html` and `deliverables.html`; screen names.

| Phrase | Page:line | Why | Strict | Lenient |
|---|---|---|---|---|
| the whole year | propaganda 71, 109, 128, 213 | The v2 vague phrase class; no exemption names it. Course page, low cost. | 1 | 1 |
| Attention, trigger (ad); Attention, Interest, Decision as values, "Post 1: recognition" (LinkedIn) | ad 128, 129; linkedin 100, 102 to 104, 180 to 181, 233 to 234 | AIDA words as values and in body text. The exemption names only the three labels. Same intent, so lenient counts it as covered. | 1 | 0 |

Fixed since the v3 review: "turnout" (0 hits), "The 20-minute call" label (now "Book a 20-minute call", `propaganda.html:224`), "how the project team is landing" (now one consultant's Insights, matching the product phrase, `deliverables.html:123`), the Admin results claim (`deliverables` "After a few cycles" now gives the view to engagement managers). Buyer copy on home and ad: 0 entries; every word not in the product docs is a segment word (calibration, staffed, rolled, hike, designation, attrition) or a name.

Not counted (false positives of the script): "quot" (an HTML entity in demo), `--w` at `js/demo.js:67` (a CSS variable).

## 4. Defects (both themes, both widths)

Dark at 375 shows no defect that light at 375 does not have on any of the six pages or the stepped demo. The ad's print pieces sit on the dark page with no beige mat; v2 dark does the same (`v2_ad_1280d_01.png`), so not logged.

### Rows from `v3_design_review.md`
| Rank then | Page | Where | Status now | Screenshot |
|---|---|---|---|---|
| Blocker | index | Hero at 1280 | Fixed: H1 2 lines; ribbon, caption and Play again in 800 px | index_1280l_00.png |
| Visible | index | Pilot card button | Fixed: green primary | sheets/index_1280_02.png |
| Visible | demo, linkedin | Two caption systems | Fixed: icon caption on all pages | demoopen_1280l_02.png, sheets/linkedin_1280_01.png |
| Visible | all | Call popover centred | Fixed: anchored under the nav button | callnote_1280l.png |
| Visible | index 375 | Empty strip in feedback frame | Fixed | index_375l_04.png |
| Visible | index 375 | Edit requests card hidden | Fixed | sheets/index_375_02.png |
| Visible | index 1280 | "memory." alone on the last line | Fixed: "manager's memory." | sheets/index_1280_03.png |
| Visible | index 1280 | Problem rows as bare sentences | Fixed: labelled rows | sheets/index_1280_00.png |
| Visible | demo 1280 | Step 4 CTA floating | Fixed: stacked under the text | sheets/demoopen_1280_01.png |
| Visible | linkedin, ad, index | Four link styles | Fixed: one `.go` style with arrow | sheets/linkedin_1280_02.png |
| Visible | deliverables 1280 | Two left edges | Fixed: new sections on the title column | sheets/deliverables_1280_00.png |
| Visible | index 375 | Circle centre label hidden | Fixed: "Consultant" shows; labels inside the gutter | sheets/index_375_02.png |
| Nit | ad | Crowded standee | Fixed: pilot line moved to the card | standee_el.png |
| Nit | propaganda 1280 | "20- / minute" in timeline | Fixed (non-breaking hyphen) | sheets/propaganda_1280_01.png |
| Nit | ad | Handout URL breaks at a hyphen | Fixed: breaks after slashes | sheets/ad_375_00.png |
| Nit | demo | Grey checked radio | Fixed: green | sheets/demoopen_375_00.png |
| Nit | all 375 | No call in the phone Menu | Fixed: last Menu item | sheets/menu_375.png |
| Visible (part of the Edit requests row) | index 375 | "Strongest signal" card hidden in the Insights frame (`index.html:171`) | Still present (inherited from v2) | sheets/index_375_01.png |

Not re-checked one by one: price card divider colour, counts table width, How it works H2 offset, Insights caption widow. None stood out in the sheets.

### New
| Rank | Page | Theme, width | Where | What | Screenshot | One-line fix |
|---|---|---|---|---|---|---|
| Nit | propaganda | light and dark, 375 | Core card, Expected response (`propaganda.html:70`) | "take the 2- / minute walkthrough" breaks at the hyphen. The timeline fix did not reach this line. | propaganda_375l_00.png, propaganda_375d_00.png | Use U+2011 in "2-minute" and "20-minute" in this card too. |
| Nit | linkedin | light and dark, 375 | Post 2 first comment (`linkedin.html:173`) | URL wraps as "Product- / Marketing-final- / assignment/v3/demo.html". | sheets/linkedin_375_01.png | Add `<wbr>` after each "/" as on the ad cards. |
| Nit | link preview | n/a | `site/assets/og.png` top left | Mono logo mark, while the site header uses the full-colour mark (decision 2026-11-25). The og3 report left this to the lead. | site/assets/og.png | Lead call: swap `.mark--mono` for the colour mark and re-render, or keep. |

No blocker. No visible-rank defect.

## 5. Link previews
- `og:image` is `https://devanshdhaked.github.io/Product-Marketing-final-assignment/v3/assets/og.png` on 6 of 6 pages.
- `og:url` is the page's own /v3/ address on 6 of 6 pages (home: `/v3/`).
- No `twitter:image` tag on any page (platforms fall back to og).
- `site/assets/og.png` (1200x630) shows "Peer feedback for appraisals / at consulting firms" and "For firms of 40 to 400 people in India.", the logo sphere and a green base band. It matches the v3 home headline and lede.

## 6. Smoke results
| Check | Result | Evidence |
|---|---|---|
| No sideways scroll | Pass | `scrollWidth` = `clientWidth` on 24 of 24 loads (6 pages, 2 widths, 2 themes) and on 4 of 4 opened demos. |
| Internal links resolve | Pass | All page targets return 200; 16 of 16 `#id` targets exist. External link (peopleanalyst.com) not fetched. |
| No /v2/ anywhere in `site/` | Pass | 0 hits in html, js, svg. QR decodes to /v3/ (3 of 3 QR images). |
| Main button label exact | Pass | Every `.btn-primary` on 6 of 6 pages reads "Book a 20-minute call"; footer link and phone Menu item the same. Prose mentions ("Scan to book a 20-minute call", "Book a 20-minute call to plan one", "in the last line") are sentences, not labels. `propaganda.html:224` uses a non-breaking hyphen, same visible text. The aria-label "Book a call" on the home close section is not visible. |
| At most one "X, not Y" per page | Pass | index 308, ad 87, propaganda 67 (sign-off); demo 65 (disclaimer); linkedin and deliverables 0. |
| No em or en dashes | Pass | 0 in visible text of the six pages and `js/demo.js`. |
| No month names | Pass | 0. ("Monday" is a weekday.) |
| Dark via the toggle | Pass | Pinned dark equals system dark, 0 pixel difference in 8 frames. |

## What this means for v3
- All three numbers meet target except two judgment items; nothing on the site blocks submission.
- Lead decision on fault 8: keep the company page as author (with the staff reshare line) or post as a named person; this is the last open fault.
- Lead decision on the AIDA words used as values on the ad and LinkedIn pages: extend the exemption in writing, or relabel. Either takes the foreign-word count to 1 or 0.
- If the residue must be 0: replace "the whole year" on `propaganda.html:71`, 109, 128, 213 with the project-team wording used elsewhere.
- Use U+2011 in the propaganda core card's "2-minute" and "20-minute" (`propaganda.html:70`).
- Add `<wbr>` after slashes in the post 2 comment URL (`linkedin.html:173`).
- Decide whether `og.png` should carry the full-colour logo mark like the site header.
- Optional, inherited: show the "Strongest signal" card on phones in the home Insights frame.
