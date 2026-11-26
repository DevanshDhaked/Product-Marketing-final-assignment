---
type: Handoff
title: "Ad restored to the v2 design report"
description: "Standee and A6 cards back on the v2 design with the ribbon and logo sphere, carrying the v3 headline, first line, QR to /v3/ and sign-off."
tags: [handoff, rad]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T14:50:00Z }
---

# Ad restored to the v2 design report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan

Files: `site/ad.html`, `site/css/ad.css` only.

Base: v2 files from 729e109. `base.css` changes since v2 are additive (new `--ink`, `.report`, `.exhibit`, `.pilot-line`, `.keynums`), and `motif.css` is unchanged, so the v2 ad.css plus motif.css bring the v2 look back without touching shared files.

Page order (unchanged from v2):
1. Intro: h1 and lede (same in v2 and v3).
2. Show well: standee left, A6 front and back right.
   - Standee, top to bottom: brand, v3 headline (first read), ribbon (v2 compact composition, still), v3 strapline under the ribbon as its caption line, then the foot: v3 first line, QR (45 by 45 image) with the printed /v3/ address, v3 pilot line.
   - A6 front: brand, v3 headline, v3 first line, QR plus /v3/ address, pilot line.
   - A6 back: v3 body text, setup line, price line, QR with the label "Book a 20-minute call or see the 2-minute walkthrough" and /v3/ address, small print.
3. Why this ad: v3 rows (Medium, Audience, Why this headline, Journey stage, Why it tracks nobody).
4. Close: v3 (call button, pilot line, walkthrough link).

Nav: v3 (call button). og tags: /v3/. Dropped from v3: the product exhibit on the standee (the brief keeps v2's ribbon instead).

Ribbon words: "3 teammates" becomes "3 people"; the aria-label drops "teammates" and "record".

Sizing: the v3 headline is about twice as long as the v2 one. Fix inside v2's system by lowering the headline cqw size and the QR width, checked by screenshots; the ribbon keeps `flex: 1 1 0` so it takes what is left.

Open questions: none blocking. Strapline placement (under the ribbon) is my call; noted under decisions. (Changed during the build: the strapline went last instead; see Final.)

## Work log

- Loaded `design-taste-frontend` and `stageshow` before markup, and read `docs/design/slop_rules.md`. Design read: a redesign that keeps the v2 look as it was. No new faux UI was added (the v3 exhibit was removed), so stageshow had nothing to apply beyond that.
- Rebuilt `site/ad.html` from the v3 file. The standee block now uses v2's structure (sd-top, ribbon SVG `cv-compact sd-cv`, sd-foot) with the v3 words. `motif.css` is linked again. The A6 headline and line use v2 classes (no `--ink` colour). Build script: `swarm/tmp/rad/build.py`.
- `site/css/ad.css`: v2 rules, plus the v3 pilot and strapline rules and the v3 A6 sizes. Standee type is set smaller than in v2 (headline 9.2cqw instead of 11.5, line 4.1cqw, QR 22cqw, ribbon margin 3cqw).
- Measured the ribbon height at 1280: v2 is 394px. With v2 sizes and v3 words it was 271px, and the box labels could not be read. After the size changes it is 316px (about 80% of v2). At 375 it is 286px. No `.pr-in` overflows at 1280 or 375 (scrollHeight minus clientHeight is 0 on all three pieces).
- Fixed a specificity problem: `.print p { margin: 0 }` (0,1,1) beat `.a6-head` margins. That bug was also in v2. The selectors are now `.print .a6-head` and `.standee .pr-pilot`.
- Wrapped "2-minute" in `<span class="nw">` on the standee and A6 first lines, because "2-" broke at the hyphen at line end.
- Smoke checks:
  - copy_scan: 88 strings, 0 unreviewed hits.
  - copy_tells: 1 contrast (the strapline, the page's one allowed "X, not Y") and 2 possible triads (two lists, not rhythm). This matches the v3 baseline exactly.
  - All local href/src targets and the index anchors (#how, #partners, #pricing) resolve.
  - No sideways scroll at 375.
- Leftover-string scan: zero hits for "Take the 2-minute walkthrough", "/v2/", the old QR alt text, "pooled", "teammates", "record" and "evidence". All 3 QR images keep 45 by 45 and the alt "opens the Sphyr home page".
- Humanizer: the 2 new strings ("3 people" and the ribbon aria-label) have no tells. Every other visible string is v3 text, unchanged.

## Final

Files written:
- `site/ad.html` and `site/css/ad.css`, commit 3e8c64b on `d1-rad`.

Key decisions:
- v2 base with v3 words. `base.css` changes since v2 only add rules, so the v2 look comes back without touching shared files.
- Standee order: brand, headline, ribbon, first line, QR with the /v3/ address, pilot line, strapline. The strapline is last, as in v3, so the "Why this headline" row ("the Sphyr name sits above it, the line under it says what Sphyr is") still matches the layout.
- The headline is the largest type and is read first. Its size is cut from 11.5 to 9.2cqw so the 74-character headline sits on 4 lines and the ribbon keeps about 80% of its v2 height.
- No cta-line next to the standee or A6-front QR, following v3: the first line already says "Scan to book a 20-minute call or see the 2-minute walkthrough". The QR label appears on the A6 back only, as the brief asks.
- The A6 sizes come from v3, because they were tuned for these words. The colours are v2's.

Approaches rejected:
- Keeping v2's 11.5cqw headline and 27cqw QR: the ribbon fell to 271px and its labels could not be read.
- Placing the strapline under the ribbon: it would push the first line away from the headline and make the rationale row wrong.

Open questions:
- The ribbon box labels ("Project 1 / 3 people") are about 8px on screen, versus about 9.5px in v2. To make them larger, either a text line has to go (not allowed by the brief) or the headline has to shrink further.

Not verified:
- Real print or scan of the QR. No WCAG or contrast checks (per the user's rule).

v2 comparison at 375: the ribbon is 286px against v2's 353px (81%). This is the same ratio as at 1280 (316 against 394), so the phone standee needs no size step of its own.

Screenshots (`swarm/tmp/rad/`). The close shots were taken with the nav set to static, so it does not cover the pieces.
- `rad_1280_light.png`, `rad_1280_dark.png`, `rad_375_light.png`
- `rad_show_1280.png` and `v2_show_1280.png` (side by side)
- `rad_1280_standee.png` (standee close shot)
- `rad_1280_a6.png` (A6 front and back)
- `rad_375_standee.png` and `v2_375_standee.png` (side by side)

Not done (out of scope): none.
