---
type: Guideline
title: "Faux UI placement"
description: "Which Sphyr prototype screens appear where on the site, how each is cropped and labelled, and every copy change made from the prototype."
tags: [design, faux-ui, prototype]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T17:04:27Z }
status: draft
commit: e3e82ae
sources:
  - resource: "https://sphyr-prototype.raviwarrier.com/"
    title: "Sphyr prototype, viewed 2026-11-24 at 1280px in light and dark"
  - resource: "docs/product/prototype_screens.md"
  - resource: "design-lab/faux-ui.html"
  - resource: "~/.claude/skills/stageshow/references/framing.md"
---

# Faux UI placement

Product views are real screens from the Sphyr prototype, rebuilt in HTML and CSS in `design-lab/faux-ui.html` (styles in `design-lab/faux-ui.css`). They are not screenshots, so they follow the site theme and stay sharp. Screen content is described in [prototype screens](../product/prototype_screens.md). Style rules are in the [design system](design_system.md) and the [slop rules](slop_rules.md).

## Rules for every frame

- Show only screens and states that exist in the prototype. Keep its layout, labels and microcopy.
- Put this label directly under every frame, outside it: "Prototype screen. Sample data, fictional people."
- Crop past the prototype's icon rail and navigation sidebar. They carry the green sparkle app icon, which reads as an AI mark, and the demo user card.
- One hero surface per frame, at most one satellite. A satellite may cover chrome or filler, never a name, a score or a sentence.
- Every real word stays whole. Only filler (chart foot, placeholder bars, card padding) is cut or faded.
- Each frame has a compact design for a 358px phone column, switched by a container query. Satellites move or drop; words stay whole.
- Frames are wrapped in `role="img"` with an `aria-label` that states what the screen shows, except the interactive feedback card, which is a real radio group.

Method: the framing and craft rules of the stageshow skill (`references/framing.md`, `references/craft.md`), ported by hand to plain CSS. The stageshow kit, its film script and its rehearsal gate were not used, because the site has no build step.

## Where each frame goes

| Frame | Page and slot | What it shows the head of talent |
|---|---|---|
| Giving feedback | Home hero right column, or the walkthrough | Rating a colleague is a few clicks, and responses are private by design |
| What the person rated sees | How it works | The rated person gets a trend and specific, anonymized comments, not one verdict |
| What a manager sees | Home (lower) or how it works | A manager sees team patterns and who needs support, from many raters |
| Team against the organization | How it works, beside the manager view | Team results are compared with the organization on the same seven dimensions |
| Edit approvals, shown honestly | Trust | The one place a manager sees who gave feedback to whom |

## The frames

### Giving feedback
- Source: Provide Feedback (`/feedback`), the person card and the "Private by design" card from the right rail.
- Composition: the card sits one gutter in from the top and sides and is cut by the stage's bottom edge inside its own padding. The Previous and Submit footer is left out rather than sliced. "Private by design" straddles the card's top edge over the empty side of its header row.
- Interaction: the three answers are real radio buttons. "Was good" shows "What stood out?"; "Could improve" shows "Where did you experience friction?"; "No interaction" shows no second step, as in the prototype. CSS only, no script.
- Real strings: the question, the three answers, the step heading, the VBA chips, "Private by design" and its sentence.

### What the person rated sees
- Source: member Insights (`/`).
- Composition: the window is inset one gutter and runs past the stage's bottom edge, fading over the chart foot. It shows the page header, three of the four score tiles (the cycle progress tile is left out) and the overall trajectory. The Jul 22 anonymized comment is the satellite, over the chart's right end, crossing the window's right edge.
- Real strings: page title and subtitle, the three tiles, "Overall trajectory", "Improving", the comment.

### What a manager sees
- Source: manager Team Insights (`/manager?view=team-insights`).
- Composition: the window alone, whole across, fading at its foot over a placeholder card. No satellite: any card over this window would cover a name or a score. Shows the page header, three of the four header tiles (team score, participation, edit requests) and Team Standouts.
- Compact: one standout list (top performers) is shown; members needing support is dropped.

### Team against the organization
- Source: the "Team vs. Organization Benchmark" card on the same screen, radar view.
- Composition: the card whole, in a well, for a column beside copy.

### Edit approvals, shown honestly
- Source: "Feedback edit approvals" on the same screen. Two of its three sample requests are shown.
- Composition: the whole card, never cropped.
- Caption, above the sample label: "In the prototype, a manager approving an edit request sees who gave the feedback and to whom. Ratings are pooled and comments are anonymized to the person rated."

## Copy changes from the prototype

People and team names are neutral placeholders until the persona copy is final. When the strategy files land in `docs/strategy/`, replace the placeholders below with the consulting sample people, roles, team name and VBA tags from there. Only the names, roles, team and tag text change; layout and microcopy stay.

| Frame | Prototype | Site now | Why |
|---|---|---|---|
| Giving feedback | Lucas Martin, UX Researcher · Peers | Member B, Senior consultant · Peers | Demo names must not appear; consulting role |
| Giving feedback | "Sphyr UI / UX VBAs" | "Engagement team VBAs" | Team name is sample data |
| Giving feedback | VBA tags (Transparency, Customer First, and so on) | Unchanged for now | Placeholder until consulting tags arrive from strategy |
| What a manager sees | Maya Chen 86, Arjun Mehta 82, Theo Brooks 76, Lucas Martin 79 | Member A 86, Member B 82, Member C 76, Member D 79 | Demo names; scores and tags unchanged |
| What a manager sees | Product Designer, Senior Engineer, Visual Designer, UX Researcher | Consultant, Senior consultant, Analyst, Associate | Consulting roles |
| Edit approvals | Maya Chen to Arjun Mehta; Leila Haddad to Lucas Martin | Member A to Member B; Member C to Member E | Demo names; reasons unchanged |
| All frames | Uppercase green eyebrow in #009163 | Same text in #007652 | #009163 small text fails AA (3.83:1) |
| Insights chart | Area line from the prototype's sample data | Curve traced by eye, May 05 to Jun 30 labels | Exact values are not in any source |
| Benchmark radar | Two near-equal shapes | Shapes traced by eye | Exact values are not in any source; caption says so |

Em dashes: the prototype's Jul 18 member comment joins two clauses with an em dash. It is not used on the site. If it is used later, replace the dash with a full stop: "Strong partnership this cycle. You connected customer evidence to the design decision without overcomplicating it." The page titles with an em dash ("Performance Insights" and others) are not shown in any frame.

## Not verified

- The icon the prototype uses for "Members Needing Support" was matched by eye to Lucide `trending-up`.
- The compact frames were reviewed at 358px inside a 1280px page and at a 375px viewport, in light theme only for the compact row.
