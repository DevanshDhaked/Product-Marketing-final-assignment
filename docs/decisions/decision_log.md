---
type: Decision Log
title: "Iteration A decisions"
description: "Decisions the team made for the final-assignment website iteration, newest first, each with its reason and what it changes."
tags: [decisions, iteration-a]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
---

# Iteration A decisions

Append new decisions on top. Do not edit an old decision; add a new one that replaces it and say which.

## 2026-11-25: Visuals on the propaganda page

- **Decision:** the propaganda page gets four visuals in the site's own style (inline SVG or HTML, no PlantUML, no external images): an audience map, a belief shift graphic with the tactics as the bridge, a channel table (cost, tracking, stage, deliverable) and a campaign flow linking post 1 and the standee, post 2, the walkthrough, post 3, the call and the pilot. Each visual replaces prose, so the page does not grow in words.

## 2026-11-25: Ribbon visual uses the original logo colours

- **Decision:** the strands and the end sphere use the logo's own colours (teal, orange, blue, yellow, green, pink, purple, red), identical in both themes. The sphere renders as the exact original logo. Replaces "Strand colours and look approved" (cool subset, no orange or red). Strands sit outside product frames, so orange and red there do not carry their product meaning.

## 2026-11-25: No research stamps on public pages

- **Decision:** no access dates ("accessed 2026-11-24"), ISO dates or "read on" notes on any public page. Sources are cited by name and year of publication only. Access dates stay in the docs.

## 2026-11-25: Hub numbering and a short propaganda page

- **Hub:** the deliverables hub lists "01 The website" (linking to the home page) before 02 to 04, so all four graded deliverables read as one set.
- **Sticky contents:** on the propaganda page, the "On this page" list stays visible while reading on desktop and highlights the section in view. On phones it becomes a small sticky bar under the nav showing the current section, which opens the full list.
- **Propaganda page:** cut from about 3,400 words to about 600. A summary card on top (audience, belief from and to, central message, tactics, channels, expected response), then one short paragraph for each point the brief requires (audience; belief; central message and reasoning; tactics and channels; why they fit; link to positioning; expected response). Everything else (persona shaping, limits, long sources, the long sequence and objections) stays in the strategy docs and the hub handoff report.

## 2026-11-25: Pricing section trimmed

