// Phone and tablet menu. The open, close, Escape, outside click and focus return come from the popover
// attribute (works without this file); this file keeps aria-expanded in step and closes the menu when a
// link is followed, so a same-page anchor does not stay covered.
(() => {
  const menu = document.getElementById("nav-menu");
  if (!menu) return;
  const btn = document.querySelector('[popovertarget="nav-menu"]');
  menu.addEventListener("toggle", (e) => {
    btn?.setAttribute("aria-expanded", String(e.newState === "open"));
  });
  menu.addEventListener("click", (e) => {
    if (e.target.closest("a")) menu.hidePopover();
  });
})();
