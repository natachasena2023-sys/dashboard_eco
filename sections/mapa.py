# sections/mapa.py
import streamlit as st


def render_sitemap() -> None:
    """Presenta una guía visual rápida de la aplicación."""
    st.title("Mapa del sitio")
    st.markdown(
        """
        Conoce la estructura general del dashboard para navegar con facilidad.  
        Cada sección está pensada para que encuentres la información clave sobre la estrategia **Basura Cero**.
        """
    )

    st.markdown("---")
    st.subheader("Secciones principales")
    st.markdown(
        """
        - **Inicio:** Panorama general, métricas clave y visualizaciones de los negocios verdes.  
        - **Mapa del sitio:** Esta guía rápida con accesos y descripción de cada módulo.  
        - **Preguntas frecuentes:** Respuestas a dudas comunes sobre el proyecto y los datos.  
        - **Descargas:** En la sección de Inicio puedes descargar la base de datos normalizada.  
        """
    )

    st.subheader("Próximas incorporaciones")
    st.markdown(
        """
        - Paneles interactivos por región.  
        - Seguimiento a indicadores de aprovechamiento y economía circular.  
        - Integración con historias de éxito de emprendimientos verdes.  
        """
    )

    st.info(
        "Sugerencia: Usa el menú lateral para moverte entre secciones "
        "o desplegar la base de datos completa."
    )
