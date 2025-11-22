from __future__ import annotations

import streamlit as st


def render_mapa() -> None:
    """Muestra un mapa del sitio simple para orientar al usuario."""
    st.title("🧭 Mapa del sitio")

    st.markdown(
        """
        Esta sección resume la estructura general del dashboard para facilitar la navegación:

        - **Inicio**: Vista principal con métricas, mapas, gráficas y la tabla completa filtrable.  
        - **Mapa del sitio**: Esta guía rápida de secciones.  
        - **Preguntas frecuentes**: Conceptos clave sobre Negocios Verdes, servicios ecosistémicos y Basura Cero.  

        Usa el menú lateral para moverte entre secciones.
        """
    )

    st.info(
        "Sugerencia: comienza por la sección **Inicio** para entender el panorama general y luego explora las preguntas frecuentes."
    )
