# sections/insights.py

import streamlit as st

# ============================================================
#   🌿 Tarjeta de Insight (Diseño Premium)
# ============================================================

def insight_card(title, value, description, icon="📌", color="#E8F5E9"):
    """
    Crea una tarjeta estilizada para presentar un insight clave.
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
            <h2 style="margin:6px 0; font-size:26px; color:#1B5E20;">
                {value}
            </h2>
            <p style="font-size:16px; color:#33691E; margin-top:6px;">
                {description}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
#   🌱 FUNCIÓN PRINCIPAL — SIN GRÁFICOS
# ============================================================

def render_insights(df):
    """
    Renderiza la sección de Insights sin gráficos,
    usando tarjetas premium, texto y storytelling.
    """

    st.title("🔍 Insights del Análisis de Negocios Verdes")

    st.markdown("""
    Esta sección presenta los **principales insights** obtenidos del análisis de la base de datos de 
    Negocios Verdes en Colombia. Se destacan patrones territoriales, tendencias sectoriales y 
    oportunidades estratégicas para fortalecer la economía circular y la transición energética.
    """)

    st.divider()

    # ============================================================
    # INSIGHT 1 – REGIÓN ANDINA LIDERA
    # ============================================================

    region_count = df["REGIÓN"].value_counts().reset_index()
    region_count.columns = ["Región", "Cantidad"]
    top_region = region_count.iloc[0]

    insight_card(
        title="La región Andina lidera en negocios verdes",
        value=f"{top_region['Cantidad']} negocios",
        description=(
            "Es la región con mayor actividad verde registrada. "
            "Su liderazgo está asociado a la concentración urbana, infraestructura económica "
            "y apoyo institucional al emprendimiento sostenible."
        ),
        icon="🌱"
    )

    st.divider()

    # ============================================================
    # INSIGHT 2 – SECTOR MÁS FUERTE
    # ============================================================

    sector_count = df["SECTOR"].value_counts().reset_index()
    sector_count.columns = ["Sector", "Cantidad"]
    top_sector = sector_count.iloc[0]

    insight_card(
        title="El sector más representativo del país",
        value=top_sector['Sector'],
        description=(
            "Este sector agrupa la mayor cantidad de negocios verdes, reflejando una tendencia "
            "hacia economía circular, bioproductos y soluciones ambientales basadas en recursos naturales."
        ),
        icon="🏆",
        color="#E3F2FD"
    )

    st.divider()

    # ============================================================
    # INSIGHT 3 – LA MIEL COMO PRODUCTO DESTACADO
    # ============================================================

    productos_miel = df["DESCRIPCIÓN"].str.contains("miel", case=False, na=False).sum()
    porcentaje_miel = round((productos_miel / len(df)) * 100, 2)

    insight_card(
        title="La miel es un producto ecológico recurrente",
        value=f"{productos_miel} negocios",
        description=(
            f"La miel representa el {porcentaje_miel}% del total. "
            "Es un producto atractivo porque es natural, fácil de certificar, "
            "y su producción está asociada a la conservación de la biodiversidad y la polinización."
        ),
        icon="🍯",
        color="#FFF3E0"
    )

    st.divider()

    # ============================================================
    # INSIGHT 4 – BRECHA EN ENERGÍAS RENOVABLES
    # ============================================================

    energias = df[df["SECTOR"].str.contains("energ", case=False, na=False)]
    cant_energias = len(energias)
    porcentaje_energias = round((cant_energias / len(df)) * 100, 2)

    insight_card(
        title="Energías renovables: sector poco aprovechado",
        value=f"{cant_energias} negocios",
        description=(
            f"Solo el {porcentaje_energias}% de los negocios corresponden a energías renovables. "
            "Esto evidencia una oportunidad importante para innovar y fortalecer proyectos de "
            "transición energética, especialmente en territorios rurales."
        ),
        icon="🔌",
        color="#E8EAF6"
    )

    st.divider()

    # ============================================================
    # RESUMEN FINAL
    # ============================================================

    st.header("📊 Resumen general de hallazgos")

    st.markdown("""
    ### 🟢 Tendencias principales
    - La región **Andina** concentra la mayor parte de negocios verdes.
    - Los sectores más fuertes son **aprovechamiento de residuos**, **bioproductos** y **agroecología**.
    - La **miel** se consolida como producto natural destacado.

    ### 🔵 Oportunidades emergentes
    - Bajo número de negocios en **energías renovables**, lo que abre un campo de innovación.
    - Alto potencial para encadenamientos productivos sostenibles.

    ### 🟡 Brechas identificadas
    - Regiones como Amazonía, Orinoquía y Pacífico están subrepresentadas.
    - Persisten desafíos en financiamiento, conectividad y asistencia técnica.

    """)

    st.success("✨ Sección de Insights cargada correctamente (versión sin gráficas).")
