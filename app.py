"""Página principal de la aplicación Streamlit El Arte del Perfume."""

from __future__ import annotations

import streamlit as st

from utils import render_sidebar, resolve_image, resolve_video


st.set_page_config(
    page_title="El Arte del Perfume",
    page_icon="🌹",
    layout="wide",
)

render_sidebar()

st.markdown(
    """
    <style>
    .hero {
        position: relative;
        padding: 4rem 2rem;
        color: white;
        border-radius: 1.5rem;
        background: linear-gradient(135deg, rgba(231, 76, 60, 0.7), rgba(155, 89, 182, 0.7)),
                    url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=compress&fit=crop&w=1600') center/cover;
        box-shadow: 0 20px 40px rgba(0,0,0,0.25);
    }
    .hero h1 {
        font-size: 3.2rem;
        margin-bottom: 0.5rem;
        animation: fadeDown 1.2s ease-in-out;
    }
    .hero p {
        font-size: 1.2rem;
        max-width: 720px;
        animation: fadeUp 1.4s ease-in-out;
    }
    @keyframes fadeDown {
        from {opacity: 0; transform: translateY(-25px);} to {opacity: 1; transform: translateY(0);}
    }
    @keyframes fadeUp {
        from {opacity: 0; transform: translateY(25px);} to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>El Arte del Perfume</h1>
        <p>
            Una experiencia sensorial que explora la historia, la ciencia y la emoción detrás de las fragancias.
            Descubre cómo los perfumes acompañan nuestros recuerdos y reflejan nuestra identidad.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.subheader("Un viaje aromático a través del tiempo")
    st.write(
        """
        Desde las civilizaciones antiguas hasta las casas de lujo contemporáneas, el perfume ha sido un símbolo de
        status, seducción y expresión personal. En esta plataforma encontrarás recursos multimedia, datos curiosos y
        un test interactivo para descubrir tu familia olfativa.
        """
    )

    perfume_gallery = [
        resolve_image("Esencia1.jpg", fallback_url="https://images.unsplash.com/photo-1501004318641-b39e6451bec6"),
        resolve_image("Esencia2.jpg", fallback_url="https://images.unsplash.com/photo-1498837167922-ddd27525d352"),
        resolve_image("Esencia3.jpg", fallback_url="https://images.unsplash.com/photo-1498842812179-c81beecf902c"),
    ]

    st.markdown("#### Galería sensorial")
    gallery_cols = st.columns(len(perfume_gallery))
    for idx, (col, image_info) in enumerate(zip(gallery_cols, perfume_gallery), start=1):
        with col:
            if image_info["path"]:
                col.image(image_info["path"], caption=f"Esencia {idx}", use_container_width=True)
            elif image_info["fallback"]:
                col.image(image_info["fallback"], caption=f"Esencia {idx}", use_container_width=True)

with col2:
    st.subheader("Elaboración artesanal")
    st.write(
        """
        Aprende cómo las esencias naturales y sintéticas se combinan en un proceso meticuloso que mezcla creatividad
        y química. Cada acorde resulta de cientos de pruebas para lograr armonías memorables.
        """
    )
    video_info = resolve_video(
        "historia_perfume.mp4",
        fallback_url="https://www.youtube.com/watch?v=QRZPy8Oag3g",
    )
    if video_info["path"]:
        st.video(video_info["path"])
    elif video_info["fallback"]:
        st.video(video_info["fallback"])


st.divider()

st.markdown("### Continúa explorando")

cta_cols = st.columns(3)

with cta_cols[0]:
    st.page_link("pages/1_Tipos_de_Perfumes.py", label="Tipos de Perfumes", icon="📘")
with cta_cols[1]:
    st.page_link("pages/2_Familias_Olfativas.py", label="Familias Olfativas", icon="🌸")
with cta_cols[2]:
    st.page_link("pages/3_Curiosidades.py", label="Curiosidades", icon="💡")

st.write("")

st.info(
    "¿Listo para descubrir tu aroma ideal? Dirígete al test interactivo en la barra lateral y obtén tu recomendación personalizada."
)


