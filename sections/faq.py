import streamlit as st


def faq_section() -> None:
    st.header("❓ Preguntas Frecuentes")

    with st.expander("🧩 ¿Qué es un Negocio Verde?"):
        st.write(
            """
            Un **Negocio Verde** es una actividad económica que incorpora criterios de
            sostenibilidad ambiental, uso eficiente de recursos, responsabilidad social
            y aporte a la conservación del patrimonio natural.
            """
        )

    with st.expander("♻️ ¿Qué es el programa Basura Cero?"):
        st.write(
            """
            **Basura Cero** es una estrategia que busca reducir la cantidad de residuos
            que llegan a rellenos sanitarios, promoviendo la **prevención**, **reutilización**,
            **reciclaje** y **aprovechamiento** de materiales, así como la economía circular.
            """
        )

    with st.expander("📊 ¿De dónde provienen los datos del dashboard?"):
        st.write(
            """
            Los datos provienen del **Listado de Negocios Verdes** consolidado por las
            autoridades ambientales en Colombia y puesto a disposición en formato abierto.
            En este dashboard se realiza una limpieza, normalización y análisis exploratorio.
            """
        )

    with st.expander("🌍 ¿Cómo se relaciona esto con la economía circular?"):
        st.write(
            """
            Muchos de los negocios verdes trabajan en la **valorización de residuos**,
            el **ecodiseño**, la **reutilización de materiales** o la **prestación de servicios
            ambientales**, lo que los convierte en actores clave dentro de la economía circular.
            """
        )

    with st.expander("🧪 ¿Puedo usar este dashboard como base para un proyecto de investigación?"):
        st.write(
            """
            ¡Claro! Este dashboard puede servir como punto de partida para:

            - trabajos académicos,
            - análisis territoriales,
            - diseño de políticas públicas,
            - formulación de proyectos de innovación o emprendimiento verde.
            """
        )
