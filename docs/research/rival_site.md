---
type: Research
title: "Other team's Sphyr site: what they do better, what we do better"
description: "Assessment of Team 01's Sphyr site (creative studios segment) against our v2, scored with the v2 baseline rubric and the professor's 2026-11-26 yardstick."
tags: [research, competitor, aida, design, v3]
sources:
  - url: "https://sphyr-website-lilac.vercel.app/"
    title: "Sphyr (Team 01) home"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary (the site itself)"
  - url: "https://sphyr-website-lilac.vercel.app/pricing.html"
    title: "Sphyr (Team 01) pricing"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary"
  - url: "https://sphyr-website-lilac.vercel.app/trust.html"
    title: "Sphyr (Team 01) trust and privacy"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary"
  - url: "https://sphyr-website-lilac.vercel.app/why-sphyr.html"
    title: "Sphyr (Team 01) why Sphyr"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary"
  - url: "https://sphyr-website-lilac.vercel.app/how-it-works.html"
    title: "Sphyr (Team 01) how it works"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary"
  - url: "https://sphyr-website-lilac.vercel.app/start-a-demo.html"
    title: "Sphyr (Team 01) start a demo"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary"
  - url: "https://sphyr-website-lilac.vercel.app/guides.html"
    title: "Sphyr (Team 01) guides (4 live guides, 7 placeholder links)"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary"
  - url: "https://sphyr-website-lilac.vercel.app/ads/ad-1.html"
    title: "Sphyr (Team 01) advertisement 1 and Team_01_advertisement_01.pdf"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary"
  - url: "https://sphyr-website-lilac.vercel.app/linkedin/post-1.html"
    title: "Sphyr (Team 01) LinkedIn posts 1 to 3 and their PDFs"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary"
  - url: "https://devanshdhaked.github.io/Product-Marketing-final-assignment/v2/"
    title: "Our Sphyr v2 home (compared through v2_baseline and site/ on iteration-b)"
    published: "2026"
    accessed: 2026-11-26
    kind: "primary"
  - resource: "docs/research/v2_baseline.md (rubric, v2 scores, v2 section map)"
  - resource: "docs/brief/professor_feedback.md (addendum 2026-11-26)"
  - resource: "docs/design/slop_rules.md, docs/product/do_not_claim.md"
  - resource: "site/index.html, site/css/*.css, site/linkedin.html on iteration-b (b6051be)"
generated: { by: claude-code/opus-5-5, at: 2026-11-26T10:20:00Z }
---

# Other team's Sphyr site

## Method
- Text: downloaded all 16 reachable pages (home, how it works, pricing, guides plus 4 guides, why Sphyr, trust, start a demo, the placeholder page, ad 1, LinkedIn posts 1 to 3) and the 4 PDFs (ad, 3 posts). Extracted visible text with a script.
- Look: Playwright at 1280 by 800 (first screen, full page after a scroll-through, one mid-page viewport) and 375 by 812 (first screen), default light theme. The first full-page capture showed large blank zones; scrolling the live page showed the content is there (reveal on scroll). Blank zones are a capture artifact, not a reader-facing defect. The 375 full-page capture started mid-page and is not used as evidence.
- Our side: `docs/research/v2_baseline.md` plus greps of `site/` on iteration-b, which the baseline says carries v2 unchanged. Our v2 was not opened live in a browser for this note.
- All scores and design judgements are one auditor (n=1). No reader from either segment was asked.

## What they do
Team 01 sells Sphyr to founders of growing creative companies (25 or more people: design studios, creative agencies, production houses, animation studios), with prices in rupees plus GST, so India is implied but not stated on home. The message is "Easy appraisals. Better culture.": feedback from everyone who sees the work, two minutes a fortnight, so founders "back the right people with confidence". Home runs hero, an illustrated seven-scene story ("Meet Meera", labelled illustrative), a problem accordion, how it works with a collage of prototype screens, a brand marquee, a trust strip and a free-demo close. The offer is a free 90-day demo for one team of up to 25, "no card, no automatic upgrade". Graded parts: one meme-format ad, three LinkedIn posts in mocked LinkedIn frames, a full pricing page with a calculator and billing terms, and no separate campaign or propaganda page (the 4 guides and the demo kit do some of that job). Course artefacts sit in the buyer's nav ("LinkedIn", "Ads"), as our "Deliverables" does.

## First-screen score (rubric from v2_baseline section 1)
Reader swapped to their segment: a founder of a 25+ person Indian creative studio.

