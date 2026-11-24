---
type: Handoff
title: "Hub and propaganda teammate report, phase 2"
description: "The deliverables hub, the propaganda strategy page and the README rewrite: drafts, research, checks and open points."
tags: [handoff, hub]
generated: { by: claude-code/opus-5-5, at: 2026-11-25T04:30:00Z }
---

# Hub and propaganda teammate report, phase 2

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Branch `d1-hub`, worktree `Product-Marketing-final-assignment.d1-hub`, based on `iteration-a` at 910ca83. Nothing written in the repo yet.

## Plan

Status: waiting for approval. HTML waits until the lead says sitecss is merged; then `git merge iteration-a` and build.

### Files

| File | Purpose | Outline |
|---|---|---|
| `site/deliverables.html` | The hub, an index in the Stripe Press pattern (display-serif title, one line, a link; nothing boxed) | Title. One line: this website is deliverable 1, with links to home and the walkthrough. Three index entries (propaganda strategy, three LinkedIn posts, the advertisement), each with its job, its place in the journey and one link. Footer from the template |
| `site/propaganda.html` | Deliverable 2, graded 15 marks | 11 sections. The first seven use the brief's 4B items as headings, in the brief's order; then the four extras from the old page. Full text in the Draft below |
| `site/css/deliverables.css` | Page styles for the hub and the propaganda page; read-only for the posts teammate | Classes listed below; tokens from `base.css` only, no raw hex |
| `README.md` | Repo front page; an evaluator may read it, so it is treated as public copy and humanized | Live link, the six pages, strategy summary, repo layout, run and redeploy. Draft below |
| `docs/handoffs/` is the lead's. I add no docs folder unless the lead wants a `docs/site_build/hub.md` note; open question 8 |

### Propaganda page layout (slop rules: at least four section layouts, nothing boxed except tables)

1. Split head: title and a two-sentence summary on the left, a short section index on the right (the index collapses under the title below 900 px).
2. Document column (max 68 characters a line) for prose sections.
3. Labelled rows (`<dl>`) for audience roles, tactics and channels: a term on the left, the explanation on the right; one column on phones.
4. Plain tables with hairlines for the belief shift (today, after) and objections.
5. Wide figure for the campaign sequence: a horizontal week ruler (week 1 to week 22) with stage bands, a vertical list on phones. Static, no motion. Uses the ribbon strand colours from `motif.css` only if sitecss exposes them as tokens; otherwise hairlines and the accent green.
6. Sources list at the end with URLs and access date.

No product frames on this page. One "X, not Y" in the whole page (the approved vision line, quoted in the positioning section).

### `deliverables.css` classes (proposed, for the posts teammate too)

- `.doc`: document column, 68ch max, body type.
- `.doc-head`: split head (title plus summary, index beside it).
- `.doc-index`: in-page section index, a plain ordered list of anchors.
- `.rows`: labelled rows on a `<dl>`; `dt` in Manrope semibold, `dd` beside it; stacks under 900 px.
- `.plain-table` inside `.table-wrap`: hairline rows, no fill, tabular figures, horizontal scroll inside the wrap only (no page overflow at 390 px).
- `.seq`: the week ruler figure (ordered list of stages with `data-from` and `data-to` weeks set as CSS custom properties).
- `.label-note`: small muted line for honest labels ("Illustrative composite, not a real person").
- `.hub-index`: the hub entries (number, serif title, one line, link).
- `.sources`: numbered source list, small type, URLs wrap.

Question for the lead: do `linkedin.html` or `ad.html` need anything beyond these (post frames, the standee mock)? I assume those live in the posts teammate's own CSS.

### Checks I will run before reporting done

Port 8824. `copy_scan.py` and `copy_tells.py` on both pages (0 unreviewed hits, at most one contrast, 0 triads); `contrast.mjs` if I add colours (I plan none); sideways scroll 0 at 390 px; smallest text 11 px or more; 0 idle frames; reduced motion; both themes; screenshots at 1280 and 375 in both themes into `site/_shots/`; every relative link resolves.

### Open questions

