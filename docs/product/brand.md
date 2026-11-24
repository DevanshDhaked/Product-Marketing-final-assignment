---
type: Research Note
title: "Brand assets and tone"
description: "Logo, colours, product UI tokens and tone found in the Sphyr sources and prototype."
tags: [brand, design]
generated: { by: claude-code/opus-5-5, at: 2026-11-24T16:32:35Z }
status: draft
sources:
  - resource: "sphyr/sphyr-logo.svg"
  - resource: "https://sphyr-prototype.raviwarrier.com/"
---

# Brand assets and tone

> Compiled by an agent from the sources on 2026-11-24. Check quotes against the source before using them in public copy.

Source keys:
- DOC = `Sphyr.io Product Documentation.pdf` (7 PDF pages, "Product Guide: Sphyr", created 2026-09-17 in ONLYOFFICE). Page numbers are PDF pages.
- WP = `Sphyr Overview Whitepaper v0.3.pdf` (9 pages with content, dated "December 2018", footer "Private and Confidential. © 2018 Ravi Warrier"). Cited as WP pN (printed page N). Printed page 1 = PDF page 3, printed page 7 = PDF page 9.
- PROTO = https://sphyr-prototype.raviwarrier.com/ (live, scraped 2026-11-24).
- BRIEF = `PMM M26 Product Marketing - Final Assignment.md`. Note: the brief spells the product "Spyhr" (line 33). All product sources, logo and prototype spell it "Sphyr". Use "Sphyr".


## 4.1 Logo mark (`sphyr-logo.svg`)
- Mark only, no wordmark. 1254x1254 viewBox, 27 flat-filled paths (Affinity export).
- Shape: a sphere built from curved, interwoven ribbon bands that wrap around a hollow, tilted toward the upper left. Reads as a globe or ball of ribbons (one ribbon per colour, suggesting many people forming one sphere). Open gap at lower left.
- Fill colours (one path each): #EDCE0F yellow, #FDBA03 / #FCC129 / #FCB306 / #FBB933 / #FAC307 amber-golds, #F67504 orange, #E00522 / #DD0F1D red, #7A0332 maroon, #E71F71 magenta-pink, #C75CC4 orchid, #8B287B plum, #886D81 dusty mauve, #3663C5 royal blue, #23355B navy, #067FAC / #0582AC / #0580AC / #0480AD / #1486AB cerulean-teal, #02A49D teal, #43C76E green, #93A502 olive, #728686 slate grey, #F8F9F9 and #F0F6F6 near-white highlights.

## 4.2 "Colorful Interwoven Ribbon Sphere.png"
- 1254x1254 RGB on white (#FEFEFE background, no transparency).
- Same ribbon-sphere shape as the SVG but rendered with smooth gradients and soft shading, more 3D and glossy. Full rainbow: orange, olive, teal, blue, violet, red, yellow, green, pink. Use for hero or large imagery; the SVG for crisp small use.

## 4.3 Whitepaper cover (WP p1)
- Gradient ribbon sphere top right with tagline "performance reviews, done right!" (lowercase). Large "Sphyr" wordmark in a light humanist sans (looks like Segoe UI / Calibri Light family; not verified). Black text on white.

## 4.4 Prototype product UI (different visual language from the logo)
- App icon: green rounded square with white "sparkles" glyph and "Sphyr" wordmark (DOC p7). It does NOT use the rainbow sphere.
- Font: Manrope (Google Fonts, weights 400/500/600/700/800), fallback ui-sans-serif, system-ui. H1 30px/700, card titles 16px/700.
- Colour tokens (OKLCH in source, hex converted):
  - background #F6FAFD; card/surface #FFFFFF; foreground/text #0D1828; muted #EAF1F8; muted text #5E6A7A; border #DAE2EA
  - primary / positive / chart-1 #009163 (emerald green); accent and positive-soft #DBF8EB / #D8F9EA (mint); accent text #005B38
  - constructive / chart-3 #E1712D (orange); constructive-soft #FFEED2 (amber cream); constructive text #4C1E01
  - destructive #DF312F; chart-2 blue #238DD4; chart-4 violet #8C6EBD; chart-5 rose #D55661; neutral-state #7B8799
  - Dark theme: background #040A16, card #0D1826, primary #34C696
  - Radius .75rem (12px). Pastel avatar colours (blue, mint, amber, rose, violet).
- Semantics: green = positive / strength; orange-amber = "could improve" / constructive (not red). Red is reserved for destructive actions (Logout, remove).

## 4.5 Tone
- DOC: blunt and opinionated ("bullshitters", "Psychopathic Work Cultures", "cuts through workplace bullshit", "bazaar negotiation"). Plain analogies (Amazon ratings, final exam).
- WP: formal, research-flavoured, 2018 startup voice ("performance reviews, done right!", "revolutionize").
- PROTO microcopy: calm, supportive, second person ("How your work is landing", "A few clicks. A stronger team.", "Private by design", "Could improve / Some friction", "Areas to improve", "Members Needing Support"). Constructive framing, never "negative" or "poor" in the member view (the manager view does say "Best and poor performers").

---
