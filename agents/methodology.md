# Methodology Framework — Reference

This file is loaded on demand from `AGENTS.md §3`. Do not read unless:
- You are adding/modifying METH-NNN audit items
- You need the PE section rendering order
- You need the 20 METH compliance table

---

## PE Structure (sections rendered, in order)

    1. Title + subtitle + version label + integrity + archive links  (index.md header)
    2. Sobre los autores                  (sections/section-authors.md)
    3. Nomenclatura                       (sections/section-nomenclature.md)
    4. Tabla de contenidos (TOC)          (inline in index.md)
    5. §0  Resumen ejecutivo             (sections/00-methodology.md)
    6. §0  Encuadre metodologico         (sections/00-methodology.md)
    7. §0  Politica de fuentes           (sections/00-methodology.md + _includes/sourcing-policy.md)
    8. §0  Politica de correccion        (sections/00-methodology.md)
    9. §0  Politica de contribucion      (sections/00-methodology.md)
    10. §0 Proposito / Que demuestra este analisis (sections/00-methodology.md)
    11. §1 Objetivo                      (sections/01-objective.md)
    12. §2 Intervencion universal Rotarix (sections/02-vaccine-timeline.md)
    13. §3 Carga de enfermedad prevacuna (sections/03-disease-burden.md)
    14. §4 Mortalidad prevacuna observada (sections/04-death-risk.md)
    15. §5 Riesgo de intususcepcion post-vacunal (sections/05-intussusception-risk.md)
    16. §6 Gradiente SES (sections/06-ses-gradient.md)
    17. §7 Analisis riesgo-beneficio por SES (sections/07-risk-benefit.md)
    18. §8 Datos post-vacunacion 2014+   (sections/08-post-vaccination.md)
    19. §9 Costo-beneficio (sections/09-cost-benefit.md)
    20. §10 Paradoja de equidad (sections/10-equity-paradox.md)
    21. §11 Conclusiones (12 items v0.2.2) (sections/11-conclusions.md)
    22. Argumentos contrarios            (sections/section-counterclaims.md)
    23. §12 Fuentes primarias (44 sources) (sections/12-sources.md)
    24. Anexo A — Fact-check (56 rows)    (sections/annex-a-factcheck.md)
    25. Anexo B — Glosario metodologico  (sections/annex-b-glossary.md)
    26. Revisiones                        (sections/section-revisions.md)

Any reordering must mirror PE's original structure. See https://project-evidence.github.io for the reference order.

---

## The 20 METH Compliance Items

When a new iteration is started, the agent MUST keep `METH-001`..`METH-020` GREEN. The status tracker is `validate_ci.py` and re-runs before any commit.

| ID  | Severity  | Item                                      | Status (v0.3.0) |
|-----|-----------|-------------------------------------------|-----------------|
| 001 | High      | Authors section (anon, COI, funding)      | PASS            |
| 002 | Low       | Domain-specific correction triggers       | PASS            |
| 003 | Medium    | Issue/PR templates + CONTRIBUTING.md      | PASS            |
| 004 | High      | Source archiving (archive.org wildcards)  | WARN (script-ready) |
| 005 | Low       | Sourcing policy fleshed out (12 clauses)  | PASS            |
| 006 | Critical  | Real PGP public key                       | PASS            |
| 007 | Critical  | Integrity hash (SHA256 of index.html)     | PASS            |
| 008 | High      | Detached GPG signature of index.html      | PASS (CI-generated) |
| 009 | High      | Nomenclature / glossary section           | PASS            |
| 010 | High      | Counter-claims section                    | PASS            |
| 011 | Medium    | Revision / version history                | PASS            |
| 012 | Low       | Proposito section deep (6 declarative findings) | PASS       |
| 013 | Critical  | Deploy workflow: archive+integrity BEFORE upload | PASS      |
| 014 | Medium    | Mobile nav toggle (JS + .show CSS)        | PASS            |
| 015 | Medium    | All nav anchor links resolve              | PASS            |
| 016 | Low       | In-page TOC present                       | PASS            |
| 017 | Low       | jekyll-scholar not present                | PASS            |
| 018 | Low       | No empty directories                      | PASS            |
| 019 | Low       | validate.py uses relative/dynamic path     | PASS            |
| 020 | Medium    | Footer links all 4 crypto files           | PASS            |

The METH numbering MUST NOT change between sessions. Audit documents reference these IDs.

Any new audit item MUST be added as `METH-NNN` and integrated into `validate_ci.py` before being referenced in this file.

When `validate_ci.py` was last run: 17 PASS / 3 WARN. The remaining WARN items:
- METH-004: source archiving (best-effort, run as `python scripts/check_sources.py`)
- Two others related to PGP (resolved by CI signing on deploy, not local)

After the v0.3.0 commit ships and re-deploys, METH-006 should remain PASS permanently (real key committed).