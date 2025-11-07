from __future__ import annotations

import streamlit as st

from utils import get_curiosities, get_timeline_html, render_sidebar, resolve_image


st.set_page_config(page_title="Curiosidades del Perfume", page_icon="💡", layout="wide")
render_sidebar()

st.title("Curiosidades del Mundo del Perfume")
st.caption("Historias, datos y rarezas que perfuman la cultura global.")

curiosidades = get_curiosities()
cols = st.columns(2)
for index, dato in enumerate(curiosidades):
    with cols[index % 2]:
        st.subheader(dato["titulo"])
        st.write(dato["descripcion"])

st.divider()

st.markdown("#### Línea de tiempo aromática")
st.markdown(get_timeline_html(), unsafe_allow_html=True)

st.divider()

st.markdown("#### Galería de perfumes legendarios")

galeria = [
    resolve_image("lengendario3.jpg", fallback_url="https://images.unsplash.com/photo-1512767347951-df63c80f31ea?auto=compress&fit=crop&w=900"),
    resolve_image("legendario1.jpg", fallback_url="https://images.unsplash.com/photo-1487412720507-6297c0ae4bda"),
    resolve_image("legendario2.jpg", fallback_url="https://images.unsplash.com/photo-1498842812179-c81beecf902c"),
]

galeria_cols = st.columns(3)
for col, imagen in zip(galeria_cols, galeria):
    with col:
        if imagen["path"]:
            st.image(imagen["path"], use_container_width=True)
        elif imagen["fallback"]:
            st.image(imagen["fallback"], use_container_width=True)


