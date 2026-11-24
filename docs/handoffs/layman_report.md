---
type: Handoff
title: "Layman clarity test report"
description: "A first-time visitor's read of the home page: what Sphyr is, jargon, doubts, scores and three fixes."
tags: [handoff, layman]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T21:42:03Z }
---

# Layman clarity test report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Persona: busy head of talent, 150-person Indian consulting firm, never heard of Sphyr. Only the browser view was used. No repo files read.

Tool note: the Playwright MCP browser was locked by another session ("Browser is already in use"). I used the Playwright library from the local npx cache with a separate headless Chrome instead. Same engine, same page, no server started. Screenshots saved under the main repo root `.playwright-mcp/` with the prefix `layman_`.

## Step 1: first screen at 1280x800 (before scrolling)

Screenshot: `.playwright-mcp/layman_desktop_first.png` (taken about 1.5 s after load, so the line animation was mid-play).

What I see: headline "The engagement ends. The evidence stays." A side line: "Sphyr asks each engagement team about your consultants and keeps every answer." One green button "See the 2-minute walkthrough". Below, two boxes "Project 1, 3 teammates" and "Project 2, 3 teammates" with three coloured lines running to the right. A "Play again" button and the note "Illustration. The projects are examples." Nav: How it works, For partners, Pricing, Deliverables.

- What I think Sphyr is: a tool that collects feedback on each of my consultants from the people they worked with on each project, and stores it, so it is still there later. My guess: it is for performance reviews.
- Who it is for: consulting firms. Probably HR or talent leads, maybe partners. The word "your consultants" tells me it is talking to the firm, so me.
- What it would change for me: when a project ends, the feedback does not get lost. At review time I would have it in one place. This is a guess. The first screen does not say "performance review" or "appraisal" in plain words.
- What it costs: not shown. There is a "Pricing" link in the nav.

First-screen reactions:
- "The engagement ends. The evidence stays." is catchy but I had to read the side line to know what "evidence" means. Evidence of what? Sounds legal at first.
- The line drawing does not tell me anything on its own. The three lines leave the project boxes and go off to the right. I did not see where they end in the first second. The "Promotion round / The whole year is in the file" label exists on the page but was not yet visible in my capture, so a fast reader may miss the payoff.
- Two identical "See the 2-minute walkthrough" buttons on one screen (nav and hero). A "Book a 20-minute call" option only appears much lower, in pricing. Fine for a first look.

After the animation settled (6 s, `layman_desktop_first_settled.png`): four project boxes, twelve lines that join and wrap into a ball on the right, labelled "Promotion round, The whole year is in the file". That label is in very light grey and is the faintest text on the screen, yet it is the payoff of the picture. Once I saw it, the picture made sense: feedback from four projects ends up in one file at promotion time.

## Step 2: whole page at 1280x800, one scroll

Screenshots: `layman_desktop_s01.png` to `layman_desktop_s11.png` (one per 800 px), `layman_desktop_full.png`.

My one sentence: Sphyr sends every consultant a two-minute feedback card about each colleague every two weeks during a project, and keeps the pooled answers so partners have the whole year in front of them at promotion time.

