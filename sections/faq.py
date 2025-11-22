# sections/faq.py
import streamlit as st


def render_faq() -> None:
    """Muestra un listado de preguntas frecuentes con respuestas."""
    st.title("Preguntas frecuentes")
    st.markdown(
        """
    Aquí encontrarás respuestas rápidas sobre el origen de la información, cómo se procesan los datos
    y cómo puedes aprovechar el tablero en tus proyectos.
    """
    )

    faq_items = [
        (
            "¿De dónde provienen los datos?",
            "Los datos se descargan de fuentes oficiales como la Superintendencia de Servicios Públicos "
            "Domiciliarios y MinVivienda, además del listado nacional de Negocios Verdes disponible "
            "en datos abiertos.",
        ),
        (
            "¿Qué son Servicios ecosistémicos?",
            "“Los servicios ecosistémicos son los beneficios que nos da la naturaleza, como agua limpia,"
            " polinización, captura de carbono y turismo de naturaleza. Son clave para la sostenibilidad y "
            "se fortalecen con estrategias como Basura Cero.",
        ),
        (
           "¿Qué son Los Ecoproductos ?",
            "es un producto que cuida el ambiente porque usa menos recursos, genera menos residuos o "
            "está hecho a partir de materiales reciclados o renovables.",
        ),
        (
            "¿Por qué aparece tanto la miel en los negocios verdes?",
            "Encontramos un alto número de negocios verdes basados en miel y apicultura. Esto sucede porque "
            "la apicultura es una actividad de muy bajo impacto ambiental, altamente alineada con los servicios "
            "ecosistémicos y con altos beneficios económicos. Además, sus subproductos se integran naturalmente"
            " a modelos de economía circular, lo que la hace coherente con los objetivos de Basura Cero.",
        ),
        (
            "¿Por qué las FNCER aparecen poco en los Negocios Verdes?",
            "Encontramos que el sector de Fuentes No Convencionales de Energía Renovable está muy poco representado"
            " en los Negocios Verdes. Esto se debe a que requiere altos niveles de inversión, trámites complejos y "
            "capacidades técnicas avanzadas, lo que deja este mercado dominado por grandes empresas y por fuera del "
            "ecosistema emprendedor. Esta baja presencia revela una gran oportunidad para impulsar proyectos territoriales "
            "de energía limpia alineados con Basura Cero y la transición energética."
        ),
        (
            "¿✅ Qué significa “Mercado Regulado” en este contexto?",
            " los negocios o servicios funcionan bajo un marco de regulación oficial, ya sea en energía, residuos, "
            "aprovechamiento o sostenibilidad.",
        ),
    ]

    for question, answer in faq_items:
        with st.expander(question):
            st.write(answer)

    st.success(
        "¿Tienes otra pregunta? ¡Añádela en el repositorio o compártela con el equipo!"
    )
