---
type: Handoff
title: "Ad medium research report, phase 1b"
description: "Verified paid, non-invasive ad placements for December 2026 to March 2027 with dates, prices, audience and tracking checks, scored, with a recommendation."
tags: [handoff, admedium]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T18:40:00Z }
---

# Ad medium research report, phase 1b

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Status 2026-11-24: complete. Read-only, nothing booked or contacted. The ad-page rationale paragraph still needs the humanizer pass.

## Plan

Read-only role: no worktree, no repo edits, no Playwright. Only this report file is written.

Inputs read: common.md, admedium.md, deliverable_map.md (ad section), channel_plan.md, communication_objectives_notes.md, persona_head_of_talent.md and segment.md (skimmed), do_not_claim.md.

Steps:
1. Research each candidate with firecrawl and exa (accessed 2026-11-24): People Matters (magazine print/digital, TechHR events), ETHRWorld (newsletter, site), NHRDN chapters (Delhi NCR, Mumbai, Bengaluru, Hyderabad) and national events, SHRM India (2026 conference dates, any 2027 or regional event in Dec 2026 to Mar 2027), IMCI (chapters, convention), consulting-specific media or events, HR or consulting podcasts and newsletters with fixed slots.
2. For each: name, owner, format and size, date or issue in Dec 2026 to Mar 2027, price or "price on request" with media kit URL, audience size and roles, tracking (cookies, pixels, lead capture), URL per fact. Mark unverified fields.
3. Score each against six criteria: reaches Kavya or Vikram in the right mindset, non-invasive, cost fits small paid layer (cap about Rs 1,50,000 per quarter per channel plan), timing in window, fit with a static visual ad for ad.html, consistency with zero-budget-first plan.
4. Recommend one exact placement (outlet, format, size, issue or date), a second choice, and a one-paragraph medium rationale for the ad page.
5. End with `## Final` per common.md.

Open questions for lead (not blocking):
- The deliverable map proposed a free event poster. The class notes say an ad implies paid placement. I treat "paid" as required and score the poster only as a fallback.
- If no outlet publishes prices, should the recommendation still name it with "price on request"? Assumed yes, marked.

## Progress (2026-11-24)

Plan executed without waiting (read-only role, per brief). Tools: firecrawl search and scrape (markdown only; its query and JSON extraction modes failed with "Query generation failed after all models" and "JSON extraction failed"), exa search. All URLs accessed 2026-11-24. Magzter (People Matters digital edition) and nationalhrd.org/events returned 403 or failed to scrape.

## 1. Verified options

Legend: V = read on the cited page today. S = search-result snippet only, page not opened. R = reseller or third-party figure, not the publisher. U = not verified. E = estimate or computed.

