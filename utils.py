# utils.py — Funciones utilitarias para EcoApp
import streamlit as st
from pathlib import Path
import base64


# =============================================================================
# 1. Cargar archivo CSS
# =============================================================================
def load_css(css_path: str) -> None:
    """
    Carga un archivo CSS desde la carpeta assets/styles.css.
    Uso:
        load_css("assets/styles.css")
    """
    css_file = Path(css_path)
    if not css_file.exists():
        st.error(f"❌ No se encontró el archivo CSS en: {css_path}")
        return

    with open(css_file, "r", encoding="utf-8") as f:
        css_content = f.read()

    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)


# =============================================================================
# 2. Convertir imagen a base64 (usado por banners)
# =============================================================================
def load_image_banner(image_path: str) -> str:
    """
    Convierte una imagen a Base64 para poder incrustarla en HTML.
    Uso:
        base64_img = load_image_banner("assets/img/baner_l.png")
    """
    img_file = Path(image_path)
    if not img_file.exists():
        st.error(f"❌ No se encontró la imagen del banner: {image_path}")
        return ""

    with open(img_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    return encoded
