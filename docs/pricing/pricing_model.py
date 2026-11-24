"""Sphyr pricing model for Indian management consulting firms (40 to 400 professionals).

Run: python3 docs/pricing/pricing_model.py
Every input carries a source key (see the pricing docs' `sources` frontmatter) or the word
ESTIMATE with its reason. Money is in Indian rupees. L = lakh = 100,000.
"""

L = 100_000
CASES = ("low", "mid", "high")

# == 1. value per seat ==
VALUE = {
    # annual VOLUNTARY attrition rate (the exit-reason shares below are shares of voluntary leavers)
    # low: SPI 2025 Table 170, voluntary, 101 to 300 staff (global PS firms)
    # mid: Aon India 2025, voluntary 12.0% of 16.2% total (Business Today, 2 Mar 2026)
    # high: Aon India 2024 professional services 22.1% total x voluntary share in 2024
    #       (13.4% of 17.7% all-industry); the share applied to one sector is an ESTIMATE
    "attrition": {"low": 0.069, "mid": 0.120, "high": 0.221 * 13.4 / 17.7},
    # annual CTC of the person who leaves (consultant band)
    # low: Praxis senior associate consultant 17.8 to 19.7 L; mid: management consultant at
    # Avalon 21.5 to 24.5 L and Praxis 22.7 to 27.2 L; high: Praxis senior consultant 29.8 to 32.9 L
    "leaver_ctc": {"low": 18 * L, "mid": 24 * L, "high": 31 * L},
    # recruiter fee as share of first-year CTC (hirekey, savannahr)
    "recruiter_fee": {"low": 0.0833, "mid": 0.125, "high": 0.1667},
    # days to recruit and days to become productive (SPI 2025 Table 170, 101 to 300)
    "vacancy_days": {"low": 75.6, "mid": 75.6, "high": 75.6},
    "ramp_days": {"low": 58.6, "mid": 58.6, "high": 58.6},
    # ESTIMATE: share of vacancy days whose work is lost rather than covered by others
    "vacancy_uncovered": {"low": 0.25, "mid": 0.50, "high": 0.75},
    # ESTIMATE: average output during ramp
    "ramp_productivity": {"low": 0.5, "mid": 0.5, "high": 0.5},
    # ESTIMATE: loaded cost = CTC x 1.2 (office, tools, benefits not in CTC)
    "loading": {"low": 1.2, "mid": 1.2, "high": 1.2},
    # revenue per billable consultant / fully loaded cost (SPI 2025: $204k / $136k, 101 to 300)
    "revenue_to_cost": {"low": 1.5, "mid": 1.5, "high": 1.5},
    # ESTIMATE: partner and manager hours to interview and onboard one replacement
    "hiring_hours": {"low": 15, "mid": 25, "high": 40},
    # ESTIMATE: hourly loaded cost of that senior time (about 45 L CTC x 1.2 / 2,000 h)
    "senior_hourly": {"low": 2700, "mid": 2700, "high": 2700},
    # ESTIMATE: client and knowledge loss as share of leaver CTC, only in the high case
    "client_loss": {"low": 0.0, "mid": 0.0, "high": 0.10},
    # share of exits whose stated reason Sphyr could touch
    # low: SPI 2025 Table 172, lack of career advancement 14.9% + management dissatisfaction 5.5%
    # high: Gallup 2008, career advancement 31.5% + management and work environment 16.5%
    # mid: ESTIMATE between the two
    "exit_share_addressable": {"low": 0.204, "mid": 0.30, "high": 0.48},
    # ESTIMATE (no study exists for Sphyr): share of those exits Sphyr prevents
    "sphyr_effect": {"low": 0.10, "mid": 0.20, "high": 0.30},
    # review hours per person per year, firm-wide
    # low: Deloitte, about 2 million hours / 65,000 people (HBR 2015)
    # mid: CEB, 40 hours per employee (SHRM 2015)
    # high: CEB blend, 1 manager (210 h) per 5 employees (40 h each), span is an ESTIMATE
    "review_hours": {"low": 2_000_000 / 65_000, "mid": 40.0, "high": (5 * 40 + 210) / 6},
    # ESTIMATE: share of those hours Sphyr removes (project-end forms, chasing, building "the
    # file" before calibration). The calibration meeting itself stays.
    "hours_saved_share": {"low": 0.15, "mid": 0.25, "high": 0.35},
    # time Sphyr adds: 26 fortnightly cycles x 2 min 09 s per deck (whitepaper 2018 paper pilot)
    "sphyr_hours_added": {c: 26 * (2 + 9 / 60) / 60 for c in CASES},
    # ESTIMATE: blended firm-wide CTC per professional (pyramid of analysts to partners)
    "blended_ctc": {"low": 15 * L, "mid": 20 * L, "high": 25 * L},
    # ESTIMATE: share of saved hours that turns into billable or other useful work
    "time_realization": {"low": 0.5, "mid": 0.75, "high": 1.0},
    "work_hours_year": {c: 2000 for c in CASES},
    # ESTIMATE: partner hours per professional per year spent building and debating the record
    # before calibration (asking for "the file", reading forms, discussing each consultant)
    "partner_hours": {"low": 0.5, "mid": 1.0, "high": 2.0},
    # ESTIMATE: share of that partner time Sphyr removes (the record is already there)
    "partner_saved_share": {"low": 0.2, "mid": 0.3, "high": 0.4},
}