### Home at 1280 (`rival_home_1280_first.png`)
Text in frame: kicker "Sphyr · Appraisals for growing studios and teams"; H1 "Easy appraisals. Better culture."; lede "Sphyr gathers two minutes of feedback a fortnight from everyone around each person, so you can back the right people with confidence."; buttons "Start a free demo", "Try the feedback card"; "One team, 90 days, no card, no automatic upgrade."; "For growing companies with teams of 25 or more, starting with design studios, creative agencies, production houses and animation studios."; right card "For founders. Know who really carries your studio."

| Question | Score | Why |
|---|---|---|
| (a) What | 3 | "Appraisals" in kicker and H1, the mechanism in the lede. |
| (b) Who | 2 | Firm type, size and buyer ("For founders") are all in frame. No country in frame (rupees appear only on pricing). The baseline docked us for missing country, so the same bar docks them. |
| (c) Next | 3 | One action, "Start a free demo", with the risk terms under it. |
| Total | 8 of 9 | Ours: 6 of 9 (baseline). The gap is (b): they name the firm type, size and buyer; we name none. |

At 375 (`rival_home_375_first.png`) the "For growing companies..." line sits at the fold edge and the "For founders" card is below it, so (b) falls to about 1 there (estimate).

### Ad, headline and first line only (same frame as the baseline's 3 of 9)
Headline "Nobody: your manager in appraisal week:"; first line "So... what did you work on in March?"

| Question | Score | Why |
|---|---|---|
| (a) What | 1 | Appraisal is named, the product is not. |
| (b) Who | 1 | Speaks as the employee, not the founder who buys. |
| (c) Next | 0 | No step in frame. |
| Total | 2 of 9 | Ours: 3 of 9. |

Whole ad (`rival_ad1_1280_full.png`): adds "Easy appraisals. Better culture.", "Sphyr asks the people who actually saw the work. Two minutes a fortnight.", "Start a free demo" and "One team of up to 25 people, 90 days, no card required": about 2, 1, 3 = 6 of 9. The rubric undersells it on one point: the meme headline is a real Attention line (stop power), which the professor said our ad lacked. The rubric measures clarity, not stopping.

## AIDA map of their home
| # | Section | Tag |
|---|---|---|
| 1 | Hero: what, who, demo, risk terms, "For founders" card | A, passes |
| 2 | "When good work goes unseen, good people leave": Meera in 7 illustrated scenes, ending with Sphyr | I (problem told as a story, then the fix) |
| 3 | "Not a new boss. A fuller picture." dark card with demo button | I to A (first Action, early) |
| 4 | "Your studio has grown past what one person can see": 3-row accordion | I (back to problem) |
| 5 | How it works, "Know who to back. Decide with evidence.", prototype collage | I (how it works) |
| 6 | "Credit follows contribution" marquee with 3 values | I (brand, weak) |
| 7 | 2018 paper pilot line, trust strip ("Anonymous by default", "Clients take part free", "No activity tracking") | I (assurance) |
| 8 | "Try it with one team.": 90 days, no card, no auto upgrade, demo kit, results report | D then A |

The journey is in order at A and at the D/A close. It breaks at row 4, which returns to the problem after the first Action, the same fault as our row 6. Home is about 1,100 words of content against our 1,810.

## They do better
| Point | Evidence | What it means for our v3 |
|---|---|---|
| Hero names buyer, firm type and size | Home hero: "For founders", "teams of 25 or more, starting with design studios, creative agencies..." | Name managing partner or head of talent and "40 to 400 person consulting firms" in frame. |
| Risk terms under every call to action | "One team, 90 days, no card, no automatic upgrade." under the hero, mid-page and close buttons (extracted home text, lines 45, 89, 197) | Matches the course notes (D: no payment friction; I: assurance). Put our pilot terms in one short line under each call. |
| Copy uses the segment's own scenes and roles | "A motion designer might work for four leads in a quarter"; post 2 "The campaign shipped on Friday. The appraisal said, 'Delivered on time.'"; producer, editor, client approval | The professor's point 5 done for their segment. Our equivalent is engagement manager, staffing, case team, client deliverable, year-end review. |
| Design speaks the segment's language | Pastel illustrated scenes, playful serif, neon meme ad (`rival_home_1280_story.png`, `rival_ad1_1280_full.png`) | A creative studio would read this as theirs. The professor's test for us is the reverse: our look must read as a consulting vendor, not a studio. |
| Ad has an Attention line | "Nobody: your manager in appraisal week" in large condensed type on neon green | Our ad needs a headline that stops a scroll before it explains. |
| LinkedIn posts give the reader something to keep | Post 1 is a three-column checklist to try on one finished project; post 2 is a scene; post 3 a coaching example | Matches "what they are on LinkedIn for". A save-worthy tool post fits our segment too. |
| Pricing and packaging are complete | Pricing page: per covered employee, monthly and yearly, minimum 25 seats, GST, proration, refund on unfixed issues, slider calculator | Our v3 pricing block should answer seat definition, minimum, tax and exit in plain terms. |
| One label per action | "Start a free demo" on every button (the nav says "Start a demo") | We had "See the 2-minute walkthrough" 6 times plus "Book a 20-minute call"; pick one primary label. |

