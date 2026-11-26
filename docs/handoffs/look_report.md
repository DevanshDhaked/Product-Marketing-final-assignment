---
type: Handoff
title: "Visual language researcher report"
description: "How consulting firms, their vendors and award-level corporate sites look, v2 against both, and two directions with a lean to A (the partner's brief)."
tags: [handoff, look]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T09:56:00Z }
---

# Visual language researcher report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

## Plan
- Read design docs, v2 live page, context docs.
- Scrape 8+ consulting sites, 8+ vendor sites, 8+ award-gallery examples.
- Write docs/research/consulting_visual_language.md (sections 1 to 5 + What this means for v3).

## Progress
- 2026-11-26T09:33:14Z started.
- Read design system, slop rules, references, ribbon motif, decision log (type, colour, ribbon, favicon), professor addendum, handoff s2-3, live v2 page text.
- Firecrawl branding format unavailable keyless ("requires Chrome CDP"). Wrote tmp/look/css_probe.py (fetch HTML + linked CSS, count @font-face, font-family, hex). Consulting probe: 11 of 13 fetched (McKinsey timed out, BCG 403); results in tmp/look/consult.jsonl.
- Finding so far: v2 references (docs/design/references.md) are mostly studio and agency Sites of the Day (Two26, MECHA, Bulletproof, Extrafazant). That is the root of the professor's "creative agency" read.
- Consulting probe (11 sites read): serif display + sans body on Bain (Tiempos, Graphik), Roland Berger (Arnhem serif), Redseer (cambon serif + Manrope), Oliver Wyman (Marsh Serif + MMC Display). McKinsey (Bower, deep blue, per Wolff Olins) and BCG (Henderson Serif logotype, per zecraft) from secondary sources since direct fetch was blocked. Homepages are insight feeds: Bain 26 h2/h3, all report titles.
- Vendor probe (12 sites read): 10 of 12 lead with an AI claim in h1 or first h2. Serif display seen on Culture Amp (Tiempos), 15Five (DM Serif Display), Betterworks (Merriweather), Workday (own headline face).
- Awwwards: scanned 74 entries in business-corporate, finance, law, consulting categories; 25 are Site of the Day or Honorable Mention. Probing 12 live sites for type and colour.
- Lead note received: firecrawl first, no branding format, exa only on firecrawl failure. Followed (exa used for McKinsey and BCG brand facts after firecrawl search returned off-topic results).
- Correction to an earlier progress line: AI in vendor headlines is 8 of 12 (strict: AI or agents in H1 or first eight headings), not 10 of 12.
- Note written: docs/research/consulting_visual_language.md (2026-11-26T09:49Z).
- Advisor review applied: Direction B entrance fade removed; Direction A exhibit labels set as sentence-case captions below frames, margin numbers as plain body text; ribbon rule defaults to approved logo colours, tonal green offered as an option; Barber Hauler motion claim fixed (it loads Swiper and 4 videos); motion column added to all three tables; "more words" changed to "more structure"; Direction A bullets tagged in What this means.
- Serif-for-headings check (tmp/look/serif_sel.py, CSS selectors): serif styles headings on Bain, Oliver Wyman, Roland Berger, Redseer (4 of 11); Praxis loads Playfair but not tied to headings. Award: Barber Hauler and Hafnia confirmed; RBB via an untraced variable.
- Lead note 2 (firecrawl restarted): BCG home page read with firecrawl markdown (dated article cards, Client Impact stories naming British Airways and Dow with one stat). McKinsey home still 403; Featured Insights page read instead (a magazine: highlights, podcast, video, books, crossword, obituaries).

## Not done (out of scope)
- No CSS, mockups, copy or site edits.
- Noticed: `docs/design/ribbon_motif.md` still says the strands avoid orange and red and that the nav uses the mono mark, while decision log entries of 2026-11-25 changed both. The doc may need a dated addendum.

## Final

