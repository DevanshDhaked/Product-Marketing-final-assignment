---
type: Handoff
title: "Other team's site assessor report"
description: "Team 01's Sphyr site for creative studios: first screen 8 of 9 against our 6, what they do better, where we are stronger, and a design verdict."
tags: [handoff, rival]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T10:07:00Z }
---

# Other team's site assessor report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan
1. Skim context: professor feedback addendum, v2_baseline section 1, slop_rules, segment and product docs.
2. Firecrawl their home page and every internal link.
3. Playwright screenshots: 1280 first screen, 1280 full page, 375 full page. Close browser.
4. Score first screen (what, who, next 0 to 3), AIDA map.
5. Compare with our v2 and v2_baseline. Write docs/research/rival_site.md.

## Progress
- 10:05Z Read context (professor addendum, v2_baseline, slop_rules, do_not_claim). Downloaded all 16 reachable pages of their site (home, how-it-works, pricing, guides + 4 guides, why-sphyr, trust, start-a-demo, under-development, ad-1, linkedin post-1..3) to tmp/rival/html and extracted text.
- Screenshots in tmp/rival: home_1280_first, home_1280_full (after scroll-through), home_1280_story, home_375_first, home_375_full, ad1_1280_full, post1_1280_full. Playwright closed.
- Note: the first full-page shots showed large blank zones. Scrolling the live page showed real content (reveal-on-scroll). Not a defect for a reader.
- Note: Playwright can only write inside the worktree; shots were saved to the gitignored .playwright-mcp/ and moved to tmp/rival. Playwright also left its own page-*.yml snapshots in .playwright-mcp/ (gitignored).
- 10:20Z Verified our side from site/ on iteration-b (privacy line index.html:299, no infinite animations, no reaction counts in linkedin.html). Read all 3 post PDFs and the ad PDF. Wrote docs/research/rival_site.md. Dash and emoji scan: clean.

## Not done (out of scope)
- Did not open our v2 live in a browser; our side comes from v2_baseline and site/ greps.
- Did not read their 4 guides in full (word counts only: 832 to 1,128 words each).
- Did not test their dark theme or the feedback-card interaction.

## Final

### Files written
- docs/research/rival_site.md (the note).
- This report.
- Scratch only: tmp/rival/ (html/, pdf/, screenshots, slices/, extract.py).

### Key findings
1. Their segment differs from ours: founders of 25+ person creative studios and agencies (home hero, https://sphyr-website-lilac.vercel.app/).
2. Home first screen scores 8 of 9 against our 6 of 9. They lose 1 on (b) for no country, the same bar the baseline used on us. The gap is that they name the buyer ("For founders"), the firm type and the size in frame.
3. Their ad scores 2 of 9 on the headline plus first line (ours 3 of 9), and about 6 of 9 as a whole ad. Its meme headline is a real Attention line, which the professor said ours lacks.
4. They put a risk line under every call to action: "One team, 90 days, no card, no automatic upgrade." It fits the course notes on D and I.
5. Their copy uses their segment's scenes and roles: motion designer, producer, client approval. Post 2 opens "The campaign shipped on Friday. The appraisal said, 'Delivered on time.'"
6. Their design is not sloppy: a coherent system that fits a creative buyer. It carries AI-landing tells (about 8 tracked uppercase kickers, bento cards, a 70s infinite marquee, about 7 "X, not Y" lines on home). It also has loose ends (11 placeholder pages, a demo form that is not connected, a truncated post author line).
7. We do better on fidelity to the product sources. Their trust page says "Nobody, not your manager and not HR, sees who wrote what" (do_not_claim 6, PROTO 3.7). Their pricing lists "Who should we promote?" as a feature (item 16). Their prototype collage uses demo names (item 17). All 3 post PDFs show invented reaction counts, and posts 2 and 3 share the same numbers. Our privacy FAQ at site/index.html:299 is accurate.

### Decisions and why
- Swapped the reader to their segment's founder when scoring. Scoring them as a consulting managing partner would test fit to our segment, not their site's clarity.
- Docked their (b) for no country, to match the baseline's bar on our v2.
- Scored the ad on the baseline frame first and the whole ad second, so the scores compare with ours.
- Called the blank zones in the full-page capture a capture artifact, after scrolling the live page showed the content.

### Approaches rejected and why
- Citing the 375 full-page capture: it started mid-page, so it is unreliable.
- Rows in "we do better" backed only by slop_rules: rules state intent, not what v2 does. Every row there has a site/ file:line or grep.
- Copying their lines into examples: the brief forbids it. The v3 bullets are patterns only.

### Open questions for the lead
- Should v3 name "Indian" in the hero to reach 3 on (b), or is firm type plus size enough?
- Our pilot terms for the risk line under each call to action: are length, team size and price settled?
- Should course artefacts (Deliverables, Ads, LinkedIn) leave the buyer's nav in v3? Both teams have this fault.

### What I did not verify
- Our v2 live render: not opened in a browser.
- Their dark theme, the interactive feedback card, the guides in full, and post 3 past its middle.
- Word counts are from extracted text, so nav and duplicate DOM nodes may inflate them slightly.
- Kicker and "X, not Y" counts are hand counts (n=1 auditor).
