---
type: Handoff
title: "Design teammate report, phase 1a"
description: "Plan, approvals, progress and final summary from the design work: tokens, contrast results, faux UI decisions, rejected approaches and unverified items."
tags: [handoff, design]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T17:30:00Z }
---

# Design teammate report, phase 1a

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Status: phase 1a deliverables done 2026-11-24. Waiting for the lead; homepage mockup (phase 1b) not started.

Worktree: `Product-Marketing-final-assignment.d1-design`, branch `d1-design`, based on `iteration-a` at eeb4c1c.

Read so far: `common.md`, `design.md`, `docs/index.md`, `docs/decisions/decision_log.md`, `docs/product/brand.md`, `docs/product/prototype_screens.md` (sections 3.0 to 3.8), `docs/product/do_not_claim.md`, `docs/site_audit/design_audit.md`, the phase notes in `docs/plan/iteration_a_plan.md`. Skills loaded: `design-taste-frontend`, `stageshow`. Not yet loaded: `hack-kit:okf-docs` (I load it before writing any doc).

## Plan

### Success number
One number: the count of text colour pairs that fail WCAG AA across both themes. Target 0. I report it first in every update, with the total number of pairs checked. Supporting checks: 8 of 8 screenshots saved, 0 validator errors, no theme flash on reload in a scripted test.

### Design read (one line)
A credibility-first B2B marketing site for the head of talent at a 40 to 400 person Indian management consulting firm, in a calm, document-like language that borrows the Sphyr prototype's own UI (Manrope, cool neutrals, emerald, orange as "could improve"), light-first with a full dark theme. Dials: variance 4, motion 2, density 4. Reason: the buyer is wary of tech jargon, the brief grades message not looks, and the strongest asset on the current site is honest labelling, so the look should get out of the way.

### Decision 1 (needs approval): stageshow as a method, not as code
The stageshow kit is React, react-dom and lucide-react, filmed through Vite (`scripts/film.mjs --gate`). The brief requires plain HTML, CSS and JS with no build step and no new dependencies, and in phase 2 I rewrite `site/style.css` and `site/main.js`, so React code would not carry over.

Proposal:
- Use stageshow's references as the rule set: `framing.md`, `craft.md`, `verify.md`, plus the closest gold examples (`static-card`, `close-up`, `fade-crop`) filmed once in the stageshow preview as visual reference only. Those reference stills stay in my scratchpad, not the repo.
- Port the geometry I need by hand to plain CSS: window chrome, row, placeholder bar, crop and bleed, edge fade, one satellite card.
- Faux UI is still frames. No cursor animation. At most one small state change (selecting a tile on the feedback card), because the existing site's interactive feedback card was praised and the motion has a clear reason (it shows the action the reviewer takes).
- The stageshow `--gate` check cannot run on plain HTML. I verify with Playwright screenshots plus the `verify.md` checklist by hand. I will not write "rehearsal passed" anywhere.
- The taste skill's stack defaults also do not apply here: React or Next, Tailwind, Motion, icon npm packages, and its ban on div-built product previews. The brief overrides them, and the taste skill's section 13 puts product UI out of its scope. The faux UI is a real component rendering of real prototype screens, not a decorative fake dashboard. I apply the taste skill to the marketing surfaces only.

### Decision 2 (informational, already checked): brand colours fail AA as text
I ran a contrast script on the prototype tokens (WCAG 2.x formula):
- White text on emerald `#009163`: 4.02:1. Fails AA for normal-size button text (needs 4.5).
- Emerald `#009163` on page background `#F6FAFD`: 3.83:1. Fails as link or body text.
- Orange `#E1712D` on white: 3.18:1. Cannot be a text colour.
- Muted text `#5E6A7A` on `#F6FAFD`: 5.24:1. Passes.
- Accent text `#005B38` on mint `#DBF8EB`: 7.30:1. Passes.
- Constructive text `#4C1E01` on cream `#FFEED2`: 12.33:1. Passes.
- Dark theme primary `#34C696` with `#040A16`: 9.12:1. Passes.

