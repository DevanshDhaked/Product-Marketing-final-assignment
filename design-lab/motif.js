// Ribbon motif behaviour. Everything here is an enhancement: without it the page shows the finished pictures.
(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // 1. Inline the mark where data-mark is set, so single ribbons can animate and part on hover.
  //    Without fetch (or on file://) the <use> reference stays and the mark still shows.
  const marks = document.querySelectorAll("svg[data-mark]");
  if (marks.length) {
    fetch("assets/sphyr-mark.svg").then((r) => r.text()).then((txt) => {
      const sym = new DOMParser().parseFromString(txt, "image/svg+xml").querySelector("#mark g");
      if (!sym) return;
      for (const svg of marks) {
        const g = sym.cloneNode(true);
        svg.querySelector("use")?.remove();
        svg.append(g);
        const box = svg.viewBox.baseVal;
        const cx = box.width / 2, cy = box.height / 2;
        g.querySelectorAll(".rib").forEach((p, k) => {
          p.style.setProperty("--k", k);
          // Hover offset: each ribbon moves a little away from the sphere's centre.
          const b = p.getBBox();
          const m = g.transform.baseVal.consolidate()?.matrix;
          const bx = m ? m.a * (b.x + b.width / 2) + m.e : b.x + b.width / 2;
          const by = m ? m.d * (b.y + b.height / 2) + m.f : b.y + b.height / 2;
          const len = Math.hypot(bx - cx, by - cy) || 1;
          p.style.setProperty("--dx", `${((bx - cx) / len) * 70}px`);
          p.style.setProperty("--dy", `${((by - cy) / len) * 70}px`);
        });
      }
    }).catch(() => {});
  }

  // 2. Replay the core visual.
  document.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-replay]");
    if (!btn) return;
    // Restart both compositions (wide and phone); only one is visible.
    for (const cv of document.getElementById(btn.dataset.replay).closest("figure").querySelectorAll(".cv")) {
      cv.classList.remove("play");
      void cv.getBoundingClientRect(); // restart CSS animations
      cv.classList.add("play");
    }
  });

  // 3. The circle: play once in view where scroll-driven animation is not supported.
  if (!reduce && !CSS.supports("animation-timeline: view()")) {
    const io = new IntersectionObserver((entries) => {
      for (const en of entries) if (en.isIntersecting) { en.target.classList.add("play"); io.unobserve(en.target); }
    }, { threshold: 0.35 });
    document.querySelectorAll(".circle").forEach((c) => io.observe(c));
  }

  // 4. Circle groups: show one group's people.
  document.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-group]");
    if (!btn) return;
    const circle = document.getElementById(btn.closest("[data-circle]").dataset.circle);
    const on = btn.getAttribute("aria-pressed") !== "true";
    btn.parentElement.querySelectorAll("[data-group]").forEach((b) => b.setAttribute("aria-pressed", "false"));
    btn.setAttribute("aria-pressed", String(on));
    if (on) circle.dataset.focus = btn.dataset.group; else delete circle.dataset.focus;
  });

  // 5. Lab only: strand palette switch.
  document.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-set-strands]");
    if (!btn) return;
    document.body.dataset.strands = btn.dataset.setStrands;
    btn.parentElement.querySelectorAll("button").forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
  });
})();
