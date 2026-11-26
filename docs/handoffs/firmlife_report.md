---
type: Handoff
title: "Consulting firm life researcher report"
description: "Roles, staffing, appraisals, pain in their words, a 42-term glossary, a do-not-use list with product mismatches, the appraisal calendar and the tagline words."
tags: [handoff, firmlife]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T09:58:00Z }
---

# Consulting firm life researcher report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan (2026-11-26)
1. Skim context docs listed in research_common.md.
2. Research Q1 to Q7 with firecrawl first, exa fallback: firm career pages (homegrown Indian and global), appraisal guides, Reddit, AmbitionBox/Glassdoor, practitioner posts.
3. Build glossary (30+ terms) and do-not-use table against docs/product/prototype_screens.md.
4. Write docs/research/consulting_firm_life.md (OKF v0.2), then ## Final here.

## Progress
- Context read. Prototype words: "Fortnightly Feedback", "cycle", "appraisal period", "team", "member", "Peers / Seniors / Subordinates", "Manager", "Admin"; "project" appears only twice, "card" only as a UI box. Mismatch with the internal one-liner ("cards after each project") to flag.
- Sources so far: hackingthecaseinterview review guide (secondary), 6 r/consulting / r/Big4 / r/KPMG threads (exa), AmbitionBox Praxis (51 reviews; title counts), AmbitionBox RedSeer (4 reviews). Firecrawl "query" format failed twice; using markdown + local keyword extraction instead.
- Added: Big 4 India calendar (The Finance Story 2024, 2 Fishbowl, 2 Reddit), staffing (strategycase, umbrex), engagement length (OC&C podcast, mbaworth, Fishbowl LEK), Redseer titles (careers page, LinkedIn), PwC India Glassdoor community quotes, 6 r/consulting pain threads.
- Note written 2026-11-26 09:40Z; two fact-check passes fixed about 12 claims (counts with Redseer, thread recount 19, URL-less quotes marked, Dutch study label, r/KPMG country, Praxis order caveat), plus global table and Praxis HR post. Third pass (after firecrawl restart, site: queries): AmbitionBox Primus Partners (50+ reviews), AmbitionBox Avalon overview, one r/IndianWorkplace Redseer question; Reddit r/consulting and Glassdoor site: queries returned 0 results. First pass fixed 4 claims (Redseer title order, Praxis reviewer pairing, "roll off" source, one unsourced rating-words quote removed; added the one practitioner "evidence" use).

