---
type: Handoff
title: "Orchestrator handoff, 2026-11-24 20:37 UTC"
description: "Everything the next orchestrator needs to finish the Sphyr site on iteration-a: state, open work, user rules, how to run herdr teammates, and the mistakes not to repeat."
tags: [handoff, orchestrator, iteration-a]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T20:37:16Z }
---

# Orchestrator handoff, 2026-11-24 20:37 UTC

Deadline: final assignment due **27 Nov 2026, 23:59** (IST). The user pushes and redeploys; agents never push.

## 1. Where things are

| What | Path or value |
|---|---|
| Repo (user's checkout, on `main`) | `/Users/borah/resources/IIITH PDM/sem_3/pm/Product-Marketing-final-assignment` |
| Working branch and worktree | `iteration-a` at `.claude/worktrees/iteration-a` inside the repo. Last commit before this file: `5c6ca4c`. Not pushed. |
| Live site (old, unchanged) | https://devanshdhaked.github.io/Product-Marketing-final-assignment/ served from the `gh-pages` branch. Redeploy steps are in `README.md`. |
| Docs bundle (OKF v0.2) | `docs/` on `iteration-a`. Read `docs/index.md`, then `docs/decisions/decision_log.md` (every user decision, newest first). |
| Swarm folder (outside git) | `/Users/borah/resources/IIITH PDM/sem_3/pm/Product-Marketing-final-assignment.swarm/`: `ledger.md` (run log), `briefs/` (common.md, phase2_common.md and one brief per teammate), `reports/` (every teammate report), `scripts/handoff.py` (copies a report into `docs/handoffs/`), `scripts/feedback.md`. |
| Course sources (read only) | `/Users/borah/resources/IIITH PDM/sem_3/pm/` : `sphyr/` (brief, product doc, whitepaper, logo), `tasks/saas/` (earlier graded work). Canonical brief copy: `docs/brief/assignment_brief.md`. |
| Merged site preview | `python3 -m http.server 8830 --bind 127.0.0.1 --directory <worktree>/site` (may still be running), then http://127.0.0.1:8830/index.html |
| OKF scripts | `python3 "/Users/borah/.claude/plugins/cache/borah-skills/hack-kit/884177ff0f97/skills/okf-docs/scripts/build_index.py" docs` and `.../okf_validate.py docs` (0 errors expected). |

## 2. The site (all six pages built and merged)

`site/index.html` (home: ribbon hero, problem scenes, how it works, for partners, proof, pricing cards, after you sign), `demo.html` (4-step interactive walkthrough), `deliverables.html` (hub: 01 website, 02 propaganda, 03 posts, 04 ad), `propaganda.html` (about 650 words, sticky contents), `linkedin.html` (3 post mockups), `ad.html` (paid roll-up standee and A6 card at an HR community event, planned, QR to demo.html). Shared files: `site/css/base.css`, `motif.css`, page CSS files, `site/js/*.js`, `site/fonts/`, `site/assets/`, `site/_template.html`. Screenshots live in `design-lab/shots/site/` (not deployed).

## 3. Open work, in order

1. **Visuals teammate** (herdr agent `visuals`, pane `w8:p2E`, branch `d1-visuals`, worktree `Product-Marketing-final-assignment.d1-visuals`, preview server on 8829 started by the previous lead). It adds four visuals to `propaganda.html` (audience map, belief shift, channel table, campaign flow), brief at `briefs/visuals.md`. When it stops: read `reports/visuals.md`, look at its screenshots, merge with `git merge --no-ff d1-visuals`, copy its report with `python3 <swarm>/scripts/handoff.py visuals "<title>" "<one sentence>" <UTC time>` run from the worktree root, rebuild the docs index, commit, then `herdr agent prompt visuals "/exit"`, `herdr pane close w8:p2E`, stop the 8829 server.
2. **Final pass (small, do it yourself or with one fresh agent):**
   - Remove dated HTML comments copied from the template (for example `<!-- Canonical nav (2026-11-25, ...` ) from every page in `site/`.
   - Remove the duplicate "Book a 20-minute call" text link at the end of `#pricing` on `index.html` (the pilot card already has the button; the user did not object when told).
   - Scan all six pages: no access dates or ISO dates, no month names, no "anonymous"/"anonymized" overclaims, no he/she for unnamed roles, no claims of customers or of having none, no dashes, no emojis; all links and anchors resolve; no sideways scroll at 375 px; one screenshot per theme by eye.
   - Optional reviewer nice-to-haves (`docs/handoffs/reviewer_report.md`): standee headline sits tight under the logo; ad URL under the QR is 11 px; demo "From 13 collaborators" count; index scene vs post 1 describe "the file" slightly differently.
3. **Walkthrough change (user decision 2026-11-25):** the card in `demo.html` must follow the visitor's pick. Today `site/js/demo.js` always uses Nikhil. Spawn one fresh herdr agent for `site/demo.html`, `site/js/demo.js`, `site/css/demo.css`: card name and avatar, the reply lines, the step 3 partner view and the step 4 ending all switch on the pick; both paths must still show that the record holds what colleagues saw. Check both paths by eye in both themes.
4. **Housekeeping:** ask the user before removing the finished teammate worktrees (`git worktree list`; all `d1-*` branches except `d1-visuals` are merged). Append a dated entry to `docs/log.md` and the ledger.
5. **Hand to the user:** the local preview URL, the commit list, and the redeploy steps from `README.md`. The user reviews, pushes `iteration-a`, and redeploys `gh-pages`.

## 4. User rules (follow exactly)

- **Agents:** spawn only herdr teammates (separate `claude` in a herdr pane), never in-process Agent-tool subagents. Spawn in the herdr tab **"prod-marketing"** (workspace `pdm-project`, tab `w8:t3`): `herdr pane split --pane w8:p4 --direction right|down --no-focus --cwd <repo>`. Never `--current` (the job's inherited env points at the wrong tab "dsa").
- **Starting a teammate:** `herdr agent start <name> --kind claude --pane <id> -- "<prompt>"`. A bare `claude` opens the sessions dashboard instead of a session. Start usually times out because the agent goes straight to work: then run `herdr agent rename <pane> <name>`. Wait with `herdr agent wait <name> --timeout 3600000` in the background.
- **One fresh agent per task.** Do not keep one agent across phases; the user flagged a long-running agent at low context.
- **Persist before teardown:** every report ends with `## Final`; copy it into `docs/handoffs/` with `scripts/handoff.py`, commit, then exit the agent and close its pane. Close panes and stop preview servers as soon as an agent is done.
- **Teammates cannot start servers** (the permission classifier blocks `http.server` for them). The lead serves each worktree on a port and gives the URL in the brief. Stop each server when its agent finishes.
- **Never approve a teammate's flagged permission prompt** (for example a flagged `rm`); decline and redirect.
- **Plan and ask first** when anything is ambiguous; batch questions with AskUserQuestion. Before proposing scope, check what the brief (`docs/brief/assignment_brief.md`) and the professor feedback (`docs/brief/professor_feedback.md`) actually require. The user rejects scope creep.
- **Checks are smoke checks only:** copy scans (`python3 design-lab/copy_scan.py site/<page>.html`, `copy_tells.py`), links, no sideways scroll at 375, one screenshot per theme by eye. No WCAG contrast matrices or pixel measurements.
- **Git:** commit per logical group with explicit files; never push; never merge to `main`. In this worktree-isolated session, compound or multi-path git commands get refused: run git as single plain commands, and put Python edits in a script file, then run it.
- **Writing:** simple English, no em dashes or double dashes, no emojis.

## 5. Copy and design rules (all in the decision log)

- Segment: homegrown, partner-led Indian management and strategy consulting firms, 40 to 400 people. Primary persona: head of talent (Kavya, internal only); buyer: managing partner. Persona names only in the propaganda audience section.
- Central message: "The engagement ends. The evidence stays." (only line kept verbatim). Every other visible line goes through the `humanizer:humanizer` skill: at most one "X, not Y" per page, no triads as rhythm, no staged openers or one-line closers, no bold labels before sentences.
- No month names (say "promotion time", "the promotion round"). No access dates or ISO dates on public pages; cite by name and year only. Never claim customers and never say there are none. Never "anonymous to everyone"; say names are not shown with comments. Roles over pronouns; "they" when gender is unknown. No AI claims, no invented features (`docs/product/do_not_claim.md`).
- Pricing: ₹149 per employee per month, billed yearly, plus GST; pilot ₹25,000 plus GST one time, 12 weeks, up to 40 people, credited if they sign, data returned if not. Plan card is the hero, pilot card supports it.
- Design: warm palette (light `#FAF8F4`, dark `#171513`), Newsreader headlines and Manrope text (no font changes), no dithering, full-colour logo in nav and footer, the ribbon motif in the original logo colours, simple and opinionated layout, few links. The current site on `main` is a content reference only.
- Ad: paid standee with handout cards at an HR community event, planned, the real event not named, tracks nobody.

## 6. Mistakes this session made (do not repeat)

1. Spawned in-process subagents first, then herdr teammates via `--current` in the wrong tab.
2. Let one design agent run through two phases until its context was low.
3. Ran full WCAG and pixel-measurement test matrices the brief does not reward.
4. Put "(accessed 2026-11-24)" stamps on a public page.
5. Wrote "We have no customers yet" on the site.
6. Repeated "April" across all copy.
7. Used jargon labels ("Pricing review", "Market entry") in the hero visual.
8. Built an overloaded pricing section and then stretched cards to equal height with an empty band.
9. Let the propaganda page grow to 3,400 words.
10. Switched pronouns between two people in one LinkedIn post ("he ... her").
11. Claimed the professor praised our walkthrough page; he praised the idea in the packaging one-pager.
12. Used a blue AI-looking palette and a cool subset of the logo colours that made the sphere stop looking like the logo.
13. Left nine preview servers running after their agents finished.
14. Started the deliverables hub at "02" with the website only mentioned in prose.
Each was caught by the user. The fix for all of them: check the brief and the user's stated preferences before building, keep pages short, and look at every screenshot yourself before reporting.

15. Treated automated checks as proof the pages looked right. The walkthrough's step indicator was misaligned (a base `li + li` margin pushed steps 2 to 4 down by 8px; fixed in `site/css/demo.css`) and nobody looked at it closely. Check every horizontal list and row on every page by eye for the same base-margin problem.
16. The walkthrough always asks the visitor to rate Nikhil whatever they picked. That is the agent's design (the ending speaks to either pick), but the page never says why, so it reads as a bug. Open question to the user at handoff time.