def exit_cost(c, v=VALUE):
    ctc = v["leaver_ctc"][c]
    loaded = ctc * v["loading"][c]
    revenue = loaded * v["revenue_to_cost"][c]
    parts = {
        "recruiter fee": ctc * v["recruiter_fee"][c],
        # seat empty: revenue lost minus cost saved, only for uncovered days
        "vacancy lost margin": (revenue - loaded) * v["vacancy_days"][c] / 365 * v["vacancy_uncovered"][c],
        # new hire paid in full, produces part of the revenue
        "ramp lost revenue": revenue * v["ramp_days"][c] / 365 * (1 - v["ramp_productivity"][c]),
        "partner and HR hiring time": v["hiring_hours"][c] * v["senior_hourly"][c],
        "client and knowledge loss": ctc * v["client_loss"][c],
    }
    return parts


def value_per_seat(c, v=VALUE):
    cost = sum(exit_cost(c, v).values())
    reduction = v["exit_share_addressable"][c] * v["sphyr_effect"][c]
    exits_avoided_per_seat = v["attrition"][c] * reduction
    attrition_year = exits_avoided_per_seat * cost
    hourly = v["blended_ctc"][c] * v["loading"][c] / v["work_hours_year"][c]
    net_hours = v["review_hours"][c] * v["hours_saved_share"][c] - v["sphyr_hours_added"][c]
    review_year = net_hours * hourly * v["time_realization"][c]
    partner_year = (v["partner_hours"][c] * v["partner_saved_share"][c] * v["senior_hourly"][c]
                    * v["time_realization"][c])
    review_year += partner_year
    return {
        "partner_month": partner_year / 12,
        "exit_cost": cost,
        "exit_cost_x_ctc": cost / v["leaver_ctc"][c],
        "relative_reduction": reduction,
        "exits_avoided_per_seat_year": exits_avoided_per_seat,
        "attrition_month": attrition_year / 12,
        "net_hours_saved": net_hours,
        "hourly": hourly,
        "review_month": review_year / 12,
        "total_month": (attrition_year + review_year) / 12,
    }


