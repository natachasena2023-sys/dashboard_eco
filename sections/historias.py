# sections/historias.py

import streamlit as st


def story_card(title, description, icon="🌿", color="#E8F5E9"):
    """
    Tarjeta premium para historias reales.
    """
    st.markdown(
        f"""
        <div style="
            background:{color};
            padding:18px 22px;
            border-radius:18px;
            margin-bottom:18px;
            border-left:6px solid #1B5E20;
        ">
            <h3 style="margin:0; font-size:24px;">{icon} {title}</h3>
            <p style="font-size:16px; color:#2E7D32; margin-top:8px;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
#    SECCIÓN PRINCIPAL — HISTORIAS DE NEGOCIOS VERDES
# ============================================================

def render_historias():
    st.title("📽️ Historias Reales de Negocios Verdes")
    st.markdown("""
    En esta sección te mostramos casos reales de negocios verdes en Colombia que están 
    transformando los territorios, generando empleo, reduciendo residuos y aportando a 
    la economía circular.  
    """)

    st.divider()

    # ============================================================
    # 1. RUTA RECICLO
    # ============================================================

    st.header("♻️ Caso real: Ruta Reciclo")

    st.markdown("""
    **Ruta Reciclo** es una iniciativa real que impulsa la economía circular mediante 
    la recolección, transformación y aprovechamiento de residuos reciclables en Colombia.  
    Su trabajo conecta hogares, empresas, recicladores y centros de acopio para crear un 
    sistema más eficiente y sostenible.
    """)

    # VIDEO DE YOUTUBE INCRUSTADO
    st.video("https://youtu.be/g_ObTtFoZN4?si=yrf--NsswpdQf3Uj")

    story_card(
        title="¿Qué hace Ruta Reciclo?",
        icon="🚛",
        description=(
            "Recolecta materiales reciclables por rutas programadas, conectando a ciudadanos, "
            "recicladores de oficio y empresas. Su modelo fortalece el reciclaje inclusivo, "
            "reduce la cantidad de residuos que llegan a rellenos sanitarios y promueve la "
            "educación ambiental."
        )
    )

    story_card(
        title="Impacto ambiental",
        icon="🌎",
        description=(
            "Ruta Reciclo contribuye directamente a la reducción de residuos, el aprovechamiento de "
            "materiales y la disminución de emisiones asociadas a la disposición final. "
            "Cada kilo de material recuperado vuelve al ciclo productivo."
        )
    )

    story_card(
        title="Impacto social",
        icon="🤝",
        color="#FFF3E0",
        description=(
            "El proyecto genera inclusión social, dignificación laboral y mejores condiciones para "
            "recicladores de oficio. Fortalece su ingreso y formalización dentro del sistema."
        )
    )

    story_card(
        title="Conexión con Basura Cero",
        icon="🔗",
        color="#E3F2FD",
        description=(
            "Ruta Reciclo es un ejemplo claro de cómo los negocios verdes pueden hacer posible la "
            "visión de Basura Cero: menos residuos, más aprovechamiento y más educación ambiental."
        )
    )

    st.success("✔ Caso Ruta Reciclo agregado exitosamente al dashboard.")
