---
type: Plan
title: "Iteration A plan"
description: "Sequenced plan to rebuild the Sphyr site and four deliverables for the consulting segment, answer every professor feedback point, and redesign with light and dark themes, with approval gates."
tags: [plan, iteration-a]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:55:00Z }
status: draft
---

# Iteration A plan

**Success number:** professor feedback points answered on the site, out of 15. The 15 are pricing 6, packaging 3, journey 3, message and channels 2, and positioning 1. At fc85cac the count is 2 of 15, both only partly. Every phase reports this number first.

Inputs: [decisions](../decisions/decision_log.md), [feedback gap map](../brief/feedback_gap_map.md), [do-not-claim list](../product/do_not_claim.md), [site audit](../site_audit/brief_compliance.md).

Effort follows the rubric. Propaganda, LinkedIn and the ad carry 40 marks, so each gets a written spec before any page is built.

## Phase 1a: strategy core (one teammate), with design tokens in parallel

The **strategy** teammate owns `docs/strategy/` and writes:

1. Segment: the confirmed consulting definition.
2. Persona: named and personal, with quotes, feelings and stakes for each stage.
3. Journey map: it uses a "Can we act on it?" column, not "Relevant". It shows what Sphyr does at each stage, and gives a substitute for social proof when there are no reviews.
4. Positioning statement: product plus vision.
5. Message guideline that a junior copywriter and designer can use: the order of what to always say, the proof behind each claim, a never-say list, tone, vocabulary, visual rules and worked examples.
6. Channel plan: zero budget and non-invasive, with an optional paid layer.
7. Acquisition and engagement: how firms are reached, the next step, and how the relationship is kept after the first touch.
8. Deliverable map: from the central message to each artefact's job, angle, journey stage, call to action and channel. It covers the propaganda strategy, all three LinkedIn posts and the ad, including the ad medium.

The **design** teammate owns `docs/design/` and `design-lab/`. In parallel it builds the light and dark tokens from the prototype's UI language, the type, spacing and components, and faux UI of real prototype screens (stageshow). These depend only on the product facts.

**Gate 1a:** the team approves the persona, the message guideline and the deliverable map.

## Phase 1b: three teammates in parallel, after gate 1a

| Teammate | Owns | Produces |
|---|---|---|
| pricing | `docs/pricing/` | It produces:<br>- The consulting value model, with every input sourced or marked as an estimate.<br>- A like-for-like comparison against named competitor plans.<br>- Cost to serve, a fixed-cost breakdown, contribution and break-even.<br>- The price, with the reason for 149 versus 150.<br>- Why the price captures only part of the value.<br>- The pilot amount, length, and what happens without conversion.<br>- The Van Westendorp decision rule. |
| first_use | `docs/packaging/` | It covers only the receiving experience: what builds anticipation before first use, what the first card gives the person who fills it, and the reason to return. Each element states its intended effect and stays within the product facts. |
| design (continues) | `docs/design/`, `design-lab/` | One static homepage mockup in both themes, built from the approved strategy copy. It also ships the canonical nav, footer and theme-toggle markup for every page. |

**Gate 1b:** the team approves the pricing numbers and the homepage mockup. Nothing on `site/` changes before this.

## Phase 2: build, after gate 1b

1. **design** rewrites `site/style.css` and `site/main.js`. That covers tokens, the theme toggle (it follows the system setting and remembers the choice), components, the calculator bug fix, mobile overflow fixes and basic accessibility.
2. Then three page teammates run in parallel. Each owns its files and uses only the step 1 classes and markup.
   - **site_core:** `index.html`, `how-it-works.html`, `demo.html` (including its inline walkthrough data), `trust.html`.
   - **site_commercial:** `pricing.html`, `deliverables.html`, the README strategy table.
   - **deliverables:** `propaganda.html`, `linkedin.html`, `ad.html`.
3. The lead merges each branch into `iteration-a` with `git merge --no-ff`. After each merge the lead rebuilds the root `docs/` index and log.

## Phase 3: review and fix

- One read-only reviewer teammate checks:
  - every page against the brief and rubric;
  - the 15 feedback points;
  - the do-not-claim list;
  - that price and message are consistent across all four deliverables;
  - links, both themes, a 375px width, and keyboard use.
- Fixes go back to the teammate who owns the file. The lead recounts the success number.

**Gate 2:** the team checks the local site with `cd site && python3 -m http.server 8765`, then pushes and redeploys gh-pages itself.

## Rules for every teammate

- Create the branch from `iteration-a` with `wt switch --create d1-<name> --base iteration-a`. Never merge into `main`. Never push.
- Read `docs/` first. Write only the files you own. Rebuild the index only for your own subfolder (`build_index.py --root docs <subfolder>`). Never edit the root `docs/index.md` or `docs/log.md`.
- Write reports, in parts, to `Product-Marketing-final-assignment.swarm/reports/<name>.md`. That folder sits beside the repo, outside git.
- Only one teammate at a time drives the shared Playwright browser.
- No em dashes, no emojis, and no invented features. Use "Sphyr". Never claim "anonymous to everyone": the manager approval queue shows who rated whom.

## Housekeeping

- Add `.playwright-mcp/` and `.claude/worktrees/` to `.gitignore` on `iteration-a`.
- Replace the stale root `final assignment.md` with a pointer to [the canonical brief](../brief/assignment_brief.md).

## Not in scope

- The labelled 2018 pilot evidence stays. No customer quotes, logos or reviews are invented.
- No deliverables are added beyond the four the brief asks for.
