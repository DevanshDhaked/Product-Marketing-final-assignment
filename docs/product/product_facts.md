---
type: Research Note
title: "Product facts"
description: "What Sphyr is and how it works according to the product documentation and whitepaper, with page citations, roadmap items marked as not current."
tags: [product, facts]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
sources:
  - resource: "sphyr/Sphyr.io Product Documentation.pdf"
  - resource: "sphyr/Sphyr Overview Whitepaper v0.3.pdf"
---

# Product facts

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Source keys:
- DOC = `Sphyr.io Product Documentation.pdf` (7 PDF pages, "Product Guide: Sphyr", created 2026-09-17 in ONLYOFFICE). Page numbers are PDF pages.
- WP = `Sphyr Overview Whitepaper v0.3.pdf` (9 pages with content, dated "December 2018", footer "Private and Confidential. © 2018 Ravi Warrier"). Cited as WP pN (printed page N). Printed page 1 = PDF page 3, printed page 7 = PDF page 9.
- PROTO = https://sphyr-prototype.raviwarrier.com/ (live, scraped 2026-11-24).
- BRIEF = `PMM M26 Product Marketing - Final Assignment.md`. Note: the brief spells the product "Spyhr" (line 33). All product sources, logo and prototype spell it "Sphyr". Use "Sphyr".


## 1.1 What Sphyr is
- WP p6: "Sphyr's performance review application is a license-based SAAS offering that allows companies, small or large to leverage a de-centralized peer review methodology in their organizations."
- WP cover (PDF p1) title: "Sphyr. Using Wisdom of the Crowds and Simplistic Processes to improve Performance Reviews in organizations worldwide. www.sphyr.io". Tagline next to logo: "performance reviews, done right!"
- DOC p1 subtitle: "Understanding Continuous Feedback, Organizational Alignment, and the Sphyr Platform".
- Two founding concepts (WP p1): "wisdom of the crowds" and "keeping it simple". Wisdom of the Crowds is credited to James Surowiecki (2004 book).

## 1.2 The problem (DOC p1-p2, "How Appraisals Can Ruin an Organization")
Annual appraisal compared to a final exam with no grades for 12 months (DOC p1). Six named failure modes:
1. Self-Appraisal Haggling and Anchoring Games ("a bazaar negotiation rather than a growth conversation").
2. The "Bullshitter" Advantage vs. Quiet Executioners.
3. Managerial Incompetence and Political Favoritism ("gut feel").
4. Fostering Psychopathic Work Cultures (DOC p2).
5. Subjective Promotions and Managerial Blind Spots (DOC p2).
6. Recency Bias and High Friction ("giant, multi-page, painful essays", run "once or twice a year") (DOC p2).
WP p2 names biases: "Fundamental Attribution Error, Dunning-Kruger Effect, Recency Bias, Attentional Bias, Availability Heuristic and Confirmation Bias". WP p2 survey answer to "Why can't you do reviews more often?": "the process was time-consuming and expensive".

## 1.3 Core philosophy and how it works
- DOC p2: "Instead of asking one manager for their isolated opinion once a year, Sphyr uses a principle called the Wisdom of the Crowds." Analogy: Amazon / Google Maps restaurant ratings ("50 real customers ... average rating of 4.8 stars over six months").
- DOC p2: "employees spend about 2 minutes every two weeks completing a quick 5-click feedback deck for the people they actually worked with."
- WP p3: "as simple as clicking on an average five times (for each individual reviewed) a fortnight."
- WP p1: "On sphyr, managers provide important feedback, but so does everyone else who interacts and has experiences with the individual."
- WP p2: "Sphyr's internal system follows a flat organization model and hence there are only spheres and members in those spheres." WP p5 footnote: "In Sphyr, a manager is considered as just another employee."
- WP p2 "Social Gamification": Sphyr "uses the same need of being liked and loved to help an individual improve themselves based on what their sphere wants or expects them to be." (Concept only; no gamification UI is described.)

## 1.4 Sphere of Influence
- DOC p2: "Employees build a personal network called a Sphere of Influence. This isn't just their direct boss; it includes peers, team members, subordinates, and even external stakeholders like clients or vendors."
- WP p2: members "are encouraged (or rather required) to add their juniors, peers, seniors and even clients, vendors and service providers (both internal and external) into their sphere." Ratings are reciprocal (WP p1: "as would the individual rate for all the others in the sphere").
- DOC p5: "Sphere Management: A dedicated tab ("My Sphyr") where employees manage their network, using a search tool to add internal colleagues or invite external clients and partners via email."
- Average sphere size in pilot: 14 members (WP p3).

