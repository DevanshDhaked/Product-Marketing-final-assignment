---
type: Handoff
title: "v3 words and supporting pages report"
description: "Walkthrough, propaganda and hub moved to consulting words (44 flagged words to 0), Manager role exhibits, call-first ending, pricing rationale and onboarding timeline placed on the hub."
tags: [handoff, words3]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T13:45:00Z }
---

# v3 words and supporting pages report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Teammate words3, Depth 1. Worktree `Product-Marketing-final-assignment.d1-words3`, branch `d1-words3`. Started 2026-11-26.

## Plan

### Success number
Flagged words on my 4 files (visible text, title, meta and og text, aria-labels; not code comments, ids, `value` or `data-tag`). Counted with `swarm/tmp/words3/wordcount.py`. The list is the common brief's never-list plus the v2_baseline section 3 entries (record, evidence, pooled, engagement as a noun, promotion round, the software tags). "Member Insights", "Member role" and "Engagement Manager" are excluded, because they are screen or title names.

- Now: 44 (demo.html 19, js/demo.js 7, propaganda.html 15, deliverables.html 3).
- Target: 0. Exceptions: "engagement" stays only inside an approved quote or title. Course words stay on the propaganda page and the hub, because both are graded deliverables.

### Files and changes

**All 3 pages: nav and head**
- Copy the header from `index.html` (lines 36 to 61). This swaps the nav button to "Book a 20-minute call" (`popovertarget="call-note"`). Every page already has `#call-note`.
- One deviation from an exact copy. Home puts `aria-current="page"` on the brand link. I drop it from the brand and keep `aria-current="page"` on the Deliverables links of deliverables.html, as today. demo.html and propaganda.html get none.
- The head inline script on demo.html stays as it is. It adds `.js`, which the locked steps need.
- og:url and og:image move from /v2/ to /v3/, with Edit, not sed.
- Footers are unchanged.

**demo.html with js/demo.js (the walkthrough). Course stage: off the main AIDA path; it is the secondary link and leads to Action.**

1. Intro (job: say what the reader will do, in about 2 minutes, with no sign-up).
   - "the record partners would have open" becomes "the Member Insights view that partners read before calibration".
   - Progress labels: "Fill one card" becomes "Give one feedback". "See what partners see" becomes "See the Manager view".
   - Meta and og descriptions change to match.
