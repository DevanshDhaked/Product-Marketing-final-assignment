---
type: Handoff
title: "v3 home page builder report"
description: "Home rebuilt as one A-I-D-A path in direction A: plain headline for Indian consulting firms, captioned product exhibits, key numbers, pilot-first pricing, call-first close and the graded-message sign-off."
tags: [handoff, home3]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T14:05:00Z }
---

# v3 home page builder report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Teammate: home3, Depth 1. Worktree `Product-Marketing-final-assignment.d1-home3`, branch `d1-home3`. Started 2026-11-26.

## Plan

### Success number
First-screen rubric (`docs/research/v2_baseline.md` section 1): 9 of 9 at 1280 by 800 and at 375 by 667, judged as a managing partner in 10 seconds. v2 scored 6 of 9. I report this number first in every update.

### Files
- `site/index.html`: rebuilt as one A-I-D-A journey. Nav markup unchanged except the nav button, which becomes `<button class="btn btn-primary" type="button" popovertarget="call-note">Book a 20-minute call</button>`. Footer and `#call-note` unchanged.
- `site/css/home.css`: rewritten for the new sections.
- `site/css/base.css`: additive only. One new token, `--ink: light-dark(#RRGGBB, #RRGGBB);` on one line (a deep green for light, a pale green ink for dark), plus new classes: `.exhibit` and its caption, `.sec-num` (section number in the left margin column), `.report` (12-column grid, 7-column reading measure, exhibits on 9 or 12 columns), `.keynums` (key-numbers row), `.pilot-line` (the line under a main button). I will not change existing rules, so other pages look the same until they opt in.
- `docs/design/design_system.md`: one dated addendum for the direction A tokens and classes.
- `docs/design/references.md`: one dated addendum replacing the studio references with RBB Economics, Hafnia Law, Barber Hauler and Redseer.
- `site/index.html` head: `og:url` and `og:image` move from `/v2/` to `/v3/`; title and description rewritten without "engagement" or "record".
- `css/motif.css` and `js/motif.js` links are removed from index.html, because they only drive the hero ribbon (`data-replay`, `.cv`) and the circle figure (`data-circle`, `.circle`), and both leave the page. The nav and footer logo use `.mark` from base.css, so they are not affected.

### Hero draft (section 1, Attention), verbatim
- H1: "Peer feedback for appraisals at Indian consulting firms of 40 to 400 people" (13 words)
- Lede: "Every two weeks, the people on each project give two minutes of feedback. Partners and the head of talent see it before calibration." (23 words)
- Main button: "Book a 20-minute call" (opens `#call-note`)
- Pilot line under it: "Start with a 12-week pilot for up to 40 people: ₹25,000 plus GST, credited to your first annual bill." (19 words)
- Secondary link: "See the 2-minute walkthrough" (to `demo.html`)
- Exhibit 1 beside the copy at 1280, under it at 375 (below the fold there).

Total text in the first screen is about 60 words, over the 25-word target in the slop rules (a target, not a limit). The slop rules also cap the hero at four text elements and 20 words of subtext. I count the pilot line as button microcopy, since the common brief requires it under every main button. Flagged for the lead.

Self-score (n=1, my judgment, to be redone on the screenshots):
- (a) What: 3. "Peer feedback for appraisals" plus the lede's two-week cycle.
- (b) Who: 3. All four parts are in the H1 and lede: consulting firm, 40 to 400 people, India, and the buyer roles (partners, head of talent).
- (c) Next: 3. One main button with its pilot line, one secondary link.

At 375 by 667 the nav, H1 (about four lines at 36px), lede, button, pilot line and walkthrough link must all sit above the fold. If they do not fit, I cut the lede first, never the who-words.

Alternative hero for the user (not my first choice): H1 "Peer feedback for appraisals at consulting firms", lede "For Indian firms of 40 to 400 people. Every two weeks, the people on each project give two minutes of feedback, ready for partners and the head of talent at calibration." Shorter H1, but the lede carries more and runs to 31 words.

### Section order
Sections after the hero carry a plain number in the left margin column (1 to 5), at body size, not uppercase.

