---
type: Handoff
title: "Headline line analysis report"
description: "What 'The engagement ends. The evidence stays.' is, the job it does on each page, and how it compares with the old site."
tags: [handoff, message]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T21:59:07Z }
---

# Headline line analysis report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Date: 2026-11-25. Read-only. Worktree `iteration-a`; `main` at `fc85cac`. Paths are relative to the worktree, except the course paths, which start with `pm/` (the read-only course folder).

## 1. What the line is in marketing terms

The line is a **tagline**. It is the short, memorable form of the central message, and the team treats it as that message's anchor. It is not a positioning statement and not a value proposition.

Where the definitions come from:
- The course PDFs do not define these terms. The only course hit is "slogan" in a group-identity passage (`pm/resources/Product_Lifecycle_Management_Course_Notes.pdf`, p9: "names, symbols, and slogans").
- So the usable definitions are the team's own notes, which cite outside sources:
  - `pm/tasks/saas/positioning-statement/framework_choice.md:19-24`. A positioning statement is internal: target, category, and why it wins against the alternative. A value proposition is "the customer-facing promise". A tagline is "a short, memorable brand phrase".
  - `pm/tasks/task05b-top-level-message/research-notes.md:19-26` gives the message hierarchy: purpose, promise, positioning, value proposition, pillars, supporting messages. It defines a tagline as the line that "compresses that promise into something quotable".
- The professor's own signals:
  - "Your message is a slogan and not a guideline" (`docs/brief/professor_feedback.md:80`).
  - Earlier, on the team's taglines: "taglines ... a subset of 'messages'", where he had asked for "a top-level message" (`pm/tasks/task05b-top-level-message/task.md:10-14`).

Why it is a tagline:
- The decisive test is in `framework_choice.md:27-30`. A line that names no target, no category and no alternative "is a North Star or tagline. It is not a positioning statement." "The engagement ends. The evidence stays." names none of the three.
- It is not a value proposition. "The evidence stays" says what the mechanism leaves behind, not who gains or what they gain. That benefit, partners deciding on the whole year, is stated in `message_guideline.md:40`, not in the six words.
- In our docs, the central message itself is the sentence at `docs/strategy/message_guideline.md:40`, together with the five-step order at `:44-54`. The positioning statement is at `docs/strategy/positioning.md:51-53`. The six words are labelled "the idea to remember" (`positioning.md:57-59`) and "the core idea" (`message_guideline.md:36-38`).

Risk: two places label the six words alone as the central message, `README.md:32` ("Central message | The engagement ends. The evidence stays.") and `docs/decisions/decision_log.md:139`. That is the same mix-up the professor marked down twice.

## 2. Where it appears and what job each appearance does

| Place | Job |
|---|---|
| `site/index.html:66`, home hero h1 | First-screen headline. It follows the web-hero formula "[the moment] + [what stays]" (`message_guideline.md:140-141`) and gives step 1, the moment. The green on "The evidence stays." marks the turn (`decision_log.md:23`). |
| `site/demo.html:243`, walkthrough step 4 h2 | The payoff after the reader has used a card. The same words come back once the reader knows what "evidence" means. |
| `site/propaganda.html:64`, core line under the title | Ties the strategy to the central message. Its rationale is at `propaganda.html:145-146`: it blames rotation so partners do not get defensive, and it "has to work in one reading". |
| `site/ad.html:69` (standee) and `site/ad.html:93` (A6 card) | Ad headline. It follows ad formula 2 (`message_guideline.md:152`), using steps 1, 3 and 5 (`:54`). |
| `site/linkedin.html:115`, post media line (Week 3 post) | Repeats the line across artefacts, as the rubric asks: "one coherent underlying marketing message across the deliverables" (`docs/brief/assignment_brief.md:266-273`). |

The line is not in the page title (`site/index.html:21`, "Sphyr: feedback from the people who saw the work").

## 3. Is it doing the job? `main` against the new version

What `main` used:
- **Headline/promise:** "Promote on merit, not politics." (`main:site/index.html:27`). The propaganda page names it as the line for "every artefact" (`main:site/propaganda.html:70`).
- **Tagline/core line:** "Built from everyone who actually worked with them, not one manager's memory. That's Sphyr." (`main:site/propaganda.html:71`). `framework_choice.md:26-30` itself calls this line a tagline.
- **Positioning statement:** "For founders of 50–300-person companies who sign off on promotions but can't see who did what, Sphyr is a 360-degree feedback layer alongside their HR system that lets them promote on merit, not politics, because it pools two-minute anonymized ratings every fortnight from everyone an employee works with." (`main:site/propaganda.html:135`).
- Live gh-pages h1 matches `main` ("Promote on merit, not politics."), checked with one curl.

Test: read only the hero h1 and its first lede, as a head of talent at a consulting firm. Does the reader learn (a) who it is for, (b) what it is, and (c) why it matters?

| | `main` | new |
|---|---|---|
| (a) who | "For growing companies" eyebrow (`main:site/index.html:26`). Clear, but it is the wrong segment for a consulting head of talent. | Implied by "engagement" and "your consultants" (`site/index.html:66-68`). "Consulting" appears 0 times in the home page text. |
| (b) what | Lede: everyone who works with each person gives "two minutes of anonymous ratings, every fortnight", which are pooled (`main:site/index.html:28`). Clear. | Lede: "asks each engagement team about your consultants and keeps every answer" (`site/index.html:68`). Vague. There is no "feedback", "360" or "review". The positioning category "360 feedback" (`positioning.md:53`) appears 0 times on the home page. |
| (c) why | Instant: promotions run "on months of evidence, not one manager's memory". | Missing from the text. The only payoff is the faint SVG label "The whole year is in the file". |

