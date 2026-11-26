---
type: Research
title: "v2 baseline: first-screen test, professor's faults, foreign words"
description: "Where the v2 site (branch iteration-a, live at /v2/) stands on the three v3 success numbers, with file and line evidence, so v3 can be scored the same way."
tags: [research, audit, baseline, v2, aida, vocabulary]
sources:
  - url: "https://devanshdhaked.github.io/Product-Marketing-final-assignment/v2/"
    title: "Sphyr v2 home (live)"
    published: "2026"
    accessed: 2026-11-26
  - url: "https://devanshdhaked.github.io/Product-Marketing-final-assignment/v2/ad.html"
    title: "Sphyr v2 advertisement page (live)"
    published: "2026"
    accessed: 2026-11-26
  - url: "https://devanshdhaked.github.io/Product-Marketing-final-assignment/v2/linkedin.html"
    title: "Sphyr v2 LinkedIn posts page (live)"
    published: "2026"
    accessed: 2026-11-26
  - resource: "site/index.html, site/ad.html, site/linkedin.html, site/demo.html, site/deliverables.html, site/propaganda.html, site/js/*.js (branch iteration-b at b6051be, same content as v2)"
  - resource: "docs/brief/professor_feedback.md (addendum 2026-11-26)"
  - resource: "docs/product/prototype_screens.md, docs/product/product_facts.md"
generated: { by: claude-code/opus-5-5, at: 2026-11-26T09:42:09Z }
---

# v2 baseline

## Method
- Source: the HTML in `site/` on branch `iteration-b` (b6051be). It carries the v2 pages unchanged. All line numbers below are `site/<page>.html` lines.
- Live check: firecrawl markdown of the live `/v2/` home, ad and LinkedIn pages on 2026-11-26. Checked and matching the repo: home hero, problem h2, pricing and pilot text, close line; ad headline and first line; all three posts. Other parts and pages were not checked live.
- Screenshot: firecrawl screenshot at 1280 by 800 failed twice ("All scraping engines failed"). The fold is estimated from `css/home.css` (two-column hero grid, h1 up to 68px, SVG below the copy). Treat "above the fold" claims as estimates.
- Visible text was extracted line by line with a script. aria-labels are listed apart from visible text.
- Every score in this note is one auditor's judgment (n=1). No reader from the segment was tested.

## 1. First-screen test

### Rubric (use the same one for v3)
| Score | Meaning |
|---|---|
| 0 | The reader cannot answer from the text in frame. |
| 1 | The reader can answer only by inference. |
| 2 | Stated, but incomplete or in words the segment would not use. |
| 3 | Stated plainly and completely, in words the segment uses. |

Questions, asked as a managing partner of a 40 to 400 person Indian consulting firm: (a) what Sphyr is, (b) who it is for, (c) what to do next.

### Home, first screen at 1280 (hero only)
Text in frame: nav "How it works / For partners / Pricing / Deliverables / See the 2-minute walkthrough" (lines 40 to 46); H1 "The engagement ends. The evidence stays." (66); lede "Every two weeks, the people who saw a consultant's work give two minutes of feedback, and Sphyr keeps it all in one record." (68); button "See the 2-minute walkthrough" (69); top of the SVG with "Project 1 ... Project 4, 3 teammates" (74 to 77). The SVG label "Promotion round / The whole year is in the file" (79) sits near the bottom of the SVG, likely at or below the fold (estimate).

| Question | Score | Text judged | Why |
|---|---|---|---|
| (a) What | 2 | lede, line 68 | Says it collects feedback and keeps it. Does not say it is for appraisals or promotions; that only appears in the SVG label, likely below the fold. The H1 says nothing about the product. |
| (b) Who | 1 | "a consultant's work" (68), "engagement" (66) | Consulting is implied. No firm type, size, country, or buyer role (head of talent, managing partner) in frame. |
| (c) Next | 3 | "See the 2-minute walkthrough" (46, 69) | One clear action, named twice. |
| Total | 6 of 9 | | |