1. The promotion moment "at most once per piece" (message guideline 5). The campaign sequence has to count back from calibration. I name it once ("week 22, when partners calibrate") and then use week numbers, but the belief, the objections and the positioning sections also need the word "calibration" a few times. Is the propaganda page exempt as a strategy document, or should I keep cutting? Current draft: "promotion round" 2, "calibrate/calibration" 7.
2. The one "X, not Y" goes to the quoted vision line. The other contrasts from the sources are rewritten. Agree?
3. Naming communities in the channel section. The message guideline allows naming communities "as places we take part in". To keep the ad's event unidentifiable, I wrote "HR peer communities and their chapter meets" and "consulting professional bodies" without names. Name National HRD Network and IMCI, or keep generic?
4. The "who else has tried it" objection. The persona doc's answer is "Nobody yet. Say so"; the 2026-11-25 decision bans announcing absence. I answer with the scorecard, the 2018 pilot and the walkthrough. Confirm.
5. Team and course byline (names, PD2.501, IIIT Hyderabad): does the template footer carry it, or should the hub show it?
6. The scorecard targets (3 to 5 paid pilots) are shown as "our estimate to test". OK on a public page?
7. Gallup gives no sample size on its page (article of 2017-09-25, updated 2026-08-21). I keep the figure with "global, sample size not stated". Or drop it?
8. Do you want a docs note for this work (for example `docs/site_build/` with its own `log.md`), or does the report plus your handoff copy suffice?

### Research done

- Scullen, Mount and Goff (2000): two data sets of managers, n = 2,350 and n = 2,142, each rated by 7 raters (2 bosses, 2 peers, 2 subordinates, self) on 3 dimensions. Idiosyncratic rater effects 62% and 53% of variance; ratee performance 21% and 25%. Source: https://peopleanalyst.com/ai/insights/ic-scullen-2000-idiosyncratic-rater-variance (accessed 2026-11-25; the docs cite 2026-11-24).
- Gallup: "only 29% of employees strongly agree that the performance reviews they receive are fair, and 26% strongly agree that they are accurate." No sample size, population or year on the page. https://www.gallup.com/workplace/236135/give-performance-reviews-actually-inspire-employees.aspx (accessed 2026-11-25).
- Dropped: the foundit 52% figure (sample size not reported).

### Stale source content I did not carry over

ETHRWorld (per-subscriber click tracking, admedium report), SHRM India's event (before the window), the old page's refund, price lock, "collusion dropped to 0%", "nobody sees who wrote what", "merit, not politics" and the "two-minute, anonymous, everyone" triad, the ₹15,000 six-week pilot, every month name in the persona and channel docs, and the dropped scorecard item.

## Draft

Public copy below had one humanizer pass at draft time. The shipped copy differs. It went through a second pass at build (commit e5bdf5c), plus the pronoun rule (0e33461) and the lead's answers. The committed pages are the source of truth, not this draft. Headings are the page's headings.

### A. deliverables.html

Title: Deliverables

Line under the title:
This website is deliverable 1. The [home page](index.html) and the [2-minute walkthrough](demo.html) present Sphyr to a head of talent, and the three pieces below carry the same message into other places.

Entries:

02. Propaganda strategy
How we plan to change what heads of talent and managing partners believe about the record a consultant leaves behind when an engagement ends. It is the reasoning behind every stage of the journey. Link: Read the strategy

03. Three LinkedIn posts
Posts for the Sphyr company page. The first helps a head of talent put a name to the problem, the second shows how the card works and points to the walkthrough, and the third sets out what a pilot is measured on before it starts. Link: Read the posts

04. The advertisement
A standee with matching handout cards, planned for an HR community event where heads of talent meet their peers. It reaches them early, when they are first putting the problem into words, and its QR code opens the walkthrough. Link: See the ad

(Note: the three-post sentence lists three real items, one per post. If copy_tells flags it I keep it and record the review.)

### B. propaganda.html

Title: Propaganda strategy

Summary (beside the index):
In our course, propaganda means communication that sets out to influence minds, and advertising is the route where money is spent. This strategy is about changing one belief held by heads of talent and managing partners at homegrown consulting firms, so that by the time they see Sphyr the problem it solves already feels real and fixable to them.

Index: 1 Audience · 2 The belief · 3 Message and reasoning · 4 Tactics and channels · 5 Why they fit · 6 Positioning · 7 Expected response · 8 Sequence · 9 The persona's influence · 10 Objections · 11 Our limits
(The middle dots are list separators in the mock only; on the page it is an ordered list.)