## We do better
| Point | Evidence | What it means for our v3 |
|---|---|---|
| Privacy claims match the product | Ours, `site/index.html:299`: "Managers approve requests to edit feedback that has already been sent, so they can see who asked to edit feedback about whom." Theirs, trust page: "Nobody, not your manager and not HR, sees who wrote what", plus "Enough voices first" and "Notes released in batches". These are not supported by the product sources (do_not_claim item 6; PROTO 3.7 shows edit approvals). | Keep our accurate line. Do not copy their stronger anonymity promise. |
| No invented social proof | Their 3 post PDFs show reactions and counts (post 1: 218, 34 comments, 45 reposts; posts 2 and 3: 142, 28 comments, 19 reposts, the same numbers). `grep` finds no such counts in our `site/linkedin.html`. | Keep mocks free of reaction counts, or label them as sample. |
| Product scope stays inside the sources | Theirs lists "'Who should we promote?'" among plan features (pricing) and as a how-it-works section; do_not_claim item 16 says it is described, not a prototype screen. Their collage uses prototype demo names (Maya Chen, Northstar), item 17. | Keep labelling described features and avoid demo names. |
| Page at rest | Their home CSS has `wm-roll 70s linear infinite` (the "Credit follows contribution" marquee). `grep infinite site/css site/js` on ours: 0 hits. | Keep the still page. |
| Fewer AI-landing tells | Theirs: about 8 uppercase, letter-spaced kickers on home ("FOR FOUNDERS", "WHAT CHANGED", "FREE DEMO"...), bento hero cards, an orange full stop on every headline, about 7 "X, not Y" lines on home ("Credit follows contribution, not visibility."; "Not a new boss. A fuller picture."), a staccato triad ("One person. One year. One sitting."). Ours: uppercase only inside product frames (`site/css/base.css:357, 392`), which slop_rules allows. | Keep our rules; their look is clean but carries the tells our rules ban. |
| No dead ends | They link 11 distinct placeholder pages ("under-development.html": product demo, release notes, whitepaper, privacy policy, security overview, contact sales, 4 guides, suggest a topic), and the demo form says "This form isn't connected yet". | Every link and the demo path on our v3 must lead somewhere real. |

Both sites post LinkedIn as the company page, not a person, and both put course artefacts in the buyer's nav. Neither is a gap between us.

## Design verdict
Not sloppy. It is a coherent, competent system: one serif display face and one sans, warm off-white, one orange accent, consistent pill buttons, real prototype screens labelled "names and numbers are sample data", a theme toggle, no sideways scroll at 375 (scrollWidth 360 within a 375 viewport). The illustrated story and the meme ad fit a creative-studio buyer, which is the holistic fit the professor asked of us. The weak points are template tells and loose ends, not craft: tracked uppercase kickers, pastel bento cards, a looping marquee, the orange-dot headline device on every heading, a truncated author line in the post mock ("Everyday pe"), blank thumbnails for posts 2 and 3 in the post sidebar, and 11 placeholder pages. For a consulting buyer this look would be wrong; for theirs it mostly works.

## What this means for v3
- Put the buyer role, firm type and size in the hero frame, as they do; this alone moves our (b) from 1 toward 3. Add "Indian" if we want the full 3.
- Put a one-line pilot risk statement (terms, length, no payment) under every primary call to action. Pattern only; use our own pilot terms.
- Make the ad headline a scroll-stopper drawn from a consulting moment, then name the product and the step in the first lines. Their meme shows stop power but scores 2 of 9 on clarity; we need both.
- Build at least one LinkedIn post as a tool the reader saves (a checklist or table for the year-end review), in consulting roles.
- Do not follow them on privacy promises, reaction counts on mocks, "Who should we promote?" as a feature, loops, or placeholder links; each is a place where we are already stronger.
- Use segment scenes the way they use "a motion designer might work for four leads in a quarter": one concrete consulting staffing line beats a general statement.
