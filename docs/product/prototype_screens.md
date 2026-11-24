---
type: Research Note
title: "Prototype screen inventory"
description: "Every screen of the professor's Sphyr prototype with its route, UI elements and exact copy, scraped 2026-11-24."
tags: [prototype, ui]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
sources:
  - resource: "https://sphyr-prototype.raviwarrier.com/"
---

# Prototype screen inventory

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Source keys:
- DOC = `Sphyr.io Product Documentation.pdf` (7 PDF pages, "Product Guide: Sphyr", created 2026-09-17 in ONLYOFFICE). Page numbers are PDF pages.
- WP = `Sphyr Overview Whitepaper v0.3.pdf` (9 pages with content, dated "December 2018", footer "Private and Confidential. © 2018 Ravi Warrier"). Cited as WP pN (printed page N). Printed page 1 = PDF page 3, printed page 7 = PDF page 9.
- PROTO = https://sphyr-prototype.raviwarrier.com/ (live, scraped 2026-11-24).
- BRIEF = `PMM M26 Product Marketing - Final Assignment.md`. Note: the brief spells the product "Spyhr" (line 33). All product sources, logo and prototype spell it "Sphyr". Use "Sphyr".


Captured 2026-11-24 with Playwright (rendered DOM text, computed CSS) and firecrawl. The prototype is a client-side React app built on Lovable ("Edit with Lovable" badge bottom right; links to lovable.dev project `lovp_07gnwrk9689hw9xvzkpvz195t3`). Plain firecrawl returns only the home screen and zero links, so routes were found from the rendered sidebar. All people, numbers and dates are demo data. Logged-in user throughout: "John Smith, Senior Developer" (avatar initials "JS").

## 3.0 Global shell (all screens)
- Layout: two-level left sidebar plus content area. Far-left icon rail with app icon (green rounded square, white sparkle glyph) and three role switches: "Member", "Manager", "Admin" (active item has mint background). Second panel: user card "John Smith / Senior Developer" with chevron, a "Light mode" / dark toggle (moon icon; aria "Use dark theme"), section label (e.g. "MEMBER"), nav links, "Logout" in red at bottom. Bell "Notifications" icon (orange dot) top right of content. "Collapse navigation" / "Open navigation" buttons (sidebar collapses).
- Page header pattern: small uppercase green eyebrow (e.g. "PERSONAL INSIGHTS"), H1 30px/700, grey subtitle.
- Cards: white, rounded (radius token .75rem = 12px), thin cool-grey border, page background very light blue-grey.
- Dark theme exists (full `.dark` token set).
- Browser titles use "<Page> — Sphyr".
- Note: the DOC p7 screenshot shows an older layout with a top nav ("Insights", "My Sphyr", "Feedback") and the user menu at top right. The live prototype uses the sidebar. Content of the Insights page is otherwise near-identical.

## 3.1 Member > Insights  `/`  (title "Performance Insights — Sphyr")
Meta description: "Track seven core performance dimensions and anonymized feedback trends." OG description: "Understand your performance trends through aggregated feedback."
- Eyebrow "PERSONAL INSIGHTS". H1 "How your work is landing". Sub "A normalized, anonymized view built from your last six feedback cycles."
- 4 KPI tiles:
  - "Overall score" 78, chip "+3", "Mixed signals this cycle".
  - "Responses received" 46, chip "+8", "From 12 collaborators".
  - "Strongest signal" "Quality of Work", chip "+4", "93 out of 100".
  - Green highlighted tile: "Current cycle progress" 94%, "16 of 17 Reviews Submitted", "1 Pending Review This Cycle", "Fortnightly Cycles Tracked: 11 of 12 Cycles Completed", "Missed Cycles: 1 Missed Fortnightly Cycle". (DOC p7 version: "SUBMISSION RATE 94%", "Given 16 of 17 reviews this cycle", "Cycles completed 11 / 12", "Missed reviews 2" in orange.)
