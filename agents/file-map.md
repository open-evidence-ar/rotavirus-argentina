# File Map — Reference

This file is loaded on demand from `AGENTS.md §8`. Read when editing paths, adding/removing files, or tracing where something lives.

---

## Authored content

    index.md                                  Orquestador — incluye las 19 secciones via include_relative
    sections/00-methodology.md                §0 Resumen + Encuadre + Politicas + Proposito (6 hallazgos declarativos)
    sections/01-objective.md                  §1 Objetivo
    sections/02-vaccine-timeline.md           §2 Marco temporal del programa de vacunacion
    sections/03-disease-burden.md             §3 Carga de enfermedad pre-vacunacion (2009-2014)
    sections/04-death-risk.md                 §4 Calculo del riesgo absoluto de muerte por rotavirus
    sections/05-intussusception-risk.md       §5 Riesgo intususcepcion (§5.1-5.9 IS metodologia)
    sections/06-ses-gradient.md               §6 Gradiente socioeconomico de la enfermedad
    sections/07-risk-benefit.md               §7 Analisis riesgo-beneficio por SES
    sections/08-post-vaccination.md           §8 Datos post-vacunacion 2014+ (§8.6 atribucion)
    sections/09-cost-benefit.md               §9 Analisis de costo-beneficio
    sections/10-equity-paradox.md             §10 La paradoja de equidad
    sections/11-conclusions.md                §11 Conclusiones (12 items v0.2.2)
    sections/12-sources.md                    §12 Fuentes (44 sources)
    sections/annex-a-factcheck.md             Anexo A Fact-check (56 rows)
    sections/annex-b-glossary.md              Anexo B Glosario metodologico
    sections/section-authors.md               Sobre los autores
    sections/section-nomenclature.md          Nomenclatura
    sections/section-counterclaims.md         Argumentos contrarios
    sections/section-revisions.md             Revisiones

## Templates, layouts, includes

    _config.yml                               Configuracion Jekyll
    _layouts/default.html                     Plantilla HTML (nav responsive, footer PGP)
    _includes/sourcing-policy.md              Politica de fuentes (12 clausulas)
    _includes/tags/calculo.html               Badge: Calculo
    _includes/tags/derivado.html              Badge: Derivado
    _includes/tags/exploratorio.html          Badge: Exploratorio
    _includes/tags/fuente.html                Badge: Fuente
    _includes/tags/nnya.html                  Badge: NNyA
    _includes/tags/observado.html             Badge: Observado
    _includes/tags/ratio.html                 Badge: Ratio
    _includes/tags/supuesto.html              Badge: Supuesto
    assets/css/style.scss                     Hoja de estilos (badges, calculo-box, nav responsive, print)

## Crypto + integrity files (tracked)

    public.pem                                PGP public key REAL (reemplaza placeholder v0.2.x)
    signature                                 PGP detached signature of index.html (CI-generado)
    integrity.txt                             SHA256 (index.html) placeholder (CI-generara al deploy)

## Build + validation

    .github/workflows/deploy.yml              build -> archive -> integrity -> sign -> upload (orden)
    Gemfile                                   jekyll 4.3 + webrick
    Gemfile.lock                              Lockfile de gemas
    validate_ci.py                            20 controles METH (001-020)
    scripts/check_sources.py                  Accesibilidad URLs fuentes (best-effort)
    scripts/validate_calculations.py          Reproducibilidad numerica (14 casos, exit 0 bloquea)

## Agent + meta files

    AGENTS.md                                 Operating manual del proyecto
    llms.txt                                  Indice LLM (enlaces raw)
    README.md                                 Resumen publico
    CONTRIBUTING.md                           Guia de contribucion
    source-metadata.yml                       Metadata de proveniencia metodologica
    .gitignore                                Excluye _site/, .env, private-key*, *.zip
    agents/daily-commands.md                  Comandos diarios
    agents/setup.md                           Dependencias + PGP
    agents/gotchas.md                         Problemas comunes
    agents/validate-cheatsheet.md             Cheatsheet METH
    agents/script-catalog.md                  Catalogo de scripts
    agents/file-map.md                        Este archivo

## Evidence

    evidence/README.md                        Manifiestos y referencias (sin PDFs crudos; directorio reservado)