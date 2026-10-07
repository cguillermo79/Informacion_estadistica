# Bases del proyecto integrador FIRELAB-Loja — Estadística Descriptiva

## Población y muestra

- **Población:** las 7.997 celdas de 500 m × 500 m (25 ha) que cubren el cantón Loja, observadas mensualmente de enero de 2019 a diciembre de 2024 (72 meses).
- **Fuente:** dataset maestro FIRELAB-Loja v1.1.0 (`dataset_maestro_firelab_loja_2019_2025_v1_1_0.csv`, SHA-256 `890423faf91207aa271feb9878b1b379e309c156e8e7128af380a5c1afe674b6`). El año 2025 no se incluye.
- **Muestra:** 400 celdas seleccionadas por **muestreo aleatorio estratificado proporcional**. Los estratos son las zonas norte (`centro_y_m >= 9555250`, 4.001 celdas) y sur (3.996 celdas), con 200 celdas por zona y semilla 2026. Las **mismas 400 celdas** se usan en las cuatro bases; la lista y la probabilidad de inclusión están en `muestra_celdas.csv`.
- **Tamaño de muestra** (proporción, 95 % de confianza, error de 5 %, p = 0,5):

  $n_0 = \dfrac{1{,}96^2 (0{,}5)(0{,}5)}{0{,}05^2} = 384{,}2$; con corrección por población finita, $n = \dfrac{384{,}2}{1 + 383{,}2/7997} \approx 367$. Se usan **400** celdas (margen para celdas de borde o con datos faltantes).

- **Sin modificar valores:** las variables se tomaron tal cual del dataset maestro. Solo se seleccionaron columnas y celdas, se redondearon los valores (2 decimales si el valor es 10 o mayor; 4 si es menor) y se agregó la ocurrencia de incendios a las bases de los grupos 1–3.

## Archivos por grupo

| Grupo | Tema | Archivo | Filas | Columnas | Unidad de observación |
|---:|---|---|---:|---:|---|
| 1 | Relieve y accesibilidad | `grupo_01_relieve/grupo_01_relieve.csv` | 400 | 24 | Celda (el relieve no cambia en el tiempo) |
| 1 | Relieve y accesibilidad | `grupo_01_relieve/grupo_01_incendios_mensuales.csv` | 28.800 | 7 | Celda–mes (para series temporales) |
| 2 | Cobertura vegetal y uso del suelo | `grupo_02_cobertura/grupo_02_cobertura.csv` | 28.800 | 30 | Celda–mes |
| 3 | Clima y condiciones atmosféricas | `grupo_03_clima/grupo_03_clima.csv` | 28.800 | 26 | Celda–mes |
| 4 | Incendios forestales y riesgo | `grupo_04_incendios/grupo_04_incendios.csv` | 28.800 | 26 | Celda–mes |

- **Columnas comunes:** todas las bases traen la identificación y ubicación de la celda (`cell_id`, `zona`, coordenadas, área dentro del cantón) y, salvo la de relieve, el tiempo (`anio`, `mes`, `anio_mes`).
- **Incendios en todas las bases:** para relacionar cada tema con los incendios, las bases incluyen la ocurrencia de incendios: `y_incendio_ge7_obs90` y `y_principal_valida`. En la base de relieve va resumida por celda (`meses_con_incendio`, `incendio_2019_2024`).
- **Grupo 4:** recibe además cuatro covariables de contexto (elevación, pendiente, precipitación y días secos) para poder relacionar la ocurrencia de incendios con el territorio en la Unidad 3.

## Archivos auxiliares

- `DICCIONARIO_VARIABLES.csv`: significado, unidad, tipo de dato y valores esperados de cada columna. La **escala de medición** (nominal, ordinal, intervalo o razón) la debe clasificar cada grupo en la Fase 2 de la Unidad 1.
- `muestra_celdas.csv`: las 400 celdas de la muestra, su estrato y su probabilidad de inclusión.
- `MANIFIESTO_BASES.csv`: dimensiones, tamaño y huella SHA-256 de cada archivo, para comprobar que no fue modificado.
- `dataset_maestro_diccionario_grupos_v1_1_0.json` y `dataset_maestro_validacion_v1_1_0.json`: referencia del dataset maestro completo.

## ¿Alcanzan estas bases para todo el proyecto?

Sí. La siguiente tabla resume qué contenido del curso puede aplicar cada grupo con su base.

| Contenido del curso | Grupo 1 Relieve | Grupo 2 Cobertura | Grupo 3 Clima | Grupo 4 Incendios |
|---|---|---|---|---|
| **U1** Población, muestra, unidad de análisis | Sí (400 celdas) | Sí (celda–mes) | Sí (celda–mes) | Sí (celda–mes) |
| **U1** Tipos de variables y escalas | Cuantitativas continuas + `zona`, `incendio_2019_2024` | Proporciones, índices, códigos | Continuas, conteos (días), códigos | Binarias, categórica `estado_ge7_obs90`, contexto |
| **U1** Tablas de frecuencias | Clases de elevación y pendiente; zona | Cobertura dominante (derivada); clases de NDVI | Clases de lluvia; meses secos | Incendios por mes, año y zona |
| **U2** Gráficos y medidas descriptivas | Sí | Sí | Sí | Sí |
| **U2** Series temporales (72 meses) | Sí, con `grupo_01_incendios_mensuales.csv` por clase de relieve | Sí (NDVI con datos en 71 de 72 meses) | Sí, completa y sin faltantes | Sí (estacionalidad marcada) |
| **U3** Intervalos de confianza (muestra → cantón) | Sí | Sí | Sí | Sí |
| **U3** Tablas de contingencia y chi-cuadrado | Clase de relieve × incendio | Cobertura dominante × incendio | Mes seco/húmedo × incendio | Zona × incendio; mes × incendio |
| **U3** Regresión logística | Incendio (sí/no) ~ relieve | Incendio ~ NDVI, cobertura | Incendio ~ lluvia, días secos | Incendio ~ covariables de contexto |
| **U3** Geoestadística (introducción) | Coordenadas UTM de 400 celdas | Ídem | Ídem | Ídem |

**Precauciones que deben conocer los grupos:**

1. **El relieve es estático.** La base del grupo 1 tiene una fila por celda; sus series temporales se construyen con `grupo_01_incendios_mensuales.csv` (por ejemplo, la proporción mensual de celdas con incendio por clase de pendiente).
2. **Faltantes de Sentinel-2.** El 19,5 % de los registros celda–mes del grupo 2 no tiene índice (nubes o falta de imagen; `sentinel_t1_missing = 1`). Se deben excluir y documentar, no rellenar.
3. **Los incendios son eventos raros.** En la muestra hay 164 meses-celda con incendio válido, que son el 0,6 % de los registros celda–mes. Corresponden a 127 de las 400 celdas (31,8 %) y se concentran de agosto a noviembre. Para chi-cuadrado conviene trabajar a nivel de celda o agrupar meses. En la regresión logística hay que interpretar probabilidades pequeñas y usar `y_principal_valida = 1`.
4. **Filas no son observaciones independientes.** Las 28.800 filas son 400 celdas × 72 meses: el tamaño efectivo para inferir al cantón es de 400 celdas, no de 28.800 filas.
5. **Asociación no es causa.** Las bases permiten describir patrones y asociaciones, no demostrar causas.

## Reglas

- Cada grupo usa solo su base y el periodo 2019–2024.
- Los CSV son de solo lectura; toda limpieza o transformación se hace con código (R o Python) y se documenta.
- Las bases completas (7.997 celdas) no se distribuyen a los estudiantes; las conserva el docente.
