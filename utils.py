from __future__ import annotations

from typing import Optional

import base64
import streamlit as st


def img_to_base64(path: str) -> Optional[str]:
    """Convierte una imagen en base64 para usarla en CSS."""
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {path}")
        return None


def load_css() -> None:
    """
    Carga el archivo assets/styles.css, inyecta los banners en base64
    y aplica el CSS a la app.
    """
    css_path = "assets/styles.css"
    try:
        with open(css_path, "r", encoding="utf-8") as f:
            css = f.read()
    except FileNotFoundError:
        st.warning("No se encontró assets/styles.css. Verifica la ruta.")
        return

    banner_sup = img_to_base64("assets/img/verde2.png") or ""
    banner_inf = img_to_base64("assets/img/verde.png") or ""

    css = css.replace("BANNER_SUPERIOR_BASE64", banner_sup)
    css = css.replace("BANNER_INFERIOR_BASE64", banner_inf)

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def apply_custom_css() -> None:
    """Alias para mantener compatibilidad con versiones anteriores."""
    load_css()


def render_footer() -> None:
    """Banner inferior con información de autores."""
    st.markdown(
        """
        <div class="banner-inferior">
            <div class="banner-content">
                <p><strong>🌿 Autores del proyecto 🌿</strong></p>
                <p>Paulina Noreña · pnorena@unal.edu.co</p>
                <p>Thomas Medina · thomasmedina519@gmail.com</p>
                <p>Angie Ruiz · angiecarorumer333@gmail.com</p>
                <p>Natacha Ochoa · ochoa0917@hotmail.com</p>
                <p>Juan Ignacio García · juanignaciogarcia7@gmail.com
                <p style="margin-top:8px; font-size: 0.85rem;">
                    💚 Proyecto académico realizado con Streamlit – Economía circular y programa Basura Cero.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