#### 1. The audience we want to influence

We are talking to homegrown, partner-led Indian management and strategy consulting firms of about 40 to 400 professionals. Inside each firm, four groups matter, and they need different things from us.

Labelled rows:
- The head of talent (champion). She feels the problem first, in project-end forms that never arrive and in exit interviews. She finds Sphyr, runs the pilot and takes the case to the partners. She needs words for the problem that partners will accept, and a small way to test it.
- The managing partner (buyer). He signs, and he chairs the calibration where partners argue about promotions. He needs to hear that partners keep the decision and that the test is small, paid and measured.
- Practice partners and engagement managers (they can veto). They fear losing discretion and gaining admin. They need to see that Sphyr adds to what they judge with and costs them two minutes a fortnight.
- Consultants (the people rated). Their trust decides whether anyone fills in a card in a 60-hour client week. They need a two-minute task and a record of their own that they can read.

Label: Kavya, Vikram and Meera below are illustrative composites built from research on the segment. They are not real people, customers or interviews.

We wrote the plan around one person. Kavya is head of talent at a 150-person firm with three offices, four practices and eleven partners. Every year a partner asks her for "the file" on a consultant he barely staffed, and she sends two thin forms and a forwarded client email. A senior consultant who left last year told her the partner who rated him had seen three weeks of his work. Meera, a senior consultant this year, has had four engagements, three engagement managers and a client CFO who praised her model to the partner. Kavya can see the same year happening again. Vikram, the managing partner, signs. He worries about good juniors leaving and about partners describing the same person in opposite terms because each saw a different engagement.

How the persona shaped each choice (table):

| What we know about Kavya | What we did |
|---|---|
| She cannot buy alone; Vikram signs, and partners can veto | Every piece explains the problem in partner terms (calibration, engagements, staffing) and keeps the decision with partners |
| She gives a new vendor about ten minutes and leaves if she has to book a sales call to understand it | The 2-minute walkthrough opens with no form and no sign-in, and the price is on the home page |
| She trusts other heads of talent more than vendors | Channels are rooms she already chose to be in, introductions from people she knows, and posts reshared by her network |
| Her one budget ask of the year is on the line | The offer is a 12-week paid pilot for up to 40 people, with what it measures agreed before it starts |
| If consultants think HR is watching them, the idea is dead | We say what the product does with feedback, and what managers can see, in plain words on the site |
| The client relationship belongs to the partner | Clients join a consultant's circle only when the consultant invites them by email, with the partner's agreement |

Who we are not trying to influence, and why (labelled rows):
- Firms under about 40 people. Partners still see everyone's work, so the belief we want to change is still mostly true for them.
- MBB, the Big 4 and other global firms. They run global review systems and global procurement, and a 12-week pilot from a head of talent does not fit how they buy.
- IT services and technology consulting. Another team in the course works on that domain, and the work pattern differs.
- Staffing firms that place people at one client for years. The client's own manager sees the work, so the record does not break up.
- Buyers who want to monitor activity. Sphyr holds only what colleagues choose to say on a card. Chasing these buyers would cost us the consultants' trust.

#### 2. The belief we want to encourage

Table:

| | Today | After the campaign |
|---|---|---|
| Belief | "Losing track of a consultant's year is just how consulting works." Or: "It's politics." | "Losing the record when engagement teams break up is a problem we can fix, and fixing it gives partners more to judge with." |
| Attitude | Resigned. Feedback tools look like admin for consultants or like HR watching them | Curious about a light, regular record from the people who saw the work, and confident partners will accept it |
| Response | Chase forms again, and explain the result in exit interviews | Take the 2-minute walkthrough, book a 20-minute call, then propose a paid pilot to the managing partner |

Why the current belief holds. It used to be true at a smaller size, when a few partners worked next to everyone. Growth took that away slowly, so there was never one moment that felt like a failure. Partners also trust their own judgement, and any message that sounds like "your partners are biased" gets rejected in the first meeting.

How we move it. We name a cause that every partner will admit to: people rotate across engagements, and memory fades. By the time partners sit down to decide, the engagement manager who saw someone's best work is on another engagement or has left the firm. Seen that way, the problem belongs to the structure of consulting work. A partner can agree with it without admitting anyone did anything wrong, and a head of talent can raise it without accusing her partners.

