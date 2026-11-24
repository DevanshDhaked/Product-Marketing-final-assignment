---
type: Handoff
title: "Design teammate report, phases 1a and 1b"
description: "Design work from tokens to the homepage mockup: decisions, check results, known gaps and next steps for the site build."
tags: [handoff, design]
generated: { by: claude-code/opus-5-5, at: 2026-11-25T01:10:00Z }
---

# Design teammate report, phases 1a and 1b

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Status: phase 1b complete, homepage mockup built and checked. Stopped for gate 1b. See "Final (handoff)" at the end. Branch d1-design is fast-forwarded to iteration-a (03aef9a).

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

## Plan 1b

Written 2026-11-24 after `git merge iteration-a` (fast-forward to 03aef9a). Read for this plan: common.md (Humanize, Spawn location, Final rules), decision log including gate 1a, `docs/strategy/deliverable_map.md`, `message_guideline.md` sections 1 to 11. Not yet read in full: positioning, journey map, acquisition_engagement, personas.

### Success number
Hits from a scripted check of all homepage copy (including captions, alt text and labels) against message guideline section 4 (never say), section 10 (don't column), the do-not-claim list, and the dash, emoji and hype word scans. Target 0. Reported first in every update with the number of strings checked. Separate gates: 0 WCAG AA failures in `contrast.mjs`, and the toggle test still passing.

### Time
You said "no hard time limit" for 1a. I assume it still holds. Say if not; the order below puts the gated decisions first.

### Step 1: reference research (method only; nothing done yet)
- Galleries: Awwwards Sites of the Day and Honorable Mentions (search by tags such as HR, business, corporate, SaaS, editorial), plus godly.website, siteinspire, land-book and saaspo or lapa.ninja for B2B SaaS.
- Target sites: HR tech, people analytics, performance and feedback tools, and B2B SaaS with a human, editorial feel. Any product name I would guess now is unverified until checked.
- Tools: firecrawl search and scrape first, exa search and fetch second. If Awwwards blocks scrapers, use exa and the galleries' tag pages. Every entry gets a URL and the access date 2026-11-24.
- Output: `docs/design/references.md` (Research Note). For each site: gallery listing URL, site URL, what it does well, and whether it fits a calm, credible look for a head of talent. Then 3 to 5 picks, each with the one specific pattern I borrow (for example a type scale, a section rhythm, a single motion moment) and what I deliberately do not borrow.

### Step 2: typeface (short stop for your pick)
- Research and shortlist 3 pairings with licences. Candidate pools: Google Fonts (OFL), Fontshare (ITF Free Font License), Velvetyne and Collletttivo (mostly OFL), and fonts listed on Uncut (licence varies per font). Direction: a display face with an editorial, human feel plus a calm text face, or one versatile family. A serif display is allowed here because the brief now asks for an editorial feel; the taste rules' bans on Fraunces and Instrument Serif as defaults still apply.
- Licence check per font, from the actual licence text: (a) commercial use on a public website at no cost, (b) self-hosting, (c) the font file sitting in a public git repo (redistribution). If any of the three is unclear or not allowed, I drop the font. I cannot confirm (c) for Fontshare's ITF licence yet; OFL allows all three.
- Build `design-lab/type.html`: each shortlisted pairing set with the real hero line and one section, in both themes, with licence notes. Screenshots at 1280 and 375.
- Stop: report the shortlist with my recommendation and wait for your pick before building the homepage, because everything after depends on it.
- Manrope stays, scoped to `.stage` product frames only, so the faux UI keeps the prototype's UI language.

### Step 3: ribbon motif, tied to the message
Concept: the ribbons are the people who saw the work. It merges with the guideline's core visual (section 9: engagements fading one by one, one continuous record line running through to April).
- Hero or section visual: four or five engagement blocks on a timeline. From each one, a few coloured ribbon strands (the people on that engagement) join the consultant's record line. Each engagement then fades out, but its strands stay in the line. At April the strands wrap into the ribbon sphere, the logo. The picture says "The engagement ends. The evidence stays." without a caption.
- Second use: the circle of people. Strand colour families map to the product's real My Sphyr groups (peers, seniors, subordinates, external). This also answers the guideline's request to show "My Sphyr" circles.
- Third use (optional): the logo assembling once from its strands, in the hero or footer, or a small hover where the ribbons part slightly and rejoin.
- At most 3 uses on the page.
Rules for the build:
- The reduced-motion state and the poster frame tell the whole story with no motion: all engagements labelled, strands joined, sphere formed.
- Inline SVG, because the current `<img>` logo cannot animate its 27 paths. Animate only transform, opacity and stroke-dashoffset. No WebGL, no animation library.
- Scroll-driven CSS (`animation-timeline: view()`) as a progressive enhancement. I will check browser support on MDN with a date. Fallback: an IntersectionObserver that plays once when the visual enters the viewport. No scroll listeners.
- Budget: motif SVG plus script under 25 KB uncompressed (estimate to confirm).
- Colour: the logo includes orange and red, but in the product orange means "could improve" and red means destructive. I propose to keep the full logo palette only on the sphere itself, and give the strands a subset (blues, teals, greens, violets, golds) so they never sit next to product status colours. Ribbons never appear inside product frames.
- Check the logo's near-white highlight paths on the light page too, not only on dark.
- Output: `docs/design/ribbon_motif.md` (concept, rules, motion, reduced motion, colour mapping) and `design-lab/motif.html` as a specimen.

### Step 4: homepage mockup
- File: `design-lab/home.html`, both themes, toggle working.
- Sections from `deliverable_map.md` (website row), each mapped to a message step and a source:
  1. Hero: what April looks like with the whole year in the file. Step 1 and the core idea. Visual: the ribbon core visual. Sources: guideline sections 1, 7, 8.
  2. How it works: two minutes every two weeks. Step 2. Visual: the feedback card frame. Sources: guideline sections 2, 3.
  3. The walkthrough: the primary call to action. Step 5.
  4. What consultants get back: the member insights frame. Step 3, with the anticipation line for consultants. Source: guideline section 7.
  5. For partners: they still decide, on the whole year. Step 3. Visual: the team-level manager frame.
  6. The circle: who gives feedback (My Sphyr groups, clients only when the partner adds them). Ribbon motif second use. Source: guideline section 3.
  7. The method and the honest 2018 pilot: 02:09, attributed exactly; the Scullen, Mount and Goff rater finding; Gallup figure. Source: guideline section 3.
  8. Pilot and scorecard: what every pilot measures and what we publish. Source: acquisition_engagement.md. Pilot length shown as a labelled placeholder (open source conflict: 6 weeks is 3 cycles, a useful record needs about 6).
  9. Price: a clearly labelled placeholder block. `docs/pricing/` does not exist yet.
  10. What Sphyr does not do. Source: guideline section 4.
  11. Vision line and the second call to action. Step 4.
  12. Footer with links to every deliverable.
- Hero choice: the ribbon core visual, because the anticipation rule asks the hero to show what she can look forward to. This moves the feedback card from the hero (the 1a placement) to "How it works". Say if you want the card in the hero instead.
- Copy rules:
  - No persona names on the page (gate 1a). No firm-size number in the hero.
  - One primary call to action label everywhere: "See the 2-minute walkthrough". One secondary: "Book a 20-minute call". Nav, hero and footer use the same words.
  - Approved strategy lines stay word for word and are not humanizer-edited: "The engagement ends. The evidence stays." and the other approved lines in guideline sections 1, 2, 7 and 8 when I use them as written.
  - Everything else I write (connective copy, captions, sample labels, alt text) goes through the `humanizer:humanizer` skill before commit.
  - Acceptance check: guideline section 11 (core idea in the first line, one call to action, every number sourced with its qualifier, nothing from section 4, no dash punctuation).
  - No "after you sign" section yet; `docs/packaging/` does not exist. A labelled placeholder if the section list needs it.
- Layout: at least five different section families, no row of three equal cards, kickers at most one per three sections, per the slop rules.

### Step 5: canonical snippets
`design-lab/snippets/`: `head.html` (color-scheme meta, no-flash script, font preloads, stylesheet links), `nav.html`, `footer.html`, `theme-toggle.html`. Copy-paste files, since the site has no build step. Existing slugs and nav labels kept (How it works, Walkthrough, Pricing, Trust, Deliverables).

### Step 6: docs
- `docs/design/references.md`, `docs/design/ribbon_motif.md`, `docs/design/homepage.md` (section map, copy sources, placeholders, humanizer log).
- `design_system.md`: a dated 2026-11-24 phase 1b addendum for the type change and the ribbon tokens. The 1a text stays; the addendum says which parts it replaces.
- Update `slop_rules.md` only by addendum if the motif needs new rules.
- Log and `docs/design/index.md`; root index untouched.

### Step 7: verification
- `contrast.mjs` after any token change, plus pairs for the new type colours if any.
- Toggle test re-run on home.html.
- Screenshots: home and type, both themes, 1280 and 375, plus home with reduced motion (the poster state).
- Scripted scans: never-say and do-not-claim, dashes, emoji, hype words.
- Size check of the motif SVG and script against the budget.
- Commits per group: research and docs; type; motif; homepage and snippets; screenshots. Report and `## Final` updated before going idle.

### Added after the lead's notes (2026-11-24)
- Skills: I reload `design-taste-frontend` and `stageshow` at the start of execution and apply them to the homepage, the motif and the frames, with the same limits as 1a (no React kit, rules only, never claim the stageshow gate ran).
- Logo variants. I will build and record these, each keeping the ribbon sphere recognisable and every ribbon distinct:
  - Full colour: the original file. Hero sphere and large uses only.
  - Mono light: all ribbons in near-white, separated by thin gaps in the page colour. Dark theme and dark surfaces.
  - Mono dark: all ribbons in near-black ink, same gaps. Light theme small uses (nav, footer, favicon at small sizes).
  - Tonal: ribbons in 4 or 5 steps of one hue (the product green), so each ribbon stays distinct by value. Candidate for the strands in the motif, which would also solve the orange and red conflict in step 3.
  - Each variant is checked at 16, 28 and 120px in both themes, and the separate ribbons must still read at 28px. Variants live in `design-lab/assets/` as SVG; the design system addendum gets a table of variant, file, where it is used and why.
- Open question 3 changes accordingly: strands in the tonal green variant (recommended), a cool subset of the logo palette, or the full palette.

### Open questions
1. Do you approve one stop after the type shortlist (step 2) for you to pick the typeface? My default if you prefer no stop: I pick by the criteria and you can veto at gate 1b.
2. Hero: ribbon core visual (recommended) or the feedback card as approved in 1a?
3. Ribbon colours: strands use a subset of the logo palette without orange and red (recommended), or the full palette?
4. Still open from 1a, not answered in the docs: dropping the manager standouts per the guideline; keeping the benchmark radar ("radar sweeps" rule); the "Engagement team VBAs" label; whether the Deliverables link should stay in the mobile nav row (I propose to add it to the scrollable row in the canonical nav).
5. Who reviews homepage copy for message fit before gate 1b: you, or the strategy teammate?

## Approval 1b (2026-11-24)
Lead approved Plan 1b: stop after the type shortlist with 3 pairings, screenshots and licence verdicts in this report; drop any font whose licence does not clearly allow all three uses. Hero is the ribbon core visual; the feedback card moves to How it works; the interactive walkthrough stays prominent. Build both strand palettes (cool logo subset and tonal green) in motif.html; the motif should feel alive, not corporate. Follow the message guideline: no manager standouts; keep the radar only if the guideline allows it as written; "Engagement team VBAs" is fine; Deliverables stays visible in the mobile nav. Lead reviews homepage copy, then the user at gate 1b. No hard time limit. Proceed with steps 1 and 2.

## Progress 1b
Success number for this stop: 3 of 3 shortlisted fonts have licences that clearly allow all three uses (all SIL OFL 1.1); 1 font family source dropped (Fontshare closed-source, ITF FFL). Homepage copy check not run yet (no homepage copy written).

### Step 1 done: references (commit 075a21a)
`docs/design/references.md`. Sample: 7 Awwwards HR-tagged entries found, 5 live sites viewed at 1280px on 2026-11-24. Awwwards HR entries are mostly recruiters and agencies. Four picks, one pattern each:
1. Inkwell (Awwwards case study, 25 Jun 2025): the home page as a short storyboarded story, proof by persuasion without client names. Not its missing navigation.
2. Make HR Work (Awwwards Site of the Day, 13 Nov 2023): one loud type-and-colour moment, the rest quiet; feels made by people. Not its illustrated character.
3. Culture Amp (viewed directly, no gallery listing confirmed): editorial serif display over a plain sans on a near-white ground. Not its badges, logo strip or AI claims.
4. Lattice (Best SaaS Web Designs listing): real product UI cropped in soft tinted wells. Not its six-tile bento, logo wall or AI section.
Rejected as references: Leapsome (AI-first, badge wall), Master People Platform (Awwwards HM, 21 Dec 2023; stock photos, generic).

### Step 2 done: type shortlist (commit 8628ee0)
Specimen: `design-lab/type.html`. Screenshots: `design-lab/shots/type-light-1280.png`, `type-dark-1280.png`, `type-light-375.png`, `type-dark-375.png`. No horizontal overflow at 375 (n=4 shots). All three set the approved lines "The engagement ends. The evidence stays.", "In April, partners calibrate on the whole year, not the last engagement." and the 02:09 stat.

| # | Pairing | Display | Text | Licence verdict | Files |
|---|---|---|---|---|---|
| 1 | Newsreader with Manrope | Newsreader, editorial serif with optical sizes and a true italic, Production Type, via Google Fonts | Manrope (already in use) | SIL OFL 1.1, no Reserved Font Name. Commercial use, self-hosting and a public repo all allowed. Licence: `design-lab/fonts/shortlist/OFL-newsreader.txt` | 132 KB roman + 147 KB italic, variable (weight and optical size; weight axis checked in browser) |
| 2 | Bricolage Grotesque, one family | Bricolage Grotesque, grotesque with ink traps and an optical size axis, Atelier Triay, via Google Fonts | Same family at text optical size | SIL OFL 1.1, no Reserved Font Name. All three uses allowed. `OFL-bricolage.txt` | 77 KB, variable (weight axis checked in browser) |
| 3 | Apfel Grotezk with Manrope | Apfel Grotezk, quirky grotesque, Collletttivo (independent Italian collective) | Manrope | SIL OFL 1.1, no Reserved Font Name. All three uses allowed. `OFL-apfel-grotezk.txt` (from the collective's GitHub repo) | 3 static weights, about 20 KB each |

Dropped: every Fontshare closed-source font (Satoshi, General Sans, Switzer, Cabinet Grotesk, Zodiak, Gambetta and the rest). The ITF Free Font License (v2.0, 17 Aug 2026, read 2026-11-24 at fontshare.com/licenses/itf-ffl) allows self-hosting for your own site but says the font "may not ... be distributed ... through another font website, font library, marketplace, repository, download service ... publicly accessible servers", and forbids modification without consent, which covers subsetting. A public git repo is a repository, so use (c) fails. Velvetyne's site was down (it showed a strike page), so no Velvetyne font was checked.

My recommendation: 1, Newsreader with Manrope. It is the one that stands apart from every HR vendor page viewed (all set in plain sans), it carries the "human, editorial" feel the user asked for, and its italic gives the second half of the core line its own voice ("The evidence stays."). Manrope stays as text, so the site and the product frames share one sans. Cost: the heaviest files (279 KB for both styles); I would load the italic only for display lines and check whether a weight-only file is smaller. Pick 2 if you want louder and more playful; pick 3 for the most unusual character, at the cost of a less established family.

### IA proposal (new direction: fewest pages and links)
The old site is used for content only, not design. Current site: 9 pages (index, how-it-works, demo, pricing, trust, deliverables, propaganda, linkedin, ad) plus a nav of 4 links and a Deliverables pill.

Proposed: 3 pages.

| Page | File | Holds | Merges |
|---|---|---|---|
| Home | `index.html` | The whole product story in 6 sections (below) | Old home, how-it-works, trust, pricing |
| The 2-minute walkthrough | `demo.html` | The interactive walkthrough, kept prominent | Old demo, rebuilt in the new design |
| Course deliverables | `deliverables.html` | Propaganda strategy, the three LinkedIn posts and the advertisement, one after another, with a 3-item index at the top and anchors `#propaganda`, `#linkedin`, `#ad` | Old deliverables, propaganda, linkedin and ad pages |

Nav on every page (one line, also on phones): Sphyr logo (home), "See the 2-minute walkthrough" (button), "Deliverables", theme toggle. That is 3 links plus the toggle. Deliverables stays visible on phones.

Footer on every page: the walkthrough, "Book a 20-minute call", and the three deliverable anchors (propaganda strategy, LinkedIn posts, advertisement), plus the course credit line. 6 links.

Home sections, cut from 12 to 6. Each carries a message step:
1. Hero (steps 1 and 5): "The engagement ends. The evidence stays.", the moment line, the ribbon core visual, one button to the walkthrough.
2. How it works (step 2): two minutes every two weeks; the interactive feedback card; who rates whom shown as the ribbon circle (peers, seniors, juniors, clients when the partner adds them). A second "Try it in the walkthrough" link here keeps the walkthrough prominent.
3. What people get back (step 3): consultants see their own record (member insights frame); partners see the whole year and still decide (team frame). One section, two frames.
4. Why you can check it (step 3 proof and trust): the rater research (Scullen, Mount and Goff), the 2018 paper pilot 02:09 with its exact qualifier, what Sphyr does not do, and what stays private and what a manager sees. Folds old trust and method.
5. Try it before April (step 5, second step): the pilot and its public scorecard, the price as a labelled placeholder until the pricing work lands, a "How we set the price" disclosure, "Book a 20-minute call". Folds old pricing.
6. Close (step 4): the vision line and the walkthrough button.

Link count per page (estimate; repeated destinations counted each time):
- Home: nav 3, in-page 3 (hero walkthrough, section 2 walkthrough, close walkthrough) plus 1 call link, footer 6. Total 13, to 5 destinations.
- Walkthrough: nav 3, end of walkthrough 2 (book a call, back to home), footer 6. Total 11.
- Deliverables: nav 3, index 3 anchors, 1 walkthrough link per deliverable (3, because each artefact's call to action is the walkthrough), footer 6. Total 15.
Old site for comparison: home page alone had nav 5, about 6 in-page and footer 4 (estimate from the audit, not counted).

Questions for this stop:
1. Type: which pairing (1, 2 or 3)?
2. Deliverables: one page with three anchored parts (recommended, fewest links), or a small hub page plus three pages (4 pages, clearer separation, more links)?
3. "Book a 20-minute call": where does it go? A `mailto:` link is simplest; a form needs a service. No booking tool is in scope today.
4. Old URLs: leave them to 404, or keep tiny redirect files for the 6 removed pages (no visible links, so graders with an old link still land in the right place)?
5. Pricing logic: is a disclosure on the home page enough, or does the pricing work need its own page? Depends on how long the pricing teammate's reasoning is.

Not verified at this stop: Velvetyne fonts (site down); Culture Amp's gallery listing; Inkwell's live site (only the case study was read); the Bricolage width axis (only weight checked); exact file sizes after any further subsetting.

## Final (phase 1b, at the type and IA stop)

### Files written with commit SHAs (branch d1-design)
- 075a21a `docs/design/references.md`, `docs/design/log.md`, `docs/design/index.md`
- 8628ee0 `design-lab/type.html`, `design-lab/fonts/shortlist/` (Newsreader roman and italic, Bricolage Grotesque, Apfel Grotezk Regular, Mittel and Fett, three OFL licence files), `design-lab/shots/type-{light,dark}-{1280,375}.png`
- Phase 1a files and SHAs: see the first Final section above and `docs/handoffs/design_report.md`.

### Key insights and findings
- Every HR vendor page viewed leads with proof Sphyr lacks (logos, badges, customer counts, AI). Sources: lattice.com, cultureamp.com, leapsome.com, viewed 2026-11-24.
- Inkwell's site faced the same constraint (no client names) and answered it with a storyboarded scroll story. Source: Awwwards case study, 25 Jun 2025.
- The Fontshare ITF Free Font License forbids distribution through a repository or publicly accessible servers and forbids modification. Source: fontshare.com/licenses/itf-ffl, v2.0, read 2026-11-24.
- Newsreader, Bricolage Grotesque and Apfel Grotezk are all SIL OFL 1.1 with no Reserved Font Name (licence files in the repo).

### Decisions and why
- All shortlisted fonts are OFL, so no licence question remains for the public repo.
- Manrope stays as the text face in two of three pairings and in all product frames, to keep the site and product in one sans.
- IA cut to 3 pages and a 3-link nav because the user found the old site confusing; the Deliverables link stays visible on phones for the grader.

### Rejected approaches and why
- Fontshare closed-source fonts: licence fails the public repo test.
- Leapsome and Master People Platform as references: AI and badge-led, or generic stock look.
- A hub page plus three deliverable pages: more pages and links than needed (kept as an alternative question).

### Open questions
1. Type pick (1, 2 or 3).
2. Deliverables as one anchored page or hub plus three pages.
3. Destination of "Book a 20-minute call".
4. Redirect files for removed URLs.
5. Pricing logic on the home page or its own page.

### Not verified
- Velvetyne fonts (site down), Culture Amp gallery listing, Inkwell live site, Bricolage width axis.
- The link counts are planned, not measured on built pages.

## IA update after user answers (2026-11-24)
Merged iteration-a (now at 5efef9f on d1-design; decision "Site structure", 0f097bf). Six pages, minimal links:

| Page | File | Links on the page (nav 3 + content + footer) |
|---|---|---|
| Home | `index.html` (folds old home, how-it-works, trust, pricing) | nav 3; content 4 (walkthrough in hero, section 2 and close; "Book a 20-minute call" note); footer 3. About 10 |
| The 2-minute walkthrough | `demo.html` | nav 3; content 2 (book-a-call note, back to home); footer 3. About 8 |
| Deliverables hub | `deliverables.html` | nav 3; content 3 (one card per deliverable); footer 3. About 9 |
| Propaganda strategy | `propaganda.html` | nav 3; content 2 (walkthrough, back to deliverables); footer 3. About 8 |
| Three LinkedIn posts | `linkedin.html` | same, about 8 |
| Advertisement | `ad.html` (the event standee and handout card) | same, about 8 |

- Nav on every page: logo (home), "See the 2-minute walkthrough" button, "Deliverables", theme toggle. Visible on phones.
- Footer shrinks to 3 links: walkthrough, deliverables, "Book a 20-minute call", plus the course credit line. The three deliverable pages are reached through the hub only, which keeps every page's link count low.
- "Book a 20-minute call" opens a small note in place: "Course project: in a live launch this books a 20-minute call with our team." No email address. Built with native `<details>` or a `popover` element, so no extra page and no link.
- Old URLs dropped without redirects.
- Wording fix in home section 2: clients are invited by the consultant, by email, from My Sphyr, with the partner's agreement. Not "when the partner adds them".
- Flag for the lead: `docs/strategy/message_guideline.md` line 176 (section 10, Do column) still says "Clients can add their view when the partner invites them." Line 67 now says the consultant sends the invite. One of the two should change; I follow line 67.

## Progress 1b, step 3 (ribbon motif)
Success number at this stop: 0 WCAG AA failures in 116 contrast checks (58 token pairs x 2 themes) after the warm palette, `node design-lab/contrast.mjs`. Homepage copy check not run yet (no homepage copy).

Commits since the type stop: 730e1f4 (font licence rename only; the `git add` for the rest aborted on a stale path), 9382682 (warm palette, prototype frame palette, Newsreader display files; completes 730e1f4), cc86d0e (ribbon motif), 0d1882c (all lab screenshots retaken in the warm palette, motif shots), 52ad4c7 (ribbon_motif.md, design_system.md phase 1b addendum), a73aa16 (merge of iteration-a with final pricing), a3779b2 (references addendum).

### Warm palette and Newsreader (user decisions)
- Light page #FAF8F4, cards #FFFEFB, text #1F1C18, muted #625C54. Dark page #171513, cards #201D1A, text #F2EEE7, muted #B3AB9F. Greens unchanged for actions and positive states; orange only as surface or icon. Lowest text pair: 4.83 (prototype muted text on prototype sunk surface, inside frames); lowest site text pair: link on sunk surface 4.84 light.
- Inside faux UI frames the prototype's own cool palette stays (`--p-*` tokens), on a warm well, so each frame reads as the real product screen.
- Newsreader for `h1` and `h2`, Manrope for everything else. Files: static optical-size-72 instances, 23 KB roman 500 plus 23 KB italic 400 (279 KB for the variable pair). Only the roman is preloaded; the italic loads only when a display line uses `<em>` (checked: it stayed "unloaded" on a page without one).
- Screenshots of the new palette: `design-lab/shots/components-light-1280.png` and `components-dark-1280.png` (also faux-ui, type, motif, at 1280 and 375).
- Recorded in `docs/design/design_system.md`, dated addendum "2026-11-24 (phase 1b)".

### Ribbon motif (step 3)
`design-lab/motif.html` with the palette switch; doc `docs/design/ribbon_motif.md`.
- Core visual: four engagements (April to March), three strands each, each engagement fades to a dashed outline while its strands stay in one record line that becomes the sphere at April. Plays once on load (about 7 s), "Play again" button, finished picture under reduced motion. A separate vertical composition below 600px (`motif-cool-*-375.png`).
- Circle: 14 strands (the 2018 pilot's average circle of 14), four groups, all turning the same way like the logo's ribbons; group buttons; draws in with `animation-timeline: view()` (Baseline 2026, newly available, MDN) or once in view via IntersectionObserver.
- Logo variants from one recolourable symbol `assets/sphyr-mark.svg` (15 ribbons, artefacts removed): full colour (large uses), mono following the theme (nav, footer, favicon), white on fixed print green #007652 (standee, green fields), strand colours (end of the core visual). Checked at 120, 28 and 16 px in both themes.
- Both strand palettes are in place for the user to compare: cool logo colours (`motif-cool-{light,dark}-1280.png`) and tonal green (`motif-tonal-{light,dark}-1280.png`). Neither uses orange or red.
- Size: motif.css 7.9 KB, motif.js 3.3 KB, sphyr-mark.svg 13.7 KB (9.4 KB gzipped together) plus about 9 KB inline SVG.
- Fixed during review: strands that doubled back, end-cap dots on undrawn strands, labels showing before their engagement, an invalid XML comment that broke the sprite, the hover parting being blocked by the intro animation, white-on-green failing in dark, the circle reading as four helices.

### Extra references (lead's research step)
`docs/design/references.md` addendum: 11 sites opened, 10 assessed (Awwwards Sites of the Day 31 Oct to 24 Nov 2026, one nominee, three product sites). New picks: Granola (serif headline left, real product right; replaces Culture Amp), Two26 Studio (one warm manifesto paragraph with a few accent words; replaces Make HR Work), MECHA (air and hairlines instead of boxes), Stripe Press (deliverables hub as an index), Bulletproof (a three-item nav is enough). Kept: Inkwell, Lattice. Homepage plan changes: hero with the core visual full width below the headline, sections parted by air, vision as one large paragraph, deliverables hub as an index.

### Noted for the homepage step (not started)
- Pricing is merged (a73aa16); I will use `docs/pricing/pricing_summary.md` wording.
- untemplated skill: only its anti-template rules and its checks (first-screen words, 0 frames in a 2 s idle window, changed share per interaction, contrast, 390 px overflow, reduced motion); no dither, no font change, frames and price block may be boxed, motif plays once then rests.
- Known gap: `components.html` still shows the old four-link nav; the canonical three-item nav and footer come with the homepage step.
- Flag from before: message guideline line 176 still says "when the partner invites them".

### Open questions at this stop
1. Strand palette: cool logo colours or tonal green? (My lean: cool; it carries the "fun" brief, tonal reads corporate.)
2. Anything in the warm palette or Newsreader setting to change before I build the homepage?

## Final (phase 1b, at the motif stop)

### Files written with commit SHAs (branch d1-design)
- 075a21a, a3779b2 `docs/design/references.md` (plus log and index)
- 8628ee0 `design-lab/type.html`, `design-lab/fonts/shortlist/`
- 730e1f4, 9382682 `design-lab/tokens.css`, `contrast.mjs`, `faux-ui.css`, `components.html`, `faux-ui.html`, `fonts/newsreader-display-*.woff2`, `fonts/OFL-newsreader.txt`, `fonts/OFL-manrope.txt`
- cc86d0e `design-lab/motif.css`, `motif.html`, `motif.js`, `assets/sphyr-mark.svg`
- 0d1882c `design-lab/shots/` (components, faux-ui, type at 1280 and 375 both themes; motif cool and tonal at 1280 both themes, cool at 375 both themes)
- 52ad4c7 `docs/design/ribbon_motif.md`, `docs/design/design_system.md` addendum

### Key insights and findings
- ITF Free Font License forbids repository distribution and modification (fontshare.com/licenses/itf-ffl, v2.0, read 2026-11-24).
- `animation-timeline` is Baseline 2026, newly available since October 2026 (MDN, read 2026-11-24).
- Selectors do not reach into `<use>` copies but custom properties do, so one SVG symbol can carry every logo variant.
- Google's static optical-size instances cut Newsreader from 279 KB to 46 KB for the two styles used.
- Recent Awwwards studio winners favour tiny navs (1 to 5 links) and one confident type or colour idea.

### Decisions and why
- Prototype palette kept inside frames, warm palette outside, per the user; frames stay true to the product.
- Strands never orange or red (product status colours).
- Core visual has a separate phone composition (stageshow rule: compact is a redesign).
- Granola and Two26 replace Culture Amp and Make HR Work as closer fits for warm, editorial, typographic.

### Rejected approaches and why
- Scaling the wide core visual down on phones: labels become about 5 px.
- Variable Newsreader files: 279 KB for two styles.
- Circle as four clusters on the axes: read as helices, not a circle.
- Scroll-linked text colour reveal (Two26): busy motion, against the untemplated rule.

### Open questions
1. Strand palette pick.
2. Palette or type adjustments before the homepage.
3. Message guideline line 176 wording.

### Not verified
- Strand colours in dark theme by contrast script (decorative; checked by eye).
- Safari and Firefox rendering of `light-dark()`, the inlined mark and the circle fallback (Chromium only).
- Unanim Studio (did not render), Delta Cafés and Preymaker (listed, not opened).
- Optical size of the Google static instances checked by look only, not by inspecting the font tables.

## Gate 1b report: homepage mockup (2026-11-24)

Success number: 0 unreviewed never-say hits in 234 visible strings on `design-lab/home.html` (`python3 design-lab/copy_scan.py design-lab/home.html`; 10 reviewed strings are denials, the no-refund term, a cited fact, "review" as an engagement type or competitor category, and prototype microcopy and sample dates).

### Copy (humanizer, by hand, then counted)
Applied the humanizer rules by hand while rewriting every visible string; the skill's file pass was not run. Only "The engagement ends. The evidence stays." is verbatim. Counts from `design-lab/copy_tells.py`, confirmed by eye, product frames excluded:
- "X, not Y" contrasts: 2 before, 1 after (section 3 headline).
- Triads as rhythm: 5 before, 0 after.
- "April": 18 before, 0 after. The promotion moment appears twice in public copy ("Promotion round" in the hero visual, "At promotion time" in the section 3 headline), three times if the scorecard's "by calibration" counts. Message guideline section 5 says "at most once per piece"; your note said once or twice on the page. Flagging the gap.
- No line announces that there are no customers (removed per your correction; guideline line 82 and 177).
- Fixed after review: the trust paragraph now says feedback in the record comes only from colleagues' cards and Sphyr logs no hours or screen activity (the prototype does track responsibilities and OKRs, so the earlier "only" claim was too broad); the exit-cost qualifier now says the ₹8.6 lakh is our estimate and nobody has measured whether Sphyr prevents exits; "the rate is the same for every employee and every firm size".

### Untemplated checks (method: Playwright MCP Chromium, no touch emulation or device scale; 8 profile runs, reduced motion first; the 15 px scrollbar guard held in all 8)
- Sideways scroll on phone: 0. Smallest phone text: 11 px.
- First-screen words: 50 at 1440 desktop, 37 at 390 phone (target 25; nav, core line, sentence and button are 33; the rest are the core visual's labels).
- Idle: 0 requestAnimationFrame frames in every run; running CSS animations 0 under reduced motion; with motion, 34 during the one-time intro at 2 s, 0 at 8.5 s.
- Changed share (1440 by 900, light): sphere hover 0.49%, circle group 1.13%, price disclosure 4.42%, call note 0.49% (text and border pixels only; about 5% by area), feedback answer 4.94% in 3 of 3 runs with the card fully in view (an earlier run with the card partly out of view measured 8.54%; it sits at the 5% limit because the card swaps its step like the product). Time to rest after the sphere hover: 160 ms.
- Boxed at rest: only faux UI frames and the two pilot and price blocks.
- Contrast: 0 failures in 201 desktop and 177 phone text nodes, both themes. Token script: 116 checks, 0 failures.
- Modes: right first frame for system light and dark, stored choice wins, toggling back to the system value clears it, a later system change keeps a stored choice.
- Fonts and hosts: Manrope and Newsreader with licence files; 0 foreign hosts; 0 page console errors. (The MCP tool's "200 errors" counter came from my own check script's broken listener, not from the page.)

### Facts for the gate
- Scorecard: `docs/strategy/acquisition_engagement.md` line 56 still marks the measured items "to be confirmed with the pricing and first-use work". The home page presents them as final.
- Prototype sample dates (May 05 to Jun 30 on the chart axis, Jul 22 and Jul 25 on comments) remain inside product frames. Decide whether the no-month rule covers them.
- Links to `demo.html`, `deliverables.html` and `index.html` are dead inside `design-lab/` until the site build.
- `components.html` and the other lab pages still use lab navs; the canonical nav lives in `design-lab/snippets/nav.html` and `home.html`.

## Final (handoff)

### Where everything is
Branch `d1-design` in worktree `Product-Marketing-final-assignment.d1-design`, last merged `iteration-a` at 823f235. Nothing pushed. Serve with `python3 -m http.server` from the worktree root and open `/design-lab/home.html`.

Phase 1b commits, oldest first: 075a21a and a3779b2 (references), 8628ee0 (type shortlist), 730e1f4 and 9382682 (warm palette, prototype frame palette, Newsreader files), cc86d0e (ribbon motif), 0d1882c (lab shots), 52ad4c7 (motif doc, design system addendum), 13fdd16 (motif: cool strands, engagement types, circle plays once), bdca406 (home, snippets, copy scanners), fddd3b1 (homepage doc), 85ee6b9 (home shots), e264573 (wording and accessibility fixes, moon icon), 7fd314d (slop rules and nav addenda), c7c0b2a (final shots). Phase 1a SHAs are in `docs/handoffs/design_report.md`.

Files:
- Docs (`docs/design/`): `design_system.md` (1a system plus two dated 1b addenda: warm palette and type, canonical nav and toggle), `slop_rules.md` (plus 1b page and copy rules addendum), `faux_ui.md`, `ribbon_motif.md`, `references.md`, `homepage.md` (section map, copy sources, checks), `index.md`, `log.md`.
- Lab (`design-lab/`): `tokens.css`, `components.css`, `faux-ui.css`, `motif.css`, `home.css`, `theme.js`, `motif.js`, `home.html`, `components.html`, `faux-ui.html`, `motif.html`, `type.html`, `snippets/{head,nav,footer,theme-toggle}.html`, `assets/` (logo, `sphyr-mark.svg`, `icons.svg`, Lucide licence), `fonts/` (Manrope, Newsreader display 500 and italic 400, OFL files; `fonts/shortlist/` is record only), checks `contrast.mjs`, `copy_scan.py`, `copy_tells.py`, screenshots in `shots/` (home, components, faux-ui, type, motif; light and dark; 1280 and 375).

### User decisions (all recorded in docs)
- Warm neutrals: light #FAF8F4 page, #1F1C18 text; dark #171513 page, #F2EEE7 text. Product greens for actions and positive states; orange only as surface or icon. Prototype's own cool palette only inside product frames.
- Type: Newsreader for `h1` and `h2` (static optical-size-72 files, 23 KB each), Manrope for everything else and inside frames.
- Strands: cool logo colours (teal, cerulean, royal blue, navy, green, olive, plum, orchid); no orange or red. Tonal green removed from the code, noted in the doc.
- No dithering anywhere; no font change; untemplated skill used only for its anti-template rules and checks.
- No month names in public copy; promotion moment named sparingly.
- Never claim customers and never announce their absence; proof built in the open (scorecard, 2018 paper pilot labelled exactly).
- Humanize every visible string; only the core line verbatim; at most one "X, not Y" per page; no triads, staged openers, closers or bold labels.
- IA: six pages (`index.html` home folding how-it-works, trust and pricing; `demo.html` walkthrough; `deliverables.html` hub; `propaganda.html`, `linkedin.html`, `ad.html`). Nav: logo, Deliverables, theme switch, walkthrough button; Deliverables visible on phones. Old URLs dropped without redirects.
- "Book a 20-minute call" opens the note "Course project: in a live launch this books a 20-minute call with our team." No email address.
- Pricing exactly as `docs/pricing/pricing_summary.md`; packaging steps from `docs/packaging/packaging_summary.md`.

### Known gaps
- Scorecard items still "to be confirmed" in strategy; shown as final on the page.
- Prototype sample dates inside product frames (no-month rule question).
- First screen 50 words at desktop (target 25).
- Feedback answer change sits at the 5% limit (4.94%).
- Promotion moment appears 2 to 3 times; guideline says once per piece.
- Checks ran in Chromium only (no Safari or Firefox), without touch emulation; no screen reader test.
- Strand colours in dark theme checked by eye only.

### Next steps for the site build (phase 2, after gate 1b)
1. Merge `d1-design` into `iteration-a`; on a new branch, copy `design-lab/tokens.css`, `components.css`, `faux-ui.css`, `motif.css`, `home.css` into `site/style.css` (one file or several, keep the order) and `theme.js` plus `motif.js` into `site/main.js` or beside it; copy `assets/` and `fonts/` (with the OFL files) into `site/`.
2. Build `site/index.html` from `design-lab/home.html`, fixing asset paths; then `demo.html` (keep the walkthrough interaction, restyle with the components), `deliverables.html` as an index (title in the display serif, one line, link), and `propaganda.html`, `linkedin.html`, `ad.html` from the strategy and ad work. Every page starts with `snippets/head.html`, uses `snippets/nav.html` (add `aria-current="page"`), ends with `snippets/footer.html` and the `#call-note` popover.
3. Delete the old pages `how-it-works.html`, `pricing.html`, `trust.html`; update the README links.
4. Fix the calculator bug and mobile overflow noted in `docs/site_audit/technical_notes.md` if the walkthrough keeps them.
5. Before each page ships: `python3 design-lab/copy_scan.py <page>`, `python3 design-lab/copy_tells.py <page>`, `node design-lab/contrast.mjs`, the toggle test and the untemplated checks as in `docs/design/homepage.md`; screenshots in both themes at 1280 and 375.
6. Settle the gaps above at gate 1b first (scorecard status, frame dates, promotion-moment count).
