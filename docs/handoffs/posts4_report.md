---
type: Handoff
title: "LinkedIn visuals and tighter copy report"
description: "A visual inside every post (post 1 type card, post 2 product screen, post 3 saveable four-check card) and posts tightened to 115 to 153 words with the same hooks, facts and endings."
tags: [handoff, posts4]
generated: { by: claude-code/opus-5-5, at: 2026-11-26T17:00:00Z }
---

# LinkedIn visuals and tighter copy report

> Copied verbatim from the teammate report so it survives teardown. Paths that started with the course folder are shortened to `tasks/...`, `sphyr/...` or the sibling worktree name.

Branch `d1-posts4`, worktree `Product-Marketing-final-assignment.d1-posts4`. Owned: `site/linkedin.html`, `site/css/posts.css`, new files under `site/assets/posts/`.

Success number: posts with a visual a doomscroller stops on, inside the post mock, 3 of 3 (now 1 of 3: only post 2 has an image). Second number: post bodies in 120 to 160 words with paragraphs of one or two short sentences, 3 of 3.

Skills loaded before any markup: `design-taste-frontend` and `stageshow`. Design read: a B2B deliverable page drawn in the v2 system (Newsreader headings, Manrope body, warm paper palette, ribbon colours only where the ribbon appears); dials 4 / 2 / 4 (static images, no motion). From stageshow I use the still-frame rules (few real strings, one focal object, crop with intent, no plate, no hand-drawn chrome), not its React kit: the site is plain HTML and CSS.

## Plan

### Files
- `site/linkedin.html`: copy of the three posts; one image figure per post (post 2 unchanged); `css/motif.css` linked so the ribbon option can reuse the site's strand colours and `.cv` styles (static, no `play` class, so nothing animates).
- `site/css/posts.css`: a shared `.li-card` image style (full card width under the text, fixed aspect, site tokens so it follows both themes like the post 2 frame), plus the post 1 and post 3 card rules.
- `site/assets/posts/`: none expected. The images are inline SVG and HTML inside the mock, so they follow the theme and use the site fonts.

### Order and job (unchanged page structure)
1. Intro. Says what the page is.
2. Post 1, Attention. Copy cut to four short paragraphs; image: one of two candidates (below), then STOP for the lead's pick.
3. Post 2, Interest. Copy to four short paragraphs; image: the Fortnightly Feedback card as it is.
4. Post 3, Decision. Copy tightened; image: a saveable card "Four checks before you sign any HR pilot", the four checks short, the Sphyr mark small at the foot.
5. How the three work together. Unchanged.

### Post 1 candidates
- A, type card: the hook set large in Newsreader, under it a plan of the calibration room (a table with the partner and the head of talent seated, four dashed empty seats marked as the four who saw the workshop). No ribbon colours.
- B, ribbon: the hook as a short headline, one project box ("Retail project, client workshop") with four strands in the logo colours that run toward a "Calibration" box and stop short of it. It is the problem half of the home ribbon, where the strands do reach the sphere.

### Copy rules applied
Hook lines verbatim; every fact kept; endings kept (post 1 question, post 2 walkthrough line, post 3 call). Word rule and copy rules from the common brief; humanizer pass before commit; copy_scan and copy_tells after.

### Open questions
- Images follow the site theme (as the post 2 frame does) rather than staying light in dark mode as a real uploaded image would. I chose theme-following for one consistent page; say if you want them fixed light.
- Post 2 currently has about 115 words after the brief's tightening; reaching 120 needs no new fact, only a split of the "Sphyr asks" sentence. I will not add facts to reach the floor.

## Build so far

Success number now: 2 of 3 posts have a visual committed (post 2 product card, post 3 checks card); post 1 waits on the pick below. Word counts (body text, script `.swarm/tmp/posts4/wc.py`): post 1 153 words in 4 paragraphs, post 2 115 in 4, post 3 138. Line ones unchanged: 55, 48 and 48 characters.