#### 3. The central message and the reasoning behind it

The engagement ends. The evidence stays.

In full: Sphyr collects the view of the people who saw a consultant's work, about two minutes every two weeks, while the engagement team is still together, so partners decide on the whole year.

Why this line:
- It describes the moment a head of talent already knows. Engagements end every few weeks, and what the team saw goes with them. She recognises it before she knows what Sphyr is.
- It blames nobody. The engagement ends on its own schedule, so the line works for partners as well as for consultants.
- It promises something a partner wants. More evidence on the table makes his decision easier to defend.
- It is short enough to repeat. Each person sees a post or a standee once, so the line has to work in one reading and stay the same everywhere.

The reasons to believe, each with its source (labelled rows):
- Ratings say a lot about the rater. In two data sets of managers (2,350 and 2,142 people, each rated by seven raters), idiosyncratic rater effects explained 62% and 53% of rating variance, and the person's actual performance 21% and 25% (Scullen, Mount and Goff, 2000) [1].
- People doubt their reviews. Gallup reports that 29% of employees strongly agree their reviews are fair and 26% that they are accurate. The figure is global, and Gallup does not state the sample on that page [2].
- Consulting has seen this already. Deloitte moved to short "snapshots" completed "at the end of a project, phase, or at least quarterly" [3]. Deloitte has nothing to do with Sphyr.
- The method takes about two minutes. In a 2018 paper-and-pen pilot run by Sphyr's founder in four companies, a card took a little over two minutes (02:09) for an average circle of 14 people. That was the method on paper, self-reported, and not today's software [4].

#### 4. Tactics and channels

Tactics (labelled rows):
- Give the problem a name. The core line gives a head of talent words she can say to a partner. Post 1 describes the moment when a partner asks for "the file" and asks readers what they send.
- Choose the cause with care. We talk about rotation and fading memory. We never describe partners as unfair or biased, in any piece.
- Repeat one idea. The website, the three posts and the ad all carry the same line and the same picture of engagements ending while one record runs through them.
- Show the workings. The site shows how cards and pooling work, what managers can see, what Sphyr does not do, the price and the pilot terms. Openness asks the reader for less trust.
- Build proof in public. Every pilot is measured on four things agreed before it starts: participation in each cycle, how many different people give feedback to each consultant, whether partners found something new, and whether consultants found their own record useful. Results stay with the firm unless it agrees to share them.
- Let the reader see for herself. The walkthrough lets a head of talent or a partner click through a card and a record in two minutes, with no form. People believe what they check more than what they are told.

Channels (labelled rows), all free except the one advertisement:
- Sphyr's LinkedIn company page, reshared by the team from their own profiles. It carries the three posts. Heads of talent and partners read LinkedIn for work, and a post a peer reshares reaches them through someone they know.
- Warm introductions through the team's, the faculty's and alumni networks. One personal note per firm, asking permission to share the walkthrough. A single introduction from someone she trusts outweighs any ad.
- HR peer communities and their chapter meets. We attend as participants and offer a talk on calibration when people rotate, if a chapter wants one. This is where heads of talent compare notes.
- Consulting professional bodies, where partners meet. A talk or a written piece on keeping track of work across engagements.
- Contributed articles in HR media that accept pieces from practitioners. They bring readers we could not reach alone, under an editor's standards.
- A monthly note, by sign-up only, with one-click unsubscribe. It keeps the relationship going after the first visit without chasing anyone.
- Our own website. Every other channel points here, to the walkthrough, the method, the price and the pilot terms.
- The advertisement. A standee with matching handout cards at an HR community event, planned and not yet booked. It is the one paid placement, because in our course advertising is the route where money is involved. The QR code opens a plain address, and nobody is tracked.

What we never do: retargeting, tracking pixels, bought or scraped contact lists, automated LinkedIn messages, cold mass email, planted comments, or any suggestion that a community, the faculty or the university endorses Sphyr.

#### 5. Why these tactics fit this audience and this objective

The objective is a change of belief, and the person whose belief we need first is a head of talent who will then have to persuade her partners. That shapes every choice.

