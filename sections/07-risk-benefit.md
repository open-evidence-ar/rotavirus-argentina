## 7. Riesgo-Beneficio Desagregado por Población
{: #riesgo-beneficio-desagregado}

### 7.1 Modelo por población

Esta sección consolida los riesgos cuantificados en §3 (muerte por RV), §5 (riesgo atribuible de intususcepción) y §6 (gradiente socioeconómico) en una tabla comparativa operativa.

| Población | Riesgo de muerte por RV (1er año) | Riesgo de IS atribuible a vacuna | Balance |
|---|---|---|---|
| **Pobre, norte (NOA/NEA)** | ~1 en 10.000–15.000 <span class="badge badge-derivado">Derivado</span> | ~1 en 18.000–33.000 <span class="badge badge-observado">Observado</span> | **<span class="badge badge-derivado">Favorable a vacunación</span>** |
| **Promedio nacional** | ~1 en 23.000–39.000 <span class="badge badge-derivado">Derivado</span> | ~1 en 18.000–33.000 <span class="badge badge-observado">Observado</span> | **<span class="badge badge-exploratorio">Neutral a marginal</span>** |
| **Medio-alto, Buenos Aires** | ~1 en 330.000–1.000.000 (proxy) <span class="badge badge-supuesto">Supuesto</span> | ~1 en 18.000–33.000 <span class="badge badge-observado">Observado</span> | **<span class="badge badge-derivado">Desfavorable (morbilidad); paridad (muerte)</span>** |

> **Notas sobre las estimaciones de muerte en sub-poblaciones:** no existe un dato nacional publicado que desagregue directamente el riesgo de muerte por RV en GBA niveles medio-altos. La estimación previa "~1 en 100.000+" se infirió aplicando el gradiente de hospitalización 5–15× (Gómez 2002); **revisada a ~1 en 330.000–1.000.000** a partir de proxy regional GBD (Troeger 2018): Argentina nacional ≈0,91/100k <5, región centro+sud ≈0,8% de muertes U5 por diarrea vs 2,1% en el norte (Degiuseppe 2013), y Chile/Uruguay (proxy alto-SES) ≈0,2/100k. Es una **estimación exploratoria** etiquetada <span class="badge badge-supuesto">Supuesto</span>; el valor directo es desconocido.

### 7.2 Razón beneficio-riesgo por 100.000 niños vacunados

> **Convención de denominador:** todas las tasas se expresan por 100.000 *niños vacunados* (curso completo de 2 dosis de Rotarix®). El exceso de intususcepción (IS) atribuible a la vacuna se concentra en los primeros 1–7 días tras la **dosis 1**; la dosis 2 añade exceso despreciable. Las figuras de exceso citadas (Desai 2012; Patel 2011) ya son *por receptor*, no por dosis, por lo que no se cuenta dos veces.

<div class="calculo-box">
<strong>Población pobre (norte):</strong>
  Muertes evitadas ≈ 7–10 por 100.000  (riesgo ~1 en 10.000–15.000)
  IS atribuibles = 3–5,6
  Cirugías inducidas (~90% de IS, LATAM) = 2,5–5
  IS fatales (CFR Américas 0,2–0,6%; Bines 2019) = ~0,03–0,1
  <strong>Razón muertes-evitadas : muertes-por-IS ≈ 70–300 : 1 (favorable)</strong>

<strong>Población medio-alto (Buenos Aires):</strong>
  Muertes evitadas ≈ 0,1–0,3 por 100.000  (riesgo ~1 en 330.000–1.000.000; Supuesto, proxy regional GBD / Troeger 2018)
  IS atribuables = 3–5,6
  Cirugías inducidas = 2,5–5
  IS fatales = ~0,03–0,1
  <strong>Razón muertes-evitadas : muertes-por-IS ≈ 1–3 : 1 (cerca de la paridad en muerte)</strong>
</div>

#### 7.2.1 — Población pobre (norte)

| | Muertes evitadas | IS atribuibles | Cirugías inducidas | IS fatales | Razón muerte:muerte |
|---|---|---|---|---|---|
| Por 100.000 | ~7–10 | ~3–5,6 | ~2,5–5 | ~0,03–0,28 | **~25–330 : 1 (favorable)** |

#### 7.2.2 — Población medio-alto (Buenos Aires)

| | Muertes evitadas | IS atribuibles | Cirugías inducidas | IS fatales | Razón muerte:muerte |
|---|---|---|---|---|---|
| Por 100.000 | ~0,1–0,3 | ~3–5,6 | ~2,5–5 | ~0,03–0,28 | **~0,4–10 : 1 (paridad a favorable)** |

> **Por qué no se restan cirugías de muertes:** restar episodios quirúrgicos (mayormente no fatales: 95–99% de recuperación, CFR 1–5% LATAM) de muertes evitadas mezcla unidades de gravedad distinta. Ningún análisis publicado de riesgo-beneficio de rotavirus (OMS/GACVS, Desai 2012, Clark 2019, ACIP) usa esa sustracción aritmética. El cuadro superior compara **muerte contra muerte**; el apartado 7.2.3 pondera la morbilidad.

#### 7.2.3 — Ponderación por morbilidad (DALY)

En términos de años de vida ajustados por discapacidad (DALY), que sí ponderan la morbilidad quirúrgica, el balance para GBA es **desfavorable**: las cirugías inducidas (2,5–5 por 100.000) superan largamente las muertes evitadas (0,1–0,3 por 100.000). La conclusión "desfavorable para GBA" se sostiene por la vía de la morbilidad, no por una sustracción muerte-cirugía. Para el norte, tanto la razón muerte:muerte como la morbilidad son favorables.

#### 7.2.4 — Análisis de sensibilidad y escenarios (GBA medio-alto)

> **Incertidumbre estructural:** no existe en ningún país una fuente publicada que estratifique la mortalidad por rotavirus por SES dentro de una región urbana (Degiuseppe 2013 estratifica por provincia, no intranurbano). El parámetro dominante — la tasa de muerte evitada en GBA — es **fundamentalmente incalculable** desde datos publicados; se presenta como escenario, no como estimación.

**Parámetros (Low / Base / High):**

| Parámetro | Low | Base | High | Fuente |
|---|---|---|---|---|
| Muerte por RV en GBA (/100k) | 0,05 | 0,15 | 0,9 | Proxy GBD (Troeger 2018) + Degiuseppe 2013 |
| Exceso IS (/100k) | 1,5 | 3,5 | 5,6 | Patel 2011 (LATAM) / OMS (cota sup.) |
| CFR de IS (%) | 1 | 3 | 5 | Patel 2011 (México 1%, Brasil 5%) |
| Fracción quirúrgica IS (%) | 85 | 90 | 95 | Patel 2011 (LATAM) |

**Razón muerte:muerte resultante (GBA), escenarios:**

| Escenario | Muerte evitada | IS fatal | Razón |
|---|---|---|---|
| Pesimista (muerte baja + IS alto) | 0,05 | 0,28 | **0,2 : 1 (desfavorable en muerte)** |
| Central | 0,15 | 0,10 | **1,5 : 1 (paridad)** |
| Optimista (muerte alta + IS bajo) | 0,9 | 0,03 | **30 : 1 (favorable)** |

El rango plausible completo de la razón muerte:muerte para GBA abarca **~0,2 : 1 a ~30 : 1**. La conclusión "desfavorable para GBA" se sostiene de forma robusta por la vía de la **morbilidad (DALY)**: las cirugías inducidas (2,5–5/100k) superan a las muertes evitadas (0,05–0,9/100k) en todos los escenarios. Sólo en el extremo pesimista de muerte evitada la razón cae por debajo de 1 en términos de muerte (ver §7.3).

### 7.3 Implicancia cuantitativa

- En la **población del norte**, la vacunación previene ~7–10 muertes por cada 100.000 niños vacunados, frente a ~0,03–0,1 muertes por IS inducida: razón favorable de ~70–300 : 1.
- En la **población medio-alta urbana**, la vacunación previene ~0,1–0,3 muertes por 100.000, frente a ~0,03–0,1 muertes por IS inducida: la razón muerte-a-muerte es **cercana a la paridad (~1–3 : 1)**.
- En **morbilidad** (DALY), el balance para GBA es **desfavorable**: las cirugías inducidas (2,5–5 por 100.000) superan las muertes evitadas (0,1–0,3 por 100.000).
- La asimetría persiste y es de orden de magnitud: el riesgo de muerte por RV en el norte es ~30–100× el de GBA; la razón beneficio-riesgo difiere en ~2 órdenes de magnitud entre subpoblaciones.

### 7.4 Implicancia poblacional nacional

Aplicando la distribución aproximada:
- ~25–30% de la cohorte nacional en situación de pobreza estructural.
- ~20–25% de la cohorte nacional en situación de nivel socioeconómico medio-alto con acceso inmediato.
- ~45–55% en situaciones intermedias.

>Hipótesis operativa (no establecida como conclusión): en la población medio-alta urbana de Argentina, que representa ~170.000 nacidos vivos por año, el balance anual estimado sería **~0,3 muertes evitadas vs. ~2,5–5 cirugías inducidas** (y ~0,03–0,1 muertes por IS inducida). Para la población pobre, el balance salvaría **~50–80 vidas/año** (§7.2.1) frente a ~1–2 muertes por IS inducida.

<small>Las estimaciones por sub-población son **derivadas** y **exploratorias**; no provienen de una fuente individual publicada de "riesgo de muerte por RV en GBA medio-alto". Se basan en aplicar gradientes publicados a cotas observadas. Ver [Anexo B](#anexo-b--glosario) para notación de badges.</small>
