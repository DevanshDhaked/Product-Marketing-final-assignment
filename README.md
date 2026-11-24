# Sphyr: Promote on merit, not politics.

Team 03's final assignment for Product Marketing (PD2.501), IIIT Hyderabad.
**Aryan · Abhinav · Devansh · Bheema**

### 🔗 Live site: **https://devanshdhaked.github.io/Product-Marketing-final-assignment/**

## The four deliverables

| # | Deliverable | Link |
|---|---|---|
| 01 | Website (central hub) | [Home](https://devanshdhaked.github.io/Product-Marketing-final-assignment/) · [All deliverables](https://devanshdhaked.github.io/Product-Marketing-final-assignment/deliverables.html) |
| 02 | Propaganda strategy | [propaganda.html](https://devanshdhaked.github.io/Product-Marketing-final-assignment/propaganda.html) |
| 03 | Three LinkedIn posts | [linkedin.html](https://devanshdhaked.github.io/Product-Marketing-final-assignment/linkedin.html) |
| 04 | Advertisement | [ad.html](https://devanshdhaked.github.io/Product-Marketing-final-assignment/ad.html) |

No sign-in is needed for anything.

## The product

Sphyr is a continuous 360-degree feedback tool for performance appraisals. Every fortnight, each employee gets two-minute anonymous ratings from everyone they work with: manager, peers, juniors, other leads, and clients and vendors. Ratings are pooled before anyone sees them, so promotions run on months of evidence, not one manager's memory. It runs alongside the company's existing HR system.

Sources: Sphyr Overview Whitepaper v0.3 (2018, Ravi Warrier) and the Sphyr.io product documentation.

## Strategy at a glance

| | |
|---|---|
| **Segment** | Founders of growing companies (50–300 people) who sign off on promotions but can't see who did what |
| **Persona** | Meera, Head of People at a growing IT services company: the champion who takes the case to the founder |
| **Central message** | *Promote on merit, not politics.* Built from everyone who actually worked with them, not one manager's memory. |
| **Belief to shift** | "My managers know who's good" → "One view is a guess; everyone's view over time is evidence" |
| **Pricing** | ₹149 per employee per month, billed annually, + GST. One flat rate. Clients and vendors free. |
| **Entry offer** | ₹15,000 six-week paid pilot, credited against the first bill. Full refund if the first six cycles show nothing new. |
| **Channels** | LinkedIn organic + LinkedIn Sponsored Content → website → 2-minute walkthrough → pilot |

## Website pages

- **Home**: problem, interactive five-click feedback card, Meera's story, the fortnight loop, labelled 2018 pilot evidence
- **How it works**: the Sphere, the card, pooling and anonymity, values cascade, works alongside your HRMS
- **Walkthrough**: a 2-minute interactive demo on sample data, where you play a founder before a promotion round
- **Pricing**: flat ₹149, cost calculator, pilot, renewal terms, how the price was set, one-page order (prototype)
- **Trust**: who sees what, the three anonymity rules, feedback not surveillance, data handling

## Repository layout

```
site/                 the website (plain HTML/CSS/JS, no build step)
assignments/          earlier team work: communication objectives, packaging, pricing one-pager
final assignment.md   assignment brief and rubric
devansh_notes.md      project notes and open items
```

## Run locally / redeploy

```bash
cd site && python3 -m http.server 8765   # open http://localhost:8765
```

The live site is served by GitHub Pages from the `gh-pages` branch. After editing `site/`, commit and run:

```bash
git subtree push --prefix site origin gh-pages
```

---
*Course project. Not a live commercial offer. The pilot results are from a 2018 pen-and-paper trial of the method, not of today's software.*
