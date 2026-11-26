---
type: Handoff
title: "LinkedIn stopping-power researcher report"
description: "Feed mechanics, why consultants and talent leaders engage, 13 real posts, what fails, and rules for the three posts."
tags: [handoff, linkedin3]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T09:56:00Z }
---

# LinkedIn stopping-power researcher report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan
1. Read context docs and current posts (site/linkedin.html, docs/handoffs/posts2_report.md).
2. Research Q1 feed mechanics (LinkedIn guidance, van der Blom 2025/2026 reports, practitioner data).
3. Q2 sharing motives (Berger STEPPS, NYT psychology of sharing).
4. Q3 at least 8 real high-engagement posts (exa, snippets, quoting articles).
5. Q4 what fails. Q5 rules and hook examples.
6. Write docs/research/linkedin_stopping_power.md, then Final.

## Progress
- 2026-11-26: context read (professor addendum, handoff s2-3, segment, personas, do_not_claim, current posts, posts2 report). Current posts: 113 / 129 / 106 words, company page, links in first comment.
- Q1 sources found: LinkedIn Engineering (dwell time 2020, next-gen feed 2026, profile relevance 2026); van der Blom Algorithm Insights 2026 Nov update via pettauer.net (800k posts, 8,000 pages; named person in line one 1.58x, own-words reshare 7.7x engagement, one link 0.86x); van der Blom posts (formats 2025-08, comments 2026-10); AuthoredUp (323k / 372k / 709k posts; first line under 40 chars +25% engagement vs over 200; 1,200 to 1,500 chars best vs author norm; under 400 chars 14% below); Ordinal (fold about 140 mobile, 210 desktop).
- Q2 sources: Berger (Penn Today 2013 Q&A), NYT Psychology of Sharing (2011, n=2,500), Edelman-LinkedIn 2024 (n=3,484) and 2025 (n=1,934).
- Q3: 10 posts with visible counts (exa crawl snapshots, one via firecrawl og:title). None from homegrown Indian consulting partners found; closest are Big 4 and Indian HR posts.
- Q4 sources: LinkedIn newsroom 2026-03 (engagement bait), LinkedIn "what to avoid" page, Social Media Today 2022, Originality.ai 2026 (n=5,000), LigoSocial 2026 (n=134,522), r/consulting threads.
- Tool note: firecrawl search returned empty or off-topic results 5 times (spam, unrelated sites) from about 30 minutes in; firecrawl scrape still works (including public LinkedIn post pages). Used exa for search after that.

## Not done (out of scope)
- No edits to `site/linkedin.html`; no final post text.
- Noticed: post 1 still uses "file" twice ("the file on Ananya", "asks for the file"), which the professor flagged. Listed in the note's v3 bullets, not changed.
- Noticed: post 2 first comment points to the /v2/ demo URL; will need /v3/ when deployed.

## Addendum: gap search, second pass (2026-11-26)
- Lead note: firecrawl restarted; try site: searches for Indian consulting partners and heads of talent, 15 minutes max.
- 9 `site:linkedin.com/posts` firecrawl searches. 1 returned results (US/global calibration posts). 8 returned empty with 0 credits, including every query with "India" or a firm name (Primus, Avalon, Praxis). One query with firm names returned spam (Facebook pages). Not retried further (stall rule).
- Added 1 post to the note as #13, off-segment: Alan Stein (ex-Google manager), calibration-room story, 26 reactions, 4 comments. Counts and text read live with firecrawl scrape.
- Gap unchanged: 0 posts from partners or heads of talent at homegrown Indian consulting firms. The note's counts against the brief (8 on role, 7 high engagement, 5 recent) are unchanged.

## Final

### Files written
- `docs/research/linkedin_stopping_power.md` (worktree iteration-b, new folder `docs/research/`), sections 1 to 5 plus `## What this means for v3`.
- This report.
- Scratch only: `.swarm/tmp/linkedin3/` (search dumps, extractor script).