| # | Option | Owner | Format and size | Date or issue in window | Price | Audience size and roles | Tracks individuals? |
|---|---|---|---|---|---|---|---|
| A | **NHRD Bangalore Chapter monthly thought-leadership meet**: paid sponsorship with a standee or table | NHRD Network, Bangalore Chapter (not-for-profit, est. 1989) [V, 1] | Sponsorship exists ("for more details / sponsorship / membership write to us") [S, 2]. Standee or table format: U. Standee size: per chapter, on request, U | Meets "every last Thursday of the month" [V, 1]. Last Thursdays: 31 Dec 2026, 28 Jan 2027, 25 Feb 2027, 25 Mar 2027 [E, computed]. 31 Dec is New Year's Eve, likely no meet [E]. Actual dates U | Price on request: reachus@nhrdbangalore.com, +91 95138 85899 [V, 1] | "over 2000 members" [V, 1]; 19,584 LinkedIn followers [S, 2]. Roles: HR professionals across industries. Attendance per meet U | No, if we print a standee and cards with a plain URL and QR code and collect no badges |
| B | **HR Showcase 2026 "The Reset"** (14th edition): exhibitor or partner stall | NHRD Bangalore Chapter [V, 3] | Exhibition area with partners (Gold Sponsor tier exists) [V, 3]. Stall size and tiers U | 4 to 5 Dec 2026, The Lalit Ashok, Bengaluru [V, 3]. 10 days from today | Price on request: reachus@nhrdbangalore.com [V, 3]. Delegate prices exclude 18% GST [V, 3] | "HR professionals, business leaders, and industry experts from across the country" [V, 3]. NHRD members get free 2-day exhibition-area entry [V, 3]. Count U | No, if no badge scanning |
| C | **People Matters daily newsletter banner** (also site banners) | People Matters Media Pvt. Ltd., Gurugram [V, 4] | Newsletter banner in the daily email; also top header, interstitial and floating site banners [R, 5]. Pixel size U | Daily, any December 2026 date [R, 5] | ₹6,300 "per insert", unit unclear [R, 5]. Dedicated email newsletter ₹1,50,000 per newsletter [R, 5]. Sponsored article ₹1,10,000 [R, 5]. Publisher rates on request [V, 4] | Publisher: 150K+ newsletter subscribers, 1.5M+ active users, 2.5M+ monthly views [V, 4]. Reseller says 3L+ subscribers and 80K+ daily visitors [R, 5]; prefer the publisher figure. 2021 kit: engaged audience 54% decision makers; cohorts 31% to 63% CHRO and HR head [V, 6, dated 2021] | Yes, partly. Reseller sells it with "1% to 2% click-through rates" and "performance reporting" [R, 5], so clicks are measured. Site banners run with cookies (U) |
| D | **ETHRWorld Daily Morning Newsletter banner** | Times Internet (ET B2B) [V, 7] | Top banner in the daily email; the 24 Nov 2026 issue carries an Indeed GIF banner [V, 8]. Size U | Daily, any December 2026 date [V, 8] | Price on request: Alliances and Advertising, Tarana Kaushik (tarana.kaushik@timesinternet.in), Ankit Punani (ankit.punani@timesinternet.in) [V, 7] | "community of 2M+ industry professionals" [V, 7]. Newsletter-only count U. Roles: HR professionals, mostly large companies (U) | Yes. Every link goes through `l.php?email=--email--&clid=...` [V, 8], so the publisher logs which subscriber clicked, even if our URL is plain |
| E | **ET Nextech Human Capital India Summit 2027**: exhibitor or partner | ETHRWorld, The Economic Times [V, 9] | Exhibitor or partner tiers (presenting, associate, supporting) [V, 9]. Booth size U | 25 to 26 Feb 2027, The Leela Ambience Gurugram [V, 9] | Price on request; brochure on the page [V, 9] | "100+ Exhibitors, 80+ Eminent Speakers, 2000+ Attendees" (organiser claim) [V, 9]. Who should attend: "CEOs, CHROs, CIOs & Other C-suite Leaders ... Talent & Workforce Transformation Leaders" [V, 9] | Unknown. Organiser registration data exists. No tracking from us if we scan nothing |
| F | **HRKatha print magazine** | HRKatha [V, 10] | Full page ₹1,00,000 per insert; double spread ₹1,71,000 [R, 11] | No issue in the window found. The publisher's store lists "Latest March 2024 edition" [V, 12] | See left [R, 11] | Publisher: "reaching 45,000 HR professionals" [V, 10]. Reseller: readership 225K [R, 11] | No (print) |