2. Step 1, the pick (job: put the reader in a partner's seat).
   - The h2 "A promotion round is coming..." becomes "Appraisal cycle: one Senior Consultant designation is open". Wording is a draft.
   - "engagements" becomes "projects".
   - Titles stay "Consultant". It is a real designation at all 3 homegrown firms in consulting_firm_life.md.
3. Step 2, the feedback (job: show the 2-minute cost).
   - Copy changes:
     - "card" becomes "feedback" in copy. The visible screen is named "Fortnightly Feedback".
     - "engagement team" becomes "project".
     - "circle" stays, because it is a product word.
   - Product strings inside the frame:
     - Remove the tag "Engagement team values". The product label is "<team> VBAs", which is banned. Home3 also removed it.
     - The friction subtitle becomes the product string "Choose the clearest signals. Your response is anonymized."
     - The right rail becomes the product line "Individual responses are normalized and grouped before anyone sees them."
     - The comment helper stays "Your comment is shown to the person without your name.". The product's "always anonymized" overclaims.
   - Chips: use the same set as home Exhibit 1, so the site shows one firm.
     - Values: Integrity, Client First, Quality of Work.
     - Friction: Consider client impact.
     - The rest are unchanged.
   - Exhibit: the figure becomes `figure exhibit`, with the caption "Exhibit 1. Fortnightly Feedback, Member role: one person's feedback on a project colleague." and `.src` "Source: Sphyr prototype screen. Sample data, fictional people."
4. Step 3, Manager view (job: brief point 2, product truth).
   - The h2 "What partners see for both of them" becomes "What partners read before calibration".
   - Body: "This is Member Insights in the Manager role. Partners read it before calibration." Then the six cycles, about 12 weeks, and 14 people, as today.
   - The made-up sub "See what colleagues said about each consultant, side by side." becomes the product string "Review individual performance signals, comparisons, feedback, and improvement areas.".
   - The "Manager view" eyebrow stays. It is the product string.
   - Exhibit 2 caption: "Exhibit 2. Member Insights, Manager role: two consultants' views placed side by side for this walkthrough.", plus `.src`. `#yours` stays in the caption. This keeps it honest: the prototype shows a member table and a drill-down, not two columns.
5. Step 4, the ending (job: Action).
   - The h2 tagline goes (see Q1).
   - "while the engagement team is still together" becomes "while the project team is still together".
   - "a record like this builds up" becomes "this view fills up for every consultant, two minutes at a time".
   - The main button stays "Book a 20-minute call". Add `<p class="pilot-line">` with the exact text of index.html:70.
   - Drop "Back to home" (see Q2).
6. js/demo.js. Strings only; no logic changes.
   - Each `compare` string gets the new tag names. So does the static `#compare` text at demo.html:171.
   - "record" becomes "Member Insights" or "feedback" in `turn`, and in the "none" and the submit replies.
   - Renamed tags change in every place they appear, all at once:
     - each chip's `value` attribute;
     - each chip's visible span;
     - `data-tag` and the span in both Insights columns.
   - Check: tick a renamed tag and submit. The count in that column must go up by 1.

**propaganda.html (course deliverable 2. The course words stay; the buyer-voiced quotes follow the word rule.)**
- The core line card shows the old tagline (see Q1).
- Belief quotes and audience quotes:
  - "The record breaks up with every engagement team" becomes "What the project team saw is lost when the project ends, and we can fix that." This is a draft.
  - The head of talent's quote is rewritten the same way.
  - "Ratings are pooled" becomes "Ratings are grouped".
- Body text:
  - "the record breaks up with each team" and "weak evidence" are reworded in the belief paragraph.
  - The Central message paragraph is reworded without "engagements" and "record".
  - The channel table caption "a fuller record" becomes "a fuller view of their year".
  - The Expected response first sign becomes: a head of talent who tells partners that project feedback is lost when people roll off.
- Exhibits: none. The figures are strategy diagrams, not product frames.
- `js/propaganda.js`: no change expected. It only drives the table of contents.

**deliverables.html (the hub; course page)**
- The lede drops "All four repeat 'The engagement ends. The evidence stays.'" and gets a hidden `<!-- TODO: ... -->` comment for the new sign-off.
- Item 02: "the record a consultant leaves behind" becomes "a consultant's project feedback over the year".
- Items "01 The website" to "04" stay.
- New "How we set the price" section. It goes after the list, as one short section tied to 01, using the text the lead pastes.
  - I edit "a seat a month" to the home wording, "per employee per month".
  - I check it for month names and customer claims.
  - Small styles go in `css/deliverables.css` only if `.doc` is not enough.
- `css/demo.css`: touched only if `.exhibit` (container-type) collapses the walkthrough figures at 375.

### Order and commits
1. Nav and head on the 3 pages. One commit.
2. Walkthrough words, exhibits and the ending (demo.html, js/demo.js, demo.css if needed). One commit.
3. Propaganda words. One commit.
4. Hub lede and pricing section. One commit.

Before any markup I load the skills `design-taste-frontend` and `stageshow`. Every visible string goes through `humanizer:humanizer`.

### Checks
- copy_scan and copy_tells on all 3 pages.
- Links resolve.
- No sideways scroll at 375.
- Screenshots of what changed: light and dark at 1280, plus one at 375. Saved to `swarm/tmp/words3/`.
- The tag-count click test in Playwright at http://localhost:8874/.
- Rerun of wordcount.py.

### Open questions (defaults in brackets)
1. The old tagline sits in two headline spots: the demo step-4 h2 and the propaganda `.core-line`, which drives "Central message" and the tactic "Carry one line on every piece".
   - For the demo, I use a plain h2 such as "At calibration, partners still decide" [default].
   - For the propaganda page, there are two options:
     - (a) Put home3's first candidate, "The project ends. The feedback stays.", in as a placeholder with a TODO comment.
     - (b) Hide the line and reword Central message without quoting it.
   - [default (a), marked pending user approval]
2. Should "Back to home" go from the walkthrough ending? The rule allows only one secondary link. [drop it; the nav brand goes home]
3. Tags. Home Exhibit 1 still shows "Stakeholder-centric" and "Resolve dependencies sooner", which v2_baseline flags as software tags.
   - (a) Match home exactly, so the site shows one firm. I flag these two for home3.
   - (b) Use the brief's consulting tags (client handling, problem solving, structured communication) on the walkthrough only.
   - [default (a)]
4. Pricing text. The home3 report has no `## For T4` section yet, so I wait for the lead's paste. Placement: deliverables.html [default], because the propaganda table of contents follows the strategy's fixed parts.
5. The propaganda "Expected response" card and flow still go walkthrough first, then call. v3 makes the call first. Should I reword it? [reword the card only: "Book a 20-minute call, or take the walkthrough first", and leave the flow order as it is]
6. The description of hub item 03 ("Posts for the Sphyr company page") may stop matching once linkedin3 ships. Should I sync it? [leave it, and note it]

### Not done (out of scope, known now)
- The onboarding text "What happens after you sign", which home3 removed from home. It is not in my brief.
- `og.png` may still show the v2 tagline. I do not own that asset.

Waiting for "approved" or changes.

## Approved (2026-11-26)
Lead approved with the defaults for Q1 (a), Q2, Q4, Q5 and Q6, plus these changes:
- Q3: one consulting tag set, shared by home and the walkthrough.
  - Values: Integrity, Client First, Quality of Work.
  - Behaviours: Punctual, Respectful, Client handling.
  - Attitudes: Takes Initiative, Solution-oriented, Resilient.
  - Friction: Consider client impact, Share updates sooner.
  - The lead is telling home3 the same.
- Step 1 h2 is a plain sentence with no colon label, for example "One Senior Consultant designation is open this appraisal cycle."
- The pricing text comes later. The other commits go first.

## Final

Success number: flagged words on my 4 files are 0, down from 44. This was counted by `swarm/tmp/words3/wordcount.py` (n=4 files). The count covers visible text, title, meta and og text, and aria-labels.

### Files and commits (branch `d1-words3`)
| SHA | Files | What |
|---|---|---|
| `85c6116` | demo.html, propaganda.html, deliverables.html | Header copied from index.html (nav button "Book a 20-minute call"), og URLs moved to /v3/ |
| `05a36ff` | demo.html, js/demo.js, css/demo.css | Walkthrough words, shared consulting tag set, Exhibits 1 and 2, Manager role, the step-4 heading, the pilot line, "Back to home" dropped |
| `c640102` | propaganda.html | Buyer quotes in project words, placeholder sign-off with a TODO, call first in Expected response |
| `b13e350` | deliverables.html, css/deliverables.css | Hub lede without the tagline (TODO comment), item 02 text, item 01 links to two new sections: "How we set the price" and "What happens after a firm signs" |

### Key decisions and why
- Nav aria-current: home marks the brand link. On my pages the brand is not marked. deliverables.html and propaganda.html keep `aria-current` on the Deliverables links, as before, because propaganda is a deliverable page.
- Exhibits:
  - Both walkthrough figures now use `exhibit` alone, with no `figure` class. `.figure figcaption` (0,1,1) outranks `.exhibit-cap` (0,1,0), so with both classes the caption kept the old muted style.
  - In demo.css, `.wt-figure figcaption` (flex) became `.wt-figure .exhibit-cap { max-width: none }`, and `.wt-yours` became a block. This puts the source line and the "your feedback" note under the caption.
- Step 3:
  - The h2 is "Both consultants in Member Insights", and the body carries "Partners read it before calibration." An h2 of "What partners read before calibration" would have repeated the body line.
  - The subtitle is the product string from prototype 3.6.
  - Exhibit 2's caption says the two views are placed side by side for this walkthrough.
- Step 4 h2: "What this changes at calibration". The JS lede that follows already says "Partners still decide".
- Exhibit 1 product strings:
  - The friction subtitle "Choose the clearest signals. Your response is anonymized." and the rail line "Individual responses are normalized and grouped before anyone sees them." are copied from the prototype.
  - The comment helper stays "Your comment is shown to the person without your name.". The product's "always anonymized" overclaims, because managers see who asked for an edit.
- Tags follow the lead's shared set. Only the friction tags "Consider client impact" and "Share updates sooner" changed; the other five friction tags are the same as on home. The click test passed for both people:
  - Nikhil: Integrity went from 17 to 18, and Responses received from 74 to 75.
  - Tara: "Share updates sooner" went from 6 to 7.
- Hub timeline: it uses roles and "the firm" instead of "you", following the rule on roles over switching pronouns.
  - "cards" became feedback, "record" became Member Insights or Insights, and "engagements" became projects.
  - "team by team" was dropped, because the head of talent's view is participation.
  - The "After the first year" row is kept.
  - "a seat a month" became "per employee per month".
  - The two sections are separate `section` elements after the hub list. Item 01 links to them.

### Rejected
- Keeping "Back to home" on the walkthrough ending. It was a second secondary link (lead approved Q2).
- Renaming the walkthrough designations. "Consultant" is a real designation at all 3 homegrown firms in the research. The h2 names the Senior Consultant designation.

### Open questions
1. copy_scan.py reports 2 unreviewed hits on demo.html, both false positives from the word "review":
   - "Review period" was already in v2.
   - "Review individual performance signals, comparisons, feedback, and improvement areas." is the product's Member Insights subtitle.
   - I do not own `design-lab/copy_scan.py`, so I did not add them to ALLOWED. Lead: add them, or tell me to reword the subtitle.
2. The propaganda core line "The project ends. The feedback stays." is a placeholder until the user approves the sign-off. There are TODO comments in propaganda.html and deliverables.html.
3. Hub item 03 still says "Posts for the Sphyr company page". It may need to change once linkedin3 lands (Q6, left as is).

### Not verified
- copy_tells "possible triads" on propaganda (5) and the hub (1): checked by eye. They are name lists and old sentences, not rhythm triads, and I left them.
- I did not run the residue method of v2_baseline across the full vocabulary. Only the wordcount list was checked.
- The flow figure on the propaganda page still shows the walkthrough before the call, as approved for Q5.
- At 375 the nav call button is hidden by the existing base.css rules, the same as on home. I did not check whether that is intended.

### Screenshots (`swarm/tmp/words3/`)
- Walkthrough: demo-1280-light-step2.png, demo-1280-light-step3.png, demo-1280-light-step4.png, demo-1280-dark-exhibit2.png, demo-375-light-step4.png.
- Hub: hub-1280-light-top.png, hub-1280-light-after.png, hub-1280-dark-price.png, hub-375-light-after.png.
- Propaganda: prop-1280-light-top.png, prop-1280-dark-top.png.

### Checks
- No sideways scroll at 375 on all 3 pages (scrollWidth 375).
- Internal links: 24 checked, 0 broken, including the anchors.
- No em or en dashes in the changed files.

## Not done (out of scope)
- `og.png` may still show the v2 tagline. I do not own that asset.
- `design-lab/copy_scan.py` ALLOWED list, for open question 1.

### Addendum to Final (after review)
- `886ba2e` deliverables.html: the timeline row "After a few cycles" changes.
  - Old: "sees who took part". No captured screen lists who took part.
  - New: "sees how much of each team has given feedback". This matches the per-team Participation tile in the Manager view (prototype 3.5).
  - Caveat: that tile is in the Manager view, so the head of talent needs a Manager role as well as Admin. The old v2 line made the same assumption.
- Hub row heights: there are no new gaps. Item 04 was already 3 lines tall (82 px), and items 01 and 04 are now both 82 px. The `1fr` row height was set by 04 before my change.
- Exhibit 1 crop after submit is not new. The stage height and panel bottom are the same with `figure` and with `exhibit` (291 px, `overflow: hidden`), so the crop comes from the existing stage.
- Tie to 01: the only visible tie is the link sentence in item 01. Someone reading top to bottom meets the two sections after item 04. Lead decides whether to add a phrase such as "For 01, the website" at the start of each section.
- New screenshot: prop-375-light-top.png. Opened and checked: hub-1280-light-top.png, prop-1280-dark-top.png.
