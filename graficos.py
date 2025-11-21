# graficos.py
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import streamlit as st

from data_loader import (
    coordenadas_departamento,
    tiene_relacion_basura_cero,
)


def plot_tendencia_anual(df: pd.DataFrame) -> None:
    """Línea de tiempo: negocios registrados por año."""
    df_anual = df.dropna(subset=["AÑO"])

    if df_anual.empty:
        st.info("No hay datos válidos de 'AÑO' para mostrar la tendencia anual.")
        return

    conteo = df_anual.groupby("AÑO").size()

    fig, ax = plt.subplots(figsize=(7, 3))
    sns.lineplot(x=conteo.index, y=conteo.values, marker="o", color="#4E7F96", ax=ax)

    ax.set_title("Tendencia anual de negocios verdes", fontsize=12, weight="bold")
    ax.set_xlabel("Año")
    ax.set_ylabel("Número de registros")

    st.pyplot(fig)


def plot_mapa_basura_cero(df: pd.DataFrame) -> None:
    """Mapa de intensidad Basura Cero por departamento."""
    if df.empty or not {"DEPARTAMENTO", "RELACIÓN BASURA CERO"}.issubset(df.columns):
        return

    mapa_df = df.copy()
    relacion_normalizada = (
        mapa_df["RELACIÓN BASURA CERO"].fillna("").astype(str).str.strip().str.lower()
    )
    mapa_df["TIENE_RELACION"] = ~relacion_normalizada.isin(
        {"", "no aplica", "no disponible"}
    )

    resumen_departamentos = (
        mapa_df.groupby("DEPARTAMENTO")
        .agg(TOTAL=("DEPARTAMENTO", "size"), ALINEADOS=("TIENE_RELACION", "sum"))
        .reset_index()
    )
    resumen_departamentos["ALINEADOS"] = resumen_departamentos["ALINEADOS"].astype(int)
    resumen_departamentos["PORCENTAJE"] = (
        resumen_departamentos["ALINEADOS"] / resumen_departamentos["TOTAL"]
    ) * 100
    resumen_departamentos["PORCENTAJE"] = resumen_departamentos["PORCENTAJE"].round(1)
    resumen_departamentos["COORDS"] = resumen_departamentos["DEPARTAMENTO"].apply(
        coordenadas_departamento
    )
    resumen_departamentos = resumen_departamentos.dropna(subset=["COORDS"])

    if resumen_departamentos.empty:
        return

    resumen_departamentos["lat"] = resumen_departamentos["COORDS"].apply(
        lambda item: item["lat"]
    )
    resumen_departamentos["lon"] = resumen_departamentos["COORDS"].apply(
        lambda item: item["lon"]
    )

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
        "El tamaño del marcador refleja el total de negocios verdes en el departamento "
        "y el color indica el porcentaje con relación identificada al programa Basura Cero."
    )


def plot_top_sectores(df: pd.DataFrame) -> None:
    """Top 10 sectores con más negocios verdes."""
    if df.empty or "SECTOR" not in df.columns or df["SECTOR"].isna().all():
        st.warning(
            "La columna 'SECTOR' no está presente, está vacía o no contiene datos válidos."
        )
        return

    st.markdown("### 🌿 Top 10 Sectores con más Negocios Verdes")

    custom_palette = [
        "#E6FFF7",
        "#B2F2E8",
        "#66D1BA",
        "#1FA88E",
        "#0B5C4A",
        "#A8E55A",
        "#88C999",
        "#C9B79C",
        "#7BBF8A",
        "#9CD25B",
    ]

    top_sectores = df["SECTOR"].value_counts().head(10)

    sns.set_style("whitegrid")
    plt.rcParams["font.family"] = "Arial"

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        x=top_sectores.values,
        y=top_sectores.index,
        palette=custom_palette[: len(top_sectores)],
        edgecolor="#0B5C4A",
        ax=ax,
    )

    for container in ax.containers:
        ax.bar_label(container, fmt="%d", padding=3, fontsize=9, color="#0B5C4A")

    ax.set_title(
        "Top 10 Sectores con más Negocios Verdes",
        fontsize=12,
        weight="bold",
        color="#0B5C4A",
        pad=10,
    )
    ax.set_xlabel("Número de Negocios", fontsize=10, color="#0B5C4A")
    ax.set_ylabel("Sector", fontsize=10, color="#0B5C4A")
    sns.despine(left=True, bottom=True)
    plt.tight_layout()

    st.pyplot(fig)


