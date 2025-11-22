from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from data_loader import coordenadas_departamento, tiene_relacion_basura_cero


def plot_mapa_basura_cero_por_departamento(df: pd.DataFrame) -> None:
    """Mapa interactivo con intensidad de alineación Basura Cero por departamento."""
    if df.empty or not {"DEPARTAMENTO", "RELACIÓN BASURA CERO"}.issubset(df.columns):
        return

    mapa_df = df.copy()
    relacion_normalizada = (
        mapa_df["RELACIÓN BASURA CERO"].fillna("").astype(str).str.strip().str.lower()
    )
    mapa_df["TIENE_RELACION"] = ~relacion_normalizada.isin({"", "no aplica", "no disponible"})

    resumen_departamentos = (
        mapa_df.groupby("DEPARTAMENTO")
        .agg(TOTAL=("DEPARTAMENTO", "size"), ALINEADOS=("TIENE_RELACION", "sum"))
        .reset_index()
    )
    if resumen_departamentos.empty:
        return

    resumen_departamentos["ALINEADOS"] = resumen_departamentos["ALINEADOS"].astype(int)
    resumen_departamentos["PORCENTAJE"] = (
        resumen_departamentos["ALINEADOS"] / resumen_departamentos["TOTAL"] * 100
    ).round(1)
    resumen_departamentos["COORDS"] = resumen_departamentos["DEPARTAMENTO"].apply(
        coordenadas_departamento
    )
    resumen_departamentos = resumen_departamentos.dropna(subset=["COORDS"])
    if resumen_departamentos.empty:
        return

    resumen_departamentos["lat"] = resumen_departamentos["COORDS"].apply(lambda item: item["lat"])
    resumen_departamentos["lon"] = resumen_departamentos["COORDS"].apply(lambda item: item["lon"])

    st.markdown("### 🗺️ Mapa interactivo: intensidad Basura Cero por departamento")
    fig_map = px.scatter_mapbox(
        resumen_departamentos,
        lat="lat",
        lon="lon",
        size="TOTAL",
        size_max=45,
        color="PORCENTAJE",
        color_continuous_scale="Greens",
        hover_name="DEPARTAMENTO",
        hover_data={
            "TOTAL": True,
            "ALINEADOS": True,
            "PORCENTAJE": ":.1f",
            "lat": False,
            "lon": False,
        },
        zoom=4.2,
        center={"lat": 4.5, "lon": -74.1},
        mapbox_style="carto-positron",
    )
    fig_map.update_layout(
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
        coloraxis_colorbar={"title": "% alineadas"},
    )
    st.plotly_chart(fig_map, use_container_width=True)
    st.caption(
        "El tamaño del marcador refleja el total de negocios verdes en el departamento y el color indica el "
        "porcentaje con relación identificada al programa Basura Cero."
    )


