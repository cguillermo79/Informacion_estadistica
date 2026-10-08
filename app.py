import streamlit as st
import streamlit.components.v1 as components
import os
import random
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# ------------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA STREAMLIT
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Estadística Descriptiva · Bloque C · UNL",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------------------
# RUTAS DE ARCHIVOS
# ------------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_html_content():
    posibles_rutas = [
        os.path.join(BASE_DIR, "dashboard_bloque_c_parte1.html"),
        os.path.join(BASE_DIR, "index.html"),
        os.path.join(BASE_DIR, "Unidad 1", "01_guias", "dashboard_bloque_c_parte1.html"),
    ]
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as f:
                return f.read()
    return None

# ------------------------------------------------------------------------------
# BARRA LATERAL (SIDEBAR)
# ------------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🏛️ UNL · FARNR")
    st.markdown("**Carrera de Ingeniería Ambiental**")
    st.markdown("**Asignatura:** Estadística Descriptiva")
    st.markdown("**Docente:** Guillermo Chuncho")
    st.markdown("**Contacto:** `carlos.chuncho@unl.edu.ec`")
    st.markdown("---")
    
    modo = st.radio(
        "Seleccione el Módulo:",
        [
            "🌐 Dashboard Completo & Microreto",
            "🧪 Simulador de Muestreo (Python/NumPy)",
            "📝 Microreto Evaluativo Nativo",
            "📁 Recursos y Guías de Estudio"
        ],
        index=0
    )
    
    st.markdown("---")
    st.markdown(
        """
        <div style="font-size: 11px; color: #64748b; line-height: 1.4;">
        <strong>Bloque C:</strong> Población, Muestra, Parámetros vs. Estadísticos,
        Errores de Muestreo, Sesgo Sistemático y Diseños Probabilísticos y No Probabilísticos.
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------------------------------
# MÓDULO 1: DASHBOARD COMPLETO (HTML / TAILWIND INTERACTIVO)
# ------------------------------------------------------------------------------
if modo == "🌐 Dashboard Completo & Microreto":
    html_code = get_html_content()
    if html_code:
        components.html(html_code, height=1400, scrolling=True)
    else:
        st.error("No se encontró el archivo del dashboard HTML. Por favor verifique el repositorio.")

# ------------------------------------------------------------------------------
# MÓDULO 2: SIMULADOR DE MUESTREO (NATIVO EN PYTHON)
# ------------------------------------------------------------------------------
elif modo == "🧪 Simulador de Muestreo (Python/NumPy)":
    st.title("🧪 Simulador Interactivo de Muestreo y Estimación")
    st.markdown(
        r"""
        Explore empíricamente cómo se comporta un **estadístico muestral** ($\bar{x}$) 
        respecto al **parámetro poblacional verdadero** ($\mu$), y cómo el **error estándar** 
        disminuye conforme se incrementa el tamaño de muestra ($n$).
        """
    )
    
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        param_mu = st.number_input("Parámetro Real μ (Turbidez NTU):", value=45.0, step=1.0)
    with col_c2:
        param_sigma = st.number_input("Desviación Poblacional σ:", value=12.0, step=1.0)
    with col_c3:
        n_muestra = st.slider("Tamaño de Muestra (n):", min_value=5, max_value=120, value=30, step=5)
        
    num_simulaciones = st.slider("Número de réplicas de muestreo (k):", min_value=100, max_value=2000, value=500, step=100)
    
    np.random.seed(42)
    # Generar muestras
    muestras = np.random.normal(loc=param_mu, scale=param_sigma, size=(num_simulaciones, n_muestra))
    medias_muestrales = np.mean(muestras, axis=1)
    
    # Cálculos teóricos vs empíricos
    ee_teorico = param_sigma / np.sqrt(n_muestra)
    ee_empirico = np.std(medias_muestrales, ddof=1)
    media_de_medias = np.mean(medias_muestrales)
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Parámetro Real (μ)", f"{param_mu:.2f} NTU")
    m2.metric("Promedio de Estimadores E(x̄)", f"{media_de_medias:.2f} NTU", delta=f"{media_de_medias - param_mu:.3f}")
    m3.metric("Error Estándar Teórico (σ/√n)", f"{ee_teorico:.2f} NTU")
    m4.metric("Error Estándar Empírico (s_x̄)", f"{ee_empirico:.2f} NTU")
    
    # Gráfico Matplotlib
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.hist(medias_muestrales, bins=35, density=True, color="#047857", alpha=0.65, edgecolor="#064e3b", label="Distribución empírica de x̄")
    
    # Curva normal teórica
    x_lin = np.linspace(medias_muestrales.min(), medias_muestrales.max(), 300)
    y_norm = (1 / (ee_teorico * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_lin - param_mu) / ee_teorico) ** 2)
    ax.plot(x_lin, y_norm, color="#b91c1c", linewidth=2.5, label="Distribución muestral teórica N(μ, σ/√n)")
    
    ax.axvline(param_mu, color="#d97706", linestyle="--", linewidth=2, label=f"μ Verdadero = {param_mu}")
    ax.set_title(f"Distribución Muestral de la Media para n = {n_muestra} (k = {num_simulaciones} réplicas)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Media muestral calculada (x̄ en NTU)")
    ax.set_ylabel("Densidad de probabilidad")
    ax.legend(loc="upper right", frameon=True)
    ax.grid(alpha=0.2)
    
    st.pyplot(fig)
    
    st.info(
        f"💡 **Interpretación para el Ingeniero Ambiental:** Al fijar $n = {n_muestra}$, "
        f"el 95% de las muestras arrojará una estimación dentro del intervalo "
        f"[{param_mu - 1.96*ee_teorico:.2f}, {param_mu + 1.96*ee_teorico:.2f}] NTU. "
        "Si desea mayor precisión, aumentar $n$ estrecha la campana, pero NO elimina sesgos de calibración."
    )

# ------------------------------------------------------------------------------
# MÓDULO 3: MICRORETO EVALUATIVO NATIVO
# ------------------------------------------------------------------------------
elif modo == "📝 Microreto Evaluativo Nativo":
    st.title("📝 Microreto Evaluativo Calificado · Bloque C")
    st.markdown(
        """
        Complete los 10 reactivos de razonamiento. Al finalizar, su nota se calculará sobre **10.0 puntos** 
        y podrá remitirla directamente a la cátedra: `carlos.chuncho@unl.edu.ec`.
        """
    )
    
    # Formulario institucional
    st.subheader("1. Identificación Institucional")
    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        est_nombre = st.text_input("Nombres y Apellidos Completos *:", placeholder="Ej. Ana Belén Carrión")
    with f_col2:
        est_email = st.text_input("Correo Institucional UNL *:", placeholder="usuario@unl.edu.ec")
    with f_col3:
        est_paralelo = st.selectbox("Paralelo:", ["Ingeniería Ambiental - Paralelo A", "Ingeniería Ambiental - Paralelo B", "Ciclo Regular"])
        
    st.markdown("---")
    st.subheader("2. Cuestionario de Razonamiento Práctico (10 Reactivos)")

    quiz = [
        {
            "id": 1,
            "q": "1. Un proyecto en Loja busca evaluar metales pesados en huertos periurbanos utilizando el catastro formal de 2018 (3.200 predios). Sin embargo, existen 1.400 huertos informales sin título surgidos recientemente. ¿Cuál es el problema central al sortear solo del catastro 2018?",
            "opts": [
                "El error muestral será cero porque el tamaño N=3.200 es exacto.",
                "Existe subcobertura en el marco muestral que genera un sesgo de selección sistemático, impidiendo generalizar a toda la población.",
                "Es un muestreo estratificado no proporcional válido por normativa ambiental.",
                "El parámetro μ fluctuará según la cantidad de huertos censados."
            ],
            "correct": 1,
            "exp": "El marco muestral debe incluir a toda la población objetivo. Excluir a los 1.400 huertos genera un sesgo de subcobertura que invalida la extrapolación."
        },
        {
            "id": 2,
            "q": "2. En la cuenca Zamora-Huacapamba, un ingeniero sortea 8 subcuencas de 32 existentes y en cada una recorre un transecto de 2 km pesando cada botella PET encontrada. ¿Cómo se clasifican las unidades?",
            "opts": [
                "La subcuenca es la unidad muestral y cada botella PET es la unidad de análisis.",
                "La unidad muestral y de análisis son idénticas y corresponden al cauce de 2 km.",
                "Cada botella es la unidad muestral y Loja es el marco muestral.",
                "No hay unidades de análisis por tratarse de un muestreo no probabilístico."
            ],
            "correct": 0,
            "exp": "La unidad muestral es la entidad sorteada (la subcuenca) y la unidad de análisis es la entidad medida (cada botella pesada)."
        },
        {
            "id": 3,
            "q": "3. Un sensor de PM2.5 tiene polvo en la lente y sobrestima sistemáticamente un +20%. El técnico recopila 300.000 datos en vez de 500 para 'eliminar el error'. ¿Qué ocurre estadísticamente?",
            "opts": [
                "El error del +20% se anula gradualmente por el teorema del límite central.",
                "La estimación gana altísima precisión (error muestral casi nulo), pero conserva intacto el sesgo sistemático del +20%.",
                "El estadístico x̄ se convierte automáticamente en el parámetro real μ.",
                "El sesgo pasa a comportarse como un error aleatorio simétrico."
            ],
            "correct": 1,
            "exp": "El sesgo sistemático no disminuye con el tamaño de muestra n; solo disminuye la variabilidad aleatoria."
        },
        {
            "id": 4,
            "q": "4. Al analizar 40 vertientes de agua en Vilcabamba se obtiene x̄ = 18.4 mg/L de nitratos. El informe concluye que 'el parámetro μ es exactamente 18.4 mg/L sin margen de duda'. ¿Por qué es un error?",
            "opts": [
                "Porque μ solo existe para aguas superficiales y no subterráneas.",
                "Porque x̄ es un estadístico muestral que estima a μ, pero nunca equivale de manera exacta ni determinista al parámetro sin un intervalo de confianza.",
                "Porque la desviación estándar debió ser numéricamente mayor a la media.",
                "Porque los nitratos son una variable ordinal y no continua."
            ],
            "correct": 1,
            "exp": "Tratar una estimación puntual muestral como una verdad determinista absoluta desconoce la naturaleza de la inferencia estadística."
        },
        {
            "id": 5,
            "q": "5. Se monitorea la DBO5 de una fábrica cada 7 días a las 09:00 AM (muestreo sistemático). La empresa limpia sus calderas con químicos todos los miércoles a las 08:30 AM. Si el sorteo inició un miércoles, ¿qué sucede?",
            "opts": [
                "Nada, porque el muestreo sistemático siempre equivale al aleatorio simple.",
                "La muestra capturará sistemáticamente el pico contaminante por sincronización con la periodicidad cíclica del fenómeno.",
                "El error muestral se anula porque los miércoles representan toda la semana.",
                "El muestreo se vuelve automáticamente estratificado óptimo."
            ],
            "correct": 1,
            "exp": "El peligro clásico del muestreo sistemático es la sincronización con ciclos periódicos del fenómeno evaluado."
        },
        {
            "id": 6,
            "q": "6. En el P.N. Podocarpus las turberas y lagunas representan solo el 3% de la superficie, pero son de alto valor ecológico. Si con n=100 se aplica muestreo estratificado proporcional (nh=3 parcelas), ¿cómo se subsana?",
            "opts": [
                "Se aplica afijación no proporcional asignando mayor muestra a las turberas y luego se reponderan los estimadores analíticamente.",
                "Se elimina el bosque montano del estudio para dar espacio a las turberas.",
                "Se cambia por un muestreo por conveniencia en senderos turísticos.",
                "La afijación proporcional siempre garantiza la mínima varianza."
            ],
            "correct": 0,
            "exp": "En estratos de bajo porcentaje pero de alto interés ambiental se usa afijación no proporcional para asegurar precisión local."
        },
        {
            "id": 7,
            "q": "7. Se entrevista a 80 agricultores que venden en el mercado mayorista un sábado y se concluye que el '78% de los campesinos de la cuenca usa plaguicidas de etiqueta roja'. ¿Cuál es la objeción metodológica principal?",
            "opts": [
                "El tamaño n=80 es ilegal en la legislación ecuatoriana.",
                "Es un muestreo por conveniencia con sesgo de selección: no representa a campesinos de autoconsumo ni fincas agroecológicas que no van a ese mercado.",
                "Debió realizarse en días de lluvia para diluir el químico.",
                "El estadístico p̂ debió integrarse numéricamente."
            ],
            "correct": 1,
            "exp": "Muestrear en ferias comerciales excluye a subgrupos clave que no comercializan allí, invalidando la generalización a toda la cuenca."
        },
        {
            "id": 8,
            "q": "8. ¿Cuál es la diferencia estructural en la composición interna de los grupos entre el Muestreo Estratificado y por Conglomerados?",
            "opts": [
                "En el estratificado los grupos son internamente homogéneos y heterogéneos entre sí; en conglomerados deben ser internamente heterogéneos y similares entre sí.",
                "En el estratificado se eligen solo algunos grupos al azar; en conglomerados se muestrean todos obligatoriamente.",
                "El estratificado es siempre no probabilístico y el de conglomerados es el único probabilístico.",
                "En conglomerados no existe marco muestral en ninguna fase."
            ],
            "correct": 0,
            "exp": "En estratificado se busca varianza interna mínima en cada grupo; en conglomerados cada grupo debe ser un microcosmos representativo."
        },
        {
            "id": 9,
            "q": "9. En un estudio sobre tala y tráfico clandestino de Romerillo sin registros oficiales, ¿qué método no probabilístico es el más idóneo?",
            "opts": [
                "Muestreo aleatorio simple con bolillero digital.",
                "Muestreo por bola de nieve (snowball), donde contactos iniciales de confianza refieren progresivamente a otros participantes de la red oculta.",
                "Muestreo sistemático con cuadrícula de 1 km².",
                "Muestreo por conglomerados catastrales municipales."
            ],
            "correct": 1,
            "exp": "La bola de nieve es la técnica idónea para investigar fenómenos clandestinos o poblaciones ocultas sin marco muestral formal."
        },
        {
            "id": 10,
            "q": "10. Para evaluar ruido en Loja: 1° se sortean 4 parroquias; 2° en cada una se sortean 5 barrios; 3° en cada barrio se miden 3 esquinas. ¿Cómo se clasifica?",
            "opts": [
                "Muestreo no probabilístico por cuotas accidentales.",
                "Muestreo probabilístico polietápico (multietápico por conglomerados sucesivos con selección aleatoria en cada etapa).",
                "Muestreo aleatorio simple con reposición infinita.",
                "Muestreo intencional por juicio técnico."
            ],
            "correct": 1,
            "exp": "Es un diseño probabilístico polietápico en 3 niveles de selección con probabilidad de inclusión cuantificable."
        }
    ]

    respuestas_usuario = {}
    with st.form("form_microreto"):
        for item in quiz:
            st.markdown(f"**{item['q']}**")
            respuestas_usuario[item["id"]] = st.radio(
                f"Seleccione su respuesta para la pregunta {item['id']}:",
                item["opts"],
                index=None,
                key=f"q_{item['id']}"
            )
            st.write("")
            
        btn_submit = st.form_submit_button("Calificar y Generar Comprobante Oficial", type="primary")

    if btn_submit:
        if not est_nombre:
            st.error("⚠️ Por favor ingrese sus Nombres y Apellidos completos.")
        elif not est_email or "@unl.edu.ec" not in est_email.lower():
            st.error("⚠️ Por favor ingrese un correo institucional válido con dominio @unl.edu.ec.")
        else:
            # Calificación
            aciertos = 0
            detalles_texto = []
            for item in quiz:
                user_sel = respuestas_usuario[item["id"]]
                if user_sel is not None:
                    opt_idx = item["opts"].index(user_sel)
                    es_correcto = (opt_idx == item["correct"])
                    if es_correcto:
                        aciertos += 1
                    status = "CORRECTO (1.0 pt)" if es_correcto else "INCORRECTO (0.0 pt)"
                    detalles_texto.append(f"P{item['id']}: {status} | Selección: {user_sel[:55]}...")
                else:
                    detalles_texto.append(f"P{item['id']}: NO RESPONDIDA (0.0 pt)")
                    
            nota_final = float(aciertos)
            porcentaje = int((aciertos / len(quiz)) * 100)
            codigo_verificacion = f"UNL-EST-C-{random.randint(100000, 999999)}-{aciertos}"
            fecha_entrega = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            st.success("🎉 ¡Microreto calificado exitosamente!")
            if nota_final >= 7.0:
                st.balloons()

            # Resumen visual
            r1, r2, r3 = st.columns(3)
            r1.metric("Estudiante", est_nombre)
            r2.metric("Calificación Final", f"{nota_final:.1f} / 10.0")
            r3.metric("Porcentaje de Acierto", f"{porcentaje}%")

            st.info(f"**Código de Verificación:** `{codigo_verificacion}` | **Fecha:** {fecha_entrega}")

            # Transmisión a carlos.chuncho@unl.edu.ec vía FormSubmit
            try:
                res = requests.post(
                    "https://formsubmit.co/ajax/carlos.chuncho@unl.edu.ec",
                    json={
                        "_subject": f"[MICRORETO STREAMLIT] {nota_final:.1f}/10 - {est_nombre} ({est_email})",
                        "_template": "table",
                        "Estudiante": est_nombre,
                        "Correo_Institucional": est_email,
                        "Paralelo": est_paralelo,
                        "Nota_Final": f"{nota_final:.1f} / 10.0 ({porcentaje}%)",
                        "Codigo_Verificacion": codigo_verificacion,
                        "Fecha_Registro": fecha_entrega,
                        "Detalle_Respuestas": "\n".join(detalles_texto)
                    },
                    timeout=8
                )
                if res.status_code == 200:
                    st.success("✅ **Calificación enviada automáticamente a la bandeja del docente:** `carlos.chuncho@unl.edu.ec`")
                else:
                    st.warning("⚠️ El servicio externo tardó en confirmar. Utilice el comprobante descargable como respaldo.")
            except Exception:
                st.warning("⚠️ No se pudo enviar por conexión web directa. Descargue su comprobante para adjuntarlo al EVA.")

            # Comprobante descargable
            reporte_completo = (
                f"==================================================\n"
                f"COMPROBANTE OFICIAL DE MICRORETO - BLOQUE C\n"
                f"UNIVERSIDAD NACIONAL DE LOJA - INGENIERÍA AMBIENTAL\n"
                f"Docente: Guillermo Chuncho (carlos.chuncho@unl.edu.ec)\n"
                f"==================================================\n"
                f"Estudiante: {est_nombre}\n"
                f"Correo Institucional: {est_email}\n"
                f"Paralelo: {est_paralelo}\n"
                f"Calificación Final: {nota_final:.1f} / 10.0 ({porcentaje}%)\n"
                f"Código Único: {codigo_verificacion}\n"
                f"Fecha y Hora: {fecha_entrega}\n"
                f"==================================================\n"
                f"DESGLOSE DE RESPUESTAS:\n"
                + "\n".join(detalles_texto) + "\n"
                f"==================================================\n"
            )

            st.download_button(
                label="📥 Descargar Comprobante Oficial (.txt)",
                data=reporte_completo,
                file_name=f"Comprobante_Microreto_{est_nombre.replace(' ', '_')}.txt",
                mime="text/plain"
            )

# ------------------------------------------------------------------------------
# MÓDULO 4: RECURSOS Y GUÍAS DE ESTUDIO
# ------------------------------------------------------------------------------
elif modo == "📁 Recursos y Guías de Estudio":
    st.title("📁 Recursos de la Asignatura y Proyecto Integrador")
    st.markdown(
        """
        Documentación oficial de la Unidad 1 para la carrera de **Ingeniería Ambiental**:
        """
    )
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.subheader("📘 Guía de Estudio 1")
        st.write("Fundamentos y conceptos introductorios.")
        ruta_g1 = os.path.join(BASE_DIR, "Unidad 1", "01_guias", "Guia 1.pdf")
        if os.path.exists(ruta_g1):
            with open(ruta_g1, "rb") as f:
                st.download_button("Descargar Guía 1 (PDF)", f, file_name="Guia_1_Estadistica.pdf")
                
    with col_g2:
        st.subheader("📗 Guía de Estudio 2")
        st.write("Ejercicios prácticos y casos de estudio de razonamiento.")
        ruta_g2 = os.path.join(BASE_DIR, "Unidad 1", "01_guias", "Guia 2.pdf")
        if os.path.exists(ruta_g2):
            with open(ruta_g2, "rb") as f:
                st.download_button("Descargar Guía 2 (PDF)", f, file_name="Guia_2_Estadistica.pdf")
                
    st.markdown("---")
    st.markdown("### 🗃️ Bases de Datos del Proyecto Integrador")
    st.markdown(
        """
        Las bases georreferenciadas del cantón Loja (2019–2024) por equipo temático están alojadas en:
        * **Grupo 1:** Relieve y accesibilidad
        * **Grupo 2:** Cobertura vegetal y uso de suelo
        * **Grupo 3:** Clima y variables atmosféricas
        * **Grupo 4:** Incendios forestales y riesgo
        
        Consulte la carpeta `Unidad 1/bases_datos_proyecto_integrador` en el repositorio para los archivos CSV y diccionarios de variables.
        """
    )