The (a) score of 2 rests on the lede alone. The H1 alone scores 0 on (a) and (b), which is what the professor's point 2 describes.

### Ad, headline and first line only
Text in frame: headline "The engagement ends. The evidence stays." (`ad.html:71`, repeated on the card at 95); first line "Every two weeks, the people who saw a consultant's work spend two minutes on it, so partners calibrate with the whole year in front of them." (`ad.html:81`, repeated at 96).

| Question | Score | Text judged | Why |
|---|---|---|---|
| (a) What | 1 | "spend two minutes on it" (81) | "it" is not named. No word for feedback, appraisal or review. The headline depends on the strands illustration (73 to 77) to mean anything. |
| (b) Who | 2 | "consultant's work", "partners calibrate" (81) | Consulting firm is stated through its words. Size, country and buyer role are absent. |
| (c) Next | 0 | none in frame | The call to action "Take the 2-minute walkthrough" with QR (84) sits outside the headline and first line, so it does not count here. |
| Total | 3 of 9 | | |

## 2. Professor's faults (the brief's list of 8)
All 8 are present in v2. None is fixed.

| # | Fault | Status | Evidence |
|---|---|---|---|
| 1 | No Attention at the top of home | Present | H1 at `index.html:66` is a tagline about evidence, not a statement of what the site is. The lede (68) names feedback but not the buyer, the firm type or the appraisal use. The nav (43) shows "Deliverables", a course word. |
| 2 | Vague lines | Present | The professor quoted "What goes wrong when the team moves on?". The repo h2 is "What goes wrong when the team has moved on" (`index.html:95`, no question mark). Same line, slightly paraphrased. Further lines of the same kind (auditor judgment): H1 "The engagement ends. The evidence stays." (66); "The whole year is in the file" (79); "Partners decide with the whole year of work in front of them." (204); "Careers should be earned in front of the people who saw the work." (374). |
| 3 | Statements that need long explanation | Present | The h2 at 95 is followed by a scenario paragraph (96), four scenes (98 to 101) and a before and after pair (104, 105): 238 words to explain one heading. The H1 needs a 4-project animation and the caption "Illustration. The projects are examples." (89) to read. "Most of a rating comes from the person giving it" (274) needs a footnoted statistic (277 to 279). |
| 4 | Not written from inside consultants' or the managing partner's lives | Present | The main scene (96) is written to the head of talent ("A partner asks you for the file"). "Managing partner" appears twice on home: as the person who asked for a better year (96) and as the sender of a launch note (362). No line speaks to a managing partner's own concerns (inference: attrition of strong consultants is touched once, at 101). |
| 5 | "file" and other non-product words | Present | "file": `index.html:79` and 87 (SVG, one of the two renders), 96 (twice), 104, 105 (6 in source, 5 rendered, since only one SVG copy shows); `linkedin.html:72`, 77. In the product, "file" appears only on the admin CSV import ("Choose file", prototype_screens 3.10). Also "record" (18 visible uses in page HTML plus 3 in `js/demo.js`, 21 in all; aria-labels not counted), "pooled", "evidence". Full list in section 3. |
| 6 | No AIDA order across home | Present | See the section map below: weak A, then four I blocks, D, Action, then an onboarding block after the Action, then a course rationale block, then Action again. "See the 2-minute walkthrough" appears 6 times on home (46, 69, 118, 326, 375, 388). |
| 7 | Ad headline is not an Attention line | Present | `ad.html:71` and 95 reuse the home tagline. `deliverables.html:63` states all four deliverables repeat it. The first line (81) does not say what is being sold. |
| 8 | LinkedIn posts do not stop a doomscroller | Present (judgment) | All three posts are from the Sphyr company page ("Sphyr ... Week 1 · Public", `linkedin.html:69`, 102, 173), not a person, so (inference) they give a resharer no reputation points. Openers: post 1 a named story with the tension only in line 2 ("the file on Ananya had two pages", 72); post 2 a 1906 ox-weighing fact (105), off-segment; post 3 a vendor process statement, "Before a firm signs anything with us, we agree in writing how the pilot will be judged." (176). |

