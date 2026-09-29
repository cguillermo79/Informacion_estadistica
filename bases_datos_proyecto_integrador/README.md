# Proyecto integrador FIRELAB_Loja — Estadística

## Propósito

Cada equipo desarrollará una investigación estadística reproducible sobre un bloque temático del cantón Loja. El objetivo no es describir todas las columnas, sino formular una pregunta concreta, seleccionar las variables que permitan responderla, comprobar la calidad de los datos y sustentar las conclusiones con tablas, gráficos y medidas estadísticas correctamente interpretadas.

El proyecto se construye durante las tres unidades:

1. **Unidad 1 — Formulación:** problema, pregunta, hipótesis u orientación del análisis, objetivos y selección justificada de variables.
2. **Unidad 2 — Metodología y avance:** depuración documentada, análisis exploratorio, tablas y gráficos preliminares.
3. **Unidad 3 — Cierre:** análisis final, interpretación, discusión de limitaciones y conclusiones.

## Base autorizada y alcance

- Fuente: `dataset_maestro_firelab_loja_2019_2025_v1_1_0.csv`.
- SHA-256 de la fuente: `890423faf91207aa271feb9878b1b379e309c156e8e7128af380a5c1afe674b6`.
- Unidad de observación: una **celda espacial de 500 m en un mes**.
- Periodo entregado: enero de 2019 a diciembre de 2024 (72 meses).
- Área de estudio: cantón Loja completo, con 7.997 celdas.
- El año 2025 no está incluido: está reservado como conjunto OOT del proyecto científico.

Las bases son extracciones del dataset maestro. No se recalcularon, imputaron, agregaron ni corrigieron valores. El archivo original debe conservarse sin cambios; toda limpieza o transformación se realizará mediante un script o cuaderno reproducible.

## Asignación de equipos

| Equipo | Tema | Zona | Registros | Celdas | Columnas | Archivo |
|---:|---|---|---:|---:|---:|---|
| 1 | Relieve y accesibilidad | Loja completo | 575.784 | 7.997 | 66 | `equipo_01_relieve_loja_completo/base_estadistica_equipo_01_relieve_loja_completo_2019_2024.csv` |
| 2 | Cobertura vegetal y uso del suelo | Loja completo | 575.784 | 7.997 | 53 | `equipo_02_cobertura_loja_completo/base_estadistica_equipo_02_cobertura_loja_completo_2019_2024.csv` |
| 3 | Clima y condiciones atmosféricas | Loja completo | 575.784 | 7.997 | 57 | `equipo_03_clima_loja_completo/base_estadistica_equipo_03_clima_loja_completo_2019_2024.csv` |
| 4 | Incendios forestales y riesgo | Loja completo | 575.784 | 7.997 | 41 | `equipo_04_incendios_loja_completo/base_estadistica_equipo_04_incendios_loja_completo_2019_2024.csv` |

## Trabajo obligatorio para todos los equipos

### 1. Formular y delimitar

- Redactar una pregunta de investigación que pueda responderse con el tema, el territorio y el periodo asignados.
- Definir un objetivo general y entre dos y cuatro objetivos específicos medibles.
- Seleccionar un conjunto manejable de variables principales y justificar su función en el análisis.
- Evitar afirmaciones causales: estas bases permiten describir patrones y asociaciones, no demostrar por sí solas causa y efecto.

### 2. Auditar la base antes de analizar

- Comprobar dimensiones, nombres y tipos de variables.
- Verificar que `cell_id`, `anio` y `mes` identifican cada registro; informar duplicados si existieran.
- Confirmar el rango 2019–2024 y los meses 1–12.
- Cuantificar valores faltantes y revisar las variables de cobertura, disponibilidad, soporte y validez del bloque.
- Diferenciar variables analíticas de variables de control de calidad (`coverage`, `n_pixels`, `disponibilidad`, `valid`, `soporte`, `missing`, entre otras).
- Documentar toda exclusión, recodificación, agregación o tratamiento de faltantes. No eliminar registros sin explicarlo.

### 3. Describir y analizar

- Elaborar una tabla de diccionario reducido con variable, significado, unidad, tipo y papel en la investigación.
- Calcular medidas adecuadas al tipo de variable: frecuencias y porcentajes para categorías; media, mediana, desviación estándar, cuartiles, rango e IQR para variables cuantitativas.
- Comparar al menos dos dimensiones pertinentes, por ejemplo años, meses, estaciones, clases o sectores espaciales.
- Construir gráficos con título, ejes, unidades, fuente y una interpretación escrita; el gráfico no sustituye el análisis.
- Examinar asociaciones solo con métodos compatibles con la escala y distribución de las variables.
- Distinguir claramente entre el número de filas, el número de celdas y el número de meses para no inflar el tamaño efectivo de la muestra.

### 4. Comunicar y reproducir

- Entregar el informe acumulativo solicitado en cada unidad.
- Adjuntar el script o cuaderno ejecutable desde la lectura del CSV hasta la generación de resultados.
- Presentar tablas y figuras numeradas y citadas dentro del texto.
- Separar resultados, interpretación, limitaciones y conclusiones.
- Preparar una defensa individual: cada integrante debe explicar la pregunta, las variables, las decisiones de limpieza y al menos un resultado principal.

## Actividades específicas por equipo

### Equipo 1 — Relieve y accesibilidad de Loja

**Propósito sugerido:** caracterizar cómo se distribuyen el relieve y la accesibilidad y estudiar la asociación entre condiciones topográficas, distancia a vías y cercanía a asentamientos.

