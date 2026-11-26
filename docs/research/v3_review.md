---
type: Research
title: "v3 review: first-screen test, professor's faults, foreign words"
description: "An adversarial re-score of the v3 site (branch iteration-b, site/) on the three v3 success numbers, using the method of v2_baseline.md, with file and line evidence and a ranked fix list."
tags: [research, audit, review, v3, aida, vocabulary]
sources:
  - resource: "site/index.html, site/ad.html, site/linkedin.html, site/demo.html, site/deliverables.html, site/propaganda.html, site/js/demo.js, site/js/propaganda.js, site/assets/ad/walkthrough-qr.svg (branch iteration-b, working tree on 2026-11-26)"
  - resource: "http://localhost:8876/site/ (local server of the iteration-b worktree), screenshots at 1280 by 800 and 375 by 667, taken with Playwright, accessed 2026-11-26"
  - resource: "docs/research/v2_baseline.md (method and v2 scores)"
  - resource: "docs/brief/professor_feedback.md (addendum 2026-11-26)"
  - resource: "docs/decisions/decision_log.md (entries '2026-11-26: v3 plan gate' and '2026-11-26: v3 headline, sign-off and the packaging refund')"
  - resource: "docs/product/prototype_screens.md, docs/product/product_facts.md, docs/product/do_not_claim.md"
generated: { by: claude-code/opus-5-5, at: 2026-11-26T13:55:00Z }
---

# v3 review

## The three numbers
| Number | v2 | v3 | Target |
|---|---|---|---|
| First-screen test, home | 6 of 9 | 9 of 9 | 9 of 9 |
| First-screen test, ad | 3 of 9 | 9 of 9 (8 if the QR target is counted, see section 1) | 9 of 9 |
| Professor's faults still present | 8 of 8 | 2 of 8 (both partial: points 4 and 8) | 0 of 8 |
| Foreign-word entries on public pages | about 20 | 8 (1 banned word in body copy, 2 course-word entries outside the allowed pages, 5 minor) | 0 |

All scores are one reviewer's judgment (n=1), read as a managing partner of a 40 to 400 person Indian consulting firm. No reader from the segment was tested.

Biggest single defect found: the ad's QR code and printed address open the v2 walkthrough, not v3 (section "Smoke results", row 1). The builders' reports do not mention it.

## Method
- Same rubric and frames as `v2_baseline.md` section 1 (0 to 3 for what, who, next).
- Unlike v2, the fold was measured, not estimated: Playwright viewport screenshots of `site/index.html` at 1280 by 800 and 375 by 667, and an element screenshot of the standee on `site/ad.html`.
- Visible text: tags, scripts, styles and the head stripped per source line by a script; strings in `js/demo.js` added. aria-labels not counted.
- Residue: visible words minus every word in `prototype_screens.md` and `product_facts.md` (358 distinct words left), read by hand; then a watch list of the plan gate's banned words and the v2 table's terms was grepped.
- The QR code was decoded in the browser with the BarcodeDetector API.
- Sideways scroll: each page loaded in a 375 px wide frame; `scrollWidth` compared with `clientWidth`.
- Links: every distinct `href` on the six pages collected in the browser; each target page fetched from the local server (all 200); each `#id` target grepped in its page (15 of 15 found). The one external link (peopleanalyst.com) was not fetched.

## 1. First-screen test

### Home at 1280 by 800 (screenshot looked at)
In frame: nav "How it works / For partners / Pricing / Deliverables" and "Book a 20-minute call" (`index.html:39` to 45); H1 "Peer feedback for appraisals at Indian consulting firms" (65); lede (67); main button (68); pilot line (69); "See the 2-minute walkthrough" (70); top of Exhibit 1, the feedback card, cut at the fold. At 375 by 667 the H1, lede, button, pilot line and walkthrough link all fit above the fold.

| Question | Score | Text judged | Why |
|---|---|---|---|
| (a) What | 3 | H1 (65), lede (67) | Says what it is (peer feedback), what it is for (appraisals), how often and how long (every two weeks, two minutes), and who reads it (partners and engagement managers before calibration). |
| (b) Who | 3 | H1 (65), lede (67) | Firm type, country and size in frame. Head of talent, the buyer, is not named in frame; a managing partner still knows it is for their firm, so not marked down. |
| (c) Next | 3 | button (68), pilot line (69), link (70) | One main action with its cost and terms right under it. |
| Total | 9 of 9 | | |

