---
type: Handoff
title: "Walkthrough teammate report, phase 2"
description: "The 4-step interactive walkthrough: script, decisions, checks and unverified items."
tags: [handoff, walkthrough]
generated: { by: claude-code/opus-5-5, at: 2026-11-25T04:30:00Z }
---

# Walkthrough teammate report, phase 2

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Status: built and committed on `d1-walkthrough` (878baed, da83b15, b3a1ecb, 0fb0fcc, f60bd23). See Final at the end; its Revision section replaces earlier claims where they differ.

Success number for this page: 0 failed checks across the phase 2 list (copy scan, copy tells, contrast, sideways scroll, smallest text, idle frames, reduced motion, links), with all 9 path combinations (3 picks times 3 card answers) walked end to end in the browser.

## Setup done

- Worktree `Product-Marketing-final-assignment.d1-walkthrough`, branch `d1-walkthrough` from `iteration-a` at 910ca83. Nothing written in the repo yet.
- Read: `docs/index.md`, `decisions/decision_log.md` (all entries), `product/do_not_claim.md`, `product/prototype_screens.md` (3.0 to 3.9), `product/product_facts.md` (grep), `design/faux_ui.md`, `design/slop_rules.md` (rules and pre-publish check), `design/homepage.md` (page map, checks), `handoffs/design_report.md` (gate 1b and Final handoff), `strategy/message_guideline.md` (all), `brief/professor_feedback.md` (pricing and packaging), `packaging/first_use_experience.md` (walkthrough row), `packaging/first_card_reward.md`, grep of `deliverable_map.md`, `journey_map.md`, `acquisition_engagement.md`, the interactive card in `design-lab/faux-ui.html`, and the old `main:site/demo.html`.
- Not read in full: `pricing_summary.md`, `packaging_summary.md` beyond the grep. The brief and `first_use_experience.md` say price and order are not part of the walkthrough, so the page carries no price.
- sitecss state at 910ca83: `site/_template.html`, `site/css/` and `site/js/` do not exist yet.

## Plan

### Files I own

| File | Purpose |
|---|---|
| `site/demo.html` | The walkthrough page. Built from `site/_template.html` (head, no-flash theme script, font preloads, 3-item nav with `aria-current="page"` on the walkthrough button, footer, `#call-note`). |
| `site/css/demo.css` | Page layout (intro, four stacked steps), the pick cards, the two-column pooled frame, done states, reduced-motion rules. Uses shared tokens only. |
| `site/js/demo.js` | Page state (pick, answer, tags, comment, submitted), step reveal and focus, the step 4 text branch, the comment counter, the seconds timer, adding the visitor's card to the pooled frame. About 120 lines, no library. |
| `site/_shots/demo-{light,dark}-{1280,375}.png` | Four screenshots, not linked from any page. |

No docs files: my brief does not give me a docs folder. If the lead wants a page doc (like `docs/design/homepage.md`), I will add `docs/site/demo.md` with its own `log.md`.

### Page structure

One page, four steps stacked in order, inside one `<ol>` so the order is real for screen readers. Not a stepper that swaps the whole view: a full swap breaks the "every interaction answers locally" rule and the 5% changed-share limit.

- With JavaScript: steps 2 to 4 start hidden. Each answer gets a local reply in place, then the next step appears below it and focus moves to its heading (`tabindex="-1"`). The page above never changes. With motion on, the new step fades in once (200 ms) and then rests. Under reduced motion it appears with no fade and no smooth scroll. The content change is the same.
- Without JavaScript: all four steps show, the card works through CSS radios as on home, and step 4 shows the neutral text.
- A small progress row at the top (four numbered marks, one filled per finished step) replaces the old "Step N of 4" kicker on every section. Kicker count on the page: 0 or 1.
- Layout families (slop rules need 4 or more): intro document column, unequal pair (step 1 pick cards), split with a product frame (step 2), wide figure (step 3), document column with two actions (step 4).

### Interaction and accessibility