- "Overall trajectory": "Composite score across all seven dimensions", chip "Improving" (trend-up icon). Green area line chart, y-axis 50/65/80/100, x-axis fortnightly dates May 05, May 19, Jun 02, Jun 16, Jun 30, Jul 14.
- "Matched peer comparison": "Benchmarks are locked to John Smith's profile: Coder / Developer · Senior Developer · Frontend Core". Toggle "Compare by Role" / "Compare by Designation". Mint strip: "Matched by Role", "Team: Team Coders", "Organization: Org-wide Coders", info icon "Unrelated roles and levels are excluded".
  - Left "Performance profile", "Seven dimensions in the latest cycle", chip "Coders". 7-axis radar: Behavior, Delivery, Quality, Policies, Dependencies, Teamwork, Engagement. Series: John Smith (green), Team Coders (blue), Org-wide Coders (grey).
  - Right "Fortnightly trend", "Score against matched peers over time", chip "6 cycles". Lines: John Smith (green, dotted markers), Team Coders (blue), Org-wide Coders (grey dashed).
- "Seven performance dimensions": "Current normalized score and cycle change", info icon. Rows with horizontal green bar, score and delta (green up-right arrow or orange down-right arrow): Professional Behavior 91 (up 4); Timeliness of Delivery 69 (down 5); Quality of Work 93 (up 4); Team Rules & Policies 81 (up 2); Resolving Dependencies 66 (down 4); Teamwork 80 (up 2); Engagement at Work 77 (down 1).
- "Top feedback received": "Most frequent anonymized feedback signals", amber chip "4 could improve". Bars with counts: Did a good job 24 (green); Was helpful 19 (green); Delayed my work 12 (orange); Took initiative 11 (blue); Was unresponsive 7 (orange). Amber callout with sparkle icon: "Quality remains a strength; earlier delivery signals and dependency follow-through need attention." (This is a templated summary line; no source says it is AI-generated.)
- "Dimension trends": "Compare your core strengths over time". 3 lines: Quality (green), Delivery (blue), Dependencies (orange).
- "Areas to improve" (target icon): "Recurring constructive signals from recent cycles". Cards with amber count badge: "Resolve dependencies earlier" 8, "Repeated across 3 cycles · Highest priority"; "Share progress more proactively" 6, "Repeated across 2 cycles"; "Protect focus time" 4, "Repeated across 2 cycles".
- "Anonymized Feedback" (message icon): "Latest first · Current appraisal period: Jul 14 – Jul 27". Each item: green label "Anonymized Feedback", date right, quote:
  - Jul 25 "You make complex workshops feel calm and inclusive. Keep giving quieter voices room to enter the discussion."
  - Jul 22 "Your handoff was clear and thoughtful. An earlier signal on the research dependency would have helped us plan around it."
  - Jul 18 "Strong partnership this cycle—you connected customer evidence to the design decision without overcomplicating it."
  - Footer "Expand to view earlier comments" (chevron).

## 3.2 Member > My Sphyr  `/sphere`  (title "My Sphyr — Sphyr")
- Eyebrow "YOUR NETWORK". H1 "My Sphyr". Sub "Keep this circle focused on people you work with regularly. You can update it at any time."
- Button "Invite to My Sphyr".
- Grouped lists with count: "Peers" 3 people (Maya Chen, Product Designer; Arjun Mehta, Senior Engineer; Lucas Martin, UX Researcher). "Seniors" 2 people (Nora Williams, Product Manager; Aisha Bello, Design Lead). "Subordinates" 2 people (Theo Brooks, Visual Designer; Leila Haddad, Content Designer). "External" 2 people (Ethan Park, "Client Partner · Northstar"; Inez Silva). Avatars are pastel circles with initials (avatar-blue/mint/amber/rose/violet tokens).

## 3.3 Member > Provide Feedback  `/feedback`  (title "Fortnightly Feedback — Sphyr")
- Eyebrow "FEEDBACK THIS FORTNIGHT". H1 "A few clicks. A stronger team." Sub "Think about your interactions this fortnight." Counter pill "4 of 17" and green progress bar.
- Card: person avatar, "Lucas Martin", "UX Researcher · Peers" (sphere group shown).
- Step 1 question: "How was your experience with Lucas Martin this fortnight?" Three tiles: smiley "Was good / Great interaction"; frown "Could improve / Some friction"; dash "No interaction / Nothing to review". Selected tile turns mint with green border.
- Step 2 if "Was good": "What stood out?" "Select all that apply." Green label "Sphyr UI / UX VBAs" (team name + VBAs). Three columns of pill chips:
  - VALUES: Transparency, Customer First, Innovation
  - BEHAVIORS: Punctual, Respectful, Stakeholder-centric
  - ATTITUDES: Takes Initiative, Solution-oriented, Resilient