| # | Id | Stage | Job | Layout family | Exhibit |
|---|---|---|---|---|---|
| Hero | `hero` | Attention | What Sphyr is, for whom, the next step | Split: copy left, exhibit right | Exhibit 1, Fortnightly Feedback |
| 1 | `problem` | Interest (problem) | One appraisal scene in their words, four short lines | Document column, 7-column measure | None |
| 2 | `how` (with `partners` on the partner step) | Interest (how it works) | Every two weeks the project team gives feedback; what the consultant sees; what partners and engagement managers see; what the head of talent sets up. Then the key-numbers row | Numbered steps beside wide exhibits, then a numbers row | Exhibit 2, Insights; Exhibit 3, Team Insights |
| 3 | `assurance` | Interest (assurance) | What is included, what stays private, what happens to pilot data, what a pilot measures | Labelled rows | None |
| 4 | `pricing` | Decision | Plan and pilot side by side; the pilot credit as the coupon; one line each for decided terms | Unequal pair (pilot block weighted with the ink green) | None |
| 5 | `call` | Action | Same main button and pilot line, walkthrough link, sign-off line | Document column, left aligned | None |

Nothing follows section 5 except the footer. The ids `how`, `partners` and `pricing` stay, because the nav links to them.

Problem draft (section 1), four lines:
- "At calibration, the partner you are staffed with now carries the most weight."
- "Recent projects count for more than the ones before them."
- "A consultant who rolled off a project months ago has nobody to present the case."
- "HR is still chasing feedback forms in the week the ratings close."

Key numbers (only from product and pricing docs, each with its source in the same block):
- 2 minutes: time per person every two weeks (product guide, DOC p2).
- Every 2 weeks: the default feedback cycle (prototype, Admin Feedback Frequency, "Fortnightly" default).
- 14 people: average circle in the 2018 paper-and-pen pilot run by Sphyr's founder (whitepaper v0.3, p3).
- 12 weeks: pilot length, six cycles (our pricing, `docs/pricing/price_and_pilot.md`).

### v2 blocks and what happens to each
| v2 block | Fate |
|---|---|
| Hero tagline H1 and ribbon animation (`cv1`, `cv1c`, "Play again") | Dropped. Tagline is rewritten into the sign-off. No ribbon figure on home. |
| Problem scenes (238 words, "file" six times, today and with Sphyr pair) | Rewritten as four lines in section 1. |
| How it works text and feedback card | Card moves to the hero as Exhibit 1. Text rewritten into section 2, step 1. |
| "Who gets a say" circle figure (strand colours, group buttons) | Dropped. The 14 becomes a key number. Ribbon colours stay in the logo only. |
| "Partners decide with the whole year..." with Insights and Team Insights frames | Rewritten. Frames kept as Exhibits 2 and 3 in section 2. |
| Scullen and Gallup statistics, 02:09 stat | Dropped. Key numbers come only from product or pricing docs. |
| "What Sphyr does not do" | Dropped. It uses "record" and "AI", and the brief's assurance list does not need it. |
| "What stays private" and the FAQ | Rewritten as one labelled row in section 3, with accurate wording. The FAQ goes. |
| "What Sphyr costs" plan and pilot cards | Rewritten in section 4. Buttons inside the cards are removed (see open questions). |
| "What a pilot measures" | Kept, shortened, as a row in section 3. |
| "How we set the price" | Removed from home. Text pasted verbatim under `## For T4` in this report. |
| "What happens after you sign" (onboarding timeline, 257 words) | Removed from home. Text pasted under `## For T4` so the lead can place it. |
| Close "Careers should be earned..." and walkthrough button | Replaced by section 5. |

### Exhibits and what changes inside each frame
Captions sit below the frame, one sentence-case line, with the existing sample line as the source: "Prototype screen. Sample data, fictional people."
- Exhibit 1. Fortnightly Feedback. Caption draft: "Exhibit 1. Fortnightly Feedback, Member role: rating one person from the project." Changes: "Member B" becomes a fictional sample name with consulting title and product group ("Associate Consultant · Peers"). The "Engagement team values" tag is removed (the product label is "<team> VBAs", a banned word). Chips become firm values from the product guide examples and consulting behaviours (for example Integrity, Quality of Work, Client first, Takes initiative). The friction subtitle uses the product string "Your response is anonymized." The radio interaction stays (CSS only).
- Exhibit 2. Insights. Caption draft: "Exhibit 2. Insights, Member role: what a consultant sees after six cycles." Changes: "Strongest area" becomes the product's "Strongest signal".
- Exhibit 3. Team Insights. Caption draft: "Exhibit 3. Team Insights, Manager role: how the project team is rated, with edit requests waiting." The edit requests tile stays visible, so the frame does not suggest full anonymity. Member Insights is not used, because it puts scores next to named people.
- Head of talent: copy says the head of talent, with the Admin role, sets the firm's values and the two-week cycle. It does not say Admin shows results, because Admin screens are configuration only.

