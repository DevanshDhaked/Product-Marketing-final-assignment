---
type: Handoff
title: "Propaganda and hub fix teammate report, phase 3"
description: "The short propaganda page with a summary card and sticky contents, the hub's 01 row, reviewer fixes and checks."
tags: [handoff, propfix]
generated: { by: claude-code/opus-5-5, at: 2026-11-25T06:30:00Z }
---

# Propaganda and hub fix teammate report, phase 3

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

I worked on branch `d1-propfix`, branched from `iteration-a`, in the worktree `Product-Marketing-final-assignment.d1-propfix`. The direction was already approved, so there was no plan stop. I used the lead's server at http://127.0.0.1:8827/ and did not start a server of my own.

The propaganda page now has 705 visible words, down from 3,389. The target was about 600. The extra words come from naming the channels and the target belief in their own paragraphs, so that each brief point stands alone.

## Progress

### Hub
- Added the row "01 The website". It links to `index.html` and to `demo.html`.
- Cut the intro to one sentence.
- Retuned the 02 line to fit the short page.
- Updated the meta and og descriptions.

### Propaganda page
- The page opens with a summary card. It holds the core line, the audience, the expected response, the belief today, the belief we want, the tactics and the channels.
- Seven sections follow, one paragraph each, in the brief's order: audience; belief (today, its cause and the target); central message and reasoning; tactics and channels (each channel named); why they fit; link to positioning; expected response.

### Contents list (lead's TOC request)
- **Desktop:** a sticky column that marks the active section with `aria-current="true"`.
- **Phone:** a sticky bar under the nav showing "On this page" and the current section. It opens the list with native details/summary, and closes on a link tap and on Escape.
- **Without JS:** an open, normal list at the top.
- **How the active section is chosen:** it is the last section whose top has passed a line 160 px down the screen. A 2 px IntersectionObserver band on that line triggers the check, and the band is rebuilt on resize. When the footer is fully visible, the last section is marked. A clicked link is marked at once, which covers pages that are already scrolled to the end. There is no scroll listener and no animation loop.

### Lead fixes
- The 2018 pilot line now reads "the cards for an average circle of 14 people took a little over two minutes (02:09)".
- The standee is "in the same opening weeks as the first of three LinkedIn posts".
- No pronouns are used for personas.
- There are no access dates or ISO dates. The one citation is "Scullen, Mount and Goff, 2000", by name and linked.

### Checks (method and numbers)

**Word count.** I counted the visible text inside `<main>`, with aria-hidden text, nav and footer excluded, using `wc.py` in my scratchpad.
- Before: 3,389. After: 705.
- The 705 includes the 7 TOC labels (17 words) and the card (about 95).

**`copy_scan.py`.**
- Propaganda: 76 strings, 0 unreviewed hits.
- Deliverables: 49 strings, 0 hits.
- Two hits were fixed on the way. Both were "track" read as surveillance: "Losing track of..." (the belief quote is now "Nobody remembers a consultant's whole year, and that is how consulting works.") and "track nobody" (now "use no ad pixels or bought lists").

**`copy_tells.py`.** 0 contrast sentences on both pages. I checked every possible triad by eye, and none is a rhythmic triad:
- Propaganda has 8: the four-item tactics list, two fragments of the six-item channel lists, the authors "Scullen, Mount and Goff", two two-part clauses and the footer's four names.
- Deliverables has 1: the footer names.

**Banned items.** A grep of both pages found 0 dashes, 0 month names, 0 uses of "anonymous", no customer talk and no access or ISO dates.

**Layout.** I ran my own headless Chrome through playwright-core, because another agent was using the shared Playwright MCP browser.
- At 1280, 390 and 375 px wide, in both themes: sideways scroll is 0 everywhere, and there are 0 console or page errors.
- The smallest text is 13 px.
- The summary card ends at 760 px in a 1280x800 viewport, so it fits on one screen.

**TOC jumps.** I tested 7 link jumps at each of 5 viewports (1280x800, 1440x1100, 1920x1200, 375x812 and 390x844), 35 jumps in all.
- The active link was correct in 35 of 35.
- No heading was covered after a jump on phones. The heading lands at 126 px, and the bar ends at 110 px.
- Scrolling back to the top marks "Audience".

**Plain wheel scrolling.**
- At 1280x800 and 375x812, every section becomes active in order, down and back up.
- At 1920x1200, "Why they fit" and "Link to positioning" are skipped while scrolling down. They never reach the line before the page ends, so the last section is marked instead.

