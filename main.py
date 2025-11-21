# main.py
"""
Punto de entrada principal de la app Streamlit modularizada.
"""

import streamlit as st

from config import (
    IMG_BANNER_SUP,
    IMG_BANNER_INF,
    IMG_BANNER_LARGO,
)
from data_loader import load_data
from utils import img_to_base64, load_css

# Secciones
from sections.home import show_home
from sections.mapa import render_sitemap
from sections.faq import render_faq


def main() -> None:
    """Controlador principal de la aplicación Streamlit."""

    st.set_page_config(
        page_title="Basura Cero | Economía Circular",
        layout="centered",
        page_icon="♻️",
    )

    # Ancho máximo del contenido
    st.markdown(
        "<style>.block-container {max-width: 900px;}</style>",
        unsafe_allow_html=True,
    )

    # Cargar datos
    df = load_data()

    # Cargar imágenes y aplicar CSS
    banner_base64 = img_to_base64(IMG_BANNER_SUP)
    banner_inferior_base64 = img_to_base64(IMG_BANNER_INF)
    

    load_css()

    # Sidebar: navegación
    st.sidebar.header("Navegación")
    section = st.sidebar.radio(
        "Selecciona una sección",
        ("Inicio", "Mapa del sitio", "Preguntas frecuentes"),
        index=0,
    )

    st.sidebar.markdown(
        """
        ---
        **Tip:** Desde la sección Inicio puedes descargar la base normalizada 
        y acceder a la visualización de sectores líderes.
        """
    )

    if section == "Inicio":
        show_home(df)
    elif section == "Mapa del sitio":
        render_sitemap()
    else:
        render_faq()


if __name__ == "__main__":
    main()