def print_value():
    print("== 1. Value per seat per month ==")
    for c in CASES:
        parts = exit_cost(c)
        print(f"\n[{c}] exit cost parts (leaver CTC Rs {VALUE['leaver_ctc'][c]:,.0f}):")
        for k, x in parts.items():
            print(f"  {k:28s} Rs {x:>10,.0f}")
        r = value_per_seat(c)
        print(f"  {'total per exit':28s} Rs {r['exit_cost']:>10,.0f}  ({r['exit_cost_x_ctc']:.2f} x CTC)")
        print(f"  relative reduction in exits  {r['relative_reduction']:.1%}")
        print(f"  exits avoided per seat/year  {r['exits_avoided_per_seat_year']:.5f}")
        print(f"  attrition value / seat / mo  Rs {r['attrition_month']:,.0f}")
        print(f"  net review hours saved/yr    {r['net_hours_saved']:.1f} h at Rs {r['hourly']:,.0f}/h")
        print(f"  staff time / mo              Rs {r['review_month'] - r['partner_month']:,.0f}")
        print(f"  partner time / mo            Rs {r['partner_month']:,.0f}")
        print(f"  review value / seat / mo     Rs {r['review_month']:,.0f} (incl. partner time)")
        print(f"  TOTAL value / seat / mo      Rs {r['total_month']:,.0f}")
    print("\nFirm view (same per-seat value at any size; shows how a firm saving becomes per seat):")
    for n in (40, 150, 400):
        for c in CASES:
            r = value_per_seat(c)
            avoided = n * r["exits_avoided_per_seat_year"]
            firm_year = r["total_month"] * 12 * n
            yrs = 1 / avoided if avoided else float("inf")
            print(f"  {n:3d} staff [{c:4s}] exits/yr {n * VALUE['attrition'][c]:5.1f}, avoided/yr {avoided:4.2f}"
                  f" (one every {yrs:4.1f} yr), firm value/yr Rs {firm_year:>11,.0f}"
                  f" -> / {n} / 12 = Rs {firm_year / n / 12:,.0f}")
    # the graded one-pager's implied number: Rs 500 x 100 staff x 12 = Rs 6 L for one exit
    print(f"\nOld one-pager check: Rs 500/seat/mo at 100 staff = Rs {500 * 100 * 12:,} per avoided exit per year")


# == 2. competitor anchors ==
USD_INR = 92.86  # exchangerates.org.uk close 23 Nov 2026
EUR_INR = 102.75  # exchangerates.org.uk 18 Nov 2026
REF_FIRM = 150  # reference firm size (head of talent persona)

# (name, plan, price per seat per month in source currency, currency, minimum annual USD or None)
COMPETITORS = [
    ("Lattice", "Performance", 10, "USD", 4000),
    ("Lattice", "Foundations bundle", 13, "USD", 4000),
    ("15Five", "Perform", 11, "USD", None),
    ("Leapsome", "Performance Reviews module", 7, "EUR", None),
    ("Peoplebox", "Performance Management", 8, "USD", None),
    ("Peoplebox", "Performance Management + 360 degree", 16, "USD", None),
    ("Confirm (WorkRamp Perform)", "Perform, from", 8, "USD", None),
    ("PerformYard", "per-seat, low end", 5, "USD", None),
    ("PerformYard", "per-seat, high end", 15, "USD", None),
]


def inr(price, cur):
    return price * (USD_INR if cur == "USD" else EUR_INR if cur == "EUR" else 1)


def keka_growth_per_seat(n):
    # Rs 15,999 a month for up to 100 employees, then Rs 150 per extra employee
    return (15999 + max(0, n - 100) * 150) / n


def greythr_growth_plus_pms_per_seat(n, pms=40):
    # Growth Rs 4,495 a month with 50 employees, Rs 85 per extra; PMS add-on Rs 35 to 45
    return (4495 + max(0, n - 50) * 85) / n + pms


