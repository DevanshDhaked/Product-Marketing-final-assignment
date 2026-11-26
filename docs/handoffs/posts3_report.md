---
type: Handoff
title: "v3 LinkedIn posts writer report"
description: "Three posts rewritten for doomscrolling consultants: short scene or number hooks, a save-worthy pilot check, one call, no hashtags."
tags: [handoff, posts3]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T13:30:00Z }
---

# v3 LinkedIn posts writer report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Branch `d1-posts3`, worktree `Product-Marketing-final-assignment.d1-posts3`. Owned files: `site/linkedin.html`, `site/css/posts.css`.

Success number: first lines under 60 characters with a scene or number in consulting words, 3 of 3 (now: 0 of 3; post 1 line one is 172 characters, post 2 is 66 characters about an ox, post 3 is 87). Draft first lines: 55, 55 and 41 characters. Second number: banned words on the page, 0 (now: "file" 2, "evidence" 1, "Member B" 1, "pooled" 0, plus the old tagline as the post 2 image line).

## Plan

### Files
- `site/linkedin.html`: nav, head tags, intro, three posts, notes, closing section.
- `site/css/posts.css`: only if the post 3 numbered list or the exhibit caption inside a post needs a rule (the `.li-body ol` spacing rule already exists). Expect 0 to 5 lines.

### Section order (job and AIDA stage)
1. Intro. Job: say what the page is. One line: three posts on the Sphyr company page, two weeks apart, for people who run appraisals at Indian consulting firms of 40 to 400 people.
2. Post 1, recognition. Stage: Attention. Text only, no link, no hashtags.
3. Post 2, how it works. Stage: Interest. Text plus one image (the feedback card as a captioned exhibit), walkthrough link in the first comment.
4. Post 3, the tool. Stage: Decision to Action. A four-check test for any HR pilot that a head of talent saves or forwards, then the offer; last line carries "Book a 20-minute call"; first comment holds the call button.
5. How the three work together. One short paragraph: the team reads every answer to post 1 before post 2 goes out; team members reshare each post in their own words (one or two sentences, never a bare reshare); the team replies to every comment within the first day; the standee ad runs at an HR event in the same weeks as post 1. Then the main button "Book a 20-minute call" with the pilot line under it (same string as home: "Start with a 12-week pilot for up to 40 people. ₹25,000 plus GST, taken off your first annual bill if you sign."), then "See the 2-minute walkthrough" as the one secondary link.

Notes beside each post stay one short line each for Job, Stage (AIDA name) and Call.

### Draft posts (to be humanized and cut after approval; word counts are body text)

Paragraph reading: line one is the first line of paragraph one, with a line break under it and no blank line, so each of posts 1 and 2 is four short paragraphs and line one still sits alone above the fold.

Post 1 (168 words). Third person by role, so it reads as a pattern, not a claimed case; "you" only in the closing question. No names.

> Four people saw the workshop. None were in calibration.
> A senior consultant built the pricing model on a retail project, then ran the client workshop the week the engagement manager was out sick. The client's CFO asked for the deck that night. Four people from the firm were in the room.
>
> Ten months later that project team has rolled off to three other clients. The engagement manager fills one feedback form from memory, and memory keeps the last few weeks. The consultant's self-review covers the rest, and partners read self-reviews with a discount.
>
> In calibration, the partner the consultant is staffed with now speaks for them, and that partner was not at the workshop. HR has one form for that project, and the room moves to the next name. Nobody calls the four. The designation waits another cycle, and so does the hike.
>
> Partners and heads of talent: before calibration, how do you reach the people who saw a consultant's best project, and what do you ask them?

Post 2 (162 words). Number hook in consulting words; Galton stays as the one story detail; Scullen, Mount and Goff (2000) as a plain number, uncited.

> Four projects this year. One manager writes the rating.
> That manager saw one of the four, usually the last one, and mostly its final weeks. In one study of two large sets of performance ratings, more than half of the spread came from who gave the rating, and about a fifth to a quarter came from the work itself.
>
> In 1906, 787 people at a country fair guessed the weight of an ox. Most were far off. Francis Galton lined up all 787 guesses, and the middle one came within 9 lb of the real 1,198 lb.
>
> Sphyr asks everyone on the project, every two weeks. Each person rates the colleagues they worked with in about two minutes. By calibration, the partner and the head of talent see grouped ratings from everyone on a consultant's projects across the year, with comments anonymized to the person rated.
>
> Rate one sample colleague yourself in the 2-minute walkthrough. The link is in the first comment.

