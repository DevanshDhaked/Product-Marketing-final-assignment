// Propaganda page contents (.toc, a <details> that is open in the HTML so it works without JS).
// Wide screens: always open, a sticky column. Phones: a closed sticky bar that shows the current
// section, closes on link tap and on Escape. The section in view comes from one IntersectionObserver;
// there is no scroll listener and no animation loop.
(() => {
  const toc = document.querySelector(".toc");
  if (!toc) return;
  const summary = toc.querySelector("summary");
  const now = toc.querySelector(".toc-now");
  const links = [...toc.querySelectorAll('a[href^="#"]')];
  const sections = links.map((a) => document.getElementById(a.hash.slice(1)));
  const wide = matchMedia("(min-width: 901px)");

  const fit = () => { toc.open = wide.matches; };
  toc.classList.add("is-live");
  fit();
  wide.addEventListener("change", fit);

  toc.addEventListener("click", (e) => {
    if (!wide.matches && e.target.closest("a")) toc.open = false;
  });
  toc.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && toc.open && !wide.matches) {
      toc.open = false;
      summary.focus();
    }
  });

  const mark = (i) => {
    links.forEach((a, j) => (j === i ? a.setAttribute("aria-current", "true") : a.removeAttribute("aria-current")));
    now.textContent = links[i].textContent;
  };
  // A section is "in view" while it crosses a band from just under the sticky bars to 45% down the
  // screen; the first one in page order wins. Between sections the last mark stays.
  const inBand = new Set();
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => (e.isIntersecting ? inBand.add(e.target) : inBand.delete(e.target)));
    const i = sections.findIndex((s) => inBand.has(s));
    if (i >= 0) mark(i);
  }, { rootMargin: "-120px 0px -55% 0px" });
  sections.forEach((s) => s && io.observe(s));
  mark(0);
})();
