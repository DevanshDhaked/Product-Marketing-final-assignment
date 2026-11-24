---
type: Research Note
title: "Brief compliance and feedback carry-over"
description: "Pass, partial or fail for each brief requirement, and whether each professor feedback point is fixed on the site."
tags: [site, audit, feedback]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
commit: fc85cac
sources:
  - resource: "site/"
  - resource: "brief/assignment_brief.md"
  - resource: "brief/professor_feedback.md"
---

# Brief compliance and feedback carry-over

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Paths are relative to `site/`. Audit of commit fc85cac on 2026-11-24.

Legend: PASS / PARTIAL / FAIL. Brief line numbers refer to `sphyr/PMM M26 Product Marketing - Final Assignment.md`.

## Required artefacts (brief:14-29, 41-48)
| Requirement | Verdict | Evidence |
|---|---|---|
| Website as central hub | PASS | Nav pill "Deliverables (4)" on every page (index.html:21); deliverables strip on home (index.html:51-59); hub page deliverables.html:28-33; footer links on every page (index.html:135). |
| Propaganda strategy | PASS | propaganda.html, 13 sections covering audience, belief, message, tactics, channels, rationale, link to positioning, expected response (brief:142-152 all mapped: 42, 57, 67, 78, 91, 134, 138). |
| Three LinkedIn posts | PASS | linkedin.html:33, 72, 118, each with purpose, audience, angle, CTA. |
| One advertisement | PASS | ad.html:32-57 creative + rationale 59-72. |
| No sign-in, links work | PASS | Local check: 0 broken hrefs/srcs/anchors across 9 pages. Live: 200 for /, all 9 pages and style.css (curl, 24 Nov). `git diff origin/gh-pages HEAD:site` is empty, so live = HEAD. |

## Assessment areas (brief:62-114)
| Requirement | Verdict | Evidence |
|---|---|---|
| Deliberate segment | PASS with a flaw | 50 to 300 founders + anti-segment (propaganda.html:45, 50-55). Flaw: persona is at a 350-person company, outside the band (propaganda.html:111), and ad targeting includes 201 to 500 (ad.html:63, propaganda.html:95). Devansh_notes.md:43 flagged this as open; it was rationalised, not fixed. |
| Persona guides message, language, channel, CTA | PARTIAL | Explicit mapping table (propaganda.html:112-120) is good. But on the public site Meera appears only as 4 short third-person cards (index.html:85-88); the professor called the earlier journey "distant and indifferent". |
| Needs, motivations, concerns, decision process | PARTIAL | Concerns covered well (objections propaganda.html:147-155, trust page). Decision process (champion -> founder) stated (propaganda.html:45-46). Motivations of the founder beyond "fairness" are thin; no "what is it costing me" anchored in numbers he trusts. |
| Journey: artefacts move awareness -> action | PASS | Stage table (deliverables.html:45-50; propaganda.html:124-130); posts link to successive destinations (linkedin.html:57, 103, 146; table 164-169). |
| Clear positioning, value, differentiation | PARTIAL | Statement at propaganda.html:135 and "two-minute, anonymous, everyone" (propaganda.html:75). Differentiation vs named alternatives (annual review, Lattice, HRMS modules) is shown only in one pricing `<details>` (pricing.html:81). No "versus what you do today" comparison on the site. |
| One central message across all artefacts | PASS with a gap | Promise + core line on home, demo, ad, Posts 2 and 3. Claim "All three end on the same promise" (linkedin.html:27) and "Every artefact... all three LinkedIn posts" (propaganda.html:70) is false for Post 1: its body ends on a question (linkedin.html:53); the promise only appears in the mock profile subtitle (linkedin.html:35). |
| Pricing and packaging consistent | PARTIAL | Price, pilot, refund, renewal match across pricing, Post 3, ad, deliverables. Mismatches: ad shows "₹149 / employee / mo billed annually" with no "+ GST" (ad.html:49) while rationale says "exactly as on the pricing page" (ad.html:68); pilot "one team of up to 25" from the pricing PDF is missing on the site; pricing PDF includes "OKRs and AI feedback summaries", site does not (site may be right per brief:35 "do not invent features", but the inconsistency is visible to a grader who has the PDF); FX ₹93 on site vs ₹95 in PDF (pricing.html:81). |
| Acquisition path and meaningful next step | PASS | Walkthrough (no sign-up) -> pilot order (demo.html:85, pricing.html:89-99). |
| Engagement after first interaction | PARTIAL | Product habit (propaganda.html:132), guided setup, renewal reminder, first-renewal credit. Nothing about what the buyer or employees get between cycles (reports, digests, quarterly reviews), and "email after the walkthrough" (propaganda.html:98) conflicts with a walkthrough that collects no email (see below). |
| Claims do not conflict with product | PARTIAL | Honest labels are strong. Internal contradictions: (a) pricing.html:88 "If you tried the walkthrough, we carry your details over" and propaganda.html:98 email follow-up, but the walkthrough asks for no details ("No sign-up", index.html:30); (b) linkedin.html:170 says people who saw Post 1 "already recognise the one-vs-Sphere image", but Post 1 has no image; the image first appears in Post 2 in the same week as the ad; (c) index.html:104-111 groups Galton 1906 under the eyebrow "Evidence · 2018 pen-and-paper pilot". |