def plot_top_sectores(df: pd.DataFrame) -> None:
    """Top 10 sectores con más negocios verdes (barra horizontal interactiva)."""
    if df.empty or "SECTOR" not in df.columns or df["SECTOR"].isna().all():
        return

    st.markdown("### 🌿 Top 10 Sectores con más Negocios Verdes")
    top_sectores = (
        df["SECTOR"].value_counts().head(10).rename_axis("SECTOR").reset_index(name="Total")
    )

    fig = px.bar(
        top_sectores.sort_values("Total"),
        x="Total",
        y="SECTOR",
        orientation="h",
        text="Total",
        color="Total",
        color_continuous_scale="Greens",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(
        xaxis_title="Número de negocios",
        yaxis_title="Sector",
        margin=dict(l=10, r=10, t=40, b=10),
        coloraxis_showscale=False,
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_tendencia_anual(df: pd.DataFrame) -> None:
    """Línea de tiempo de número de negocios verdes por año."""
    if "AÑO" not in df.columns:
        return

    st.markdown("### 📈 Tendencia anual de negocios verdes")
    df_anual = df.dropna(subset=["AÑO"])
    if df_anual.empty:
        return

    conteo = df_anual.groupby("AÑO").size().reset_index(name="Total")
    fig = px.line(
        conteo,
        x="AÑO",
        y="Total",
        markers=True,
        labels={"AÑO": "Año", "Total": "Número de registros"},
    )
    fig.update_layout(margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)


def plot_relacion_basura_cero(df: pd.DataFrame) -> None:
    """Resumen de iniciativas alineadas o no con Basura Cero + categorías."""
    if df.empty or "RELACIÓN BASURA CERO" not in df.columns:
        return

    st.markdown("### ♻️ Relación con el programa Basura Cero")
    st.markdown(
        """
        La siguiente clasificación busca identificar cómo cada iniciativa se conecta con los pilares del
        programa **Basura Cero**. Se analizan palabras clave en la descripción, sector y subsector para
        agrupar los proyectos según su enfoque.
        """
    )

    resumen_relacion = (
        df["RELACIÓN BASURA CERO"]
        .fillna("No aplica")
        .apply(
            lambda valor: (
                "Iniciativas alineadas"
                if str(valor).strip().lower() not in {"no aplica", "no disponible", ""}
                else "Sin relación identificada"
            )
        )
        .value_counts()
        .rename_axis("Relación")
        .reset_index(name="Total")
    )

    if resumen_relacion.empty:
        return

    fig_relacion = px.pie(
        resumen_relacion,
        names="Relación",
        values="Total",
        color="Relación",
        color_discrete_map={
            "Iniciativas alineadas": "#1FA88E",
            "Sin relación identificada": "#C9B79C",
        },
        hole=0.35,
    )
    fig_relacion.update_traces(
        hovertemplate=(
            "<b>%{label}</b><br>Participación: %{percent}"
            "<br>Cantidad: %{value}<extra></extra>"
        ),
        textinfo="percent+label",
        textposition="inside",
    )
    fig_relacion.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig_relacion, use_container_width=True)

    # Barras por categoría
    relacion_series = (
        df["RELACIÓN BASURA CERO"].fillna("No aplica").str.get_dummies(sep=", ").sum().sort_values(ascending=False)
    )
    if not relacion_series.empty:
        st.markdown("#### Distribución general por categoría Basura Cero")
        data = relacion_series.rename_axis("Categoría").reset_index(name="Total")
        fig_cat = px.bar(
            data.sort_values("Total"),
            x="Total",
            y="Categoría",
            orientation="h",
            text="Total",
            color="Total",
            color_continuous_scale="Greens",
        )
        fig_cat.update_traces(textposition="outside")
        fig_cat.update_layout(
            xaxis_title="Número de iniciativas",
            yaxis_title="Categoría Basura Cero",
            margin=dict(l=10, r=10, t=40, b=10),
            coloraxis_showscale=False,
        )
        st.plotly_chart(fig_cat, use_container_width=True)


def plot_autoridades(df: pd.DataFrame) -> None:
    """Barras interactivas con las autoridades ambientales con más registros."""
    if df.empty or "AUTORIDAD AMBIENTAL" not in df.columns:
        return

    st.markdown("### 🏛️ Autoridades ambientales y Basura Cero")
    st.markdown(
        """
        Conoce qué tan activa está cada autoridad ambiental en el programa y cómo se distribuyen
        las iniciativas con relación identificada a **Basura Cero**.
        """
    )

    autoridades_norm = (
        df["AUTORIDAD AMBIENTAL"].fillna("No registra").astype(str).str.strip().replace("", "No registra")
    )

    top_autoridades = (
        autoridades_norm.value_counts()
        .head(15)
        .reset_index(name="Total")
        .rename(columns={"index": "AUTORIDAD AMBIENTAL"})
    )
    top_autoridades = top_autoridades.sort_values("Total")

    if top_autoridades.empty:
        return

    fig_aut = px.bar(
        top_autoridades,
        x="Total",
        y="AUTORIDAD AMBIENTAL",
        orientation="h",
        color="Total",
        color_continuous_scale="Greens",
        text="Total",
    )
    fig_aut.update_traces(
        hovertemplate=("<b>%{y}</b><br>Total de iniciativas: %{x}<extra></extra>"),
        textposition="outside",
    )
    fig_aut.update_layout(
        coloraxis_showscale=False,
        xaxis_title="Número de iniciativas registradas",
        yaxis_title="Autoridad ambiental",
        margin=dict(l=0, r=30, t=30, b=0),
    )
    st.plotly_chart(fig_aut, use_container_width=True)
