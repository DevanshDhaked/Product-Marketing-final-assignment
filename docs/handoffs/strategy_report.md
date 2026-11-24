---
type: Handoff
title: "Strategy teammate report, phase 1a"
description: "Plan, progress and final summary from the strategy work: files and commits, insights with sources, decisions, rejected approaches, open questions and unverified items."
tags: [handoff, strategy]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T17:11:40Z }
---

# Strategy teammate report, phase 1a

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Status (2026-11-24): done. All 9 files written and committed on `d1-strategy` (last commit 2f3a4b7). Validator 0 errors. Feedback points covered: 7 of 7. Waiting for gate 1a review. See `## Final` at the end.

Worktree: `Product-Marketing-final-assignment.d1-strategy`, branch `d1-strategy` from `iteration-a` (eeb4c1c).

Read so far: docs/index.md, decisions/decision_log.md, brief/ (assignment brief sections 1 to 4, professor feedback, gap map), product/do_not_claim.md, product_facts.md, evidence_and_claims.md, prototype_screens.md (My Sphyr), prior_work/source_conflicts.md and research_backing.md (headings and key rows), plan/iteration_a_plan.md, and in the course folder tasks/saas/positioning-statement/ (professor_lens, consulting_segment, consulting_pain, positioning_drafts, positioning_options_v3, decisions_pending, alternatives_and_competitors).

## Plan

### Success number

Professor feedback points in my scope answered with a file and section: target 7 of 7 (list below). Validator errors: target 0.

### Feedback coverage table (my scope)

| # | Feedback point | Answered in |
|---|---|---|
| F1 | Journey column must be "Can we do anything about it?", not "Relevant" | journey_map.md, every stage table, column "Can we act on it?" (Yes / Partly / No plus action) |
| F2 | The "company outgrows what one person can see" touchpoint: can we act on it? | journey_map.md, stage 1 "Trigger", explicit answer: No on the growth itself, Yes on the moment it becomes visible (second office, a partner calibration fight, a strong exit) |
| F3 | Social proof when the product is new and has no reviews | journey_map.md, stage "Seeking validation"; detail in acquisition_engagement.md section "Proof without reviews" |
| F4 | Journey is detailed but not personal | persona_head_of_talent.md (whole file) and journey_map.md written in first person per stage, with feelings and stakes |
| F5 | Message is a slogan, not a guideline for a junior copywriter and designer | message_guideline.md (whole file) |
| F6 | No money and no creepy, privacy-invading marketing: how do channels change? | channel_plan.md (whole file), plus segment.md "How to find them" |
| F7 | Positioning "too focused on the present", needs product plus vision | positioning.md |

Out of my scope and left to others: pricing (6 points, pricing teammate) and packaging (3 points, first_use teammate). Segmentation and persona had no specific comment but sit under the 63/100 combined grade, so segment.md and the personas cover them.

### Rules every file follows (later teammates inherit these)

1. Quotes from the head of talent, managing partner and Meera are illustrative composites. Each file labels them so. They must never appear on the site, posts or ad as testimonials (do_not_claim item 8).
2. Employee review quotes (AmbitionBox, Reddit) are used unattributed as "employee reviews of homegrown Indian consulting firms", never with names.
3. No partner or head-of-talent interview exists. Buyer language in both personas is marked as a hypothesis to test.
4. The "Who Should We Promote?" leadership screen is not in the prototype. The managing partner pitch uses screens that exist: manager team insights, member insights, participation, the 7 parameters, fortnightly trends.
5. The 2018 pilot is always "a 2018 paper-and-pen pilot run by Sphyr's founder in four companies". Safest stat: 2 min 09 s per card for a 14-person sphere. No other pilot percentage is used as a software result.
6. Anonymity line: "ratings are pooled and comments are anonymized to the person rated". Never "anonymous to everyone".
7. Client raters: the prototype shows an "External" group in My Sphyr (for example "Client Partner") and an "Invite to My Sphyr" button; DOC p5 says external people are invited by email. So client raters may appear, but only as "the partner opts the client in", never as a headline.
8. Pilot price and length are owned by the pricing teammate (phase 1b). My files say "a paid pilot" and do not fix rupees or weeks. I flag the known conflict: a 6-week pilot is 3 fortnightly cycles, while the sources say about 6 cycles (12 weeks) are needed for a usable signal (source_conflicts.md row 11). I do not resolve it.
9. Timing: appraisals land April to June, so the selling window is November to January. Today is 24 November 2026. Channel sequencing and the journey trigger use this.
10. Sources: external facts get a URL and access date 2026-11-24. The load-bearing ones are re-fetched with firecrawl or exa (India consulting market size, Primus 400+, SPI 2025 tables, typical engagement length and team size). Gallup, Scullen et al. and foundit came "via team answers"; I trace each to a primary source or mark it second-hand.

