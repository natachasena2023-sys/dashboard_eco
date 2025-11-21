# sections/faq.py
import streamlit as st


def render_faq() -> None:
    """Muestra un listado de preguntas frecuentes con respuestas."""
    st.title("Preguntas frecuentes")
    st.markdown(
        """
    Aquí encontrarás respuestas rápidas sobre el origen de la información, cómo se procesan los datos
    y cómo puedes aprovechar el tablero en tus proyectos.
    """
    )

    faq_items = [
        (
            "¿De dónde provienen los datos?",
            "Los datos se descargan de fuentes oficiales como la Superintendencia de Servicios Públicos "
            "Domiciliarios y MinVivienda, además del listado nacional de Negocios Verdes disponible "
            "en datos abiertos.",
        ),
        (
            "¿Cada cuánto se actualiza la información?",
            "Puedes reemplazar el enlace del CSV por la versión más reciente publicada en GitHub u otra fuente. "
            "La función de carga está cacheada para optimizar el rendimiento.",
        ),
        (
            "¿Cómo se realizó la limpieza de los datos?",
            "Se estandarizaron nombres de columnas, se normalizaron productos y sectores, y se completaron "
            "las regiones basadas en la autoridad ambiental correspondiente.",
        ),
        (
            "¿Puedo descargar la base de datos filtrada?",
            "Sí. En la sección de Inicio encontrarás un botón para descargar el CSV con la versión normalizada "
            "del dataset.",
        ),
        (
            "¿Qué puedo hacer si falta una imagen del banner?",
            "La aplicación mostrará una advertencia y utilizará un marcador de posición, por lo que puedes "
            "subir tus propias imágenes a la carpeta `assets/img/` para personalizarlo.",
        ),
    ]

    for question, answer in faq_items:
        with st.expander(question):
            st.write(answer)

    st.success(
        "¿Tienes otra pregunta? ¡Añádela en el repositorio o compártela con el equipo!"
    )