## 3. Foreign words (provisional)
Method: tokenized all visible page text, removed every word that appears in `prototype_screens.md` or `product_facts.md`, read the residue (415 distinct words), then checked known terms by hand. A parallel teammate is researching consulting vocabulary; entries marked "to confirm" wait on that.

Not flagged: "How your work is landing" (product H1, Insights screen). "circle" is in the product's My Sphyr subtitle ("Keep this circle focused on people you work with regularly"), so it is a partial match; the tab name is "My Sphyr".

### Visible text
| Phrase | Page:line | Why | Tag |
|---|---|---|---|
| file | index 79 or 87 (one SVG renders), 96 (twice), 104, 105; linkedin 72, 77 | Product uses "file" only for CSV upload. Professor fault 6. | product mismatch |
| record | index 68, 294, 300, 318, 342, 343, 361; demo 63, 245; linkedin 179; propaganda 71, 102, 139, 144, 203, 216; deliverables 77; js/demo.js 14, 19 | The product calls this view "Insights" / "Performance Insights" / "Member Insights". A user who signs in will not find a "record". | product mismatch |
| evidence (tagline) | index 66; ad 71, 95; linkedin 115, 162; demo 243; propaganda 66, 144; deliverables 63 | Not a product word. | product mismatch |
| pooled, pools | index 297, 299, 300, 318; ad 106; linkedin 110; propaganda 114 | Product says "normalized and grouped", "anonymized and aggregated". | product mismatch |
| Juniors | index 170, 193 | Product group is "Subordinates". | product mismatch (likely deliberate) |
| Clients (circle group) | index 171, 194 | Product group is "External". | product mismatch (likely deliberate) |
| Strongest area | index 215 | Product tile says "Strongest signal". | product mismatch |
| Engagement team values | index 135, 144; linkedin 131 | Product label is "<team name> VBAs". | product mismatch (minor) |
| Your name is not shown with your response | index 143 | Product says "Your response is anonymized." | product mismatch (minor) |
| teammates | index 74 to 77; ad 74 to 77 | Product says "Peers" and "collaborators". | product mismatch; likely non-consulting (to confirm) |
| calibrate | ad 81, 96 | Not a product word. | product mismatch; likely real consulting vocabulary (to confirm) |
| the team has moved on | index 95 | Professor flagged it as vague. | likely non-consulting (to confirm) |
| promotion round | index 79; demo 77; linkedin 181 | Firms may say promotion cycle or year-end review. | likely non-consulting (to confirm) |
| project-end form | index 96, 100 | Firms may name this engagement review or case evaluation. | likely non-consulting (to confirm) |
| a seat a month | index 349 | SaaS buyer word. Product source says "per head". | product mismatch; likely non-consulting (to confirm) |
| Customer First, Stakeholder-centric, Innovation, Resolve dependencies sooner, Consider customer impact | index 137 to 148; linkedin 133 to 135 | Product demo tags, written for a software team. Tags are configurable (Organization VBAs, prototype 3.11), so the site may show consulting tags. | product match; likely non-consulting (to confirm) |
| Deliverables (nav, page) | every page nav, e.g. index 43; deliverables.html | Course word for the assignment parts, on the buyer's nav. | likely non-consulting usage (course word) |
| propaganda (page name), standee, handout, Journey stage, Job, Call to action, trigger, belief, tactics, storyline, campaign | propaganda.html; ad 63, 88, 102, 120 to 125; linkedin 89 to 93, 160 to 164, 196 to 200 | Course and marketing words on public pages, beside the buyer copy. | likely non-consulting usage (course words) |

