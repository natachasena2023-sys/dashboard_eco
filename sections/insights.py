# sections/insights.py

import streamlit as st
import plotly.express as px


# ============================================================
#   🌿 Tarjeta de Insight (estilo premium)
# ============================================================

def insight_card(title, value, description, icon="📌", color="#E8F5E9"):
    """
    Crea una tarjeta visual para presentar un insight clave.
    """
    st.markdown(
        f"""
        <div style="
            background:{color};
            padding:18px 20px;
            border-radius:16px;
            margin-bottom:18px;
            border-left:6px solid #2E7D32;
        ">
            <h3 style="margin:0; font-size:22px;">{icon} {title}</h3>
            <h2 style="margin:5px 0 10px 0; font-size:28px; color:#1B5E20;">
                {value}
            </h2>
            <p style="font-size:16px; color:#33691E; margin:0;">
                {description}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
#   🌱 FUNCIÓN PRINCIPAL — Adaptada: render_insights(df)
# ============================================================

def render_insights(df):
    """
    Renderiza la sección de Insights dentro del Dashboard.
    Usa el mismo estilo de las secciones render_home, render_mapa, render_faq.
    """

    st.title("🔍 Insights del Análisis de Negocios Verdes")

    st.markdown("""
    Esta sección resume los **hallazgos clave** del análisis exploratorio realizado sobre los 
    Negocios Verdes en Colombia, destacando patrones territoriales, sectores predominantes y 
    oportunidades emergentes relacionadas con economía circular y transición energética.
    """)

    st.divider()

    # ============================================================
    # 1️⃣ REGIONES CON MAYOR PARTICIPACIÓN
    # ============================================================

    st.header("🌎 1. Regiones con mayor presencia de negocios verdes")

    region_count = df["REGIÓN"].value_counts().reset_index()
    region_count.columns = ["Región", "Cantidad"]

    
    st.plotly_chart( use_container_width=True)

    top_region = region_count.iloc[0]

    insight_card(
        title="La región Andina lidera en negocios verdes",
        value=f"{top_region['Cantidad']} negocios",
        description=(
            "La región Andina concentra la mayor cantidad de negocios verdes, impulsada por la "
            "densidad poblacional, infraestructura y apoyo institucional."
        ),
        icon="🌱"
    )

    st.divider()

    # ============================================================
    # 2️⃣ SECTORES MÁS REPRESENTATIVOS
    # ============================================================

    st.header("🏭 2. Sectores predominantes")

    sector_count = df["SECTOR"].value_counts().reset_index()
    sector_count.columns = ["Sector", "Cantidad"]

    fig_sector = px.pie(
        sector_count,
        names="Sector",
        values="Cantidad",
        hole=0.45,
        title="Participación por sector",
    )
    st.plotly_chart(fig_sector, use_container_width=True)

    top_sector = sector_count.iloc[0]

    insight_card(
        title="El sector más representativo del país",
        value=top_sector['Sector'],
        description=(
            "Este sector reúne la mayor proporción de negocios verdes, mostrando la fuerza de la "
            "economía circular, bioproductos y soluciones ambientales."
        ),
        icon="🏆",
        color="#E3F2FD"
    )

    st.divider()

    # ============================================================
    # 3️⃣ LA MIEL COMO PRODUCTO DESTACADO
    # ============================================================

    st.header("🍯 3. La miel como producto ecológico destacado")

    productos_miel = df["DESCRIPCIÓN"].str.contains("miel", case=False, na=False).sum()
    porcentaje_miel = round((productos_miel / len(df)) * 100, 2)

    insight_card(
        title="Alta presencia de negocios basados en miel",
        value=f"{productos_miel} negocios",
        description=(
            f"La miel representa el {porcentaje_miel}% del total. Es uno de los productos más "
            "populares por su bajo impacto ambiental, narrativa natural y alto valor comercial."
        ),
        icon="🍯",
        color="#FFF3E0"
    )

    st.divider()

    # ============================================================
    # 4️⃣ ENERGÍAS RENOVABLES — OPORTUNIDAD EMERGENTE
    # ============================================================

    st.header("⚡ 4. Energías renovables: sector poco explotado")

    energias = df[df["SECTOR"].str.contains("energ", case=False, na=False)]
    cant_energias = len(energias)
    porcentaje_energias = round((cant_energias / len(df)) * 100, 2)

    insight_card(
        title="Baja participación en energías renovables",
        value=f"{cant_energias} negocios",
        description=(
            f"Los negocios de energías renovables representan solo el {porcentaje_energias}% del "
            "total, revelando un espacio ideal para inversión, innovación y transición energética."
        ),
        icon="🔌",
        color="#E8EAF6"
    )

    st.divider()

    # ============================================================
    # 5️⃣ RESUMEN GENERAL
    # ============================================================

    st.header("📊 5. Resumen general de hallazgos")

    st.markdown("""
    ### 🟢 Tendencias principales
    - La región **Andina** lidera la actividad verde.
    - Sectores de **aprovechamiento de residuos** y **bioproductos** dominan el ecosistema.
    - La **miel** destaca como producto natural y recurrente.

    ### 🔵 Oportunidades emergentes
    - Bajo desarrollo del sector de **energías renovables**.
    - Creciente preferencia por productos orgánicos y sostenibles.

    ### 🟡 Brechas identificadas
    - Regiones como Amazonía, Orinoquía y Pacífico están subrepresentadas.
    - Persisten desafíos de acceso a mercados, tecnología y financiación.
    """)

    st.success("✨ Sección de Insights cargada correctamente.")


# ============================================================
# FIN DEL ARCHIVO
# ============================================================