def print_competitors():
    print("\n== 2. Competitor anchors (Rs per seat per month) ==")
    print(f"USD/INR {USD_INR}, EUR/INR {EUR_INR}")
    for name, plan, p, cur, minimum in COMPETITORS:
        line = f"  {name:28s} {plan:38s} {cur} {p:>5} = Rs {inr(p, cur):>6,.0f}"
        if minimum:
            seats = minimum / 12 / p
            line += f"  (min ${minimum:,}/yr binds below {seats:.0f} seats)"
        print(line)
    for n in (40, REF_FIRM, 400):
        print(f"  Keka Growth (full HRMS incl. reviews) at {n:3d} staff: Rs {keka_growth_per_seat(n):,.0f} per seat")
        print(f"  greytHR Growth + PMS add-on (Rs 40)   at {n:3d} staff: Rs {greythr_growth_plus_pms_per_seat(n):,.0f} per seat"
              f" (PMS alone Rs 35 to 45)")
    old_low, old_high = 665, 1425
    print(f"  Old one-pager check: 149 / {old_low} = {149 / old_low:.0%}, 149 / {old_high} = {149 / old_high:.0%}")


# == 3. cost to serve and margin floor ==
# ESTIMATE: employer cost on top of CTC (insurance, laptop, leave cover)
EMPLOYER_LOADING = 1.10
# customer success hourly cost: AmbitionBox average CSM CTC Rs 14.7 L x loading / 2,000 h
CS_HOURLY = 14.7 * L * EMPLOYER_LOADING / 2000

VARIABLE = {
    # ESTIMATE: storage, compute and bandwidth that grow with seats, Rs per seat per month
    "hosting per seat": 1.0,
    # ESTIMATE 8 emails per seat per month (invites, reminders, digests) x SES $0.16 per 1,000
    "email per seat": 8 * 0.16 / 1000 * USD_INR,
    # ESTIMATE: 0.05 support tickets per seat per month x 20 min at CS hourly cost
    "support per seat": 0.05 * 20 / 60 * CS_HOURLY,
}
# ESTIMATE: onboarding hours per firm (kickoff 1, import and setup 4, training 3,
# first-cycle support 6, handover 1, preparation 5), paid back over 12 months
ONBOARDING_HOURS = 20
# Razorpay 2% + 18% GST on the fee; ESTIMATE share of invoices paid by card or UPI
# (the rest by bank transfer at no fee)
GATEWAY_FEE = 0.02 * 1.18
GATEWAY_SHARE = 0.25
TARGET_GM = 0.80  # Benchmarkit CY2024 median 77%, subscription-only 81%


def variable_cost_per_seat(price, firm=REF_FIRM):
    parts = dict(VARIABLE)
    parts["onboarding, paid back over 12 months"] = ONBOARDING_HOURS * CS_HOURLY / 12 / firm
    parts["payment fees"] = price * GATEWAY_FEE * GATEWAY_SHARE
    return parts


def floor_price(firm=REF_FIRM):
    # solve p = cost(p) / (1 - GM), where cost has a part proportional to p
    fixed_part = sum(v for k, v in variable_cost_per_seat(0, firm).items())
    share = GATEWAY_FEE * GATEWAY_SHARE
    return fixed_part / (1 - TARGET_GM - share)


# == 4. fixed cost and break-even ==
# monthly fixed cost by line, Rs. People are CTC per year from AmbitionBox unless ESTIMATE.
PEOPLE = [
    # (role, FTE, CTC per year, basis)
    ("Founder, product and sales", 1, 20 * L, "ESTIMATE, paid like a senior CSM or designer"),
    ("Founder, engineering", 1, 20 * L, "ESTIMATE, same"),
    ("Full-stack engineer", 2, 13.4 * L, "AmbitionBox top-10% full-stack Rs 13.4 L"),
    ("Product designer", 0.5, 15.0 * L, "AmbitionBox average Rs 15 L"),
    ("Inside sales, research and outreach", 1, 4.6 * L, "AmbitionBox average Rs 4.6 L"),
]
OTHER_FIXED = {
    # ESTIMATE from AWS list prices: 2 x t4g.medium ($0.034/h), RDS db.t4g.medium Multi-AZ
    # (2 x $0.065/h), backups, monitoring; +20% for Mumbai region and headroom
    "infrastructure base": ((2 * 0.034 + 2 * 0.065) * 730 + 50) * 1.2 * USD_INR,
    # ESTIMATE: workspace email, code hosting, design, CRM, monitoring for about 6 people
    "software tools": 30_000,
    # channel plan cap: about Rs 1,50,000 per quarter for the paid layer
    "sales and marketing (paid layer)": 150_000 / 3,
    # ESTIMATE: events, travel to firms in Mumbai, Delhi NCR, Bengaluru
    "travel for sales and onboarding": 25_000,
    # ESTIMATE: chartered accountant for GST, TDS and ROC filings; contract templates;
    # no security certification is claimed or budgeted
    "accounting, legal and compliance": 25_000,
    # ESTIMATE: 4 co-working seats
    "office (co-working)": 32_000,
}


