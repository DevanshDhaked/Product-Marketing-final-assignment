// The 2-minute walkthrough (demo.html). Reveals one step at a time. Everything after step 1
// follows the pick. Nothing is stored or sent: no storage, no network.
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var SCALE = 50; // bar length scale shared by both columns, so the bars compare fairly

  // Counts match the Member Insights columns in demo.html (collaborators out of a circle of 14).
  var people = {
    tara: {
      first: "Tara", full: "Tara Menon", initials: "TM", av: "av-amber", others: 10,
      compare: "Tara's cards came from 10 of the 14 people in that circle, against 13 for Nikhil. The tags they picked most for Tara were Stakeholder-centric and Customer First.",
      turn: "You picked Tara, and Tara's record backs what you saw in client meetings. It also shows 13 colleagues who saw Nikhil's work over six cycles, and very little of that work reached you. Partners still decide, now with both records open."
    },
    nikhil: {
      first: "Nikhil", full: "Nikhil Rao", initials: "NR", av: "av-blue", others: 13,
      compare: "Nikhil's cards came from 13 of the 14 people in that circle, against 10 for Tara. The tags they picked most for Nikhil were Takes Initiative and Solution-oriented.",
      turn: "You picked Nikhil on a hunch, and the hunch now has a record behind it: 13 colleagues over six cycles, in their own words. Partners still decide, with what the people who saw the work said in front of them."
    }
  };
  var marks = $$(".wt-progress li");
  var pick = null, started = 0;

  function done(n) { if (marks[n - 1]) marks[n - 1].classList.add("is-done"); }

  // The next step appears below with no scroll and no focus move, so the local answer stays in view
  // and arrow keys keep moving between radios (WCAG 3.2.2).
  function reveal(id) {
    var s = document.getElementById(id);
    if (!s.classList.contains("wt-locked")) return;
    s.classList.remove("wt-locked");
    s.classList.add("is-new");
  }

  // Step 1: the pick
  $$('input[name="wt-pick"]').forEach(function (r) {
    r.addEventListener("change", function () {
      pick = r.value;
      var p = people[pick];
      $("#reply-1").textContent = "You picked " + p.first + ". We'll come back to that at the end.";
      $$("[data-first]").forEach(function (el) { el.textContent = p.first; });
      $$("[data-full]").forEach(function (el) { el.textContent = p.full; });
      $$("[data-av]").forEach(function (el) { el.textContent = p.initials; el.className = "fx-avatar " + p.av; });
      $("#compare").textContent = p.compare;
      $("#turn").textContent = p.turn;
      done(1);
      reveal("step-2");
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
    var reply, p = people[pick], col = $('[data-col="' + pick + '"]');

    if (answer === "none") {
      reply = took + " This card tells Sphyr you didn't work with " + p.first + " this fortnight, so it adds nothing to " + p.first + "'s record. The option is there so that people with nothing to rate don't have to make something up.";
    } else {
      reply = took + " Your card joins those from " + p.others + " other colleagues in " + p.first + "'s record, and " + p.first + " sees what you said without your name on it.";
      var resp = $(".fx-kpi .v", col);
      resp.textContent = Number(resp.textContent) + 1;
      var list = answer === "good" ? ".wt-tags" : ".wt-areas";
      $$(".fx-step-" + answer + " input:checked").forEach(function (c) {
        $$(list + " li", col).forEach(function (li) { if (li.dataset.tag === c.value) bump(li); });
      });
      var said = text.value.trim();
      if (said) {
        var item = document.createElement("div");
        item.className = "fx-fb-item";
        item.innerHTML = '<div class="fx-fb-label"><span>Anonymized Feedback</span><span>Cycle 6</span></div><p class="fx-fb-text"></p>';
        $(".fx-fb-text", item).textContent = said; // the visitor's words, never parsed as HTML
        var head = $(".wt-feed .fx-card-head", col);
        head.parentNode.insertBefore(item, head.nextSibling);
      }
      $("#yours").hidden = false;
    }

    var icon = { good: "i-smile", improve: "i-frown", none: "i-minus" }[answer];
    $("#done-icon").setAttribute("href", "assets/icons.svg#" + icon);
    body.hidden = true;
    $("#card-done").hidden = false;
    $("#reply-2").textContent = reply;
    // The card now sits in the picked column, so the pick can no longer change under it.
    $$('input[name="wt-pick"]').forEach(function (r) { r.disabled = true; });
    done(2); done(3); done(4);
    reveal("step-3");
    reveal("step-4");
    $("#card-done").focus({ preventScroll: true }); // Submit is gone; keep focus on its answer, in place
    // The card got shorter, which can leave the answer above the screen on phones. Bring it back, instantly.
    var r = $("#reply-2").getBoundingClientRect();
    if (r.top < 64 || r.bottom > window.innerHeight) $("#card-done").scrollIntoView({ block: "start" });
  });
})();