- Step 2 if "Could improve": "Where did you experience friction?" "Choose the clearest signals. Your response is anonymized." Same label "Sphyr UI / UX VBAs".
  - VALUES: Share context earlier, Consider customer impact
  - BEHAVIORS: Improve punctuality, Respond more consistently, Resolve dependencies sooner
  - ATTITUDES: Take greater ownership, Stay open to feedback
- Step 3 comment: button "Add a comment" opens textarea. Prompt "Let Lucas know what's on your mind?", helper "Your comments and review are always anonymized.", placeholder "Share a helpful example or context…", counter "0/400".
- Buttons "Previous", "Submit".
- Right rail: lock card "Private by design" / "Individual responses are normalized and grouped before anyone sees them." Card "THIS CYCLE": 3 Completed, 14 Remaining, green pill "4-cycle streak · 8 weeks".
- "SUBMITTED" list "Completed Feedback This Fortnight", "3 completed": Maya Chen 😊, Arjun Mehta 🚫, Nora Williams 😊, each "Submitted · Read only".
- Difference vs DOC p4: DOC step-2 tags are fixed (Performance / Attitude / Behavior; "Met targets, Did a good job ..."; negative "Delayed work, Was unresponsive, Quality issues, Behaved improperly"). PROTO uses configurable VBA tags grouped Values / Behaviors / Attitudes. The manager view (3.6) still shows DOC-style tags ("Did a good job", "Met targets", "Missed work or meetings"). For mockups, either set is supported; the PROTO set is the most current.

## 3.4 Member > My Objectives & Responsibilities  `/objectives`
- Eyebrow "PERSONAL EXECUTION". H1 "My Objectives & Responsibilities". Sub "Break down objectives assigned by your manager into focused, trackable responsibilities."
- Stats: "2 OBJECTIVES", "2/4 RESPONSIBILITIES DONE", "73% AVG. PROGRESS".
- Objective blocks "O1", "O2" labelled "ASSIGNED OBJECTIVE", function "Product / Engineering", objective text, "2 responsibilities", "Due 2026-09-30".
- Table columns: Responsibility | People | Status | Due Date | Priority | Progress | Updates. Status and priority are dropdowns; due date picker; avatar stack in People; updates count. Button "Add Responsibility".
- Demo objective text includes "Complete v2.0 API integrations by end of Q3" and "Build webhook listener for real-time manager approval notifications". These are fictional customer tasks, NOT Sphyr features.

## 3.5 Manager > shared header (all `/manager?view=...`)  (title "Manager Team Workspace — Sphyr")
- Eyebrow "MANAGER VIEW". Selector "Select Team: Sphyr UI / UX". Segmented "Review period: Last Cycle | All Cycles".
- KPI tiles: "Team score 82, Up 2 points this cycle"; "Team members 6, 3 locations"; "Participation 96%, 24 of 25 reviews given"; "Edit requests 3, Awaiting your decision".
- Manager nav: "Member Insights", "Team Insights", "Team Responsibilities", "Manage Teams".

## 3.6 Manager > Member Insights  `/manager?view=member-insights`
- H1 "Member Insights". Sub "Review individual performance signals, comparisons, feedback, and improvement areas."
- Table "Select a member to review their performance signals, feedback, and improvement areas." Columns: Member | Trend | Trend verdict | Overall assessment. Rows: John Smith (Senior Engineer) 81; Maya Chen 90; Arjun Mehta 87; Lucas Martin 83; Theo Brooks 79; Leila Haddad 71. Verdict "Positive", assessment "Good" (sparkline in Trend column).
- Per-member drill-down not captured (shared browser was taken by another agent mid-run; firecrawl actions unavailable).

