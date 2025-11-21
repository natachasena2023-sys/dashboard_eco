# utils.py
import streamlit as st
import base64
from config import (
    IMG_BANNER_SUP,
    IMG_BANNER_INF,
)


def img_to_base64(path: str):
    """Convierte una imagen en base64."""
    try:
        with open(path, "rb") as img:
            return base64.b64encode(img.read()).decode()
    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {path}")
        return None


def load_css():
    """Carga styles.css e inserta dinámicamente los banners."""
    # 1. Leer styles.css
    try:
        with open("assets/styles.css", "r", encoding="utf-8") as f:
            css = f"<style>{f.read()}</style>"
    except FileNotFoundError:
        st.error("No se encontró assets/styles.css")
        return

    # 2. Convertir imágenes
    banner_sup = img_to_base64(IMG_BANNER_SUP)
    banner_inf = img_to_base64(IMG_BANNER_INF)

    # 3. Agregar estilos para banners (SIN STYLE EXTRA AL FINAL)
    extra_css = "<style>"

    if banner_sup:
        extra_css += f"""
        .banner {{
            background-image: url("data:image/png;base64,{banner_sup}") !important;
        }}
        """

    if banner_inf:
        extra_css += f"""
        .banner-inferior {{
            background-image: url("data:image/png;base64,{banner_inf}") !important;
        }}
        """

    extra_css += "</style>"

    # 4. Inyectar estilos
    st.markdown(css + extra_css, unsafe_allow_html=True)