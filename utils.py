"""Funciones auxiliares y datos estáticos para la app "El Arte del Perfume"."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd


BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
VIDEO_DIR = ASSETS_DIR / "video"


def get_asset_path(*parts: str) -> Path:
    """Retorna la ruta absoluta a un recurso dentro de assets."""

    return ASSETS_DIR.joinpath(*parts)


def resolve_image(name: str, fallback_url: Optional[str] = None) -> Dict[str, Optional[str]]:
    """Devuelve un diccionario con la ruta local o el fallback para una imagen."""

    path = IMAGES_DIR / name
    if path.exists():
        return {"path": str(path), "fallback": fallback_url}
    return {"path": fallback_url, "fallback": fallback_url}


def resolve_video(name: str, fallback_url: Optional[str] = None) -> Dict[str, Optional[str]]:
    """Devuelve un diccionario con la ruta local o el fallback para un video."""

    path = VIDEO_DIR / name
    if path.exists():
        return {"path": str(path), "fallback": fallback_url}
    return {"path": fallback_url, "fallback": fallback_url}


def get_perfume_types() -> pd.DataFrame:
    """Información tabular acerca de los tipos de perfumes y sus concentraciones."""

    data = [
        {
            "Tipo": "Parfum (Extracto)",
            "Concentración": "20-40% esencia",
            "Duración": "8-12 horas",
            "Notas Destacadas": "Ricas, intensas, cercanas a la piel",
        },
        {
            "Tipo": "Eau de Parfum",
            "Concentración": "15-20% esencia",
            "Duración": "6-8 horas",
            "Notas Destacadas": "Profundidad, gran estela",
        },
        {
            "Tipo": "Eau de Toilette",
            "Concentración": "8-12% esencia",
            "Duración": "4-6 horas",
            "Notas Destacadas": "Versátil, ideal para el día",
        },
        {
            "Tipo": "Eau de Cologne",
            "Concentración": "2-5% esencia",
            "Duración": "2-3 horas",
            "Notas Destacadas": "Refrescante, cítrica",
        },
        {
            "Tipo": "Body Mist",
            "Concentración": "1-3% esencia",
            "Duración": "1-2 horas",
            "Notas Destacadas": "Muy ligera, uso frecuente",
        },
    ]
    return pd.DataFrame(data)


def get_perfume_examples() -> Dict[str, List[str]]:
    """Devuelve ejemplos de marcas asociadas a cada tipo."""

    return {
        "Parfum (Extracto)": ["Chanel No.5 Parfum", "Maison Francis Kurkdjian Baccarat Rouge 540"],
        "Eau de Parfum": ["Dior J'adore", "YSL Libre"],
        "Eau de Toilette": ["Acqua di Gio", "CH 212"],
        "Eau de Cologne": ["4711 Original", "Tom Ford Neroli Portofino"],
        "Body Mist": ["Victoria's Secret Love Spell", "Bath & Body Works Gingham"],
    }


def get_olfactive_families() -> Dict[str, Dict[str, str]]:
    """Información descriptiva de familias olfativas."""

    return {
        "Floral": {
            "descripcion": "Bouquets ricos en notas de flores frescas y pétalos dulces.",
            "ejemplos": "Chanel No.5, Marc Jacobs Daisy",
            "imagen": resolve_image("floral.jpg", fallback_url="https://images.unsplash.com/photo-1487412720507-6297c0ae4bda"),
        },
        "Cítrica": {
            "descripcion": "Fragancias vivaces con notas de limón, bergamota, mandarina.",
            "ejemplos": "Dior Eau Sauvage, Atelier Cologne Orange Sanguine",
            "imagen": resolve_image("citricas.jpg", fallback_url="https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=compress&fit=crop&w=900"),
        },
        "Amaderada": {
            "descripcion": "Aromas de maderas nobles, resinas y vetiver.",
            "ejemplos": "Terre d'Hermès, Tom Ford Oud Wood",
            "imagen": resolve_image("amaderadas.jpg", fallback_url="https://images.unsplash.com/photo-1498842812179-c81beecf902c?auto=compress&fit=crop&w=800"),
        },
        "Oriental": {
            "descripcion": "Composiciones especiadas, dulces y envolventes.",
            "ejemplos": "Guerlain Shalimar, Yves Saint Laurent Opium",
            "imagen": resolve_image("orientales.jpg", fallback_url="https://images.unsplash.com/photo-1512767347951-df63c80f31ea?auto=compress&fit=crop&w=900"),
        },
        "Aromática": {
            "descripcion": "Notas herbales como lavanda, salvia y romero.",
            "ejemplos": "Giorgio Armani Acqua di Giò Profumo, Dior Sauvage",
            "imagen": resolve_image("aromatica.jpg", fallback_url="https://images.unsplash.com/photo-1465408953385-7c4624fa7d6a?auto=compress&fit=crop&w=800"),
        },
    }


def get_family_graph() -> str:
    """Genera un gráfico en formato Graphviz DOT que relaciona las familias olfativas."""

    return """
        digraph FamiliasOlfativas {
            rankdir=LR;
            node [shape=ellipse, style=filled, color="#f1c40f", fontname="Helvetica"];
            Floral -> Oriental;
            Floral -> Aromática;
            Cítrica -> Aromática;
            Cítrica -> Amaderada;
            Oriental -> Amaderada;
            Oriental -> Gourmand [label="subfamilia"];
            Amaderada -> Aromática;
            Aromática -> Fougere [label="mezcla clásica"];
        }
    """


def get_curiosities() -> List[Dict[str, str]]:
    """Lista de curiosidades destacadas del universo del perfume."""

    return [
        {
            "titulo": "El origen del término perfume",
            "descripcion": "Proviene del latín 'per fumum', que significa 'a través del humo'.",
        },
        {
            "titulo": "Perfume como símbolo de estatus",
            "descripcion": "En el Antiguo Egipto, solo la realeza podía utilizar ciertos aceites aromáticos.",
        },
        {
            "titulo": "La primera casa moderna",
            "descripcion": "Guerlain, fundada en 1828, revolucionó la perfumería francesa con composiciones complejas.",
        },
        {
            "titulo": "Narices profesionales",
            "descripcion": "Los maestros perfumistas pueden identificar cientos de materias primas con un solo olfato.",
        },
    ]


def get_timeline_html() -> str:
    """Devuelve HTML sencillo para una línea de tiempo histórica de perfumes icónicos."""

    return """
    <div class="timeline">
      <style>
        .timeline {font-family: 'Helvetica', sans-serif; margin-top: 1rem;}
        .timeline-item {border-left: 3px solid #f39c12; padding-left: 1rem; margin-bottom: 1rem;}
        .timeline-year {font-weight: bold; color: #d35400;}
        .timeline-desc {margin: 0.25rem 0 0 0; color: #2c3e50;}
      </style>
      <div class="timeline-item">
        <div class="timeline-year">1921</div>
        <p class="timeline-desc">Chanel No.5 introduce aldehídos y redefine la perfumería moderna.</p>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">1957</div>
        <p class="timeline-desc">Diorissimo celebra las notas florales verdes con lirio del valle.</p>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">1992</div>
        <p class="timeline-desc">Thierry Mugler Angel populariza la familia gourmand.</p>
      </div>
      <div class="timeline-item">
        <div class="timeline-year">2013</div>
        <p class="timeline-desc">Maison Francis Kurkdjian Baccarat Rouge 540 simboliza el lujo moderno.</p>
      </div>
    </div>
    """


@dataclass
class QuizQuestion:
    pregunta: str
    opciones: Dict[str, str]


def get_quiz_questions() -> List[QuizQuestion]:
    """Genera la lista de preguntas para el test olfativo."""

    return [
        QuizQuestion(
            pregunta="¿Qué sensación buscas en tu fragancia diaria?",
            opciones={
                "fresco": "Ligereza y frescura",
                "floral": "Romanticismo y dulzura",
                "oriental": "Sensualidad y calidez",
                "amaderado": "Sofisticación y elegancia",
            },
        ),
        QuizQuestion(
            pregunta="¿Qué notas prefieres al inicio de un perfume?",
            opciones={
                "fresco": "Cítricos chispeantes",
                "floral": "Pétalos suaves",
                "oriental": "Especias exóticas",
                "amaderado": "Hierbas y maderas aromáticas",
            },
        ),
        QuizQuestion(
            pregunta="¿Cómo quieres que te recuerden?",
            opciones={
                "floral": "Delicada y encantadora",
                "oriental": "Misteriosa e intensa",
                "amaderado": "Elegante y profesional",
                "fresco": "Vibrante y jovial",
            },
        ),
        QuizQuestion(
            pregunta="¿Qué entorno te inspira más?",
            opciones={
                "fresco": "Una costa mediterránea",
                "floral": "Un jardín en primavera",
                "oriental": "Un bazar oriental",
                "amaderado": "Un bosque lluvioso",
            },
        ),
        QuizQuestion(
            pregunta="Elige un accesorio que complemente tu estilo",
            opciones={
                "amaderado": "Reloj de cuero",
                "oriental": "Joyas doradas",
                "floral": "Fular de seda",
                "fresco": "Gafas de sol",
            },
        ),
    ]


RECOMMENDATIONS = {
    "fresco": {
        "titulo": "Familia Cítrica/Acuática",
        "descripcion": "A todas luces refrescante, perfecta para días dinámicos y climas cálidos.",
        "imagen": resolve_image("esencia_3.jpg", fallback_url="https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=compress&fit=crop&w=900"),
    },
    "floral": {
        "titulo": "Familia Floral",
        "descripcion": "Delicada y romántica, ideal para momentos íntimos y ocasiones especiales.",
        "imagen": resolve_image("esencia_2.jpg", fallback_url="https://images.unsplash.com/photo-1487412720507-6297c0ae4bda"),
    },
    "oriental": {
        "titulo": "Familia Oriental/Ámbar",
        "descripcion": "Notas especiadas y dulces que envuelven con magnetismo nocturno.",
        "imagen": resolve_image("esencia_1.jpg", fallback_url="https://images.unsplash.com/photo-1512767347951-df63c80f31ea?auto=compress&fit=crop&w=900"),
    },
    "amaderado": {
        "titulo": "Familia Amaderada/Aromática",
        "descripcion": "Elegancia serena basada en vetiver, cedro y hierbas nobles.",
        "imagen": resolve_image("esencia_1.jpg", fallback_url="https://images.unsplash.com/photo-1498842812179-c81beecf902c?auto=compress&fit=crop&w=800"),
    },
}


def evaluate_quiz(responses: List[str]) -> Dict[str, str]:
    """Analiza las respuestas y retorna la mejor recomendación."""

    scores: Dict[str, int] = {"fresco": 0, "floral": 0, "oriental": 0, "amaderado": 0}
    for choice in responses:
        if choice in scores:
            scores[choice] += 1

    best = max(scores, key=scores.get)
    result = RECOMMENDATIONS[best]
    return {
        "codigo": best,
        "titulo": result["titulo"],
        "descripcion": result["descripcion"],
        "imagen": result["imagen"],
        "puntajes": scores,
    }


def render_sidebar():
    """Construye la barra lateral de navegación con enlaces a todas las páginas."""

    import streamlit as st  # importación local para evitar dependencias circulares

    st.markdown(
        """
        <style>
        [data-testid="stSidebarNav"] {display: none;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.title("El Arte del Perfume")
    st.sidebar.caption("Explora cada sección para descubrir el universo aromático.")

    st.sidebar.page_link("app.py", label="Inicio")
    st.sidebar.page_link("pages/1_Tipos_de_Perfumes.py", label="Tipos de Perfumes")
    st.sidebar.page_link("pages/2_Familias_Olfativas.py", label="Familias Olfativas")
    st.sidebar.page_link("pages/3_Curiosidades.py", label="Curiosidades")
    st.sidebar.page_link("pages/4_Test_Interactivo.py", label="Test Interactivo")
    st.sidebar.page_link("pages/5_Contacto.py", label="Contacto y Créditos")


__all__ = [
    "get_asset_path",
    "resolve_image",
    "resolve_video",
    "get_perfume_types",
    "get_perfume_examples",
    "get_olfactive_families",
    "get_family_graph",
    "get_curiosities",
    "get_timeline_html",
    "get_quiz_questions",
    "evaluate_quiz",
    "render_sidebar",
]