Excluded after checking:
- **SHRM India Annual Conference and Expo 2026**: 26 to 27 Nov 2026 [V, 13], before the window. Official venue is YASHOBHOOMI Convention Centre, Dwarka, New Delhi [V, 13]. A third-party listing says Taj Palace [S, 14]; that is wrong. No SHRM India event in Dec 2026 to Mar 2027 found (U).
- **People Matters TechHR Singapore 2027**: 18 Mar 2027, Marina Bay Sands [S, 15]. Wrong country. TechHR India date in the window not found (U).
- **People Matters print magazine**: went monthly in 2020 [S, 16]; 2021 kit said "about 80K+ monthly readers" [V, 6]. Its 2026 advertise page calls it a "digital, subscription-supported publication" [V, 4]. A print issue in Dec 2026 to Mar 2027 is U.
- **IMCI**: 2500+ members, 8 chapters, "annual national conventions" [V, 17]. A "Consultants Forum" e-newsletter exists (June 2026, March 2026 issues) [V, 17]. No paid ad product or event date in the window found (U). Best route stays the Layer 1 talk.
- **Consultancy.in**: its advertising offer is "Partnerships" for consulting firms (profile, jobs, employer branding) [V, 18]. Vendor display ads U. The "over 4 million visitors per year" figure is the whole Consultancy.org network, not India [V, 18].
- **NHRDN National Conference 2027**: 29th edition, hosted by the Delhi and NCR Chapter [S, 19]. Date U, probably after the window, since the 2026 edition ran 25 to 26 June [S, 20].
- **Podcasts or newsletters with fixed reads** (HR or consulting, India): none with a public slot or rate found. Searched once; not exhaustive.
- **NHRD Journal ads (Sage)**: a rate card exists [S, 21]. It is an academic journal with low reach and no fit. Not scored.

Audience caveat: every option reaches HR in general, mostly at large companies. None is specific to 40 to 400 person consulting firms. The share of readers or attendees who are heads of talent at homegrown consulting firms is unknown and likely small (guess).

### Sources (all accessed 2026-11-24)
1. https://nhrdbangalore.com/nhrd-bangalore/
2. https://in.linkedin.com/company/nhrdbangalorechapter (search snippet)
3. https://hrshowcase.in/
4. https://www.peoplematters.in/advertise-with-us
5. https://www.themediaant.com/digital/peoplematters-advertising (reseller)
6. https://pm1-31ef.kxcdn.com/docs/media-kits/People_Matters_Media_Kit_2021.pdf
7. https://hr.economictimes.indiatimes.com/contact_us.php
8. https://hr.economictimes.indiatimes.com/newsletter (24 Nov 2026 issue)
9. https://hr.economictimes.indiatimes.com/nextech
10. https://www.hrkatha.com/partner-with-us/
11. https://www.themediaant.com/magazine/hr-katha-magazine-advertising (reseller)
12. https://www.hrkatha.com/magazine-subscriptions/
13. https://www.shrmconference.org/iac/
14. https://growthacademyasia.com/event/shrm-india-annual-conference-expo-2026/ (search snippet)
15. https://singapore.techhrconference.com/purchase (search snippet)
16. https://www.peoplematters.in/article/performance-management/people-matters-goes-monthly-259 (search snippet)
17. https://imcindia.co.in/
18. https://www.consultancy.in/advertise
19. https://in.linkedin.com/company/nhrdn-delhi-ncr-chapter (search snippet)
20. https://www.instagram.com/p/DVNmnjkEY8Y/ (search snippet)
21. https://services.sagepub.com/browse-rate-cards/ (search snippet)

## 2. Scoring

Scale per criterion: 2 = good, 1 = partial or unknown, 0 = fails. Six criteria, maximum 12. Scores are judgement on the facts above, not measured.

