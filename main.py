from __future__ import annotations

import streamlit as st

# Carga de datos
from data_loader import load_data

# Secciones del dashboard
from sections.home import render_home
from sections.mapa import render_mapa
from sections.faq import render_faq
from sections.insights import render_insights
from sections.basura_cero import render_basura_cero
from sections.historias import render_historias   # ⬅️ NUEVO

# Utilidades
from utils import load_css


def main() -> None:
    # Configuración general de la app
    st.set_page_config(
        page_title="Basura Cero | Negocios Verdes en Colombia",
        layout="centered",
        page_icon="♻️",
    )

    # CSS personalizado
    load_css()

    # Cargar dataset
    df = load_data()

    # Sidebar de navegación
    st.sidebar.header("Navegación")

    section = st.sidebar.radio(
        "Selecciona una sección",
        (
            "Inicio",
            "Mapa del sitio",
            "Preguntas frecuentes",
            "Insights",
            "Basura Cero",
            "Historias Reales",       # ⬅️ NUEVO
        ),
        index=0,
    )

    st.sidebar.markdown(
        """
        ---
        💡 *Tip:* En **Inicio** puedes descargar la base normalizada y 
        filtrar por región, sector y relación con Basura Cero.
        """
    )

    # Router de vistas
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

    elif section == "Historias Reales":
        render_historias()   # ⬅️ NUEVO


if __name__ == "__main__":
    main()
