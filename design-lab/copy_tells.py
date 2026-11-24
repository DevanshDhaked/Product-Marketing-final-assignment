"""Count humanizer tells in a page's visible copy (not product frames): 'X, not Y' contrasts and triads.

Run: python3 design-lab/copy_tells.py design-lab/home.html
Contrast: a sentence that sets a negative half against a positive one (", not ", "not ... but", "rather than",
"instead of", or a sentence pair "...not X. ... Y"). Triad: a list of exactly three items ("A, B and C").
Product frames (.stage) are excluded: their text is the prototype's own microcopy.
Prints each hit so a person can confirm it; the counts are a screen, not a verdict.
"""
import re
import sys
from html.parser import HTMLParser


class Visible(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.out, self.buf = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        skip = tag in ("script", "style") or "stage" in (a.get("class") or "").split() or "cv" in (a.get("class") or "").split() or tag == "svg" and "circle" in (a.get("class") or "")
        self.stack.append((tag, skip))

    def handle_endtag(self, tag):
        while self.stack:
            t, _ = self.stack.pop()
            if t == tag:
                break

    def handle_data(self, data):
        if any(s for _, s in self.stack):
            return
        t = " ".join(data.split())
        if t:
            self.out.append(t)


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+", text) if s.strip()]


CONTRAST = re.compile(r",\s*not\b|\bnot\s+\w+(\s+\w+){0,6}\s+but\b|\brather than\b|\binstead of\b|\bnot the\b|\bnot a\b|\bnot one\b", re.I)
TRIAD = re.compile(r"\b[\w'₹%-]+(?:\s[\w'₹%-]+){0,4},\s[\w'₹%-]+(?:\s[\w'₹%-]+){0,4},?\s(?:and|or)\s[\w'₹%-]+", re.I)


def main(path):
    v = Visible()
    v.feed(open(path, encoding="utf8").read())
    text = " ".join(v.out)
    c_hits, t_hits = [], []
    for s in sentences(text):
        if CONTRAST.search(s):
            c_hits.append(s)
        for m in TRIAD.finditer(s):
            if m.group(0).count(",") == 2 or (m.group(0).count(",") == 1):
                t_hits.append(m.group(0))
    for s in c_hits:
        print("CONTRAST:", s[:150])
    for s in t_hits:
        print("TRIAD?  :", s[:150])
    print(f"{len(c_hits)} contrast sentences, {len(t_hits)} possible triads (confirm by eye)")


if __name__ == "__main__":
    main(sys.argv[1])
