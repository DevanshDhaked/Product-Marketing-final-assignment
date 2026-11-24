// The 2-minute walkthrough (demo.html). Reveals one step at a time and adds the visitor's card to
// Nikhil's column. Nothing is stored or sent: no storage, no network.
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var calm = window.matchMedia("(prefers-reduced-motion: reduce)");
  var SCALE = 50; // bar length scale shared by both columns, so the bars compare fairly

  var names = { tara: "Tara", nikhil: "Nikhil" };
  var turns = {
    tara: "You picked Tara, and you might still be right, because partners still decide. You now decide with more in front of you: 13 colleagues saw Nikhil's work over six cycles, and very little of it reached you in a client meeting.",
    nikhil: "You picked Nikhil on a hunch, and the hunch now has a record behind it: 13 colleagues over six cycles, in their own words. Partners still decide, with what the people who saw the work said in front of them."
  };
  var marks = $$(".wt-progress li");
  var pick = null, started = 0;

  function done(n) { if (marks[n - 1]) marks[n - 1].classList.add("is-done"); }

  function reveal(id, focus) {
    var s = document.getElementById(id);
    if (!s.classList.contains("wt-locked")) return;
    s.classList.remove("wt-locked");
    s.classList.add("is-new");
    if (!focus) return;
    var h = $("h2", s);
    s.scrollIntoView({ behavior: calm.matches ? "auto" : "smooth", block: "start" });
    h.focus({ preventScroll: true });
  }

  // Step 1: the pick
  $$('input[name="wt-pick"]').forEach(function (r) {
    r.addEventListener("change", function () {
      pick = r.value;
      $("#reply-1").textContent = "You picked " + names[pick] + ". We'll come back to that at the end.";
      $("#turn").textContent = turns[pick];
      done(1);
      reveal("step-2", true);
    });
  });

  // Step 2: the card
  var body = $("#card-body"), submit = $("#wt-submit"), text = $("#wt-text"), count = $("#wt-count");
  function start() { if (!started) started = Date.now(); }
  body.addEventListener("pointerdown", start);
  body.addEventListener("keydown", start);
  body.addEventListener("change", start);
  $$('input[name="wt-exp"]').forEach(function (r) {
    r.addEventListener("change", function () { submit.disabled = false; });
  });
  text.addEventListener("input", function () { count.textContent = text.value.length + "/400"; });

  function bump(li) {
    var b = $(".num", li), n = Number(b.textContent) + 1;
    b.textContent = n;
    var bar = $(".fx-track > i", li);
    if (bar) bar.style.setProperty("--w", Math.min(n / SCALE, 1));
  }

  submit.addEventListener("click", function () {
    var answer = $('input[name="wt-exp"]:checked');
    if (!answer) return;
    answer = answer.value;
    var secs = Math.max(1, Math.round((Date.now() - (started || Date.now())) / 1000));
    var took = "That took you " + secs + (secs === 1 ? " second." : " seconds.");
    var reply;

    if (answer === "none") {
      reply = took + " This card tells Sphyr you didn't work with Nikhil this fortnight, so it adds nothing to his record. The option is there so that people with nothing to rate don't have to make something up.";
    } else {
      reply = took + " Your card joins the other 13 from Nikhil's circle this cycle, and Nikhil sees what you said without your name on it.";
      var resp = $("#n-responses");
      resp.textContent = Number(resp.textContent) + 1;
      var list = answer === "good" ? "#n-tags" : "#n-areas";
      $$(".fx-step-" + answer + " input:checked").forEach(function (c) {
        $$(list + " li").forEach(function (li) { if (li.dataset.tag === c.value) bump(li); });
      });
      var said = text.value.trim();
      if (said) {
        var item = document.createElement("div");
        item.className = "fx-fb-item";
        item.innerHTML = '<div class="fx-fb-label"><span>Anonymized Feedback</span><span>Cycle 6</span></div><p class="fx-fb-text"></p>';
        $(".fx-fb-text", item).textContent = said; // the visitor's words, never parsed as HTML
        var head = $("#n-feed .fx-card-head");
        head.parentNode.insertBefore(item, head.nextSibling);
      }
      $("#yours").hidden = false;
    }

    var icon = { good: "i-smile", improve: "i-frown", none: "i-minus" }[answer];
    $("#done-icon").setAttribute("href", "assets/icons.svg#" + icon);
    body.hidden = true;
    $("#card-done").hidden = false;
    $("#reply-2").textContent = reply;
    done(2); done(3); done(4);
    reveal("step-4", false);
    reveal("step-3", true);
  });
})();
