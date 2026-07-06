# Rotavirus Argentina — Análisis de Riesgo-Beneficio por Nivel Socioeconómico

> Estudio descriptivo con trazabilidad de evidencia sobre la asimetría riesgo-beneficio de la vacunación universal contra rotavirus (Rotarix®) en Argentina, desagregada por nivel socioeconómico · **v0.2.0**

## Informe completo

**[Leer informe publicado](https://open-evidence-ar.github.io/rotavirus-argentina)** · [Descargar (.zip)](https://open-evidence-ar.github.io/rotavirus-argentina/archive.zip)

## Hallazgos clave

| Indicador | Pobre (NOA/NEA) | Promedio nacional | Medio-alto (GBA) |
|---|---|---|---|
| Riesgo de muerte por RV (1er año) | ~1 en 10.000–15.000 | ~1 en 23.000–39.000 | ~1 en 100.000+ |
| Riesgo atribuible de IS post-vacuna | ~1 en 18.000–33.000 | ~1 en 18.000–33.000 | ~1 en 18.000–33.000 |
| Riesgo de cirugía inducida | ~1 en 33.000–63.000 | ~1 en 33.000–63.000 | ~1 en 33.000–63.000 |
| **Balance neto por 100.000 vacunados** | **+4 a +8 vidas salvadas** | Marginal | **−0,6 a −2 cirugías en exceso** |

Para niños de bajos recursos en provincias del norte, la vacunación salva vidas: el riesgo de muerte por la enfermedad supera claramente al riesgo de intususcepción atribuible. Para niños sanos de nivel socioeconómico medio-alto con acceso inmediato a atención pediátrica, el balance individual poblacional se invierte — el riesgo de cirugía inducida excede al riesgo de muerte por la enfermedad.

El programa de vacunación universal se mantiene tanto por razones logísticas y políticas como por beneficios poblacionales agregados. La asimetría de magnitud entre sub-poblaciones justifica debate público transparente, no retiro de la política.

## Contribuir

Aceptamos nueva evidencia factual, refutaciones y correcciones. Ver [CONTRIBUTING.md](CONTRIBUTING.md).

- [Reportar nueva evidencia](https://github.com/open-evidence-ar/rotavirus-argentina/issues/new?template=evidence-submission.md)
- [Refutar una afirmación](https://github.com/open-evidence-ar/rotavirus-argentina/issues/new?template=rebuttal.md)
- [Reportar error técnico](https://github.com/open-evidence-ar/rotavirus-argentina/issues/new?template=bug-report.md)

## Verificar autoría (Fase 3 — pendiente)

- [Clave pública PGP](https://open-evidence-ar.github.io/rotavirus-argentina/public.pem) — Placeholder fase 2
- [Firma detached](https://open-evidence-ar.github.io/rotavirus-argentina/signature) — Placeholder fase 2
- [Hash de integridad](https://open-evidence-ar.github.io/rotavirus-argentina/integrity.txt) — Generado automáticamente por CI

La verificación criptográfica plena (clave GPG real, firma detached válida, hash de integridad firmado) se completa en Fase 3 del proyecto. Hasta entonces, la trazabilidad descansa en el historial de revisiones y en la inmutabilidad de versiones firmadas en git.

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
| `validate_ci.py` | Validator de cumplimiento metodológico (20 controles METH) |
| `source-metadata.yml` | Metadata de proveniencia metodológica |
| `evidence/` | Manifiesto y referencias (sin PDFs crudos — sólo referencias) |
| `public.pem` / `signature` / `integrity.txt` | Verificación criptográfica (placeholders Fase 2) |

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
- **Fase 2** (en curso): estructura Jekyll completa, secciones divididas, badges de evidencia, validador de metodología, deploy a GitHub Pages.
- **Fase 3** (pendiente): firma criptográfica plena (clave GPG real, firma detached, integrity hash firmado).

## Advertencia

Este estudio NO recomienda a padres individuales no vacunar a sus hijos. NO acusa a organismos sanitarios (Ministerio de Salud, ANMAT, sociedades científicas) de mala praxis. NO niega que el rotavirus es una enfermedad grave que mata niños en Argentina. **Describe** una asimetría cuantitativa documentada entre sub-poblaciones y propone debate público informado.

La decisión clínica individual corresponde al pediatra y a los padres con información completa. Las recomendaciones de sociedades científicas deben seguirse mientras no se revise consensualmente la política.