## Website guidance (brief:118-135)
| Item | Verdict | Evidence |
|---|---|---|
| Audience and value clear | PASS | Hero eyebrow + lede (index.html:26-28). |
| Positioning + central message | PASS | index.html:27, 130. |
| Order makes sense to customer | PASS | Problem -> contrast -> story -> how -> evidence -> price -> CTA (index.html sections 3-9). Minor: the deliverables strip sits second, between hero and problem, breaking the customer flow (index.html:51-59). Defensible for grading. |
| Reflects persona and journey | PARTIAL | See persona row above. |
| Appropriate CTAs | PASS | Walkthrough primary everywhere, pilot secondary. |
| Working links to all deliverables | PASS | See above. |

## Propaganda guidance (brief:139-156)
PASS on structure. Every brief bullet has a section. Weak points: channel rationale ignores budget and ethics of retargeting (see section 4); "why this tactic" column is good (propaganda.html:79-89).

## LinkedIn guidance (brief:160-174)
PASS on distinct purposes (problem / belief / offer, linkedin.html:164-169). Gaps: Post 1 has no promise line (contradicts linkedin.html:27); "Tuesday mornings when professionals are most active" is unsourced (linkedin.html:170); posts are from the brand page only, no founder or employee voice, although propaganda.html:47 names quiet contributors as amplifiers.

## Ad guidance (brief:178-191)
PASS. Clear message, benefit, medium rationale, CTA rationale. Gaps: "+ GST" missing (ad.html:49); visible LinkedIn button says "Learn more" while the rationale sells "See the pooled view in 2 minutes" as the CTA (ad.html:53-54, 67), which is acceptable since LinkedIn buttons are fixed labels, but say so; the ad is an HTML mock, not an exported 1080x1080 image as claimed (ad.html:27).

## Final checklist (brief:341-356)
| Item | Verdict |
|---|---|
| Website complete and accessible | PARTIAL. Complete, but visible "(Offer pending faculty confirmation.)" at pricing.html:71 reads as unfinished. Mobile overflow on 3 pages (section 6). |
| Communicates product and value | PASS |
| Clear links to all deliverables | PASS |
| Propaganda complete with reasoning and tactics | PASS |
| Three posts included and accessible | PASS |
| Ad included and accessible | PASS |
| Consistent with central message | PARTIAL (Post 1, ad GST, FX, OKR/AI features) |
| Reflects segment, persona, journey | PARTIAL (350-person persona, 201-500 targeting) |
| Pricing, packaging, acquisition, engagement | PARTIAL (see section 4 pricing items) |
| All links work, permissions open | PASS |
| One website link | PASS (README.md:6) |
| By 23:59 27 Nov | Pending |

Other notes:
- The brief spells the product "Spyhr" (brief:31, 33); the site, README and course docs use "Sphyr". Note only, not a fail; consider one line in the footer if the grader is literal.
- Scullen, Mount & Goff 2000 "62% and 53%" is still marked unverified in devansh_notes.md:157 yet appears at index.html:76, linkedin.html:86, propaganda.html:73, 83. The site's own guardrail (propaganda.html:160) makes an unverified figure a credibility risk. Status: VERIFY, not known wrong.
- Lattice "$10 per seat per month" (pricing.html:81) not verified in this audit.

---

## 4. Feedback carry-over