### aria-labels only (not seen by sighted readers)
| Phrase | Page:line | Tag |
|---|---|---|
| strands, record line, Sphyr sphere | index 73, 81; ad 73 | product mismatch |
| Promotion round (in label) | index 73, 81 | likely non-consulting (to confirm) |

## 4. Home page section map
AIDA tags use the professor's course definitions: A (Awareness/Attention) says what the site is about; I (Interest) is the problem and assurance (guarantee, refund, manual); D (Decision) is low friction to choose; A (Action) is the step. Word counts are visible text, including labels inside figures; the hero counts one SVG copy (both `cv-wide` and `cv-compact` are in the DOM, only one renders).

| # | Lines | Heading | One-line summary | Words | Tag |
|---|---|---|---|---|---|
| 1 | 64 to 91 | H1 "The engagement ends. The evidence stays." | Tagline, one-line lede, walkthrough button, 4-project animation. | 65 | A, fails (professor point 2) |
| 2 | 93 to 108 | "What goes wrong when the team has moved on" | Head of talent scenario with a thin file, four failure scenes, today vs with Sphyr. | 238 | I (problem) |
| 3 | 110 to 160 | "Two minutes every two weeks" + h3 "Your firm's values on every card" | How the card works, with the prototype card. | 230 | I (how it works) |
| 4 | 161 to 201 | h3 "Who gets a say" | Circle of peers, seniors, juniors, clients; 14-person pilot average. | 70 | I |
| 5 | 202 to 271 | "Partners decide with the whole year of work in front of them." + h3 "For consultants", "For partners and engagement managers" | Benefit by role, with two prototype screens. | 277 | I (benefit) |
| 6 | 272 to 292 | "Most of a rating comes from the person giving it" | Three statistics (Scullen 2000, Gallup, 2018 pilot). | 96 | I (back to problem) |
| 7 | 293 to 307 | h3 "What Sphyr does not do", "What stays private" | Limits and a privacy FAQ. | 241 | I (assurance) |
| 8 | 308 to 345 | "What Sphyr costs" | Plan price, pilot offer, what a pilot measures; "Book a 20-minute call" at 334. | 179 | D, then A (Action) |
| 9 | 346 to 356 | h3 "How we set the price" | Pilot cost, competitor price, break-even, price survey. | 140 | none (course rationale) |
| 10 | 357 to 371 | h3 "What happens after you sign" | Onboarding timeline from kickoff to the first year. | 257 | I (assurance) placed after Action |
| 11 | 372 to 380 | "Careers should be earned in front of the people who saw the work." | Vision line and walkthrough button. | 17 | A (Action) |

Where the journey breaks: at row 1 (no Attention), at row 6 (the page returns to the problem after the product), and at rows 9 and 10 (rationale and assurance come after the first Action). About 1,150 of 1,810 words (rows 2 to 7) are Interest before any Decision content.

## What this means for v3
- Score v3 with the rubric in section 1, on the same frames (home hero at 1280, ad headline plus first line). v2 baseline: home 6 of 9, ad 3 of 9.
- The two lowest v2 scores are home (b) "who" at 1 and ad (c) "next" at 0. The v3 hero must name the firm type and buyer in frame; the ad's first two lines must carry a next step.
- The ad (a) score of 1 comes from "spend two minutes on it"; the v3 ad's first line must name what Sphyr is.
- Remove or replace "file" (5 rendered on home, 2 on LinkedIn) and "record" (21 visible: 18 in HTML, 3 in js/demo.js) with the product's screen names, or with the consulting terms the vocabulary research confirms.
- Re-run the residue method (page words minus product-doc words) on v3 and compare the count of mismatch entries with this table.
- Re-draw the section map for v3 and check that no Interest or assurance block sits after the first Action, and that course rationale (row 9) and course words (Deliverables, propaganda, Job, Journey stage) leave the buyer's path.
- The product tags shown on home and LinkedIn are software-team tags; since VBAs are configurable, v3 may show consulting tags without a false claim.
- Re-check all 8 faults against v3 with file and line evidence, using the table in section 2.
