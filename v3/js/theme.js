// Two-state theme toggle (light, dark) that starts from the system setting.
// The tiny inline script in <head> applies a stored choice before first paint; this file
// handles clicks, other tabs and system changes. Pattern: Chrome for Developers,
// "Dark mode toggles" (developer.chrome.com/docs/modern-web-guidance/guides/ui-components/dark-mode-toggle, accessed 2026-11-24).
(() => {
  const KEY = "sphyr-theme";
  const root = document.documentElement;
  const mq = matchMedia("(prefers-color-scheme: dark)");
  const system = () => (mq.matches ? "dark" : "light");
  const shown = () => root.dataset.theme || system();

  const render = () => {
    for (const b of document.querySelectorAll("[data-theme-toggle]")) {
      b.setAttribute("aria-pressed", String(shown() === "dark"));
    }
  };
  const apply = (t) => {
    if (t === "light" || t === "dark") root.dataset.theme = t;
    else delete root.dataset.theme;
    render();
  };

  // Target is the opposite of what is on screen. If it equals the system setting the user is
  // undoing their choice, so the stored value is removed rather than pinned.
  const toggle = () => {
    const target = shown() === "dark" ? "light" : "dark";
    const pin = target === system() ? null : target;
    try { pin ? localStorage.setItem(KEY, pin) : localStorage.removeItem(KEY); } catch (e) { /* storage blocked: theme still applies for this page */ }
    apply(pin);
  };

  document.addEventListener("click", (e) => {
    if (e.target.closest("[data-theme-toggle]")) toggle();
  });
  // No stored choice: follow the system live. A stored choice is never cleared here.
  mq.addEventListener("change", render);
  addEventListener("storage", (e) => { if (e.key === KEY) apply(e.newValue); });
  render();
})();