So in light theme the emerald splits into two roles: a darker emerald for button fill and link text (I target about 5:1 or better, near `#007A52`, exact value chosen by the script), and `#009163` kept for large or non-text use (chart lines, focus ring, the radar series). Orange stays a surface and icon colour only; its text is `#4C1E01` on cream. I check every pair in both themes, including muted text on the page background and on cards, placeholder and helper text, and focus rings at 3:1 against adjacent colours. The script lives in `design-lab/contrast.mjs` (Node, no dependencies) and its output table goes into `design_system.md`.

### Decision 3 (needs the lead): faux UI copy and sample data
1. The prototype's sample data is developer-flavoured ("Senior Developer", "Team Coders", "Sphyr UI / UX", "Coder / Developer"). The buyer runs a consulting firm. My recommendation: keep the layout, components, labels and microcopy exactly as in the prototype. VBA tags are configurable per firm in the product, so swapping in consulting-style VBA tags is truthful. Swap the sample people, roles and team name to consulting ones (for example a senior consultant on an engagement team) only if the lead approves, and label every frame as sample data. The strategy teammate owns the persona copy, so I would take names and roles from strategy, or use neutral placeholders until phase 1b. Which do you want: (a) prototype data verbatim, (b) consulting sample data from strategy, (c) consulting VBA tags only, prototype people kept?
2. Some source copy contains em dashes: the Jul 18 quote (an em dash joins "this cycle" and "you connected") and the page titles (an em dash between the page name and "Sphyr"). The project rule bans em dashes. I plan to pick other quotes where one exists, replace the dash with a full stop or comma where it does not, and log each change in `faux_ui.md`. Confirm this is acceptable.
3. The prototype's app icon is a green rounded square with a white sparkle glyph. Stageshow flags sparkle icons and "a glyph in a coloured square" as stock AI tells, and `do_not_claim.md` warns the sparkle must not imply AI. Options: (a) reproduce it faithfully inside the faux chrome because it is the product's real icon, (b) use the ribbon sphere mark in the faux chrome, (c) omit the app icon from the crop. I recommend (c): crop past the icon rail so the question does not arise, and use the ribbon mark only in site chrome.
4. The manager team insights screen includes "Feedback edit approvals", which shows who gave feedback to whom. If I show the manager view, I will not crop it in a way that implies full anonymity. Captions use the common.md wording: ratings are pooled and comments are anonymized to the person rated. I propose to show the team benchmark and standouts on the home or how-it-works page, and the edit approvals card honestly on the trust page with a caption that explains what the manager sees. Confirm.

### Decision 4: theme toggle with no flash
- An inline blocking script in `<head>`, placed before the stylesheet link. It reads `localStorage` key `sphyr-theme`; if absent it uses `matchMedia('(prefers-color-scheme: dark)')`; it sets `data-theme` on `<html>`.
- CSS sets `color-scheme: light` or `dark` per theme, and a `<meta name="color-scheme" content="light dark">` so form controls and scrollbars match before CSS loads.
- The toggle is a `<button>` with a visible label and `aria-pressed`, keyboard reachable. It stores the explicit choice. When no choice is stored, the page follows live system changes.
- Two states (light, dark) that start from the system setting. I do not plan a third "system" state; say if you want one.
- Proof of no flash: a Playwright test that stores dark, reloads, and checks at DOMContentLoaded that `<html data-theme="dark">` is set and the computed body background is the dark token. Also a check with storage empty under emulated dark and light `prefers-color-scheme`. Results go in the report.
- Before building it, I research current practice with firecrawl and exa, and cite dated sources (access date 2026-11-24) in the `sources` frontmatter of `design_system.md`. If the research contradicts this approach, I report it before deciding.

### Decision 5: eyebrow rule
The prototype puts a small uppercase green eyebrow on every page header, and the audit calls eyebrows the number one slop tell. `slop_rules.md` will state: eyebrows stay inside faux UI frames because that is the real product; on site sections they are rationed to at most 1 per 3 sections, in Manrope (not mono), and never above every heading.