### Pricing (section 4), line by line
Decided, used:
- ₹149 per employee per month, billed yearly, plus GST; same rate for every employee and firm size (`price_and_pilot.md` line 44).
- New joiners billed from the month they join; clients you invite give feedback free ("What the price includes").
- Example: a 150-person firm pays ₹22,350 a month, plus GST (`pricing_summary.md` line 29).
- Pilot: 12 weeks, six cycles, up to 40 people, ₹25,000 plus GST (line 45).
- The coupon: the ₹25,000 comes off the first annual bill if the firm signs (line 45).
- If the firm does not sign: its ratings and comments as a CSV file, the rest deleted, the fee is not returned (line 46 and "If the firm does not sign").
- Results stay with the firm unless it agrees to share them ("Publishing results", consent only).
- Included: setup, training and training materials, support (WP p6 to p7, `product_facts.md` 1.15).

Not decided, left out, listed in the final report: any minimum seat count; whether a seat means every employee or only people enrolled in Sphyr; what happens if the firm leaves after the annual plan; how long the credit stays open; how many days the CSV and the deletion take.

### Checks and process
1. Load `design-taste-frontend` and `stageshow` before writing markup.
2. Phase 1: `--ink` token and new classes in base.css, the hero and Exhibit 1. Screenshots at 1280 light, 1280 dark and 375 light into `.swarm/tmp/home3/`. Commit. Write `## Phase 1 done` with the screenshot paths and the hero text verbatim. Stop.
3. Phase 2 only after "phase 2 approved": sections 1 to 5, the two doc addenda, checks, commits, `## Final`.
4. Every visible string goes through the `humanizer:humanizer` skill before commit.
5. Smoke checks: `copy_scan.py` and `copy_tells.py` on `site/index.html`, links resolve, no sideways scroll at 375, the screenshots above. Known scanner hits on real product strings inside frames ("Nothing to review", "24 of 25 reviews given") are kept and listed, because the product uses them. Page copy avoids "review" and "reviews", which the scanner reads as social proof.
6. Commits: one per logical group, explicit files, single plain git commands.

### Open questions (each with my default)
1. Role-label collision. The brief bans "member" for people but requires real role labels. Default: the capitalised role names (Member, Manager, Admin) appear only in exhibit captions and in one line about who sees what, never as a word for people.
2. Ink green scope. Default: `--ink` is added to base.css, but only home applies it to headings and rules (through home.css), so other pages do not change until their teammates opt in. Alternative: apply it to all h1 and h2 in base.css now.
3. Buttons in the price block. Default: none, so the page has one main ask, in the hero and the Action only. The Action section sits right after the price block.
4. Contrast script. Slop rule 9 says to run `node design-lab/contrast.mjs` when a token changes; the common brief says no contrast audits. Default: run the existing script once for the new token, no other audit.
5. Partners on product views. Default: copy says "partners and engagement managers with the Manager role see Team Insights". This assumes the firm gives partners the Manager role, which the product allows but does not state.
6. "The fee is not returned" on the pilot card. Default: keep it, since the term is decided and the brief asks for what happens if the firm leaves. "Refund" cannot be used (scanner).
7. Onboarding timeline. Default: off home, text pasted under `## For T4`.
8. `og.png` may still show the v2 tagline. I do not own the asset. Default: leave it and list it under Not done.