- Step 1: a real radio group (`fieldset`, `legend`), each choice a large label card. Keyboard: arrow keys. Touch: whole card is the target.
- Step 2: the three answers are radios (same markup as `design-lab/faux-ui.html`); the value tags are real checkboxes styled as chips; "Add a comment" is a button that opens a labelled `textarea` (`maxlength="400"`, live counter); "Submit" is disabled until an answer is picked.
- Every local reply sits in an `aria-live="polite"` region.
- The visitor's comment is inserted with `textContent` only, never `innerHTML`.
- Nothing is stored or sent. No `localStorage`, no network calls. The page says so in one line.

### Dependencies and asks to the lead

- I need the faux UI frame styles (`fx-window`, `fx-panel`, `fx-tile`, `fx-opt`, `chip`, `fx-vba`, `fx-sat` and the rest from `design-lab/faux-ui.css`). I do not know whether sitecss ports them into `site/css/base.css`. If they are not in shared CSS, may I copy only the classes this page uses into `demo.css`, or should sitecss add them?
- I need the icons `i-smile`, `i-frown`, `i-minus`, `i-lock` in `site/assets/icons.svg` (they exist in `design-lab/assets/icons.svg`).
- Port 8823 for my checks; the shared Playwright browser for screenshots and the 9-path walk. Please confirm I may use the browser in my build step.

### Checks I will run before reporting (method and numbers in the report)

1. `python3 design-lab/copy_scan.py site/demo.html` and `python3 design-lab/copy_tells.py site/demo.html`: 0 unreviewed hits, at most one "X, not Y", 0 triads.
2. `node design-lab/contrast.mjs` only if I add colours (plan: no new colours).
3. Untemplated checks as in `docs/design/homepage.md`: sideways scroll 0 at 390 px, smallest text 11 px, 0 idle frames after load and after each step, reduced motion keeps the content change, contrast in both themes.
4. All 9 path combinations walked in the browser, plus keyboard only and the no-JS view.
5. Links: home, deliverables, the call note, all relative.
6. The month-name grep (all twelve names and short forms) on the built page: 0.
7. Humanizer skill pass on every visible string before commit.

### Commits (planned)

1. `site/demo.html` and `site/css/demo.css` and `site/js/demo.js`: "Add consulting walkthrough page".
2. `site/_shots/demo-*.png`: "Add walkthrough screenshots".

## Script

Draft copy below. Every string outside the product frame goes through the humanizer skill and the two copy scanners at build time, so the wording will tighten. Strings inside the frame are the prototype's own labels and keep its casing.

### Page top

- Title tag: "The 2-minute walkthrough | Sphyr"
- Meta description: "Pick a consultant to promote, fill one Sphyr card, and see what partners see. Sample data, fictional people. No sign-up."
- H1 (display serif): "The 2-minute walkthrough"
- One line: "Pick who you would promote, fill one card, then see the record partners would have in front of them. No sign-up."
- Label: "Sample data, fictional people. Tara and Nikhil are an example, not real consultants."
- Note: "Nothing you choose or type here leaves this page."

### Step 1: Pick someone

- H2: "A promotion round is coming, with one senior consultant slot."
- Text: "You are one of the partners deciding. Two consultants from the practice are up. Here is what you remember of each."
- Radio group, legend: "Who would you promote?"
  - Choice A. Avatar "TM". "Tara Menon", "Consultant". What you remember: "Presented the findings to the client's leadership on your last two engagements. You have seen her work up close."
  - Choice B. Avatar "NR". "Nikhil Rao", "Consultant". What you remember: "Worked on the same two engagements. You rarely saw him in client meetings and can't say much about what he did."
- Local reply after a pick: "You picked Tara. Hold on to that; step 4 comes back to it." (or Nikhil). The card shows a selected state.
- Then step 2 appears.

This is the only place the promotion moment is named on the page.

### Step 2: Fill one card