def plot_relacion_basura_cero(df: pd.DataFrame) -> None:
    """Gráficos relacionados con la relación al programa Basura Cero."""
    if (
        df.empty
        or "RELACIÓN BASURA CERO" not in df.columns
        or df["RELACIÓN BASURA CERO"].isna().all()
    ):
        return

    st.markdown("### ♻️ Relación con el programa Basura Cero")
    st.markdown(
        """
        La siguiente clasificación busca identificar cómo cada iniciativa se conecta con los pilares del
        programa **Basura Cero**. Se analizan palabras clave en la descripción, sector y subsector para
        agrupar los proyectos según su enfoque.
        """
    )

    # Pie general alineadas vs no
    resumen_relacion = (
        df["RELACIÓN BASURA CERO"]
        .fillna("No aplica")
        .apply(
            lambda valor: (
                "Iniciativas alineadas"
                if str(valor).strip().lower()
                not in {"no aplica", "no disponible", ""}
                else "Sin relación identificada"
            )
        )
        .value_counts()
        .rename_axis("Relación")
        .reset_index(name="Total")
    )

    if not resumen_relacion.empty:
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
        df["RELACIÓN BASURA CERO"]
        .fillna("No aplica")
        .str.get_dummies(sep=", ")
        .sum()
        .sort_values(ascending=False)
    )

    if not relacion_series.empty:
        st.markdown("#### Distribución general por categoría")
        fig_rel, ax_rel = plt.subplots(figsize=(7, 4))
        sns.barplot(
            x=relacion_series.values,
            y=relacion_series.index,
            palette="Greens",
            edgecolor="#0B5C4A",
            ax=ax_rel,
        )
        ax_rel.set_xlabel("Número de iniciativas", fontsize=10, color="#0B5C4A")
        ax_rel.set_ylabel("Categoría Basura Cero", fontsize=10, color="#0B5C4A")
        ax_rel.set_title(
            "Iniciativas clasificadas por su relación con Basura Cero",
            fontsize=12,
            weight="bold",
            color="#0B5C4A",
        )
        for container in ax_rel.containers:
            ax_rel.bar_label(
                container,
                fmt="%d",
                padding=3,
                fontsize=9,
                color="#0B5C4A",
            )
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        st.pyplot(fig_rel)

    # Heatmap por región
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
        relacion_exploded["RELACIÓN BASURA CERO"] = (
            relacion_exploded["RELACIÓN BASURA CERO"].astype(str).str.strip()
        )
        relacion_exploded = relacion_exploded[
            relacion_exploded["RELACIÓN BASURA CERO"].str.lower() != "no aplica"
        ]

        if not relacion_exploded.empty:
            relacion_por_region = (
                relacion_exploded.groupby(["REGIÓN", "RELACIÓN BASURA CERO"])
                .size()
                .reset_index(name="TOTAL")
            )

            if not relacion_por_region.empty:
                st.markdown("#### Intensidad de categorías por región")
                pivot = relacion_por_region.pivot(
                    index="REGIÓN",
                    columns="RELACIÓN BASURA CERO",
                    values="TOTAL",
                ).fillna(0)

                fig_heat, ax_heat = plt.subplots(
                    figsize=(8, max(3, 0.5 * len(pivot.index)))
                )
                sns.heatmap(
                    pivot,
                    cmap="Greens",
                    annot=True,
                    fmt=".0f",
                    linewidths=0.5,
                    cbar_kws={"label": "Número de iniciativas"},
                    ax=ax_heat,
                )
                ax_heat.set_xlabel(
                    "Categoría Basura Cero", color="#0B5C4A", fontsize=10
                )
                ax_heat.set_ylabel("Región", color="#0B5C4A", fontsize=10)
                ax_heat.set_title(
                    "Mapa de calor: enfoques Basura Cero por región",
                    color="#0B5C4A",
                    fontsize=12,
                    weight="bold",
                    pad=10,
                )
                plt.tight_layout()
                st.pyplot(fig_heat)


