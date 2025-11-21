# 🌱 Dashboard Eco — Negocios Verdes & Basura Cero

Bienvenido al **Dashboard Eco**, una aplicación web interactiva construida en **Streamlit** para visualizar, analizar y explorar información oficial sobre **Negocios Verdes en Colombia** y su relación con el programa **Basura Cero**.

Este proyecto fue desarrollado con una arquitectura modular, limpia y mantenible, ideal para uso académico, institucional o de investigación.

---

## 📁 Estructura del Proyecto

```
dashboard_eco/
│
├── main.py                 # Punto de entrada principal
├── config.py               # Rutas, constantes, configuración global
├── utils.py                # Carga de CSS, manejo de imágenes, utilidades
├── data_loader.py          # Carga, limpieza y normalización de datos
├── dictionaries.py         # Diccionarios de categorías, regiones, colores
├── graficos.py             # Gráficos y visualizaciones
│
├── assets/
│   ├── styles.css          # Estilos personalizados de toda la app
│   └── img/                # Recursos gráficos
│        ├── verde.png
│        ├── verde2.png
│        ├── mapa_basura_cero.jpg
│        └── baner_l.png
│
└── sections/               # Módulos de contenido por pantalla
    ├── home.py             # Sección principal (Inicio)
    ├── mapa.py             # Mapa del sitio
    └── faq.py              # Preguntas frecuentes
```

---

## 🚀 ¿Qué hace este Dashboard?

### 🔹 **1. Limpia y normaliza datos oficiales**

Incluye procesos de:

* Corrección de inconsistencias en columnas
* Normalización de regiones y autoridades ambientales
* Estandarización de departamentos
* Detección automática de categorías Basura Cero

### 🔹 **2. Visualiza indicadores clave**

El dashboard incluye:

* Mapa interactivo de intensidad Basura Cero (Mapbox)
* Top 10 sectores con más negocios verdes
* Tendencia anual de registros
* Gráficos de autoridades ambientales
* Distribución por categorías Basura Cero
* Mapa comparativo por región

### 🔹 **3. Proporciona herramientas para explorar datos**

* Filtros por región, sector y relación Basura Cero
* Tabla interactiva completa
* Descarga del dataset limpio en CSV

---

## 🎨 Diseño e Interfaz

El proyecto integra:

* **CSS personalizado** con estilos ecológicos
* Banners superiores e inferiores dinámicos cargados en Base64
* Componentes estilizados como métricas, secciones y tarjetas

El archivo `styles.css` centraliza todos los estilos visuales.

---

## 📊 Fuentes de Datos

Los datos utilizados son abiertos y provienen de:

* Ministerio de Ambiente y Desarrollo Sostenible
* Superintendencia de Servicios Públicos Domiciliarios (SSPD)
* Registros de Negocios Verdes (Datos Abiertos)

---

## ▶️ Cómo ejecutar el proyecto

### Requisitos previos

* Python 3.10+ recomendado
* Instalar dependencias:

```bash
pip install -r requirements.txt
```

### Ejecutar la aplicación

```bash
streamlit run main.py
```

La aplicación se abrirá automáticamente en tu navegador en:

```
http://localhost:8501
```

---

## 🧠 Arquitectura Modular

Este proyecto está diseñado bajo un enfoque modular:

* **main.py** controla navegación y layout
* **sections/** contiene las pantallas separadas
* **data_loader.py** se encarga del procesamiento de datos
* **graficos.py** aporta visualizaciones reutilizables
* **dictionaries.py** centraliza estructuras para limpieza
* **utils.py** maneja estilos y recursos visuales

Esta arquitectura permite agregar nuevas secciones sin afectar las existentes.

---

## 📌 Próximas Mejoras (Roadmap)

* Panel comparativo por región
* Análisis predictivo de tendencias
* Integración con bases en tiempo real
* Mapa avanzado de materiales aprovechados
* Dashboard para compradores de material reciclado

---

## 👨‍💻 Autores

Proyecto desarrollado por estudiantes del Bootcamp de Análisis de Datos, con un enfoque en sostenibilidad, economía circular y tecnologías limpias.

---

## 📝 Licencia

Este proyecto se distribuye bajo licencia **MIT**, permitiendo uso académico, institucional y libre modificación.

---

## 🌿 Nota Final

> *Este dashboard refleja el compromiso con la sostenibilidad, la innovación ambiental y la visualización de datos para el beneficio de las comunidades y la economía circular en Colombia.*