### Sign-off candidates (user picks; first choice goes on the page)
1. "The project ends. The feedback stays." (first choice: closest to the old line, in the segment's words)
2. "Every project counts at appraisal time."
3. "Rated by the people who saw the work, on every project."

"Review" is left out of all three because the copy scanner reads it as social proof.

Waiting for "approved" or changes.

## Paused (resume point)

Paused on 2026-11-26 at the lead's request, during Phase 1. The lead approved the plan with these changes: do not run contrast.mjs; take `--ink` from an existing product green in base.css; pricing copy says "a CSV export of its ratings and comments" and never "file"; defaults for Q1, Q2, Q3, Q5, Q6, Q7 and Q8 approved; use sign-off choice 1 for now.

Done:
- Loaded the `design-taste-frontend` and `stageshow` skills. Design read: an editorial report landing page for consulting partners, native CSS, dials 4 / 1 / 4 (a still page with feedback motion only).
- `site/css/base.css`: added the token `--ink: light-dark(#005B38, #A4E9CB);` after `--link`. These are the values of `--on-positive-soft`, a text green that is already tested. Committed as WIP.

Half done: none. No other file has been touched.

Not started (Phase 1):
- `site/css/base.css`: new classes `.exhibit` with `.exhibit-cap` (a caption below the frame, no bold label, with the sample line as its source), `.report` (12-column grid), `.sec-num` and `.pilot-line`. Add them as a new block at the end of the file.
- `site/css/home.css`: replace the hero rules (lines 12 to 34). The H1 spans the full width on two lines at 1280. Row 2 puts the copy in 5 columns and Exhibit 1 in 7. Apply `--ink` to `.home h1, .home h2`. The old `.hero h1 em` rule at line 47 goes.
- `site/index.html`:
  - Nav button: change it to `<button class="btn btn-primary" type="button" popovertarget="call-note">Book a 20-minute call</button>`.
  - New hero with the text in the Plan.
  - Pilot line: "Start with a 12-week pilot for up to 40 people. ₹25,000 plus GST, taken off your first annual bill if you sign."
  - Move the feedback card figure out of `#how` into the hero as Exhibit 1. Inside the card:
    - Use a fictional sample name with "Associate Consultant · Peers".
    - Remove both "Engagement team values" tags.
    - Use consulting chips such as Integrity, Client First and Quality of Work.
    - The friction subtitle becomes the product string "Choose the clearest signals. Your response is anonymized." (`prototype_screens.md` 3.3).
    - The satellite text becomes the product string "Individual responses are normalized and grouped before anyone sees them."
  - Head: new title and description; `og:url` and `og:image` move to `/v3/`.
  - Keep the motif.css and motif.js links until Phase 2, because the old circle figure is still on the page during Phase 1.
- Humanizer pass on the visible strings, then the smoke checks and screenshots (1280 light, 1280 dark, 375 light) to `.swarm/tmp/home3/`, then commit, then `## Phase 1 done`.

Exact next step: add the new classes block at the end of `site/css/base.css`.

Decisions since the plan: `--ink` values as above. The pilot line wording above (adds "if you sign"). Use the product strings in Exhibit 1 instead of the v2 site wording.

## Resumed

Resumed on 2026-11-26 from the resume point above. Next step taken: add the new classes block at the end of `site/css/base.css`. Plan and lead changes unchanged.

## Phase 1 done

Success number: first-screen rubric 9 of 9 at 1280 by 800 and at 375 by 667 (n=1, my judgment from the screenshots below; the lead and the user re-score). What 3, who 3, next 3.

Commits on `d1-home3`:
- `ad0e0ff` WIP: `--ink` token in `site/css/base.css` (before the pause).
- `ea3163a` `site/css/base.css`: direction A classes `.report` (12 columns, column 1 for the number, reading text on 7, `.span-9`, `.span-12`; one column below 760px), `.sec-num`, `.exhibit` with `.exhibit-cap` and `.src` (caption below the frame over an ink hairline), `.pilot-line`. Additive only.
- `45ec3db` `site/index.html` and `site/css/home.css`: new hero with Exhibit 1, nav button "Book a 20-minute call" (opens `#call-note`), `.home h1, .home h2` in `--ink`, new title and description, `og:url` and `og:image` on `/v3/`. The feedback card moved from `#how` into the hero. The ribbon figure and its "Play again" control are gone from the hero. motif.css and motif.js stay linked until Phase 2 (the circle figure is still on the page).

Hero text, verbatim:
- H1: "Peer feedback for appraisals at Indian consulting firms of 40 to 400 people"
- Lede: "Every two weeks, the people on each project give two minutes of feedback. Partners and the head of talent see it before calibration."
- Main button: "Book a 20-minute call"
- Pilot line: "Start with a 12-week pilot for up to 40 people. ₹25,000 plus GST, taken off your first annual bill if you sign."
- Secondary link: "See the 2-minute walkthrough" (to `demo.html`)
- Exhibit 1 caption: "Exhibit 1. Fortnightly Feedback, Member role: rating one person from the project." Source line: "Source: Sphyr prototype screen. Sample data, fictional people."
- Title and og:title: "Sphyr: peer feedback for appraisals at consulting firms"

Inside Exhibit 1: sample person "Ananya Rao, Associate Consultant · Peers" (fictional); both "Engagement team values" tags removed; chips Integrity, Client First, Quality of Work (org values from the product guide, DOC p3), with the v2 behaviours and attitudes kept; friction subtitle "Choose the clearest signals. Your response is anonymized." and satellite "Individual responses are normalized and grouped before anyone sees them." (both product strings, `prototype_screens.md` lines 68 and 74). Radio interaction unchanged (CSS only).

Checks:
- Humanizer pass on the new strings: no changes. The pilot line's second sentence is a fragment; kept as the lead approved it.
- `copy_scan.py`: 262 strings, 0 unreviewed hits. `copy_tells.py`: 0 contrasts, 5 possible triads, all in v2 sections Phase 2 replaces or in the footer names.
- 1280: H1 on two lines (126px tall); copy, button, pilot line and link above the fold; Exhibit 1 runs past the fold, its caption below it.
- 375 by 667: no sideways scroll (scrollWidth 375). Bottoms: H1 250, button 448, pilot line 528, walkthrough link 580, all above 667. Exhibit 1 starts below the link.

Screenshots (`Product-Marketing-final-assignment.swarm/tmp/home3/`):
- `p1_1280_light.png`
- `p1_1280_dark.png`
- `p1_375_light.png`
- `p1_1280_exhibit1.png` (the exhibit with its caption)

Notes for review:
- At 375 the pilot line ends with "you sign." alone on its third line.
- `#how` now holds text only until Phase 2 rebuilds it.
- First-screen word count is about 60 (over the 25-word target), as flagged in the Plan.
- Playwright may only write inside the worktree, so screenshots were taken into `.playwright-mcp/` (ignored by git) and moved to `.swarm/tmp/home3/`.

Stopped. Waiting for "phase 2 approved".

### Phase 1 addendum (after self-review)

- Product-truth flag on the lede, for the lead to decide. Do not ship without a decision. "Partners and the head of talent see it before calibration" may overclaim. `docs/product/prototype_screens.md` line 144 says: "No HR/leadership org-wide performance dashboard beyond admin config and manager team views." The Admin role (head of talent) has configuration screens only. It holds no results view unless the firm also gives that person the Manager role. I did not change the hero, because the lead approved it verbatim. Proposed fix: "Every two weeks, the people on each project give two minutes of feedback. Partners see it before calibration." The head of talent's part (setting up the firm's values and the two-week cycle) moves to section 2. Alternative: keep the line and add in section 2 that the head of talent sees results with the Manager role. This rests on the same assumption as plan Q5.
- Exhibit 1 at 375 checked: `p1_375_exhibit1.png` in the same folder. The compact design applies (tile subtitles hidden, chip groups stacked, the satellite clear of the name). The sticky nav covers the top of the satellite in this element capture only. At 375 the card has empty space at its foot, because the three answer steps share one cell sized to the tallest.
- For Phase 2: the nav comment in `site/css/base.css` (lines 171 to 174) still describes a "walkthrough button" that hides below 760px. Rewrite it when base.css is next touched, since other teammates copy this nav.

