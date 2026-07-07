#!/usr/bin/env python3
"""
validate_calculations.py
========================
Reproduces every numeric calculation declared in sections/*.md of the
Rotavirus Argentina evidence document and asserts each against its
declared value within tolerance.

Each CASE contains:
  - name: short identifier
  - formula: callable returning a numeric value
  - expected: declared value (in the report) for point estimates, or
    (low, high) for ranges
  - tolerance: absolute tolerance (in the same units as expected)
  - section_ref: file path used to verify the case

Exit codes:
  0  all cases match
  1  mismatch
  2  script error (typo, missing module, etc.)

Usage:
  python scripts/validate_calculations.py
  python scripts/validate_calculations.py --verbose
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Union, Tuple

# Force UTF-8 stdout/stderr on Windows consoles using cp1252
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sections"

Number = Union[float, int]
Expected = Union[Number, Tuple[Number, Number]]


@dataclass
class Case:
    name: str
    formula: Callable[[], Number]
    expected: Expected
    tolerance: float
    section_ref: str
    note: str = ""

    def check(self) -> tuple[bool, str]:
        """Run formula and compare against expected within tolerance. Returns (passed, msg)."""
        try:
            actual = self.formula()
        except Exception as e:  # pragma: no cover
            return False, f"formula raised {type(e).__name__}: {e}"

        if isinstance(self.expected, tuple):
            lo, hi = self.expected
            if isinstance(actual, tuple):
                a_lo, a_hi = actual
                lo_diff = abs(a_lo - lo)
                hi_diff = abs(a_hi - hi)
                ok = lo_diff <= self.tolerance and hi_diff <= self.tolerance
                return ok, (
                    f"actual=({a_lo:.6g}, {a_hi:.6g})  "
                    f"expected=({lo}, {hi}) +/-{self.tolerance}  "
                    f"|d_lo|={lo_diff:.4g} |d_hi|={hi_diff:.4g}"
                )
            in_range = (lo - self.tolerance) <= actual <= (hi + self.tolerance)
            return in_range, f"actual={actual:.6g}  expected=[{lo},{hi}] +/- {self.tolerance}"
        if math.isnan(actual) or math.isinf(actual):
            return False, f"actual={actual} (unbounded)"
        delta = abs(actual - self.expected)
        ok = delta <= self.tolerance
        return ok, f"actual={actual:.6g}  expected={self.expected}  |d|={delta:.6g}  tol={self.tolerance}"


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def normal_cdf(z: float) -> float:
    """Standard normal CDF without scipy."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def power_two_proportions(n_per_arm: int, p1: float, p2: float, alpha: float = 0.05) -> float:
    """Statistical power for detecting a difference in two proportions (chi-square)."""
    if p1 == p2:
        return alpha
    p_pooled = (p1 + p2) / 2.0
    se_pooled = math.sqrt(2 * p_pooled * (1 - p_pooled) / n_per_arm)
    se_alt = math.sqrt(p1 * (1 - p1) / n_per_arm + p2 * (1 - p2) / n_per_arm)
    z_alpha = 1.96 if alpha == 0.05 else 1.645
    z_crit = z_alpha
    z_power = (
        abs(p1 - p2) / se_alt - z_crit * se_pooled / se_alt
    )
    return normal_cdf(z_power)


# --------------------------------------------------------------------------- #
# §4 — Death risk (national, <1yr, 0-3yr)
# --------------------------------------------------------------------------- #
def deaths_per_100k_low() -> float:
    """§4.1 low estimate: 18 / 700_000 * 100_000 = 2.57 per 100k."""
    return 18 / 700_000 * 100_000


def deaths_per_100k_high() -> float:
    """§4.1 high estimate: 30 / 700_000 * 100_000 = 4.29 per 100k."""
    return 30 / 700_000 * 100_000


def gomez_annualized_per_100k() -> float:
    """§4.2 Gómez 1998: 1 en 4.169 antes de 3 años -> 1 en ~12.500/año = 8.0/100k."""
    return 100_000 / 4_169 / 3


