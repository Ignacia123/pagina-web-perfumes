from __future__ import annotations

import streamlit as st

from utils import evaluate_quiz, get_quiz_questions, render_sidebar


st.set_page_config(page_title="Test Interactivo", page_icon="🧪", layout="wide")
render_sidebar()

st.title("Descubre tu Familia Olfativa")
st.caption("Responde las siguientes preguntas y obtén una recomendación personalizada.")

questions = get_quiz_questions()

with st.form("quiz_form"):
    responses = []
    for idx, question in enumerate(questions, start=1):
        choice = st.radio(
            label=f"{idx}. {question.pregunta}",
            options=list(question.opciones.keys()),
            format_func=lambda key, opciones=question.opciones: opciones[key],
            key=f"pregunta_{idx}",
        )
        responses.append(choice)

    submitted = st.form_submit_button("Ver mi recomendación")

if submitted:
    resultado = evaluate_quiz(responses)
    st.success(
        f"Tu perfil predominante es: **{resultado['titulo']}**\n\n{resultado['descripcion']}"
    )

    st.markdown("#### Puntuaciones obtenidas")
    cols = st.columns(len(resultado["puntajes"]))
    for col, (familia, puntaje) in zip(cols, resultado["puntajes"].items()):
        col.metric(label=familia.capitalize(), value=puntaje)

else:
    st.info("Completa el cuestionario y pulsa el botón para conocer tu familia olfativa ideal.")