def plot_autoridades(df: pd.DataFrame) -> None:
    """Gráficos de autoridades ambientales y Basura Cero."""
    if "AUTORIDAD AMBIENTAL" not in df.columns or df["AUTORIDAD AMBIENTAL"].isna().all():
        return

    st.markdown("### 🏛️ Autoridades ambientales y Basura Cero")
    st.markdown(
        """
    Conoce qué tan activa está cada autoridad ambiental en el programa y cómo se distribuyen
    las iniciativas con relación identificada a **Basura Cero**.
    """
    )

    autoridades_norm = (
        df["AUTORIDAD AMBIENTAL"]
        .fillna("No registra")
        .astype(str)
        .str.strip()
        .replace("", "No registra")
    )

    # Top 15 autoridades por número de iniciativas
    top_autoridades = (
        autoridades_norm.value_counts()
        .head(15)
        .reset_index(name="Total")
        .rename(columns={"index": "AUTORIDAD AMBIENTAL"})
        .sort_values("Total")
    )

    if not top_autoridades.empty:
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
            hovertemplate="<b>%{y}</b><br>Total de iniciativas: %{x}<extra></extra>",
            textposition="outside",
        )
        fig_aut.update_layout(
            coloraxis_showscale=False,
            xaxis_title="Número de iniciativas registradas",
            yaxis_title="Autoridad ambiental",
            margin=dict(l=0, r=30, t=30, b=0),
        )
        st.plotly_chart(fig_aut, use_container_width=True)
        st.caption(
            "Las barras muestran las autoridades con mayor número de registros en el dataset."
        )

    # Distribución alineadas vs no alineadas por autoridad
    autoridades_df = df.assign(
        AUTORIDAD_NORMALIZADA=autoridades_norm,
        ESTADO_ALINEACIÓN=df["RELACIÓN BASURA CERO"].apply(
            lambda valor: (
                "Iniciativas alineadas" if tiene_relacion_basura_cero(valor) else
                "Sin relación identificada"
            )
        ),
    )

    principales_autoridades = top_autoridades["AUTORIDAD AMBIENTAL"].tolist()

    distribucion_autoridad = (
        autoridades_df[
            autoridades_df["AUTORIDAD_NORMALIZADA"].isin(principales_autoridades)
        ]
        .groupby(["AUTORIDAD_NORMALIZADA", "ESTADO_ALINEACIÓN"])
        .size()
        .reset_index(name="Total")
    )

    if distribucion_autoridad.empty:
        return

    distribucion_autoridad["Porcentaje"] = (
        distribucion_autoridad["Total"]
        / distribucion_autoridad.groupby("AUTORIDAD_NORMALIZADA")["Total"].transform(
            "sum"
        )
        * 100
    )

    orden_autoridades = (
        top_autoridades.sort_values("Total", ascending=False)["AUTORIDAD AMBIENTAL"].tolist()
    )

    fig_aut_stack = px.bar(
        distribucion_autoridad,
        x="Total",
        y="AUTORIDAD_NORMALIZADA",
        color="ESTADO_ALINEACIÓN",
        orientation="h",
        category_orders={"AUTORIDAD_NORMALIZADA": orden_autoridades},
        color_discrete_map={
            "Iniciativas alineadas": "#1FA88E",
            "Sin relación identificada": "#C9B79C",
        },
        custom_data=["Porcentaje"],
    )
    fig_aut_stack.update_traces(
        hovertemplate=(
            "<b>%{y}</b><br>%{color}<br>Total: %{x}"
            "<br>Participación: %{customdata[0]:.1f}%<extra></extra>"
        )
    )
    fig_aut_stack.update_layout(
        barmode="stack",
        xaxis_title="Número de iniciativas",
        yaxis_title="Autoridad ambiental",
        legend_title="Estado de la relación",
        margin=dict(l=0, r=30, t=30, b=0),
    )
    st.plotly_chart(fig_aut_stack, use_container_width=True)
    st.caption(
        "El gráfico apilado indica cuántas iniciativas de cada autoridad tienen relación identificada "
        "con Basura Cero frente a las que aún no muestran esa alineación."
    )