How it works, as I understood it:
1. At kickoff, I (head of talent) give Sphyr our firm's values. They become the tags on every card.
2. People come in from a spreadsheet. Sphyr sits beside our HR system, it does not replace it.
3. The managing partner sends a note. Each consultant picks a circle of close colleagues (engagement manager and team; a client lead can be added from the second cycle, with the partner's OK).
4. Every two weeks, each person gets one card per colleague: pick how it went (Was good / Could improve / No interaction), tick tags that stood out, optional note. About two minutes for the whole set.
5. Answers are pooled. The person rated sees comments without names.
6. Consultants see a trend of how their work is landing. Engagement managers see a team view during the project. I see who took part, team by team.
7. At the promotion round, partners have the whole year's record. The decision stays with partners.
8. Price: Rs 149 per employee per month, billed yearly, plus GST. A 12-week pilot for up to 40 people is Rs 25,000, credited if we sign.

Words or phrases I did not understand or had to guess:
- "evidence" (hero headline). Evidence of what? I guessed "feedback record" only after reading the side line.
- "Engagement team VBAs" (sample card chip). No idea what VBA means. I guessed Values, Behaviors, Attitudes from the group labels below it.
- "normalized" ("Private by design: Individual responses are normalized and grouped", and "A normalized, anonymized view" on the consultant screen). Statistics word. I do not know what is done to the answers.
- "pooled" ("Ratings are pooled", pricing list). Guessed: averaged together.
- "cycle" / "feedback cycles" (dashboards, timeline, FAQ). Guessed: one two-week round. Never said in plain words next to the first use.
- "Composite score across all seven dimensions" (consultant screen). What seven dimensions? The card shows three ratings and nine tags, not seven of anything.
- "Strongest signal", "Mixed signals this cycle" (consultant screen). Dashboard talk. "Mixed signals" sits next to a +3 rise and an "Improving" badge, which confused me.
- "Edit requests, 3, Awaiting your decision" and "decide feedback edit requests" (manager screen). Who asks to edit feedback, and why does a manager approve it? Not explained in the visible text (I did not open the FAQ answers).
- "02:09" (stats row). Reads like a clock time. I had to read the line below to know it means 2 minutes 9 seconds.
- "62% and 53% of the differences in performance ratings came from who was doing the rating, in two large data sets" (stats row). I had to read it twice.
- "Deliverables" (top nav, footer). On a product site I expected a feature list. It is unclear what a buyer would find there.
- "For partners" (nav) vs the "For partners and engagement managers" section. Fine, but I did not know if it is a separate page.
- "circle" (Who gets a say). Guessable.
- Rating words change between screens: card says "Was good / Could improve / No interaction", the manager screen says "Positive / No interaction / Could improve". I had to assume "Was good" = "Positive".

What made me doubt it:
- "No AI writes or scores anything" (What Sphyr does not do), but the sample screens show "Overall score 78" and "Team score 82". So who or what makes the score? This is the question a partner would ask me first.
- The proof numbers are old or small: a 2018 paper-and-pen pilot in four companies, self-reported, from the founder's own whitepaper v0.3; a research paper from 2000. Nothing from a firm that used the product.
- "Edit requests" made me worry that feedback can be changed after it is written, which cuts against "keeps every answer".
- Who gets a say: text says the circle is the engagement manager and the team, with clients only from the second cycle, but the illustration counts 3 clients in an "average circle" of 14. Small, but I noticed.
- Pricing says "per employee". For a 150-person firm I would ask: do partners and support staff count, or only consultants who use it? The example (150 x 149 = 22,350) suggests everyone.
- The footer says it is a course project and Sphyr is not on sale. As a real buyer that ends it. As a reader of a course project it is honest and fine.

Where I would stop reading and why:
- I understood the product at "Today / With Sphyr" (screen 3). A busy reader could stop there.
- I would skim the two dashboard screens. They are dense with scores and terms (signal, dimensions, edit requests) that the page does not explain, so they raise questions instead of answering them.
- I would then jump to "What Sphyr costs". The pricing block is the clearest part of the page. I would stop after pricing; the "What happens after you sign" timeline is useful but long.

## Step 3: first screen at 375x800 (phone)

Screenshots: `layman_phone_first.png`, `layman_phone_first_settled.png`, `layman_phone_s01.png` to `layman_phone_s15.png`, `layman_phone_full.png`.

- What Sphyr is: same as desktop. The side line sits right under the headline, so I read it sooner than on desktop.
- Who it is for: same as desktop, consulting firms and their talent or HR lead.
- What it would change for me: same guess as desktop, feedback from each project is not lost by review time.
- What it costs: not shown on the first screen.
- Headline, side line and the green button all fit on the first screen.
- The project picture is stacked vertically. Lines run down off the bottom of the screen. The "Promotion round, The whole year is in the file" payoff is below the fold, so on a phone the first screen shows only four boxes and lines with no point.
- Header on phone shows "Deliverables" and "Menu" but no walkthrough button. Fine, the hero has one.
- Nothing looked broken. No sideways scroll: page width equals screen width at both 1280 and 375, and no element pokes past the edge. No console errors at either width.
- Cramped: the consultant "Overall trajectory" chart is very short on phone and the feedback popup covers most of it, so the line is barely visible (`layman_phone_s07.png`). The manager screen and pricing cards read fine.

## Step 4: scores

- First-screen clarity: 3 of 5. The side line tells me what Sphyr does, but the headline is abstract ("evidence"), and the picture's payoff is faint on desktop and off-screen on phone.
- Whole-page clarity: 4 of 5. The problem story, the "Today / With Sphyr" pair, the card and the pricing make it clear; the dashboard jargon and the "score" vs "No AI scores" clash cost one point.

## Step 5: three changes, smallest first

1. Make the "Promotion round, The whole year is in the file" label in the hero picture as dark as the other text, so the picture's point is readable at a glance.
2. Make "No AI writes or scores anything" and the scores on the sample screens ("Overall score 78", "Team score 82") agree. Today the page says nothing scores, then shows scores with no source. One line near either place would do; the team knows what the true wording is.
3. Replace or explain jargon on the sample screens and card: "VBAs", "normalized", "cycle" (say "every two weeks" once next to it), "seven dimensions", "signal", and use one set of rating words ("Was good" vs "Positive").

## Final

Findings:
- I could tell what Sphyr is from the first screen's side line within a few seconds: a tool that collects feedback on consultants from each project team and keeps it for promotion time. The headline alone does not say this.
- The hero picture's payoff label is faint on desktop and below the fold on phone.
- Jargon on the sample screens: VBAs, normalized, pooled, cycle, seven dimensions, strongest signal, mixed signals, edit requests, 02:09.
- Biggest doubt: "No AI writes or scores anything" next to screens showing "Overall score 78" and "Team score 82", with no word on how scores are made. Second: "Edit requests" is unexplained.
- Evidence is thin for a buyer: founder's 2018 self-reported pilot and a 2000 study.
- Pricing is the clearest section. Only open question is who counts as an "employee".
- Phone: no overflow, no console errors, nothing broken. Consultant trend chart is cramped and mostly covered by the feedback popup.

Scores: first screen 3 of 5, whole page 4 of 5.

Top 3 changes (smallest first):
1. Darken the "Promotion round" label in the hero picture.
2. Make "No AI writes or scores anything" agree with the scores shown on the sample screens.
3. Remove or explain jargon on the card and sample screens, and use one set of rating words.

What I did not check:
- Only the home page. I did not open the walkthrough, Deliverables, For partners or Pricing pages, or any FAQ / accordion answers (all were closed; I did not expand them).
- Did not click "Play again", the dark-mode toggle, the phone Menu, or "Book a 20-minute call".
- Used headless Chrome via the Playwright library, not the Playwright MCP browser (it was locked by another session). Animation timing may differ from a real browser.
- No accessibility, contrast measurement, or other screen sizes beyond 1280x800 and 375x800.
- I did not read any repo files, so I cannot say which claims on the page are intended or sourced.