## 1.5 Values, Behaviors and Attitudes (VBAs) and goals
- DOC p3-p4: "Org-Wide Level: The CEO or HR team configures core organizational values (e.g., Integrity, Quality of Work, Timeliness, Resourcefulness). These automatically become evaluation criteria on every employee's feedback deck across the entire company."
- DOC p4: "Team/Project Level: Managers can add specific values relevant to their function over and above the company-wide set." Examples: "Resolving Dependencies or Code Quality" (engineering), "Client Engagement" (sales).
- DOC p4: "Seamless Integration: On the actual feedback cards, employees don't see confusing dividers between "Company Rules" and "Team Rules." They just see a clean list of relevant behavioral options to tap." (This "integration" means merging value lists in the UI, not software integration.)
- DOC p4 "Target & Execution Frameworks": "flexible goal-tracking frameworks (similar to OKRs) where leadership sets strategic objectives, managers assign team targets, and every employee can connect their direct contributions to those goals." PROTO implements this as OKR cascades (Admin 3.13, Manager 3.9, Member 3.4).
- DOC p3 diagram "Top-Down Guidance meets Bottom-Up Intelligence" (4 boxes, top to bottom): "LEADERSHIP / CEO / HR ADMIN: Sets Org-Wide Values, Behaviors & Goals" -> "TEAM MANAGERS: Adds Team-Specific VBAs & Projects" -> "(Sets Expectations Top-Down)" -> "EMPLOYEE NODES: Completes Fortnightly 5-Click Feedback Decks for their Sphere" -> "(Data Flows Upward)" -> "REAL-TIME AGGREGATED INTELLIGENCE: Identifies High Performers & Top Culture Champions Across Teams & Departments".

## 1.6 Fortnightly feedback card (DOC p4, "The 3-Step Feedback Card Deck (The Core Engine)")
- "Every fortnight, an employee opens Sphyr and sees a carousel of cards representing people in their Sphere."
- Step 1, High-Level Experience: "Positive (😊), Negative (☹️), or Neutral / No Interaction (🚫)" for "the past two weeks". PROTO labels (use these in mockups): "Was good / Great interaction", "Could improve / Some friction", "No interaction / Nothing to review" (section 3.3).
- Step 2, Factor Tagging:
  - If Positive: "Performance (Met targets, Did a good job), Attitude (Showed creativity, Took initiative), and Behavior (Was helpful, Stakeholder-centric)."
  - If Negative: "friction tags (Delayed work, Was unresponsive, Quality issues, Behaved improperly)."
- Step 3, Anonymized Micro-Notes: "An optional space to leave qualitative context. The UI explicitly reassures the reviewer that their notes and ratings are strictly anonymized."
- WP p1: each experience "leaves an influencing emotion, either a positive or a negative one"; sphere "provide markers or factors that result in the experiences".

## 1.7 Rating scale
- Input scale is not numeric: 3-way experience (DOC p4: Positive / Negative / Neutral or No Interaction; PROTO: Was good / Could improve / No interaction) plus factor tags.
- Output: normalized scores. PROTO and DOC p7 screenshot show scores out of 100 (e.g. "93 out of 100"), chart axes 50 to 100.
- WP p6 pilot table used a "range of 5" for trend points. No source states the formula that converts taps to a 0-100 score. Do not describe the algorithm.

## 1.8 The 7 core parameters
DOC p4: "Professional Behavior, Timeliness of Delivery, Quality of Work, Adherence to Policies, Resolving Dependencies, Teamwork, and Engagement." WP p6 version: "Professional Behavior, Timeliness of Delivery, Quality of Work, Adherence to Team Rules/Organization Policies, Resolving of Dependencies, Team work, and Engagement at Work". PROTO labels: Professional Behavior, Timeliness of Delivery, Quality of Work, Team Rules & Policies, Resolving Dependencies, Teamwork, Engagement at Work. Radar short labels: Behavior, Delivery, Quality, Policies, Dependencies, Teamwork, Engagement.

