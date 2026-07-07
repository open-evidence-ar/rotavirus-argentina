# Script Catalog — Reference

This file is loaded on demand from `AGENTS.md §8`. Read when adding, modifying, or running scripts in the `scripts/` directory or the root `validate_ci.py`.

---

## Root: validate_ci.py

**Purpose:** 20 METH methodology compliance checks (METH-001 through METH-020).
**Type:** Python 3.x, no external dependencies (stdlib only).
**Run:** `python validate_ci.py`
**Exit codes:**
- 0 = all checks PASS (some WARN allowed)
- 1 = at least one check FAIL
**Output:** stdout, table format with `[CHECK]`, `[PASS]`, `[FAIL]`, `[WARN]` markers.
**When to run:** before every commit. CI does NOT run this script (CI runs the build + numeric validation + source checks).

Checks covered:
- METH-001: Authors / anonymity section presence
- METH-002: Correction policy depth
- METH-003: Contribution policy completeness (CONTRIBUTING.md)
- METH-004: Source archiving (WARN-only; archive.org wildcard presence)
- METH-005: Sourcing policy specificity (12 clauses)
- METH-006: PGP public key real vs placeholder (PASS now with real key)
- METH-007: Integrity hash presence
- METH-008: Signature file presence
- METH-009: Nomenclature / glossary section
- METH-010: Counter-claims section
- METH-011: Revision log (section-revisions.md)
- METH-012: Purpose depth (PE-style, 6 declarative findings)
- METH-013: Deploy workflow order
- METH-014: Mobile nav toggle (JS + CSS)
- METH-015: Nav anchor links resolve
- METH-016: In-page TOC present
- METH-017: jekyll-scholar NOT present (intentional absence)
- METH-018: No empty directories
- METH-019: validate.py uses relative/dynamic path
- METH-020: Footer links all 4 crypto files (public.pem, signature, integrity.txt, archive.zip)

---

## scripts/validate_calculations.py

**Purpose:** Numeric reproducibility of calculations claimed in `sections/*.md`. Each test case specifies a formula, expected value, tolerance, and the section reference. Recomputes from primary inputs and asserts |actual - expected| <= tolerance.
**Type:** Python 3.x, stdlib only (math, re, dataclasses, pathlib).
**Run:** `python scripts/validate_calculations.py --verbose`
**Exit codes:**
- 0 = all cases PASS
- 1 = at least one case mismatch (numeric regression)
- 2 = missing reference (a sections file referenced by a test case is not found)
**Outputs:**
- stdout: per-case `[PASS]`/`[FAIL]` with actual/expected/tolerance
- `evidence/calculations-report.json` when `--json` is passed
**Test cases covered (14 total):**
- §4.1 deaths <1yr per 100k LOW (2.57, tol 0.05)
- §4.1 deaths <1yr per 100k HIGH (4.29, tol 0.05)
- §4.2 Gómez 1998 annualized per 100k (8.0, tol 0.1)
- §5.1 RCT RR 31 days (0.857, tol 0.01)
- §5.1 RCT RR 100 days (0.5625, tol 0.01)
- §5.5 RCT power for 30 to 35/100k difference (0.06, tol 0.05)
- §5.8 surgery attributable per 100k LOW (1.59, tol 0.05)
- §5.8 surgery attributable per 100k HIGH (2.97, tol 0.05)
- §5.8 surgery LOW 1-in-X rate (1.587, tol 0.05)
- §5.8 surgery HIGH 1-in-X rate (3.03, tol 0.05)
- §7.2 balance poor (north) range (4.0-8.4, tol 0.5)
- §7.2 balance medio-alto range (-2.0 - -0.6, tol 0.2)
- §8.3 casos evitados per year annualized (58487, tol 200)
- §6.1 NOA/national mortality ratio (2.625, tol 0.1)
**CI behavior:** runs in `deploy.yml` BEFORE Jekyll build; exit code 1 blocks deploy (numeric regression cannot ship). Exit code 2 also blocks.

---

## scripts/check_sources.py

**Purpose:** Parse `sections/12-sources.md`, extract every source row's primary URL, classify (DOI / generic / archive.org wildcard), and run HEAD/GET requests to verify accessibility within timeout.
**Type:** Python 3.x, stdlib only (urllib, re, json, argparse, dataclasses).
**Run:** `python scripts/check_sources.py [--source NN] [--timeout 8] [--json] [--verbose]`
**Exit codes:**
- 0 = all sources reachable OR all unreachable ones are archive.org wildcards
- 1 = at least one URL is unreachable (publisher 4xx/5xx, timeout, DNS failure)
- 2 = structural error in 12-sources.md (no rows parsed, file missing)
**Behavior notes:**
- archive.org wildcard URLs (containing `/web/2*/`) are classified as always-200; reported as PASS with note
- HTTP 403 is reported as FAIL with note "may be rate-limited or paywalled; verify manually" (publishers like who.int sometimes block non-browser UAs)
- HEAD is the first attempt; falls back to GET on 405/403
**Outputs:**
- stdout table by default; per-source line with `--verbose` or when a source FAILS
- `evidence/sources-report.json` when `--json` is passed (machine-readable)
**CI behavior:** runs in `deploy.yml` BEFORE Jekyll build as best-effort (`|| true`); exit 1 does NOT block deploy. Dead URLs get reported in the Actions log for manual investigation.

---

## Adding a new script

1. Place under `scripts/` if it is build/validation tooling; root if it is structural (like `validate_ci.py`)
2. Add an entry to THIS file (`agents/script-catalog.md`) describing purpose, run command, exit codes, CI behavior
3. If the script should run in CI, update `.github/workflows/deploy.yml` with a new step
4. If the script validates content, add a corresponding METH-NNN check to `validate_ci.py` and update `agents/validate-cheatsheet.md`
5. Consider Windows encoding: add `sys.stdout.reconfigure(encoding="utf-8")` near the top (Python 3.7+) — console is cp1252 here, breaks on section sign, arrow, approx, times, etc.