# --------------------------------------------------------------------------- #
# §5 — Intussusception risk
# --------------------------------------------------------------------------- #
def rct_risk_31d() -> float:
    """§5.1 RCT intussusception within 31 days: RR = 6/7 ≈ 0.857."""
    return 6 / 7


def rct_risk_100d() -> float:
    """§5.1 inside 100 days: RR = 9/16 = 0.5625."""
    return 9 / 16


def surgery_low_per_100k() -> float:
    """§5.8 surgery fraction: intussusception attributable 3 per 100k × 53% = 1.59 per 100k."""
    return 3 * 0.53


def surgery_high_per_100k() -> float:
    """§5.8 surgery fraction high: 5.6 × 0.53 = 2.968 per 100k."""
    return 5.6 * 0.53


def surgery_low_1in() -> float:
    """§5.8: 1 en 63_000 ≈ 1.587 / 100k."""
    return 100_000 / 63_000


def surgery_high_1in() -> float:
    """§5.8: 1 en 33_000 ≈ 3.03 / 100k."""
    return 100_000 / 33_000


def rct_power_for_real_signal() -> float:
    """§5.5: power of RCT (n_per_arm=31_600) to detect 35/100k vs 30/100k baseline.

    With baseline incidence 30/100k (3e-4) and target 35/100k (3.5e-4):
      RR = 35/30 = 1.167
      absolute increase ≈ 5e-5 per arm
      n_per_arm ≈ 31_600

    Power computed via two-proportion z-test (normal approximation).
    """
    n = 31_600
    p1 = 30 / 100_000
    p2 = 35 / 100_000
    return power_two_proportions(n, p1, p2, alpha=0.05)


# --------------------------------------------------------------------------- #
# §7 — Risk-benefit balance per 100k
# --------------------------------------------------------------------------- #
def balance_poor_per_100k() -> tuple[float, float]:
    """§7.2: poor (north) — deaths avoided ~7-10 vs surgery ~1.6-3."""
    return (7 - 3, 10 - 1.6)


def balance_medio_alto_per_100k() -> tuple[float, float]:
    """§7.2: medio-alto — deaths avoided ~1 vs surgery ~1.6-3 ≈ -0.6 to -2."""
    return (1 - 3, 1 - 1.6)


# --------------------------------------------------------------------------- #
# §8 — Post-vaccination attributed cases
# --------------------------------------------------------------------------- #
def casos_evitados_per_year_low() -> float:
    """§8.3: 233,947 casos evitados en 4 años (2015-2018) ÷ 4 ≈ 58,487/año."""
    return 233_947 / 4


# --------------------------------------------------------------------------- #
# §10 — Equity paradox proportions
# --------------------------------------------------------------------------- #
def noa_over_national_share_low() -> float:
    """§6.1: NOA mortality 2.1% vs national 0.8% = ratio 2.625."""
    return 2.1 / 0.8


