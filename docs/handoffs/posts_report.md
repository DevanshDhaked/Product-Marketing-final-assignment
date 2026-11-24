---
type: Handoff
title: "LinkedIn posts and ad teammate report, phase 2"
description: "The three LinkedIn post mockups and the standee ad with its rationale: drafts, checks, QR verification, decisions and unverified items."
tags: [handoff, posts]
generated: { by: claude-code/opus-5-5, at: 2026-11-25T03:30:00Z }
---

# LinkedIn posts and ad teammate report, phase 2

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Worktree: `Product-Marketing-final-assignment.d1-posts`, branch `d1-posts` from `iteration-a` at 910ca83. Nothing committed yet. Status: plan and draft written, waiting for approval. HTML waits for the sitecss merge.

## Plan

### Success number
Both pages pass every phase 2 check with 0 unreviewed copy hits, 0 contrast failures, 0 sideways scroll at 390 px and 0 idle frames, in both themes. Until the build, the number is the draft copy checks below.

### What I read
`docs/index.md`, `decisions/decision_log.md` (all), `strategy/deliverable_map.md`, `strategy/message_guideline.md` (all), `strategy/acquisition_engagement.md` (scorecard and engagement), `product/do_not_claim.md`, `product/evidence_and_claims.md` (pilot), `design/faux_ui.md`, `handoffs/design_report.md` (Final), `handoffs/admedium_report.md` (options, recommendation), `brief/communication_objectives_notes.md`, the brief sections C and D, `main:site/linkedin.html` and `main:site/ad.html` as text only, and the sitecss plan in its report.

### Files
1. `site/linkedin.html`, from `site/_template.html`.
   - Header: title in Newsreader, one short intro line.
   - Three post blocks. Each one has the post mockup on the left and its note on the right. On phones the note sits under the mockup.
   - The mockup is a generic feed card: the Sphyr mark and name, a true tagline, a relative time ("1w"), the post text with a "see more" fold after the first two lines (CSS `details`, no JS), and the Like, Comment, Repost and Send bar drawn with Lucide icons from `assets/icons.svg`.
   - Post 2 carries the "Giving feedback" frame from base.css as its image, with the core line above it and the label "Prototype screen. Sample data, fictional people." below it. Posts 2 and 3 show one first comment from the Sphyr page with the link.
   - Not shown: the LinkedIn logo, reaction counts, follower counts, other commenters or replies. Any of those would be invented proof.
   - Note per post: job, belief it shifts, journey stage, call to action and when it runs. This is a small `dl` with muted labels as structure, not bold labels in front of sentences.
   - Section "How the three work together": one paragraph and a three-step strip (week 1, week 3, week 5).
   - Links: walkthrough (`demo.html`), the ad page, the deliverables hub.
2. `site/ad.html`, from `site/_template.html`.
   - Header plus a stage that shows the portrait roll-up standee at the 850 by 2000 mm ratio. The A6 card sits beside it, front and back, at 105 by 148 mm. On phones they stack.
   - The standee uses the ribbon motif from `css/motif.css` and `js/motif.js`: four boxes "Project 1 · 3 teammates" to "Project 4 · 3 teammates", fading, with one line running through. It also has the headline, the supporting line, the call to action, the QR and the URL.
   - Rationale beside or below it, in nine short sections: medium, audience, message, benefit, visual, call to action, journey stage, placement, why it tracks nobody.
3. `site/css/posts.css`: feed card chrome, the fold, the note layout and the sequence strip, in both themes.
4. `site/css/ad.css`: standee and card proportions, print look (flat colour, no shadow glow), stage layout and phone layout.
5. `site/assets/ad/walkthrough-qr.svg`: a real QR code for `https://devanshdhaked.github.io/Product-Marketing-final-assignment/demo.html`, generated as static SVG. See question 1.
6. No page JS. The fold is `details` and the motif uses the shared `motif.js`. If the ad needs the motif to run more than once on a page, I will ask.
7. `site/_shots/`: linkedin and ad, light and dark, 1280 and 375 (8 PNGs).

### Checks (after the build)
Serve on port 8825. Run `copy_scan.py` and `copy_tells.py` on both pages and `contrast.mjs` if I add colours. Run the untemplated checks from `docs/design/homepage.md` (sideways scroll at 390, smallest text 11 px, idle frames, reduced motion, contrast in both themes), the toggle and no-flash test, and confirm every link resolves. I will also decode the QR SVG back to text with a second tool, to prove it opens the exact URL. Before committing, every visible string goes through the humanizer again.