### Files in docs/strategy/

Each is an OKF v0.2 concept file with frontmatter, plus `index.md` and `log.md` for the folder. I load `hack-kit:okf-docs` before writing and only rebuild the index for `docs/strategy`.

**1. segment.md.** Purpose: the confirmed segment with its reasoning.
- Definition (confirmed 2026-11-24): homegrown, partner-led Indian management and strategy consulting firms, about 40 to 400 professionals. Earlier draft also had "offices in 2 or more metros"; I keep it as a strong signal, not a hard filter. Open question Q1.
- Why the pain is sharpest here: work in 6 to 12 week engagements, people rotate across 4 or more a year, work happens at the client, one April to June decision, partner memory and proximity, the bench.
- Size: market size in USD (re-fetched) and an estimate of the number of firms in the band, built bottom-up from named firm lists and directories, marked as an estimate with its method.
- Buying unit: champion (head of talent), buyer (managing partner), veto holders (practice partners, consultants, clients).
- Anti-segment: under 40, MBB and Big 4, IT and tech consulting, staffing or body-shop firms, solo advisors.
- How to find them without scraped lists: public firm websites and press, industry bodies, campus placement reports, alumni networks, events, newsletters people chose to receive.

**2. persona_head_of_talent.md.** Purpose: the primary persona, named and personal (working name "Kavya", head of talent at a 150-person Gurugram firm, Meera is one of her consultants; name open, Q2).
- Who she is in a paragraph, not a table. Her day in a week of November, with chasing project-end forms.
- Goals, fears, her own words (labelled composite).
- How she wins internally: what she must bring to the managing partner, who can veto her, what makes her look good or exposed.
- Her stakes at each journey stage (short table that points to journey_map.md).
- What she must never hear from us (surveillance, "replaces partners").

**3. persona_managing_partner.md.** Purpose: shorter secondary buyer persona.
- What he fears (losing good juniors to MBB and Big 4, calibration fights, partiality exits), what he needs to hear to sign, the questions he will ask, what proof he accepts, what makes him say no. Buyer language marked as hypothesis.

**4. journey_map.md.** Purpose: walk in Kavya's shoes from trigger to renewal.
- Opens with the Meera story in two paragraphs so the reader cares.
- Stages: trigger, naming the problem, looking for answers, seeking validation, making the case to the partner, paid pilot, first appraisal on Sphyr, renewal.
- Per stage columns: what she does, what she thinks and feels (first person), touchpoint, problem, "Can we act on it?" (Yes / Partly / No), and what Sphyr or the team does.
- F2 answered directly: growth itself is No; the moment the gap shows is Yes, and we meet it there with the right content.
- F3 answered directly: substitute proof on day one. Candidates: the method in public (how cards, spheres and pooling work, with a demo anyone can click), the 2018 founder pilot labelled honestly, a small design-partner or paid-pilot cohort with a published scorecard (what we will measure and report, set before the pilot), peer references from that cohort, borrowed research credibility.
- Post-purchase rows start after first use. Encounter to first use belongs to first_use; I point to their file.

**5. positioning.md.** Purpose: one statement that mixes product and vision.
- Vision half from the professor's own words (recognition earned, not politicked; quiet contributors seen; a voice for everyone; growth over judgement). I will draft 2 or 3 candidates built from options v3 (E3, V3, G3 family) and the consulting anchor "The engagement ends. The evidence stays.", and recommend one. Open question Q3.
- Named alternatives: the year-end appraisal from memory, one manager's project-end form, HRMS review modules (Keka, Darwinbox), global suites (PerformYard, Lattice) with what each lacks.
- Differentiation that survives comparison: fortnightly rhythm on by default while the team is still together, two-minute one-tap cards, the consultant's own sphere including opted-in clients, many pooled raters. Not lead claims: "continuous", "360", "client feedback", "project-based" (competitors claim them).
- Reason to believe, value discipline (one, stated), and what Sphyr is not.

