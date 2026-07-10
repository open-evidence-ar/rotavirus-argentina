## Anexo B — Glosario de denominadores y notación de badges
{: #anexo-b--glosario}

### B.1 — Notación de badges (taxonomía de evidencia)

| Badge | Categoría | Significado |
|---|---|---|
| <span class="badge badge-observado">◎ Observado</span> | Observado | Dato directo de literatura revisada por pares (peer-reviewed, con DOI) o de un informe oficial publicado (resolución ministerial, position paper OMS, prospecto regulatorio FDA/EMA). |
| <span class="badge badge-derivado">◇ Derivado</span> | Derivado | Aritmética reproducible sobre datos observados. La cadena de cálculo está reproducida en el cuerpo del informe. La reproducción es independiente del lector: dados los números observados, el resultado es determinista. |
| <span class="badge badge-supuesto">△ Supuesto</span> | Supuesto | Parámetro sin fuente directa verificable, etiquetado con su rango de incertidumbre. Se distingue explícitamente del dato observado; no se presenta como hecho. Ejemplo: "Riesgo medio-alto GBA = ~1 en 330.000–1.000.000 (proxy)" se infiere aplicando gradientes publicados (GBD/Troeger 2018 + Degiuseppe 2013) pero no se observa directamente en una fuente Argentina publicada. |
| <span class="badge badge-exploratorio">○ Exploratorio</span> | Exploratorio | Comparación entre unidades débiles para exploración de órdenes de magnitud. Útil para motivar hipótesis pero no para establecer afirmaciones. El balance neto poblacional medio-alto en Argentina se aproxima con elementos exploratorios (gradientes imported comparados con EVAS en México y EE.UU.). |

### B.2 — Denominadores de riesgo de intususcepción (IS)

| Pregunta | Numerador | Denominador | Resultado típico |
|---|---|---|---|
| ¿Existe aumento de IS en vacunados vs no vacunados? | 6 (Rotarix) u 7 (placebo) | 63.225 lactantes (RCT pre-licencia) | NO (RR 0,85, sin aumento significativo) |
| ¿Exceso IS post-comercialización México? | ~45 excesos | 1,5 millones vacunados | ~3-4 / 100.000 (1 en 30.000) |
| ¿Exceso IS post-comercialización EE.UU.? | ~5,3 / 100.000 | Vigilancia PRISM/VSD | 5,3 / 100.000 (1 en 19.000) |
| ¿Exceso IS promedio OMS global? | — | — | 5,6 / 100.000 (1 en 18.000) |
| ¿Exceso IS mínimo (Canadá)? | 0,9 / 100.000 | — | 1 en 111.000 |
| ¿Riesgo cirugía por IS atribuible a vacuna? | ~90% de IS (LATAM, [Patel 2011](https://doi.org/10.1056/NEJMoa1012952)) | Aplicado a exceso IS | 2,5–5 / 100.000 (1 en 20.000–37.000) |

### B.3 — Denominadores de riesgo de muerte por rotavirus

| Pregunta | Numerador | Denominador | Resultado típico | Badge |
|---|---|---|---|---|
| ¿Riesgo nacional anual de muerte por RV <5? | 30–50 | ~700.000 nacidos vivos × 5 cohortes activas | ~1–3 / 100.000/año | ◎ Observado (numerador), ◇ Derivado (riesgo) |
| ¿Riesgo estimado en <1 año (nacional)? | 18–30 (60% de <5) | 700.000 | 2,6–4,3 / 100.000 (1 en 23.000–39.000) | ◇ Derivado |
| ¿Riesgo anualizado 0–3 años (Gómez 1998)? | — | 4.169 (riesgo acumulado) | ~8 / 100.000/año (1 en 12.500) | ◎ Observado original (Gómez), ◇ Derivado anualización |
| ¿Riesgo estimado muerte por RV en NOA/NEA (pobre)? | — | — | ~7–10 / 100.000 (1 en 10.000–15.000) | ◇ Derivado (gradiente aplicado) |
| ¿Riesgo estimado muerte por RV en GBA medio-alto? | — | — | ~0,1–0,3 / 100.000 (1 en 330.000–1.000.000; proxy) | △ Supuesto (gradiente aplicado sobre estimación regional; no observado directamente) |

### B.4 — Términos abreviados del informe

Definidos en [Nomenclatura](#nomenclatura) (al inicio del informe). Incluye: RV, IS, ADD, NOA, NEA, GBA, SIVILA, DEIS, OMS, EMA, Rotarix, RotaTeq, entre otros.

### B.5 — Términos metodológicos (vigilancia de intususcepción y poder estadístico)

| Término | Definición | Relevancia para este informe |
|---|---|---|
| **RCT (Randomized Controlled Trial)** | Ensayo clínico controlado aleatorizado. Gold standard para eficacia, pero limitado para detectar eventos raros post-vacunación por tamaño muestral. | El RCT de Rotarix (N=63.225) tenía <6% de poder para detectar el riesgo IS real post-marketing (~5,6/100.000). Necesitaría ~2,4M por brazo. |
| **Poder estadístico** | Probabilidad de detectar un efecto real si existe. Para el RCT de Rotarix, era ~30× por debajo del efecto RotaShield, no del efecto real. | Explica por qué la "ausencia de señal" del RCT no debe leerse como "evidencia de ausencia de riesgo". |
| **SCCS (Self-Controlled Case Series)** | Diseño donde cada individuo es su propio control: compara incidencia en ventana de riesgo (1-7 días post-vacuna) vs. ventana de control. Estadísticamente potente pero con vulnerabilidades. | Metodología dominante en estudios post-comercialización de IS. Limitaciones: sesgo de vacunado sano, estacionalidad, IS-contraindica-vacunación subsiguiente. |
| **SCRI (Self-Controlled Risk Interval)** | Variante del SCCS con ventana de riesgo pre-especificada y ventana de control fija. | Usado por Yih et al. 2014 en EE.UU. (PRISM). Misma exposición a sesgos que SCCS. |
| **Sesgo de vacunado sano (healthy vaccinee bias)** | Los médicos vacunan cuando el niño está sano → tasa de eventos pre-vacunación artificialmente baja → RI inflado al alza. | Vulnerabilidad documentada en SCCS para IS. Si presente, sobreestima el riesgo atribuible. |
| **Categoría CIOMS "muy raro"** | Convención de frecuencia: <1/10.000. Clasificación, no estimación de riesgo. | El prospecto Rotarix dice "menos de 1 en 10.000 (muy raro)" — esta es la categoría CIOMS derivada del RCT null, NO una estimación del riesgo real post-marketing. |
| **Ventana de riesgo temporal** | Período post-vacunación durante el cual se evalúa riesgo aumentado. Para IS: 1-7 días post-dosis 1 es donde se concentra la señal (RR 5-10×); 31 días la diluye. | El RCT usó 31 días (dilución); los estudios post-marketing detectan señal en 1-7 días. |
| **RotaShield (RRV-TV)** | Primera vacuna contra rotavirus (Wyeth, retirada 1999). Señal IS ~10× más alta que Rotarix/RotaTeq. OR 21,7 para días 3-14 post-dosis 1. | Detuvo el desarrollo de vacunas contra rotavirus por 7 años. Define el "fantasma" que motiva el temor a IS en todas las vacunas posteriores. |

### B.6 — Advertencia general sobre denominadores

Las cifras del informe combinan:
- Numeradores y denominadores publicados en la literatura peer-reviewed.
- Derivaciones aritméticas reproducibles aplicadas a poblaciones argentinas.
- Estimaciones por sub-población aplicando gradientes publicados (con badge △ Supuesto u ○ Exploratorio según corresponda).

Cuando aparece una cota "**~1 en X**" en el texto, debe interpretarse como **estimación de orden de magnitud**, no como valor exacto. Los rangos están libres de falsa precisión: si la cifra es "~1 en 100.000", el rango plausible asociado es 1 en 80.000–150.000 (con incertidumbre de gradiente).

---

*Última revisión: 10 julio 2026. Versión 0.3.0.*
