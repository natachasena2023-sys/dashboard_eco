# sections/home.py
from __future__ import annotations

import textwrap
from typing import Tuple, List

import pandas as pd
import streamlit as st

from config import IMG_MAPA_BASURA_CERO
from data_loader import (
    tiene_relacion_basura_cero,
)
from graficos import (
    plot_mapa_basura_cero,
    plot_top_sectores,
    plot_tendencia_anual,
    plot_relacion_basura_cero,
    plot_autoridades,
)


def render_home_header(df: pd.DataFrame) -> None:
    """Encabezado principal con banner y métricas."""
    st.markdown(
        """
        <div class="banner">
            🌿 Residuos con propósito: Colombia hacia la Economía Circular 🌿
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("## Bienvenido al Dashboard de Negocios Verdes en Colombia")
    st.write(
        "Este panel permite explorar información limpia, estandarizada y "
        "enriquecida con indicadores de Economía Circular."
    )

    st.caption("Análisis exploratorio del registro nacional de negocios verdes.")
    st.markdown(resumen_texto(df))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">📄</div>
                <div class="metric-content">
                    <div class="metric-label">Registros</div>
                    <div class="metric-value">{len(df):,}</div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">📊</div>
                <div class="metric-content">
                    <div class="metric-label">Columnas</div>
                    <div class="metric-value">{df.shape[1]}</div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">🗺️</div>
                <div class="metric-content">
                    <div class="metric-label">Departamentos</div>
                    <div class="metric-value">{df["DEPARTAMENTO"].nunique()}</div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image(
            IMG_MAPA_BASURA_CERO,
            caption=(
                "Fuente: Datos abiertos del Gobierno de Colombia "
                "(SSPD y MinVivienda, 2023–2024)"
            ),
            use_container_width=True,
        )

    with col_text:
        st.markdown(
            """
            El mapa muestra la **distribución geográfica de 12 proyectos del Programa Basura Cero**, 
            con una inversión total aproximada de **$119.212 millones de pesos**.  
            Estas iniciativas están orientadas a la **gestión integral de residuos**, el 
            **aprovechamiento de materiales reciclables** y el **cierre progresivo de botaderos**.

            Explora el mapa para conocer en qué departamentos se están desarrollando los proyectos,
            su inversión y fase de avance. 
            """
        )


@st.cache_data(show_spinner=False)
def resumen_texto(df: pd.DataFrame) -> str:
    """Genera texto resumen según los datos filtrados."""
    if df.empty:
        return "**No hay datos para mostrar.**"

    top_dep = df["DEPARTAMENTO"].value_counts().idxmax()
    top_sector = df["SECTOR"].value_counts().idxmax()
    year_min, year_max = df["AÑO"].min(), df["AÑO"].max()

    return textwrap.dedent(
        f"""
        **Resumen del subconjunto activo**

        * Departamento con más negocios: **{top_dep}**
        * Sector predominante: **{top_sector}**
        * Años cubiertos: **{year_min} – {year_max}**
    """
    )


@st.cache_data(show_spinner=False)
def obtener_opciones_filtros(
    df: pd.DataFrame,
) -> Tuple[List[str], List[str], List[str]]:
    """Precalcula y cachea las opciones únicas para los filtros de la tabla."""
    if "REGIÓN" in df.columns:
        regiones = sorted(
            region
            for region in df["REGIÓN"].dropna().unique().tolist()
            if str(region).strip()
        )
    else:
        regiones = []

    if "SECTOR" in df.columns:
        sectores = sorted(
            sector
            for sector in df["SECTOR"].dropna().unique().tolist()
            if str(sector).strip()
        )
    else:
        sectores = []

    if "RELACIÓN BASURA CERO" in df.columns:
        categorias_relacion = sorted(
            {
                categoria.strip()
                for valor in df["RELACIÓN BASURA CERO"].dropna()
                for categoria in str(valor).split(",")
                if categoria.strip()
                and categoria.strip().lower()
                not in {"no aplica", "no disponible"}
            }
        )
    else:
        categorias_relacion = []

    return regiones, sectores, categorias_relacion


def show_home(df: pd.DataFrame) -> None:
    """Sección completa 'Inicio'."""
    render_home_header(df)

    # Mapa Basura Cero
    plot_mapa_basura_cero(df)

    # Top sectores
    plot_top_sectores(df)

    # Tendencia anual
    st.markdown("### 📈 Tendencia anual de negocios verdes")
    plot_tendencia_anual(df)
    st.markdown("")

    # Relación Basura Cero
    plot_relacion_basura_cero(df)

    # Autoridades ambientales
    plot_autoridades(df)

    # Tabla y filtros
    regiones_op, sectores_op, categorias_relacion_op = obtener_opciones_filtros(df)

    if not df.empty:
        with st.expander("📊 Ver Listado_de_Negocios_Verdes"):
            st.caption(
                "La descarga incluye la base completa normalizada, "
                "independientemente de los filtros aplicados."
            )
            csv_full = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Descargar Base de Datos en CSV",
                data=csv_full,
                file_name="negocios_verdes_normalizados.csv",
                mime="text/csv",
            )

            filtered_df = df.copy()

            if "REGIÓN" in df.columns and regiones_op:
                seleccion_regiones = st.multiselect(
                    "Selecciona regiones",
                    regiones_op,
                    help=(
                        "Elige una o más regiones para focalizar la vista de la tabla."
                    ),
                )
                if seleccion_regiones:
                    filtered_df = filtered_df[
                        filtered_df["REGIÓN"].isin(seleccion_regiones)
                    ]

            if "SECTOR" in df.columns and sectores_op:
                seleccion_sectores = st.multiselect(
                    "Selecciona sectores",
                    sectores_op,
                    help="Delimita la tabla a los sectores de tu interés.",
                )
                if seleccion_sectores:
                    filtered_df = filtered_df[
                        filtered_df["SECTOR"].isin(seleccion_sectores)
                    ]

            if "RELACIÓN BASURA CERO" in df.columns and categorias_relacion_op:
                seleccion_relacion = st.multiselect(
                    "Categorías Basura Cero",
                    categorias_relacion_op,
                    help=(
                        "Filtra iniciativas que mencionen explícitamente las categorías "
                        "asociadas al programa Basura Cero."
                    ),
                )
                if seleccion_relacion:
                    import re as _re

                    patron = "|".join(_re.escape(cat) for cat in seleccion_relacion)
                    series_rel = (
                        filtered_df["RELACIÓN BASURA CERO"].fillna("").astype(str)
                    )
                    mask_relacion = series_rel.str.contains(patron, regex=True)
                    filtered_df = filtered_df[mask_relacion]

            st.dataframe(filtered_df, use_container_width=True)

    st.markdown(
        """
        <div class="banner-inferior">
            🌿 Gracias por apoyar los Negocios Ecológicos 🌿
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        💚 *Proyecto académico realizado con Streamlit - Inspirado en la sostenibilidad y el diseño ecológico.*  
        """
    )