## Not done (out of scope)
- PerformYard markets "Performance management for consulting firms" (https://www.performyard.com/performance-management-for-consulting) and runs a CFGI case study with per-project feedback forms: a likely competitor, not analysed.
- completeaiagents.com lists a "Project Staff Appraisal Collection Agent" (forms within 3 days of project end, chases late replies). Dropped as evidence (AI-agent listing, not practitioner). Possible competitor signal only.
- Prototype demo data uses software titles ("Senior Developer", "Team Coders"); a consulting-data demo would be a product task, not research.

## Final

### Files written
- `docs/research/consulting_firm_life.md` (OKF v0.2, 43 sources in frontmatter, YAML parses). Created folder `docs/research/` (did not exist).
- This report.
- Scratch only: `.swarm/tmp/firmlife/` (dumps, d.sh, kw.py). Safe to delete.

### Key findings
1. Homegrown ladders differ by firm but borrow strategy titles: Avalon (Associate Consultant, Consultant, Senior Consultant, AVP, Executive Director), Redseer (Associate Consultant to Engagement Manager, Associate Partner, Partner), Praxis (Associate Consultant 7 of 24 titled reviews, up to Partner), Primus (Consultant, Senior Consultant, Manager, AVP, MD). Sources: firm career pages, AmbitionBox.
2. "Project" against "engagement" is mixed but leans "project": Avalon 9 to 0, AmbitionBox Praxis 8 to 1, AmbitionBox Primus 16 to 0, Redseer 0 to 2 (homegrown total 33 to 3). Global: McKinsey "engagement", BCG and Bain "case", Deloitte "project". To HR, "engagement" means employee engagement (Praxis HR post), and the product radar has an "Engagement" dimension.
3. "Evidence" is explainer and calibration-room language; 0 of 19 consulting practitioner threads use it for their own review (1 manager outside consulting: "lower rating with ZERO evidence"). Consultants say feedback, project feedback form, project review, rating, self-review, promotion case.
4. Strongest pain lines: "the Partner you are staffed with at the time of review tends to have the strongest influence" and "More recent or longer projects tend to carry more weight" (r/consulting 1q6k0ti); "Ratings are as opaque as they can be" (Glassdoor PwC India); HR: "you're only at 50% of the reviews done, and the year is almost over!" (Keegan and Den Hartog 2019, Dutch firms).
4a. Homegrown pain word is "partiality" (Primus, 4 uses): "Partiality is rampant. If you become a yesman to the leadership they might still think of giving you a promotion"; "good young talent ( who leave also very soon after being demotivated from partiality". Avalon: "44% employees rated Avalon Consulting 3 or below on promotions / appraisal" (AmbitionBox aggregate). Homegrown reviewers blame people (MDs, founder, leadership), not process.
4b. Homegrown HR is generalist: a Praxis "HR Associate - Build" post covers "hiring, onboarding, engagement, performance management, and HR operations" (JobLeads, 1 post).
4c. Global-firm comparison table added (McKinsey, BCG, Bain, Deloitte, Accenture; hackingthecaseinterview, secondary).
5. Projects last 1 to 2 months (OC&C) or 6 to 8 weeks; guess 5 to 10 managers per consultant per year.
6. Calendar: Big 4 India (3 of 4) rate in April to June, hikes from July, bonus September; EY is July to June with September payouts. April to June assumption holds for Big 4; unverified for homegrown.
7. Product word mismatches (for the lead): radar dimension "Engagement" collides with the tagline; product is fortnightly and team-based while consulting is project-based; "Subordinates", "Member", "Admin", "VBAs" are not consulting words; no partner role; software titles in demo data.

### Decisions I made and why
- Counted Big 4 India and global-firm voices as segment evidence, labelled clearly, because homegrown first-person sources were thin (2 AmbitionBox pages).
- Kept "guess" labels on managers-per-year and on alternatives for "Member" and "Admin": no source.
- Quoted no individuals by name or handle; role labels only. Skipped abusive or legal-threat lines in Praxis reviews.

### Approaches rejected and why
- Firecrawl `query` format: failed twice ("Query generation failed"). Used markdown plus local keyword extraction.
- Firecrawl search for Reddit: tokens like "r/consulting" return R-language results; fell back to exa for Reddit and Fishbowl (per lead note, only on firecrawl failure).
- completeaiagents.com as evidence: vendor listing, not practitioner.
- Further HR-posting search for Avalon, Redseer, Primus: firecrawl search returned unrelated results; stopped rather than spend exa quota.

### Open questions for the lead
- Tagline: keep "engagement" and "evidence", or move to "project" and "feedback"? Data favours the second for homegrown firms; not decided.
- The product's "Engagement" radar dimension: rename in copy, explain, or avoid "engagement" in the tagline?
- Fortnightly cadence versus "after each project": which does the site promise?
- Is a consulting-data demo (consulting titles, a partner) in scope for v3?

### What I did not verify
- Head of talent and HR business partner roles at homegrown firms; years per level at homegrown firms; any homegrown firm's appraisal calendar.
- Global-firm ladders (McKinsey, BCG, Bain, Deloitte, Accenture Strategy titles) beyond what sources stated; not filled from memory.
- Exa highlights are excerpts; quotes are exact fragments but surrounding context was not read in full. Word counts are from about 7 excerpted dumps: directional only.
- AmbitionBox reviewer title and date pairing for individual Praxis quotes.
