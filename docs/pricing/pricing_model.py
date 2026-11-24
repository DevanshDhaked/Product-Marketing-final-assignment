"""Sphyr pricing model for Indian management consulting firms (40 to 400 professionals).

Run: python3 docs/pricing/pricing_model.py
Every input carries a source key (see the pricing docs' `sources` frontmatter) or the word
ESTIMATE with its reason. Money is in Indian rupees. L = lakh = 100,000.
"""

L = 100_000
CASES = ("low", "mid", "high")

# ---------------------------------------------------------------- 1. value per seat
VALUE = {
    # annual attrition rate in the firm
    # low: SPI 2025 Table 170, voluntary, 101 to 300 staff (global PS firms)
    # mid: Aon India 2025-26, all industries, 2025
    # high: Aon India 2024-25, professional services, 2024
    "attrition": {"low": 0.069, "mid": 0.162, "high": 0.221},
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
    return {
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
        print(f"  review value / seat / mo     Rs {r['review_month']:,.0f}")
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


# ---------------------------------------------------------------- 2. competitor anchors
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


if __name__ == "__main__":
    print_value()
    print_competitors()
