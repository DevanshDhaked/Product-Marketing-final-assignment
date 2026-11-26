---
type: Handoff
title: "AIDA stage labels report"
description: "Journey stage rows removed from the LinkedIn and ad notes; the propaganda campaign flow and channel table carry the AIDA stage once, in the professor's four words."
tags: [handoff, stage3]
generated: { by: claude-code/opus-5-5, at: 2026-11-27T01:10:00Z }
---

# AIDA stage labels report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Final

Success number: 3 of 3 pages changed and committed, 0 new copy_scan hits.

Branch check before each commit: `git branch --show-current` printed `d1-stage3` (3 times).

### Files and commits
- 315ce1b `site/linkedin.html`: removed the "Journey stage" row from all 3 post notes. Job and Call to action unchanged.
- 02fce34 `site/ad.html`, `design-lab/copy_scan.py`: removed the "Journey stage" row from "Why this ad". It held the only body link to the LinkedIn posts, so one sentence moved to the end of the Medium row: "The standee runs in the same weeks as the first LinkedIn post." (link on "first LinkedIn post"). The Medium row is an exact-match allowlist entry in copy_scan.py (reviewed "endorse" denial), so the entry was updated to the new extracted text; without that the scan reported 1 unreviewed hit.
- 1bee2f0 `site/propaganda.html`: in the campaign flow (#response), each step gets one stage word in its own `<span class="flow-job">` above the existing job line. Post 1 and standee = Attention; post 2 = Interest; walkthrough = Interest; post 3 = Decision; call = Action; pilot = Action. No new class, CSS or colour.

### Key decisions
- Stage word in `.flow-job`, not `.flow-when`: `.flow-when` is absolute and nowrap in a 52 px band above the line, and "From week 3, Interest" would nearly fill a 137 px column at 1280 and overflow narrower. A separate span also avoids "Action: Up to 40 people..." on the pilot step.
- Ad link sentence in Medium, not "Why it tracks nobody" (adjacent, but a timing sentence reads oddly there) and not "Why this headline" (frozen by brief).

### Open question for the lead
- The channel table on propaganda.html (#tactics) has a "Stage" column with journey-map words: Naming the problem, Looking for answers, Seeking validation (source: journey_map.md). It is per channel, not per flow step, so I left it. Conflict: the "Sphyr's LinkedIn page" row says "Naming the problem" while it carries all 3 posts, which the flow now labels Attention, Interest and Decision. Options: leave it (two vocabularies, journey vs AIDA), or rename the column/values. Not changed: hard scope.

### Checks
- copy_scan: linkedin 1 unreviewed hit (pre-existing on HEAD, social proof line in post 1, not touched); ad 0; propaganda 0.
- copy_tells: possible triads and contrasts listed are all in unchanged text.
- humanizer on the new strings: no tells.
- Links: only new/kept link is `linkedin.html` (exists). Flow anchors unchanged.
- Sideways scroll at 375: scrollWidth 375 on all 3 pages.
- Dark mode set via `data-theme="dark"` on html.

### Screenshots (looked at each)
In `swarm/tmp/stage3/`: before_flow_1280, prop_flow_1280_light, prop_flow_1280_dark, prop_flow_375, ad_why_1280_light, ad_why_1280_dark, ad_medium_375, li_note1_1280_light, li_note3_1280_dark, li_note2_375 (all .png).

### Not verified
- Dark at 375 (not required). LinkedIn note 2 at 1280 light/dark (notes 1 and 3 shown; same markup).
- Visual note: stage word and job share one muted caption style, so they read as two equal lines. Brief asked for existing style; a stronger stage label would need a CSS change.

### Approaches rejected
- Prefixing the job ("Attention: name the problem"): awkward on the pilot price line.
- Editing the channel table Stage column: outside brief, needs mappings the brief did not give.

Browser closed. Idle.

### Addendum 2026-11-27: channel table Stage column (lead request)

Branch check: `git branch --show-current` printed `d1-stage3` before the commit.

- e820a56 `site/propaganda.html` (#tactics): the Stage column now uses the flow's words. The heading "Stage" is unchanged. This closes the open question above.
  - Sphyr's LinkedIn page: Attention, Interest, Decision (one post each). Lead's string.
  - Standee at an HR event: Attention. Lead's mapping.
  - Warm introductions: Interest. It carries the walkthrough, which the flow labels Interest.
  - Articles in HR media: Attention. It carries the rater research, which names the problem for a cold reader (was "Naming the problem").
  - Our website: Interest. A reader who looks Sphyr up is weighing it (was "Looking for answers").
  - HR community meets: Decision. Peers vouching is the validation step before a firm decides (was "Seeking validation").
  - The table has no call or pilot rows, so Action appears only in the flow.
- Checks: copy_scan 0 unreviewed hits. copy_tells flags nothing in the new cells. No sideways scroll at 375 (scrollWidth 375).
- Screenshots, both looked at: `prop_chan_1280_light.png`, `prop_chan_375.png` in `swarm/tmp/stage3/`.
- Visual note: at 1280 the LinkedIn cell wraps as "...Decision (one / post each)". It reads fine. Keeping "(one post each)" together would need a CSS or nbsp change, which was not made.

Browser closed. Idle.