## 3.7 Manager > Team Insights  `/manager?view=team-insights`
- H1 "Team Insights". Sub "Compare team health, spot coaching priorities, and decide feedback edit requests."
- "Team vs. Organization Benchmark": "Last cycle comparison across all seven parameters." Toggle "Radar | Trend". Radar axes Behavior, Delivery, Quality, Policies, Dependencies, Teamwork, Engagement. Legend "Organization Average", "Team Average".
- "Team Standouts & Focus Areas": "Best and poor performers from the latest feedback cycle."
  - "Top Performing Members": Maya Chen 86 (Did a good job, Was helpful); Arjun Mehta 82 (Took initiative, Met targets).
  - "Members Needing Support": Theo Brooks 76 (Delayed my work, Was unresponsive); Lucas Martin 79 (Missed work or meetings, Delayed my work).
- "Rating distribution": "Aggregated last-cycle responses": Positive 68%, No interaction 21%, Could improve 11%.
- "Anonymized team feedback": "Last cycle · Latest first": Jul 25 "The team stayed calm under pressure and protected quality through a difficult release." Jul 22 "Dependency risks need to be surfaced earlier, especially when another team owns the handoff." Jul 18 "Strong collaboration this cycle. Pairing sessions helped unblock work quickly."
- "Feedback edit approvals": "Review requests before submitted feedback can be reopened." Cards: requester, "Feedback given to <name>", "Reason for edit", buttons "Reject" / "Approve". Examples: Maya Chen -> Arjun Mehta "I selected the wrong delivery tag and want to correct it."; Theo Brooks -> Nora Williams "I have more context to add after our project retrospective."; Leila Haddad -> Lucas Martin "My rating was submitted before I finished the comment."
- ANONYMITY NOTE: this panel shows the manager who gave feedback to whom. Anonymity applies to the recipient's view, not to manager governance. Never claim "fully anonymous to everyone".

## 3.8 Manager > Team Responsibilities  `/manager?view=team-tasks`
- H1 "Team Responsibilities". Sub "Monitor team responsibilities and supporting tasks in one shared view."
- "Team responsibility monitor": "Review responsibilities, add supporting tasks, and step in where work needs support." Filters: Team Member (All members), Role (All roles), Objective (All objectives).
- Columns: Responsibility | Linked Objective | Assigned Person | Status | Due Date | Priority | Progress | Updates. Status values seen: Done, Working on it, Stuck, Not Started. Priority: High, Medium. Progress as %.

## 3.9 Manager > Manage Teams  `/teams?section=...`  (title "Team Management Hub — Sphyr")
Sub-nav: "Team Profile", "Roster Management", "Team VBAs", "Team OKRs & KR Cascade". Top: "Active Team: Sphyr UI / UX" selector, button "Create New Team".
- `section=profile`: eyebrow "TEAM SETTINGS", H1 "Team Profile", "Maintain the identity, operating locations, and purpose of this team." Fields: Team Name; Locations (checkboxes Reykjavík, London, Remote); Description; button "Save Team Profile".
- `section=roster`: eyebrow "PEOPLE OPERATIONS", H1 "Roster Management", "Search internal members, capture their relationship, or move people between managed teams." Search "Search by name or email", button "Add internal member". "Current Team Members: 6 people in Sphyr UI / UX", each "Role · Location" with "Move" button.
- `section=vbas`: eyebrow "Feedback framework", H1 "Team VBAs", "Control the Values, Behaviors, and Attitudes shown when this team receives feedback." Three modes: "Inherit Template: Use a saved template exactly.", "Inherit & Customize: Start from a template, then adjust.", "Custom Team VBAs: Build this team's tags from scratch." "VBA Template: Organization Baseline". "Positive VBAs: Signals to recognize and reinforce." 9 tags; "Constructive VBAs: Signals that guide useful improvement." 7 tags (same tags as 3.3). Button "Save Team VBAs".
- `section=okrs`: eyebrow "Top-down alignment", H1 "Team Objectives & Responsibility Cascade", "Turn responsibilities inherited by Sphyr UI / UX into targeted, trackable outcomes for individual team members." "Inherited Team Objectives: Functional objectives assigned from Organization Administration." Objectives A (Product / Engineering) and B (Quality / Design) with per-role responsibilities (Coders / Engineers, Testers / QA, Designers) and due dates. "Assign a Member Responsibility: Create a targeted responsibility beneath one inherited objective. Its due date is inherited automatically." Fields Inherited Objective, Team Member, Responsibility ("Define a measurable responsibility"), button "Assign Responsibility". "Member Responsibility Tracking: Team members grouped by functional role with their assigned outcomes." with editable progress %.