Build-time guards:
- `copy_tells.py` skips text inside `.stage` and `.cv` (faux UI and motif). All marketing copy stays in plain HTML outside those classes, and the built pages must show at least the draft's string counts (58 and 33).
- Before the ad page claims it tracks nobody, I grep the built `site/*.html` and `site/css/*.css` for external origins (`https://` in `src`, `href`, `@import`, font CDNs, analytics), with most attention on `demo.html`, where the QR lands. A hit goes to the lead before the claim ships.

### Open questions for the lead
1. **QR generator.** None is installed: `qrencode`, `zint`, Python `segno` and `qrcode` are all missing, and none is in npm global. I propose `segno` (pure Python, no dependencies) in a scratchpad venv: `python3 -m venv $SCRATCH/qr && $SCRATCH/qr/bin/pip install segno`. It would write the SVG once. To prove the code, I also need a decoder, and none is installed: I propose `zxing-cpp` (pip, same venv) to read back a PNG render of the SVG. The alternative generator is `npx qrcode`. Please approve the generator and the decoder together. Nothing is installed until you say so.
2. **Short plain URL.** The real address is long. We own no short domain. `sphyr.io` is named in the whitepaper but is not ours, and link shorteners count clicks. I propose printing the full address in small type under the QR code, with the QR doing the work. On the standee that reads as `devanshdhaked.github.io/Product-Marketing-final-assignment/demo.html`. Is that acceptable?
3. **Price on the ad.** I recommend no price on the standee, which carries one message. I would put the exact line "₹149 per employee per month, billed yearly, plus GST" on the back of the A6 card, because the card is what a head of talent takes back to the partners. Keep it, or drop it?
4. **Poster.** I propose that all three posts come from the Sphyr company page, so no team member's name is attached to lines they did not write, and team members reshare them. Should one post instead go out under a named team member (Aryan, Abhinav, Devansh or Bheema)? If so, which post and whose name?
5. **Post 1 and message step 2.** The deliverable map says post 1 covers "message steps 1 and 2 only". I kept it to the scene and the question, plus one line that says the next post shows how. A recognition post that explains the mechanism starts to sell. Is that acceptable?
6. **Reviewed scanner hits.** The ad page has to say "Why it tracks nobody" and "no endorsement", so `copy_scan.py` flags "track" and "endorse" as denials. The scanner's ALLOWED list belongs to the design lab, not to me. Can sitecss or you add those exact strings, or should I report them as reviewed hits?

## Draft

All copy below was written by hand against the humanizer rules (contrasts, closers, triads, dashes, bold labels re-searched after each edit), then counted with `copy_scan.py` and `copy_tells.py` on a scratch HTML copy. The copy is at `/private/tmp/claude-501/-Users-borah-resources-IIITH-PDM-sem-3-pm-Product-Marketing-final-assignment/b1f02b1a-238c-4cc6-89df-71fa421ff731/scratchpad/_draft_posts.html` and `_draft_ad.html` in the same folder.

Results for linkedin: 58 strings, 0 unreviewed hits, 0 contrast sentences, 1 triad flag. The flag is the author list "Scullen, Mount and Goff", which the citation needs, so it was reviewed. Results for ad: 33 strings, 0 contrast sentences, 0 triads, and 3 hits, all of them denials (question 6).

