from __future__ import annotations

import streamlit as st

from data_loader import load_data

# Secciones del dashboard
from sections.home import render_home
from sections.mapa import render_mapa
from sections.faq import render_faq
from sections.insights import render_insights           # ⬅️ NUEVO
from sections.basura_cero import render_basura_cero    # ⬅️ NUEVO

# Utilidades
from utils import load_css


def main() -> None:
    # Configuración general de la página
    st.set_page_config(
        page_title="Basura Cero | Negocios Verdes en Colombia",
        layout="centered",
        page_icon="♻️",
    )

    # Cargar CSS personalizado
    load_css()

    # Cargar el dataset
    df = load_data()

    # Barra lateral de navegación
    st.sidebar.header("Navegación")

    section = st.sidebar.radio(
        "Selecciona una sección",
        (
            "Inicio",
            "Mapa del sitio",
            "Preguntas frecuentes",
            "Insights",
            "Basura Cero",
        ),
        index=0,
    )

    st.sidebar.markdown(
        """
        ---
        💡 *Tip:* En **Inicio** puedes descargar la base normalizada y filtrar
        por región, sector y relación con Basura Cero.
        """
    )

    # Router de navegación
    if section == "Inicio":
        render_home(df)

    elif section == "Mapa del sitio":
        render_mapa()

    elif section == "Preguntas frecuentes":
        render_faq()

    elif section == "Insights":
        render_insights(df)

    elif section == "Basura Cero":
        render_basura_cero()


if __name__ == "__main__":
    main()
