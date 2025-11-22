from __future__ import annotations

import streamlit as st

from utils import load_css, load_image_banner
from data_loader import cargar_datos
from graficos import (
    plot_tendencia_anual,
    plot_mapa_basura_cero,
    plot_top_sectores,
    plot_relacion_basura_cero,
    plot_autoridades,
)
from sections.home import home_section
from sections.mapa import mapa_section
from sections.faq import faq_section


st.set_page_config(
    page_title="🌿 EcoApp – Negocios Verdes en Colombia",
    page_icon="🌱",
    layout="wide",
)

load_css("assets/styles.css")

top_banner_b64 = load_image_banner("assets/img/baner_l.png")
if top_banner_b64:
    st.markdown(
        f"""
        <div class="banner-top">
            <img src="data:image/png;base64,{top_banner_b64}" class="banner-image" />
        </div>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data(show_spinner=True)
def load_data():
    return cargar_datos()


df = load_data()

st.sidebar.title("📊 Navegación")
menu = st.sidebar.radio(
    "Ir a:",
    [
        "🏡 Inicio",
        "🗺️ Mapa General",
        "📈 Gráficos Interactivos",
        "❓ Preguntas Frecuentes",
    ],
    index=0,
)

st.sidebar.markdown("### 🌿 Sobre el proyecto")
st.sidebar.info(
    "Este dashboard explora el panorama de los **Negocios Verdes en Colombia**, "
    "con énfasis en su relación con el programa **Basura Cero** y la economía circular."
)

if menu == "🏡 Inicio":
    home_section(df)
elif menu == "🗺️ Mapa General":
    mapa_section(df)
elif menu == "📈 Gráficos Interactivos":
    st.header("📈 Gráficos Interactivos")

    st.subheader("📅 Tendencia anual")
    plot_tendencia_anual(df)
    st.markdown("---")

    st.subheader("🗺️ Mapa Basura Cero")
    plot_mapa_basura_cero(df)
    st.markdown("---")

    st.subheader("🌿 Sectores principales")
    plot_top_sectores(df)
    st.markdown("---")

    st.subheader("♻️ Relación con Basura Cero")
    plot_relacion_basura_cero(df)
    st.markdown("---")

    st.subheader("🏛️ Autoridades ambientales")
    plot_autoridades(df)
elif menu == "❓ Preguntas Frecuentes":
    faq_section()

bottom_banner_b64 = load_image_banner("assets/img/verde2.png")
if bottom_banner_b64:
    st.markdown(
        f"""
        <div class="banner-bottom">
            <img src="data:image/png;base64,{bottom_banner_b64}" class="banner-image" />
        </div>
        """,
        unsafe_allow_html=True,
    )