### Files written
- `docs/research/consulting_visual_language.md` (sections 1 to 5, What this means for v3).
- Scratch only, not for commit: `.swarm/tmp/look/css_probe.py`, `aw_list.py`, `aw_site.py`, `serif_sel.py`, `fix_note.py`, and the `*.jsonl` outputs.

### Key findings
1. Root cause of the "creative agency" read: 4 of 7 picks in `docs/design/references.md` are studios or agencies (Two26, MECHA, Bulletproof, Extrafazant). The hero ribbon animation, the italic brand line, the manifesto paragraph (from Two26) and the scene structure (from Inkwell) come from that list.
2. v2's base is already in the consulting register. A serif is loaded on 5 of 11 consulting pages and styles headings on 4 (Bain Tiempos, Oliver Wyman Marsh Serif, Roland Berger Arnhem, Redseer Cambon), checked by CSS selector. Redseer (homegrown Indian strategy firm) pairs a serif with Manrope on warm neutrals (https://redseer.com/). RBB Economics, Barber Hauler and Hafnia Law (award or Siteinspire picks) use serif on warm paper or stone.
3. Consulting pages are publications: on 5 of 11, most headings are research titles (Bain: 26 of 26). Numbers in headlines (Sattva H1 "A decade of green spending. ₹17000 crores of investments."). H1s say what the firm is (Redseer, ZS).
4. One hue on white or warm neutral is the norm (McKinsey deep blue and "high contrast", Wolff Olins and Transform 2019; Bain red; Redseer red). Roland Berger is the multicolour exception.
5. Vendors: 8 of 12 lead with AI or agents; serif display on 3 of 12; PSA tools name their category in the H1. Sphyr cannot copy this register (do_not_claim).
6. Award corporate (11 read): one hue family on 10 of 11, serif on 5 of 11, proof as named lists (mandates, rankings, projects), quiet ones load no motion library.
7. Indian mid-size firm sites are not a craft benchmark (template fonts, sliders on 3 of 6). Borrow their content habits, not their look.

### Decisions and why
- Measured type and colour from HTML and CSS with a script, because firecrawl branding needs Chrome CDP and the query format failed 6 of 6; no browser by brief.
- Used exa for McKinsey and BCG identity only after firecrawl search returned off-topic results. After the firecrawl restart, read BCG home and McKinsey Featured Insights with firecrawl markdown; McKinsey home still 403.
- Dropped 6 crypto or "AI finance" 3D Honorable Mentions as off-register.
- Proposed A (editorial report, keeps v2 system) and B (Swiss corporate grid, sans-led, cool white). I lean to A: smallest degrade risk, evidence that v2's type and palette already match the register.

### Approaches rejected and why
- Copying Indian firm sites' look: template grade (Montserrat or Poppins, sliders), would degrade.
- Vendor register (AI, logo walls, violet): conflicts with do_not_claim and was rejected in v2.
- Screenshots via firecrawl: brief forbids screenshots.

### Open questions for the lead
1. Direction A or B (user's call). Both listed with risks.
2. Direction A rule 6 now defaults to the approved logo colours; a tonal green ribbon figure is offered only as an option for the user.
3. Should the core ribbon animation go entirely, or stay behind a reader-started "Play" control lower on the page?
4. Is moving the theme toggle to the footer acceptable, given the toggle took real work in v2?

### What I did not verify
- Rendered layout, grid, type sizes and motion as seen: inferred from code signals only (no browser).
- McKinsey home page (403); its type and colour, and BCG's, come from Wolff Olins, Transform, Zecraft and MetaDesign pages, not from the sites' CSS.
- RBB's serif use (variable not traced), and Mosaic's and Implement's serif use in headings.
- Whether Bower is a serif and whether SLR's Albra is a serif (from memory, marked in the note).
- Theme toggle presence on consulting sites (not checked in code; marked as inference).
- Godly, Land-book, Lapa Ninja, Minimal Gallery, Httpster, Commerce Cream, One Page Love: not reachable or not parsed; only Awwwards and Siteinspire were used.
