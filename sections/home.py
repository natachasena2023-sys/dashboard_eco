# sections/home.py
from __future__ import annotations

import textwrap
from typing import Tuple, List

import pandas as pd
import streamlit as st

from config import IMG_MAPA_BASURA_CERO
from graficos import (
    plot_mapa_basura_cero,
    plot_top_sectores,
    plot_tendencia_anual,
    plot_relacion_basura_cero,
    plot_autoridades,
)


# ============================================================
# ENCABEZADO: Banner, métricas y resumen
# ============================================================

def render_home_header(df: pd.DataFrame) -> None:
    """Encabezado principal con banner y métricas premium."""

    # Banner superior premium
    st.markdown(
        """
        <div class="banner" style="background-image: url('assets/img/baner_l.png');">
            <div class="banner-title-container">
                <h1 class="banner-title">
                    ♻️ Residuos con propósito:<br>
                    Colombia hacia la Economía Circular
                </h1>
            </div>
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

    # --- MÉTRICAS ---
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
                    <div class="metric-value">{df['DEPARTAMENTO'].nunique()}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Imagen mapa + texto
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
            Estas iniciativas están orientadas a la **gestión integral de residuos**, 
            el **aprovechamiento de materiales reciclables** y el **cierre progresivo de botaderos**.

            Explora el mapa para conocer en qué departamentos se están desarrollando los proyectos,
            su inversión y fase de avance.
            """
        )


# ============================================================
# Resumen
# ============================================================

@st.cache_data(show_spinner=False)
def resumen_texto(df: pd.DataFrame) -> str:
    if df.empty:
        return "**No hay datos para mostrar.**"

    top_dep = df["DEPARTAMENTO"].value_counts().idxmax()
    top_sector = df["SECTOR"].value_counts().idxmax()
    year_min, year_max = df["AÑO"].min(), df["AÑO"].max()

    return textwrap.dedent(
        f"""
        **Resumen del subconjunto activo**

        • Departamento con más negocios: **{top_dep}**  
        • Sector predominante: **{top_sector}**  
        • Años cubiertos: **{year_min} – {year_max}**
        """
    )


# ============================================================
# Filtros
# ============================================================

@st.cache_data(show_spinner=False)
def obtener_opciones_filtros(
    df: pd.DataFrame
) -> Tuple[List[str], List[str], List[str]]:

    regiones = sorted(
        [r for r in df.get("REGIÓN", []).dropna().unique().tolist() if str(r).strip()]
    )

    sectores = sorted(
        [s for s in df.get("SECTOR", []).dropna().unique().tolist() if str(s).strip()]
    )

    if "RELACIÓN BASURA CERO" in df.columns:
        categorias_relacion = sorted(
            {
                categoria.strip()
                for val in df["RELACIÓN BASURA CERO"].dropna()
                for categoria in str(val).split(",")
                if categoria.strip()
                and categoria.strip().lower() not in {"no aplica", "no disponible"}
            }
        )
    else:
        categorias_relacion = []

    return regiones, sectores, categorias_relacion


# ============================================================
# Vista principal "Inicio"
# ============================================================

def show_home(df: pd.DataFrame) -> None:
    render_home_header(df)

    # Visualizaciones
    plot_mapa_basura_cero(df)
    plot_top_sectores(df)

    st.markdown("### 📈 Tendencia anual de negocios verdes")
    plot_tendencia_anual(df)

    plot_relacion_basura_cero(df)
    plot_autoridades(df)

    # -----------------------------------------------------------
    # Tabla + filtros
    # -----------------------------------------------------------
    regiones_op, sectores_op, categorias_relacion_op = obtener_opciones_filtros(df)

    if not df.empty:
        with st.expander("📊 Ver Listado_de_Negocios_Verdes"):

            st.caption(
                "La descarga incluye la base COMPLETA normalizada, "
                "independientemente de los filtros."
            )

            csv_full = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Descargar Base de Datos en CSV",
                data=csv_full,
                file_name="negocios_verdes_normalizados.csv",
                mime="text/csv",
            )

            filtered_df = df.copy()

            # Región
            seleccion_regiones = st.multiselect(
                "Selecciona regiones",
                regiones_op,
            )
            if seleccion_regiones:
                filtered_df = filtered_df[filtered_df["REGIÓN"].isin(seleccion_regiones)]

            # Sector
            seleccion_sectores = st.multiselect(
                "Selecciona sectores",
                sectores_op,
            )
            if seleccion_sectores:
                filtered_df = filtered_df[filtered_df["SECTOR"].isin(seleccion_sectores)]

            # Categorías Basura Cero
            seleccion_relacion = st.multiselect(
                "Categorías Basura Cero",
                categorias_relacion_op,
            )
            if seleccion_relacion:
                import re as _re
                patron = "|".join(_re.escape(cat) for cat in seleccion_relacion)
                mask = (
                    filtered_df["RELACIÓN BASURA CERO"]
                    .fillna("")
                    .str.contains(patron, regex=True)
                )
                filtered_df = filtered_df[mask]

            # Mostrar tabla
            st.dataframe(filtered_df, use_container_width=True)

    # ===============================================================
    # BANNER INFERIOR PREMIUM
    # ===============================================================

    st.markdown(
        """
        <div class="banner-inferior" style="background-image: url('assets/img/baner_l.png');">
            <div class="banner-inferior-content">
                <div class="banner-inferior-title">
                    <strong>🌿 Autores 🌿</strong>
                </div>
                <div class="banner-inferior-list">
                    Paulina Noreña · pnorena@unal.edu.co<br>
                    Thomas Medina · thomasmedina519@gmail.com<br>
                    Angie Ruiz · angiecarorumer333@gmail.com<br>
                    Natacha Ochoa · ochoa0917@hotmail.com<br>
                    Juan Ignacio García · juanignaciogarcia7@gmail.com
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        💚 *Proyecto académico realizado con Streamlit — Inspirado en la sostenibilidad y el diseño ecológico.*  
        """
    )
