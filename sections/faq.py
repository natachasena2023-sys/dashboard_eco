from __future__ import annotations

import streamlit as st


def render_faq() -> None:
    """Preguntas frecuentes sobre el proyecto y los conceptos clave."""
    st.title("❓ Preguntas frecuentes")

    with st.expander("¿De dónde provienen los datos?"):
        st.write(
            "Los datos se descargan de fuentes oficiales como el Listado Nacional de Negocios Verdes "
            "y los conjuntos de datos abiertos del Gobierno de Colombia (SSPD, MinVivienda, etc.)."
        )

    with st.expander("¿Qué son Servicios ecosistémicos?"):
        st.write(
            "Son los beneficios que nos brinda la naturaleza, como el suministro de agua, la polinización, "
            "la captura de carbono, la regulación del clima o el disfrute recreativo. "
            "Los negocios verdes buscan proteger y potenciar estos servicios."
        )

    with st.expander("¿Qué son Ecoproductos?"):
        st.write(
            "Son productos que reducen su impacto ambiental a lo largo de su ciclo de vida: usan menos recursos, "
            "generan menos residuos o están elaborados a partir de materiales reciclados o renovables."
        )

    with st.expander("¿Por qué aparece tanto la miel en los negocios verdes?"):
        st.write(
            "La apicultura y los productos derivados de la miel son muy frecuentes porque combinan bajo impacto ambiental, "
            "apoyo a la polinización (un servicio ecosistémico clave) y buenas oportunidades económicas para comunidades rurales."
        )

    with st.expander("¿Por qué las FNCER aparecen poco en los Negocios Verdes?"):
        st.write(
            "Las Fuentes No Convencionales de Energía Renovable suelen requerir altas inversiones, "
            "trámites complejos y capacidades técnicas especializadas. Por eso, muchas iniciativas de este tipo "
            "quedan en manos de grandes empresas y no se registran como emprendimientos verdes tradicionales, "
            "lo que revela una oportunidad importante para la política pública."
        )

    with st.expander("¿Qué significa que un proyecto esté alineado con Basura Cero?"):
        st.write(
            "En este dashboard, un proyecto se considera alineado cuando en su descripción, sector o subsector se "
            "identifican palabras clave asociadas al aprovechamiento de residuos, reciclaje, economía circular, "
            "bioinsumos, energías renovables u otros enfoques del programa Basura Cero."
        )

    st.success("¿Tienes otra pregunta? Puedes proponer nuevas preguntas para futuras versiones del tablero.")