## Pricing (70/100)
| Feedback point | Status | Evidence |
|---|---|---|
| ₹667 value: show how one avoided resignation becomes ₹500 per employee per month | NOT addressed | pricing.html:80 says only "estimated from two things... attrition-cost data... time-cost method". No arithmetic, no headcount, no salary, no attrition rate. Weaker than the PDF, which at least named the ₹500 + ₹167 split. propaganda.html:164 "No fear selling about attrition numbers we can't support" sits awkwardly next to an unsupported attrition-based value. |
| Competitor comparison: name plans and basis | PARTIAL | One named plan with date and FX: Lattice Performance $10/seat at ₹93/USD, checked 24 Nov 2026 (pricing.html:81). PDF used three vendors at ₹95. No like-for-like feature basis. FX disagrees with the PDF. |
| ₹150 vs ₹149, and why capture only ₹149 of ₹667 | NOT addressed | "₹149 sits on that floor" (pricing.html:79) is wrong on its face: ₹149 is below a ₹150 floor (79.9% margin). "At ₹149 you keep most of that value" (pricing.html:80) restates the choice without a reason (penetration, proof-building, charm price, market anchor). |
| Break-even: ₹8L fixed-cost breakdown, ₹119 includes all variable costs | NOT addressed | Only "break-even is about 67 customers of 100 employees" (propaganda.html:145). No fixed-cost line items on the site at all. |
| Pilot: why ₹15,000, why six weeks, what if no conversion | NOT addressed | pricing.html:67 states the offer only. Six weeks = three cycles is implied but not argued. No non-conversion terms. Also unexplained: the PDF caps the pilot at 25 people; 25 x ₹149 x 1.5 months = about ₹5,600, so the pilot costs about 2.7x list. That premium needs a reason (setup cost, commitment signal). Separately, the refund window is 6 cycles / 12 weeks on the annual plan (pricing.html:68) vs a 3-cycle pilot; readers may confuse the two. |
| Van Westendorp: how results drive the decision | NOT addressed | Van Westendorp is absent from the site (grep: 0 hits). |

## Packaging (69/100)
| Feedback point | Status | Evidence |
|---|---|---|
| Too much reassurance, not enough excitement / anticipation | NOT addressed | Site tone is reassurance-heavy: "Low risk to try" (pricing.html:65), refund (index.html:124), trust page, "No surprise renewals". Nothing builds anticipation before first use (e.g. "your first pooled view arrives on day 28", a founder preview of what they will learn, a launch moment for employees). |
| Acquisition content mixed into packaging | N/A for final brief, but note | The final rubric does reward acquisition, so AIDA content is fine here. |
| First-use experience: what does the user get from the first card | NOT addressed | The done state of the card says the rating joins Priya's Sphere and is anonymous (index.html:45; demo.html:61 "Pooled with everyone else's..."). No reward for the reviewer: no "you're one of 9 voices for Priya", no view of feedback they themselves will receive, no reason to return. The demo rewards the founder (step 3), not the employee. |
| Liked the interactive demo and employee focus | KEPT | demo.html 4-step walkthrough; card on home. |

## Segmentation, persona, journey, messages, channels (63/100)
| Feedback point | Status | Evidence |
|---|---|---|
| Journey: "Can we do anything about it?" framing, not "Relevant" | NOT addressed on site | The site journey (index.html:85-88; propaganda.html:124-130; deliverables.html:45-50) lists stages and metrics. No per-touchpoint "what can we do" column. The "company grows to 120" type of touchpoint (feedback.md:57) still appears as a given ("Nobody did anything wrong. The company just grew." index.html:64) with no intervention. |
| No reviews for a new product: how to provide social proof | PARTIAL | First-25 case-study trade (pricing.html:71; propaganda.html:88). Research authority (Galton, Scullen) and 2018 method pilot. Missing: anything a buyer can check today (founder-to-founder references, pilot customers' public notes, open methodology, a named advisor). |
| Journey map not personal, distant | NOT addressed | Meera = four 30-word third-person cards (index.html:85-88). No quotes, feelings, stakes, or moments in her week. |
| Message is a slogan, not a guideline for copywriters/designers | PARTIAL | Message hierarchy (promise / core line / proof points / RTBs, propaganda.html:68-74), word rules (propaganda.html:75), fallback (76), tone notes (119), guardrails (157-165). Still missing a usable brief: do/don't phrases, words to avoid, one example per format, visual rules for the one-vs-Sphere device. |
| No money and no creepy tactics: change the channel list | NOT addressed, arguably worse | Plan depends on paid LinkedIn Sponsored Content (propaganda.html:95; ad.html:62) plus retargeting of site visitors and post engagers (propaganda.html:106; linkedin.html:170; ad.html:63). Retargeting is the "stalking" pattern the professor named. No budget figure anywhere. Zero-budget channels (founder communities, HR forums, guest posts, employees as amplifiers, the walkthrough as a shareable link) exist only as "planned, phase 4" (propaganda.html:97). Also clashes with the site's own "Feedback, not surveillance" stance (trust.html:51). |

---