## Phase 2 (started 2026-11-26)

Lead approved Phase 2 with changes: (1) lede becomes "Every two weeks, the people on each project give two minutes of feedback. Partners and engagement managers see it before calibration."; the head of talent's part (sets the firm's values and the two-week cycle, Admin role) goes in section 2. (2) H1 stays as is until the lead says otherwise. (3) Fix the base.css nav comment. (4) Avoid the 375 orphan "you sign." with a small wording change if one does it.

## For T4

Removed from home in Phase 2, pasted verbatim (HTML stripped) from `site/index.html` at commit `45ec3db`, for the lead to place. Both are course rationale or after-sale detail, not the buyer's path.

### How we set the price (was a disclosure in the v2 pricing section)

The pilot fee covers what a pilot costs us to run, about 30 hours of our team's time plus 12 weeks of running costs. At the plan rate, the same pilot would bring in about ₹16,500, which is less than that.

- ₹149 is about a third of the cheapest standalone appraisal software we found. That is PerformYard, whose published price for firms of a few hundred people is about ₹464 a seat a month.
- At this rate, about 49 firms of 150 people cover our fixed costs.
- We think six fortnightly cycles is about the fewest that show partners a pattern they can use, so the pilot runs 12 weeks.
- A price survey of heads of talent and partners will decide whether ₹149 changes. A change would apply only to firms that sign after it.