Image under post 2: the feedback card, reworked to match home Exhibit 1 (Ananya Rao, Associate Consultant, the same sample chips), without "Member B", without the "Engagement team values" tag and without the old tagline line. Caption below in the home style: "Exhibit 1. Fortnightly Feedback, Member role: rating one colleague from the project." with source "Sphyr prototype screen. Sample data, fictional people." Private line uses the home's prototype copy: "Individual responses are normalized and grouped before anyone sees them."

Post 3 (140 words). A test the reader can use on any vendor, ours included. Number in line one.

> Four checks before you sign any HR pilot.
> Scope it like a client project, and write these down before anyone signs:
> 1. The line that means it failed, and who calls it.
> 2. Who still takes part after the second cycle. If people drop off, the tool is extra work.
> 3. One question for partners at the end: what did you learn about a consultant that you did not know? Ask for a name.
> 4. One question for consultants: would you keep doing this if HR stopped chasing you?
>
> We run our pilots on these four checks, with one practice of up to 40 people for 12 weeks. The firm sets each target before the first cycle and keeps the results.
>
> Book a 20-minute call to plan one before your next appraisal cycle. The link is in the first comment.

### Other changes in `site/linkedin.html`
- Nav: copied from `site/index.html`, which swaps the nav button to "Book a 20-minute call" (popover).
- Head: `og:url` and `og:image` to `/v3/`; description rewritten to match the intro.
- Post 2 first comment: the shown URL changes from `/v2/demo.html` to `/v3/demo.html` (href stays `demo.html`).
- Not verified so far: the Scullen, Mount and Goff figures (62% and 53% rater, 21% and 25% ratee) come from the old page text and posts2, not from the paper.
- Hashtags: none on the page (post 1 loses its three).
- No reaction counts (none today).

### Before markup
Load the `design-taste-frontend` and `stageshow` skills, obey `docs/design/slop_rules.md` where they disagree, and run every visible string through `humanizer:humanizer` before each commit.

### Checks after the build
copy_scan, copy_tells, links resolve, no sideways scroll at 375, screenshots at 1280 light and dark and at 375, all looked at. Read each post at 375 as a tired engagement manager; rewrite any line one I would scroll past.