- `b35c7ee` Copy. Post 1: paragraph 3 has three short sentences, since two would mean dropping "the room moves to the next name" or the designation and hike line. Post 2: split into four paragraphs; I added one sentence, "The other three reach the rating secondhand.", which follows from the line before it and adds no new fact. Post 2 is still 115 words, under the 120 floor; I did not pad it further. Post 3: one sentence split, and "these four checks" became "these checks" because the list sits right above it. Humanizer: no tells found. copy_scan: only the known "self-review" false positive. copy_tells: 0 contrasts, and every flagged triad is a two-item phrase.
- `03c91ea` Post 3 card. HTML and CSS inside the mock, 4:5 like a portrait feed image. Sizes are set in units of a 540-wide design (container query units), so the card scales as one picture and wraps the same way at 1280 and 375 (checked: 550 by 688 and 341 by 426). Title in Newsreader, numbers in ink green, hairlines, and the Sphyr mark small at the foot. Checks 3 and 4 are shortened for the card ("Ask partners what they learned about a consultant. Ask for a name." and "Ask consultants if they would keep going without HR chasing them."). The post text keeps the full wording.

## Post 1 options

Both are inline SVG at 1:1 on the same ground as the post 2 image, with the hook in Newsreader (roman, then green italic as in the home headline). Both are in the post 1 mock now, B `hidden`, and not committed. Screenshots of the whole post mock:

- A, type card: `.swarm/tmp/posts4/post1-option-a-1280.png`, `.swarm/tmp/posts4/post1-option-a-375.png`. The hook is large, and under it two equal boxes: "Client workshop" holds four filled green discs and "Calibration" holds four empty dashed places. Four strings, no ribbon colours. It reads in one glance at phone size.
- B, ribbon: `.swarm/tmp/posts4/post1-option-b-1280.png`, `.swarm/tmp/posts4/post1-option-b-375.png`. A smaller hook, and under it one "Client workshop / Retail project" box with four strands in the logo colours. The strands break into dots before a "Calibration / One form" box. This is one project, not the home ribbon's four project boxes: post 1 is about four people on one project, and this is the problem half of the home ribbon (where the strands do reach the sphere). The colour makes it stop the scroll harder; it needs `css/motif.css` linked on this page for the strand colours.

My pick: A. It says the hook twice in a form a phone reader gets in one glance, and it leaves the ribbon's colour and its payoff (strands reaching the sphere) for the home page. B is the more striking image, and it ties the series to the brand.

Stopped here, waiting for the lead's pick. Browser closed.

## Lead reply
Pick A (type card). Remove B and its markup, do not link motif.css.

## Final

Success number: posts with a visual inside the post mock, 3 of 3 (was 1 of 3). Word counts 153, 115 and 138 (post 2 is under the 120 floor; see below). Hook lines are verbatim, at 55, 48 and 48 characters.

### Files written, with commit SHAs
- `site/linkedin.html`: `b35c7ee` (copy), `03c91ea` (post 3 card), `72b7d7c` (post 1 type card).
- `site/css/posts.css`: `03c91ea` (`.li-img` and the post 3 card rules), `72b7d7c` (`.li-art` rules for the post 1 card).
- `site/assets/posts/`: none. Both images are inline in the mock.
- This report.

### Key decisions and why
- Post 1 uses option A, the lead's pick. The B markup, the `css/motif.css` link and the B-only CSS rules (`art-hook-sm`, `art-sub`, `art-strand`, `art-dots`) were removed before the commit. No strand colours are left on the page.
- The images are inline SVG (post 1) and HTML with container query units (post 3). Each scales as one picture and wraps the same way at every width. They use site tokens, so they follow the theme as the post 2 frame does. No raw hex, no gradients and no photos.
- All three images sit on the same `--stage-ground` band, edge to edge, with hairlines above and below. The three posts read as one set, and each image matches the v2 post 2 image style.
- The post 3 card shortens checks 3 and 4, so each check fits in two lines inside a 4:5 frame. The post text keeps the full wording.
- Newsreader is used only in the weights `base.css` declares (500 roman, 400 italic), so no fake bold or italic appears.

