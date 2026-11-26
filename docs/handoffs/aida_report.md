---
type: Handoff
title: "AIDA researcher report"
description: "The professor's AIDA against the standard model, with rules for one page, one ad and one post, assurance evidence both ways, and the tagline question."
tags: [handoff, aida]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T10:00:00Z }
---

# AIDA researcher report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan
- Read common rules, brief, professor addendum, handoff sections 2 and 3, personas, product facts, do-not-claim list. Done.
- Research with firecrawl first (user asked), exa fallback: AIDA origin and variants (AIDCA, AIDAS, Gartner buying jobs); Attention rules (Ogilvy, Schwartz, NN/g); B2B SaaS assurance norms; low-friction decision steps; CTA count; CAC; tagline as Attention line; 3 to 5 real B2B landing pages, one print ad, one LinkedIn post.
- Write `docs/research/aida.md` in the iteration-b worktree. Then `## Final` here.

## Progress
- 2026-11-26: context read. Pilot terms confirmed in `docs/decisions/decision_log.md` line 119: 12 weeks, up to 40 people, Rs 25,000 plus GST, credited to first bill, else data as CSV and rest deleted. Refund and price lock "Not adopted" (line 120).
- Tools: firecrawl search returns many opaque redirect URLs (`http:///go/v1/...`) and off-topic results for several queries (car games, GitHub, stock news); firecrawl `query` and `json` formats failed ("Query generation failed after all models", "JSON extraction failed"). firecrawl markdown scrape works. exa search worked 3 times then hit its free rate limit. Fallbacks used: WebSearch for discovery, firecrawl scrape and curl for verification.
- Q1 and Q2 sources in hand: Wikipedia AIDA wikitext, Gartner buyer enablement ebook, NN/g, Ogilvy notes (verified by curl on 2 pages), Copyhackers on Schwartz.
- Q3 to Q5: curl'd 10 HR-tool home pages and 8 pricing pages, outline script at `.swarm/tmp/aida/outline.py`. Pilot and guarantee sources scraped with firecrawl (Heavybit, Pravin Kumar, Conversion Rate Experts). SaaStr page returned 403.
- Note written: `docs/research/aida.md`.

## Not done (out of scope)
- `docs/index.md` and `docs/research` log entry for the new note: lead to add (I do not edit existing files).
- The deployed /v2/ hero was not compared with `site/index.html` on iteration-b.
- Some team docs still mention the older Rs 15,000 / six-week pilot (`docs/site_audit/*`, `docs/brief/feedback_gap_map.md`); they are audits of v1, but a reader could mix them up.

## Final

### Files written
- `Product-Marketing-final-assignment.iteration-b/docs/research/aida.md` (sections 1 to 8, stage checklist table, "What this means for v3" with 8 bullets).
- This report.
- Scratch only: `.swarm/tmp/aida/` (outline.py, raw HTML, wikitext). Not for commit.

### Key findings
1. The professor's model is Attention, Interest, Decision, Action in his v2 review (his class notes say Awareness). "Decision" has precedent: Wikipedia lists an "Attention, Interest, Decision, Action" variant (Moreira 2024) and Kitson 1920 has "Secure Decision and Action". His Interest is assurance; his Decision is friction removal. Recommend following his reading for grading. Source: https://en.wikipedia.org/wiki/AIDA_(marketing)
2. Gartner: six buying jobs, "90% of all buyers reported revisiting, or looping back", "Only 17% of buying time" with suppliers (2019 ebook PDF).
3. Attention: NN/g, value proposition "within 10 seconds"; 57% of viewing time above the fold. Ogilvy: 5x read the headline, name the brand, flag the reader, no puns. No source found for a "5 second test".
4. Assurance scan (raw HTML, n = 10 home, 8 pricing): demo-led CTA 10 of 10; refund or guarantee 0 of 18 pages; free trial on 3 of 8 pricing pages; "pilot" on 0 of 8.
5. Pilot vs guarantee: Kumar says skip a guarantee "when value takes months to show, when setup costs you real money" (fits Sphyr's six cycles and cost-to-serve fee); CRE shows +29% from guarantee microcopy, but on a consumer course page. Both sides written up; not decided.
6. "A manual" maps to an existing fact: price includes "training and training materials" (whitepaper p6 to p7).
7. HubSpot (40,000+ pages): 3-field forms convert best; CXL shows cutting fields can hurt.
8. Tagline: the v2 H1 was exactly "The engagement ends. The evidence stays." (`site/index.html:66`) and the professor said the top of that page did not say what the site is about. Evidence for both readings written up; not decided.
9. LinkedIn: about 210 characters desktop, 140 mobile before "see more" (vendor sources); LinkedIn ranks with a dwell-time skip model (LinkedIn Engineering 2020).

### Decisions I made and why
- Recommended the professor's Attention, Interest, Decision, Action for grading, because his own v2 review spells it that way and the brief says it is his course.
- Used HR and performance tools as the landing-page sample because I found no consulting-specific feedback tool page in the time box; flagged it as a gap.
- Counted page features from raw HTML instead of rendered pages because firecrawl's LLM extraction failed; flagged counts as rough.

### Approaches rejected and why
- Citing the Imagescape "11 to 4 fields, 120%" figure: could not verify the original.
- Citing the Unbounce 13.5% single-CTA figure as fact: only found second hand; mentioned with that caveat.
- Citing India's DPDP Act for data deletion: did not confirm the document I downloaded; left it out.
- Constructing a sample LinkedIn post and presenting it as real: LinkedIn needs login; gave shapes only, labelled "examples, not final copy".

### Open questions for the lead
- Refund or guarantee against pilot framing as the Interest assurance (section 3 gives both sides).
- Tagline as H1 or strapline (section 8 gives both sides).
- Primary CTA label to use on every page and the ad (20-minute call vs walkthrough).
- Whether to add a referral or extended-pilot credit as the B2B "coupon" beyond the existing pilot credit.

### What I did not verify
- Rendered (JavaScript) versions of the 10 vendor pages; counts may miss content loaded by script.
- That `site/index.html` on iteration-b equals the deployed /v2/ the professor saw.
- Original Ogilvy and Schwartz texts (used notes pages and Copyhackers quoting the book).
- LinkedIn "see more" cutoff against LinkedIn's own documentation.
- Edelman-LinkedIn figures (sponsored survey, no independent replication).
- The Gartner 17% figure's underlying sample.