**6. message_guideline.md.** Purpose: something a junior copywriter and designer can execute.
- Core idea in one line.
- Always-say order: the moment, the mechanism, the result, then the vision line.
- Claim and allowed proof table.
- Never-say list (from do_not_claim and alternatives: anonymous, unbiased, objective, ends favouritism, replaces HR or partners, AI, real-time, tracks productivity, named customers, reviews).
- Tone and vocabulary: consulting words (engagement, partner, calibration, staffing, bench, promotion round), not HR jargon (VBA, sphere score, ONA, talent management suite).
- Headline formulas with 3 worked examples each for web hero, LinkedIn post opener and ad.
- Per-audience variants: head of talent, managing partner, consultant.
- Visual rules: show the consultant's record running across fading engagements and real prototype cards; never show faces being scored, surveillance dashboards, stock handshakes.
- Do and don't table.

**7. channel_plan.md.** Purpose: zero budget and non-creepy first.
- Layer 1, zero budget: founder-led and team-led LinkedIn organic, the professor's own network, alumni and partner networks, consulting community events and newsletters people subscribe to, the public method page and demo, peer references from the pilot cohort.
- Each channel: why it fits Kavya or the partner, which stage it serves, what we never do there.
- Explicit bans: retargeting, scraped lists, cold mass email, buying contact data, pixel tracking.
- Layer 2, optional small paid layer with spend caps and consent rules (for example a sponsored newsletter slot or an event stall). Cap and amount marked as estimates.
- Sequencing November to January.

**8. acquisition_engagement.md.** Purpose: how firms are reached and how the relationship stays useful.
- How a firm first hears of us, the single meaningful next step (one CTA, proposed: try the live demo, then a short call with the head of talent; to be confirmed, Q4).
- Proof without reviews (detail for F3).
- After the first touch: what we send and only with consent.
- After purchase, starting after first use: real product moments only (fortnightly cycles and reminders, member insights trends, manager team insights, participation, the April calibration).
- Boundary note: anything between first encounter and first use is first_use's scope.

**9. deliverable_map.md.** Purpose: one central message and each artefact's job.
- Central message, then a row each for website, propaganda strategy, LinkedIn post 1, 2, 3, the ad: job, belief it shifts, angle, journey stage, CTA, channel.
- LinkedIn posts: three different jobs (provoke the problem, show the mechanism, invite to proof), not one message three times.
- Ad medium: 2 or 3 candidates scored on zero budget, non-invasive, persona fit and brief fit (for example a print or digital slot in a consulting community newsletter, an event poster or standee, a placement-week or alumni magazine slot). I recommend one; the team decides at gate 1a.

### Order of work

1. Research and source re-fetch (segment numbers, firm-count estimate, channel facts such as named communities and newsletters).
2. segment.md, then both personas.
3. journey_map.md and positioning.md.
4. message_guideline.md, channel_plan.md, acquisition_engagement.md.
5. deliverable_map.md last, since it draws on all of the above.
6. index.md, log.md, validator to 0 errors. Commits per logical group: research and segment, personas, journey, positioning and message, channels and acquisition, deliverable map, index and log.

### Open questions for the lead

- Q1: Keep "offices in 2 or more metros" as a hard part of the segment, or only as a signal? I propose signal only, since the confirmed definition leaves it out.
- Q2: Name for the head of talent persona. I propose "Kavya". Gender: the brief says "she"; the managing partner "he". Confirm.
- Q3: Do you want me to recommend one positioning statement, or present 2 or 3 for the team to pick at gate 1a? I propose: recommend one, list the two runners-up.
- Q4: The single CTA across all artefacts. I propose "try the live demo" as the low-commitment step, with "book a 20-minute call" as second step. Confirm or change.
- Q5: May I name real Indian consulting communities, newsletters and events in channel_plan.md (after checking they exist), or keep them as types?
- Q6: Time budget. Deadline is 27 November 23:59. I assume this phase should land within about 4 to 6 hours of work. Tell me if it is less.

## Progress

### 2026-11-24: plan approved

Lead answers: Q1 metros are a signal, not a filter. Q2 Kavya (she), managing partner (he). Q3 recommend one statement, list two runners-up. Q4 primary CTA "the 2-minute walkthrough" on our own site (demo.html), never "live demo"; second step a 20-minute call with the head of talent. Q5 name real communities, newsletters and events only after checking they exist, with URL and access date, never implying partnership or endorsement. Q6 no hard time limit, quality first. New rule: the report ends with a `## Final` section (files with SHAs, key insights with sources, decisions and why, rejected approaches and why, open questions, what I did not verify).

### 2026-11-24: research step done