- Trabajar con elevación, pendiente, orientación (`northness` y `eastness`), distancia a asentamientos, presencia construida, distancia a vías y presencia vial.
- Revisar primero las columnas de cobertura y número de píxeles de ALOS, GHSL y OSM; los valores con poco soporte no deben interpretarse igual que los de cobertura completa.
- Crear clases justificadas de elevación, pendiente o accesibilidad y comparar sus frecuencias y medidas resumen.
- Analizar al menos dos relaciones, por ejemplo pendiente–distancia a vías y elevación–distancia a asentamientos.
- Elaborar como mínimo: una tabla descriptiva, dos distribuciones, un gráfico de relación y una representación espacial basada en `centro_x_m` y `centro_y_m`.

> Las variables de relieve y accesibilidad son esencialmente estáticas y aparecen repetidas en los 72 meses. Para describir el territorio se debe conservar una sola fila por `cell_id`; contar las 575.784 filas como observaciones territoriales independientes produciría pseudorreplicación.

### Equipo 2 — Cobertura vegetal y uso del suelo de Loja

**Propósito sugerido:** describir la composición de coberturas del territorio y analizar la evolución temporal de indicadores espectrales de vegetación, humedad, agua y afectación.

- Examinar las nueve proporciones MAATE y comprobar `suma_prop_maate_9v`, `soporte_maate` y `anio_cut` antes de interpretarlas.
- Trabajar con los índices Sentinel-2: NDVI, NDMI, NBR y NDWI, incluyendo sus medias y desviaciones.
- Revisar `disponible_sentinel_t1`, `sentinel_t1_missing`, cobertura válida, observabilidad, número de observaciones y `lag_meses`.
- Identificar las coberturas dominantes y comparar los índices por año, mes o tipo de cobertura relevante.
- Elaborar como mínimo: una tabla de composición, una serie temporal, una comparación entre coberturas, un gráfico de asociación y una representación espacial.

> Las proporciones MAATE corresponden a una cobertura basal y no deben presentarse como si cambiaran cada mes. Los índices Sentinel-2 sí tienen componente temporal, sujeto a disponibilidad y calidad de observación.

### Equipo 3 — Clima y condiciones atmosféricas de Loja

**Propósito sugerido:** describir la variabilidad temporal y espacial de la precipitación, la sequedad y el viento, e identificar meses o años con condiciones atmosféricas extremas.

- Analizar precipitación acumulada, precipitación máxima diaria, días secos, días húmedos y velocidad media, máxima y variabilidad del viento.
- Diferenciar las variables del mes actual (`t1`) de los acumulados o resúmenes de los dos y tres meses previos (`prev2m`, `prev3m`).
- Filtrar o señalar periodos sin historia completa mediante `chirps_historia_3m_completa` y `chelsa_historia_3m_completa`.
- Revisar días válidos, disponibilidad y cobertura antes de comparar periodos.
- Elaborar como mínimo: perfiles mensuales, comparación anual, distribución de extremos, relación precipitación–días secos o precipitación–viento y una representación espacial.

> Los resúmenes móviles comparten meses entre observaciones consecutivas; no deben interpretarse como mediciones independientes ni sumarse entre sí.

### Equipo 4 — Incendios forestales y riesgo en Loja

**Propósito sugerido:** describir la frecuencia espacial y temporal de evidencia de fuego y evaluar la estabilidad de los resultados ante distintos umbrales de detección.

- Usar `y_incendio_ge7_obs90` como respuesta principal y contrastarla con las respuestas de sensibilidad `ge7`/`ge8` y `obs80`/`obs95`/`obs100`.
- Restringir el análisis principal a observaciones válidas según `y_principal_valida` y, cuando corresponda, `fila_elegible_modelado_principal`.
- Calcular frecuencias y proporciones de meses con incendio por año, mes y celda; identificar concentración temporal y espacial sin confundir conteos con tasas.
- Comparar resultados entre umbrales y explicar qué cambia y qué permanece estable.
- Elaborar como mínimo: tabla de prevalencia, serie temporal, gráfico estacional, mapa o dispersión espacial de frecuencia y tabla de sensibilidad.

> `viirs_source_coverage_frac`, `viirs_disponibilidad_support_pct` y las variables de evidencia son trazabilidad del resultado. No deben utilizarse automáticamente como predictores del mismo incendio, porque producirían fuga de información.

## Archivos auxiliares

- `MANIFIESTO_BASES.csv`: inventario, dimensiones, zona y huellas SHA-256 de los archivos entregados.
- `dataset_maestro_diccionario_grupos_v1_1_0.json`: familias de variables, controles de calidad, respuesta principal y variables de sensibilidad.
- `dataset_maestro_validacion_v1_1_0.json`: resultados de validación del dataset maestro.

## Estructura mínima recomendada de la entrega

```text
equipo_XX/
├── README.md                  # pregunta, integrantes e instrucciones de ejecución
├── informe/                   # PDF y fuente LaTeX solicitada
├── src/                       # script(s) o cuaderno reproducible
├── resultados/
│   ├── tablas/
│   └── figuras/
└── datos/
    └── README.md              # referencia al CSV original; no duplicar ni modificar la fuente
```

## Lista de comprobación final

- [ ] La pregunta corresponde al tema, Loja y al periodo 2019–2024.
- [ ] El CSV original permanece intacto.
- [ ] Los faltantes y controles de calidad están cuantificados y explicados.
- [ ] Las unidades de análisis espacial y temporal se interpretan correctamente.
- [ ] Cada tabla y figura responde a un objetivo y tiene interpretación.
- [ ] Los resultados pueden regenerarse ejecutando el código entregado.
- [ ] Las conclusiones responden a la pregunta y no exceden la evidencia.
- [ ] Todos los integrantes pueden defender individualmente el trabajo.