### Open questions for the lead
1. Nav `aria-current`: copying the index nav exactly puts `aria-current="page"` on the brand link and removes it from "Deliverables". I propose to copy it exactly except that `aria-current="page"` stays on the "Deliverables" links (desktop and menu), as on the current page. Approve, or copy byte for byte?
2. Closing section links: the rule says the walkthrough is the only secondary link. Today the section also has "Next: the advertisement" and "All deliverables". I propose to keep "Next: the advertisement" as a plain text link (page navigation for the grader) and drop "All deliverables" (the nav already has it). Approve?
3. Post 2 as a 6 to 10 page document post (research rule 6, "lead to decide"): I propose no, one image only. Reason: the data is about company pages in general, not our segment, and it adds a carousel mock to build and check by the 27 Nov deadline.
4. Exhibit numbering: this page has one exhibit, so I number it "Exhibit 1" (numbering per page). Or should it continue from home?
5. Post 1 says "partners read self-reviews with a discount". It is an inference from the research (self-review is the consultant arguing their own case), not a quoted source. Keep, or cut to "Your self-review covers the rest."?
6. Hashtags: none on the page. Or keep up to two on post 1 (for example #Consulting #PerformanceReview)?

## Lead reply (2026-11-26)
Approved with changes: posts 2 and 3 must not start with "Four"; post 2 says "partners and engagement managers see" (Admin has no results view); the study line is one plain sentence; post 3 says "Our pilot is built on these four checks"; cut "partners read self-reviews with a discount". Q1 aria-current proposal approved, Q2 approved, Q3 one image, Q4 number per page, Q6 no hashtags.

## Build

Success number: first lines under 60 characters, scene or number, consulting words: 3 of 3 (was 0 of 3).
- Post 1: "Four people saw the workshop. None were in calibration." (55 characters), 161 words.
- Post 2: "One manager rates a year spent on four projects." (48), 150 words.
- Post 3: "12 weeks in, how will you know the pilot worked?" (48), 140 words.
Banned words on the page: 0 ("file", "evidence", "pooled", "Member B", old tagline all gone). Hashtags: 0. Reaction counts: 0.

Study sentence as shipped: "Research on performance ratings finds that more than half of a rating reflects who gave it, and a quarter or less reflects the work itself." I wrote "a quarter or less" in place of the lead's example "less than a quarter", because the source figures are 21% and 25% and 25% is not less than a quarter.

Humanizer pass (embedded mode) changed three lines: "memory keeps the last few weeks" to "it covers the last few weeks"; merged "Nobody calls the four." into the sentence before it (dramatic fragment); "in their own words, with a sentence or two of their own" to "with a sentence or two in their own words".

## Checks (smoke only)
- copy_scan: 158 strings, 1 hit, false positive: "self-review" matches the scanner's `\breviews?\b` social-proof pattern. "self-review" is a glossary term (consulting_firm_life.md section 5), so kept.
- copy_tells: 0 contrast sentences; 6 possible triads, all checked by eye: two-item phrases ("in the last line and the first comment", "with a sentence or two"), the post 2 detail chain ("one of the four, usually the last one, and mostly its final weeks"), and the footer team names (not mine). None is a rhythm triad.
- No em or en dashes in the file.
- Links: 5 of 5 same-origin URLs return 200 at http://localhost:8873/site/ (linkedin, index, deliverables, demo, ad).
- 375: scrollWidth 375 = clientWidth 375, no sideways scroll.
- Screenshots looked at: 1280 light and dark full page, 375 full page, 375 post 1 viewport. Read post 1 at 375 as a tired engagement manager: line one is a scene with "calibration" in it and sits alone above the body; I would stop.

## Final

### Files written, with commit SHAs
- `site/linkedin.html`, `site/css/posts.css`: `3d20220`.
- `site/linkedin.html`: `b2ecf4a` (post 2 hook, "members" removed), `86cb77c` (post 2 card tags: "Stakeholder-centric" to "Client handling", "Resolve dependencies sooner" to "Share updates sooner", visible text only; there were no value attributes).
- This report.

### Key decisions and why
- Post 1 is told in the third person by role (senior consultant, engagement manager, partner, HR), "you" only in the closing question. No names, so it reads as a pattern and not as a real case (brief; posts2 open question on Ananya).
- Line one sits as the first line of paragraph one with a `<br>`, so posts 1 and 2 are four paragraphs ("four paragraph post") and line one still stands alone above the fold.
- Post 2 image reuses the home Exhibit 1 card markup (Ananya Rao, Associate Consultant, same chips and the prototype privacy line), made `inert` with `role="img"`, radio name `p2-exp`, ids removed so they do not clash. Caption in the home exhibit style, numbered per page: "Exhibit 1. Fortnightly Feedback, Member role: rating one colleague from the project." The "Engagement team values" tag and the old tagline line are gone.
- Post 3 is a four-check test for any HR pilot, framed as scoping a client project, with no price. The first comment keeps the "Book a 20-minute call" popover.
- Notes are one line each, with the AIDA stage named (Attention, Interest, Decision).
- Closing section: one paragraph (reads every answer, replies within the first day, team members reshare in their own words, the standee ad runs in the same weeks), then "Book a 20-minute call" with the home pilot line under it, "See the 2-minute walkthrough" as the one secondary link, and "Next: the advertisement" as a plain page link. "All deliverables" dropped (lead approved).
- Nav copied from `site/index.html`, with `aria-current="page"` on Deliverables (desktop and menu) and not on the brand (lead approved).
- Head: description rewritten; `og:url` and `og:image` point at `/v3/`; the shown first-comment URL is `/v3/demo.html`.
- CSS: removed the now unused `.li-tags` and `.li-media-line` rules; added `.li-next-page` (one spacing rule).

### Approaches rejected and why
- Second-person post 1 ("Four people saw your workshop"): it switched who "you" was between the body and the question.
- "Scope an HR pilot like a client project." as post 3 line one: an instruction, not a scene or number. Moved into line two.
- All three hooks starting with "Four": the lead flagged it as a template pattern across a series.
- Document (carousel) version of post 2: the lead chose one image.
- "three other projects" in post 1 to dodge the copy_scan hit: the hit is a false positive and "clients" is the better detail.

### Open questions
- Should design-lab/copy_scan.py treat "self-review" as allowed? Not my file.
- Post 1 says "The client's CFO asked for the deck that night." This is an invented scene detail inside a composite. Fine for a role-based pattern, but flag if the lead wants every detail sourced.

### What I did not verify
- Scullen, Mount and Goff figures against the paper (taken from posts2 and the old page).
- That partners see results in the product: per the lead's note, the Manager role (engagement managers) sees Insights; partners appear only as decision makers. The line "partners and engagement managers see" follows the lead's wording.
- No dark screenshot at 375 (not required).

### Screenshots
`Product-Marketing-final-assignment.swarm/tmp/posts3/`: `linkedin-1280-light.jpg`, `linkedin-1280-dark.jpg`, `linkedin-375-light.jpg`, `linkedin-375-post1.jpg`.

## Not done (out of scope)
- At 375 the nav shows no "Book a 20-minute call" button (same nav as home, copied exactly); any change belongs to the home or base owner.
- The copy_scan false positive on "self-review" (design-lab, not my file).

## Addendum after review (2026-11-26)

Commit `b2ecf4a` (after `3d20220`):
- Post 2 line one is now "One manager writes the rating for four projects." (48 characters). "A year spent on four projects" was slow to read. To keep post 2 at or above 150 words, "Most were far off" became "Most of them were far off" (151 words now).
- Closing note: "Team members reshare" had the banned word "member". It is now "People on our team reshare each post with a sentence or two in their own words."

Full banned-word grep (file, record, evidence, pooled, member, subordinate, VBA, resources, teammates, moves on, anonymous) on `site/linkedin.html`:
- Visible hits: 1, "Member role" in the Exhibit 1 caption. This is allowed: it is the product's real role label, and home Exhibit 1 uses the same caption.
- Other hits: only `fx-vba` CSS class names, which no reader sees.

After the edit I reran copy_scan (same single "self-review" false positive), copy_tells (0 contrast sentences, the same 6 triad candidates, all fine by eye) and the word counts (161, 151, 140). Line ones are 55, 48 and 48 characters.

Phone read at 375, one viewport per post:
- Post 1: line one is a calibration scene. I would stop.
- Post 2: line one names the reader's own rating set-up. I would stop.
- Post 3: line one is a question for whoever buys or judges a pilot. A tired engagement manager might scroll past. A head of talent or partner, the buyer this post is for, would not. I kept it on purpose and flag it here.
- Screenshots: `linkedin-375-post2.jpg`, `linkedin-375-post3.jpg` in the same tmp folder.

Humanizer check of the intro lede, the meta description and the three notes: no tells found, nothing changed.

The ad page on this branch still says it runs "in the same weeks as the first LinkedIn post", which matches my closing note. The parallel ad teammate may change that line.

## Not done (out of scope), added
- Persistence: this report lives only in `.swarm/reports/`. For the lead:
  - copy it to `docs/handoffs/posts3_report.md` (as was done for posts2);
  - add a decision-log entry replacing "2026-11-25: LinkedIn posts rewritten". It should record: no hashtags; one image for post 2; exhibits numbered per page; no shared opening word across the three hooks; "partners and engagement managers see"; post 3 is the pilot check; posts 1 and 2 at about 150 to 220 words.
- Stale cross-references outside my files:
  - `site/propaganda.html:222` still labels Post 3 "Proof in the open" (now "a check to keep"). Post 1 "Name the problem" and Post 2 "Show how" still fit.
  - `docs/strategy/deliverable_map.md:38-51` describes post 3 as "the public pilot scorecard" against "nobody has used this", and post 2 as "mechanism and the evidence". Both are older framing.
  - `docs/site_audit/page_inventory.md:70-71` describes the pre-v2 posts (Galton hook, Rs 149 price). That is a historical audit, so probably leave it.
- `docs/design/slop_rules.md:122` uses the phrase "proof built in the open" as a rule. It is not a post reference, so no change needed.


Note: `site/index.html` on this branch still shows "Stakeholder-centric" and "Resolve dependencies sooner" in home Exhibit 1. That is not my file, so I left it for the home owner.
