---
type: Handoff
title: "Other pages polish report"
description: "Design-review fixes on demo, LinkedIn, ad, propaganda and hub: v2 captions, one link style, calmer standee, clean line breaks, hub sections on the title column, call in the phone menu."
tags: [handoff, ppages]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T15:50:00Z }
---

# Other pages polish report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Skills loaded before any markup: `design-taste-frontend` and `stageshow`.

## Plan

Approved in the brief; going on without waiting. Hard scope: items 1 to 7 of the brief only.

1. Captions. `site/demo.html` (two figures) and `site/linkedin.html` (post 2 frame): replace `figcaption.exhibit-cap` ("Exhibit N.", rule, Source line) with the index caption `<figcaption><span class="sample-label"><svg icon i-info/>View, role: line. Prototype screen. Sample data, fictional people.</span></figcaption>`. Demo figures go back to `class="figure"` as in v2 (`.figure:has(> .stage)` in base.css keeps the container query). The bold `wt-yours` note stays, styled as v2 (flex row in the caption). `site/css/demo.css` follows.
2. Demo step 4: `.wt-end` aligns to start, CTA stacked under the text as v2 did; balance the paragraph so "a time." is not alone. Step 1: the checked radio dot is green (`accent-color` already set; fix whatever greys it).
3. Linkedin "Next: the advertisement" becomes `.go` with the arrow, like the walkthrough link above it. Ad already has only `.go`; check only.
4. Ad standee: remove `.pr-pilot` from the standee only. Printed URLs (standee, card front, card back): `<wbr>` after each "/", and the hyphenated part held in `.nw` so no line starts or ends inside it.
5. Propaganda timeline "Book a 20-minute call": U+2011 in "20‑minute" in that step label only.
6. Deliverables: the two new sections indent to the title column on desktop (72 px number column plus gap, the hub grid); the `.after` term column widens so "Every two weeks after that" stays on one line.
7. Phone Menu item: waits for `## Menu markup` in `reports/phome.md` (not there yet).

Checks: copy_scan and copy_tells on every changed page, links, no sideways scroll at 375, screenshots 1280 light and dark plus 375 of each changed spot, compared with v2.

Open question for the lead: `reports/phome.md` does not exist yet, so item 7 has no markup. Please send the Menu markup or point me at it.

## Progress (items 1 to 6 done)

- 34fcafc Demo: icon captions (figures back to `class="figure"` as v2; `.figure:has(> .stage)` keeps the container query), step 4 is one column at the text measure with the call under the text, checked radio drawn green. Root cause of the grey dot: demo.js disables the radios after Submit and a disabled native radio greys out; the radio is now drawn with `appearance: none`.
- 05a54f2 LinkedIn: icon caption in the post 2 frame; "Next: the advertisement" is `.go` with the arrow, gap matched to the walkthrough link.
- 4cd8105 Ad: pilot line removed from the standee only (card front and the page close keep it); unused `.standee .pr-pilot` rule deleted. The three printed URLs have `<wbr>` after each slash and the hyphenated part in `.nw`, so they break only after a slash. Measured: the held part stays inside its card at 1280 and 375.
- c10ee46 Propaganda: U+2011 in the timeline's "Book a 20-minute call"; it now breaks "Book a / 20-minute call".
- 81c6a52 Deliverables: the two sections start at x 200 like the index titles on desktop (measured: 200, 200, 200 at 1280); term column 13rem, "Every two weeks after that" on one line.
- Ad item 3: the ad page has only one secondary link (`.go`), so no change was needed.
- Checks: no sideways scroll on any of the five pages at 1280 and 375. copy_scan and copy_tells hits are all strings this change did not touch. No new visible copy was written (only removals and the existing caption pattern), so the humanizer pass had nothing new to check.

Waiting on item 7: `reports/phome.md` has no `## Menu markup` section yet (only `## Plan`).

## Final

Result: 7 of 7 brief items done on branch `d1-ppages` (6 commits). No sideways scroll on any of the five pages at 1280 and 375 (5 pages x 3 settings measured).

Files written, with commits:
- 34fcafc `site/demo.html`, `site/css/demo.css`: icon captions, step 4 call under the text, green checked radio.
- 05a54f2 `site/linkedin.html`, `site/css/posts.css`: icon caption, both text links as `.go` with arrow (gap tightened; re-checked at 1280 and 375).
- 4cd8105 `site/ad.html`, `site/css/ad.css`: standee without pilot line, URLs break only after "/".
- c10ee46 `site/propaganda.html`: U+2011 in the timeline's "20-minute".
- 81c6a52 `site/css/deliverables.css`: new sections on the title column (x 200), term column 13rem.
- 333b2e6 all five pages: last `#nav-menu` item `<li><button type="button" popovertarget="call-note">Book a 20-minute call</button></li>`, markup exactly as the lead sent it. It opens `#call-note` on all five pages at 375 (checked by clicking).

Key decisions and why:
- Demo figures went back to `class="figure"` (v2), not `exhibit` plus a plain figcaption: base.css `.figure figcaption` and `.figure:has(> .stage)` already give the caption spacing and the container query for the stacked Insights columns.
- Checked radio: the root cause was `demo.js` disabling the radios after Submit (a disabled native radio greys out). Drawing the radio with `appearance: none` fixes it without changing the lock behaviour.
- Step 4: stacked under the text (v2 option), one column at `--measure`; this also removed the "a time." widow.
- Printed URL: `<wbr>` alone would still let the browser break at the hyphens, so the hyphenated segment sits in the existing `.print .nw` (nowrap). Measured inside its card at 1280 and 375.
- Deliverables: indented to the title column (72px plus `--s-5`, the hub grid) on desktop only; on phones the hub is one column, so there is one edge already.

Approaches rejected:
- U+2011 inside the printed URL: a copied URL would contain a non-ASCII hyphen.
- Top-aligning the step 4 CTA beside the text: needs a magic offset tied to the H2 height.
- Re-enabling the radios in `demo.js`: the lock is intended behaviour; only its look was wrong.

Open questions: none.

Not verified:
- The Menu item with phome's styling: base.css styling lives on phome's branch, so here the button shows browser-default style. Look again after phome merges.
- 1280 dark and light screenshots of the Menu: it is a phone-only control, so only 375 was taken.
- Humanizer pass: no new visible copy was written (removals and the existing caption pattern only).
- copy_scan and copy_tells hits on these pages are all strings this change did not touch; not reworded (out of scope).

Screenshots (`.swarm/tmp/ppages/`): `demo_step1_*`, `demo_step2cap_*`, `demo_step3_*`, `demo_step4_*`, `li_media_*`, `li_next_*`, `ad_show_*`, `prop_flow_*`, `deliv_edge_*`, `deliv_after_*` (each at 1280l, 1280d, 375l), `menu_demo_375l.png`, `menu_callnote_demo_375l.png`.

## Not done (out of scope)
- Dropped v2 parts noted in the design review (ad links to the LinkedIn posts and to all deliverables, the demo's "Back to home" button): not in my brief.
- The call popover position (review item): not in my brief.

Browser closed. Idle.