- H2: "Now fill one card, the way Nikhil's colleagues do"
- Text: "Every two weeks, each person in a consultant's circle fills a short card for them. Say you were on Nikhil's engagement team this fortnight."
- Product frame (interactive, real radio group), from Provide Feedback (prototype 3.3):
  - Person: avatar "NR", "Nikhil Rao", "Consultant · Peers"
  - Legend: "How was your experience with Nikhil Rao this fortnight?"
  - Tiles: "Was good / Great interaction", "Could improve / Some friction", "No interaction / Nothing to review"
  - If Was good: "What stood out?", "Select all that apply.", team label "Engagement team VBAs", Values: Transparency, Customer First, Innovation; Behaviors: Punctual, Respectful, Stakeholder-centric; Attitudes: Takes Initiative, Solution-oriented, Resilient
  - If Could improve: "Where did you experience friction?", "Choose the clearest signals. Your response is anonymized.", same team label, Values: Share context earlier, Consider customer impact; Behaviors: Improve punctuality, Respond more consistently, Resolve dependencies sooner; Attitudes: Take greater ownership, Stay open to feedback
  - If No interaction: no second step, as in the prototype
  - Comment (Was good and Could improve only): button "Add a comment"; label "Let Nikhil know what's on your mind?"; helper "Your comments and review are always anonymized."; placeholder "Share a helpful example or context…"; counter "0/400"
  - Button: "Submit" (the prototype's "Previous" is left out; there is no previous card here)
  - Satellite: "Private by design" / "Individual responses are normalized and grouped before anyone sees them."
- Caption under the frame: "Prototype screen. Sample data, fictional people."
- After Submit, inside the frame the card body is replaced by the prototype's submitted row: "Nikhil Rao", the chosen answer icon, "Submitted · Read only".
- Local reply outside the frame, by answer:
  - Was good or Could improve: "That took you 14 seconds. Your card joins the other 13 from Nikhil's circle this cycle. Nikhil sees the tags and your comment without your name on them." (seconds measured from the first tap in the card to Submit, on this page only)
  - No interaction: "That took you 4 seconds. This card tells Sphyr you didn't work with Nikhil this fortnight, so it adds nothing to his record. Nobody has to make up a rating."
- Then step 3 appears.

Privacy wording check: "without your name on them" is about what the person rated sees. It does not claim that nobody can see who gave the card (the manager's edit approvals show that). The page does not repeat the privacy point elsewhere.

### Step 3: See what partners see

- H2: "What partners see for both of them"
- Text: "This is Sphyr's Member Insights view after six cycles, about 12 weeks, of cards from the 14 people in each consultant's circle."
- Product frame (static, `role="img"` with an `aria-label` that reads out both columns):
  - Header: eyebrow "MANAGER VIEW", H1 "Member Insights", sub "Review individual performance signals, comparisons, feedback, and improvement areas.", segmented "Review period: Last Cycle | All Cycles" with All Cycles active, chip "6 cycles"
  - Two equal columns, one per consultant. Each: person row; tile "Responses received" with "From N collaborators"; "Top feedback received" / "Most frequent positive anonymized signals" with four tag bars and counts; "Improvement areas" / "Recurring constructive signals to coach" with count and "Repeated across N cycles"; "Anonymized Feedback" with one comment labelled by cycle.
- Caption: "Prototype screen. Sample data, fictional people."
- Line under the caption, only if the visitor submitted Was good or Could improve: "Nikhil's column includes the card you just filled." Their tags add 1 to any matching bar and their comment, if any, shows as the newest item, labelled "Cycle 6".
- Then step 4 appears right away (no extra action needed); a "Continue" button is not used.

Sample data (fictional; all counts checked by hand):

| Item | Tara Menon | Nikhil Rao (before the visitor's card) |
|---|---|---|
| Circle | 14 people | 14 people |
| Cards with an interaction, cycles 1 to 6 | 10, 11, 10, 11, 12, 11 = 65 | 12, 12, 13, 12, 13, 12 = 74 |
| "No interaction" cards | 4, 3, 4, 3, 2, 3 = 19 | 2, 2, 1, 2, 1, 1 = 9 |
| Total cards (14 times 6 = 84) | 65 + 19 = 84 | 74 + 9 = 83, plus the visitor's card = 84 |
| Was good / Could improve | 49 / 16 | 68 / 6 |
| Responses received (shown) | 65 | 74, or 75 with the visitor's card |
| From N collaborators | 10 | 13 |
| Top feedback received | Stakeholder-centric 31, Customer First 27, Respectful 14, Solution-oriented 9 | Takes Initiative 41, Solution-oriented 38, Respectful 22, Transparency 17 |
| Improvement areas | Share context earlier 9, Repeated across 4 cycles; Resolve dependencies sooner 6, Repeated across 3 cycles | Share context earlier 4, Repeated across 2 cycles |
| Anonymized Feedback | Cycle 5: "The client meeting went well because you knew what their CFO would ask. Please bring us in earlier when the storyline changes." | Cycle 6: "You rebuilt the cost model after the scope change and walked two of us through it before the client call. It saved us the week." |

Checks on the table: every positive tag count is at most the Was good count (31 and 41 are the largest, against 49 and 68); every constructive count is at most the Could improve count; "Repeated across N cycles" is at most 6; collaborators are at most 14. "No interaction" share is 23% for Tara and 11% for Nikhil, against 21% in the prototype's team distribution.

Story choice: Tara is not weak. She has a 75% positive share (49 of 65), strong client tags, and a fair constructive signal. The turn is breadth and volume: Nikhil's cards come from 13 of 14 people and mostly say he takes initiative and solves problems, while the partner saw little of it.

### Step 4: The turn

- H2 (display serif, verbatim): "The engagement ends. The evidence stays."
- Text, by pick:
  - Picked Tara: "You picked Tara, and you might still be right. Partners still decide. What changed is what you are deciding on: 13 colleagues watched Nikhil work for six cycles, and almost none of that reached you in a client meeting."
  - Picked Nikhil: "You picked Nikhil on a hunch. Now the hunch has a record behind it, from 13 colleagues over six cycles, in their own words. Partners still decide, and now they can point to what the people who saw the work said."
  - No pick, or no JavaScript: "Partners still decide. Sphyr gives them the view of the people who saw the work, cycle by cycle, while the engagement team is still together."
- Actions: primary button "Book a 20-minute call" (opens the shared `#call-note`); secondary link "Back to home" (`index.html`).

"X, not Y" count planned on the page: 0. The old closing line ("not one manager's memory") is not carried over.

### Old demo content not carried over

- The IT founder framing, 1 to 5 stars, "Send anonymously", "Anonymous. Released later, in a batch.", the "out of 5" pooled table, "Most-used tag ... from 9 different people across 3 teams", the price and pilot buttons, links to `pricing.html` and `trust.html`, the "That's Sphyr." closer.

## Open questions for the lead (each with my default)

1. Scores next to people. The brief asks for both consultants' pooled records side by side; the message guideline (section 9) and slop rules ban scores next to people. Default: no score numbers, no overall score, no seven-dimension bars, no trajectory chart. The frame shows only response counts, collaborator counts, tag counts and comments. Option: add the seven dimension bars (prototype row names) without numbers. Which do you want?
2. The manager's per-member drill-down was never captured rendered; only its strings exist (from the bundle: "Top feedback received / Most frequent positive anonymized signals", "Improvement areas / Recurring constructive signals to coach", "Anonymized Feedback"). Default: build the columns from the captured member Insights layout (prototype 3.1) with those manager strings, under the standard caption. Is that acceptable, or should someone capture the real drill-down first?
3. Names. Persona names and prototype demo names are both banned. Default: "Tara Menon" (visible) and "Nikhil Rao" (quiet) with the label "an example, not real consultants". I made the quiet one a man to avoid the old quiet-woman pattern. Option: "Consultant A" and "Consultant B".
4. Reveal or all visible. Default: steps 2 to 4 appear one at a time below the previous step, so the turn is not spoiled. Option: all four visible from the start, with only local changes.
5. Tags. Default: the prototype's VBA tags on the card and the same tags counted in the pooled view, so a visitor sees their tags again. The prototype's manager screens use the older tag set ("Did a good job", "Delayed my work"); I do not mix the two. Option: write sample firm values for a consulting firm (the product lets the admin set them), which adds invented sample tags.
6. The seconds line ("That took you 14 seconds") is page copy measured on the page, not a product feature and not the 2018 pilot figure. Keep it?
7. `journey_map.md` and `acquisition_engagement.md` mention a monthly note sign-up after the walkthrough. My brief gives only two next steps. Default: no sign-up on this page.
8. Shared styles and icons (see Dependencies above).

Status: plan awaiting approval. HTML blocked until sitecss is merged into `iteration-a`.

## Approval (2026-11-25)

Lead approved the plan and script with all defaults: no scores, no overall score, no dimension bars; drill-down built from the member Insights layout with the manager strings; Tara Menon and Nikhil Rao labelled as an example; one step at a time; prototype VBA tags only; keep the measured seconds line; no sign-up; use the base.css catalogue. Nav copied from `site/_template.html` with `aria-current` on nothing. sitecss merged at c705c3e.

## Progress (2026-11-25)

Success number: 0 failed checks in 12 of 12 check profiles, and 9 of 9 walk paths correct.

- Merged `iteration-a` (c705c3e) into `d1-walkthrough`. Built `site/demo.html`, `site/css/demo.css`, `site/js/demo.js` to the approved script.
- Humanizer pass by hand on all page copy and reply strings. Changes: intro lede merged into two sentences; step 3 text now states the counts (13 of 14 against 10) in place of "Read the two columns side by side"; the two step 4 branches rewritten to drop "What has changed is what you decide on" and a doubled "now"; the "No interaction" reply ends on the reason for the option, no longer a one-line closer.
- Bug found in the walk and fixed before commit: for "Could improve", the count bump hit the area title `<b>` and wrote NaN into it. It now targets `.num`.

## Final

### Files written, with commits (branch `d1-walkthrough`, nothing pushed)
- 878baed "Add consulting walkthrough page": `site/demo.html` (replaces the old IT walkthrough), `site/css/demo.css`, `site/js/demo.js`.
- da83b15 "Add walkthrough screenshots": `site/_shots/demo-{light,dark}-{1280,375}.png` (full page, after the Tara and "Was good" path, not linked from any page).

### Checks (method and numbers)
Browser: the shared Playwright MCP browser was busy ("Browser is already in use"), so I used a separate headless Google Chrome via a cached `playwright-core` (scripts in my scratchpad, not in the repo), against the lead's server at http://127.0.0.1:8823/site/demo.html. Themes were set by `prefers-color-scheme` emulation, not by the toggle.
- Walk: 3 picks (Tara, Nikhil, none) times 3 answers = 9 paths. All 9: steps 2 to 4 revealed (3 locked at load, 0 after submit), focus on the step 3 heading, the right step 4 branch, the right submitted icon. "Was good" with Takes Initiative: responses 74 to 75, Takes Initiative 41 to 42. "Could improve" with Share context earlier: 74 to 75, area count 4 to 5. "No interaction": 74, no change, no caption line. A typed `<b>x</b>` comment rendered as text (0 injected elements). 0 page errors, 0 failed requests.
- Profiles: reduced motion and motion on, light and dark, widths 1280, 375 and 390 (12 runs). In all 12: contrast failures 0 (114 to 117 visible text nodes, computed colours against the nearest solid background, 4.5:1 under 24 px, 3:1 above), sideways scroll 0, smallest text 11 px, running animations 0 at 2.1 s after load and 0 at 2.1 s after the last step.
- No JS: all 4 steps visible, the card's "Could improve" step opens through the CSS radios.
- Keyboard: arrow key in the pick group selects Nikhil and moves focus to the step 2 heading; Space on "Was good", Enter on Submit moves focus to the step 3 heading.
- `copy_scan.py`: 179 strings, 3 hits, all reviewed: "review" inside prototype strings ("Your comments and review are always anonymized.", "Review individual performance signals...", "Review period"). `copy_tells.py`: 1 contrast ("Tara and Nikhil are an example, not real consultants.", the lead-approved label, the page's one allowed), 1 triad flag (the footer names from the shared template). Dashes in my three files: 0. Month names: 0.
- Links: every relative `href` and `src` on the page resolves to a file in `site/`. `index.html#how`, `#partners`, `#pricing` resolve only once the new home page lands (sitecss note).
- `contrast.mjs` not run: I added no colours; demo.css uses tokens only.

### Key insights and findings
- The prototype shows two tag sets: the card's VBA tags and the older set ("Did a good job") in the manager views. The page uses only the VBA tags, so the tags a visitor taps reappear in step 3.
- The manager per-member drill-down was never captured rendered. Step 3 uses the member Insights layout (prototype 3.1) with the drill-down strings from the bundle ("Top feedback received / Most frequent positive anonymized signals", "Improvement areas / Recurring constructive signals to coach", "Anonymized Feedback") plus the manager header and "Review period: Last Cycle | All Cycles".
- Without scores the turn rests on three things the prototype shows: collaborators (13 of 14 against 10), tag counts (Takes Initiative 41, Solution-oriented 38 against Tara's client tags) and one comment each. Step 3's text names the first two directly, so the turn reads even if the visitor only skims the frame.

### Decisions I made and why
- Step 3 frame uses `role="group"`, not `role="img"` as `faux_ui.md` asks. The frame changes when the visitor's card lands, and its tags and comments are the point of the step, so a screen reader user should read them as text.
- No-flash for the locked steps: the head script adds class `js` to `<html>` (one extra statement in the copied template script), and `.js .wt-locked` hides steps 2 to 4. Without JS every step shows.
- "Add a comment" is a `details`/`summary` (works without JS and with the keyboard) styled as the prototype's button.
- After Submit the card body becomes the prototype's "Completed Feedback This Fortnight" row with "Submitted · Read only"; the prototype's emoji is drawn as the Lucide smile, frown or minus icon (no emojis on the site).
- The step 4 heading is the core line verbatim; step 4 is an unequal pair with the call button as the one primary in that view. Layout families on the page: document column (intro), split (steps 1 and 2), wide figure (step 3), unequal pair (step 4).
- Bars in step 3 use one scale (50) for both columns so they compare fairly. "Share context earlier" for Nikhil is taken as repeated in cycles 3 and 6, so the visitor's cycle 6 card keeps "Repeated across 2 cycles" correct.

### Approaches rejected and why
- A stepper that swaps the whole view: breaks "every interaction answers locally" and the changed-share limit.
- Score numbers, the overall score, dimension bars and the trajectory chart: lead decision (1), message guideline section 9.
- Reusing `.fx-flow` and `.fx-fade` for step 3: the fade would hide words at the foot of the window; the window shows whole.

### Open questions
- `_template.html` says to put `aria-current="page"` on the walkthrough button on demo.html; the lead said nothing. I followed the lead. The template comment should be updated by sitecss.
- The nav's "See the 2-minute walkthrough" button links to this same page. Kept as copied.
- On phones step 3 stacks the two columns, so the side by side comparison becomes top and bottom. The step 3 text carries the comparison in words.

### What I did not verify
- The theme toggle on this page (shared `theme.js`), the nav Menu popover and the call-note popover open and close (shared parts; only that the button has `popovertarget="call-note"`).
- Safari and Firefox, touch emulation, a real screen reader.
- The seconds line with a human pace (the script measured 1 to 2 seconds).
- Changed-share per interaction in pixels (not measured; each interaction changes the step it is in, and reveals the next step below).

### Revision after review (2026-11-25), replaces earlier claims where they differ

Success number: 0 failed checks in 12 of 12 profiles plus 8 of 8 open-card contrast runs; 9 of 9 walk paths correct; the step 1 and step 2 answers in view after the click at 1280 and 375.

Commits on `d1-walkthrough`, newest first (nothing pushed):
- f60bd23 "Retake walkthrough screenshots" (`site/_shots/demo-{light,dark}-{1280,375}.png`)
- 0fb0fcc "Keep walkthrough answers in view, use names over pronouns" (`site/demo.html`, `site/css/demo.css`, `site/js/demo.js`)
- b3a1ecb merge of `iteration-a` (brings the roles-over-pronouns rule 6404e61 and the sitecss favicon and narrow-nav changes)
- da83b15 and 878baed as listed above. The shots in da83b15 are superseded.

What changed and why:
- The first build broke its own rule. Each reveal scrolled the new step to the top and moved focus to its heading. That pushed the local answers (the pick reply, the seconds line and the reward line) off screen. A focus move on a radio change also breaks arrow-key browsing between the two picks (WCAG 3.2.2). My earlier "Keyboard" check counted focus landing on the step 2 heading as a pass; that was wrong. Now: a pick reveals step 2 below with no scroll and no focus move. Submit reveals steps 3 and 4 below and moves focus to the submitted row (`#card-done`, `tabindex="-1"`, no scroll). This departs from the approved plan ("focus moves to its heading"), because the brief says every interaction answers locally.
- On phones the card shrinks on Submit, which left the reply above the screen. The step 2 reply now sits under the card frame. After Submit, if the reply is not in view, the page brings the submitted row back under the sticky nav (instant, `scroll-margin-top: 80px`). On desktop nothing moves.
- Roles over pronouns (lead message, guideline section 5): the step 1 memories and the step 3 text name Tara and Nikhil instead of "she", "he", "him", "his". Grep for he, she, him, her, his in my page and script: 0.
- Copy: the Tara branch of step 4 no longer says "you might still be right, because partners still decide". It reads "You picked Tara, and you might still be right. Partners still decide, and you now decide with more in front of you: ...".
- Favicon lines synced with the updated `_template.html`.

Checks after the fix (same headless Chrome method as above):
- Walk, 9 paths: same counts as before (responses 75 or 74, Takes Initiative 42, Share context earlier 5, typed HTML not parsed). Focus ends on `card-done` in all 9. 0 page errors.
- Answers in view, viewport at 1280 by 900 and 375 by 812: after the pick, the reply and the checked pick are fully in view at both widths. After Submit, the reply and the submitted row are fully in view at both widths. Checked by bounding boxes and by eye on the viewport screenshots.
- Keyboard: Space selects Tara, ArrowDown moves to Nikhil and focus stays on the radio (`wt-pick:nikhil`). The next Tab lands on the first card answer.
- No-flash: with `sphyr-theme=dark` stored, the system set to light and `js/theme.js` blocked, the page loads with `data-theme="dark"` and a dark body (rgb 23, 21, 19), and the `js` class is set. Toggle: `aria-pressed` goes from false to true and the body goes from rgb 250, 248, 244 to rgb 23, 21, 19.
- Contrast on the open card (not covered before): light and dark, "Was good" and "Could improve", one tag checked, comment open, 1280 and 375. 8 runs, 0 failures, 58 to 66 text nodes, smallest text 11 px, sideways scroll 0. Placeholder text is not a text node and was not measured.
- 12 profiles after Submit (reduced motion and motion on, light and dark, 1280, 375, 390): 0 contrast failures, sideways scroll 0, smallest text 11 px, 0 running animations 2.1 s after load and after the last step.
- `copy_scan.py`: 179 strings, the same 3 reviewed prototype "review" strings. `copy_tells.py`: 1 contrast (the lead-approved sample label), 1 triad flag (footer names). Dashes 0. Month names 0.

Still not verified: the call-note and Menu popovers, Safari and Firefox, touch emulation, a screen reader, the seconds line at a human pace, changed share in pixels.

### Full-colour logo (2026-11-25)
- Merged `iteration-a` (d1e0160, brings d9ba411). Nav and footer marks in `site/demo.html` now use `class="mark"` (2 places). The nav, footer and icon lines match `site/_template.html` exactly (diff empty).
- 91dff19 Use full-colour logo and d44894d Retake walkthrough screenshots with full-colour logo.
- 12 profile runs after the change: 0 errors, 0 contrast failures, sideways scroll 0, smallest text 11 px, 0 running animations. Logo colours in the dark theme checked by the run only, not by eye.
