# Estadística Descriptiva — Proyecto Integrador y Recursos de Aprendizaje

**Carrera de Ingeniería Ambiental · Universidad Nacional de Loja · Ciclo septiembre 2026 – febrero 2027**  
**Docente:** Guillermo Chuncho (`carlos.chuncho@unl.edu.ec`)

[![Abrir en Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://informacionestadistica-etzfkqjbmr8tyfno47xvsi.streamlit.app)

> 🚀 **Aplicación Web Oficial (Streamlit Cloud):**  
> 👉 **[https://informacionestadistica-etzfkqjbmr8tyfno47xvsi.streamlit.app](https://informacionestadistica-etzfkqjbmr8tyfno47xvsi.streamlit.app)**  
> *(Dashboard interactivo de muestreo, simulador Monte Carlo de parámetros vs. estadísticos y **Microreto Evaluativo Calificado de 10 reactivos** con calificación automática y envío a `carlos.chuncho@unl.edu.ec`)*.

---

Este repositorio reúne el material oficial del proyecto integrador y los recursos didácticos de la asignatura. Durante todo el semestre, cada grupo trabaja con datos ambientales reales y georreferenciados del cantón Loja (2019–2024) del proyecto FIRELAB-Loja: relieve, cobertura vegetal, clima e incendios forestales.

---

## 🌐 Acceso a la Aplicación

1. **En Línea (Estudiantes y Docente):** Ingrese directamente a **[https://informacionestadistica-etzfkqjbmr8tyfno47xvsi.streamlit.app](https://informacionestadistica-etzfkqjbmr8tyfno47xvsi.streamlit.app)** desde cualquier dispositivo sin instalar nada.
2. **Local (Desarrollo):**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```
3. **Local directo en el navegador (archivo HTML independiente):**
   Abra directamente [`index.html`](index.html) o [`Unidad 1/01_guias/dashboard_bloque_c_parte1.html`](Unidad%201/01_guias/dashboard_bloque_c_parte1.html).

---

## Empiece aquí

**[Guía paso a paso para descargar el repositorio y preparar el entorno](00_guia_descarga/guia_descarga_repositorio_estadistica.pdf)**: qué es la terminal, cómo aceptar la invitación, instalar Git, clonar este repositorio, crear y activar el entorno virtual (`.venv`), instalar las librerías (`requirements.txt`) y actualizar el material con `git pull`.

---

## Unidad 1

| Carpeta | Contenido |
|---|---|
| [`Unidad 1/01_guias`](Unidad%201/01_guias/) | **Guías de estudio Bloque C**: Guía 1 (Fundamentos Teóricos de Muestreo Ambiental, PDF y LaTeX), Guía 2 (Taller Práctico y Microreto de Razonamiento, PDF y LaTeX) y Dashboard interactivo con simulador y evaluación. |
| [`Unidad 1/guia_proyecto_integrador`](Unidad%201/guia_proyecto_integrador/guia_proyecto_integrador_estadistica.pdf) | **Guía del proyecto integrador** (PDF y fuente LaTeX): grupos e integrantes, bases, fases, fechas y qué presentar en cada unidad. |
| [`Unidad 1/formato_proyecto_integrador`](Unidad%201/formato_proyecto_integrador/) | **Formato LaTeX del informe** (`proyecto_integrador_estadistica.tex` + `referencias.bib`, normas APA 7). |
| [`Unidad 1/bases_datos_proyecto_integrador`](Unidad%201/bases_datos_proyecto_integrador/README.md) | **Bases de datos** de los cuatro grupos, diccionario de variables y descripción de la muestra. |

---

## Grupos

| Grupo | Tema | Base |
|---:|---|---|
| 1 | Relieve y accesibilidad | `grupo_01_relieve/` |
| 2 | Cobertura vegetal y uso del suelo | `grupo_02_cobertura/` |
| 3 | Clima y condiciones atmosféricas | `grupo_03_clima/` |
| 4 | Incendios forestales y riesgo | `grupo_04_incendios/` |

Los integrantes de cada grupo están especificados en la guía del proyecto integrador.

---

## Descarga y Clonación

```bash
git clone https://github.com/cguillermo79/Informacion_estadistica.git
```

También puede usar **Code → Download ZIP** en la página del repositorio. La carpeta `Unidad 1` tiene un espacio en el nombre: en la terminal escríbala entre comillas (`cd "Unidad 1"`).

---

## Reglas de los Datos

- Cada grupo usa únicamente su base y el periodo 2019–2024.
- Los CSV son de solo lectura: toda limpieza o transformación se hace con código reproducible y se documenta.
- Las bases corresponden a una muestra estratificada de 400 de las 7.997 celdas del cantón; los resultados describen la muestra y se generalizan al cantón con inferencia estadística (Unidad 3).
