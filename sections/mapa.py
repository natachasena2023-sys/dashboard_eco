import streamlit as st
import pandas as pd

from graficos import plot_mapa_basura_cero


def mapa_section(df: pd.DataFrame) -> None:
    st.header("🗺️ Mapa General de Negocios Verdes y Basura Cero")

    st.markdown(
        """
        Este mapa muestra la distribución de los negocios verdes por departamento,
        destacando el porcentaje de iniciativas que tienen **relación identificada**
        con el programa **Basura Cero**.

        - El **tamaño del punto** representa el número total de iniciativas registradas.
        - El **color** indica el porcentaje de negocios alineados con Basura Cero.
        """
    )

    plot_mapa_basura_cero(df)

    st.markdown("---")
    st.subheader("Descripción de campos usados en el mapa")
    st.markdown(
        """
        - **DEPARTAMENTO**: Territorio donde se ubica el negocio verde.  
        - **TOTAL**: Número total de negocios verdes registrados en el departamento.  
        - **ALINEADOS**: Cantidad de iniciativas que presentan relación con Basura Cero.  
        - **PORCENTAJE**: Proporción de iniciativas alineadas frente al total del departamento.
        """
    )