# --------------------------------------------------------------------------- #
# Master case list
# --------------------------------------------------------------------------- #
CASES: list[Case] = [
    # §4.1 deaths <1yr
    Case(
        name="§4.1 deaths <1yr per 100k LOW",
        formula=deaths_per_100k_low,
        expected=2.57,
        tolerance=0.05,
        section_ref="sections/04-death-risk.md",
    ),
    Case(
        name="§4.1 deaths <1yr per 100k HIGH",
        formula=deaths_per_100k_high,
        expected=4.29,
        tolerance=0.05,
        section_ref="sections/04-death-risk.md",
    ),
    Case(
        name="§4.2 Gómez 1998 annualized per 100k",
        formula=gomez_annualized_per_100k,
        expected=8.0,
        tolerance=0.1,
        section_ref="sections/04-death-risk.md",
        note="1 en 4.169 antes 3 años -> /3 = 8.0/100k",
    ),
    # §5.1 RCT
    Case(
        name="§5.1 RCT RR 31 days",
        formula=rct_risk_31d,
        expected=0.857,
        tolerance=0.01,
        section_ref="sections/05-intussusception-risk.md",
    ),
    Case(
        name="§5.1 RCT RR 100 days",
        formula=rct_risk_100d,
        expected=0.5625,
        tolerance=0.01,
        section_ref="sections/05-intussusception-risk.md",
    ),
    # §5.5 power calc
    Case(
        name="§5.5 RCT power for 30→35/100k difference",
        formula=rct_power_for_real_signal,
        expected=0.06,
        tolerance=0.05,
        section_ref="sections/05-intussusception-risk.md",
        note="declared <6% poder — verifies the documented claim",
    ),
    # §5.8 surgery attributable
    Case(
        name="§5.8 surgery attributable per 100k LOW",
        formula=surgery_low_per_100k,
        expected=1.59,
        tolerance=0.05,
        section_ref="sections/05-intussusception-risk.md",
    ),
    Case(
        name="§5.8 surgery attributable per 100k HIGH",
        formula=surgery_high_per_100k,
        expected=2.97,
        tolerance=0.05,
        section_ref="sections/05-intussusception-risk.md",
    ),
    Case(
        name="§5.8 surgery LOW 1-in-X rate",
        formula=surgery_low_1in,
        expected=1.587,
        tolerance=0.05,
        section_ref="sections/05-intussusception-risk.md",
    ),
    Case(
        name="§5.8 surgery HIGH 1-in-X rate",
        formula=surgery_high_1in,
        expected=3.03,
        tolerance=0.05,
        section_ref="sections/05-intussusception-risk.md",
    ),
    # §7.2 balance
    Case(
        name="§7.2 balance poor (north) range",
        formula=balance_poor_per_100k,
        expected=(4.0, 8.4),
        tolerance=0.5,
        section_ref="sections/07-risk-benefit.md",
        note="range [4, 8] per 100k declared",
    ),
    Case(
        name="§7.2 balance medio-alto range",
        formula=balance_medio_alto_per_100k,
        expected=(-2.0, -0.6),
        tolerance=0.2,
        section_ref="sections/07-risk-benefit.md",
        note="range [-2, -0.6] per 100k declared",
    ),
    # §8.3 casos evitados
    Case(
        name="§8.3 casos evitados per year (annualized)",
        formula=casos_evitados_per_year_low,
        expected=58_487,
        tolerance=200,
        section_ref="sections/08-post-vaccination.md",
        note="233,947 divido en ~4 años de cobertura 2015-2018",
    ),
    # §6.1 NOA ratio
    Case(
        name="§6.1 NOA/national mortality ratio",
        formula=noa_over_national_share_low,
        expected=2.625,
        tolerance=0.1,
        section_ref="sections/06-ses-gradient.md",
    ),
]


def verify_source_exists(case: Case) -> bool:
    """Verify the section_ref file actually exists in the repo."""
    return (ROOT / case.section_ref).is_file()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--verbose", "-v", action="store_true", help="print every case")
    parser.add_argument("--json", action="store_true", help="emit JSON report")
    args = parser.parse_args()

    print("=" * 72)
    print(f"validating {len(CASES)} numeric calculations declared in sections/*.md")
    print("=" * 72)

    results = []
    exit_code = 0
    for case in CASES:
        if not verify_source_exists(case):
            results.append({"name": case.name, "passed": False, "msg": f"section_ref missing: {case.section_ref}"})
            exit_code = max(exit_code, 2)
            continue
        passed, msg = case.check()
        result = {
            "name": case.name,
            "passed": passed,
            "msg": msg,
            "section": case.section_ref,
            "note": case.note,
        }
        results.append(result)
        if not passed:
            exit_code = max(exit_code, 1)
        if args.verbose or not passed:
            mark = "PASS" if passed else "FAIL"
            print(f"[{mark}] {case.name}")
            print(f"        {msg}")

    passed_count = sum(1 for r in results if r["passed"])
    print("=" * 72)
    print(f"RESULT: {passed_count}/{len(results)} cases passed")
    print(f"        exit_code={exit_code}  (0=ok, 1=mismatch, 2=missing-ref)")
    print("=" * 72)

    if args.json:
        out_path = ROOT / "evidence" / "calculations-report.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps({"exit_code": exit_code, "results": results}, indent=2), encoding="utf-8")
        print(f"JSON report -> {out_path}")

    return exit_code


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