def fixed_monthly():
    people = {f"{r} ({fte} FTE)": fte * ctc * EMPLOYER_LOADING / 12 for r, fte, ctc, _ in PEOPLE}
    return people, OTHER_FIXED


SEGMENT_SEATS = (18_000, 48_000)  # segment.md guess: 150 to 400 firms x about 120 professionals
CANDIDATES = (149, 199, 249, 299)


def print_costs_and_breakeven():
    print("\n== 3. Cost to serve per seat per month (at the 150-person reference firm) ==")
    print(f"  CS hourly cost Rs {CS_HOURLY:,.0f}")
    for price in (199,):
        parts = variable_cost_per_seat(price)
        for k, x in parts.items():
            print(f"  {k:40s} Rs {x:6.2f}")
        print(f"  {'total at price Rs ' + str(price):40s} Rs {sum(parts.values()):6.2f}")
    for n in (40, REF_FIRM, 400):
        var = sum(variable_cost_per_seat(199, n).values())
        print(f"  margin floor at {TARGET_GM:.0%} gross margin, {n:3d}-person firm: Rs {floor_price(n):,.0f};"
              f" gross margin at Rs 199: {(199 - var) / 199:.1%}")

    print("\n== 4. Fixed cost per month ==")
    people, other = fixed_monthly()
    for k, x in {**people, **other}.items():
        print(f"  {k:45s} Rs {x:>9,.0f}")
    fixed = sum(people.values()) + sum(other.values())
    print(f"  {'TOTAL':45s} Rs {fixed:>9,.0f}   (people Rs {sum(people.values()):,.0f})")

    print("\n== 5. Price candidates (150-person firm) ==")
    mid = value_per_seat("mid")["total_month"]
    low = value_per_seat("low")["total_month"]
    for p in CANDIDATES:
        var = sum(variable_cost_per_seat(p).values())
        contrib = p - var
        gm = contrib / p
        seats = fixed / contrib
        firms = seats / REF_FIRM
        pen = (seats / SEGMENT_SEATS[1], seats / SEGMENT_SEATS[0])
        print(f"  Rs {p}: variable Rs {var:5.1f}, contribution Rs {contrib:5.1f}, GM {gm:.1%}, "
              f"share of mid value {p / mid:.1%}, low-case value minus price Rs {low - p:+.0f}, "
              f"break-even {seats:,.0f} seats = {firms:.0f} firms of 150, "
              f"{pen[0]:.0%} to {pen[1]:.0%} of segment seats")
    mid_exit = value_per_seat("mid")["exit_cost"]
    for p in (149, 199):
        bill = p * REF_FIRM * 12
        print(f"  Rs {p} at {REF_FIRM} seats: Rs {bill:,} a year plus GST = {bill / mid_exit:.2f} mid-case exits;"
              f" pays for itself if it prevents one exit every {mid_exit / bill:.1f} years")
    print(f"  Rs 199 vs cheapest global like-for-like module Rs {inr(7, 'EUR'):,.0f}: {199 / inr(7, 'EUR'):.0%};"
          f" vs PerformYard low end Rs {inr(5, 'USD'):,.0f}: {199 / inr(5, 'USD'):.0%};"
          f" vs Keka Growth at {REF_FIRM}: {199 / keka_growth_per_seat(REF_FIRM):.0%}")
    return fixed