### Approaches rejected and why
- Option B (ribbon strands breaking off before calibration): the lead picked A.
- Four project boxes for the ribbon option: post 1 is about four people on one project.
- Padding post 2 up to 120 words: that would add words without a fact.
- A 1:1 post 3 card: four checks plus the title did not fit with room; the card is 4:5 instead.

### Checks (smoke)
- copy_scan: 172 strings, 1 hit, the known "self-review" false positive. copy_tells: 0 contrasts; 5 triad candidates, all two-item phrases or the footer names.
- No em or en dashes in `linkedin.html` or `posts.css`.
- Links: 13 of 13 same-origin URLs return 200 (pages, CSS, fonts, icons, mark).
- 375: scrollWidth 375 = clientWidth 375, so there is no sideways scroll.
- Looked at each post at 1280 light, 1280 dark and 375 light, against the v2 page. Same card, hairlines, ground and type as v2. Posts 1 and 3 now carry an image like v2's post 2. The dark images read cleanly: green turns to the light mint ink, and the dashed places stay visible.

### Open questions
- Post 2 is 115 words, under the brief's "about 120". Add a line, or keep it as is?
- "The other three reach the rating secondhand." in post 2 is an inference from the line before it, not a sourced fact. Keep or cut?
- Should the images stay light in dark mode, as a real uploaded image would? Today they follow the theme.

### What I did not verify
- The Scullen, Mount and Goff figures (carried over from posts3).
- Dark mode at 375 (not required).
- Real LinkedIn crop behaviour for a 4:5 image in the feed; the mock shows it whole.

### Screenshots
In `.swarm/tmp/posts4/`:
- Each post: `final-post1-1280-light.png`, `final-post1-1280-dark.png`, `final-post1-375-light.png`, and the same three for `post2` and `post3`.
- Options: `post1-option-a-1280.png`, `post1-option-a-375.png`, `post1-option-b-1280.png`, `post1-option-b-375.png`.
- References: `ref-v2-linkedin-1280.png`, `ref-before-linkedin-1280.png`, `ref-home-1280.png`.

## Not done (out of scope)
- `design-lab/copy_scan.py` still flags "self-review" (not my file).
- Persistence: this report lives only in `.swarm/reports/`. The lead may want to copy it to `docs/handoffs/posts4_report.md`. The lead may also want a decision-log line: post 1 type card, post 3 checks card, images follow the theme.

Idle.

## Addendum: dark theme check (lead request)

Result: posts 1 and 3 images look intentional in dark at 1280 and 375. No code change.
- Choice: themed, not light printed cards. The post 2 product frame also themes in dark: it turns to the product's own dark navy and is not kept light. So all three images go dark together, and none is a light box on the dark page.
- Post 1 image in dark: the ground is the near-black stage ground. The hook is in off-white, with the italic line in the light mint ink. The boxes are dark surface with a visible outline. The four filled places are mint, and the four dashed places stay visible.
- Post 3 image in dark: same ground. The title and checks are in off-white and the numbers in mint. The hairlines and the logo mark are visible.
- Whole page in dark at 1280 and 375: the three images and the notes read cleanly. There is no sideways scroll at 375 (375 = 375) and the computed color-scheme is dark.
- Screenshots in `.swarm/tmp/posts4/`: `final-page-1280-dark.png`, `final-page-375-dark.png`, `final-post1-img-1280-dark.png`, `final-post1-img-375-dark.png`, `final-post3-img-1280-dark.png`, `final-post3-img-375-dark.png` (plus `final-post{1,2,3}-1280-dark.png` from before). All looked at.
- This closes the open question on dark: the images follow the theme. "Dark mode at 375 not verified" in Final is now verified.

Browser closed. Idle.
