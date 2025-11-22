import pandas as pd
import plotly.express as px
import streamlit as st

from data_loader import coordenadas_departamento, tiene_relacion_basura_cero


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


def plot_mapa_basura_cero(df: pd.DataFrame) -> None:
    if df.empty or not {"DEPARTAMENTO", "RELACIÓN BASURA CERO"}.issubset(df.columns):
        st.info("No hay datos suficientes para construir el mapa.")
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
        resumen_departamentos["ALINEADOS"] / resumen_departamentos["TOTAL"] * 100
    )

    resumen_departamentos["COORDS"] = resumen_departamentos["DEPARTAMENTO"].apply(
        coordenadas_departamento
    )
    resumen_departamentos = resumen_departamentos.dropna(subset=["COORDS"])

    if resumen_departamentos.empty:
        st.info("No hay coordenadas disponibles para los departamentos del mapa.")
        return

    resumen_departamentos["lat"] = resumen_departamentos["COORDS"].apply(
        lambda c: c["lat"]
    )
    resumen_departamentos["lon"] = resumen_departamentos["COORDS"].apply(
        lambda c: c["lon"]
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
            "PORCENTAJE": True,
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
    if df.empty or "SECTOR" not in df.columns or df["SECTOR"].isna().all():
        st.warning(
            "La columna 'SECTOR' no está presente, está vacía o no contiene datos válidos."
        )
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
        margin=dict(l=0, r=0, t=30, b=0),
        coloraxis_showscale=False,
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_relacion_basura_cero(df: pd.DataFrame) -> None:
    if (
        df.empty
        or "RELACIÓN BASURA CERO" not in df.columns
        or df["RELACIÓN BASURA CERO"].isna().all()
    ):
        st.info("No hay información suficiente sobre la relación con Basura Cero.")
        return

    st.markdown("### ♻️ Relación con el programa Basura Cero")

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

    relacion_series = (
        df["RELACIÓN BASURA CERO"]
        .fillna("No aplica")
        .str.get_dummies(sep=", ")
        .sum()
        .sort_values(ascending=False)
    )

    if not relacion_series.empty:
        st.markdown("#### Distribución general por categoría")
        categorias = relacion_series.reset_index()
        categorias.columns = ["Categoría", "Total"]

        fig_rel = px.bar(
            categorias,
            x="Total",
            y="Categoría",
            orientation="h",
            color="Total",
            color_continuous_scale="Greens",
            text="Total",
        )
        fig_rel.update_traces(textposition="outside")
        fig_rel.update_layout(
            xaxis_title="Número de iniciativas",
            yaxis_title="Categoría Basura Cero",
            margin=dict(l=0, r=0, t=30, b=0),
            coloraxis_showscale=False,
        )
        st.plotly_chart(fig_rel, use_container_width=True)

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

                fig_heat = px.imshow(
                    pivot,
                    color_continuous_scale="Greens",
                    text_auto=True,
                    aspect="auto",
                    labels=dict(color="Número de iniciativas"),
                    title="Mapa de calor: enfoques Basura Cero por región",
                )

                st.plotly_chart(fig_heat, use_container_width=True)


def plot_autoridades(df: pd.DataFrame) -> None:
    if "AUTORIDAD AMBIENTAL" not in df.columns or df["AUTORIDAD AMBIENTAL"].isna().all():
        st.info("No hay datos sobre autoridades ambientales en el dataset.")
        return

    st.markdown("### 🏛️ Autoridades ambientales y Basura Cero")

    autoridades_norm = (
        df["AUTORIDAD AMBIENTAL"]
        .fillna("No registra")
        .astype(str)
        .str.strip()
        .replace("", "No registra")
    )

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
