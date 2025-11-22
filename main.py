from __future__ import annotations

import streamlit as st

from data_loader import load_data
from sections.home import render_home
from sections.mapa import render_mapa
from sections.faq import render_faq
from sections.insights import render_insights   # ⬅️ NUEVO
from utils import load_css


def main() -> None:
    st.set_page_config(
        page_title="Basura Cero | Negocios Verdes en Colombia",
        layout="centered",
        page_icon="♻️",
    )

    # CSS y tema visual
    load_css()

    # Cargar datos
    df = load_data()

    # Navegación lateral
    st.sidebar.header("Navegación")
    section = st.sidebar.radio(
        "Selecciona una sección",
        ("Inicio", "Mapa del sitio", "Preguntas frecuentes", "Insights"),  # ⬅️ NUEVO
        index=0,
    )
    st.sidebar.markdown(
        """
        ---
        💡 *Tip:* En **Inicio** puedes descargar la base normalizada y filtrar
        por región, sector y relación con Basura Cero.
        """
    )

    # Router de secciones
    if section == "Inicio":
        render_home(df)

    elif section == "Mapa del sitio":
        render_mapa()

    elif section == "Preguntas frecuentes":
        render_faq()

    elif section == "Insights":   # ⬅️ NUEVO
        render_insights(df)


if __name__ == "__main__":
    main()
