# data_loader.py
from __future__ import annotations

from typing import Optional
import re

import pandas as pd
import streamlit as st

from config import DATA_URL
from dictionaries import (
    DEPARTMENT_CANONICAL,
    DEPARTMENT_COORDS,
    MAPEO_REGION,
    categorias_basura_cero,
)


# ============================================================
# Funciones auxiliares de limpieza y normalización
# ============================================================

def normalizar_region(region: str) -> Optional[str]:
    """Normaliza el nombre de una región a su forma estandarizada."""
    if pd.isna(region):
        return None
    region = str(region).strip().upper()
    reemplazos = {
        "CARIBE": "CARIBE",
        "ANDINA": "ANDINA",
        "PACIFICO": "PACÍFICO",
        "PACÍFICO": "PACÍFICO",
        "ORINOQUIA": "ORINOQUÍA",
        "ORINOQUÍA": "ORINOQUÍA",
        "AMAZONIA": "AMAZONÍA",
        "AMAZONÍA": "AMAZONÍA",
    }
    return reemplazos.get(region, region)


def normalizar_departamento(valor: Optional[str]) -> Optional[str]:
    """Normaliza el nombre de un departamento y devuelve su forma canónica."""
    if pd.isna(valor):
        return pd.NA

    texto = str(valor).strip().upper()
    texto = texto.replace(".", " ").replace(",", " ")
    texto = re.sub(r"\s+", " ", texto)

    return DEPARTMENT_CANONICAL.get(texto, texto)


def coordenadas_departamento(nombre: Optional[str]):
    """Obtiene las coordenadas del departamento con base en su nombre canónico."""
    if pd.isna(nombre):
        return None

    clave = DEPARTMENT_CANONICAL.get(str(nombre).strip().upper(), None)
    if clave is None:
        return None
    return DEPARTMENT_COORDS.get(clave)


def limpiar_numeros(texto: str) -> str:
    """Elimina prefijos numéricos tipo '1.2.3. ' al inicio del texto."""
    if pd.isna(texto):
        return texto
    return re.sub(r"^\s*[\d\.]+\s*", "", str(texto))


def tipo_relacion_basura_cero(fila: pd.Series) -> str:
    """Detecta palabras clave y asigna categoría de economía circular."""
    texto = f"{fila['DESCRIPCIÓN']} {fila['SECTOR']} {fila['SUBSECTOR']}".lower()
    tipos = []

    for categoria, palabras in categorias_basura_cero.items():
        if any(p in texto for p in palabras):
            tipos.append(categoria)

    return ", ".join(tipos) if tipos else "No aplica"


def tiene_relacion_basura_cero(valor) -> bool:
    """Determina si un registro tiene relación con el programa Basura Cero."""
    if pd.isna(valor):
        return False
    valor = str(valor).strip().lower()
    return valor not in ["", "no aplica", "no disponible"]

def normalizar_sector(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza la columna SECTOR a texto limpio y MAYÚSCULAS."""
    if "SECTOR" in df.columns:
        df["SECTOR"] = df["SECTOR"].astype(str).str.strip().str.upper()
    return df


def plot_if_not_empty(func, df: pd.DataFrame):
    """Ejecuta una función de ploteo solo si el DataFrame no está vacío."""
    if df.empty:
        st.info("No hay datos con los filtros seleccionados.")
        return
    func(df)


# ============================================================
#     --- Función principal de carga y limpieza --- 
# ============================================================

@st.cache_data(show_spinner=False)
def load_data(dummy: int = 1) -> pd.DataFrame:
    """
    Carga el dataset desde GitHub, lo limpia y devuelve un DataFrame listo para usar.
    El parámetro dummy permite que Streamlit re-evalúe el cache si se desea.
    """
    df = pd.read_csv(DATA_URL)

    # Limpieza de columnas con saltos de línea en el nombre
    renames = {col: col.split("\n")[0] for col in df.columns if "\n" in col}
    df = df.rename(columns=renames)
    df.columns = df.columns.str.upper().str.strip()

    # Limpieza de AÑO
    if "AÑO" in df.columns:
        df["AÑO"] = df["AÑO"].astype(str).str.replace(",", "")
        df["AÑO"] = pd.to_numeric(df["AÑO"], errors="coerce").astype("Int64")

    # Normalizar AUTORIDAD AMBIENTAL
    if "AUTORIDAD AMBIENTAL" in df.columns:
        df["AUTORIDAD AMBIENTAL"] = (
            df["AUTORIDAD AMBIENTAL"].astype("string").str.strip().str.upper()
        )

    # Normalizar REGIÓN
    if "REGIÓN" in df.columns:
        df["REGIÓN"] = df["REGIÓN"].astype("string").map(normalizar_region)

        def asignar_region(row):
            region = row["REGIÓN"]
            if pd.isna(region) or str(region).lower() == "no registra":
                return MAPEO_REGION.get(row["AUTORIDAD AMBIENTAL"], region)
            return region

        df["REGIÓN"] = df.apply(asignar_region, axis=1)
        df["REGIÓN"] = df["REGIÓN"].map(normalizar_region)

    # Normalizar DEPARTAMENTO
    if "DEPARTAMENTO" in df.columns:
        df["DEPARTAMENTO"] = df["DEPARTAMENTO"].astype("string").map(
            normalizar_departamento
        )

    # Limpiar numeración en categorías
    for col in ["CATEGORÍA", "SECTOR", "SUBSECTOR"]:
        if col in df.columns:
            df[col] = df[col].apply(limpiar_numeros)

    # 🔥 NORMALIZAR SECTOR AQUÍ
    df = normalizar_sector(df)
    
    # Limpieza de PRODUCTO PRINCIPAL
    if "PRODUCTO PRINCIPAL" in df.columns:
        df["PRODUCTO PRINCIPAL"] = df["PRODUCTO PRINCIPAL"].astype(str).str.upper()
        df["PRODUCTO PRINCIPAL"] = df["PRODUCTO PRINCIPAL"].str.replace(
            ".", "", regex=False
        )
        df["PRODUCTO PRINCIPAL"] = df["PRODUCTO PRINCIPAL"].replace(
            {"MIEL": "MIEL DE ABEJAS"}
        )

    # Clasificación BASURA CERO
    if all(col in df.columns for col in ["DESCRIPCIÓN", "SECTOR", "SUBSECTOR"]):
        df["RELACIÓN BASURA CERO"] = df.apply(tipo_relacion_basura_cero, axis=1)

    # Columna BASURA 0 (Sí / No)
    if "RELACIÓN BASURA CERO" in df.columns:
        df["BASURA 0"] = df["RELACIÓN BASURA CERO"].apply(
            lambda x: "Sí"
            if pd.notna(x)
            and str(x).strip() != ""
            and str(x).lower() != "no aplica"
            else "No"
        )

    return df