Verified on 2026-11-24 (curl, firecrawl, exa): Mordor India consulting market (USD 9.36 B 2026, 18.93 B by 2032; SMEs fastest growing); Primus Partners 400+ professionals (SMEStreet, Sep 2026); The Hindu homegrown firms article; strategycase "six to twelve weeks"; The Finance Story "4 to 5 projects", Deloitte April to March cycle, 1,000+ benched; Umbrex review components and calibration; AmbitionBox quotes (Primus 197 reviews, Avalon 264 reviews); Scullen et al. 62% and 53% rater variance vs 21% and 25% performance (via peopleanalyst summary; primary is J. Applied Psychology 85(6), 2000); Gallup 29% fair, 26% accurate, 14% inspired (gallup.com, 2017 article); foundit appraisal survey 24 Jul 2026 (52% actively looking, 37% of those well represented had a manager who actively advocated; sample size not stated in the release); Deloitte snapshots at end of each project or quarterly (ATD blog). Channels confirmed to exist: IMCI (imcindia.co.in, 8 chapters), NHRDN Delhi and NCR chapter (about 2,300 members), People Matters and TechHR India, SHRM India (shrmi.in), ETHRWorld daily newsletter.

Dropped: "36% call their appraisal effective" (foundit) could not be found in the 2026 release, so it is not used. AmbitionBox category averages could not be read reliably, so only verbatim review text is used. Firecrawl search returned off-topic results for several queries; exa hit its free rate limit; direct fetch with curl and Python worked.

### 2026-11-24: segment and personas landed

- segment.md committed 2217b20. Personas committed 7c34c16.
- Decision: in the persona story Meera is still at the firm and is the person being rated this year; the exit that triggers Kavya is a different composite consultant (Siddharth) who left last June. Reason: the October story had Meera leave, which would leave nobody to rate in the journey.
- Decision: the firm and all people are unnamed or fictional composites; no real firm name is used for Kavya's firm.
- Note: build_index.py with `--root docs` also writes the root docs/index.md. I revert that file after each run (`git checkout docs/index.md`), so the root index does not list docs/strategy yet. The lead must add it when merging.

### 2026-11-24: journey, positioning and message landed

- journey_map.md committed 22d4dc8. positioning.md and message_guideline.md committed 1920d33. Validator: 0 errors.
- Finding: PerformYard has a consulting page that claims "project-based review cycles", feedback "from clients, peers, and mentors", reviews aligned "to project or client engagement completion" and a "running record" (performyard.com, accessed 2026-11-24). It is the closest alternative. Sphyr's difference is therefore stated as rhythm (fortnightly by default while the team is together), effort (two-minute cards), the person's own circle, partners still deciding, and segment fit. "Project reviews", "client feedback" and "running record" must not be claimed as unique.
- Decision: recommended statement is a vision line plus a product line (IKEA shape). Runners-up B (a voice) and C (growth) listed with reasons.
- Interpretation to confirm: "a 20-minute call with the head of talent" is read as a call between our team and the prospect firm's head of talent.

### 2026-11-24: channels, acquisition, deliverable map and review fixes landed

- channel_plan.md and acquisition_engagement.md committed 2a43cc4. deliverable_map.md committed 68140fb. Review fixes committed 2f3a4b7.

## Final

**Success number: 7 of 7 professor feedback points in my scope answered, each with a file and section. Validator: 0 errors (3 warnings, all in files outside docs/strategy).**

### 1. Files written, with commit SHAs

All in `docs/strategy/` on branch `d1-strategy` (worktree `Product-Marketing-final-assignment.d1-strategy`).

| File | First commit | Later change |
|---|---|---|
| segment.md | 2217b20 | 2f3a4b7 |
| index.md, log.md | 2217b20 | every later commit |
| persona_head_of_talent.md | 7c34c16 | 2f3a4b7 |
| persona_managing_partner.md | 7c34c16 | |
| journey_map.md | 22d4dc8 | 2f3a4b7 |
| positioning.md | 1920d33 | 2f3a4b7 |
| message_guideline.md | 1920d33 | 2f3a4b7 |
| channel_plan.md | 2a43cc4 | 2f3a4b7 |
| acquisition_engagement.md | 2a43cc4 | |
| deliverable_map.md | 68140fb | 2f3a4b7 |

Feedback coverage (file and section that answer each point):