She is sceptical of vendors and short of time, so the evidence has to be something she can check herself: a walkthrough with no form, sources named on the page, a price she can see. She hears about new ideas from peers, so the channels are peer rooms and introductions, and the posts are written so she can forward them. The partners she has to persuade will reject anything that sounds like a complaint about them, so the cause we name is rotation and memory. Consultants decide whether the record exists at all, so nothing we publish talks about watching or measuring them, and the site says plainly what managers can see.

The zero-budget rule and the no-tracking rule fit the same audience. A firm that sells fairness to its own people will not trust a vendor that follows them around the web. Keeping the paid part to one standee in a room she chose to enter is consistent with what Sphyr asks firms to believe about it.

#### 6. How the strategy connects to positioning

Our positioning has a vision line and a product line.

Vision: "Careers in consulting should be earned in front of the people who saw the work, not decided by whoever remembers it."

Product: "For homegrown consulting firms where people move from engagement to engagement, Sphyr is 360 feedback that takes two minutes every two weeks, from the people each consultant works with. Unlike a year-end review written from memory or one manager's end-of-project form, it keeps the record when the team breaks up, so partners decide on the whole year."

Each part has a job here. "People move from engagement to engagement" is the cause we name in the belief shift. "Two minutes every two weeks" answers the fear of admin. "Partners decide on the whole year" answers the partner's veto. The vision line is the reason a consultant would want this, and the core line compresses all of it into seven words.

Every piece follows the same order: the moment the engagement ends, the two-minute mechanism, what partners see, the vision, then one next step. The website uses all five. The posts stop earlier and ask a question or point to the walkthrough. The ad uses the moment, what partners see and the walkthrough.

#### 7. The action and response we expect

In order:
- She recognises the problem and says so: a comment on post 1, a saved post, a post forwarded to a partner.
- She takes the 2-minute walkthrough.
- She books a 20-minute call with our team.
- She takes a pilot proposal to her managing partner: 12 weeks, six fortnightly cycles, up to 40 people, ₹25,000 plus GST, credited against the first annual bill if the firm signs. If it does not sign, the firm gets its data as a CSV file and the rest is deleted.
- After the pilot, the firm decides on its own scorecard. The price is ₹149 per employee per month, billed yearly, plus GST, for any firm size.

How we will know, without tracking anyone: weekly totals of walkthrough visits, never per person; the question "where did you hear about us?" on every call; and the number of pilots. Our estimate to test is three to five paid pilots by week 8 of the sequence below.

The change of belief shows before any of that. A head of talent who describes the problem to a partner as a record that breaks up with the team, and not as unfair partners, has already moved.

#### 8. The campaign sequence over the selling season

We count weeks from the first post. The sequence starts about 22 weeks before partners calibrate, because a 12-week pilot has to finish with time left for partners to read the records.

| Weeks | Stage | What runs | What we want |
|---|---|---|---|
| 1 to 2 | Name the problem | Post 1, the website and walkthrough live, the first warm introductions | Heads of talent recognise the moment and start using the line |
| 3 to 4 | Show how it works | Post 2, the standee and handout cards at an HR community event, talks where a community invites us | Walkthrough visits; the idea that two minutes a fortnight is less work than chasing forms |
| 5 to 6 | Earn trust | Post 3 on what every pilot measures, 20-minute calls | Calls booked; pilot proposals drafted for managing partners |
| 7 to 8 | Make the case to partners | Calls with managing partners when the head of talent invites us, the partner section of the site | Pilots agreed and started by week 8 |
| 9 to 20 | Run the pilots | Six fortnightly cycles, the monthly note, check-ins on participation | Consultants see their own record; participation holds through busy client weeks |
| 21 to 22 | Partners read the records | A short guide for partners on reading a record across cycles | Partners come to the discussion with the whole year in front of them |
| After | Review and refer | The scorecard reviewed with the head of talent and the managing partner | A decision on the firm's own results; heads of talent who choose to talk to peers |

#### 9. Objections we expect, and our answers

