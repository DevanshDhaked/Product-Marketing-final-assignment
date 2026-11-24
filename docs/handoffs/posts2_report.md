---
type: Handoff
title: "LinkedIn posts rewrite report"
description: "The three LinkedIn posts rewritten to about 110 to 130 words each, story-led, without disclaimers or citation chains; old and new text in full."
tags: [handoff, posts2]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T23:21:06Z }
---

# LinkedIn posts rewrite report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Branch `d1-posts2` (base `0c79de9`, iteration-a). Only `site/linkedin.html` changed: post bodies only. Hashtags (post 1), first-comment text and URLs, the post 2 product screen and media line, the notes beside each post, and the rest of the page are unchanged.

Old text below is from the branch base `0c79de9`. The older posts on `main` were used only as a voice reference (per the lead's mid-task note), not as the "old" version.

## Words per post

| Post | Before | After |
|---|---|---|
| 1 | 149 | 113 |
| 2 | 261 | 129 |
| 3 | 241 | 106 |

Counted on the post body without the "…more" label and hashtags. Target range: the lead's note (80 to 140) replaced the brief's 60 to 120.

## Posts, old and new in full

Post 1 keeps its hashtags: #Consulting #TalentManagement #PeopleDevelopment. Posts 2 and 3 have none (page total stays at three).
First comments, unchanged: post 2 "The 2-minute walkthrough: devanshdhaked.github.io/Product-Marketing-final-assignment/v2/demo.html"; post 3 "Book a 20-minute call" (popover button). Post 1 has no comment.

### Post 1 old

A partner asks you for "the file" on a senior consultant they never staffed. What do you send?

Usually it is the consultant's self-appraisal and one form from an engagement manager who has since moved to another client. The people who saw the consultant's best work were on an engagement that closed months ago, and they are spread across other engagements now.

Nobody did anything wrong here. When an engagement closes, the team scatters, and what they saw goes with them. So the partner reads the file and then rings the one engagement manager they know. That call ends up counting for more than anything written down.

We think those people should be asked while the team is still together, and our next post shows how.

Heads of talent, when a partner asks for the file, what goes in it? And who do you call to fill the gaps?

#Consulting #TalentManagement #PeopleDevelopment

### Post 1 new

Ananya built the pricing model on a retail engagement and ran the client workshop when the engagement manager fell ill. At promotion time, the file on Ananya had two pages.

One was their self-appraisal. The other was a form from that engagement manager, who had since moved to another client and mostly remembered the last few weeks.

The four people who watched that workshop were on other engagements by then, and nobody asked them. So the partner rang the one manager they knew well, and Ananya's promotion waited another year.

Heads of talent, when a partner asks for the file, what is in it? And who do you call to fill the gaps?

#Consulting #TalentManagement #PeopleDevelopment

### Post 2 old

In two large data sets, more than half of the variation in performance ratings came from who did the rating. In consulting, that person may have seen one engagement out of four.

The study is Scullen, Mount and Goff, 2000. Idiosyncratic rater effects (the particular way each rater tends to rate) explained 62% and 53% of rating variance in the two data sets. The actual performance of the person rated explained 21% and 25%.

So a single rating tells a partner quite a lot about the rater. Asking more of the people who saw the work, while they still remember it, gets you closer to the work itself.

That is how Sphyr works. Every two weeks, each person gets a short card for each colleague they worked with, asking how the work together went that fortnight. They tap one of the answers on the card below and add a tag or two, plus a note if they want one. In a 2018 paper-and-pen pilot run by Sphyr's founder, the cards took a little over two minutes (02:09) for an average circle of 14 people.

Ratings are pooled and comments are anonymized to the person rated. Over the year each consultant builds up a record from the people who saw the work, and partners bring it to calibration, where they still make the decision. Two minutes every two weeks is a lot less work than chasing appraisal forms from people who have already moved on.

You can try a card yourself in the 2-minute walkthrough. The link is in the first comment.

### Post 2 new

In 1906, 787 people at a country fair guessed the weight of an ox.

Many of them were far off. Francis Galton took the middle guess of all 787, and it came within 9 lb of the real weight of 1,198 lb (Galton, Nature, 1907).

A consultant is often judged on one guess, from the manager on the last engagement. A single rating like that tells you more about the person who gave it than about the consultant.

Sphyr asks everyone who worked with the consultant. Every two weeks, each person gets a short card for each colleague, and it takes about two minutes. Ratings are pooled, and names are not shown with comments.

Try a card yourself in the 2-minute walkthrough. The link is in the first comment.

### Post 3 old

The firm and our team agree in writing how a Sphyr pilot will be judged before it starts. This is what every pilot measures.

How many people take part in each cycle.

How many different people give feedback to each consultant.

Whether partners found something new in the records, and whether it changed any discussion.

Whether consultants found their own record useful, and whether they want to keep going.

The firm agrees the target for each one before the first cycle opens. Results stay with your firm unless you agree to share them.

We publish this because a firm trying something new should know the test before it signs anything. The method itself was tried before the software existed, in a 2018 paper-and-pen pilot run by Sphyr's founder in four companies. Those results were self-reported, so the one figure we use from it is time: cards took a little over two minutes for an average circle of 14.

A pilot runs for 12 weeks, which is six fortnightly cycles, with up to 40 people. It costs ₹25,000 plus GST, and that amount comes off the first annual bill if the firm signs. If it does not sign, the firm gets its data as a CSV file and we delete the rest.

If you would like to run one with a single practice before your next promotion round, book a 20-minute call with our team. The link is in the first comment.

### Post 3 new

Before a firm signs anything with us, we agree in writing how the pilot will be judged.

We look at whether people keep taking part each cycle, and whether partners and consultants find something in the records they did not already know. The firm sets the target for each one and keeps the results.

A pilot runs for 12 weeks with one practice of up to 40 people. It costs ₹25,000 plus GST, credited to the first annual bill if the firm goes ahead.

If your next promotion round is coming up, book a 20-minute call with our team. The link is in the first comment.

## Checks (smoke only)

- `design-lab/copy_scan.py site/linkedin.html`: 141 strings checked, 0 unreviewed hits, 1 reviewed denial (pre-existing).
- `design-lab/copy_tells.py site/linkedin.html`: 0 contrast sentences; 2 possible triads, both confirmed by eye as not triads ("whether people keep taking part each cycle, and whether partners and consultants..." is two items; the footer team names are a list of people).
- No em dashes, en dashes or emojis in the file.
- Links: 8 of 8 same-origin links return OK at http://127.0.0.1:8838/linkedin.html (hrefs unchanged).
- 375 px: scrollWidth 360 = clientWidth 360, no sideways scroll (rechecked on the final text).
- 1280 light, full page: `.playwright-mcp/linkedin-1280-light-v2.jpg` in the worktree, looked at. Shorter posts leave no layout gaps; no CSS change needed.
- humanizer pass done on each post, then read aloud and cut.

## Final

### Files written, with commit SHAs
- `site/linkedin.html`: `9441e36` (rewrite all three posts), `baa338d` (post 1: name the engagement manager once).
- This report.

### Key insights and findings
- Galton figures in post 2 checked: "Vox Populi", Nature 75, 450-451, 7 March 1907, https://doi.org/10.1038/075450a0 (accessed 2026-11-25 via exa search). 787 usable guesses at the 1906 West of England Fat Stock and Poultry Exhibition; median 1,207 lb; dressed weight 1,198 lb, so the middle guess was 9 lb out. The old `main` post cited "Nature, 1906", which is the fair year, not the publication year.
- "A single rating tells you more about the person who gave it than about the consultant" rests on Scullen, Mount and Goff (2000): rater effects 62% and 53% of variance vs ratee performance 21% and 25%. Stated in plain words, no citation, as the brief asked.
- The two minutes per card figure is the pilot's 02:09 per circle, said only as "about two minutes".

### Decisions and why
- Followed the lead's voice note over the brief where they differ: post 2 carries one short bracket citation "(Galton, Nature, 1907)"; post 1 is a story about one named consultant (Ananya, "they"/"their") with specific actions and an outcome.
- Post 2 uses the Galton ox story as the hook and the one research story; the rater point is stated plainly as the bridge to Sphyr.
- Post 3 names two measures in one sentence (participation each cycle; whether partners and consultants find something new in the records). Dropped the "how many different people rate each consultant" measure to avoid a list.
- Price appears once with "credited to the first annual bill"; CSV export and deletion terms cut.
- Privacy: "Ratings are pooled, and names are not shown with comments." No "anonymous" claim.
- "A consultant is often judged" instead of "Most firms judge" to avoid an unbacked majority claim.

### Approaches rejected and why
- First rewrite (60 to 120 words, plain recognition post with no story, Scullen as the post 2 fact): superseded by the lead's voice note asking for story hooks.
- Carrying over from `main`: emojis, arrows, more than 3 hashtags, anonymity claims, refund, price lock, the Rs 15,000 pilot, founder/engineer framing, "Illustrative" note, "not X, it's Y" lines. All left out.

### Open questions
- Post 1's Ananya story is a scenario with no "illustrative" label (the lead said not to carry that note). It never says Ananya is a Sphyr user, but a reader could take it as a real case. Lead to confirm this is acceptable.
- Post 2 has a story fact (Galton) plus a plain rater claim (Scullen, uncited). The brief allowed "at most one plain research fact"; I count Galton as the one fact and the rater line as the post's point. Lead to confirm.

### Not verified
- Scullen et al. figures were taken from the existing page text, not re-checked against the paper.
- Dark theme not screenshotted (brief asked for light only).

### Not done (out of scope)
- Nothing else on the page or other pages touched. The post notes ("Show the evidence for asking more people") still describe post 2 accurately; not edited.
