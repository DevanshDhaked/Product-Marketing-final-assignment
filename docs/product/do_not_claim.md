---
type: Research Note
title: "Do-not-claim list"
description: "Claims the sources do not support, such as integrations, AI, certifications and customers, that marketing must not make."
tags: [claims, guardrails]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
sources:
  - resource: "sphyr/Sphyr.io Product Documentation.pdf"
  - resource: "https://sphyr-prototype.raviwarrier.com/"
---

# Do-not-claim list

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Source keys:
- DOC = `Sphyr.io Product Documentation.pdf` (7 PDF pages, "Product Guide: Sphyr", created 2026-09-17 in ONLYOFFICE). Page numbers are PDF pages.
- WP = `Sphyr Overview Whitepaper v0.3.pdf` (9 pages with content, dated "December 2018", footer "Private and Confidential. © 2018 Ravi Warrier"). Cited as WP pN (printed page N). Printed page 1 = PDF page 3, printed page 7 = PDF page 9.
- PROTO = https://sphyr-prototype.raviwarrier.com/ (live, scraped 2026-11-24).
- BRIEF = `PMM M26 Product Marketing - Final Assignment.md`. Note: the brief spells the product "Spyhr" (line 33). All product sources, logo and prototype spell it "Sphyr". Use "Sphyr".


Not supported by DOC, WP or PROTO. Do not state as current capability:
1. Integrations of any kind: HRMS/HRIS (Workday, BambooHR, SAP, Darwinbox, etc.), payroll, Slack, Microsoft Teams, Google Workspace, Jira, calendar, SSO/SAML/SCIM, API or webhooks. Only supported: CSV/XLS/XLSX member import and domain signups (PROTO 3.10), email invites for external sphere members (DOC p5). The word "Seamless Integration" in DOC p4 means merged VBA lists on the card, not software integration. "v2.0 API integrations" and "webhook listener" in PROTO are demo task data.
2. AI or machine learning as a current feature. "AI-assisted" natural language queries and automated coaching are roadmap (DOC p5-p6). The PROTO summary callout has a sparkle icon but no source calls it AI.
3. Roadmap items as live: Personal Reflection Journal, Automated Coaching & Counseling, Ad-Hoc Guidance (pulse) Surveys, Natural Language Data Queries, Audit-Ready Policy Generator.
4. Pricing figures, tiers, free trial, freemium, per-seat price as facts from the sources. The BRIEF (line 98-104, rubric line 306) requires the team to apply its own pricing and packaging decisions; present those as our proposal. Source facts only: license-based SaaS, "flat-fee for a range of licenses (users)" including "business support, training and training materials, set up and configuration support and flexible billing" (WP p6-p7).
5. Security or compliance: SOC 2, ISO 27001, GDPR/DPDP compliance, encryption, data residency, uptime SLA, audit readiness. (Audit-Ready Policy Generator is roadmap.)
6. Specific anonymity mechanics: minimum response thresholds, k-anonymity, "even admins cannot see", "untraceable". PROTO shows managers see who gave feedback to whom in edit approvals (3.7). Safe line: PROTO copy "Individual responses are normalized and grouped before anyone sees them."
7. Scoring algorithm details or "bias-free" / "eliminates bias" as a guarantee. WP p2 heading says "Eliminating Bias" but the text says it gives "a more accurate view". Prefer "reduces single-manager bias".
8. Customer logos, named customers, testimonials, user counts, funding, awards, case studies beyond the anonymous 2018 four-company pilot (Co. A-D, unnamed).
9. Pilot results as software results. The pilot was "paper and pen" (WP p4). Do not generalize percentages to "Sphyr customers see X".
10. Mobile apps (iOS/Android), offline use, browser extensions, multilingual support, accessibility certification.
11. Automatic payroll, bonus or compensation calculation. DOC p5 says leadership "can query crowdsourced data" for promotion decisions; it does not compute pay.
12. Replacing managers or HR. Manager still approves edits, sets team VBAs and OKRs.
13. "Real-time" data as a literal claim. Feedback is collected per cycle (fortnightly default). DOC uses "real-time visibility" loosely; prefer "every cycle" or "every two weeks".
14. Self-appraisal module. DOC p1 criticizes self-appraisal; no self-review screen exists.
15. Gamification beyond what exists. PROTO shows only a "4-cycle streak · 8 weeks" pill and progress counters. No badges, leaderboards or points.
16. Leadership "Who Should We Promote?" as a visible screen. It is described (DOC p5) but not in PROTO. If mocked, label it as described in the product guide.
17. The PDF/PROTO demo names (John Smith, Maya Chen, "Sphyr UI / UX" team, Northstar) as real people or clients.

---

## Method notes and gaps
- Prototype routes: `/`, `/sphere`, `/feedback`, `/objectives`, `/manager?view=member-insights|team-insights|team-tasks`, `/teams?section=profile|roster|vbas|okrs`, `/admin?view=directory|vbas|frequency|okrs`. 15 screens captured. The JS route bundle confirms only 7 top-level paths (`/`, `/sphere`, `/feedback`, `/objectives`, `/manager`, `/teams`, `/admin`): no login, leadership, pricing or settings route exists.
- Root meta (index bundle): title "Sphyr — Continuous 360° Feedback", description "Continuous, anonymized 360-degree feedback powered by your Sphyr."
- Notifications panel (from bundle): "Feedback reminder: 3 reviews remaining for this fortnight cycle" ("Due Friday", constructive tone); "Feedback received: You received 4 new items of Anonymized ..."; empty state "All caught up".
- Manager member drill-down (from bundle strings, not seen rendered): "Overall trajectory comparison"; radar "Member, role/designation, and organization across seven dimensions"; "Performance dimensions" / "Current normalized member scores"; "Top feedback received" / "Most frequent positive anonymized signals"; "Improvement areas" / "Recurring constructive signals to coach"; "Anonymized Feedback". Edit rejection flow: "Confirm rejection", "Optional reason for rejection". Responsibility detail: "Task under responsibility", "Task updates", "Working notes", "Activity thread", "Add manager comment". Empty states: "There are no feedback edit requests waiting.", "This team has no members yet.", "No responsibilities match these filters."
- Not captured rendered: manager per-member drill-down and notification panel (copy recovered from bundle above), dropdown option lists for status/priority, dark-mode screenshots, mobile layout.