# == 6. pilot ==
PRICE = 199  # recommended list price, see price_and_pilot.md
PILOT_WEEKS = 12  # 6 fortnightly cycles
PILOT_MAX_SEATS = 40
# ESTIMATE: extra hours for a pilot beyond normal onboarding: success test agreed in writing (2),
# mid-pilot check (2), scorecard report and review meeting (6)
PILOT_EXTRA_HOURS = 10


def print_pilot(fixed):
    print("\n== 6. Pilot ==")
    months = PILOT_WEEKS * 7 / 30.4
    for seats in (25, PILOT_MAX_SEATS):
        var = sum(v for k, v in variable_cost_per_seat(PRICE, seats).items()
                  if not k.startswith("onboarding"))
        cost = (ONBOARDING_HOURS + PILOT_EXTRA_HOURS) * CS_HOURLY + var * seats * months
        at_list = PRICE * seats * months
        print(f"  {seats} seats, {PILOT_WEEKS} weeks ({months:.2f} months): cost to serve Rs {cost:,.0f}, "
              f"list price for same seats and time Rs {at_list:,.0f}")
    fee = 25_000
    print(f"  Proposed fee Rs {fee:,}: per seat-month at 40 seats Rs {fee / (40 * months):,.0f}, "
          f"at 25 seats Rs {fee / (25 * months):,.0f}")
    print(f"  Fee as credit against a first annual bill at 150 seats: "
          f"{fee / (PRICE * REF_FIRM * 12):.1%} of Rs {PRICE * REF_FIRM * 12:,}")
    # time check: 6 cycles before an April calibration round
    import datetime as dt
    april = dt.date(2027, 4, 1)
    start = april - dt.timedelta(weeks=PILOT_WEEKS)
    today = dt.date(2026, 11, 24)
    print(f"  Latest start for {PILOT_WEEKS // 2} cycles before {april}: {start} "
          f"({(start - today).days} days after {today})")

    print("\n== 7. Price lock for early firms ==")
    for n_firms, rise in ((10, 50), (25, 50), (10, 100)):
        cost = n_firms * REF_FIRM * rise * 12
        print(f"  {n_firms} firms of {REF_FIRM} locked at Rs {PRICE}, if list rises by Rs {rise}: "
              f"Rs {cost:,.0f} a year of forgone revenue")
    seats = fixed / (PRICE - sum(variable_cost_per_seat(PRICE).values()))
    print(f"  Break-even needs {seats / REF_FIRM:.0f} firms of {REF_FIRM}; 10 locked firms = "
          f"{10 / (seats / REF_FIRM):.0%}, 25 = {25 / (seats / REF_FIRM):.0%}")

    print("\n== 8. Months to break-even (ESTIMATE ramp) ==")
    contrib = PRICE - sum(variable_cost_per_seat(PRICE).values())
    firms = fixed / (contrib * REF_FIRM)
    cs_hours = firms * ONBOARDING_HOURS + firms * REF_FIRM * 0.05 * 20 / 60 * 12
    print(f"  Customer success hours a year at break-even: {cs_hours:,.0f} h = {cs_hours / 2000:.2f} FTE"
          f" (paid as variable cost at Rs {CS_HOURLY:,.0f}/h)")
    # run-rate break-even, not cash payback; ignores churn and price rises
    # start: 3 to 5 pilots before April (deliverable map), converting at the 50% threshold
    # in validation_plan.md; then ESTIMATED new firms a month
    for pilots in (3, 5):
        start_firms = pilots * 0.5
        for adds in (1, 2, 3):
            months = max(0.0, (firms - start_firms) / adds)
            print(f"  {pilots} pilots x 50% = {start_firms:.1f} firms, then {adds} new firms a month: "
                  f"run-rate break-even after about {months:.0f} months")


if __name__ == "__main__":
    print_value()
    print_competitors()
    fixed = print_costs_and_breakeven()
    print_pilot(fixed)