**Keyboard and motion.**
- On desktop, Tab reaches all 7 links in order.
- On phone, Enter on the summary opens the list. Escape closes it and returns focus to the summary.
- `getAnimations()` returns 0 after load.
- Under reduced motion, the chevron transition is 0s.

**Links.** I fetched every relative href on both pages with curl from 8827, and all returned 200. In-page anchors match the 7 section ids. A grep of `site/`, `README.md` and `docs/` found no links to the dropped anchors `#sequence`, `#objections` or `#limits`.

**Contrast.** I added no new colours, only existing tokens, so I did not run `contrast.mjs`.

## Final

### Files written, with commits (branch d1-propfix)
- 096cace: `site/deliverables.html`. Hub row 01, a one-sentence intro, the 02 line and the meta descriptions.
- 86e0c24: the propaganda rewrite in `site/propaganda.html`, `site/css/deliverables.css` and the new `site/js/propaganda.js`.
- 22950da: removed the dead CSS left over from the old page from `site/css/deliverables.css` (doc-head, doc-index, doc-num, seq, table-stack, sources, table and h3 spacing). The screenshots were byte-identical before and after.
- e851b16: in `site/propaganda.html`, named the channels and the target belief and added the "attend as guests" line. In `site/js/propaganda.js`, fixed the active section at the page end and on tall screens.
- e315f14 and f6ed652: screenshots in `design-lab/shots/site/`:
  - `propaganda-{light,dark}-{1280,375}.png`
  - `deliverables-{light,dark}-{1280,375}.png`
  - `propaganda-toc-midpage-1280.png`
  - `propaganda-toc-bar-open-375.png`

### Key insights and findings
- Each of the seven brief points fits in one paragraph of about 60 to 90 words without losing the specifics:
  - the professor's "to influence minds"
  - free channels with no pixels or bought lists
  - the paid standee as the one ad
  - the "who else has tried it" answer: the four measures agreed before every pilot, plus the 2018 paper pilot
- The cut material is already kept elsewhere, so the cut loses nothing. The persona-shaping table, limits, sources list, 7-stage sequence and objections are in `docs/handoffs/hub_report.md` (24 mentions) and in `docs/strategy/`.
- The ad timing now matches `ad.html:126` and `linkedin.html:220`: the standee runs in the same weeks as the first post. The old page said weeks 3 to 4.
- An IntersectionObserver band set as a percentage of the screen gives the wrong active section on tall screens, because these sections are short (about 200 px). A fixed 160 px line, plus a footer-visible end state, plus marking the clicked link, is correct at every viewport tested.

### Decisions and why
- **One element for the TOC.** A single `<details open>` serves as both the desktop column and the phone bar. One list means no duplicate words, and the no-JS fallback works without extra markup.
- **Sticky phone bar needs JS.** The bar is sticky only after JS adds `.is-live`. Without JS, the open list would cover the content.
- **Scoped CSS.** The new CSS is scoped to `.page-prop`, `.prop-*` and `.toc`. I checked that no other page links `deliverables.css`, so I deleted the dead rules.
- **Core line once.** The core line appears once, in the card. The "Central message" paragraph explains it without repeating it.
- **One citation.** The only inline citation is Scullen, Mount and Goff (2000), linked to the summary page with no date. I dropped Gallup and Deloitte to save words.
- **Event names.** The page does not name NHRD or IMCI. HR community meets are described as places "we attend as guests", which keeps the no-endorsement point short.

### Rejected approaches
- **A popover for the phone list.** Its content is hidden without JS.
- **Two TOC lists, one per layout.** This doubles the words and the markup.
- **A scroll-listener highlight.** It breaks the rule of 0 idle frames.
- **A band at 120 px to 30% of the screen.** Several sections fell inside it on tall screens, so it gave the wrong active section.
- **Extra blank space after the last section** so it can scroll up to the line. That empty space at the end costs more than the footer check.

### Open questions
- At 705 words the page is about 17% over 600. Trimming further would cut a brief point or the named channels. This is the lead's call.
- I dropped the persona Meera. Only Kavya and Vikram remain, labelled illustrative. Should Meera come back?

### Not verified
- I tested in Chrome only, not in Safari or Firefox. Both support `details`, IntersectionObserver and optional chaining.
- I did not test with a screen reader.
- On very tall screens (1920x1200), plain scrolling skips two sections in the highlight, as described in Checks. Clicking those sections still marks them correctly.
- I did not use the shared Playwright MCP browser, because it was busy.