### Ad, headline and first line (standee, `ad.html:69` to 70; same on the A6 card, 101 to 102)
Headline: "Calibration is on Monday. Half the project feedback forms are still blank." First line: "Sphyr collects peer feedback for appraisals every two weeks, for heads of talent at Indian consulting firms of 40 to 400 people. Book a 20-minute call, or scan to see the 2-minute walkthrough."

| Question | Score | Text judged | Why |
|---|---|---|---|
| (a) What | 3 | first line (70) | Names the product and its job in segment words. |
| (b) Who | 3 | first line (70) | Buyer role, firm type, country and size. |
| (c) Next | 3 | first line (70) | "Book a 20-minute call, or scan to see the 2-minute walkthrough" names the next step plainly, inside the frame. |
| Total | 9 of 9 | | |

Scoring rule: as in v2, only the headline and first line count, and the QR block sits outside that frame (v2 gave (c) 0 for the same reason). Under that rule (c) is 3. Two problems sit just outside the frame and would make (c) a 2 if counted: the standee prints no way to book the call (no phone, no booking address), and the QR and printed address open the v2 walkthrough (`.../v2/demo.html`, section 4). Both are in the fix list.

The headline itself is now an Attention line (professor's ad point): it names a week only a consulting firm's head of talent knows.

## 2. Professor's faults
| # | Fault | v3 status | Evidence |
|---|---|---|---|
| 1 | No Attention at the top of home | Fixed | H1 `index.html:65` states product, use and segment; lede 67 adds size and readers. |
| 2 | Vague lines | Fixed | Problem h2 is now "What happens at calibration today" (117), followed by four concrete scenes (119 to 122). "The engagement ends. The evidence stays." and "the whole year is in the file" are gone from home and ad. Residue: "the whole year" stays on `propaganda.html:70`, 108, 127, 212 (course page, low cost). |
| 3 | Statements that need long explanation | Fixed | Problem section is 57 visible words (114 to 125), no footnoted statistic on home. Each step in section 2 is one h3 and one or two sentences (131 to 138, 168 to 171, 205 to 208). |
| 4 | Not written from inside the reader's life | Partly present (judgment) | The problem scenes use the reader's own room: staffing partner carries the weight (119), recency (120), "rolled off" (121), HR chasing forms (122). The managing partner persona lists three fears: good juniors leaving, "partiality" in exit interviews, partner time (`docs/strategy/persona_managing_partner.md:35` to 38). Home touches partiality (119) and partner time ("two minutes", 67), but no line names the first fear, a good consultant who leaves. LinkedIn post 1 comes close ("The designation waits another cycle, and so does the hike.", `linkedin.html:76`); home does not. |
| 5 | "file" and other non-product words | Fixed | "file", "record", "evidence", "pooled", "teammates", "subordinates", "VBAs", "resources": 0 visible hits on public pages. Minor residue in section 3. |
| 6 | No AIDA order across home | Fixed | Section map below: A, I, I, I (assurance), D, A. No Interest or course rationale after the Action; price rationale and onboarding moved to `deliverables.html:99` to 126. |
| 7 | Ad headline is not an Attention line | Fixed | `ad.html:69` and 101, new line, not the home tagline. |
| 8 | LinkedIn posts do not stop a doomscroller | Partly present (judgment) | Openers are better: post 1 "Four people saw the workshop. None were in calibration." (72), post 2 "One manager writes the rating for four projects." (104). Post 1 ends with a question a partner can answer from experience (77), which earns reputation points. Still present: all three posts come from the Sphyr company page (69, 101, 178); post 2 keeps the 1906 ox paragraph (107) that the v2 baseline called off-segment; post 3 opens on "the pilot" (181), which a reader who has never heard of Sphyr does not own yet. |

## 3. Foreign words (residue)
Allowed and not counted: "Deliverables" in the nav; course words on `propaganda.html` and `deliverables.html`; product role and screen names in exhibit captions and exhibits ("Member role", "Peers", "collaborators", "signals", "normalized"); "engagement manager"; "Fortnightly Feedback", "Insights", "Team Insights", "Member Insights" when naming a screen.

| Phrase | Page:line | Why | Tag |
|---|---|---|---|
| Member Insights, Member role (in body copy) | demo 63 (lede), 168 (h2), 169; deliverables 118; js/demo.js 14, 79, 81 | "member" is on the plan gate's banned list. The brief allows role names in exhibit captions only, and the plan gate's screen-name allowance names "Fortnightly Feedback" and "Insights", not "Member Insights". It is the real screen name, so this is a lead decision: exempt it in writing, or write "a consultant's Insights screen". | banned word in body copy (lead decision) |
| Journey stage, trigger | ad 133 | Course words on the ad page, which is not the propaganda page or hub. | course word outside allowed pages |
| Job, Journey stage, Call to action, Attention, Interest, Decision, recognition | linkedin 88 to 92, 165 to 169, 206 to 210 | Same, on the post notes beside each mockup. | course word outside allowed pages |
| circle | demo 106, 169 (twice); deliverables 119, 120; js/demo.js 13, 18 | Product tab is "My Sphyr"; "circle" only appears in its subtitle. Firms say "the people you work with" or "your project team". | partial product match, likely non-consulting |
| turnout | index 226 | Product KPI is "Participation". | product mismatch (minor) |
| landing (not as the screen title) | deliverables 121 "how the project team is landing" | The product phrase is "How your work is landing", for one person. Used for a team it reads vague. | vague (minor) |
| the whole year | propaganda 70, 108, 127, 212 | The v2 vague phrase class. On the course page, so low cost. | vague (minor) |
| The 20-minute call | propaganda 223 | A call button with a label other than "Book a 20-minute call". | label drift (minor) |

v2 had about 20 entries, most of them product mismatches in buyer copy. v3 has none in buyer copy on home; what is left is course labels on two deliverable pages and four minor words.

## 4. Smoke results
| Check | Result | Evidence |
|---|---|---|
| Links in the ad point at /v3/ | FAIL | QR `assets/ad/walkthrough-qr.svg` decodes to `https://devanshdhaked.github.io/Product-Marketing-final-assignment/v2/demo.html`. Printed address `/v2/demo.html` at `ad.html:73`, 105, 118. `og:url` and `og:image` at `ad.html:22`, 23 also `/v2/`. Decision log "v3 plan gate", Submit URL point, requires /v3/. |
| No partner role claimed | Pass | Partners appear as people "who have the Manager role" (`index.html:170`); `demo.html:169` "a screen for the Manager role". |
| Admin has no results view | FAIL (likely, one line) | `deliverables.html:121`: "The head of talent sees how much of each team has given feedback". Participation is a Team Insights tile (`prototype_screens.md:87`), a Manager view. The four Admin screens (118 to 140) show a directory, VBA tags, the cadence and OKRs, with no response counts; the Feedback Frequency subtitle mentions "submission tracking" (132) but the screen shows only the schedule. Home is correct (`index.html:207`). |
| No "anonymous" overclaim | Pass | 0 hits for "anonymous". "anonymized" is used with the edit-request caveat (`index.html:224`, `ad.html:113`). |
| At most one "X, not Y" per page | Pass | One per page: the sign-off (`index.html:263`, `ad.html:92`, `propaganda.html:66`) or `demo.html:64` (disclaimer). |
| No month names | Pass | 0 in visible text. |
| No customer claims | Pass | None found. |
| No em or en dashes | Pass | 0 in the six public HTML files and `js/demo.js`. |
| Main button label exactly "Book a 20-minute call" | Pass, one drift | Every `call-note` button on every page uses it, except the flow item "The 20-minute call" at `propaganda.html:223`. |
| One secondary link | Pass, one extra | "See the 2-minute walkthrough" is the only secondary call link. `linkedin.html:222` adds "Next: the advertisement" (page navigation, not a call). |
| Every internal link resolves | Pass | All `href` targets exist on the six pages; all `#id` targets exist. |
| No sideways scroll at 375 | Pass | `scrollWidth` = `clientWidth` = 375 on all six pages. |

## 5. Home page section map (v3)
Tags use the course definitions as in `v2_baseline.md` section 4. Word counts are visible text including exhibit labels.

| # | Lines | Heading | One-line summary | Words | Tag |
|---|---|---|---|---|---|
| hero | 63 to 112 | H1 "Peer feedback for appraisals at Indian consulting firms" | What, who, call button with pilot line, walkthrough link, Exhibit 1 feedback card. | 199 | A (with an early Action) |
| 1 | 114 to 125 | "What happens at calibration today" | Four scenes from the calibration room. | 57 | I (problem) |
| 2 | 127 to 216 | "Two minutes every two weeks" | Feedback card, consultant's Insights, partners' Team Insights, head of talent setup, four key numbers; Exhibits 2 and 3. | 445 | I (how it works) |
| 3 | 218 to 229 | "What you get and what stays private" | Setup, training, materials, privacy, results ownership, what a pilot measures. | 115 | I (assurance) |
| 4 | 231 to 252 | "Price and pilot" | Pilot fee credited to the first bill, plan price, worked example. | 100 | D |
| 5 | 254 to 265 | "Talk to us before your next appraisal cycle" | Call button, pilot line, walkthrough link, sign-off. | 49 | A (Action) |

Caveat: the hero count includes the exhibit's hidden "Could improve" and "No interaction" steps (`index.html:93` to 101, shown only when a reader picks them), about 45 words; v2 counted rendered text only. The rendered hero is about 155 words.

The order is A, I, I, I, D, A with no block after the Action. Interest before Decision is about 617 words (v2: about 1,150). Section 2 holds 46 percent of the page's words; it is the one place a skimmer could stall.

## What still needs fixing
Ranked by how much each would cost the grade.

1. `site/assets/ad/walkthrough-qr.svg`, `ad.html:73`, 105, 118 (and `ad.html:22`, 23): the QR and printed address open the v2 walkthrough. Regenerate the QR for `/v3/demo.html` and change the three printed addresses and the two meta tags to `/v3/`.
2. `ad.html:70`, 102: the ad asks for a call but prints no way to book one. Either point the QR at a /v3/ page whose first button is the call and say "Scan to book a 20-minute call", or print a booking address. A grader who reads past the first line will notice.
3. `deliverables.html:121`: the head of talent is said to see participation, which only the Manager role sees. Give the line to engagement managers, or say "if the head of talent also has the Manager role".
4. `index.html:118` to 123: add one scene with the managing partner's own cost (a strong consultant misses a designation and leaves), in the words post 1 already uses (`linkedin.html:76`). Closes fault 4.
5. `linkedin.html:107`: cut the 1906 ox paragraph; the line at 104 already makes the point. Consider posting from a named founder's profile instead of the company page (69, 101, 178). Closes most of fault 8.
6. `demo.html:63`, 168, 169; `deliverables.html:118`; `js/demo.js:14`, 79, 81: "Member Insights" in body copy uses a banned word. Lead decision: record an exemption for the screen name, or write "a consultant's Insights screen".
7. `ad.html:133`, `linkedin.html:88` to 92, 165 to 169, 206 to 210: course labels outside the allowed pages. Rename to plain labels ("What it is for", "Where the reader is", "What we ask") or have the lead record them as allowed annotations. The grader may want these labels, so this is a lead decision.
8. `demo.html:106`, 169; `deliverables.html:119`, 120; `js/demo.js:13`, 18: replace "circle" with "the people they work with" or the product's "My Sphyr".
9. `index.html:226`: "Turnout" to "Participation", the product's word.
10. `propaganda.html:223`: label "The 20-minute call" to "Book a 20-minute call".
11. `deliverables.html:121`: "how the project team is landing" to "how the project team is rated".

## What this means for v3
- Fix the ad QR and the three printed /v2/ addresses before anything else; a grader who scans the standee lands on the site the professor rejected.
- Give the standee a printed way to book the call; the ad scores 9 of 9 only because the v2 rule ignores the QR block.
- Correct `deliverables.html:121` so no page gives the Admin role a results view.
- Add one managing-partner cost scene to the home problem list to close fault 4.
- Cut the ox paragraph from post 2 and decide on a person, not the company page, as the post author to close fault 8.
- Lead decisions needed: course labels on the ad and LinkedIn pages, and "Member Insights" in body copy; rename, or record them as allowed.
- Swap "circle" and "turnout" for product or segment words; these are the last word-rule misses in buyer-facing text.
- Home first screen needs no change: 9 of 9 at both 1280 and 375.