### Decision 6: assets, font, icons
- Logo: the ribbon PNG is RGB on white with no alpha, so it shows a white box on dark. I use the SVG. I check its near-white highlight paths (`#F8F9F9`, `#F0F6F6`) on the dark background; if they read as holes I note it and propose a dark-theme treatment (I will not edit the logo's shape or colours without approval).
- Font: Manrope only, which ties the site to the product. I drop Inter and JetBrains Mono. Numbers use Manrope tabular figures. Loading: self-host one Manrope variable woff2 (SIL OFL) in `design-lab/fonts/` with `font-display: swap` and a preload, replacing the render-blocking `@import`. It is a file, not a package dependency. Alternative: a Google Fonts `<link>` with preconnect. I recommend self-hosting.
- Icons: the prototype uses Lucide-style line icons. With no dependencies allowed, I paste the few inline SVGs I need verbatim from Lucide (ISC licence, noted in a comment) for faux UI only. Site sections use no icons unless a component needs one.

### Files

1. `docs/design/design_system.md` (OKF concept file). Outline: direction paragraph; colour roles for light and dark (surface, surface raised, text, text muted, border, primary action, primary text on action, link, positive, constructive surface and text, destructive, focus ring), each with hex and the measured contrast pair; type scale (Manrope, about six steps, fluid clamp for display only); spacing scale (4px base); radius (12px cards from the prototype, 8px inputs, buttons one documented rule); elevation (two levels, shadows tinted to the background, none in dark, surface steps instead); components (nav, footer, theme toggle, buttons, section layouts with at least four distinct families, cards, tables, quote, stat, faux UI frame, prototype label, note or disclaimer); motion (hover and press feedback only, 150 to 200 ms, one ease; all off under `prefers-reduced-motion`); theme toggle behaviour with sources.
2. `docs/design/slop_rules.md` (OKF concept file). Do and do not lists for page builders, grouped by visual, layout, type, copy and faux UI. Sources: the design audit items with their file and line, plus the taste skill rules that apply to a static B2B site. Includes the eyebrow rule, no hero glow, no three identical cards, no mono labels, no "X, not Y" closers as a habit, no staccato triads, no invented numbers, one accent, one radius rule, honest labels kept.
3. `docs/design/faux_ui.md` (OKF concept file). For each screen (feedback card 3.3, member insights 3.1, manager team insights 3.7, and edit approvals if approved): where it goes on the site and which message it supports, the crop (which panel, what bleeds, what is left out), the real strings kept (3 to 7 per frame), the label text, and every copy change from the prototype with its reason. The label wording proposal: "Prototype screen. Sample data, fictional people." placed below the frame, not on it.
4. `docs/design/index.md` and `docs/design/log.md`, built with `build_index.py --root docs design`. I do not touch the root `docs/index.md` or `docs/log.md`.
5. `design-lab/tokens.css`: custom properties for both themes on `[data-theme]`, the `@font-face`, base type and spacing scale. Written so phase 2 can lift it into `site/style.css` as is.
6. `design-lab/components.html`: every component listed above, rendered once, with the working toggle and the inline no-flash script. A side-by-side light and dark strip is not used; the toggle switches the whole page (page theme lock).
7. `design-lab/faux-ui.html`: the three faux UI frames in site context (frame plus caption plus label), both themes via the toggle, desktop and a compact 358px design per frame (a redesign, not a squeeze, per stageshow framing rules).
8. `design-lab/theme.js`: the toggle logic shared by both lab pages (the head script stays inline). `design-lab/contrast.mjs`: the contrast check, run with `node design-lab/contrast.mjs`, exits non-zero on any failure.
9. `design-lab/shots/`: 8 PNGs, named `<page>-<theme>-<width>.png`, for components and faux-ui, light and dark, 1280 and 375, full page.

### Steps, in order
1. Load `hack-kit:okf-docs`. Research theme toggle practice (firecrawl, exa), dated.
2. View the live prototype in Playwright at 1280, both themes, for component style; capture the dark theme tokens that the docs did not record. Film the stageshow gold references.
3. Write `contrast.mjs`, pick tokens until 0 failures, write `tokens.css`.
4. Build `components.html` and `theme.js`; test the toggle and the no-flash reload.
5. Build `faux-ui.html`.
6. Write the three docs, build the folder index, run the validator.
7. Take the 8 screenshots, review them against the slop rules and the stageshow checklist, fix, retake.
8. Commits, one per group: docs; tokens, components and toggle; faux UI; screenshots.
9. Final report: files, SHAs, contrast count, a section "taken from the prototype, changed, and why", open questions, what I did not verify.

### Open questions for the lead
1. Time budget: how long do I have? If it is under about 3 hours, I propose to cut the compact 358px faux UI designs and ship the 1280 frames plus a simple scaled version at 375.
2. Decision 3 items 1 to 4 (sample data, em dash replacement in quotes, app icon, manager view placement).
3. Self-host Manrope (recommended) or Google Fonts link?
4. Two-state toggle starting from the system setting (recommended), or three states?
5. Approve the stageshow-as-method approach in decision 1, including that the stageshow gate cannot run.

## Approval (2026-11-24)
Lead approved the plan with these answers: no hard time limit, keep the compact 358px designs; sample data option (b), consulting people, roles, team and VBA tags read from `docs/strategy/` in the d1-strategy worktree (not copied), neutral placeholders until then; em dash replacement in quotes approved and logged in faux_ui.md; app icon option (c), crop past the icon rail; manager view placement approved; self-host Manrope with the OFL licence next to the font; two-state toggle from the system setting; stageshow as a method only, never claim the gate ran.

## Progress

### Step 1 done: theme research (2026-11-24)
Sources: Chrome for Developers, "Dark mode toggles" (https://developer.chrome.com/docs/modern-web-guidance/guides/ui-components/dark-mode-toggle) and MDN `light-dark()` (https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark), both accessed 2026-11-24.
Findings that refine the approved approach (no change to the decision):
- CSS must work without JS: with no stored choice the page follows the system through `color-scheme: light dark`. Colours use `light-dark()`, Baseline widely available (since May 2024 per MDN).
- The inline head script stays tiny and only applies the stored value. Wrap `localStorage` in try/catch.
- Two-state toggle rule: the target is the opposite of what is rendered now. If the target equals the system setting, remove the stored value instead of storing it. Never remove a stored value later just because the system changed to match it. Sync other tabs with the `storage` event.
- Two states are the recommended form for a toggle in site chrome. A way back to "system" exists through the rule above.

### Step 2 done: prototype viewed (2026-11-24)
- Read the full light and dark token set from the live prototype's CSS (Playwright, computed via canvas from OKLCH). Dark theme values the docs lacked: foreground #F4F7FB, muted text #A5B3C1, border #2C394A, accent #043123 with text #A4E9CB, positive #27CF9B, constructive #F7A224 with text #FFD69A on #3D1D00, destructive #FF655A, popover #121C2B, avatar tints.
- Confirmed: Manrope, Lucide icons (the app icon is `lucide-sparkles`), H1 30px, cards 12px radius with hairline border, buttons 14px weight 500.
- Reference screenshots (feedback, insights, team insights, light and dark) are in the main repo's untracked `.playwright-mcp/ref/`, not committed.
- Deviation: I did not film the stageshow gold examples. That needs `npm install` of the React kit and a Vite dev server. I read `framing.md` and `craft.md` in full and ported the shadow tokens from `kit/stage.css` instead.
- Strategy files are not in `docs/strategy/` on d1-strategy yet. Faux UI uses neutral placeholders until they land.

### Steps 3 to 5 done (2026-11-24)
Success number: 0 AA failures in 70 contrast checks (35 pairs x 2 themes), from `node design-lab/contrast.mjs`.
- `tokens.css`: light and dark via `light-dark()`; Manrope self-hosted (latin variable woff2, 24 KB) with `OFL.txt` beside it. Light action green changed from #009163 to #007652 (white text 5.66:1); destructive from #DF312F to #C62B29 (5.30:1 on page). Added `--border-strong` (#7B8799 / #5B6B80) for control outlines at 3:1.
- Theme toggle test (Playwright, components.html, 7 scenarios): all 7 correct. On reload with a stored choice the first animation frame already has the stored theme and its background (light stored under dark system: rgb(246,250,253); dark stored under light system: rgb(4,10,22)), so no flash. Toggling back to the system value removes the stored key; a system change does not clear a stored choice.
- 375px: no horizontal overflow on either lab page (checked by script, n=2 pages).
- Faux UI: feedback card (interactive, radio inputs, no JS), member insights, team insights, benchmark radar, edit approvals, plus each frame's compact 358px design. Review fixes made: satellites covered words on 2 frames, team satellite removed (any card over that window covers names or scores), radar moved to its own frame, flow layout so stage height follows content.
- Icons: 27 Lucide icons in an SVG sprite, copied verbatim, ISC licence file included.
- Commits: 95824f1 (tokens, components, toggle, contrast), e3e82ae (faux UI).
- Strategy files still absent at 2026-11-24; placeholders in use (Member A to E, consulting roles, "Engagement team VBAs").

### Steps 6 to 8 done (2026-11-24)
- After review: strategy files landed on d1-strategy (2f3a4b7). Applied message guideline section 9 to the faux UI; see Final.
- Docs: `docs/design/` with design_system.md, slop_rules.md, faux_ui.md, index.md, log.md. Validator: 0 errors, 3 warnings, all 3 in files I do not own (brief, prior_work).
- `build_index.py --root docs docs/design` also rewrites the root `docs/index.md` (adds a design line). common.md forbids editing the root index, so I restored it with `git checkout docs/index.md`. The root index therefore does not list `docs/design/` yet. The lead needs to add it at merge.
- Screenshots: 8 PNGs in `design-lab/shots/` (5.2 MB), taken with system theme emulated and storage cleared, reduced motion on.

## Final

### Success number
0 WCAG AA failures in 80 contrast checks (40 token pairs x 2 themes), `node design-lab/contrast.mjs`, commit b511713. The pairs are listed by hand; the script does not sweep rendered pages.

### Files and commits (branch d1-design)
- 95824f1 `design-lab/tokens.css`, `components.css`, `components.html`, `theme.js`, `contrast.mjs`, `fonts/manrope-latin-wght.woff2`, `fonts/OFL.txt`, `assets/sphyr-logo.svg`, `assets/icons.svg`, `assets/LUCIDE-LICENSE.txt`
- e3e82ae `design-lab/faux-ui.css`, `design-lab/faux-ui.html`
- 2412023 `docs/design/design_system.md`, `slop_rules.md`, `faux_ui.md`, `index.md`, `log.md`
- 980316e `design-lab/shots/` (8 PNGs: components and faux-ui, light and dark, 1280 and 375)
- ed4a817 manager frame changed to team-level panels; anonymity wording limited to what the prototype shows; faux UI VBA group titles changed from `h4` to `div` (no headings inside product frames); `container-type` scoped to `.figure:has(> .stage)`; 5 more contrast pairs
- 1909caa docs aligned with `docs/strategy/message_guideline.md` section 9 (d1-strategy, commit 2f3a4b7)
- b511713 8 screenshots retaken
Extra files beyond the brief's list: `components.css`, `faux-ui.css`, `theme.js`, `contrast.mjs`, `fonts/`, `assets/`. Each is needed by the lab pages and is meant to lift into `site/` in phase 2.

### Taken from the prototype, changed, and why
Taken: Manrope; the full light and dark token set (read from the live CSS); 12px surface radius; hairline cards; green = strength, orange = could improve, red only for destructive; Lucide icons; the feedback card, insights, team insights, benchmark and edit approvals screens with their labels and microcopy; the product's own "Anonymized feedback" item as the site quote style.
Changed:
- Action green #009163 to #007652: white text on #009163 is 4.02:1 and link text 3.83:1, both fail AA. #009163 kept for non-text.
- Destructive #DF312F to #C62B29: 4.33:1 on the page.
- Faux UI eyebrow text uses #007652 for the same reason.
- New `--border-strong` for 3:1 control outlines (prototype input border about 1.4:1) and `--stage-ground` for the frame well.
- Sample people, roles and team name replaced by neutral consulting placeholders (Member A to E, "Engagement team VBAs"); demo names must not appear.
- Icon rail and sidebar cropped out (approved option c), which removes the sparkle app icon.
- Dropped Inter, JetBrains Mono and the render-blocking Google Fonts import.

### Key insights with sources
- Two-state toggle rule: target is the opposite of what is shown; if it equals the system setting, remove the stored value; never clear a stored value on a later system change; CSS must work without JS. Chrome for Developers, https://developer.chrome.com/docs/modern-web-guidance/guides/ui-components/dark-mode-toggle, accessed 2026-11-24.
- `light-dark()` is Baseline widely available since May 2024. MDN, https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark, accessed 2026-11-24.
- The prototype's brand green fails AA as small text (my contrast script, WCAG 2.x formula, self-checked against 21:1 for black on white).
- Any satellite card over the manager view covers a name or a score, so that frame has none (found in visual review, 2 review rounds).

### Decisions and why
- Stageshow as a method only (approved): no build step allowed; the React kit would not carry into `site/`.
- Flow layout for frames: stage height follows content, so no word is cut when copy changes.
- Radar moved to its own frame instead of a satellite.
- Manager frame shows team-level data only (rating distribution, anonymized team feedback). Strategy's message guideline section 9 says never show the "Members Needing Support" list, any screen naming a low performer, or scores on people. This overrides the plan item you approved ("benchmark and standouts"). The standouts version is in commit e3e82ae if you want it back.
- Sample people stay neutral (Member A to E). The message guideline asks for neutral placeholders and defines no consulting sample people or VBA tags, so the prototype's VBA tags stay.
- Anonymity copy says only what the prototype shows ("In the prototype, the edit approvals card shows the manager who gave feedback to whom"). Earlier "only when" and "the one place" wording removed: the manager per-member drill-down was never captured, so "only" cannot be proved.
- Feedback card interaction with radio inputs and CSS `:has()`, no JS: the state change is the product's own and is keyboard accessible.
- Kicker defined as sentence case 15px green, max 1 per 3 sections; uppercase eyebrow allowed only inside product frames.
- Nav: Deliverables button hides under 760px; the footer keeps every deliverable one click away.

### Rejected approaches and why
- Filming stageshow gold examples: needs npm install of the React kit and a Vite server; I read framing.md and craft.md and ported the shadow tokens instead.
- Satellites straddling half outside on the insights frame: left a dead strip of well; the satellite now crosses the edge by 16px over the chart.
- Fixed stage heights: cut chips and text when content wrapped.
- Third "system" toggle state: not approved; the remove-on-match rule gives a way back to system.

### Open questions
1. Root `docs/index.md` does not list `docs/design/` (I may not edit it). Add at merge.
2. Standouts conflict: your approval said "benchmark and standouts"; the strategy guideline forbids standouts. I followed the guideline. Confirm.
3. The guideline's never-show list includes "radar sweeps". The benchmark radar is a data chart, not a sweep, but the team should decide whether to keep it.
4. The guideline suggests showing "My Sphyr" circles. Not built in phase 1a; can add in 1b if wanted.
5. The frame label "Engagement team VBAs" keeps the product's word "VBA", which the guideline lists as jargon to avoid in copy. It is the product's own label; keep or rename?
6. Under 760px the Deliverables button is hidden in the nav. Confirm the footer link is enough, or move it into the scrollable link row in phase 1b.
7. Screenshots add 5.2 MB to a public repo. Keep, or convert to JPEG or WebP?

### Not verified
- Rupee glyph in the Manrope latin subset: a canvas test suggests Manrope renders it; the font file was not inspected.
- Lab pages were tested in Playwright's Chromium only. Safari and Firefox not tested.
- No screen reader test. Keyboard use of the feedback card radios was not tested by hand.
- The logo's near-white highlight paths on dark were checked by eye at 28px only.
- Chart curve and radar shapes are traced by eye from the prototype (labelled as such).
- Strategy docs were read only for sections 6 to 10 of message_guideline.md and grep hits; the persona and journey files were not read in full.
- The "Members Needing Support" icon was matched by eye to Lucide `trending-up`.
