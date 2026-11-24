"""Copy scan for Sphyr pages: every visible string, aria-label, alt and title against the never-say lists.

Run: python3 design-lab/copy_scan.py design-lab/home.html
Sources of the lists: docs/strategy/message_guideline.md sections 4, 5, 10 and 11, docs/product/do_not_claim.md,
docs/pricing/pricing_summary.md ("What not to say"), docs/design/slop_rules.md.
Each hit is printed with its string. A hit is not always a violation: a line that denies something
("No AI writes or scores it") matches the term; ALLOWED lists the exact strings a person has reviewed.
Exit code 1 if any unreviewed hit remains.
"""
import re
import sys
from html.parser import HTMLParser

NEVER = {
    "anonymity claim": r"\banonymous\b|fully anonymi|untraceable|nobody can see",
    "fairness claim": r"\bunbiased\b|\bobjective\b|fair promotion|ends favouritism|stops politics|bias-free|eliminat\w* bias",
    "replaces": r"\breplaces?\b",
    "AI wording": r"\bAI\b|\bsmart\b|intelligent",
    "real-time": r"real[- ]time",
    "surveillance": r"\btrack(s|ing)?\b|\bmonitor(s|ing)?\b|productivity",
    "integrations": r"integrat|Keka|Darwinbox|Slack|\bTeams\b|\bSSO\b|\bAPI\b|webhook",
    "social proof": r"trusted by|our customers|loved by|\breviews?\b|testimonial|case stud",
    "pilot numbers as results": r"94%|88%|0% collusion|customers see|firms see|customers save",
    "roadmap": r"Who Should We Promote|mobile app|journal|coaching|pulse survey",
    "wrong call to action": r"live demo|free trial|sign up free|get started",
    "money promise": r"\brefund|money[- ]back|price[- ]lock",
    "hype": r"seamless|empower|unlock|revolution|cutting[- ]edge|leverage|world[- ]class|elevate|game[- ]changing|supercharge|robust",
    "endorsement": r"endorse|in partnership with|IMCI|NHRDN",
    "announcing absence": r"no customers|not have customers|we.re new|no reviews yet|nobody has used|no track record",
}
MONTHS = r"\b(January|February|March|April|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b"  # case-sensitive; "May" left out (the word may)
DASHES = r"[—–]|\s--\s"
EMOJI = r"[\U0001F300-\U0001FAFF☀-➿]"

# Strings reviewed by a person: the term is used in a denial or a required qualifier, not as a claim.
ALLOWED = {
    # Denials and required statements: the term is used to say what Sphyr does not do or does not offer.
    "Sphyr hands partners a record and leaves the decision with them. The feedback in that record comes only from what colleagues chose to say on their cards, and Sphyr logs no hours or screen activity. No AI writes or scores anything. Your people come in from a spreadsheet, and Sphyr sits beside your HR system.",
    "If you sign afterwards, the ₹25,000 comes off your first annual bill. If you don't, you get your data as a spreadsheet (CSV) and we delete the rest. The fee isn't refunded.",
    # Propaganda channel table column header; every answer in it is "No".
    "Tracks anyone?",
    # Cited research fact (message guideline section 3).
    "of employees strongly agree that their performance reviews are fair, and 26% that they are accurate.",
    # "Review" names an engagement type, the competitor category, or our closing results review.
    "Pricing review",
    "₹149 is 32% of the lowest list price we found for a dedicated review tool: PerformYard's $5 a seat, about ₹464, for firms of several hundred people. Peoplebox and Confirm start at about ₹743, so we are about a fifth of theirs. We read these prices on 24 November 2026.",
    "The pilot fee covers our cost of running the 12 weeks, from setup to the results review at the end. If you sign, all of it counts towards your first year.",
    # Prototype microcopy inside product frames, shown as the real product.
    "Nothing to review",
    "Compare team health, spot coaching priorities, and decide feedback edit requests.",
    "24 of 25 reviews given",
    # Prototype sample dates in product frames (chart axis, comment dates). Flagged to the lead under the no-month rule.
    "May 05", "May 19", "Jun 02", "Jun 16", "Jun 30", "Jul 22", "Jul 25",
}


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        for k, v in attrs:
            if k in ("aria-label", "alt", "title", "content") and v:
                self.out.append(v.strip())

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1

    def handle_data(self, data):
        t = " ".join(data.split())
        if t and not self.skip:
            self.out.append(t)


def main(path):
    p = Text()
    p.feed(open(path, encoding="utf8").read())
    strings = [s for s in p.out if not s.startswith(("width=", "light dark", "text/html"))]
    hits, reviewed = [], 0
    for s in strings:
        checks = {**NEVER, "dash": DASHES, "emoji": EMOJI}
        for name, rx in checks.items():
            if re.search(rx, s, re.I):
                if s in ALLOWED:
                    reviewed += 1
                else:
                    hits.append((name, s))
        if re.search(MONTHS, s) and s not in ALLOWED:
            hits.append(("month name", s))
    for name, s in hits:
        print(f"HIT [{name}] {s[:140]}")
    print(f"{len(strings)} strings checked, {len(hits)} unreviewed hits, {reviewed} reviewed denials")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