### What happens after you sign (was the onboarding timeline at the end of the v2 pricing section)

Your first cards go out on a date you agree with us. Here is what each person gets, and when.

- Before the first cycle: In a short kickoff with our team, your head of talent adds the firm's own values, and those words become the tags on every card. Together you pick the day the first cycle opens.
- Also before it opens: We show your partners a sample record built from people on four engagements, then the same screen for their own practice, still empty. It starts filling from the date you picked, and the decisions stay with them.
- The week before: The managing partner sends each consultant a note. Each consultant then adds the people they work with closely to their circle.
- The first cycle: One card per person in your circle, about two minutes in all. While you fill in theirs, they are filling in yours.
- After a few cycles: Consultants start to see what their colleagues noticed, along with the notes written to them. Engagement managers see how the current team is landing while the work is still going on, and your head of talent sees who took part, team by team, without chasing anyone.
- Every two weeks after that: A new set of cards. Over time each person builds up a line showing how their work is landing.
- After the first year: Our team goes through the year with you, including voluntary exits against the year before if you agree. You decide on renewal from your own results.

## Final

Success number: the first screen scores 9 of 9 on the rubric at 1280 by 800 and at 375 by 667 (n=1, my judgment from the screenshots; the lead and the user re-score). At 375 the walkthrough link ends at 580 px of 667.

### Files and commits (branch `d1-home3`)
| SHA | Files | What |
|---|---|---|
| `ad0e0ff` | `site/css/base.css` | `--ink` token (WIP, before the pause) |
| `ea3163a` | `site/css/base.css` | `.report`, `.sec-num`, `.exhibit`, `.exhibit-cap`, `.pilot-line` |
| `45ec3db` | `site/index.html`, `site/css/home.css` | Phase 1: hero with Exhibit 1, nav button, ink headings, v3 head tags |
| `ad9c271` | `site/css/base.css` | `.keynums`; section number on the heading's first baseline; `.pilot-line` balanced; nav comment rewritten for the call button |
| `4592f61` | `site/index.html`, `site/css/home.css` | Phase 2: sections 1 to 5, Exhibits 2 and 3, the new lede, motif.css and motif.js unlinked, home.css rewritten (271 lines out, 113 in) |
| `51f40fd` | `docs/design/design_system.md`, `docs/design/references.md` | Dated addenda: direction A tokens and classes; RBB Economics, Hafnia Law, Barber Hauler and Redseer as the references |
| `1385616` | `site/index.html` | Problem line 1 uses the consultant's role, not "you" (see key decisions) |
| `fd6a059` | `site/index.html` | Lead's mid-phase change: Exhibit 1 tags "Client handling" and "Share updates sooner" |
| `db1cf6f` | `docs/design/references.md` | The four new references added to the `sources` frontmatter (additive) |
| `b699f1d` | `site/index.html` | User's decision: new H1 and lede (see "User decision on the hero" below) |
| `dc8e4b8` | `site/index.html` | User's decision: new sign-off (see "User decision on the sign-off" below) |

### User decision on the hero (applied 2026-11-26)
- H1: "Peer feedback for appraisals at Indian consulting firms"
- Lede: "For firms of 40 to 400 people. Every two weeks, the people on each project give two minutes of feedback. Partners and engagement managers see it before calibration."
- Title and descriptions unchanged. The title "Sphyr: peer feedback for appraisals at consulting firms" and the descriptions (the old lede without the firm size) do not repeat the old H1.
- Sign-off unchanged: "The project ends. The feedback stays."
- Checks: `copy_scan.py` 0 unreviewed hits; `copy_tells.py` 0 contrasts, 1 possible triad (the footer names).
- Fold, measured bottoms in px:
  - 1280 by 800: H1 238, lede 422, button 490, pilot line 546, walkthrough link 590.
  - 375 by 667: H1 210 (three lines), lede 378, button 438, pilot line 518, walkthrough link 570.
  - Nothing up to and including the walkthrough link drops below the fold at 375; it ends 97 px above it. No sideways scroll (scrollWidth 375).
- Screenshots, looked at: `p3_1280_light.png` and `p3_375_light.png` in `.swarm/tmp/home3/`. At 1280 the H1 now runs two lines on about two thirds of the width. At 375 the top of Exhibit 1 shows at the fold.