| Option | Reaches Kavya or Vikram in the right mindset | Non-invasive | Cost fits small paid layer | Timing in window | Fits a static visual ad (ad.html) | Fits zero-budget-first plan | Total |
|---|---|---|---|---|---|---|---|
| A. NHRD Bangalore monthly meet, sponsored standee | 2: a room she chose, peers, learning mode. HR from all industries, not consulting-specific | 2: print and QR to a plain URL | 1: price unknown; guess it fits the ₹50,000 to ₹1,50,000 event cap | 1: 28 Jan 2027 (computed) is inside the window but after the plan's December ad slot | 2: same portrait poster design as the gate 1a proposal | 2: paid version of Layer 1 channel 4; disclosed as Sphyr | **10** |
| B. HR Showcase 2026, smallest exhibitor or partner slot with a standee | 2: same as A, larger and national | 2: if no badge scan | 1: price unknown; a 2-day national event may exceed the cap (guess) | 1: 4 to 5 Dec matches the plan, but only 10 days of lead time | 2: standee or stall backdrop | 2: same as A | **10** |
| C. People Matters newsletter banner | 1: inbox skim of daily HR news; broad audience | 1: publisher measures clicks | 2: ₹6,300 per insert (reseller, unit unclear) | 2: any December day | 1: small banner; QR useless in email | 1: Layer 2 allows a newsletter, but its "no tracking links" rule fails at the publisher | **8** |
| F. HRKatha print, full page | 1: broad HR | 2: print | 1: ₹1,00,000 (reseller) | 0: no issue in the window found | 2: full page | 1 | **7** (fails on timing) |
| D. ETHRWorld newsletter banner | 1: broad, large-company HR | 0: per-subscriber click redirect, verified | 1: price on request | 2: any December day | 1: small banner | 1 | **6** |
| E. ET Nextech 2027 exhibitor | 1: CHRO and C-suite at large firms; a 40 to 400 person firm's head of talent is less likely there (guess) | 2: if no badge scan | 0: likely far above cap (guess) | 1: late February, too late for the trigger job | 2: booth graphics | 0: big-ticket expo spend clashes with the plan | **6** |

A and B tie on score. B wins on timing if it can be booked this week; A wins on cost risk and lead time. Both use the same creative, so the choice does not change the ad design.

## 3. Recommendation

**Recommended placement:** a paid sponsor standee at an NHRD Bangalore Chapter gathering, booked as the smallest sponsor or exhibitor option on offer. First target: **HR Showcase 2026, 4 to 5 Dec 2026, The Lalit Ashok, Bengaluru**. Format: one portrait roll-up standee carrying the ad, plus A6 handout cards with the same design. Standee size: per the organiser's specification, on request, not verified. Decision gate: book only if the chapter confirms a slot and a price within ₹1,50,000 by 27 Nov 2026 (estimate of the latest workable date for printing). No badge scanning, no lead form, QR to a plain URL.

**Second choice:** the same standee and cards as a paid sponsor at the **NHRD Bangalore Chapter monthly thought-leadership meet on Thursday 28 Jan 2027** (date computed from "every last Thursday"; confirm with reachus@nhrdbangalore.com). If the Delhi and NCR, Mumbai or Hyderabad chapters offer a December or January meet sponsorship, the same creative fits; their sponsorship terms were not found.

**Not recommended, but the only digital option that could pass:** a People Matters daily newsletter banner in mid December 2026. Use it only if the lead accepts publisher-side click measurement. ETHRWorld is ruled out on tracking.

**Medium rationale for the ad page (draft public copy; must go through the humanizer before it ships):**

> This ad is planned as a paid standee, with matching handout cards, at HR Showcase 2026 in Bengaluru on 4 and 5 December, an event run by the National HRD Network's Bangalore chapter. Heads of talent go there to learn from each other, so the ad meets them where they already listen to peers. It tracks nobody. There is no pixel, no badge scan and no form. The QR code opens a plain web address for the 2-minute walkthrough. Anyone curious can look, and anyone else can walk past. December leaves time for a firm to try a different record before the April round. Paying for a place at a chapter event does not mean the chapter endorses Sphyr.

Geography note: Kavya's composite firm is headquartered in Gurugram with offices in Mumbai and Bengaluru (persona_head_of_talent.md, line 29). Bangalore is picked only because it is the one chapter with verified dates and a sponsorship contact. Once its terms are known, the NHRDN Delhi and NCR Chapter (about 2,300 members per the channel plan) is the better target for the same creative. The rationale paragraph should then name that chapter instead.

