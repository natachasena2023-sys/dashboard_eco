# sections/historias.py

import streamlit as st


# ============================================================
#   Tarjeta de presentación premium
# ============================================================

def story_card(title, description, icon="🌿", color="#E8F5E9"):
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
#   SECCIÓN COMPLETA – HISTORIAS REALES DE NEGOCIOS VERDES
# ============================================================

def render_historias():

    st.title("📽️ Historias Reales de Negocios Verdes")
    st.markdown("""
    Estos casos reales muestran cómo los emprendimientos colombianos están transformando 
    residuos en oportunidades ambientales, sociales y económicas.
    """)

    st.divider()

    # ============================================================
    # 1. RUTA RECICLO
    # ============================================================

    st.header("♻️ Caso 1: Ruta Reciclo")

    st.video("https://youtu.be/g_ObTtFoZN4?si=yrf--NsswpdQf3Uj")

    story_card(
        title="¿Qué hace Ruta Reciclo?",
        icon="🚛",
        description=(
            "Recolecta materiales reciclables por rutas programadas, conectando a hogares, "
            "empresas y recicladores de oficio. Su modelo impulsa el reciclaje inclusivo y "
            "la educación ambiental."
        )
    )

    story_card(
        title="Impacto ambiental",
        icon="🌎",
        description=(
            "Reduce residuos enviados a rellenos, recupera materiales y fortalece la economía circular."
        )
    )

    story_card(
        title="Impacto social",
        icon="🤝",
        color="#FFF3E0",
        description=(
            "Dignifica el trabajo de los recicladores, mejora sus ingresos y los vincula a cadenas formales."
        )
    )

    st.divider()

    # ============================================================
    # 2. RECICLARTE
    # ============================================================

    st.header("🎨 Caso 2: Reciclarte (Arte con materiales reciclados)")

    story_card(
        title="¿Qué hace Reciclarte?",
        icon="🧑‍🎨",
        description=(
            "Transforma residuos como vidrio, plástico, cartón y metal en piezas de arte, decoración "
            "y mobiliario. El arte se convierte en un vehículo para educar sobre sostenibilidad."
        )
    )

    story_card(
        title="Impacto ambiental",
        icon="♻️",
        description=(
            "Recupera materiales que normalmente terminarían en ríos o rellenos sanitarios."
        )
    )

    story_card(
        title="Impacto social",
        icon="🎭",
        color="#FFF3E0",
        description=(
            "Promueve el arte local, involucra comunidades vulnerables y educa sobre reciclaje creativo."
        )
    )

    st.divider()

    # ============================================================
    # 3. BOTELLAS DE AMOR
    # ============================================================

    st.header("🧱 Caso 3: Botellas de Amor")

    story_card(
        title="¿Qué hace Botellas de Amor?",
        icon="🧴",
        description=(
            "Recolecta plásticos flexibles (que normalmente no tienen reciclaje comercial) para usarlos "
            "como materia prima en la fabricación de madera plástica para viviendas, mobiliario urbano "
            "y parques infantiles."
        )
    )

    story_card(
        title="Innovación",
        icon="🧪",
        color="#E3F2FD",
        description=(
            "Su modelo convierte materiales sin valor comercial en productos duraderos y útiles para comunidades."
        )
    )

    story_card(
        title="Impacto comunitario",
        icon="🏘️",
        description=(
            "Ayuda a construir viviendas, parques y mobiliario ecológico para poblaciones necesitadas."
        )
    )

    st.divider()

    # ============================================================
    # 4. FIBRAS RECICLADAS – TEXTIL SOSTENIBLE
    # ============================================================

    st.header("🧵 Caso 4: Textiles hechos con fibras recicladas")

    story_card(
        title="¿Qué hacen estos emprendimientos?",
        icon="👗",
        description=(
            "Transforman botellas PET y desechos textiles en fibras para fabricar ropa, bolsos y telas "
            "sostenibles, reduciendo el impacto de la industria textil."
        )
    )

    story_card(
        title="Problema que resuelven",
        icon="⚠️",
        description=(
            "El sector textil es uno de los más contaminantes del mundo. Estas iniciativas reducen "
            "huella hídrica, residuos y emisiones."
        )
    )

    story_card(
        title="Impacto social",
        icon="🧵",
        color="#FFF3E0",
        description=(
            "Generan empleo para mujeres cabeza de hogar y comunidades creativas."
        )
    )

    st.divider()

    # ============================================================
    # 5. EKOBOOT – CALZADO CON LLANTAS RECICLADAS
    # ============================================================

    st.header("👟 Caso 5: EkoBoot (Calzado con llantas recicladas)")

    story_card(
        title="¿Qué hace EkoBoot?",
        icon="♻️",
        description=(
            "Convierte llantas usadas —un residuo altamente contaminante— en suelas de zapatos "
            "duraderas y resistentes, combinando moda y sostenibilidad."
        )
    )

    story_card(
        title="Impacto ambiental",
        icon="🌍",
        description=(
            "Evita que miles de llantas terminen en ríos, quemas ilegales o botaderos clandestinos."
        )
    )

    story_card(
        title="Modelo social",
        icon="🛠️",
        color="#FFF3E0",
        description=(
            "Involucran a zapateros tradicionales, comunidades artesanas y emprendedores locales."
        )
    )

    st.divider()

    # ============================================================
    # 6. RECUPERACIÓN DE ACEITE USADO
    # ============================================================

    st.header("🛢️ Caso 6: Empresas recuperadoras de aceite usado")

    story_card(
        title="¿Qué hacen estas empresas?",
        icon="🔋",
        description=(
            "Recolectan aceite de cocina usado en hogares, restaurantes y cafeterías para transformarlo "
            "en biocombustible (biodiésel), jabones y otros productos circulares."
        )
    )

    story_card(
        title="Problema que resuelven",
        icon="⚠️",
        description=(
            "Un solo litro de aceite puede contaminar más de 1000 litros de agua. Estas empresas "
            "evitan que llegue a tuberías, ríos o suelos."
        )
    )

    story_card(
        title="Impacto social",
        icon="🤲",
        color="#FFF3E0",
        description=(
            "Generan ingresos para recolectores, incentivan la economía circular y promueven educación ciudadana."
        )
    )

    st.success("✔ Historias reales agregadas exitosamente.")
