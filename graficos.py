# graficos.py — Versión 100% interactiva con Plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

from data_loader import (
    coordenadas_departamento,
    tiene_relacion_basura_cero,
)


# =============================================================================
# 1. Tendencia anual (INTERACTIVA)
# =============================================================================
def plot_tendencia_anual(df: pd.DataFrame) -> None:
    df_anual = df.dropna(subset=["AÑO"])
    if df_anual.empty:
        st.info("No hay datos válidos de 'AÑO' para mostrar la tendencia anual.")
        return

    conteo = df_anual.groupby("AÑO").size().reset_index(name="Total")

    fig = px.line(
        conteo,
        x="AÑO",
        y="Total",
        markers=True,
        title="📈 Tendencia anual de negocios verdes",
    )

    fig.update_traces(line_color="#1FA88E")
    fig.update_layout(
        xaxis_title="Año",
        yaxis_title="Número de registros",
        margin=dict(l=0, r=0, t=40, b=0),
    )

    st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# 2. Mapa interactivo Basura Cero
# =============================================================================
def plot_mapa_basura_cero(df: pd.DataFrame) -> None:
    if df.empty or not {"DEPARTAMENTO", "RELACIÓN BASURA CERO"}.issubset(df.columns):
        return

    mapa_df = df.copy()
    relacion_normalizada = (
        mapa_df["RELACIÓN BASURA CERO"]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.lower()
    )
    mapa_df["TIENE_RELACION"] = ~relacion_normalizada.isin(
        {"", "no aplica", "no disponible"}
    )

    resumen_departamentos = (
        mapa_df.groupby("DEPARTAMENTO")
        .agg(TOTAL=("DEPARTAMENTO", "size"), ALINEADOS=("TIENE_RELACION", "sum"))
        .reset_index()
    )

    resumen_departamentos["PORCENTAJE"] = (
        resumen_departamentos["ALINEADOS"] / resumen_departamentos["TOTAL"]
    ) * 100

    resumen_departamentos["COORDS"] = resumen_departamentos["DEPARTAMENTO"].apply(
        coordenadas_departamento
    )
    resumen_departamentos = resumen_departamentos.dropna(subset=["COORDS"])

    resumen_departamentos["lat"] = resumen_departamentos["COORDS"].apply(lambda c: c["lat"])
    resumen_departamentos["lon"] = resumen_departamentos["COORDS"].apply(lambda c: c["lon"])

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
        hover_data={"TOTAL": True, "ALINEADOS": True, "PORCENTAJE": True},
        zoom=4.2,
        center={"lat": 4.5, "lon": -74.1},
        mapbox_style="carto-positron",
    )

    fig_map.update_layout(
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
        coloraxis_colorbar={"title": "% alineadas"},
    )

    st.plotly_chart(fig_map, use_container_width=True)


