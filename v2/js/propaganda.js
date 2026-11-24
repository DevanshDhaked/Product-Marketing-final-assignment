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

  let picked = -1;
  let pickedAt = 0;
  const fit = () => { toc.open = wide.matches; };
  toc.classList.add("is-live");
  fit();
  wide.addEventListener("change", fit);

  toc.addEventListener("click", (e) => {
    const a = e.target.closest("a");
    if (!a) return;
    picked = links.indexOf(a);
    pickedAt = performance.now();
    mark(picked); // the page may not move at all if it is already scrolled to the end
    if (!wide.matches) toc.open = false;
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
  // The current section is the last one whose top has passed a line 160px down the screen, just under
  // the sticky nav and bar. Observers only trigger the check: a 2px band on that line fires when a
  // section edge crosses it, and it is rebuilt when the window is resized. At the very end of
  // the page the last sections cannot scroll that high, so when the footer is fully on screen the
  // last section is marked, unless a contents link was just used.
  const LINE = 160;
  let atEnd = false;
  const update = () => {
    let i = 0;
    sections.forEach((s, j) => { if (s.getBoundingClientRect().top < LINE + 2) i = j; });
    // shortcut: a click counts for 1s, which covers an instant jump; upgrade if smooth scrolling is added.
    if (atEnd) i = picked >= 0 && performance.now() - pickedAt < 1000 ? picked : sections.length - 1;
    mark(i);
  };
  let io;
  const watch = () => {
    io?.disconnect();
    io = new IntersectionObserver(update, { rootMargin: `-${LINE}px 0px ${LINE + 2 - innerHeight}px 0px` });
    sections.forEach((s) => io.observe(s));
  };
  watch();
  addEventListener("resize", watch);
  const foot = document.querySelector(".foot");
  if (foot) {
    new IntersectionObserver(([e]) => {
      atEnd = e.intersectionRatio >= 0.98;
      update();
    }, { threshold: [0, 0.98, 1] }).observe(foot);
  }
  update();
})();
