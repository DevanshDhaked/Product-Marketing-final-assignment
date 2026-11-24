---
type: Handoff
title: "Short deliverable pages teammate report"
description: "Ad rationale cut to about 200 words, LinkedIn notes cut to one line each, standee logo spaced from the headline."
tags: [handoff, short]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T21:13:53Z }
---

# Short deliverable pages teammate report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Word counts before (tag-stripped, inside `<main>`)

Method: `re.sub(r'<[^>]+>', ' ', main)` then split on whitespace. Includes SVG text labels in mockups.

- `site/ad.html`: 510 total. The "Why this ad" rationale section alone: 315 (the 530 in the decision log was likely an older or whole-page count).
- `site/linkedin.html`: 1,186 total. Post mockups (the three `<article>` blocks, incl. mockup chrome): 798. Notes (`post-note` blocks): 234. Rest is the intro and "How the three work together".
- Dated template HTML comments: none found in either page (`grep "<!--"` is empty), so nothing to remove.

## Word counts after

- `site/ad.html`: rationale ("Why this ad") 315 to 202. Whole `<main>` 510 to 397.
- `site/linkedin.html`: whole `<main>` 1,186 to 991. Notes (`post-note` blocks) 234 to 117. Post `<article>` blocks unchanged (798).

## Checks
- copy_scan (iteration-a version): linkedin 0 unreviewed hits. ad has 3 hits: [endorsement] Medium row, and [surveillance] on "Why it tracks nobody" and its row. All three are denials, and the same 3 hits were there before my edit. Adding them to `ALLOWED` needs a change to the shared `design-lab/copy_scan.py`, so I ask the lead to do it.
- copy_tells: 0 contrast sentences on both pages. Possible triads are only the footer names and unchanged post text.
- Links resolve on both pages (relative href/src all exist).
- Sideways scroll at 375: none (scrollWidth equals clientWidth on both pages).
- Humanizer pass run on every changed string.
- Viewed by eye: ad light and dark at 1280 (full page and standee crop), ad light 375 (full page) and dark 375 (standee crop), linkedin light and dark 1280 (full page), linkedin light 375 in four native-size slices (note rows, li-bar, comment bubbles, button row all in line). The blank strip under the footer in the 375 full-page captures is a capture artifact: the footer bottom equals the document height (6,323 px).
- Meta and og descriptions on both pages still match the content. `deliverables.html` has no wording about the cut rows.
- Exact strings for `ALLOWED` in `design-lab/copy_scan.py` (ad.html, all denials):
  - `A roll-up standee on a paid sponsor spot, with A6 cards on a stand beside it for people to take. It is planned for an HR community event of the kind national HR network chapters run, and paying for the spot does not mean the organisers endorse Sphyr. Our class notes call advertising the push route where "money is involved", which is why the spot is a paid one.`
  - `Why it tracks nobody`
  - `Nobody's badge is scanned and nobody fills in a form. The QR code and the printed address open the same plain page with no tracking parameters, so a scan tells us nothing about who made it.`

## Final

### Files written, with commits (branch `d1-short`)
- `29271b7` Ad page: `site/ad.html`, `site/css/ad.css`, `design-lab/shots/site/ad-short-{light,dark}-1280.png`, `ad-short-light-375.png`, `ad-short-dark-375.png`.
- `0f83405` LinkedIn page: `site/linkedin.html`, `site/css/posts.css`, `design-lab/shots/site/linkedin-short-{light,dark}-1280.png`, `linkedin-short-light-375.png`.

### Key findings
- The decision log's "about 530" for the ad page matches the whole page (510), as its 1,170 for linkedin matches that whole page (1,186). The mockups, intro and buttons alone take about 195 words, so the whole page cannot reach 200 to 250. I applied the target to the "Why this ad" rationale: 202 words now.
- Lead's extra fix (standee logo spacing). Root cause: `.print p { margin: 0 }` (specificity 0,1,1) beat `.sd-head { margin-top: 10cqw }` (0,1,0), so the gap between the logo row and the headline was 0 px. Fix: selector `.print .sd-head` with `margin-top: var(--s-5)` (24 px). Measured 24 px at 1280 and 375; checked by eye in both themes at both widths.
- The same reset also cancels `.pr-url { margin-top: 1.5cqw }` and `.a6-head { margin-top: 2cqw }`. These were not asked for, so I left them alone. The A6 card still shows about 14 px between the logo and the headline from line height, and it looks fine.
- The three linkedin `<article>` blocks are byte-identical to HEAD before my edit (compared with `cmp` against a saved copy). The posts are word for word.
- Dated template comments: none in either page, and none on `iteration-a` either. Nothing to remove.

### Decisions and why
- ad.html: kept the `dl.rows` structure with 4 rows (Medium, Audience, Journey stage, Why it tracks nobody). Cut Message, Benefit, Visual and Call to action, because the standee and cards show all four. Placement and the endorsement disclaimer moved into Medium. Kept a shortened "money is involved" line, because it is what makes this a paid ad rather than word of mouth. Kept "walk on" once; the second "walk past" is cut. No CSS change for the cuts.
- linkedin.html: each note now has exactly Job, Journey stage and Call to action, one short line each. I dropped "Belief it shifts" and dropped "When it runs", since the mockup header shows "Week N". Stage names match `docs/strategy/journey_map.md` (Trigger, Looking for answers, Seeking validation). The lede no longer repeats "two weeks apart" or "each has its own job". "How the three work together" now keeps only facts the mockups do not show: the team reads replies before post 2, reshares, and the standee runs in the same weeks. Its button row stays.
- posts.css: `.post-note` is sticky on desktop (min-width 961px, top 65px nav + `--s-5`). The short note now stays beside its tall post while it scrolls, so the right column is no longer a dead gap. The 65 px is the measured nav height; base.css has no token for it.

### Rejected
- Cutting "How the three work together" entirely: the brief asks that the posts work together, and the buttons need a home.
- Fixing the `.print p` reset at its root in ad.css: it would also move `.pr-url` and `.a6-head`, which is outside the ask.

### Open questions
- Lead: allowlist the 3 ad denial strings in `copy_scan.py`, or accept them as reviewed.
- My base is 2 commits behind `iteration-a` (866aa99, 1934851). Neither commit touches my 4 files, so I expect no merge conflict.

### Not verified
- Sticky notes on tablet widths between 961 and 1100 px.
- Dark theme at 375 for linkedin (light only, as the brief asks). Ad dark 375 was checked because the lead asked for it.
