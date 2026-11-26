---
type: Handoff
title: "v3 ad builder report"
description: "Standee and A6 card rebuilt with a calibration-week headline as the Attention, the call in the first line, and a feedback card exhibit; 9 of 9 on the first-screen rubric."
tags: [handoff, ad3]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T13:40:00Z }
---

# v3 ad builder report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Worktree `Product-Marketing-final-assignment.d1-ad3`, branch `d1-ad3`. Started 2026-11-26.

Read: both briefs; decision log (v3 plan gate, Short deliverable pages, Ad placement chosen); professor feedback addendum 2026-11-26; `aida.md` sections 2, 7, 8 and the checklist; `consulting_firm_life.md` sections 3 to 5; `rival_site.md` ad score and "What this means"; `v2_baseline.md` section 1; `consulting_visual_language.md` direction A; `faux_ui.md`; `slop_rules.md`; `do_not_claim.md`; `price_and_pilot.md` (pilot terms); `home3.md` (sign-off candidates, lead's "use choice 1 for now"); current `site/ad.html`, `site/css/ad.css`, home nav and Exhibit 1 in `site/index.html`, `.report`, `.exhibit`, `.pilot-line` and `.fx-*` in `site/css/base.css`; the `ALLOWED` list in `design-lab/copy_scan.py`.

## Plan

Success number: the ad scores 9 of 9 on the `v2_baseline.md` rubric from the headline and first line alone (v2: 3 of 9).

### Files
- `site/ad.html`: nav, the standee, the A6 front and back, the rationale, the closing call.
- `site/css/ad.css`: the new print layout and the exhibit inside the standee. Tokens and classes come from `base.css` (`--ink`, `.exhibit`, `.exhibit-cap`, `.pilot-line`, `.fx-*`). No raw hex.
- Nothing else. `motif.css` stays in the repo; the ad page stops linking it, because the ribbon figure is gone.

### Headline proposals (first choice goes on the page; the lead and the user pick)
All three are a scene from the appraisal cycle, use no pun, need no second line, and avoid "review" (the copy scanner reads it as social proof), file, evidence, pooled and engagement. None uses "X, not Y".

| # | Headline | Who it stops | Why |
|---|---|---|---|
| 1 (first choice) | Calibration is on Monday. Half the project feedback forms are still blank. | Head of talent | The head of talent is the one chasing managers before calibration (`consulting_firm_life.md` s4: "you're only at 50% of the reviews done", the Cycle 1 reminder thread). At an HR event the head of talent is the person walking past. The fix is what Sphyr does: feedback is given every two weeks, so nothing is blank at the end. |
| 2 | The partner rating this consultant saw three weeks of the year's work. | Partner | s4: "the Partner you are staffed with at the time of review tends to have the strongest influence". It matches the home trigger scene. It can read as an accusation to a partner, which may also be why it stops one. |
| 3 | The rating rests on the last project. The consultant did five this year. | Both | s4: "More recent or longer projects tend to carry more weight." Two short sentences. The weakest on stop power, because recency bias is a known idea. |

The numbers in the headlines (half, three weeks, five) are scene details, not claims. The rationale says the headline is a scene.

Brand beside the headline: the Sphyr mark and name sit directly above it, at the same left edge.

### First line (the same for all three headlines)
"Sphyr is peer feedback every two weeks for heads of talent at Indian consulting firms of 40 to 400 people. Book a 20-minute call."

The call sits inside the first line, so (c) scores under the strict frame. The QR row follows directly under it.

### Self-score (headline 1 plus the first line; my estimate, scored by the author, so treat it as a guess until the lead scores it)
| Question | Score | Text judged | Why |
|---|---|---|---|
| (a) What | 3 | "Sphyr is peer feedback every two weeks" plus "Calibration", "project feedback forms" | Names the product, what it is and its cadence. The headline sets it in the appraisal cycle. |
| (b) Who | 3 | "heads of talent at Indian consulting firms of 40 to 400 people" | Covers role, firm type, size and country, the three gaps the baseline named. |
| (c) Next | 3 | "Book a 20-minute call." | One call, in the first line, with the exact label. |
| Total | 9 of 9 | | |

### Standee (850 by 2000 mm), top to bottom
1. Brand row: mark and "Sphyr". Job: brand beside the headline (Ogilvy). Stage: A.
2. Headline (Newsreader, `--ink`). Job: stop the reader. Stage: A.
3. First line, with the call. Job: what Sphyr is, for whom, the next step. Stage: A to Action.
4. Call row: the QR plus "Book a 20-minute call", "or scan to see the 2-minute walkthrough" and the printed address (unchanged). Job: act now. This sits at about chest height on a real standee, where a QR can be scanned. Stage: Action.
5. Pilot line, verbatim from home: "Start with a 12-week pilot for up to 40 people. ₹25,000 plus GST, taken off your first annual bill if you sign." Job: assurance and low friction. Stage: Interest and Decision.
6. Exhibit: home's Fortnightly Feedback card made static ("Was good" selected, the standout chips, "Private by design"). It is `role="img"` with an aria-label, not the live radio group (`faux_ui.md` rule). The card is cut by the standee's bottom edge, the way the stageshow framing rule describes. The standee renders under 440px wide, so the compact container query applies: the tile subtitles drop and the chips stack. That view keeps every word whole. Job: show the product is a two-minute form. Stage: Interest.
7. Caption under the frame: "Exhibit 1. Fortnightly Feedback, Member role: rating one person from the project." Source line: "Source: Sphyr prototype screen. Sample data, fictional people."
8. Strapline, small, at the foot: "The project ends. The feedback stays." This is home3's sign-off choice 1. The lead set it "for now", and it is pending the user's approval.

### A6 card front
Brand row, headline, first line with the call, QR row, pilot line. It is the standee's first read at card size, with no exhibit, because a second crop at 105 mm would be unreadable.

### A6 card back (Interest and Decision)
- How it works, in about 40 words: every two weeks, the people on a consultant's project spend about two minutes rating them. Ratings are grouped and comments are anonymized to the person rated. Managers approve edit requests and see who asked. Partners still decide. ("Pooled" and "engagement team" from v2 are removed.)
- What the price includes: setup, training and training materials.
- The price line, as now: "₹149 per employee per month, billed yearly, plus GST" (matches home).
- QR row (same labels as the front) and the existing small print about no tracking.

### Page sections (`ad.html`)
1. Intro: H1 "The advertisement" and the existing lede. It stays a deliverable page for the grader.
2. The pieces: the standee on the left, the two cards on the right, as now. The figure captions stay.
3. "Why this ad", the rationale, about 230 words in labelled rows:
   - Medium: verbatim. It is on the scanner's allowlist (the "endorse" denial).
   - Audience: rewritten, about 35 words. Heads of talent and partners at Indian consulting firms of 40 to 400 people. The room holds HR people from every industry, so the headline uses a moment only a consulting firm has.
   - Why this headline (new, about 60 words): most passers-by read only the headline, so the headline is the Attention. It is a moment from the reader's own appraisal cycle, in their words, and needs no second line. The brand sits beside it, and the line under it names the product, the reader and the call. The v2 headline was a slogan the reader had to decode.
   - Journey stage: as now, with the link to the first LinkedIn post.
   - Why it tracks nobody: the heading and the sentence, verbatim (both are allowlisted).
4. Close: "Book a 20-minute call" (the existing `call-note` popover), the pilot line, and "See the 2-minute walkthrough" as the only secondary link. The "The three LinkedIn posts" button and the "All deliverables" text link are removed (default; see Q3).

Nav: the markup is copied from `site/index.html`, with `aria-current="page"` moved from the brand to the two Deliverables links (see Q2). The footer and the `call-note` popover stay as they are.

Design: direction A. Headline in `--ink`; product green only on the actions; no ribbon figure; no animation. On screen the pieces keep the light paper colours in both themes, as now.

### Build steps
1. Load the `design-taste-frontend` and `stageshow` skills. Write the markup and CSS.
2. Run every visible string through the `humanizer:humanizer` skill.
3. Run `copy_scan` and `copy_tells` on `site/ad.html`, check the links, and check for sideways scroll at 375.
4. Take screenshots at 1280 (light and dark) and 375, at http://localhost:8872/site/ad.html, saved under `.swarm/tmp/ad3/`, and look at them.
5. Commit in two groups: (1) the ad pieces and their CSS, (2) the rationale and the closing call. Then write `## Final`.

### Open questions (each has a default I will use unless told otherwise)
- Q1. Rubric frame. Default: the call is inside the first line ("... 400 people. Book a 20-minute call."), so it scores under the strict "headline and first line" reading. Alternative: the lead counts the call row directly under the first line as part of the first read. The first line then ends at "people", which reads cleaner on the standee.
- Q2. Nav `aria-current`. The brief says to copy the nav exactly. Home marks the brand as the current page, which is wrong on `ad.html`. Default: move `aria-current="page"` to the Deliverables links, as v2 did. Nothing else in the nav changes.
- Q3. Extra links at the close. The rule allows only one secondary link. Default: remove the LinkedIn button and the "All deliverables" link. The Journey stage row still links to the post, and the nav has Deliverables.
- Q4. How a reader books a call from print. The QR opens `/v2/demo.html`, and the call button there is in the nav. Default line: "Book a 20-minute call" in bold, then "or scan to see the 2-minute walkthrough". At deploy, the lead may want the QR to open a page where the call button is the main action.
- Q5. Exhibit choice. Default: home's feedback card (Member role), which suits headline 1. If the user picks headline 2 or 3 (partner), the better crop is Manager Team Insights, showing the rating distribution and the anonymized team feedback, labelled "Manager role". The CSS for both is already in `base.css`.
- Q6. Strapline. Default: "The project ends. The feedback stays." at the standee foot only, pending the user's approval. Remove it if the user rejects the sign-off.

Waiting for "approved" or changes.

## Approval
2026-11-26: the lead approved the plan with the defaults for Q1 to Q6. Headline 1 goes on the page. All three headlines stay in this report for the user to pick from (see "Headline proposals" in the Plan).

## Final

Success number: the ad scores 9 of 9 on the `v2_baseline.md` rubric from the headline and first line alone (v2: 3 of 9). This is my own score as the author, so it is a guess until the lead or someone outside the team scores it.

### Self-score of the shipped text
Headline: "Calibration is on Monday. Half the project feedback forms are still blank."
First line: "Sphyr collects peer feedback for appraisals every two weeks, for heads of talent at Indian consulting firms of 40 to 400 people. Book a 20-minute call, or scan to see the 2-minute walkthrough."

| Question | Score | Text judged | Why |
|---|---|---|---|
| (a) What | 3 | "Sphyr collects peer feedback for appraisals every two weeks" | Names the product, the job (appraisals) and the cadence. The baseline docked v2 for leaving out "for appraisals", so the line states it rather than leaving it to "Calibration". |
| (b) Who | 3 | "heads of talent at Indian consulting firms of 40 to 400 people" | Covers role, firm type, size and country, the three gaps the baseline named. |
| (c) Next | 3 | "Book a 20-minute call" | One call with the exact label, inside the first line. |
| Total | 9 of 9 | | |

### Files and commits (branch `d1-ad3`)
- `9b2fefb`: the page rebuild in `site/ad.html` and `site/css/ad.css`.
- `6196a3c`: "Attention" and "for appraisals" added to the copy, plus the fit fixes for the standee and the A6 front.
- The plan said one commit for the pieces and one for the rationale. Both sit in the same file, and `git add -p` is interactive, so the first commit holds the whole rebuild.

### What is on the page
- Standee, top to bottom:
  - the Sphyr brand row
  - the headline in `--ink`
  - the first line, with the call in it
  - the QR code and the printed address, both unchanged
  - home's pilot line, verbatim
  - Exhibit 1: home's Fortnightly Feedback card, shown still (`role="img"`, "Was good" selected, no satellite), with home's caption and source line
  - the strapline "The project ends. The feedback stays." (pending the user)
- A6 front: the same first read at card size (brand, headline, first line, QR, pilot line). No exhibit.
- A6 back:
  - how it works, with "grouped" in place of v2's "pooled" and "the people a consultant worked with" in place of v2's "engagement team"
  - managers approve edit requests and see who asked; partners still decide
  - "Setup, training and training materials are included."
  - the price, and a QR row labelled "See the 2-minute walkthrough"
- Rationale: 259 words including the row labels (about 247 without them).
  - "Medium" and "Why it tracks nobody" are verbatim, because the scanner allowlists them.
  - "Audience" is rewritten.
  - "Why this headline" is new. It says, in plain words, that most people walking past read only the headline, so the headline is the Attention.
  - "Journey stage" is as before.
- Close: the "Book a 20-minute call" button (the existing `call-note` popover), the pilot line, and "See the 2-minute walkthrough" as the only secondary link. The LinkedIn button and the "All deliverables" link are removed (Q3).
- Nav: copied from `site/index.html`. A diff shows the only change is `aria-current="page"`, now on the two Deliverables links and not on the brand (Q2).
- `motif.css` is no longer linked from `ad.html`. The file stays in the repo.

### Key decisions and why
- The call sits inside the first line, so (c) scores 3 even under the strict frame (Q1). The QR row under it carries only the code and the address, so the call label is not repeated.
- The exhibit is shown at its natural height. The stage's bottom edge cuts inside the card's own padding (`.fx-hero-card` margin set to -8px), so no control is sliced. The first draft made the frame fill the standee's leftover height, and its edge cut through the answer tiles. The "What stood out?" step is left out, because at standee size the edge would cut through its chips.
- The product frame is sized in px, so it does not shrink with the standee. Container queries scale the stage by 0.84 when the exhibit is 340px or narrower and by 0.76 at 310px or narrower. That covers the desktop standee (380px wide, exhibit 334px) and the phone standee (343px, exhibit 302px).
- Fit, measured as the gap between the last line and the piece's foot (the bottom padding is 17 to 23px):
  - 1280: standee 19px, A6 front 20px, A6 back 20px
  - 1000: 18, 21, 21
  - 375: 17, 22, 22
  - To get there, the standee's vertical gaps shrank by 1cqw each. The A6 card's gap went from 5 to 4cqw, its padding from 8 by 7 to 7 by 6.5cqw, and its headline from 8.6 to 8.2cqw.
- Humanizer:
  - Two one-line closers in the rationale ("Everyone else can walk on.", "It needs no second line.") are merged into the sentence before them, because both carry a fact.
  - The two strings changed in the second commit raised no tells.

### Rejected
- Showing the exhibit's second step (the chips): the frame's edge would cut through real words at standee size.
- An exhibit on the A6 front: a crop at 105 mm would be unreadable.
- Making the frame fill the standee's leftover height: its edge sliced the answer tiles.

### Checks (smoke only)
- `copy_scan` after the second commit: 92 strings, 0 unreviewed hits, 4 reviewed denials (all allowlisted).
- `copy_tells`: 0 contrast sentences. It also flags 2 possible triads, which I checked by eye:
  - "Setup, training and training materials" is the product's real inclusion list (WP p6 to p7, decision log). It is not a rhythm triad.
  - "Abhinav, Devansh and Bheema" is the team names in the footer, which I did not change.
- Em dashes and en dashes in `ad.html` and `ad.css`: 0.
- Banned words (file, record, evidence, pooled, member, subordinates, resources, teammates, engagement): 0 in the copy. "Member role" is the product's real role name and appears only in the exhibit caption.
- Links: every href on the page returns 200 from the lead's server, and the `#how`, `#partners` and `#pricing` anchors exist in `index.html`.
- No sideways scroll at 375 (scrollWidth 375).

### Open questions for the user and the lead
- Headline choice, from the three in the Plan. If the user picks 2 or 3 (written for partners), I recommend switching the exhibit to Manager Team Insights (Q5).
- Strapline: "The project ends. The feedback stays." is home3's sign-off choice 1, still waiting for the user's approval.
- From print, the call is booked through the walkthrough page, whose nav has the call button (Q4). At deploy the QR could open a page where the call button is the main action.
- The headline's "Monday" and "Half" are details of the scene, not claims. The copy scanner raised nothing.

### Not verified
- The rubric score was not given by anyone outside the team.
- Dark at 375 was not screenshotted. Dark was checked at 1280 only; the printed pieces keep their paper colours in both themes by design.
- At 1000 the fit was measured but not screenshotted.
- Firefox below version 126 does not support `zoom`. There, the standee's foot would be about 30px over at 375.

### Screenshots
All in `Product-Marketing-final-assignment.swarm/tmp/ad3/`, taken from the state committed in `6196a3c`:
- `ad3_light_1280.png` (full page)
- `ad3_dark_1280.png` (full page)
- `ad3_pieces_dark_1280.png` (the standee and the cards)
- `ad3_light_375.png` (full page)
- `ad3_pieces_375.png` (the standee and the cards)

### Not done (out of scope)
- The QR image and the URL it encodes (`/v2/demo.html`), the printed address, and the `og:url` and `og:image` meta, which still point at `/v2/`. The lead regenerates and rewrites these at deploy.
- `og.png` may still show the v2 tagline. It is not my file.
