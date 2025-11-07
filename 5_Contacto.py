from __future__ import annotations

import streamlit as st

from utils import render_sidebar


st.set_page_config(page_title="Contacto y Créditos", page_icon="📬", layout="wide")
render_sidebar()

st.title("Sobre Nosotras")

st.markdown("---")

st.header("Nuestra pasión por los aromas")

st.write(
    """
    **Fragrances IeJ S.A.** Es una empresa ficticia dedicada a la divulgación de la cultura del perfume. Fundada en 2025 por una perfumistas y amantes de
    las fragancias con el único propósito de compartir conocimientos y secretos sobre este arte.

    Nuestro equipo está compuesto por:

    * **Javiera:** Perfumista experta.
    * **Maria** Social Management.
    * **Patricia** Creadora de contenido digital.

    """
)

st.warning("Toda la información y los perfumes son exclusivos de la dueña.")


