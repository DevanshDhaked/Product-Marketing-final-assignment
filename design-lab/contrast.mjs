// WCAG 2.x contrast check for design-lab/tokens.css, both themes.
// Run: node design-lab/contrast.mjs [path/to/file.css]   (default design-lab/tokens.css; prints a markdown table, exits 1 on any failure)
// Text pairs need 4.5:1 (AA, normal text). Non-text pairs (control outlines, focus ring,
// chart marks, icons) need 3:1 (WCAG 1.4.11).
import { readFileSync } from "node:fs";

const css = readFileSync(process.argv[2] ?? new URL("./tokens.css", import.meta.url), "utf8");
const tokens = {};
for (const m of css.matchAll(/--([\w-]+):\s*light-dark\((#[0-9a-fA-F]{6}),\s*(#[0-9a-fA-F]{6})\)/g)) {
  tokens[m[1]] = { light: m[2], dark: m[3] };
}

const lum = (hex) => {
  const c = [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16) / 255)
    .map((v) => (v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4));
  return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
};
const ratio = (a, b) => {
  const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05);
};

const TEXT = 4.5, UI = 3;
const pairs = [
  ["text", "bg", TEXT], ["text", "surface", TEXT], ["text", "surface-sunk", TEXT], ["text", "surface-raised", TEXT],
  ["text-muted", "bg", TEXT], ["text-muted", "surface", TEXT], ["text-muted", "surface-sunk", TEXT], ["text-muted", "surface-raised", TEXT],
  ["link", "bg", TEXT], ["link", "surface", TEXT], ["link", "surface-sunk", TEXT],
  ["on-action", "action", TEXT], ["on-action", "action-hover", TEXT],
  ["on-positive-soft", "positive-soft", TEXT], ["on-positive-soft", "bg", TEXT], ["on-positive-soft", "surface", TEXT],
  ["on-constructive-soft", "constructive-soft", TEXT],
  ["text", "avatar-blue", TEXT], ["text", "avatar-mint", TEXT], ["text", "avatar-amber", TEXT], ["text", "avatar-rose", TEXT], ["text", "avatar-violet", TEXT],
  ["text-muted", "stage-ground", TEXT],
  ["text", "positive-soft", TEXT], ["text-muted", "positive-soft", TEXT], ["on-positive-soft", "surface-raised", TEXT],
  ["text-muted", "constructive-soft", TEXT], ["text", "constructive-soft", TEXT],
  ["destructive", "bg", TEXT], ["destructive", "surface", TEXT],
  ["text", "surface-sunk", TEXT], ["text-muted", "surface-sunk", TEXT],
  // Prototype palette inside faux UI frames.
  ["p-text", "p-bg", TEXT], ["p-text", "p-surface", TEXT], ["p-text", "p-surface-sunk", TEXT],
  ["p-text-muted", "p-bg", TEXT], ["p-text-muted", "p-surface", TEXT], ["p-text-muted", "p-surface-sunk", TEXT], ["p-text-muted", "p-surface-raised", TEXT],
  ["link", "p-bg", TEXT], ["link", "p-surface", TEXT], ["on-positive-soft", "p-surface", TEXT], ["on-positive-soft", "p-surface-raised", TEXT],
  ["p-text", "avatar-blue", TEXT], ["p-text", "avatar-mint", TEXT], ["p-text", "avatar-amber", TEXT],
  ["p-border-strong", "p-surface", UI], ["action", "p-surface", UI],
  ["border-strong", "bg", UI], ["border-strong", "surface", UI],
  ["focus", "bg", UI], ["focus", "surface", UI],
  ["action", "bg", UI], ["action", "surface", UI],
  ["brand", "surface", UI], ["constructive", "surface", UI],
  ["chart-2", "surface", UI], ["neutral-state", "surface", UI],
];

// Self-check of the formula against known values (black on white is 21:1).
if (Math.abs(ratio("#000000", "#FFFFFF") - 21) > 0.01) throw new Error("contrast formula broken");

let fails = 0;
const rows = ["| Foreground | Background | Need | Light | Dark |", "|---|---|---|---|---|"];
for (const [fg, bg, need] of pairs) {
  if (!tokens[fg] || !tokens[bg]) { console.error(`missing token: ${!tokens[fg] ? fg : bg}`); fails++; continue; }
  const cell = (t) => {
    const r = ratio(tokens[fg][t], tokens[bg][t]);
    const ok = r >= need;
    if (!ok) fails++;
    return `${r.toFixed(2)}${ok ? "" : " FAIL"}`;
  };
  rows.push(`| --${fg} | --${bg} | ${need}:1 | ${cell("light")} | ${cell("dark")} |`);
}
console.log(rows.join("\n"));
console.log(`\n${pairs.length * 2} checks, ${fails} failures`);
process.exit(fails ? 1 : 0);
