from __future__ import annotations

import streamlit as st

from utils import (
    get_perfume_examples,
    get_perfume_types,
    render_sidebar,
    resolve_image,
)


st.set_page_config(page_title="Tipos de Perfumes", page_icon="📘", layout="wide")
render_sidebar()

st.title("Tipos de Perfumes")
st.caption("Comprende las concentraciones, duraciones y ejemplos emblemáticos.")

df = get_perfume_types()
st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()

tipo_seleccionado = st.radio("Selecciona un tipo para conocer más detalles:", df["Tipo"].tolist())

imagenes_tipo = {
    "Parfum (Extracto)": resolve_image(
        "baccarat.jpg",
        fallback_url="https://images.unsplash.com/photo-1512767347951-df63c80f31ea?auto=compress&fit=crop&w=900",
    ),
    "Eau de Parfum": resolve_image(
        "dior.jpg",
        fallback_url="https://images.unsplash.com/photo-1487412720507-6297c0ae4bda?auto=compress&fit=crop&w=900",
    ),
    "Eau de Toilette": resolve_image(
        "acqua.jpg",
        fallback_url="https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=compress&fit=crop&w=900",
    ),
    "Eau de Cologne": resolve_image(
        "Cologne.jpg",
        fallback_url="https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=compress&fit=crop&w=900",
    ),
    "Body Mist": resolve_image(
        "body.jpg",
        fallback_url="https://images.unsplash.com/photo-1465408953385-7c4624fa7d6a?auto=compress&fit=crop&w=900",
    ),
}

col_info, col_image = st.columns([2, 1], gap="large")

with col_info:
    fila_tipo = df[df["Tipo"] == tipo_seleccionado].iloc[0]
    st.subheader(tipo_seleccionado)
    st.markdown(
        f"**Concentración aproximada:** {fila_tipo['Concentración']}  \
        **Duración estimada:** {fila_tipo['Duración']}  \
        **Perfil olfativo:** {fila_tipo['Notas Destacadas']}"
    )

    ejemplos = get_perfume_examples().get(tipo_seleccionado, [])
    if ejemplos:
        st.markdown("**Referencias célebres:**")
        st.write(" · ".join(ejemplos))

    with st.expander("¿Cuándo elegir este tipo?", expanded=True):
        recomendaciones = {
            "Parfum (Extracto)": "Eventos memorables, noches y climas fríos donde la intensidad destaca.",
            "Eau de Parfum": "Uso versátil, ideal para oficina, citas y salidas sociales.",
            "Eau de Toilette": "Perfecto para el día a día, ambientes cálidos o reuniones informales.",
            "Eau de Cologne": "Refréscate después del ejercicio o durante veranos intensos.",
            "Body Mist": "Reaplica con frecuencia para mantener un halo sutil durante todo el día.",
        }
        st.write(recomendaciones.get(tipo_seleccionado, ""))

with col_image:
    imagen = imagenes_tipo.get(tipo_seleccionado)
    if imagen and imagen["path"]:
        st.image(imagen["path"], caption=tipo_seleccionado)


