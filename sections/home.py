from __future__ import annotations

from typing import Tuple, List
import re as _re

import pandas as pd
import streamlit as st

from graficos import (
    plot_mapa_basura_cero_por_departamento,
    plot_top_sectores,
    plot_tendencia_anual,
    plot_relacion_basura_cero,
    plot_autoridades,
)
from utils import render_footer


@st.cache_data(show_spinner=False)
def resumen_texto(df: pd.DataFrame) -> str:
    """Genera un breve resumen del subconjunto de datos activo."""
    if df.empty:
        return "No hay datos para mostrar."
    top_dep = df["DEPARTAMENTO"].value_counts().idxmax()
    top_sector = df["SECTOR"].value_counts().idxmax()
    year_min, year_max = df["AÑO"].min(), df["AÑO"].max()
    return (
        "**Resumen del subconjunto activo**\n\n"
        f"* Departamento con más negocios: **{top_dep}**\n"
        f"* Sector predominante: **{top_sector}**\n"
        f"* Años cubiertos: **{year_min} – {year_max}**"
    )


@st.cache_data(show_spinner=False)
def obtener_opciones_filtros(df: pd.DataFrame) -> Tuple[List[str], List[str], List[str]]:
    """Lista de opciones únicas para filtros (región, sector, categorías Basura Cero)."""
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


def render_home(df: pd.DataFrame) -> None:

    # Banner superior con imagen completa
    st.markdown(
        """
        <img src="assets/img/baner_l.png" class="banner-img">
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## Bienvenido al Dashboard de Negocios Verdes en Colombia")

    st.write(
        "Este panel permite explorar información limpia, estandarizada y enriquecida con indicadores "
        "relacionados con la economía circular y el programa **Basura Cero**."
    )
    st.markdown(resumen_texto(df))

    # Métricas principales
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"<div class='metric-card'><div class='metric-icon'>📄</div>"
            f"<div class='metric-content'><div class='metric-label'>Registros</div>"
            f"<div class='metric-value'>{len(df):,}</div></div></div>",
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"<div class='metric-card'><div class='metric-icon'>📊</div>"
            f"<div class='metric-content'><div class='metric-label'>Columnas</div>"
            f"<div class='metric-value'>{df.shape[1]}</div></div></div>",
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"<div class='metric-card'><div class='metric-icon'>🗺️</div>"
            f"<div class='metric-content'><div class='metric-label'>Departamentos</div>"
            f"<div class='metric-value'>{df['DEPARTAMENTO'].nunique()}</div></div></div>",
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.subheader("Mapa de proyectos emblemáticos del programa Basura Cero")
    st.image(
        "assets/img/mapa_basura_cero.jpg",
        caption="Fuente: Datos abiertos del Gobierno de Colombia (SSPD y MinVivienda, 2023–2024).",
        use_container_width=True,
    )

    # Visualizaciones principales
    plot_mapa_basura_cero_por_departamento(df)
    plot_top_sectores(df)
    plot_tendencia_anual(df)
    plot_relacion_basura_cero(df)
    plot_autoridades(df)

    # Tabla detallada con filtros
    regiones_op, sectores_op, categorias_relacion_op = obtener_opciones_filtros(df)
    if not df.empty:
        with st.expander("📊 Ver Listado_de_Negocios_Verdes"):
            st.caption(
                "La descarga incluye la base completa normalizada, independientemente de los filtros aplicados."
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
                    help="Elige una o más regiones para focalizar la vista de la tabla.",
                )
                if seleccion_regiones:
                    filtered_df = filtered_df[filtered_df["REGIÓN"].isin(seleccion_regiones)]

            if "SECTOR" in df.columns and sectores_op:
                seleccion_sectores = st.multiselect(
                    "Selecciona sectores",
                    sectores_op,
                    help="Delimita la tabla a los sectores de tu interés.",
                )
                if seleccion_sectores:
                    filtered_df = filtered_df[filtered_df["SECTOR"].isin(seleccion_sectores)]

            if "RELACIÓN BASURA CERO" in df.columns and categorias_relacion_op:
                seleccion_relacion = st.multiselect(
                    "Categorías Basura Cero",
                    categorias_relacion_op,
                    help=(
                        "Filtra iniciativas que mencionen explícitamente las categorías asociadas al programa Basura Cero."
                    ),
                )
                if seleccion_relacion:
                    patron = "|".join(_re.escape(cat) for cat in seleccion_relacion)
                    series_rel = filtered_df["RELACIÓN BASURA CERO"].fillna("").astype(str)
                    mask_relacion = series_rel.str.contains(patron, regex=True)
                    filtered_df = filtered_df[mask_relacion]

            st.dataframe(filtered_df, use_container_width=True)

    # Banner inferior de cierre + autores
    render_footer()
