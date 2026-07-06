# evidence/

Directorio reservado para manifiestos de evidencia y referencias archivadas.

## Política

Per AGENTS.md §3 MUST NOT: **never commit raw PDFs — only references to them**. El contenido de las fuentes citadas en `sections/12-sources.md` no se replica aquí; sólo se referencian vía DOI o URL con enlace de archivo web.

## Uso esperado (Fase 2 y posterior)

| Subdirectorio | Contenido |
|---|---|
| `demographics/` | CSVs derivados de proyecciones INDEC (nacidos vivos por año, distribución provincial) |
| `sources/` | Manifiestos de fuentes citadas (`source-manifest.yml` con número, DOI, URL-canónica, archive-link, estado de verificación) |

## Estado

- Fase 2 (actual): directorio vacío. Las fuentes se referencian directamente desde `sections/12-sources.md` con enlaces archive web.archive.org.
- Fase 3+: este directorio puede ser poblado con datos derivados reproducibles (CSVs de proyecciones populacionales, logs de auditoría de DOIs).
