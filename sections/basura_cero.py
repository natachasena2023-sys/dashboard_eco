# sections/basura_cero.py

import streamlit as st


# ================================
#      Tarjeta Premium
# ================================

def info_card(title, description, icon="♻️", color="#E8F5E9"):
    st.markdown(
        f"""
        <div style="
            background:{color};
            padding:16px 22px;
            border-radius:18px;
            margin-bottom:18px;
            border-left:6px solid #1B5E20;
        ">
            <h3 style="margin:0; font-size:22px;">{icon} {title}</h3>
            <p style="font-size:16px; color:#2E7D32; margin-top:8px;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================
#   SECCIÓN PRINCIPAL – BASURA CERO & NEGOCIOS VERDES
# ============================================

def render_basura_cero():

    st.title("♻️ Basura Cero y su Relación con los Negocios Verdes")

    st.markdown("""
    El programa **Basura Cero** es una estrategia que busca transformar la forma en que gestionamos
    los residuos en Colombia. No se trata solo de reciclar, sino de **cambiar el modelo** hacia
    un sistema donde los residuos se convierten en recursos valiosos.  
    """
    )

    st.divider()

    # ============================================================
    # 1. ¿Qué es Basura Cero?
    # ============================================================

    info_card(
        title="¿Qué es Basura Cero?",
        icon="🗑️",
        description=(
            "Es un enfoque que busca reducir al máximo la generación de residuos y garantizar que "
            "los materiales se reincorporen a los ciclos productivos. Impulsa la economía circular, "
            "el aprovechamiento, la separación en la fuente y el consumo responsable."
        )
    )

    # ============================================================
    # 2. ¿Cómo se conecta con los Negocios Verdes?
    # ============================================================

    info_card(
        title="Conexión directa entre Basura Cero y los Negocios Verdes",
        icon="🔗",
        color="#E3F2FD",
        description=(
            "Los Negocios Verdes son actores claves de Basura Cero, ya que transforman residuos en "
            "productos útiles, generan empleos sostenibles y reducen la presión sobre los rellenos "
            "sanitarios. Son una alternativa ambiental, económica y socialmente viable."
        )
    )

    st.markdown("""
    Por ejemplo:
    - Empresas que convierten plástico reciclado en muebles.  
    - Negocios que transforman residuos orgánicos en compost.  
    - Proyectos que fabrican textiles a partir de fibras recuperadas.  
    """)

    st.divider()

    # ============================================================
    # 3. Desafíos actuales de Basura Cero en Colombia
    # ============================================================

    st.header("🚧 Desafíos del país")

    info_card(
        title="Falta de cultura ciudadana",
        icon="🧠",
        description=(
            "Aún persisten barreras culturales: poca separación en la fuente, desinformación y "
            "baja apropiación del concepto de economía circular."
        )
    )

    info_card(
        title="Infraestructura insuficiente",
        icon="🏗️",
        description=(
            "Varias ciudades no cuentan con suficientes centros de aprovechamiento, rutas selectivas "
            "o sistemas robustos de clasificación."
        )
    )

    info_card(
        title="Mercados poco desarrollados",
        icon="💼",
        description=(
            "Falta articulación entre recicladores, transformadores y compradores. Muchos materiales "
            "reciclados no tienen mercado estable."
        )
    )

    info_card(
        title="Formalización y desigualdad",
        icon="⚖️",
        description=(
            "Recicladores, asociaciones y pequeños negocios enfrentan barreras para formalizarse, "
            "acceder a financiación o competir con grandes industrias."
        )
    )

    st.divider()

    # ============================================================
    # 4. ¿Por qué este proyecto es importante?
    # ============================================================

    st.header("🌍 ¿Por qué es tan interesante este proyecto?")

    info_card(
        title="Impacto ambiental",
        icon="🌿",
        description=(
            "Permite visualizar cómo los negocios verdes pueden reducir residuos, proteger ecosistemas "
            "y fomentar prácticas de economía circular en todo el país."
        )
    )

    info_card(
        title="Impacto social",
        icon="🤝",
        description=(
            "Muchos negocios verdes generan empleo local, fortalecen comunidades rurales y dignifican "
            "el trabajo de miles de recicladores."
        )
    )

    info_card(
        title="Impacto económico",
        icon="📈",
        description=(
            "El sector aporta nuevas oportunidades de negocio, innovación, turismo sostenible y "
            "encadenamientos productivos que diversifican la economía nacional."
        )
    )

    st.divider()

    # ============================================================
    # 5. ¿Cuál es nuestro papel como ciudadanía?
    # ============================================================

    st.header("🧑‍🤝‍🧑 ¿Cuál es nuestra función como ciudadanos?")

    info_card(
        title="Separar correctamente los residuos",
        icon="🗂️",
        description=(
            "La separación en la fuente es la acción más poderosa y sencilla para apoyar Basura Cero. "
            "Permite que los materiales realmente puedan ser aprovechados."
        )
    )

    info_card(
        title="Consumir responsablemente",
        icon="🛒",
        color="#FFF3E0",
        description=(
            "Elegir productos reutilizables, locales, con menor empaque o hechos por negocios verdes "
            "apoya directamente la sostenibilidad."
        )
    )

    info_card(
        title="Apoyar a los Negocios Verdes locales",
        icon="💚",
        description=(
            "Comprar sus productos, recomendar sus servicios y visibilizarlos potencia el crecimiento "
            "de la economía circular en nuestras comunidades."
        )
    )

    info_card(
        title="Participar en programas y educación ambiental",
        icon="📚",
        description=(
            "La ciudadanía informada impulsa transformaciones. Participar en procesos de educación "
            "ambiental fortalece el cambio cultural hacia hábitos sostenibles."
        )
    )

    st.success("✔ Sección Basura Cero cargada correctamente.")
