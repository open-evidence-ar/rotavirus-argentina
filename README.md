# Rotavirus Argentina — Análisis de Riesgo-Beneficio por Nivel Socioeconómico

> Estudio descriptivo con trazabilidad de evidencia sobre la asimetría riesgo-beneficio de la vacunación universal contra rotavirus (Rotarix®) en Argentina, desagregada por nivel socioeconómico · **v0.3.0**

## Informe completo

**[Leer informe publicado](https://open-evidence-ar.github.io/rotavirus-argentina)** · [Descargar (.zip)](https://open-evidence-ar.github.io/rotavirus-argentina/archive.zip)

## Hallazgos clave

| Indicador | Pobre (NOA/NEA) | Promedio nacional | Medio-alto (GBA) |
|---|---|---|---|
| Riesgo de muerte por RV (1er año) | ~1 en 10.000–15.000 | ~1 en 23.000–39.000 | ~1 en 100.000+ |
| Riesgo atribuible de IS post-vacuna | ~1 en 18.000–33.000 | ~1 en 18.000–33.000 | ~1 en 18.000–33.000 |
| Riesgo de cirugía inducida | ~1 en 33.000–63.000 | ~1 en 33.000–63.000 | ~1 en 33.000–63.000 |
| **Balance neto por 100.000 vacunados** | **+4 a +8 vidas salvadas** | Marginal | **−0,6 a −2 cirugías en exceso** |

Para niños de bajos recursos en provincias del norte, la vacunación salva vidas: el riesgo de muerte por la enfermedad supera claramente al riesgo de intususcepción atribuible. Para niños sanos de nivel socioeconómico medio-alto con acceso inmediato a atención pediátrica, el balance individual poblacional se invierte — el riesgo de cirugía inducida excede al riesgo de muerte por la enfermedad. **El estudio documenta ambas asimetrías con trazabilidad de fuentes y propone que el debate público se base en datos, no en consensos administrativos**.

## Lo que este estudio demuestra

1. **El balance riesgo-beneficio varía por población** — favorable en NOA/NEA, desfavorable en GBA medio-alto.
2. **La mortalidad por rotavirus ya estaba estructuralmente reducida antes de la vacuna** —acceso a SRO/TRO y pediatría explican reducción histórica de 3–14× (Munos 2010; Troeger 2018).
3. **Los datos post-vacunación no pueden atribuirse exclusivamente a la vacuna** — García Martí 2022 (GSK) no controla por SRO/saneamiento/reemplazo de cepas; declara mortalidad pendiente de "estudios futuros" 10 años después.
4. **La paradoja de equidad es real** — los niños que más necesitan la vacuna son los que menos la reciben; los que menos la necesitan son los que más la reciben.
5. **No existe consentimiento informado real** — los padres reciben la vacuna sin conocer el balance cuantitativo de su contexto.
6. **La ausencia de datos estratificados por SES no es accidental** — es una omisión sistemática con claros indicadores de negligencia institucional y sesgo político a favor de la vacunación universal, no por evidencia.

> La conclusión racional de los datos no es "no vacunar" ni "vacunar siempre". Es **informar antes de decidir**. La ausencia de consentimiento informado en una población donde el balance es desfavorable no es protección — es omisión.

## Contribuir

Aceptamos nueva evidencia factual, refutaciones y correcciones. Ver [CONTRIBUTING.md](CONTRIBUTING.md).

- [Reportar nueva evidencia](https://github.com/open-evidence-ar/rotavirus-argentina/issues/new?template=evidence-submission.md)
- [Refutar una afirmación](https://github.com/open-evidence-ar/rotavirus-argentina/issues/new?template=rebuttal.md)
- [Reportar error técnico](https://github.com/open-evidence-ar/rotavirus-argentina/issues/new?template=bug-report.md)

## Verificar autoría

- [Clave pública PGP](https://open-evidence-ar.github.io/rotavirus-argentina/public.pem) — RSA 4096, fingerprint `93604ADBAFBDBB56D60B37CA8585492BFC14A09A`
- [Firma detached](https://open-evidence-ar.github.io/rotavirus-argentina/signature) — Generada automáticamente por CI en cada deploy
- [Hash de integridad](https://open-evidence-ar.github.io/rotavirus-argentina/integrity.txt) — SHA256 de `index.html`

La firma PGP detached se regenera automáticamente en cada deploy mediante GitHub Actions (secreto `GPG_PRIVATE_KEY`). La firma firma el archivo `index.html` (no el `integrity.txt`). Para verificar localmente:

    curl -s https://open-evidence-ar.github.io/rotavirus-argentina/signature -o _live_sig.asc
    curl -s https://open-evidence-ar.github.io/rotavirus-argentina/index.html -o _live_index.html
    curl -s https://open-evidence-ar.github.io/rotavirus-argentina/integrity.txt -o _live_integrity.txt
    gpg --verify _live_sig.asc _live_index.html
    # Expected: "Good signature from Rotavirus Argentina Evidence"
    # Then confirm the integrity hash matches the downloaded HTML:
    # SHA256(_live_index.html) must equal the hash in _live_integrity.txt

## Estructura del repositorio

| Directorio / archivo | Contenido |
|---|---|
| `sections/` | Secciones del informe (§0–§12 + anexos A/B + sections estructurales) |
| `_includes/` | Términos de sourcing policy + tags de badges (HTML) |
| `_layouts/default.html` | Plantilla HTML del sitio (Jekyll) |
| `assets/css/style.scss` | Hoja de estilos (badges, calculo-box, nav responsive) |
| `index.md` | Página única que incluye todas las secciones via `{% include_relative %}` |
| `_config.yml` | Configuración Jekyll |
| `llms.txt` | Índice LLM con enlaces raw a todas las secciones ([llmstxt.org](https://llmstxt.org)) |
| `llms-full.txt` | Texto completo del informe concatenado (todas las secciones), generado automáticamente por `_plugins/llms_full_generator.rb` en cada `jekyll build` |
| `validate_ci.py` | Validator de cumplimiento metodológico (20 controles METH) |
| `scripts/validate_calculations.py` | Reproducibilidad numérica (14 casos — bloquea deploy si regresión) |
| `scripts/check_sources.py` | Verificación de accesibilidad de URLs de fuentes (best-effort) |
| `agents/` | 7 archivos de referencia operativa (comandos, setup, gotchas, etc.) |
| `source-metadata.yml` | Metadata de proveniencia metodológica |
| `evidence/` | Manifiesto y referencias (sin PDFs crudos — sólo referencias) |
| `public.pem` / `signature` / `integrity.txt` | Verificación criptográfica (`public.pem` real; `signature` + `integrity.txt` generados por CI) |

## Metodología

Replica la estructura de [Project-Evidence](https://github.com/Project-Evidence/project-evidence.github.io) y el proyecto hermano [State vs Family Evidence](https://github.com/open-evidence-ar/state-vs-family-evidence). Manual operativo completo en [AGENTS.md](AGENTS.md).

Las cuatro categorías de evidencia son:

| Badge | Significado |
|---|---|
| **◎ Observado** | Dato directo de literatura peer-reviewed o de informe oficial |
| **◇ Derivado** | Aritmética reproducible sobre datos observados |
| **△ Supuesto** | Parámetro sin fuente directa, etiquetado con su rango |
| **○ Exploratorio** | Comparación entre unidades débiles para exploración de orden de magnitud |

## Fases del proyecto

- **Fase 1** (completada): recopilación de hallazgos, fuentes y borradores iniciales.
- **Fase 2** (completada): estructura Jekyll completa, secciones divididas, badges de evidencia, validador de metodología, deploy a GitHub Pages.
- **Fase 3** (parcial): firma criptográfica PGP real implementada (clave RSA 4096, CI auto-firma en cada deploy). Pendiente: validación peer-review de todos los números contra fuentes originales, desagregación sub-provincial.

## Posición epistemológica

Este estudio:

- Reconoce que el rotavirus es una enfermedad grave que puede matar niños en Argentina.
- Reconoce que la intususcepción post-vacunación es un evento adverso real con consecuencias quirúrgicas posibles.
- Documenta que la política universal se mantiene por sesgo político a favor de la vacunación universal, no por evidencia estratificada para todas las subpoblaciones — el sistema de vigilancia argentino puede estratificar y elige no hacerlo desde hace 10+ años.
- Propone transparencia, vigilancia activa con desagregación por SES, y debate público con datos reproducibles — no propone el retiro de la vacuna.

La decisión clínica individual corresponde al pediatra y a los padres con información completa. La posición racional del análisis es que cada familia debería poder evaluar el balance riesgo-beneficio de su contexto específico antes de decidir.