| # | Feedback point | Answered in |
|---|---|---|
| F1 | "Relevant" should be "Can we do anything about it?" | journey_map.md: "How to read 'Can we act on it?'" and the "Can we act on it?" column in every stage table |
| F2 | The "company outgrows what one person can see" touchpoint | journey_map.md: Stage 1 first row, and "The 'outgrows what one person can see' touchpoint, answered" |
| F3 | Social proof when there are no reviews | journey_map.md: Stage 4 and "Social proof when there are no reviews"; acquisition_engagement.md: "The pilot scorecard (proof without reviews)" |
| F4 | Journey is detailed but not personal | persona_head_of_talent.md (whole file, "Her week in late November", "In her own words"); journey_map.md: "Where the story starts" and the narrative plus quote that opens each stage |
| F5 | Message is a slogan, not a guideline | message_guideline.md, sections 1 to 11 |
| F6 | No money, not creepy: how do channels change | channel_plan.md: "Principles", "Never do", "Layer 1: zero budget", "Layer 2: optional small paid layer"; segment.md: "How to find them without scraped lists" |
| F7 | Positioning "too focused on the present" | positioning.md: "Recommended statement" (vision line plus product line) and "Why this one" |

Also covered without a specific comment: segmentation (segment.md) and persona (both persona files), which sat under the 63/100 combined grade.

### 2. Key insights and findings (with sources, all accessed 2026-11-24)

