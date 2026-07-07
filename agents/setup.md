# Setup — Reference

This file is loaded on demand from `AGENTS.md §8`. Read when installing deps, regenerating PGP, or troubleshooting PATH/Python issues.

---

## Dependencies

| Tool       | Version | Verified  | Install                                    |
|------------|---------|-----------|--------------------------------------------|
| Ruby       | 3.3.x   | 3.3.x     | winget install RubyInstallerTeam.RubyWithDevKit.3.3 |
| Bundler    | 4.x     | via bundle | gem install bundler                       |
| Jekyll     | 4.4.x   | 4.4.x     | bundle install                             |
| GnuPG      | 2.5.x   | 2.5.20    | winget install GnuPG.GnuPG                 |
| Python     | 3.8+    | LibreOffice 3.8.10 / CI 3.11 | `C:\Program Files\LibreOffice\program\python.exe` |
| PowerShell | 5.1     | for sign  | bundled with Windows                      |

PATH setup after install (Windows, one-time per session):

    `$env:PATH = "C:\Ruby33-x64\bin;C:\Program Files\GnuPG\bin;$env:PATH"`

For Python: this project uses the LibreOffice Python at `C:\Program Files\LibreOffice\program\python.exe` because the Microsoft Store "python.exe" alias is a stub. The CI workflow uses `actions/setup-python@v5` with Python 3.11.

---

## Ruby gems

`Gemfile` declares only:

    gem "jekyll", "~> 4.3"
    gem "webrick"

`jekyll-scholar` is NOT used (METH-017). Do NOT re-add unless `_bibliography/` and a `scholar` config block exist.

---

## PGP key (Rotavirus Argentina Evidence)

- **Identity:** `Rotavirus Argentina Evidence`
- **Fingerprint:** `93604ADBAFBDBB56D60B37CA8585492BFC14A09A`
- **Public key file:** `public.pem` (committed in repo, ASCII armored)
- **Private key:** stored as GitHub Secret `GPG_PRIVATE_KEY`; NOT in repo; deleted locally after upload
- **Local gpg keyring:** the signing key was deleted from the local keyring after export. GitHub Actions re-imports the secret from the GitHub Secret on every deploy and signs `_site/index.html` automatically.

---

## Re-generate PGP key (only if compromised / lost)

    gpg --batch --passphrase "" --quick-gen-key "Rotavirus Argentina Evidence" default default 0
    gpg --armor --export "Rotavirus Argentina Evidence" --output public.pem
    gpg --armor --export-secret-keys "Rotavirus Argentina Evidence" --output private-key.asc

Then:
1. Update `public.pem` (commit to git)
2. Update the fingerprint reference in this file
3. Upload the new private key to the GitHub Secret `GPG_PRIVATE_KEY` (Settings → Secrets and variables → Actions → New repository secret)
4. Delete `private-key.asc` locally
5. Confirm with `git status` that `private-key.asc` is NOT staged (gitignored via `.gitignore` pattern `private-key*`)

---

## First-time repo clone setup

    git clone https://github.com/open-evidence-ar/rotavirus-argentina.git
    cd rotavirus-argentina

    # Ruby + gems
    `$env:PATH = "C:\Ruby33-x64\bin;$env:PATH"`
    bundle install

    # Verify build
    bundle exec jekyll build

    # Verify methodology
    & "C:\Program Files\LibreOffice\program\python.exe" validate_ci.py

    # Verify numeric calculations
    & "C:\Program Files\LibreOffice\program\python.exe" scripts/validate_calculations.py --verbose

Expected outcome: 17 PASS / 3 WARN on `validate_ci.py` (WARN items are PGP-related, resolved by the workflow on deploy); 14/14 PASS on `validate_calculations.py`.