| Objection | Our answer |
|---|---|
| A partner: "So now HR rates my team?" | Partners still decide. They see the view of the people who worked with each consultant on every engagement, and they fill in the same two-minute cards as everyone else |
| A head of talent: "My consultants won't fill in another form in a 60-hour week." | A card takes about two minutes, every two weeks, for the people in their circle. In the 2018 paper pilot it took 02:09 for a circle of 14. Each consultant also gets to read their own record |
| A consultant: "This is HR watching us." | Sphyr holds only what colleagues choose to say on a card. Ratings are pooled and comments are anonymized to the person rated. A manager who approves a request to edit feedback can see who gave it, and we say so on the site |
| A partner: "Will my clients be asked to rate my people?" | Only when the consultant invites a client by email, with the partner's agreement. The client relationship stays with the partner |
| "We already have reviews in our HR system." | Sphyr runs next to it. People are imported from a spreadsheet. It adds what the HR system does not keep: a view from everyone a consultant worked with, every two weeks, across engagements |
| "Who else has tried this?" | Every pilot is measured on the same four things, agreed before it starts, and the firm keeps its results unless it agrees to share them. The method was tried on paper in 2018. And the walkthrough lets you check the product yourself in two minutes |
| The managing partner: "What if it shows us nothing?" | The pilot costs ₹25,000 plus GST, which is what it costs us to run. If the firm does not sign, it gets its data as a CSV file and the rest is deleted |

#### 10. Our limits

Propaganda can mislead, and a product that asks firms to trust a fairer record cannot afford to. So we hold these lines. We do not invent customers, reviews or statistics. Every story is labelled as an illustration. The 2018 pilot is always described as paper and pen, run by the founder, and self-reported. We never call the feedback anonymous without saying what managers can see. We never use fear of losing people, false deadlines or limited places to push a decision. We name communities only as places we take part in, and none of them endorses Sphyr.

(Note: section 10 heading on the page is "Our limits"; the index says 11 items because the summary counts as none. I will renumber to 10 in the build.)

#### Sources

1. Scullen, Mount and Goff (2000), "Understanding the latent structure of job performance ratings", Journal of Applied Psychology 85(6), summary at https://peopleanalyst.com/ai/insights/ic-scullen-2000-idiosyncratic-rater-variance (accessed 2026-11-24)
2. Gallup, "Give Performance Reviews That Actually Inspire Employees", https://www.gallup.com/workplace/236135/give-performance-reviews-actually-inspire-employees.aspx (accessed 2026-11-24)
3. ATD, "Reinventing Performance Management at Deloitte", https://www.td.org/content/atd-blog/reinventing-performance-management-at-deloitte (accessed 2026-11-24)
4. Sphyr Overview Whitepaper v0.3, 2018, pages 3 to 4 (course material, not public)
5. Sphyr prototype, https://sphyr-prototype.raviwarrier.com/ (accessed 2026-11-24)

### C. README.md

```
# Sphyr

Team 03's final assignment for Product Marketing (PD2.501), IIIT Hyderabad.
Aryan, Abhinav, Devansh, Bheema.

Live site: https://devanshdhaked.github.io/Product-Marketing-final-assignment/

## The deliverables

| # | Deliverable | Page |
|---|---|---|
| 1 | Website, the hub for everything else | [Home](.../index.html), [2-minute walkthrough](.../demo.html), [Deliverables](.../deliverables.html) |
| 2 | Propaganda strategy | [propaganda.html](.../propaganda.html) |
| 3 | Three LinkedIn posts | [linkedin.html](.../linkedin.html) |
| 4 | Advertisement | [ad.html](.../ad.html) |

Nothing needs a sign-in.

## The product

Sphyr is 360 feedback for performance appraisal. Every two weeks each person spends about two minutes on short cards for the people they worked with. Ratings are pooled and comments are anonymized to the person rated. Each person can read their own record, and managers see team and member trends across cycles. It runs next to the firm's HR system; people are imported from a spreadsheet.

Sources: Sphyr Overview Whitepaper v0.3 (2018) and the Sphyr product guide and prototype shared in class.

## Strategy in brief

| | |
|---|---|
| Segment | Homegrown, partner-led Indian management and strategy consulting firms of about 40 to 400 professionals |
| Persona | The head of talent, who finds Sphyr, runs the pilot and takes the case to the managing partner, who signs |
| Central message | The engagement ends. The evidence stays. |
| Price | ₹149 per employee per month, billed yearly, plus GST, the same for any firm size |
| Pilot | 12 weeks, six fortnightly cycles, up to 40 people, ₹25,000 plus GST, credited against the first annual bill if the firm signs |
| Channels | LinkedIn company page and team reshares, warm introductions, HR and consulting communities, our own site, and one paid standee at an HR community event |

## Repository layout

site/          the website (plain HTML, CSS and JS, no build step)
docs/          strategy, pricing, packaging, design and decision records
design-lab/    design mockups and the copy and contrast checks
assignments/   earlier team work
final assignment.md   the assignment brief and rubric
devansh_notes.md      project notes

## Run locally and redeploy

cd site && python3 -m http.server 8765    (open http://localhost:8765)

GitHub Pages serves the site from the gh-pages branch. After editing site/, commit and run:
git subtree push --prefix site origin gh-pages

Course project, not a live commercial offer. The 2018 pilot was a paper-and-pen trial of the method, not of today's software.
```

