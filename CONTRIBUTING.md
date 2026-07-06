# Contribuciones al informe Rotavirus Argentina

Aceptamos contribuciones que aporten nueva evidencia factual. Toda contribución debe cumplir con nuestra [Política de Fuentes](https://open-evidence-ar.github.io/rotavirus-argentina/#politica-de-fuentes).

## Cómo contribuir

### Reportando nueva evidencia

Abrir un issue usando la plantilla **"Nueva evidencia"** ([crear issue](https://github.com/open-evidence-ar/rotavirus-argentina/issues/new?template=evidence-submission.md)). Incluir:
- URL o DOI de la fuente (peer-reviewed preferido)
- Tipo de evidencia (Observado / Derivado / Supuesto / Refutación)
- Sección del informe afectada
- Cadena de cálculo (si es derivado)

### Refutando una afirmación

Abrir un issue usando la plantilla **"Refutación"** ([crear issue](https://github.com/open-evidence-ar/rotavirus-argentina/issues/new?template=rebuttal.md)). Incluir:
- Cita exacta o número de sección de la afirmación refutada
- Fuente de la evidencia refutatoria
- Impacto en las conclusiones

### Corrigiendo errores

Abrir un issue usando la plantilla **"Error técnico o de método"** ([crear issue](https://github.com/open-evidence-ar/rotavirus-argentina/issues/new?template=bug-report.md)) o enviar un [pull request](https://github.com/open-evidence-ar/rotavirus-argentina/pulls) directo.

### Enviando cambios (Pull Requests)

1. [Fork del repositorio](https://github.com/open-evidence-ar/rotavirus-argentina/fork)
2. Crear una rama descriptiva (`git checkout -b fix/giordano-2001-doi`)
3. Hacer cambios siguiendo el formato del informe
4. Validar localmente: `python validate_ci.py`
5. Commit con mensajes descriptivos
6. Push y abrir [Pull Request](https://github.com/open-evidence-ar/rotavirus-argentina/pulls)

## Política de evidencia

Toda fuente debe ser:

- **Preferentemente peer-reviewed** (con DOI) — primera prioridad de la jerarquía.
- **Oficial** cuando no sea peer-reviewed: organismos estatales (Ministerio de Salud, ANMAT, INDEC, DEIS), position papers de OMS/OPS, prospectos regulatorios (FDA, EMA).
- **Accesible**: URL pública o DOI verificable
- **Fechada**: Año de publicación visible
- **Archivada**: Si es sujeto a cambio, vía [archive.is](https://archive.is) o [web.archive.org](https://web.archive.org)

Para datos derivados, mostrar siempre la cadena de cálculo completa para reproducibilidad. Los supuestos se etiquetan explícitamente y se justifica su rango.

### Jerarquía de fuentes (AGENTS.md §4)

| Prioridad | Tipo de fuente |
|---|---|
| 1 | Peer-reviewed con DOI |
| 2 | Documentos oficiales (Ministerio de Salud, Resolución, norma) |
| 3 | WHO/PAHO position papers |
| 4 | Documentos del fabricante (FDA PI, EMA EPAR — declarando conflicto de interés estructural) |
| 5 | Preprints (claramente etiquetados) |

## Auditoría conocida v0.2.0

La auditoría de DOIs realizada en v0.2.0 (subagentes grounding-1 y grounding-2, julio 2026) detectó 3 fuentes con DOI incorrecto en `index.md`:

- **Fuente #9 (Giordano 2001)**: DOI listado `10.1590/s0036-46652001000400005` apunta a un artículo sobre hepatitis B. Se mantiene la cita con texto completo en scielo.br; DOI correcto pendiente de verificación.
- **Fuente #26 (originally listed as "Lim SS 2018")**: DOI `10.1186/s12916-018-1074-y` corresponde realmente a **Chang AY et al.** 2018. Cita corregida en `12-sources.md`.
- **Fuente #27 (originally listed as "Adebayo 2020")**: DOI `10.1371/journal.pone.0232941` corresponde realmente a **Anderson JD et al.** 2020. Cita corregida en `12-sources.md`.

Cualquier verificación adicional será bienvenida vía PR.

## Anonimato

El informe es publicado por autores anónimos. Las contribuciones individuales pueden mantenerse anónimas salvo solicitud explícita de atribución.

## Contacto

Todos los aportes, correcciones y refutaciones se reciben via [GitHub Issues](https://github.com/open-evidence-ar/rotavirus-argentina/issues) o [Pull Requests](https://github.com/open-evidence-ar/rotavirus-argentina/pulls).

Informe publicado: [open-evidence-ar.github.io/rotavirus-argentina](https://open-evidence-ar.github.io/rotavirus-argentina)

## Licencia

Al enviar aportes, aceptás que los mismos se publiquen bajo la licencia del informe (ver LICENSE, pendiente de definición).
