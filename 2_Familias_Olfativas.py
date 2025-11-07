from __future__ import annotations

import streamlit as st

from utils import get_family_graph, get_olfactive_families, render_sidebar


st.set_page_config(page_title="Familias Olfativas", page_icon="🌸", layout="wide")
render_sidebar()

st.title("Familias Olfativas")
st.caption("Explora los universos aromáticos que inspiran a perfumistas de todo el mundo.")

familias = get_olfactive_families()
familia_seleccionada = st.selectbox("Elige una familia para ver sus características:", list(familias.keys()))

info_familia = familias[familia_seleccionada]

col_texto, col_imagen = st.columns([2, 1])

with col_texto:
    st.subheader(familia_seleccionada)
    st.write(info_familia["descripcion"])
    st.markdown(f"**Perfumes representativos:** {info_familia['ejemplos']}")

with col_imagen:
    imagen_info = info_familia["imagen"]
    image_source = imagen_info.get("path")
    fallback_source = imagen_info.get("fallback")

    if image_source:
        st.image(image_source, caption=familia_seleccionada, width=320)
    elif fallback_source:
        st.image(fallback_source, caption=familia_seleccionada, width=320)

st.divider()

st.markdown("#### Relaciones entre familias")
st.graphviz_chart(get_family_graph())