## 3.10 Admin > Member Directory & Signups  `/admin?view=directory`  (title "Organization Administration — Sphyr")
Admin nav: "Member Directory & Signups", "Organization VBAs", "Feedback Frequency", "Strategic OKRs & Cascading KRs".
- Eyebrow "PEOPLE ADMINISTRATION". H1 "Member Directory & Signups". Sub "Import, add, and maintain everyone who can participate in Sphyr."
- Button "Add Member". "Import member records: Upload a CSV, XLS, or XLSX file. The first row should contain column names." "Choose file".
- "Directory status: 4 active users · 2 awaiting approval".
- "Active Users: Edit organization details or remove access." Columns Member | Role & designation | Function | Manager | Actions (edit, remove icons). Member shows "EMP-1042 · john.smith@sphyr.example". Role & designation e.g. "Coder / Developer" + "Senior Developer".
- "Pending Signups: Review new signups from your organization domain." Rows with timestamp ("Today, 09:42"), "Reject" / "Approve".

## 3.11 Admin > Organization VBAs  `/admin?view=vbas`
- Eyebrow "ORGANIZATION BASELINE". H1 "Master Values, Behaviors & Attitudes". Sub "These tags form the default baseline inherited by manager templates and teams across the organization."
- "Global VBA baseline": "Changes cascade to teams using the unmodified Organization Baseline." Chip "Global cascade active".
- "Positive VBAs: Qualities to recognize and reinforce." and "Constructive VBAs: Signals for actionable improvement.", each with Values / Behaviors / Attitudes editable tag inputs and "Add tag". Button "Save & cascade".

## 3.12 Admin > Feedback Frequency  `/admin?view=frequency`
- Eyebrow "REVIEW CADENCE". H1 "Feedback Frequency". Sub "Set one organization-wide rhythm for feedback assignments and submission tracking."
- "Select feedback frequency" radio cards: "Weekly: Fast, continuous check-ins"; "Fortnightly: Balanced, continuous feedback" (default); "Monthly: Monthly review windows"; "Quarterly: Long-form quarterly cycles".
- "Fortnightly cycle schedule: Schedule preview based on the current organization calendar." Current cycle starts 14 Sep 2026, ends 27 Sep 2026; next starts 28 Sep 2026. Button "Save frequency".
- Fact for marketing: cadence is configurable (PROTO). DOC and WP describe fortnightly as the method.

## 3.13 Admin > Strategic OKRs & Cascading KRs  `/admin?view=okrs`
- Eyebrow "TOP-DOWN ALIGNMENT". H1 "Strategic OKRs & Cascading KRs". Sub "Leaders define responsibilities directly; every assigned KR becomes the recipient manager's objective for the next cascade."
- Three forms: "Create strategic objective" ("Set an organization-level outcome owned by executive leadership.", placeholder "Increase gross margins by 15% this financial year", button "Create objective"); "Assign key responsibility" ("Map a responsibility directly to a function, department, team, or role.", fields Parent Objective, Assign to, Function, Owner, Key Responsibility, button "Assign responsibility"); "Cascade to the next level" ("Treat an assigned KR as the manager's objective, then assign its child result.", button "Cascade KR").
- "Cascading Alignment Tree": "Organization Objective → assigned KR → inherited manager objective → team or individual KR." Example nodes with progress %: "Increase gross margins by 15% this financial year" (Owner: CEO / Organization, 58%) -> "Product Teams: Reduce cost of production by 10%" (64%) -> "Sphyr UI / UX: Reduce design-to-build rework by 20%" (71%), "Frontend Core: Reduce platform operating cost by 12%" (57%); "Marketing: Increase market share by 20%" (49%) -> "Growth Manager: Create three new qualified acquisition channels" (45%); "People & Culture: Hire 15 new salespeople" (60%) -> "Talent Team: Fill eight priority sales roles this quarter".

## 3.14 Not present in PROTO
- No leadership "Who Should We Promote?" query screen (DOC p5 only).
- No HR/leadership org-wide performance dashboard beyond admin config and manager team views.
- No roadmap items (journal, coaching, pulse surveys, NL queries, policy generator).
- No pricing, login/signup page, onboarding, settings, integrations page, or mobile app. Mobile responsiveness not checked.
- "Notifications" bell exists; its content was not opened.

---