# =============================================================================
# 3. Top sectores (INTERACTIVO)
# =============================================================================
def plot_top_sectores(df: pd.DataFrame) -> None:
    if df.empty or "SECTOR" not in df.columns or df["SECTOR"].isna().all():
        st.warning("La columna 'SECTOR' no contiene datos válidos.")
        return

    st.markdown("### 🌿 Top 10 Sectores con más Negocios Verdes")

    conteo = df["SECTOR"].value_counts().head(10).reset_index()
    conteo.columns = ["SECTOR", "Total"]

    fig = px.bar(
        conteo,
        x="Total",
        y="SECTOR",
        orientation="h",
        color="Total",
        color_continuous_scale="Greens",
        text="Total",
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(
        xaxis_title="Número de negocios",
        yaxis_title="Sector",
        coloraxis_showscale=False,
        margin=dict(l=0, r=0, t=30, b=0),
    )

    st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# 4. Relación Basura Cero (INTERACTIVO)
# =============================================================================
def plot_relacion_basura_cero(df: pd.DataFrame) -> None:
    if "RELACIÓN BASURA CERO" not in df.columns:
        return

    st.markdown("### ♻️ Relación con el programa Basura Cero")

    # Pie alineadas vs no
    resumen_relacion = (
        df["RELACIÓN BASURA CERO"]
        .fillna("No aplica")
        .apply(
            lambda v: (
                "Iniciativas alineadas"
                if str(v).strip().lower() not in {"no aplica", "no disponible", ""}
                else "Sin relación identificada"
            )
        )
        .value_counts()
        .reset_index()
    )
    resumen_relacion.columns = ["Relación", "Total"]

    fig_relacion = px.pie(
        resumen_relacion,
        names="Relación",
        values="Total",
        hole=0.35,
        color="Relación",
        color_discrete_map={
            "Iniciativas alineadas": "#1FA88E",
            "Sin relación identificada": "#C9B79C",
        },
    )

    fig_relacion.update_traces(
        textinfo="percent+label",
        hovertemplate="<b>%{label}</b><br>Cantidad: %{value}<br>%{percent}<extra></extra>",
    )

    st.plotly_chart(fig_relacion, use_container_width=True)

    # Barras por categorías
    relacion_series = (
        df["RELACIÓN BASURA CERO"]
        .fillna("No aplica")
        .str.get_dummies(sep=", ")
        .sum()
        .sort_values(ascending=False)
    )

    if not relacion_series.empty:
        categorias = relacion_series.reset_index()
        categorias.columns = ["Categoría", "Total"]

        fig_cat = px.bar(
            categorias,
            x="Total",
            y="Categoría",
            orientation="h",
            color="Total",
            color_continuous_scale="Greens",
            text="Total",
        )

        fig_cat.update_traces(textposition="outside")
        fig_cat.update_layout(
            margin=dict(l=0, r=0, t=40, b=0),
            xaxis_title="Número de iniciativas",
            yaxis_title="Categoría Basura Cero",
            coloraxis_showscale=False,
        )

        st.plotly_chart(fig_cat, use_container_width=True)

    # Heatmap por región (INTERACTIVO)
    if "REGIÓN" in df.columns:
        relacion_exploded = (
            df.assign(
                **{
                    "RELACIÓN BASURA CERO": df["RELACIÓN BASURA CERO"]
                    .fillna("No aplica")
                    .str.split(", ")
                }
            )
            .explode("RELACIÓN BASURA CERO")
        )

        relacion_exploded = relacion_exploded[
            relacion_exploded["RELACIÓN BASURA CERO"].str.lower() != "no aplica"
        ]

        if not relacion_exploded.empty:
            tabla = (
                relacion_exploded.groupby(["REGIÓN", "RELACIÓN BASURA CERO"])
                .size()
                .reset_index(name="TOTAL")
                .pivot(index="REGIÓN", columns="RELACIÓN BASURA CERO", values="TOTAL")
                .fillna(0)
            )

            fig_heat = px.imshow(
                tabla,
                text_auto=True,
                aspect="auto",
                color_continuous_scale="Greens",
                labels=dict(color="Número de iniciativas"),
                title="🔥 Mapa de calor: categorías Basura Cero por región",
            )

            st.plotly_chart(fig_heat, use_container_width=True)


# =============================================================================
# 5. Autoridades ambientales (INTERACTIVO)
# =============================================================================
def plot_autoridades(df: pd.DataFrame) -> None:
    if "AUTORIDAD AMBIENTAL" not in df.columns:
        return

    st.markdown("### 🏛️ Autoridades ambientales y Basura Cero")

    autoridades_norm = (
        df["AUTORIDAD AMBIENTAL"]
        .fillna("No registra")
        .astype(str)
        .str.strip()
        .replace("", "No registra")
    )

    # Top 15
    top_aut = (
        autoridades_norm.value_counts()
        .head(15)
        .reset_index()
        .rename(columns={"index": "AUTORIDAD", "AUTORIDAD AMBIENTAL": "Total"})
    )

    fig_aut = px.bar(
        top_aut,
        x="Total",
        y="AUTORIDAD",
        orientation="h",
        color="Total",
        color_continuous_scale="Greens",
        text="Total",
    )

    fig_aut.update_traces(textposition="outside")
    fig_aut.update_layout(
        margin=dict(l=0, r=30, t=30, b=0),
        coloraxis_showscale=False,
        xaxis_title="Número de iniciativas",
        yaxis_title="Autoridad ambiental",
    )

    st.plotly_chart(fig_aut, use_container_width=True)

    # Barras apiladas (alineadas vs no)
    autoridades_df = df.assign(
        AUT_NORM=autoridades_norm,
        ESTADO_ALINEACIÓN=df["RELACIÓN BASURA CERO"].apply(
            lambda v: (
                "Iniciativas alineadas" if tiene_relacion_basura_cero(v)
                else "Sin relación identificada"
            )
        ),
    )

    principales = top_aut["AUTORIDAD"].tolist()

    distrib = (
        autoridades_df[autoridades_df["AUT_NORM"].isin(principales)]
        .groupby(["AUT_NORM", "ESTADO_ALINEACIÓN"])
        .size()
        .reset_index(name="Total")
    )

    fig_stack = px.bar(
        distrib,
        x="Total",
        y="AUT_NORM",
        color="ESTADO_ALINEACIÓN",
        orientation="h",
        color_discrete_map={
            "Iniciativas alineadas": "#1FA88E",
            "Sin relación identificada": "#C9B79C",
        },
    )

    fig_stack.update_layout(
        barmode="stack",
        margin=dict(l=0, r=30, t=30, b=0),
        xaxis_title="Número de iniciativas",
        yaxis_title="Autoridad ambiental",
        legend_title="Estado",
    )

    st.plotly_chart(fig_stack, use_container_width=True)