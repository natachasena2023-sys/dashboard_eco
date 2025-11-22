import streamlit as st
import pandas as pd


def home_section(df: pd.DataFrame) -> None:
    st.title("🌿 EcoApp – Dashboard de Negocios Verdes en Colombia")

    col1, col2 = st.columns([2, 3])

    with col1:
        total = len(df)
        departamentos = df["DEPARTAMENTO"].nunique() if "DEPARTAMENTO" in df.columns else 0
        sectores = df["SECTOR"].nunique() if "SECTOR" in df.columns else 0

        st.metric("Total de negocios verdes", f"{total:,}".replace(",", "."))
        st.metric("Departamentos presentes", departamentos)
        st.metric("Sectores identificados", sectores)

    with col2:
        st.markdown(
            """
            Este dashboard explora el universo de **Negocios Verdes en Colombia** a partir
            del listado consolidado de iniciativas registradas ante las autoridades ambientales.

            El objetivo es responder preguntas como:
            - ¿En qué regiones se concentran más negocios verdes?
            - ¿Qué sectores tienen mayor presencia?
            - ¿Cómo se conectan estos negocios con el programa **Basura Cero**?

            Usa el menú lateral para navegar por mapas, gráficos y una sección de preguntas frecuentes
            que te ayudará a interpretar los resultados.
            """
        )

    st.markdown("---")

    st.subheader("🔎 Exploración rápida de la tabla")
    st.caption("Puedes filtrar, ordenar y buscar dentro del listado de negocios verdes.")

    st.dataframe(df, use_container_width=True, hide_index=True)
