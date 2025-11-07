# Guía de instalación y ejecución

## Requisitos previos

- Python 3.9 o superior
- Acceso a una terminal (PowerShell, cmd o similar)
- Conexión a internet para instalar dependencias

## 1. Instalar dependencias

```bash
pip install streamlit pandas
```

Si cuentas con un archivo `requirements.txt`, ejecuta:

```bash
pip install -r requirements.txt
```

## 2. Ejecutar la aplicación

```bash
cd perfume_app
streamlit run app.py
```

Streamlit abrirá la página en tu navegador predeterminado. Si no se abre automáticamente, visita `http://localhost:8501/`.

## 3. Estructura del proyecto

```
perfume_app/
├── app.py
├── utils.py
├── assets/
│   ├── images/
│   └── video/
└── pages/
    ├── 1_Tipos_de_Perfumes.py
    ├── 2_Familias_Olfativas.py
    ├── 3_Curiosidades.py
    ├── 4_Test_Interactivo.py
    └── 5_Contacto.py
```

## 4. Personalización

- Coloca tus imágenes en `assets/images/`.
- Ajusta textos e información en los archivos de `pages/` y en `app.py`.

## 5. Detener la aplicación

Presiona `Ctrl+C` en la terminal donde se esté ejecutando Streamlit.

¡Listo! Con estos pasos tendrás “El Arte del Perfume” funcionando en tu máquina.
