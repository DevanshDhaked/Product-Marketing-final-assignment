# Sphyr

Team 03's final assignment for Product Marketing (PD2.501) at IIIT Hyderabad, by Aryan, Abhinav, Devansh and Bheema.

Live site: https://devanshdhaked.github.io/Product-Marketing-final-assignment/

## The site and the deliverables

The website is deliverable 1 and the hub for the other three. Nothing needs a sign-in.

| Page | What it is |
|---|---|
| [Home](https://devanshdhaked.github.io/Product-Marketing-final-assignment/index.html) | Deliverable 1: how Sphyr works, what partners see, the price and the pilot |
| [2-minute walkthrough](https://devanshdhaked.github.io/Product-Marketing-final-assignment/demo.html) | Part of deliverable 1: the product on sample data, no form |
| [Deliverables](https://devanshdhaked.github.io/Product-Marketing-final-assignment/deliverables.html) | The index of deliverables 2 to 4 |
| [Propaganda strategy](https://devanshdhaked.github.io/Product-Marketing-final-assignment/propaganda.html) | Deliverable 2 |
| [Three LinkedIn posts](https://devanshdhaked.github.io/Product-Marketing-final-assignment/linkedin.html) | Deliverable 3 |
| [Advertisement](https://devanshdhaked.github.io/Product-Marketing-final-assignment/ad.html) | Deliverable 4 |

## The product

Sphyr is 360 feedback for performance appraisal. Every two weeks, each person spends about two minutes on short cards for the people they worked with. Ratings are pooled and comments are anonymized to the person rated, and each person can read their own record. Managers see team and member trends across cycles. Sphyr runs next to the firm's HR system, and people are imported from a spreadsheet.

Sources: the Sphyr Overview Whitepaper v0.3 (2018), and the Sphyr product guide and prototype shared in class.

## Strategy in brief

| | |
|---|---|
| Segment | Homegrown Indian management and strategy consulting firms led by their partners, with about 40 to 400 professionals |
| Persona | The head of talent, who finds Sphyr, runs the pilot and takes the case to the managing partner, who signs |
| Central message | The engagement ends. The evidence stays. |
| Price | ₹149 per employee per month, billed yearly, plus GST, the same for any firm size |
| Pilot | 12 weeks (six fortnightly cycles) for up to 40 people at ₹25,000 plus GST, credited against the first annual bill if the firm signs |
| Channels | The Sphyr LinkedIn page with team reshares, warm introductions, HR and consulting communities, our own site, and one paid standee at an HR community event |

## Repository layout

```
site/                 the website (plain HTML, CSS and JS, no build step)
docs/                 strategy, pricing, packaging, design and decision records
design-lab/           design mockups and the copy and contrast checks
assignments/          earlier team work
final assignment.md   the assignment brief and rubric
devansh_notes.md      project notes
```

## Run locally and redeploy

```bash
cd site && python3 -m http.server 8765   # then open http://localhost:8765
```

GitHub Pages serves the site from the `gh-pages` branch. After editing `site/`, commit and run:

```bash
git subtree push --prefix site origin gh-pages
```

This is a course project and Sphyr is not on sale. The 2018 pilot was a paper-and-pen trial of the method, before today's software.