## Final

**Files written and commit SHAs.** Only this report: `Product-Marketing-final-assignment.swarm/reports/admedium.md`. No commits; read-only role, no worktree.

**Key insights and findings (sources in section 1, accessed 2026-11-24).**
- SHRM India IAC 2026 is 26 to 27 Nov 2026 at YASHOBHOOMI, New Delhi [13]: outside the window. The channel plan cites it; that row should be dropped or moved.
- ETHRWorld's daily newsletter wraps every link in a per-subscriber redirect (`l.php?email=--email--&clid=`) [8]. A plain URL does not stop the publisher tracking who clicked. This breaks the channel plan's Layer 2 assumption that a newsletter slot can be non-invasive.
- People Matters lists 150K+ newsletter subscribers and 1.5M+ active users [4]. A reseller lists a newsletter banner at ₹6,300 per insert and a dedicated mailer at ₹1,50,000 [5]. The reseller also sells click-through reporting.
- HRKatha claims print reach of 45,000 HR professionals [10], but its store's latest edition is March 2024 [12]. Treat print as not running.
- People Matters print in 2026 is unverified; its own page now calls it a digital publication [4].
- NHRD Bangalore has 2000+ members and meets every last Thursday [1]; sponsorship exists by email [2]. HR Showcase 2026 runs 4 to 5 Dec 2026 in Bengaluru with an exhibition area [3].
- ET Nextech Human Capital India Summit is 25 to 26 Feb 2027 in Gurugram, aimed at CEOs and CHROs, with 2000+ attendees claimed [9].
- No paid ad product found for IMCI or Consultancy.in. No HR or consulting podcast or newsletter with a public fixed-read rate found.
- No option targets 40 to 400 person consulting firms. All reach HR broadly.

**Decisions made and why.**
- Treated "paid" as required for the ad, per the class notes ("money is involved"). The free poster from gate 1a becomes the creative for a paid standee, so no design work is lost.
- Ranked tracking above reach, per the channel plan's "never do" list. That moved both newsletters below the event standee.
- Preferred publisher figures over reseller figures where they conflict.

**Approaches rejected and why.**
- ETHRWorld newsletter: per-subscriber click tracking, verified.
- ET Nextech: late February, likely above cap, and aimed at large-company CXOs.
- HRKatha and People Matters print: no issue in the window verified.
- SHRM IAC 2026: before the window. TechHR Singapore: wrong country.
- LinkedIn sponsored post: not re-researched; the gate 1a map already scored it weakest on tracking.

**Open questions for the lead.**
1. Accept a January date (28 Jan 2027) as the fallback, given the plan puts the ad in December?
2. Is anyone on the team an NHRD member? Members get free exhibition-area entry at HR Showcase [3], which helps staffing a stand.
3. Will the lead contact reachus@nhrdbangalore.com for sponsor terms? That would turn the price from unknown into a quote. Outward contact needs the lead's or user's approval.
4. Should the ad page show the placement as planned ("would run at") rather than booked? Recommended: say "planned", since nothing is booked.

**What I did not verify.**
- Any sponsor or stall price at NHRD Bangalore or HR Showcase; whether a small standee-only option exists; standee dimensions.
- Actual NHRD Bangalore meet dates for Dec 2026 to Mar 2027 (computed only).
- Monthly meet sponsorship terms for the Delhi and NCR, Mumbai and Hyderabad chapters (nationalhrd.org/events failed to load).
- People Matters' own rates, the unit of the ₹6,300 banner price, banner pixel sizes, and whether People Matters' newsletter wraps links per subscriber (inferred from the reseller's CTR reporting).
- Attendance per chapter meet and the share of attendees from consulting firms.
- Whether People Matters still prints a magazine.
- The rationale paragraph has not been through the humanizer. It is written as planned, not booked, and must stay that way unless a booking happens.
- Facts marked S come from search snippets only; the pages were not opened.