- **PerformYard is the closest competitor and already sells to consulting firms.** Its consulting page claims "project-based review cycles", feedback "from clients, peers, and mentors", reviews aligned "to project or client engagement completion", and a "running record" (https://www.performyard.com/performance-management-for-consulting, https://www.performyard.com/continuous-feedback). So Sphyr cannot claim project reviews, client feedback or a running record as unique. The difference that survives: a light fortnightly rhythm as the method's default while the team is together, two-minute cards, each person's own circle, partners still deciding, and fit with homegrown firms.
- **The prototype has no org-wide HR or leadership view.** Kavya's admin screens are configuration only. Partners see the record through manager "Member Insights" and "Team Insights". The persona and the guideline promise only that.
- **Client raters are real but partner-gated.** The prototype's "My Sphyr" has an "External" group (for example "Client Partner") and an "Invite to My Sphyr" button; the product guide p5 says external people are invited by email.
- **Engagements run six to twelve weeks** (https://strategycase.com/what-is-management-consulting/). One Big 4 India consultant was on "4 to 5 projects" a year; Deloitte India follows April to March and "normally declare[s] in May"; 1,000+ mid-level staff were benched in 2023 (https://thefinancestory.com/big-4-india-layoffs-benching-appraisals-2024).
- **Market:** India management consulting services USD 9.36 B in 2026 to USD 18.93 B by 2032 (https://www.mordorintelligence.com/industry-reports/india-management-consulting-services-market). Its SME segment is client size, not consulting firm size.
- **Upper size edge:** Primus Partners reached "400+ professionals" in seven years (https://smestreet.in/infocus/primus-partners-marks-7-years-of-building-a-homegrown-consulting-firm-for-a-changing-india-12535379).
- **Lower size edge:** SPI 2025 Table 170 (p148): voluntary attrition 6.1% at 10 to 30 staff, 7.7% at 31 to 100 (https://get.kantata.com/rs/677-LEJ-696/images/2025-ps-maturity-benchmark.pdf). This covers all professional services firms, mostly outside India.
- **Rater effect:** idiosyncratic rater effects explained 62% and 53% of rating variance in two data sets, and performance 21% and 25% (Scullen, Mount and Goff 2000, via https://peopleanalyst.com/ai/insights/ic-scullen-2000-idiosyncratic-rater-variance).
- **Gallup:** 29% of employees strongly agree their reviews are fair and 26% that they are accurate (https://www.gallup.com/workplace/236135/give-performance-reviews-actually-inspire-employees.aspx).
- **foundit Appraisal Survey 2026:** 52% actively looking; among those well represented in their appraisal, 37% said their manager actively advocated for them; no sample size stated (https://hr.economictimes.indiatimes.com/news/workplace-4-0/half-of-indias-professionals-are-already-job-hunting-during-appraisal-season-survey/132602041).
- **Deloitte snapshots** are completed "at the end of a project, phase, or at least quarterly" (https://www.td.org/content/atd-blog/reinventing-performance-management-at-deloitte). This is borrowed credibility only; it is not a Deloitte link to Sphyr.
- **Channels that exist:** IMCI (https://imcindia.co.in/); the NHRDN Delhi and NCR chapter, about 2,300 members (https://in.linkedin.com/company/nhrdn-delhi-ncr-chapter); SHRM India (https://www.shrmi.in/); People Matters and TechHR India (https://www.peoplematters.in/); the ETHRWorld daily newsletter (https://hr.economictimes.indiatimes.com/newsletter).
- **Timing:** the selling window is November to January, and the work starts at the opening of that window.

### 3. Decisions I made, and why

- **Recommended positioning** is a vision line ("Careers in consulting should be earned in front of the people who saw the work, not decided by whoever remembers it.") plus a product line. The anchor is the team's earlier "The engagement ends. The evidence stays." Why: the vision comes from the professor's own whitepaper beliefs, and the anchor was already settled by the team in October.
- **Value discipline: customer intimacy with the segment.** Simplicity is a design principle, not the discipline.
- **Ad medium recommended: a printed A2 poster with a matching A6 handout card at HR and consulting community events.** Why: near-zero cost, nobody is tracked, and it meets Kavya among peers. The same design can later run as a paid newsletter slot. The team decides at gate 1a.
- **LinkedIn posts publish as Sphyr or as team members in their own names, never as the professor or founder.** Why: writing in a real person's name would impersonate him.
- **Meera is still at the firm and is the person being rated.** The triggering exit is a different composite (Siddharth). Why: if Meera leaves, the journey has nobody to rate.
- **Persona names never appear in the ad or the posts.** Why: those formats cannot carry the "illustrative example" label.
- **Pilot price and length are left to the pricing work.** I flagged the conflict and did not resolve it: a 6-week pilot is 3 cycles, while the sources say about 6 cycles are needed.
- **The "20-minute call" is read as our team talking to the firm's head of talent.**
- **Website section order:** anticipation first, "what Sphyr does not do" near the end. Why: the packaging grade criticised reassurance over excitement.

### 4. Approaches rejected, and why

- **Runner-up B ("a voice"):** strong for consultants, but the managing partner may hear "less say for partners".
- **Runner-up C ("growth"):** soft for a buyer whose pain is calibration, and it leans on a trend line that needs several cycles.
- **Ad on LinkedIn (sponsored post):** the platform tracks users, which is the weakest fit with the no-tracking stance.
- **Paid newsletter slot as the primary ad:** it violates the zero-budget starting point. It is kept as the upgrade path.
- **Leading with client feedback or project reviews:** PerformYard claims both, and partners guard client relationships.
- **The "36% call their appraisal effective" foundit figure:** not found in the 2026 report, so not used.
- **AmbitionBox category averages and exact review counts:** could not be read reliably. Only verbatim review text is used.

### 5. Open questions

1. Gate 1a: approve the ad medium (poster and handout recommended), the recommended statement, and the persona and message guideline.
2. Pricing: pilot length and price. The scorecard targets in acquisition_engagement.md must match the length chosen.
3. Is the "partner page" (a short page for partners) a separate site page or a section? This is for the website teammate.
4. Does the product show feedback per consultant by engagement (team)? Scorecard metric 3 assumes the firm may need to count it by hand.
5. The root `docs/index.md` does not list `docs/strategy`. `build_index.py --root docs` writes the root index; I reverted that change each time, per the rule against editing it. The lead should add the entry when merging.
6. Confirm the reading of "a 20-minute call with the head of talent".

### 6. What I did not verify

- Scullen et al. (2000): checked only through the peopleanalyst summary, not the journal article.
- The SHRM India Annual Conference 2026 (15th edition): seen only in a search snippet of shrmconference.org; the page returned 403.
- The NHRDN Mumbai, Bengaluru and Hyderabad chapters: seen only in a LinkedIn listing snippet. The national conference is known only from a LinkedIn post.
- Whether ETHRWorld sells newsletter slots, and at what rate. Its site only lists advertising formats.
- Whether People Matters accepts contributed articles.
- Keka's 360 claim: read from the navigation of its pricing page only.
- The Hindu quote: read on the live page on 2026-11-24. The "nearly 85%" foreign-share figure from October was not re-checked and is not used.
- The firm-count estimate (150 to 400 firms, 18,000 to 48,000 seats) is a guess with a method, not a count.
- All buyer and head of talent language is a hypothesis. No interviews exist.
- The prototype notification text ("Feedback reminder: 3 reviews remaining for this fortnight cycle") comes from the JS bundle, not a rendered screen.
- Paid-layer cost caps are estimates, not quotes.
- I did not open the professor's prototype or Playwright myself (not allowed by my brief). Product claims rely on docs/product/.