## 1.9 Anonymity and pooling rules
- DOC p2: "Strict Anonymity & Data Normalization: Reviews and qualitative notes are anonymized and aggregated together. This strips away office politics and personal grudges".
- WP p3: "The ratings are anonymous as they should be, but without compromising on the verity of the feedback provided."
- DOC p5: peer benchmarking is "anonymous" ("anonymously benchmark their performance against relevant peers").
- GAP: no source states a minimum number of responses before scores or notes are shown, a pooling threshold, or how anonymity is technically enforced. Do not claim "minimum N reviewers" or similar.
- Note a tension: DOC p5 says managers can "approve or reject employee requests to edit previously submitted feedback", so submitted feedback is linked to its author somewhere in the system. Avoid "even admins cannot see who wrote it".

## 1.10 Employee dashboard (DOC p4-p5, "Employee Insights & Dashboards")
"7 Core Parameters" (normalized), "Fortnightly Score Trends" (line graphs), "Peer & Level Benchmarking" (toggle; "comparing a Senior Developer's scores against all other Senior Developers"), "Submission Compliance Tracker" ("e.g., 94% Completion Rate"), "Anonymized Notes Feed & Areas to Improve" ("reverse-chronological feed of qualitative notes received during the current appraisal period, alongside a summary widget highlighting top recurring constructive tags"), "Sphere Management" ("My Sphyr" tab). DOC p7 is a full-page screenshot of this dashboard (same as PROTO Insights, section 3).

## 1.11 Manager dashboard (DOC p5, "Manager & Leadership Intelligence")
- "Managers use Sphyr both as employees (getting reviewed by their own Spheres) and as team leaders overseeing collective performance".
- "Team Roster & Setup: Managers can set up project teams, define locations, and manage team member assignments."
- "Macro Team Dashboards: Aggregated view showing team-wide score distributions, culture alignment, and recurring operational bottlenecks."
- "Governance & Approvals: A dedicated queue where managers can review and approve or reject employee requests to edit previously submitted feedback."
- PROTO implements these as Manager views (section 3.5 to 3.9): team score, participation, Team vs. Organization radar, standouts, rating distribution, anonymized team feedback, "Feedback edit approvals", team profile with locations, roster, team VBAs, team OKRs. "Recurring operational bottlenecks" has no dedicated widget.

## 1.12 Leadership dashboard
- DOC p5: "Apolitical Decision Support ("Who Should We Promote?"): An objective intelligence tool for leadership. When deciding who deserves a bonus, pay raise, or promotion, leadership can query crowdsourced data to surface genuine high performers".
- DOC p3 diagram: "REAL-TIME AGGREGATED INTELLIGENCE: Identifies High Performers & Top Culture Champions Across Teams & Departments".
- No separate "leadership dashboard" or promotion-query screen is shown in PROTO. HR/admin screens in PROTO are configuration only: member directory and CSV import, org VBAs, feedback frequency, strategic OKRs (section 3.10 to 3.13).

## 1.13 HRMS relationship
- No source mentions HRMS, HRIS, payroll, SSO, or any third-party system. The only external channel named is email invites for external sphere members (DOC p5). Position Sphyr as a feedback layer only if the team states it as our framing, not as a product integration. The brief's rubric word "integration" (row "Pricing, packaging, acquisition, and engagement integration", BRIEF ~line 306-315) means joining pricing, acquisition and engagement into one plan, not software integration.

## 1.14 Roadmap (NOT current; DOC p5-p6, "Ecosystem Roadmap (Future Innovations)")
Label every one of these "roadmap" or "future" if used at all:
1. "Personal Reflection Journal: A private space for employees to log personal achievements, project wins, and obstacles".
2. "Automated Coaching & Counseling: If the platform detects consecutive score dips in a specific parameter (e.g., Quality of Work dropping 3 cycles in a row), it automatically offers guidance".
3. "Ad-Hoc Guidance Surveys: An employee can initiate an anonymous pulse survey to their Sphere".
4. "Natural Language Data Queries: An AI-assisted interface allowing managers or HR leadership to ask plain-English questions against the database".
5. "Audit-Ready Policy Generator: Pre-formatted documentation templates that HR teams can export to prove compliance with industry certifications or formal audit standards."

## 1.15 Commercial model
- WP p6-p7: "license-based SAAS offering"; "Sphyr's pricing is flat-fee for a range of licenses (users) that includes business support, training and training materials, set up and configuration support and flexible billing." WP p7: "a reasonable price point per head". No price amounts. No tiers named.

---
