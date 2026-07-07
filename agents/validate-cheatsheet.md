# Validation Cheatsheet — Reference

This file is loaded on demand from `AGENTS.md §3`. Read when:
- Running validation and need a quick command reference
- A METH check fails and you need to understand what it checks
- Adding a new audit item

---

## Commands

```bash
# Fast gate (no build, source-only) — 20 METH checks
python validate_ci.py

# Numeric reproducibility (14 test cases, must exit 0)
python scripts/validate_calculations.py --verbose

# Source accessibility (best-effort, exit 1 does not block)
python scripts/check_sources.py --timeout 8

# JSON reports
python scripts/validate_calculations.py --json    # -> evidence/calculations-report.json
python scripts/check_sources.py --json            # -> evidence/sources-report.json

# Full build + integrity + signing (manual; CI automates this)
bundle exec jekyll build
sha256sum _site/index.html > _site/integrity.txt   # Linux/WSL
gpg --armor --detach-sign --default-key "Rotavirus Argentina Evidence" _site/index.html  # local-only; CI does this
mv _site/index.html.asc _site/signature
```

---

## All METH checks (idempotent, order-stable)

```
[CHECK] METH-001 Authors / anonymity section
[CHECK] METH-002 Correction policy depth
[CHECK] METH-003 Contribution policy completeness
[CHECK] METH-004 Source archiving (WARN-only)
[CHECK] METH-005 Sourcing policy specificity
[CHECK] METH-006 PGP key (real vs placeholder) — PASS now with real key
[CHECK] METH-007 Integrity hash
[CHECK] METH-008 Signature file
[CHECK] METH-009 Nomenclature / glossary
[CHECK] METH-010 Counter-claims section
[CHECK] METH-011 Revision log
[CHECK] METH-012 Purpose depth (PE-style, 6 findings)
[CHECK] METH-013 Deploy workflow order
[CHECK] METH-014 Mobile nav toggle (JS + .show CSS)
[CHECK] METH-015 Nav anchor links
[CHECK] METH-016 In-page TOC
[CHECK] METH-017 jekyll-scholar (must be ABSENT)
[CHECK] METH-018 Empty directories
[CHECK] METH-019 validate.py path
[CHECK] METH-020 Footer links (4 crypto files)
```

Any new audit item MUST be added as `METH-NNN` and integrated into `validate_ci.py` before being referenced in this file.

---

## Validation flow before commit (manual)

1. `python validate_ci.py` — expect 17 PASS / 3 WARN (PGP placeholders reduced to 0 WARN after v0.3.0)
2. `python scripts/validate_calculations.py --verbose` — expect 14/14 PASS
3. `python scripts/check_sources.py --timeout 8` — best-effort; expect 0-5 unreachable (publishers throttle)
4. `bundle exec jekyll build` — expect `Configuration file: _config.yml` and no errors
5. `git status` — confirm `private-key*` is NOT staged (gitignored)
6. `git diff --stat` — confirm only intended files changed

---

## CI behavior (`.github/workflows/deploy.yml`)

The deploy workflow runs the following IN ORDER:

1. `actions/checkout@v4` — clone repo
2. `ruby/setup-ruby@v1` — Ruby 3.2 + bundler-cache
3. `actions/configure-pages@v5` — Pages setup
4. `actions/setup-python@v5` — Python 3.11
5. **`python scripts/validate_calculations.py --verbose`** — BLOCKS deploy on numeric regression (exit 1)
6. `python scripts/check_sources.py --timeout 8 || true` — best-effort, never blocks
7. `bundle exec jekyll build` — site build
8. `sha256sum _site/index.html > _site/integrity.txt` — integrity
9. **Sign build** (only if `GPG_PRIVATE_KEY` env var present) — re-imports key, signs `_site/index.html`, moves `_site/index.html.asc` to `_site/signature`
10. **Generate archive** — `_site/archive.zip` containing `public.pem`, `integrity.txt`, `signature`, `llms.txt`
11. `actions/upload-pages-artifact@v3` — upload
12. `actions/deploy-pages@v4` — deploy

If step 5 fails (numeric regression), the deploy aborts before Jekyll build (saving compute).

If step 9 fails (signing issue), the deploy aborts (PGP-signed `signature` is mandatory for the methodology).

---

## METH-006: PGP key real vs placeholder

The check inspects `public.pem` and looks for:
- Real key block header: `-----BEGIN PGP PUBLIC KEY BLOCK-----`
- Real key length (not 0 bytes)
- Absence of placeholder text: `PLACEHOLDER`, `TODO`, `replace-me`, `example-only`

Status as of v0.3.0: **PASS** (real PGP key committed, fingerprint `93604ADBAFBDBB56D60B37CA8585492BFC14A09A`).

---

## When a METH check fails

1. Read the specific check name in `validate_ci.py` (search for `meth_006`, `meth_013`, etc.)
2. Identify what the check inspects (file presence, regex, substring match, etc.)
3. Fix the underlying issue (real fix, not bypass)
4. Re-run `python validate_ci.py` — confirm PASS
5. If the check itself is wrong (false positive), update the check in `validate_ci.py` AND document the rationale under the specific METH-NNN entry