There are no month names, no persona names, no customer claims and no announcement that there are none. The promotion moment appears at most once per post, and once on the ad page (the standee's "partners calibrate").

### Post 1: recognition (Sphyr company page, week 1)

> A partner asks you for "the file" on a senior consultant he never staffed. What do you send him?
>
> Usually it is her self-appraisal and one form from an engagement manager who has since moved to another client. The people who saw her best work were on an engagement that closed months ago, and they are spread across other engagements now.
>
> Nobody did anything wrong here. Its people scatter when an engagement closes, and what they saw goes with them. So the partner reads the file and then rings the one engagement manager he knows. That call ends up counting for more than anything written down.
>
> We think those people should be asked while the team is still together, and our next post shows how.
>
> Heads of talent, when a partner asks for the file, what goes in it? And who do you call to fill the gaps?
>
> #Consulting #TalentManagement #PeopleDevelopment

Note:
- Job: get heads of talent to recognise the problem and talk about it with peers.
- Belief it shifts: from "this is just how promotions work" to "the record breaks up with the team, and that can be fixed".
- Journey stage: the trigger, when a head of talent first puts a name to the problem.
- Call to action: the question at the end. There is no link, so the post reads as a question to peers.
- When it runs: week 1 of the sequence.

### Post 2: mechanism (Sphyr company page, week 3)

> In two large data sets, more than half of the variation in performance ratings came from who did the rating. In consulting, that person may have seen one engagement out of four.
>
> The study is Scullen, Mount and Goff, 2000. Idiosyncratic rater effects (the particular way each rater tends to rate) explained 62% and 53% of rating variance in the two data sets. The actual performance of the person rated explained 21% and 25%.
>
> So a single rating tells a partner quite a lot about the rater. Asking more of the people who saw the work, while they still remember it, gets you closer to the work itself.
>
> That is how Sphyr works. Every two weeks, each person gets a short card for each colleague they worked with, asking how the work together went that fortnight. They tap one of the answers on the card below and add a tag or two, plus a note if they want one. In a 2018 paper-and-pen pilot run by Sphyr's founder, the cards took a little over two minutes (02:09) for an average circle of 14 people.
>
> Ratings are pooled and comments are anonymized to the person rated. Over the year each consultant builds up a record from the people who saw the work, and partners bring it to calibration, where they still make the decision. Two minutes every two weeks is a lot less work than chasing appraisal forms from people who have already moved on.
>
> You can try a card yourself in the 2-minute walkthrough. The link is in the first comment.

Image: the core line "The engagement ends. The evidence stays." above the "Giving feedback" frame. The frame shows the card question "How was your experience with Member B this fortnight?" and the three real answer tiles. Under it sits the label "Prototype screen. Sample data, fictional people."

First comment (Sphyr): "The 2-minute walkthrough: devanshdhaked.github.io/Product-Marketing-final-assignment/demo.html"

Note:
- Job: show the evidence for asking more people, and show how small each ask is.
- Belief it shifts: from "more feedback means more admin" to "two minutes every two weeks is less work than chasing forms at the end of the year".
- Journey stage: looking for answers.
- Call to action: the 2-minute walkthrough, linked in the first comment.
- When it runs: week 3, after the team has replied to the answers on the first post.

### Post 3: proof built in the open (Sphyr company page, week 5)

> The firm and our team agree in writing how a Sphyr pilot will be judged before it starts. This is what every pilot measures.
>
> 1. How many people take part in each cycle.
> 2. How many different people give feedback to each consultant.
> 3. Whether partners found something new in the records, and whether it changed any discussion.
> 4. Whether consultants found their own record useful, and whether they want to keep going.
>
> The firm agrees the target for each one before the first cycle opens. Results stay with your firm unless you agree to share them.
>
> We publish this because a firm trying something new should know the test before it signs anything. The method itself was tried before the software existed, in a 2018 paper-and-pen pilot run by Sphyr's founder in four companies. Those results were self-reported, so the one figure we use from it is time: cards took a little over two minutes for an average circle of 14.
>
> A pilot runs for 12 weeks, which is six fortnightly cycles, with up to 40 people. It costs ₹25,000 plus GST, and that amount comes off the first annual bill if the firm signs. If it does not sign, the firm gets its data as a CSV file and we delete the rest.
>
> If you would like to run one with a single practice before your next promotion round, book a 20-minute call with our team. The link is in the first comment.

First comment (Sphyr): "Book a 20-minute call: devanshdhaked.github.io/Product-Marketing-final-assignment/#call" (or whichever anchor opens `#call-note`, to confirm against the template).

Note:
- Job: give a careful buyer a reason to trust something new.
- Belief it shifts: from "new means risky" to "an open method and a test agreed in advance are safer to rely on than a vendor's claims".
- Journey stage: seeking validation and making the case to the managing partner.
- Call to action: book a 20-minute call.
- When it runs: week 5.

### How the three work together (page copy)

> The first post asks heads of talent to describe the problem in their own words, and the team reads every answer before the second post goes out. The second answers with the research and the card, then sends readers to the walkthrough, where they can try it without talking to anyone. The third is for the reader who has seen the walkthrough and now has to convince the partners, so it shows the test a pilot has to pass and offers a call. Team members reshare each post from their own profiles. The standee ad runs at an HR event in the same weeks as the first post and carries the same line.

### The ad: roll-up standee (portrait)

- Top: the Sphyr logo.
- Visual: the ribbon. Four boxes, "Project 1 · 3 teammates" to "Project 4 · 3 teammates", fade one after another while one line runs through them all and stays clear.
- Headline: "The engagement ends. The evidence stays."
- Supporting line: "Every two weeks, the people who saw a consultant's work spend two minutes on it, so partners calibrate with the whole year in front of them."
- Call to action: "Take the 2-minute walkthrough", then the QR code and the URL in small type.
- No price (question 3).

### The ad: A6 handout card

- Front: the standee design at card size, with the same headline, line, call to action and QR code.
- Back:
  > Sphyr asks the people who worked with each consultant for short cards every two weeks, while the engagement team is still together. Ratings are pooled and comments are anonymized to the person rated. Partners still make the decisions.
  >
  > ₹149 per employee per month, billed yearly, plus GST *(only if question 3 says yes)*
  >
  > Take the 2-minute walkthrough *(QR and URL)*
  >
  > No sign-up. We add nothing to this link or code that identifies you.

### Ad page intro and rationale (page copy)

> The advertisement. A roll-up standee and a matching handout card, planned for a paid sponsor spot at an HR community event.

- Medium: A roll-up standee on a paid sponsor spot at an HR community event, with A6 cards on a stand beside it for people to take. In our class notes, advertising is the push route where "money is involved", so the placement is a paid one. The same poster put up for free would count as word of mouth.
- Audience: Heads of talent at partner-led consulting firms of about 40 to 400 people, and the partners who sometimes come with them. The room will hold HR people from every industry, so the copy uses consulting words like engagement and calibrate. The right people stop, and everyone else can walk on.
- Message: The core line, with one supporting line on how it works.
- Benefit: Partners have a year of views from the people who saw each consultant's work.
- Visual: The ribbon from the website. Four project boxes fade one after another while a single line (the consultant's record) runs through all of them and stays clear at the end. There are no faces or scores on it.
- Call to action: Take the 2-minute walkthrough. The QR code and the printed address open the same page, and it asks for nothing.
- Journey stage: The trigger, when a head of talent first puts a name to the problem. It runs in the same weeks as the first LinkedIn post.
- Placement: Planned for an HR community event of the kind run by national HR network chapters. Paying for a spot does not mean the organisers endorse Sphyr.
- Why it tracks nobody: Nobody's badge is scanned and nobody fills in a form. The QR code holds the plain page address with no tracking parameters, so a scan tells us nothing about who made it. People who are curious can look, and everyone else can walk past.

## Status (at the plan stop)
- Done: worktree, reading, plan, full draft copy with copy checks (method and counts above).
- Not done: any file in `site/`, the QR code, screenshots, commits.
- Blocked on: approval, the sitecss merge, and questions 1 to 6. Questions 1 and 2 block the ad build.
- Not verified: the shape of the call-note anchor in the template; whether `motif.js` can run twice on one page (standee and card front); and the claim that LinkedIn folds after about two lines (shown as an approximation in the mockup).

## Build (after approval)

Merged `iteration-a` at c705c3e (sitecss pass 1), then built both pages from `site/_template.html` with the new 4-link nav. `aria-current="page"` is on Deliverables in both the bar and the Menu popover. The approved draft copy is used verbatim, plus the lead's answers: no price on the standee, the exact price line on the card back, and all three posts from the Sphyr company page.

### Checks (method and numbers)
- Method: a private headless Google Chrome driven by the local `playwright-core` (npx cache), against the lead's server at http://127.0.0.1:8825/. The shared Playwright MCP browser was in use by another session, so I did not touch it. I started no server.
- `copy_scan.py`: linkedin 160 strings, 0 unreviewed hits, 1 reviewed denial ("Nothing to review", the prototype tile). Ad 90 strings, 3 hits, all reviewed denials (question 6), exact strings:
  1. "Planned for an HR community event of the kind run by national HR network chapters. Paying for a spot does not mean the organisers endorse Sphyr."
  2. "Why it tracks nobody"
  3. "Nobody's badge is scanned and nobody fills in a form. The QR code holds the plain page address with no tracking parameters, so a scan tells us nothing about who made it. People who are curious can look, and everyone else can walk past."
- `copy_tells.py`: 0 contrast sentences on both pages. Triad flags: the footer's team names "Aryan, Abhinav, Devansh and Bheema" (template, on both pages), and on linkedin the author list "Scullen, Mount and Goff", which the citation needs. All 3 flags are names, reviewed. String counts (160, 90) are above the draft's 58 and 33, so no copy is hidden inside `.stage` or `.cv`.
- Sideways scroll: 0 at 1280, 390 and 375, both pages, both themes.
- Smallest text: 11 px on both pages. On linkedin it is the prototype frame's VBA heading; on the ad it is the printed URL, which is held at `max(11px, 2.6cqw)`.
- Idle: 0 running animations and 0 DOM changes in the 1 s after load (measured 1.5 s after networkidle), with and without reduced motion. Neither page loads `motif.js`; the standee ribbon is the finished picture with no `play` class.
- Theme: the toggle sets `data-theme="dark"` and `aria-pressed="true"`, and the body turns #171513. After a reload the stored theme is already set when the document's first readystatechange fires (no flash). The standee and card stay light paper in dark mode on purpose (`color-scheme: light` on `.print`), because they are printed objects.
- Contrast: I added no colour tokens and removed the one raw hex, so `contrast.mjs` was not run. The print pieces reuse the light theme tokens.
- Links: 8 unique links per page, 0 bad (local links fetched with status 200, anchors present). Console errors and failed requests: 0 on both pages, both themes, both widths.
- QR: `segno` 1.6.6 wrote version 5, error level M, 45 modules with a 4-module border. I added `viewBox` and `shape-rendering="crispEdges"` so it scales. `zxing-cpp` decoded the segno PNG, and separately decoded element screenshots of all 3 QR codes as rendered on `ad.html`. All 3 decode to exactly `https://devanshdhaked.github.io/Product-Marketing-final-assignment/demo.html`. Both tools live in a scratchpad venv only.
- External origins: grep of `site/*.html`, `site/css/*.css` and `site/js/*.js` for `http(s)` in `src`, `href`, `@import` and `url()`, and for analytics, gtag, plausible and Google Fonts: 0 hits outside og meta. That includes the current `demo.html`, which is still the old page until the walkthrough teammate replaces it.
- Screenshots: `site/_shots/{linkedin,ad}-{light,dark}-{1280,375}.png` (8 files, full page; the theme comes from colour-scheme emulation).

## Final

### Files written, with commit SHAs (branch d1-posts)
- 0265982: `site/assets/ad/walkthrough-qr.svg`
- d8b46fe: `site/linkedin.html`, `site/css/posts.css`
- eb35f35: `site/ad.html`, `site/css/ad.css`
- 51c2052: `site/_shots/linkedin-*.png`, `site/_shots/ad-*.png` (8 PNGs)
- Nothing pushed. No docs written (my brief names no docs file).

### Key insights and findings
- A container's own padding cannot use its own container units. `cqw` on `.print` padding resolved against the viewport and made the cards unreadable (a6 headline 10.6 px). The fix is an inner `.pr-in` box that carries the padding.
- `light-dark()` tokens resolve per element through `color-scheme`, so setting `color-scheme: light` on a subtree pins a printed object to its light colours in dark mode without new colour values.
- The motif's compact (portrait) composition suits the standee. I dropped its "Promotion round / The whole year is in the file" label so the standee names the moment only once ("partners calibrate").
- No QR tool was installed. segno plus zxing-cpp in a venv works offline with no repo change.

### Decisions and why
- Post folds (`details`) open by default. With the fold closed, the 1280 shot showed each post as two lines beside a full note, so a grader could miss the post text. The fold markup stays and still works if it is closed.
- The post 2 card frame has `inert` and `role="img"`, because a feed image is a picture and not a form. Radio IDs are unique to the page.
- Feed mockups show no reaction counts, follower counts or other commenters; showing them would be invented proof. The action bar uses Lucide icons: thumbs-up and message-square-text from `icons.svg`, and repeat-2 and send inlined in the page (Lucide licence already in `assets/`).
- The first comment on post 3 is the footer's `#call-note` popover button, since there is no call URL.
- No page JS on either page.

### Rejected approaches and why
- The shared Playwright MCP browser: it was locked by another instance ("Browser is already in use"). I used a private headless Chrome instead.
- An animated ribbon on the standee: a printed ad does not move, and it would add motion after load.
- Printing a shortened URL: we own no short domain, and shorteners count clicks.

### Open questions
- `site/assets/og.png` is referenced by the template's `og:image`, but `og.png` sits at `site/og.png`. That belongs to sitecss or the lead.
- Should `copy_scan.py` ALLOWED gain the 3 ad strings above, so the page scan exits 0?
- `deliverables.html` and `propaganda.html` are still the old pages on this branch. The links resolve, but the content belongs to other teammates.

### Not verified
- Safari and Firefox: checks ran in Chrome only.
- Screen reader: not tested.
- Real print sizes: the standee and card are on-screen mockups; text sizes for real print were not set.
- Phone scanning of the on-screen QR: decoded from screenshots with zxing-cpp only, not with a phone camera.
