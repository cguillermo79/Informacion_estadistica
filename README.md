# Estadística Descriptiva — Proyecto integrador

**Carrera de Ingeniería Ambiental · Universidad Nacional de Loja · Ciclo septiembre 2026 – febrero 2027**
**Docente:** Carlos Guillermo Chuncho Morocho

Este repositorio reúne el material del proyecto integrador de la asignatura. Durante todo el semestre, cada grupo trabaja con datos ambientales reales y georreferenciados del cantón Loja (2019–2024) del proyecto FIRELAB-Loja: relieve, cobertura vegetal, clima e incendios forestales.

## Unidad 1

| Carpeta | Contenido |
|---|---|
| [`Unidad 1/guia_proyecto_integrador`](Unidad%201/guia_proyecto_integrador/guia_proyecto_integrador_estadistica.pdf) | **Guía del proyecto integrador** (PDF y fuente LaTeX): grupos e integrantes, bases, fases, fechas y qué presentar en cada unidad. |
| [`Unidad 1/formato_proyecto_integrador`](Unidad%201/formato_proyecto_integrador/) | **Formato LaTeX del informe** (`proyecto_integrador_estadistica.tex` + `referencias.bib`, normas APA 7). |
| [`Unidad 1/bases_datos_proyecto_integrador`](Unidad%201/bases_datos_proyecto_integrador/README.md) | **Bases de datos** de los cuatro grupos, diccionario de variables y descripción de la muestra. |

## Grupos

| Grupo | Tema | Base |
|---:|---|---|
| 1 | Relieve y accesibilidad | `grupo_01_relieve/` |
| 2 | Cobertura vegetal y uso del suelo | `grupo_02_cobertura/` |
| 3 | Clima y condiciones atmosféricas | `grupo_03_clima/` |
| 4 | Incendios forestales y riesgo | `grupo_04_incendios/` |

Los integrantes de cada grupo están en la guía del proyecto integrador.

## Descarga

```bash
git clone https://github.com/cguillermo79/Informacion_estadistica.git
```

También puede usar **Code → Download ZIP** en la página del repositorio. La carpeta `Unidad 1` tiene un espacio en el nombre: en la terminal escríbala entre comillas (`cd "Unidad 1"`).

## Reglas de los datos

- Cada grupo usa únicamente su base y el periodo 2019–2024.
- Los CSV son de solo lectura: toda limpieza o transformación se hace con código y se documenta.
- Las bases son una muestra estratificada de 400 de las 7.997 celdas del cantón; los resultados describen la muestra y se generalizan al cantón con inferencia (Unidad 3).