### Page order (as built)
Hero (Attention): H1, lede, "Book a 20-minute call", pilot line, "See the 2-minute walkthrough", Exhibit 1 (Fortnightly Feedback, Member role).
1. `problem`: "What happens at calibration today", the four lines from the Plan.
2. `how`: "Two minutes every two weeks". Four steps: the project team gives feedback (points to Exhibit 1); the consultant sees Insights (Exhibit 2, Member role); partners and engagement managers with the Manager role see Team Insights (`#partners`, Exhibit 3, Manager role); the head of talent, with the Admin role, sets the firm's values and the two-week cycle and adds people from a spreadsheet. Then the key-numbers row: 2 minutes, 2 weeks, 14, 12 weeks, each with its source.
3. `assurance`: "What you get and what stays private". Rows: setup and training, what stays private, your results, what a pilot measures.
4. `pricing`: "Price and pilot". The pilot comes first, on 7 of 12 columns, outlined in the ink. The coupon, in a dashed box: "The ₹25,000 comes off your first annual bill if you sign." Below it: "If you do not sign, you keep a CSV export of your ratings and comments and we delete the rest. The fee is not returned." The plan sits on 5 columns: ₹149, the same rate for every employee and firm size, new joiners billed from the month they join, clients free, and the 150-person example.
5. `call`: "Talk to us before your next appraisal cycle". The same button, pilot line and walkthrough link, then the sign-off "The project ends. The feedback stays." Then the footer.

