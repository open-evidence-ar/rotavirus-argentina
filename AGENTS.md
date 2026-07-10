# AGENTS.md — Rotavirus Argentina

Operating manual for the rotavirus risk-benefit analysis project. Adapted from the parent project [State vs Family Evidence](../state-vs-family-evidence/AGENTS.md); replicates its methodology and architecture.

---

## 1. Project Identity

**Name:** Vacunación contra Rotavirus en Argentina — Análisis de Riesgo-Beneficio por Nivel Socioeconómico
**Parent project:** [State vs Family Evidence](../state-vs-family-evidence/AGENTS.md)
**Deploy:** https://open-evidence-ar.github.io/rotavirus-argentina
**Repo:** https://github.com/open-evidence-ar/rotavirus-argentina
**Methodology source:** [Project-Evidence](https://github.com/Project-Evidence/project-evidence.github.io)
**Language:** Spanish (es)
**Type:** Single-page Jekyll document deployed to GitHub Pages
**Version:** 0.3.0 (Fase 2 completada; Fase 3 parcial — PGP real + scripts de validación)

---

## 2. Purpose

Descriptive study with traceable evidence analyzing the risk-benefit ratio of universal rotavirus vaccination (Rotarix®) in Argentina, disaggregated by socioeconomic level.

### Core thesis

The risk-benefit of rotavirus vaccination is not uniform across populations. For low-SES children in northern provinces, vaccination clearly saves lives. For healthy, well-nourished urban children with immediate access to pediatric care, the attributable risk of intussusception (surgical bowel obstruction) exceeds the risk of death from the disease.

### Methodology inherited from parent project

- Evidence before assertion — every claim traces to a numbered, archived, dated source
- Both harms acknowledged — both disease deaths AND vaccine adverse events are real
- Asymmetry, not accusation — describes scale asymmetries, does not accuse individuals or institutions
- Change trail — every iteration logged
- Local-first review — all changes preview locally before push

---

## 3. Core Rules

### MUST do

1. Every number must cite a specific source with DOI or URL
2. Run `python validate_ci.py` (when created) before any build
3. Update `section-revisions.md` when substantive changes ship
4. Never commit raw PDFs — only references to them

### MUST NOT do

- Make claims without sourcing
- Use absolute language ("vaccines are safe/dangerous") — use conditional language with population context
- Edit source references after publication
- Create empty directories

---

## 4. Source Hierarchy

| Priority | Source type | Example |
|---|---|---|
| 1 | Peer-reviewed studies with DOI | Degiuseppe 2017, García Martí 2022 |
| 2 | Official government documents | Resolución 1027/2014 |
| 3 | WHO/PAHO position papers | WHO 2021 |
| 4 | Vaccine manufacturer documents | Rotarix Prescribing Information |
| 5 | Preprints (clearly labeled) | — |

---

## 5. Phase 1 — Completed

- [x] Create folder structure
- [x] Write initial findings document (`index.md` — monolítico 407 líneas)
- [x] Compile all sources

## 6. Phase 2 — Completed (v0.2.0)

- [x] Create Jekyll structure (config, layouts, includes)
- [x] Split `index.md` monolítico into `sections/*.md` (19 archivos)
- [x] Add evidence data files / sources organization
- [x] Add cálculo-box + intervalo-box + badges (CSS portado del parent)
- [x] Add `validate_ci.py` checks (20 controles METH adaptados)
- [x] GitHub Pages deploy workflow + issue/PR templates
- [x] Source URL discovery + archive web.archive.org wildcards
- [x] Auditoría de DOIs con subagentes (grounding-1, grounding-2)
- [ ] First deploy to GitHub Pages (pending git push)
- [ ] Continuous integration tests confirmed green

## 7. Phase 3 — In Progress (v0.3.0)

- [x] Generate real GPG keypair (RSA 4096, fingerprint `93604ADBAFBDBB56D60B37CA8585492BFC14A09A`)
- [x] Replace `public.pem` placeholder with real public key (`signature` + `integrity.txt` are CI-generated, not committed)
- [x] Configure `secrets.GPG_PRIVATE_KEY` on GitHub Actions
- [x] Numeric validation scripts (`scripts/validate_calculations.py` — 14 cases; `scripts/check_sources.py` — 38 sources)
- [x] `agents/` directory (7 reference files adapted from parent project)
- [ ] Optional: CSV evidence data files (INDEC-derived demographic projections, JS calc boxes for interactive calc-chain demonstration)
- [ ] Validate all numbers against original sources (peer review)
- [ ] Add regional breakdown tables (sub-provincial)

---

## 8. Key Files

| File | Purpose |
|---|---|
| `index.md` | Orquestador — incluye las 19 secciones via `{% include_relative %}` |
| `_config.yml` | Configuración Jekyll |
| `Gemfile` | Ruby dependencies (jekyll + webrick) |
| `_layouts/default.html` | Plantilla HTML del sitio (nav responsive, footer PGP) |
| `_includes/sourcing-policy.md` | Política de fuentes (12 cláusulas jerarquizadas) |
| `_includes/tags/*.html` | 8 badges HTML (Observado / Derivado / Supuesto / Exploratorio / etc.) |
| `sections/` | 19 archivos .md: §00-methodology → §11-conclusions + 3 secciones estructurales + 2 anexos |
| `assets/css/style.scss` | Hoja de estilos (badges, calculo-box, nav responsive, print) |
| `evidence/` | Manifiestos y referencias (sin PDFs crudos — sólo referencias) |
| `AGENTS.md` | Este archivo — operating manual |
| `validate_ci.py` | 20 controles de metodología (METH-001 a METH-020) |
| `source-metadata.yml` | Metadata de proveniencia metodológica (PE + parent project) |
| `llms.txt` | Índice LLM con enlaces raw a todas las secciones |
| `public.pem` / `signature` / `integrity.txt` | Verificación criptográfica (`public.pem` real RSA 4096; `signature` + `integrity.txt` generados por CI en cada deploy, no commiteados) |
| `.github/workflows/deploy.yml` | CI: build Jekyll + firmar PGP + cargar GitHub Pages |
| `.github/ISSUE_TEMPLATE/*.md` | Templates para evidencia / refutación / bug-report |
| `README.md` | Resumen público del proyecto |
| `CONTRIBUTING.md` | Guía de contribución + política de fuentes |

---

## 9. Authorship

This analysis was conducted by tracing published peer-reviewed literature and official vaccine regulatory documents. No original data was collected. All calculations are derived from published estimates applied to Argentine demographic data.

---

## 10. Ethics Note (v0.2.2)

This study describes statistical asymmetries in risk-benefit across populations. Its position is **declarative and evidence-based**, not defensive.

**It documents (as findings, see §00 "Qué demuestra este análisis"):**

- The risk-benefit of rotavirus vaccination varies by population in Argentina.
- Pre-vaccine mortality was already structurally reduced by SRO/TRO + access to pediatric care (Munos 2010); the vaccine was added to a scenario where mortality was already low.
- Post-vaccination data (García Martí 2022, GSK-funded) cannot be attributed solely to the vaccine.
- The equity paradox is real: those who need the vaccine most get it least; those who need it least get it most.
- Informed consent does not exist in Argentina — parents receive the vaccine without knowing the quantitative balance for their context.
- The absence of SES-stratified data is a systematic omission with clear indicators of institutional negligence and political bias toward maintaining the universal vaccination narrative — not by evidence.

**The rational conclusion of the data is not "don't vaccinate" nor "always vaccinate" — it is _inform before deciding_.**

**Limits of this analysis:**

- Does not tell individual parents what to do. Clinical decisions belong with pediatricians.
- Recognizes that rotavirus **is** a serious disease that kills children in Argentina.
- Recognizes that post-vaccination intussusception **is** a real adverse event with potential surgical sequelae.
- Calls for transparency, active surveillance with SES disaggregation, and public debate on reproducible data — does **not** propose withdrawal of the vaccine.

The responsible position is that every family should be able to evaluate the risk-benefit of their specific context before deciding — both harms (death-from-disease AND surgery-from-vaccine) are real, and both should be transparently communicated.
