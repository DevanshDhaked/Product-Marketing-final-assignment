---
type: Handoff
title: "v3 review fixes report"
description: "Reviewer fixes: the managing partner's cost on home, Participation, the head of talent's view, the call label in propaganda, the ox paragraph cut, and the ad QR and addresses aimed at the home page."
tags: [handoff, fix3]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T15:00:00Z }
---

# v3 review fixes report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Plan approval skipped: the brief is the approved plan.

## Final

Result: all 7 brief items done; 4 commits on `d1-fix3`.

### Files written, with commits
- `site/index.html` (9d85f96): problem list gets a fifth line, "A strong consultant misses a designation and leaves after the hike letters go out." Section 3 "Turnout in each cycle" becomes "Participation in each cycle".
- `site/deliverables.html`, `site/propaganda.html` (cab87c5):
  - Deliverables "After a few cycles": "Engagement managers see how the project team is rated while the work is still going on. The same view shows how much of the team has given feedback, so nobody chases forms." The head of talent line is gone.
  - Propaganda flow item "The 20-minute call" becomes "Book a 20-minute call".
- `site/linkedin.html` (ea4e388): post 2 loses the 1906 ox paragraph. The next paragraph now opens "So Sphyr asks everyone on the project, every two weeks." One word ("So") joins it to the research line before it.
- `site/ad.html` (4af54c2):
  - Standee and A6 front first line now ends "... of 40 to 400 people. Scan to book a 20-minute call or see the 2-minute walkthrough."
  - The three printed `.../v2/demo.html` addresses become `.../v2/`.
  - The A6 back QR label is now "Book a 20-minute call or see the 2-minute walkthrough".
  - The three QR alt texts become "QR code that opens the Sphyr home page", so they stay true. The QR image was not touched.

### Key decisions
- Deliverables: participation moves to engagement managers (Manager role), the brief's first option. "The same view" avoids a pronoun switch. "So nobody chases forms" keeps the old benefit (no chasing) without giving Admin a results view.
- Home fifth line: added "go out" after "hike letters" so the line reads as a finished sentence.
- Ad rationale (`ad.html:134`): left unchanged. It says the QR and address "open the same plain page" and never names the walkthrough, so it stays true. "Then asks for a call" at 132 also stays true.
- Standee first line: "book" is lower case because it sits mid-sentence (brief's exact string). The full button label "Book a 20-minute call" is used on the A6 back.

### Rejected
- "If the head of talent also has the Manager role, they see ...": clumsier, and it still points a reader at the head of talent for a results view.
- Rewriting the post 2 join with a new sentence: "So" is enough, and the brief asks for the fewest words.

### Checks
- `humanizer:humanizer` on all 8 changed strings: no tells.
- copy_scan: 0 unreviewed hits on index, ad, deliverables and propaganda. linkedin has 1 unreviewed hit, "[social proof] Ten months later ... three other clients" in post 1. It was already there at HEAD before my edits; I did not touch it.
- copy_tells: 1 contrast on index and ad (the sign-off, as intended). Possible triads are all existing strings or names; none come from my edits.
- No sideways scroll at 375: index scrollWidth 375 = clientWidth 375, and the same on ad. The problem list has 5 items.
- I took screenshots at 1280 (light theme) and looked at both. Browser closed.

### Open questions
- The QR image (`assets/ad/walkthrough-qr.svg`) presumably still encodes `.../v2/demo.html` (I did not decode it). The lead must regenerate it for the v3 home URL at deploy, or the alt text and label will not match what a scan opens.
- At 1280 the standee first line wraps as "2-" / "minute walkthrough". This is a print artifact, so a non-breaking hyphen (`2&#8209;minute`) would be a one-entity fix. I did not change it because it is out of scope.

### Not verified
- Dark-theme screenshot and the 375 screenshot (the brief asked only for 1280 shots of the two areas).
- Rendered views of deliverables, propaganda and linkedin: checked by grep only.

### Screenshots
- `Product-Marketing-final-assignment.swarm/tmp/fix3/home_problem_1280.png`
- `Product-Marketing-final-assignment.swarm/tmp/fix3/ad_standee_1280.png`

## Not done (out of scope)
- `ad.html:22` to 23: `og:url` and `og:image` still point to `/v2/ad.html`. The lead's v2 to v3 rewrite at deploy should cover them.
- Reviewer's suggestion to post LinkedIn posts from a named founder's profile instead of the company page.
- The existing copy_scan social-proof hit in LinkedIn post 1.
