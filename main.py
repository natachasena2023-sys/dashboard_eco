# main.py — Dashboard Interactivo de Negocios Verdes en Colombia
# =============================================================================
# Autores: Angie Ruiz, Natacha Ochoa, Paulina Noreña,
#          Juan Ignacio García, Thomas Medina
# Estilo: Moderno, ecológico, modular, interactivo
# =============================================================================

from __future__ import annotations
import streamlit as st
from pathlib import Path

# Cargar módulos propios
from utils import load_css, load_image_banner
from data_loader import cargar_datos
from graficos import (
    plot_tendencia_anual,
    plot_mapa_basura_cero,
    plot_top_sectores,
    plot_relacion_basura_cero,
    plot_autoridades,
)

# Secciones modulares
from sections.home import home_section
from sections.mapa import mapa_section
from sections.faq import faq_section

# =============================================================================
# CONFIGURACIÓN GENERAL DE LA APP
# =============================================================================
st.set_page_config(
    page_title="🌿 EcoApp – Negocios Verdes Colombia",
    page_icon="🌱",
    layout="wide",
)

# Cargar CSS personalizado
load_css("assets/styles.css")

# =============================================================================
# BANNERS SUPERIOR E INFERIOR
# =============================================================================
st.markdown(
    """
    <div class="banner-top">
        <img src="assets/img/baner_l.png" class="banner-image">
    </div>
    """,
    unsafe_allow_html=True,
)

# =============================================================================
# CARGAR DATASET
# =============================================================================
@st.cache_data(show_spinner=True)
def load_data():
    return cargar_datos()

df = load_data()

# =============================================================================
# MENÚ LATERAL (SIDEBAR)
# =============================================================================
st.sidebar.title("📊 Navegación")
menu = st.sidebar.radio(
    "Ir a:",
    ["🏡 Inicio", "🗺️ Mapa General", "📈 Gráficos Interactivos", "❓ Preguntas Frecuentes"],
    index=0,
)

st.sidebar.markdown("### 🌿 Información")
st.sidebar.info(
    "Dashboard de análisis de **Negocios Verdes en Colombia**.\n"
    "Proyecto enfocado en sostenibilidad, Basura Cero y economía circular."
)

# =============================================================================
# SECCIONES
# =============================================================================

# -----------------------------
# 🏡 INICIO
# -----------------------------
if menu == "🏡 Inicio":
    home_section(df)

# -----------------------------
# 🗺️ MAPA
# -----------------------------
elif menu == "🗺️ Mapa General":
    mapa_section(df)

# -----------------------------
# 📈 GRÁFICOS INTERACTIVOS
# -----------------------------
elif menu == "📈 Gráficos Interactivos":

    st.header("📈 Gráficos Interactivos")

    # Tendencia por año
    st.subheader("📅 Tendencia anual")
    plot_tendencia_anual(df)

    st.markdown("---")

    # Mapa Basura Cero
    st.subheader("🗺️ Mapa Basura Cero")
    plot_mapa_basura_cero(df)

    st.markdown("---")

    # Sectores
    st.subheader("🌿 Sectores principales")
    plot_top_sectores(df)

    st.markdown("---")

    # Relación Basura Cero
    st.subheader("♻️ Relación con Basura Cero")
    plot_relacion_basura_cero(df)

    st.markdown("---")

    # Autoridades ambientales
    st.subheader("🏛️ Autoridades ambientales")
    plot_autoridades(df)

# -----------------------------
# ❓ FAQ
# -----------------------------
elif menu == "❓ Preguntas Frecuentes":
    faq_section()

# =============================================================================
# BANNER INFERIOR
# =============================================================================
st.markdown(
    """
    <div class="banner-bottom">
        <img src="assets/img/verde2.png" class="banner-image">
    </div>
    """,
    unsafe_allow_html=True,
)
