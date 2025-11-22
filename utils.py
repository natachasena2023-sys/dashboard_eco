import base64
from pathlib import Path
import streamlit as st


def load_css(css_path: str) -> None:
    css_file = Path(css_path)
    if not css_file.exists():
        st.warning(f"⚠️ No se encontró el archivo CSS en: {css_path}")
        return

    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()

    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)


def load_image_banner(image_path: str) -> str:
    img_file = Path(image_path)
    if not img_file.exists():
        return ""
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    return encoded