Evidence from the one simulated first-time reader (n=1):
- "catchy but I had to read the side line to know what 'evidence' means. Evidence of what? Sounds legal at first." (`docs/handoffs/layman_report.md:29`, `:52`).
- "The first screen does not say 'performance review' or 'appraisal' in plain words." (`layman_report.md:25`).
- The reader did get it after scrolling (`layman_report.md:39`).

Verdict, adversarial:
- **`main` is faster.** In one screen it tells the reader what Sphyr is and why it matters.
- **But `main` would fail with this audience.**
  - It speaks to founders, not a head of talent.
  - It uses words the current guideline bans: "anonymous" (`message_guideline.md:75`) and a politics/fairness promise (`:76`).
  - "Not politics" implies the partners are political. A head of talent cannot forward that to partners. Main's own fallback note admits this risk (`main:site/propaganda.html:76`).
- **The new line is truer and fits the segment, and it travels well across all five artefacts.**
- **But as the home hero it relies on its lede, and the lede does not name the category or the outcome.**

So the problem is the hero pair, not the six words. A head of talent gets "what and why" faster from `main`, and gets "is this for my firm and is it true" only from the new version.

## 4. Recommendation

**Keep the line verbatim. Pair it with a plain lede that names the category and the record.** Replace `site/index.html:68` with, for example:

"Every two weeks, the people who saw a consultant's work give two minutes of feedback, and Sphyr keeps it all in one record."

Why this lede:
- It reuses the ad body line (`site/ad.html:79`, `:94`) and adds the word "feedback", which answers the reader's "evidence of what?". That keeps the two artefacts consistent.
- It covers step 2 (`message_guideline.md:49`) and the record.
- It adds no "X, not Y" contrast. The home page has none now, and the limit is one per page (`decision_log.md:84`).
- It leaves out the moment on purpose. The moment can be named "at most once per piece" (`message_guideline.md:100`, `decision_log.md:83`), and the hero already names it once, in the SVG label "Promotion round / The whole year is in the file" (`index.html:79`, shown again at `:87` in the phone version). An earlier draft of this lede ended "so partners calibrate with the whole year in front of them". That draft would have named the moment a second time. It would also have repeated the h2 at `index.html:204` ("Partners decide with the whole year of work in front of them.").
- Trade-off: the outcome then lives in the faint label. If the team wants the outcome in the text, move the moment from the label into the lede. Do not put it in both.
- It uses no word from the "never say" list. It still needs the humanizer pass like all other copy (`decision_log.md:84`).

## Out of scope

- The page title (`site/index.html:21`) does not carry the line or the category. That is fine, but it was not checked against the share-card rules.
- The payoff label "The whole year is in the file" is the faintest text on the first screen (`layman_report.md:33`). That is a design issue.
- `README.md:32` and `decision_log.md:139` call the tagline "Central message". A relabel (tagline, with the central message being `message_guideline.md:40`) would pre-empt the professor's "slogan, not guideline" critique. This touches canonical docs, so ask first.

## Final

1. **What it is.** A tagline: the compressed form of the central message. It is not a positioning statement (no target, category or alternative; `framework_choice.md:27-30`) and not a value proposition (it says what stays, not who gains). The central message proper is `message_guideline.md:40` plus the order at `:44-54`.
2. **What it does.** It is the first-screen hook on the home hero (`index.html:66`), the recall payoff in the walkthrough (`demo.html:243`), the strategy anchor in the propaganda page (`propaganda.html:64`), the ad headline (`ad.html:69`, `:93`) and the repeated LinkedIn line (`linkedin.html:115`). Together these give the rubric's "one coherent underlying message".
3. **Is it working?** As a cross-artefact anchor, yes. As the home hero, only partly.
   - `main` ("Promote on merit, not politics." plus a mechanism lede) tells a reader what Sphyr is and why it matters faster.
   - But `main` targets founders and uses words the guideline now bans.
   - The new hero lede does not say "feedback" or name the promotion outcome. The one simulated reader asked "evidence of what?" (n=1).
4. **Recommendation.** Keep the line verbatim and pair it with a plain lede at `index.html:68`: "Every two weeks, the people who saw a consultant's work give two minutes of feedback, and Sphyr keeps it all in one record." The moment stays in the hero label only, to keep the once-per-piece rule (`message_guideline.md:100`).

**Sources:**
- `docs/brief/assignment_brief.md`, `docs/brief/professor_feedback.md`, `docs/brief/communication_objectives_notes.md`
- `docs/strategy/positioning.md`, `docs/strategy/message_guideline.md`, `docs/decisions/decision_log.md`, `docs/handoffs/layman_report.md`
- `README.md`
- `site/*.html` on `iteration-a`, and `git show main:site/{index,propaganda,deliverables,ad,linkedin,how-it-works}.html`
- Course folder: `tasks/saas/positioning-statement/framework_choice.md`, `tasks/task05b-top-level-message/{task,research-notes,top-level-message}.md`, `resources/Product_Lifecycle_Management_Course_Notes.pdf`
- Live h1 via curl.

**Not checked:**
- I did not view the pages in a browser or at http://127.0.0.1:8830/. I read the HTML source only.
- I did not run the humanizer on the proposed lede.
- I did not test the proposed lede with a reader.
- I did not read the course lecture slides beyond a grep of the two PDFs in `pm/resources/`.
- I fetched only the live h1, not the full live pages.
- The layman evidence is one simulated reader.
