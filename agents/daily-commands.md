# Daily Commands — Reference

This file is loaded on demand from `AGENTS.md §8`. Read when running day-to-day commands on this project.

---

## Environment setup (per session, Windows PowerShell 5.1)

```powershell
# Ruby must be prepended each session (not in PATH by default)
$env:PATH = "C:\Ruby33-x64\bin;C:\Program Files\GnuPG\bin;$env:PATH"

# Python is at the LibreOffice location (Microsoft Store "python.exe" is a stub)
$PY = "C:\Program Files\LibreOffice\program\python.exe"

# Force UTF-8 console output (cp1252 by default on this machine)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

---

## Validation

```bash
# Methodology checks (20 METH controls); fast gate, no Jekyll build
& $PY validate_ci.py

# Numeric calculations (arithmetic reproducibility for sections/*.md); must exit 0
& $PY scripts/validate_calculations.py --verbose

# Source accessibility check (best-effort; exit 1 = dead URLs, not blocking)
& $PY scripts/check_sources.py --timeout 8

# JSON reports (machine-readable)
& $PY scripts/validate_calculations.py --json        # -> evidence/calculations-report.json
& $PY scripts/check_sources.py --json                # -> evidence/sources-report.json
```

---

## Local build + integrity + sign

```bash
# Jekyll build (single-pass)
bundle exec jekyll build

# Generate integrity hash
sha256sum _site/index.html > _site/integrity.txt    # Linux/WSL
# Windows PowerShell:
Get-FileHash _site/index.html -Algorithm SHA256 | Select-Object Hash | Out-File _site/integrity.txt -Encoding ascii

# Sign with PGP (local key must be imported in gpg keyring)
gpg --armor --detach-sign --default-key "Rotavirus Argentina Evidence" _site/index.html
Move-Item _site/index.html.asc _site/signature -Force

# Verify locally (sanity check)
gpg --verify _site/signature _site/index.html
```

---

## Deploy (push to main triggers GitHub Actions)

```bash
# Set remote with PAT (extract from .env, gitignored)
$PAT = (Get-Content .env | Select-String "^GITHUB_PAT=").Line -replace "GITHUB_PAT=", ""
git remote set-url origin "https://open-evidence-ar:$PAT@github.com/open-evidence-ar/rotavirus-argentina.git"

git push origin main

# Restore URL without PAT (security hygiene)
git remote set-url origin "https://github.com/open-evidence-ar/rotavirus-argentina.git"
```

After push, monitor:
- https://github.com/open-evidence-ar/rotavirus-argentina/actions
- Live site: https://open-evidence-ar.github.io/rotavirus-argentina/

---

## Verify the live PGP signature (post-deploy)

```bash
# Fetch the auto-generated detached signature, the signed HTML, and the integrity hash
curl -s https://open-evidence-ar.github.io/rotavirus-argentina/signature -o _live_signature.asc
curl -s https://open-evidence-ar.github.io/rotavirus-argentina/index.html -o _live_index.html
curl -s https://open-evidence-ar.github.io/rotavirus-argentina/integrity.txt -o _live_integrity.txt

# Verify the detached signature against the actual index.html (NOT the hash file)
gpg --verify _live_signature.asc _live_index.html
# Expected output: "Good signature from Rotavirus Argentina Evidence"

# Separately confirm the integrity hash matches the downloaded HTML:
#   SHA256(_live_index.html) must equal the hash in _live_integrity.txt
#   (PowerShell: (Get-FileHash _live_index.html -Algorithm SHA256).Hash.ToLower())
```

---

## Adding a new source

1. Add entry to `sections/12-sources.md` (next sequential number, with DOI/URL and archive URL)
2. Add archive wildcard to `evidence/source-urls.txt` if relevant
3. Cite the source inline in the relevant `sections/*.md` file as `[#NN]` linking to `12-sources.md#source-NN`
4. Run `& $PY scripts/check_sources.py --source NN --verbose` to verify the new URL is alive
5. Run `& $PY validate_ci.py` (METH-004 source archiving check)
6. Update `section-revisions.md` with the addition

---

## Adding a new numeric calculation

1. Add the calculation in `sections/*.md` inside a `{% include_relative %}` block or directly as a `calculo-box` (CSS class)
2. Add a test case to `scripts/validate_calculations.py` covering the new formula (actual vs expected within tolerance)
3. Run `& $PY scripts/validate_calculations.py --verbose` — new case must PASS
4. Update `section-revisions.md` with the addition

---

## Common troubleshooting

- **Jekyll build fails with `webrick` not found**: `bundle add webrick`
- **Python script fails with UnicodeEncodeError (cp1252)**: prepend `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8` to the session, or ensure `sys.stdout.reconfigure(encoding="utf-8")` is at the top of the script (already in both scripts/)
- **gpg: signing failed: No secret key**: the local key was deleted after upload to GitHub Secrets. GitHub Actions does the signing now, not local. Only the public key is local.
- **METH-006 (PGP) shows WARN**: `public.pem` still contains placeholder text. Replace with real exported `gpg --armor --export "Rotavirus Argentina Evidence"` output.

