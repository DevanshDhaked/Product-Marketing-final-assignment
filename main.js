// Feedback card: any .fcard on the page becomes playable.
document.querySelectorAll('.fcard').forEach(card => {
  let clicks = 0;
  const counter = card.querySelector('.clicks');
  const bump = () => { clicks++; if (counter) counter.textContent = clicks + (clicks === 1 ? ' click' : ' clicks'); };
  card.querySelectorAll('.stars button').forEach(b => b.addEventListener('click', () => {
    card.querySelectorAll('.stars button').forEach(x => x.classList.toggle('on', +x.dataset.v <= +b.dataset.v));
    card.dataset.rating = b.dataset.v; bump();
  }));
  card.querySelectorAll('.tags button').forEach(b => b.addEventListener('click', () => { b.classList.toggle('on'); bump(); }));
  const send = card.querySelector('.send');
  if (send) send.addEventListener('click', () => {
    if (!card.dataset.rating) { card.querySelector('.stars').animate([{transform:'translateX(-4px)'},{transform:'translateX(4px)'},{transform:'none'}], 200); return; }
    bump();
    card.classList.add('sent');
    const out = card.querySelector('.clicks-final');
    if (out) out.textContent = clicks;
    card.dispatchEvent(new CustomEvent('sent', { bubbles: true }));
  });
});

// Pricing calculator. Rs 149 x 12 x headcount, + 18% GST; pilot Rs 15,000 credited on first bill.
const inr = n => '₹' + Math.round(n).toLocaleString('en-IN');
const calc = document.getElementById('calc');
if (calc) {
  const run = () => {
    const n = Math.max(1, +calc.querySelector('#heads').value || 0);
    const annual = n * 149 * 12;
    calc.querySelector('#c-annual').textContent = inr(annual);
    calc.querySelector('#c-gst').textContent = inr(annual * 0.18);
    calc.querySelector('#c-first').textContent = inr(annual * 1.18 - 15000);
    calc.querySelector('#c-month').textContent = inr(n * 149);
  };
  calc.addEventListener('input', run); run();
}

// Order form (course prototype: nothing is sent anywhere).
const order = document.getElementById('order');
if (order) order.addEventListener('submit', e => {
  e.preventDefault();
  const n = +order.heads.value;
  order.querySelector('.result').innerHTML =
    `<b>Pilot request recorded (prototype).</b><br>Six-week pilot for ${n} people: ${inr(15000)} + GST, credited against your first annual bill of ${inr(n * 149 * 12)} + GST. ` +
    `In the live product this page would confirm a kickoff call and send your welcome kit. No data left this page.`;
});