- **Decision:** the pricing section was too large. Plan card: ₹149, "per employee per month, billed yearly, plus GST", "Same rate for every employee and firm size", four short bullets (a two-minute card every two weeks; a record for each person, ratings pooled; your firm's values on the cards; setup, training and support by our team), "Clients you invite to give feedback: free", and one example line "A 150-person firm pays ₹22,350 a month, plus GST". Pilot card: ₹25,000 one time, "12 weeks, up to 40 people", and one line "Comes off your first annual bill if you sign. If not, you keep your data."
- **Equal cards:** the plan and pilot cards are the same height on desktop.
- **Price reasons on the site:** the closed "How we set the price" toggle adds four plain lines: ₹149 against the cheapest dedicated review tool found (PerformYard, about ₹464 a seat), break-even at about 49 firms of 150 people, why the pilot runs six cycles (12 weeks), and that a price survey of heads of talent and partners decides whether ₹149 moves. This partly reverses "Price and pilot (gate 1b)", which kept the reasoning internal.
- **Moved out:** the bills table, OKRs, spreadsheet import and new-joiner billing stay in [pricing](../pricing/pricing_summary.md). The scorecard sits behind a small "What a pilot measures" toggle under the pilot card. The 02:09 stat moves to the proof section.

## 2026-11-25: Full-colour logo in nav and footer

- **Decision:** the nav and footer use the full-colour ribbon logo (`class="mark"`) in both themes, replacing the one-colour `mark--mono` variant. Checked on the light and dark backgrounds. The mono and white variants stay available for print and small-icon uses.

## 2026-11-25: Top navigation and pricing section

- **Nav:** a corporate SaaS style nav: logo, "How it works" (`index.html#how`), "For partners" (`#partners`), "Pricing" (`#pricing`), "Deliverables" (`deliverables.html`), the "See the 2-minute walkthrough" button and the theme toggle. On phones a menu button opens the links and "Deliverables" stays visible. Replaces the three-item nav.
- **Pricing section:** follows the graded one-pager's order. Plan card first: ₹149 per employee per month, billed yearly, plus GST; what is included (no AI); clients and other outside raters invited by email at no charge; example bills for 100, 150 and 300 people. Then a smaller "Getting started" pilot card: ₹25,000 one-time, 12 weeks, up to 40 people, credited to the first yearly bill; if the firm does not sign it gets its data and the rest is deleted. A "How we set the price" link opens the reasoning: the fee is the cost to serve a pilot (about 30 hours of setup, training and review at ₹809 an hour plus running costs, ₹25,324 to ₹25,965), list price for the same seats would lose about ₹9,500 per pilot, and a fee above cost would profit on a trial.
- **Why:** the old pricing section was hard to read; the old site's single card and the graded one-pager put the per-person price first.

## 2026-11-25: Gate 1b, homepage approved

- **Homepage:** `design-lab/home.html` is approved as the base for the site build, with these changes: the ribbon boxes say "Project 1 · 3 teammates" and so on; the first screen is trimmed to about 30 words (core line, one short sentence, the button; the rest moves below the fold); dates inside faux product frames become cycles ("Cycle 1" to "Cycle 6") and relative times, so no month name appears anywhere on the site.
- **Pilot scorecard:** four plain items (participation per cycle, number of different people giving feedback to each consultant, whether partners found something new, whether consultants found their record useful). The engagement-count item is dropped. The publishing line becomes "Results stay with your firm unless you agree to share them."
- **Build:** phase 2 starts with fresh agents: site-css first, then home, walkthrough, propaganda plus hub, posts plus ad in parallel, then a reviewer.

## 2026-11-25: Ribbon visual labels

- **Decision:** the engagement boxes in the ribbon visual say "Project 1 · 3 teammates" to "Project 4 · 3 teammates" instead of consulting engagement types ("Pricing review", "Market entry" and so on), which read as jargon unrelated to feedback.

## 2026-11-25: No month in public copy, no customer talk

- **Timing:** public copy names no month. It says "promotion time", "the promotion round" or "when partners calibrate", at most once per piece. The assignment does not require a date, and a repeated month became a tic and an assumption about every firm.
- **Humanized copy:** every visible word goes through the `humanizer:humanizer` skill, including approved strategy lines; only "The engagement ends. The evidence stays." stays verbatim. Per page: at most one "X, not Y" contrast, no triads as rhythm, no staged openers or one-line closers, no stacked fragments, no inflated words, no bold labels before sentences, no dashes. The phase 3 review counts these.
- **Customers:** public copy never claims customers and never announces that there are none. It shows proof built in the open: what every pilot measures, agreed before it starts, the 2018 pilot labelled exactly, and the pilot offer.

## 2026-11-25: Strand colours and look approved

- **Decision:** the ribbon strands use the cool logo colours (blues, teals, greens, violets, olive), never orange or red, which mean "could improve" and "destructive" in the product. The tonal green option is dropped. The warm palette and Newsreader headlines are approved as built in `design-lab/`.

## 2026-11-24: Limits on the untemplated skill

- **Decision:** the `untemplated` skill is used only for its anti-template rules (no hero plus three equal cards, no glow, nothing invented, no busy motion, one local answer per interaction, two designed modes, a phone layout of its own) and its measured checks (first-screen words, idle frames, changed share, contrast, phone overflow, reduced motion).
- **Not applied:** dithering of pictures (none anywhere), its type rule (Newsreader plus Manrope stays, no font change), its ban on boxes where product frames or the price block need them, and its named directions.

## 2026-11-24: Price and pilot (gate 1b)

- **Price:** ₹149 per employee per month, billed yearly, plus GST, the same for every firm size. This is the graded submission's price. The pricing work showed ₹149 passes the stated rule (cost floor ₹121 at 80% gross margin, at or below the low-case value ₹209). It needs about 49 firms of 150 to break even, against 35 at ₹199.
- **Pilot:** 12 weeks (6 fortnightly cycles), up to 40 people, ₹25,000 plus GST (the cost to serve), credited against the first bill if the firm signs. If it does not sign, the firm gets its data as a CSV and the rest is deleted. Only the length changed from the graded six weeks, because three cycles are too few for a usable signal.
- **Not adopted (scope):** the conditional refund, the early-customer price lock and the January start push. The final brief asks only that the site present pricing and packaging consistently and make the value understandable (brief section 3, rubric line "pricing, packaging, acquisition and engagement integration"). The reasoning that answers the pricing feedback stays in [pricing](../pricing/index.md) as internal backing.

## 2026-11-24: Typeface and colour base

- **Typeface:** Newsreader (SIL OFL 1.1) for display headlines, Manrope (SIL OFL 1.1) for body and UI. The team asked for the font that best fits the product and the segment. An editorial serif reads as credible to management consulting partners and heads of talent, who live with serif-set reports and decks. Bricolage Grotesque read as too loud and Apfel Grotezk as too quirky for that buyer. Playfulness comes from the ribbon motif, not the type.
- **Colour base:** warm neutrals, light theme first. The blue-white `#F6FAFD` and navy `#040A16` from the prototype read as a generic AI palette and are replaced by warm paper and warm charcoal. Product greens stay for actions and positive states. Faux UI frames may keep the prototype's own colours because they show the real product.
- **Replaces:** the phase 1a tokens and the open typeface item in "Site structure" below.

## 2026-11-24: Site structure

- **Pages:** home (`index.html`, folds the old how-it-works, trust and pricing), the 2-minute walkthrough (`demo.html`), a deliverables hub (`deliverables.html`) and three deliverable pages (`propaganda.html`, `linkedin.html`, `ad.html`). Six pages in all, minimal links on each.
- **Second call to action:** "Book a 20-minute call" opens an honest note: "Course project: in a live launch this books a 20-minute call with our team." No email address is published.
- **Old URLs:** `how-it-works.html`, `pricing.html` and `trust.html` are dropped without redirects. The README links are updated to the new pages.
- **Open:** the headline typeface (shortlist in `design-lab/type.html`), and whether the pricing reasoning needs its own page.

## 2026-11-24: Ad placement chosen

- **Decision:** the one advertisement is a paid sponsor standee (portrait roll-up) with matching A6 handout cards, placed at an HR community event of the kind run by NHRD Network chapters, in the December to January window before the April round. It tracks nobody: no pixel, no badge scan, no form; a QR code opens a plain URL for the 2-minute walkthrough.
- **Naming:** the ad page does not name the specific real event (research found HR Showcase 2026, NHRD Bangalore, 4 to 5 Dec 2026). It describes the placement generically and says "planned", not "booked". No endorsement by any body is implied.
- **Why:** advertising means money is involved ([class notes](../brief/communication_objectives_notes.md)); the event standee was the best verified paid option that reaches heads of talent among peers without tracking. Both newsletters measure clicks per subscriber ([research](../handoffs/admedium_report.md)).
- **Replaces:** the LinkedIn Sponsored Content ad with retargeting on `main` (`site/ad.html`). Its reasoning layout (medium, audience, message, benefit, visual, call to action, journey stage) is kept as a content pattern only.
- **Fix needed:** the channel plan lists SHRM India's 2026 conference (26 to 27 Nov 2026), which falls before the selling window; drop or move that row.

## 2026-11-24: Simple site, new information architecture

- **Decision:** the current site on `main` is a content reference only, not a design or navigation reference. The team finds it confusing and hard to navigate, with too many links.
- **Direction:** simple and clear, yet pleasing and opinionated to look at, not a generalized average website. Use the fewest pages and links that still meet the brief: the website as hub with clear links to the propaganda strategy, the three LinkedIn posts and the ad, plus the 2-minute walkthrough.
- **Replaces:** the phase 2 page split in [the plan](../plan/iteration_a_plan.md) (nine existing pages) until the new page list is approved at gate 1b.

## 2026-11-24: Design direction for phase 1b

- **References:** study Awwwards and similar galleries for comparable products (HR tech, people analytics, feedback tools, editorial B2B SaaS) and borrow named patterns.
- **Logo:** use the ribbon-sphere logo in a playful way (motif, assembly, ribbons as the people around a consultant). It may be recoloured (all white, dark, mono) if the sphere stays recognisable and its ribbon sections stay distinct.
- **Type:** not limited to Google Fonts, not excluding them. The font must be free to self-host on a public site, with its licence recorded.
- **Skills:** use `design-taste-frontend` and `stageshow`. The prototype's UI language stays inside faux UI frames. Light and dark themes with the toggle stay.
- **Replaces:** the phase 1a choice of Manrope as the only font is open again.

## 2026-11-24: Gate 1a results

- **Central message and positioning approved:** "The engagement ends. The evidence stays." with the vision and product lines in [positioning](../strategy/positioning.md). Condition: all copy must read as written by people. Run every piece of public copy through the `humanizer:humanizer` skill before it ships.
- **Persona use approved:** the brief grades persona use, not a persona deliverable (brief lines 66, 129, 170, 330, 351). Kavya, Vikram and Meera stay an internal base that shapes copy, channel and call to action. They are named only in the propaganda strategy's audience section, not on a site page.
- **Three LinkedIn posts approved** as mapped in [the deliverable map](../strategy/deliverable_map.md).
- **Ad medium reopened:** the professor's class notes ([communication objectives](../brief/communication_objectives_notes.md)) define advertising as the push route where "money is involved". A free event poster would be word of mouth or PR, not an advertisement. The ad should be a small, paid, non-invasive placement. The exact placement is open until specific events or slots are verified with dates and prices.

## 2026-11-24: Segment definition confirmed, persona, ad medium, plan approved

- **Segment:** the consulting definition below is confirmed by the team. It replaces the "proposed" status.
- **Primary persona:** the head of talent (champion), who finds Sphyr, runs the pilot and takes the case to the managing partner. The managing partner is the secondary buyer persona. Meera, a senior consultant, is the person being rated.
- **Ad medium:** the brief asks for "one advertisement designed for an appropriate medium and audience", not a LinkedIn ad. Only the three LinkedIn posts must be on LinkedIn. The strategy work proposes the ad medium with its reasoning, and the team approves it at gate 1a.
- **Plan:** [the iteration A plan](../plan/iteration_a_plan.md) is approved. Phase 1a starts.

## 2026-11-24: Segment is consulting (exact definition proposed, awaiting confirmation)

- **Status:** the team chose consulting. The exact definition below is a proposal until the team confirms it.
- **Decision:** the canonical segment is homegrown, partner-led Indian management and strategy consulting firms of about 40 to 400 professionals. The managing partner is the buyer, the head of talent is the champion, and Meera, a senior consultant, is the person being rated. IT and tech consulting are out.
- **Why:** the course assigned Team 3 the consulting domain (`tasks/saas/positioning-statement/task.md`, 5 Oct). The professor's feedback asks for a personal journey and a message a junior copywriter can use, and a narrow, concrete segment serves both. The definition comes from `tasks/saas/positioning-statement/positioning-onepager.pdf`.
- **Replaces:** the live site's segment (founders of 50 to 300 person IT services firms, Meera as Head of People) and the graded 29 Sep segment (founder-led product IT, 30 to 500, Rohan).
- **Changes:** the website copy, persona, journey, propaganda strategy, all three LinkedIn posts, the ad and the pricing inputs.

## 2026-11-24: Pricing follows the feedback and the math

- **Decision:** keep a flat per-employee model. Re-derive every number for consulting: the value per employee, the competitor comparison on named plans, the margin floor, fixed costs, contribution, break-even, the pilot amount, its length and what happens if the firm does not convert, and how Van Westendorp results set the final price. If the math no longer supports ₹149 or the ₹15,000 six-week pilot, the number changes.
- **Why:** pricing scored 70/100 because the key numbers had no supporting logic ([feedback](../brief/professor_feedback.md)).
- **Gate:** the re-derived numbers are shown to the team before any site change.

## 2026-11-24: Visual direction is light and dark with a toggle

- **Decision:** the site supports a light and a dark theme with a visible toggle. It should stop reading as AI-made. Grading is on message and reasoning; looks only make an impression (brief line 12).

## 2026-11-24: Source PDFs stay out of the repo

- **Decision:** `docs/` holds markdown digests that quote and cite sources. It does not copy the professor's whitepaper, the product documentation or the graded PDFs. The repo is public.

## 2026-11-24: Working branch and deploy

- **Decision:** all iteration work happens on the `iteration-a` branch. Commits are made per logical group. A person on the team pushes and redeploys `gh-pages`; agents do not push.