### Lead's Phase 2 changes, how each landed
1. Lede: done verbatim. The page description and og:description were changed to match. The head of talent's part is step 4 of section 2.
2. H1: unchanged, waiting for your call.
3. Nav comment in base.css: rewritten. It now names the call button and `#call-note`, and says the walkthrough link moves into the page.
4. The 375 orphan: a shorter wording ("off" for "taken off") still left a 61 px last line. I reverted to the approved wording and set `text-wrap: balance` on `.pilot-line` in base.css. At 375 the line now breaks into three even lines (234, 242 and 232 px). No wording change.
5. Exhibit 1 tags (lead's mid-phase message): "Stakeholder-centric" became "Client handling" and "Resolve dependencies sooner" became "Share updates sooner", both still selected. The "Was good" step now holds exactly the shared set: Integrity, Client First, Quality of Work; Punctual, Respectful, Client handling; Takes Initiative, Solution-oriented, Resilient. Assumption: the friction list you gave ("Consider client impact", "Share updates sooner") names the tags shared with the walkthrough, not the full friction step. So the other five friction tags stay: Share context earlier, Improve punctuality, Respond more consistently, Take greater ownership, Stay open to feedback. Say if the friction step should hold only the two. The column headings stay "Behaviors" because that is the product's spelling inside the frame.
6. `## For T4`: written above, with the text of both removed blocks, for words3 to place.

### Key decisions and why
- The pilot leads the price pair, because the pilot is the ask. The plan stays visible beside it. Neither block has a button (Plan Q3): one main ask, in the hero and in section 5.
- `.keynums` went into base.css, not home.css, so other pages can reuse it. The figure scales down on phones and never wraps ("2 minutes" wrapped at 375 before the fix).
- Four lines of copy were reworded to clear `copy_tells` triads. The meaning held, and all four still match the product facts.
- "The head of talent sets it up once" lost the word "once": the Admin can change the settings later.
- Problem line 1 changed from the Plan draft. "The partner you are staffed with now" became "the partner a consultant is staffed with now". On every other line "you" means the buyer, and the common brief says to use roles instead of switching pronouns. Line 3 already says "a consultant".
- The ₹8.6 lakh attrition estimate left the plan card. The brief's Decision list does not include it, and it is a value-model estimate, not a decided term.

### Removed from home (beyond the Plan's table)
"What Sphyr does not do", the FAQ, the Scullen and Gallup statistics, the 02:09 stat, the circle figure and its group buttons, the plan's inclusions list (now the assurance rows), and the close manifesto with its walkthrough button.

### Not decided in `docs/pricing/price_and_pilot.md`, left off the page
Any minimum seat count; whether a seat is every employee or only people enrolled in Sphyr (the page says "per employee" only); what happens if the firm leaves after an annual plan; how long the credit stays open after the pilot; how many days the CSV export and the deletion take (the doc suggests 60, 7 and 30 days, unconfirmed).

### Approaches rejected
- A wording change for the 375 orphan: it did not fix the orphan (see change 4 above).
- Subgrid price cards with six aligned rows (the v2 approach): with no action row they no longer need it, and flex columns are simpler.
- Applying `--ink` to every h1 and h2 in base.css: rejected per Plan Q2. Only home opts in.

### Open questions
1. H1: does "40 to 400 people" stay? (You and the user.)
2. Sign-off: the user picks one of the three in the Plan. The page uses choice 1, "The project ends. The feedback stays."
3. Partners on product views: the copy says partners and engagement managers "who have the Manager role" see Team Insights. This assumes firms give partners that role (Plan Q5).
4. `og.png` may still show the v2 tagline. I do not own the asset.
5. The source for the "2 minutes" key number reads "Sphyr product documentation" (product guide, DOC p2). Say if you want the page number on the page.

### Checks
- `copy_scan.py site/index.html`: 203 strings, 0 unreviewed hits.
- `copy_tells.py`: 0 contrasts, 1 possible triad (the footer names, not mine).
- Links: every local href, every anchor, every icon id and every `popovertarget` resolves (script `.swarm/tmp/home3/links.py`).
- 375: no sideways scroll (scrollWidth 375); no element outside the frames runs past 375.
- Banned-word scan of visible text: "Member" appears only as the role label in two exhibit captions (Plan Q1). No file, record, evidence, pooled, VBA, resources, teammates, anonymous or dashes.
- Humanizer pass on all new strings: one change ("once" dropped). The triad rewrites are above.
- The new class names do not collide with other pages.

### What I did not verify
- I did not click the `#call-note` popover open; the markup matches the footer button's.
- No keyboard pass and no screen-reader pass.
- No 375 dark shot (the brief asks for 375 light only).
- Other pages after the base.css additions: the rules are additive, with new class names, so other pages should not change, but I did not load them.
- Exhibits 2 and 3 at 375 only in the full-page shot, not as a close-up. Section 3 (assurance rows) at 375 was not looked at up close either.
- Exhibit 1 after the tag change was not re-shot. Both new tags are shorter than the old ones, and the chips wrap.
- The full-page captures show the sticky nav part-way down the page. This comes from the capture, not from the layout.

### Screenshots (`Product-Marketing-final-assignment.swarm/tmp/home3/`)
Phase 1: `p1_1280_light.png`, `p1_1280_dark.png`, `p1_375_light.png`, `p1_1280_exhibit1.png`, `p1_375_exhibit1.png`.
Phase 2, all in the shipped state except as noted: `p2_1280_light_full.png`, `p2_1280_dark_full.png`, `p2_375_light_full.png` (these three show the old problem line 1 and the old tags), `p2_1280_light_pricing.png`, `p2_375_light_keynums.png`, `p2_375_light_pricing.png`, `p2_375_light_call.png`. I looked at each one. In the 1280 shots the theme switch can show the wrong state, because the theme was set by script; this does not affect the layout.

## Not done (out of scope)
- Placing "How we set the price" and "What happens after you sign" on another page (see `## For T4`).
- Copying the new nav button to other pages (other teammates).
- Updating `og.png`.
- OKF bundle: the two dated addenda (`docs/design/design_system.md`, `docs/design/references.md`) need a line in `docs/log.md`, and the index entry for references.md may need its description updated. I do not own those files; the lead logs them.
- The template comment at the top of `site/index.html` still lists motif.css and motif.js among the shared files. It belongs to the template, so I left it.

### User decision on the sign-off (applied 2026-11-26, addendum to Final)
- The sign-off in section 5 is now "Built from everyone on the project, not one manager's memory." It replaces "The project ends. The feedback stays." and echoes the team's graded central message. The three Plan candidates are superseded.
- H1 and lede (`b699f1d`) and the sign-off (`dc8e4b8`) are separate commits.
- One "X, not Y" check: `copy_tells.py` reports 1 contrast sentence, the sign-off. A scan of visible text and head content for not, rather than, instead of, isn't and never found 4 sentences. The sign-off is the only contrast. The other 3 are plain negatives, not contrasts: "If you do not sign, you keep a CSV export...", "The fee is not returned.", and the footer's "Sphyr is not on sale here."
- `copy_scan.py`: 0 unreviewed hits. `copy_tells.py`: 1 possible triad (the footer names).
- Not verified: the new sign-off was not screenshotted. It is longer than the old line and set in the same display size, so it wraps to about three lines at 375 (an estimate).