README questions: keep the team names? Keep the redeploy command (agents do not push; it is for the team)? The `.../` stands for the live URL; full URLs in the build.

## Progress

- 2026-11-25: worktree created, docs read, sample sizes checked, Plan and Draft written. Waiting for approval and for sitecss to merge.
- 2026-11-25: ran `copy_scan.py` and `copy_tells.py` on a scratch HTML wrapper of Draft A and B (scratchpad `hub.html`, `prop.html`).
  - Hub: 10 strings, 0 hits, 0 contrasts, 0 triads.
  - Propaganda: 111 strings, 18 unreviewed keyword hits, 1 contrast (the vision line, intended), 29 possible triads.
  - The 18 hits are words like "tracking", "endorse", "reviews", "fair" and "anonymized" used in guardrails, objections and the never-do list, which deny or qualify a claim. I will review each in the build and record it in the scanner's reviewed list if the scanner supports one, otherwise list them here.
  - Of the 29 triads, about 10 are real three-item lists that cannot change (author names, persona names, Deloitte's quote, the three posts). About 19 are rhythm and I will cut or reshape them during the humanizer file pass before commit. Target: 0 rhythmic triads.
- Waiting for: plan approval, answers to the 8 open questions, and the sitecss merge.

## Progress (build)

- 2026-11-25: merged `iteration-a` (c705c3e), built both pages, `deliverables.css` and the README, then applied the lead's answers to questions 1 to 8 and the new roles-over-pronouns rule.


## Final

### Files written, with commit SHAs (branch `d1-hub`, not pushed)

- dd22a86 `site/css/deliverables.css`, `site/deliverables.html` (hub)
- 615c2dc `site/propaganda.html`
- 29063d3 `README.md`
- 0e33461 `site/deliverables.html`, `site/propaganda.html`: people named by role, with "they" where gender is not given (new copy rule)
- e5bdf5c `site/deliverables.html`, `site/propaganda.html`. Copy changes:
  - Humanizer pass: removed the one-line closers and staged openers, varied the seven sequence rows that all used "We want", and rewrote the "Why this line" paragraph.
  - Removed a hidden contrast ("never per person").
  - Deloitte now "moved to" snapshots instead of "replaced".
  - Each hub entry has one sentence naming its job and journey stage, and one link.
  - `.doc-num` is `aria-hidden`, so headings no longer read "1The audience".
- 41669d6 `site/deliverables.html`, `site/propaganda.html`: full-colour logo mark in the nav and footer (`class="mark"`), per the user change.
- Not committed: `site/_shots/` (14 PNGs). They sit inside `site/`, so committing them would deploy them with `git subtree push`. Lead to decide.

### Key insights and findings (with sources)

- Scullen, Mount and Goff (2000) used two data sets of managers (n = 2,350 and n = 2,142), each rated by 7 raters. https://peopleanalyst.com/ai/insights/ic-scullen-2000-idiosyncratic-rater-variance (read 2026-11-25)
- Gallup's 29% and 26% figures come with no sample size, population or year on the page (published 2017-09-25, modified 2026-08-21). https://www.gallup.com/workplace/236135/give-performance-reviews-actually-inspire-employees.aspx (read 2026-11-25). The page says "global, sample size not stated".
- `base.css` already had `.doc`, `.rows`, `.table-wrap`, `.figure`, `.src-note` and `.go`. `deliverables.css` only adds `.doc-head`, `.doc-index`, `.doc-num`, `.core-line`, `.table-stack`, `.hub-index`, `.seq` and `.sources`.
- Chrome caps one capture at 16384 px, so a taller full-page screenshot repeats content. The propaganda page at 375 px is about 21,700 px tall, so it is saved in parts.
- `copy_tells.py` only catches contrasts written with ", not ". A clipped tail like "weekly totals, never per person" slips through, so check for it by eye.

### Decisions I made and why

- The propaganda page's first seven headings follow the brief's 4B items in order, so a grader can map them directly. The four extras follow (sequence, persona, objections, limits).
- The sequence counts weeks from the first post. It names the promotion moment once ("week 22, when partners calibrate") and works back: a 12-week pilot must start by week 8.
- The sequence is drawn as a static week ruler with bars on desktop, and becomes a plain list with a left rule on phones. There is no motion.
- The three-column belief table stacks into labelled blocks under 640 px (`.table-stack`), because it was unreadable at 375 px.
- The core line is set once in the display serif (`.core-line`).
- Sources use ISO access dates (2026-11-24), so the page has no month names.
- Each hub entry links only from its title (the Stripe Press pattern; few links). I removed the extra "Read the strategy" style links.
- `deliverables.css` has no raw hex values. The sequence bars use `--brand`, and the "after" stage uses `--border-strong`.

### Approaches rejected and why

- A data table for the sequence: it reads poorly on phones. The ordered list carries the same text for screen readers.
- Whitelisting scanner hits in `design-lab/copy_scan.py`: that is a shared file outside my ownership.
- The shared Playwright MCP browser: another session was using it. I used playwright-core in my scratchpad with local Chrome instead.

### Open questions for the lead

1. Should `site/_shots/` be committed? They would deploy with the site.
2. In the template, `og:image` points to `assets/og.png`, but the image is `site/og.png`. This belongs to the shared template owner.
3. The hub numbers its entries 02 to 04, and propaganda says "Deliverable 2 of 4". Check this matches `linkedin.html` and `ad.html`.
4. Should the README keep the `git subtree push` redeploy steps? It is for the team; agents do not push.

### What I did not verify

- Safari, Firefox, touch input and screen readers.
- Contrast of the sequence bars in dark theme, which I checked only by eye.
- Whether `linkedin.html` and `ad.html` match the hub's one-line descriptions. I wrote those from `deliverable_map.md` and the ad decision, not from the built pages.
- The ATD page on Deloitte, which I did not open. I used the wording in the repo docs.
- README links on the live site. They resolve only after the team redeploys.

### Checks (final state, after 41669d6; screenshots regenerated)

Method: playwright-core 1.65.1 in my scratchpad driving local Chrome, against the lead's server on 8824.

- 24 of 24 runs pass. The runs cover 2 pages, 2 themes, widths 1280, 390 and 375, and reduced motion on and off.
  - Sideways scroll is 0 in every run.
  - Smallest text is 13 px (the "On this page" label). The limit is 11 px.
  - Page `requestAnimationFrame` calls over 2 s after load: 0. Running animations: 0.
  - Console errors: 0.
  - The stored theme applies on load in both themes.
  - `aria-current` is on Deliverables in both nav lists only.
- Links: 21 relative links checked. 18 resolve. The 3 failures are the template's `index.html#how`, `#partners` and `#pricing`. Those anchors do not exist yet on this branch's old home page.
- `copy_scan.py`:
  - Hub: 48 strings, 0 hits.
  - Propaganda: 245 strings, 22 hits. I reviewed all 22 by eye. Every one is a denial, a qualifier or a source title: "reviews", "track", "endorse", the qualified "anonymous", the brief's word "objective", and "Journal" in a journal name.
- `copy_tells.py`:
  - Hub: 0 contrasts. 1 triad, which is the template footer's team names.
  - Propaganda: 1 contrast, the quoted vision line, as agreed. 16 possible triads. By eye, all 16 are real lists (persona names, author names, Deloitte's quote, the never-do list, footer names) or two-item sentences the scanner miscounts.
- Other searches on visible copy:
  - Month names: 0. Em dashes, en dashes and double hyphens: 0.
  - Persona names after the audience section: 0.
  - Gendered pronouns left: 1, "Kavya gets one new budget line a year, and her name is on it". That sentence has one person and her gender is given.
- `contrast.mjs`: not run. No colours were added.
- Screenshots: `site/_shots/{deliverables,propaganda}-{light,dark}-{1280,375}.png`. Propaganda at 375 is saved as `-part1` to `-part4`.
