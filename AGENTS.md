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
**Version:** 0.2.0 (Fase 2 — estructura Jekyll completa; Fase 3 pendiente para firma PGP)

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

## 6. Phase 2 — In Progress (v0.2.0)

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

## 7. Phase 3 — Pending (post v0.2.0 deploy)

- [ ] Generate real GPG keypair
- [ ] Replace `public.pem` / `signature` / `integrity.txt` placeholders with real signed artifacts
- [ ] Configure `secrets.GPG_PRIVATE_KEY` on GitHub Actions
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
| `public.pem` / `signature` / `integrity.txt` | Verificación criptográfica (placeholders Fase 2; reales Fase 3) |
| `.github/workflows/deploy.yml` | CI: build Jekyll + firmar PGP + cargar GitHub Pages |
| `.github/ISSUE_TEMPLATE/*.md` | Templates para evidencia / refutación / bug-report |
| `README.md` | Resumen público del proyecto |
| `CONTRIBUTING.md` | Guía de contribución + política de fuentes |

---

## 9. Authorship

This analysis was conducted by tracing published peer-reviewed literature and official vaccine regulatory documents. No original data was collected. All calculations are derived from published estimates applied to Argentine demographic data.

---

## 10. Ethics Note

This study describes statistical asymmetries in risk-benefit across populations. It does not:
- Tell parents not to vaccinate
- Accuse institutions of malpractice
- Deny that rotavirus is a serious disease

It does:
- Present published data honestly
- Acknowledge that risk-benefit varies by population
- Call for transparent, stratified vaccination policy