### Key findings (with sources)
1. Mobile fold is about 140 characters (Ordinal 2026). First lines under 40 characters earn about 25% more engagement than over 200 (AuthoredUp, n=323,111). Current post 1 first line is 119 characters.
2. Length is not our problem: 1,200 to 1,500 characters (about 200 to 250 words) did best against each author's norm; under 400 characters 14% below (AuthoredUp, n=116,251). Our posts are about 650 to 800 characters.
3. Company page specifics (van der Blom Nov 2026 via pettauer.net; 800k posts, 8,000 pages): page reach 1.6% of followers; a named person in line one 1.58x; employee reshare in own words 7.7x engagement vs bare reshare; one external link 0.86x; 6 to 10 page documents 1.10x.
4. LinkedIn itself (Newsroom 2026-03-12; "what to avoid" page) demotes engagement bait ("comment to agree", "Like if you agree!", irrelevant hashtags). Feed ranks on dwell / skip (Engineering 2020) and interest history (Engineering 2026).
5. Sharing is self-presentation: Berger social currency ("look good, smart, and in-the-know"); NYT n=2,500: 68% share to define who they are, 94% weigh usefulness to the recipient.
6. AI-sounding posts: -21% engagement vs same author (LigoSocial, n=134,522). Consultants openly mock vapid thought leadership and firm-marketing reshares (r/consulting threads 2021, 2022, 2025).
7. Twelve real posts with counts (n=12), plus #13 (off-segment, added in the second pass). 8 are by the brief's roles; 7 of those are high engagement; 5 of those 7 are from the last two years. So the brief's target of 8 is not fully met (short by 1 on role, 3 on recency). 7 of 12 open with a scene, dialogue or number; 10 of 12 use the reader's working terms in the first two lines. Best comment rates end with a question answerable from experience. Strongest consulting example: "My manager told me to charge 6 hours yesterday." (PwC, 591 reactions, 58 comments). Only post from inside a real consulting firm: Dalberg associate partner, 375 reactions, 11 comments (2023).

### Decisions and why
- Treated practitioner/vendor datasets as patterns, not causes, and said so in the note; only LinkedIn Engineering/Newsroom are platform sources.
- Recommended keeping the first-comment link and measuring, because the evidence conflicts (van der Blom 2025 "avoid"; Nov 2026 page data says test; one agency claim of a 2026 penalty unverified).
- Hook examples avoid "file" and avoid inventing customers; post 1 hooks use roles or second person because Ananya is a fictional composite.
- Used exa after firecrawl search failed repeatedly (lead allowed fallback). Firecrawl scrape kept working.
- After advisor review: added 2 posts (Dalberg, Karanth), labelled off-role and unknown-role posts as pattern evidence only, recounted patterns against stated rules (first count of 8 of 10 was overstated), trimmed Berger claims to the fetched text (dropped "awe" and "sadness does not"), stated the Edelman 52% / 54% figures with their uncertainty, and added source URLs for GBG, the Kaushik summary page and the Edelman PDF.
- Added a caveat that the 1.58x named-person figure is about real staff, not fictional names.

### Approaches rejected and why
- Scraping LinkedIn search pages directly for more consulting posts: firecrawl search returned spam/unrelated results; exa crawl snapshots gave text plus counts more cheaply.
- Cross-author ranking by engagement: counts depend on follower size, so the table is for patterns only.
- Dacia DeRidder (451 reactions, 25 comments) and Kristina Tevzadze posts: role outside the brief, and the DeRidder scrape returned text from a different post on the page, so the hook could not be matched. Left out.
- Citing humblebrag research (Sezer, Gino, Norton 2018): not fetched this session, so left out rather than cited from memory.

### Open questions for the lead
1. Post 2 as a 6 to 10 page document post (the card, one question per page)? It changes the mock on `site/linkedin.html`.
2. Keep the named fictional "Ananya" (page data favours a named person in line one) or switch to a role? Same open question as posts2 report.
3. Raise posts 1 and 2 to about 150 to 220 words? The professor said "4 paragraph post"; data supports it if each added line is a detail.

### What I did not verify
- Van der Blom report itself (paid); figures are from Pettauer's summary and van der Blom's own posts.
- Engagement counts are exa crawl snapshots (date of crawl not shown); only Chandrasekaran was read live (firecrawl, og:title "50 likes, 25 comments").
- Socialinsider, RevBoss, DSMN8 format figures came from an exa-surfaced summary page, not opened.
- Scullen, Mount and Goff (2000) figures behind the post 2 hook example were not re-checked.
- Edelman 2024: which of 52% and 54% is decision makers vs C-level (garbled extract; PDF not opened).
- Roles of Harshad Ingle and Shikhar Raj (not shown on the pages read).
- No data found on line breaks or white space by themselves; the paragraph advice is practice.
- Ordinal's 140/210 character fold is a vendor claim; not measured on a device.
