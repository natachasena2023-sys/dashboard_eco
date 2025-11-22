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
    """Limpia y mapea el nombre de un departamento a su forma canónica."""
    if pd.isna(valor):
        return pd.NA
    texto = str(valor).strip().upper()
    texto = texto.replace(".", " ").replace(",", " ")
    texto = re.sub(r"\s+", " ", texto)
    return DEPARTMENT_CANONICAL.get(texto, texto)


def coordenadas_departamento(nombre: Optional[str]):
    """Devuelve lat/lon aproximadas de un departamento."""
    if pd.isna(nombre):
        return None
    clave = DEPARTMENT_CANONICAL.get(str(nombre).strip().upper(), None)
    if clave is None:
        return None
    return DEPARTMENT_COORDS.get(clave)


def limpiar_numeros(texto: str) -> str:
    """Elimina numeración inicial en campos de texto (p.e. '1. SECTOR')."""
    if pd.isna(texto):
        return texto
    return re.sub(r"^\s*[\d\.]+\s*", "", str(texto))


def normalizar_sector(df: pd.DataFrame) -> pd.DataFrame:
    """Pone el sector en mayúsculas y sin espacios extremos."""
    if "SECTOR" in df.columns:
        df["SECTOR"] = df["SECTOR"].astype(str).str.strip().str.upper()
    return df


def tipo_relacion_basura_cero(fila: pd.Series) -> str:
    """Clasificación automática de la relación con Basura Cero."""
    texto = f"{fila['DESCRIPCIÓN']} {fila['SECTOR']} {fila['SUBSECTOR']}".lower()
    tipos = []
    for categoria, palabras in categorias_basura_cero.items():
        if any(p in texto for p in palabras):
            tipos.append(categoria)
    return ", ".join(tipos) if tipos else "No aplica"


def tiene_relacion_basura_cero(valor) -> bool:
    """Determina si un valor indica relación con Basura Cero."""
    if pd.isna(valor):
        return False
    valor = str(valor).strip().lower()
    return valor not in ["", "no aplica", "no disponible"]


@st.cache_data(show_spinner=False)
def load_data(dummy: int = 1) -> pd.DataFrame:
    """Carga el dataset remoto, limpia y crea campos derivados."""
    df = pd.read_csv(DATA_URL)

    # Quitar saltos de línea en nombres de columna
    renames = {col: col.split("\n")[0] for col in df.columns if "\n" in col}
    df = df.rename(columns=renames)
    df.columns = df.columns.str.upper().str.strip()

    # AÑO
    if "AÑO" in df.columns:
        df["AÑO"] = df["AÑO"].astype(str).str.replace(",", "")
        df["AÑO"] = pd.to_numeric(df["AÑO"], errors="coerce").astype("Int64")

    # AUTORIDAD AMBIENTAL
    if "AUTORIDAD AMBIENTAL" in df.columns:
        df["AUTORIDAD AMBIENTAL"] = df["AUTORIDAD AMBIENTAL"].astype("string").str.strip().str.upper()

    # REGIÓN (normalizada + relleno por autoridad ambiental)
    if "REGIÓN" in df.columns:
        df["REGIÓN"] = df["REGIÓN"].astype("string").map(normalizar_region)

        def asignar_region(row):
            region = row["REGIÓN"]
            if pd.isna(region) or str(region).lower() == "no registra":
                return MAPEO_REGION.get(row["AUTORIDAD AMBIENTAL"], region)
            return region

        df["REGIÓN"] = df.apply(asignar_region, axis=1)
        df["REGIÓN"] = df["REGIÓN"].map(normalizar_region)

    # DEPARTAMENTO
    if "DEPARTAMENTO" in df.columns:
        df["DEPARTAMENTO"] = df["DEPARTAMENTO"].astype("string").map(normalizar_departamento)

    # Quitar numeración de categoría, sector, subsector
    for col in ["CATEGORÍA", "SECTOR", "SUBSECTOR"]:
        if col in df.columns:
            df[col] = df[col].apply(limpiar_numeros)

    # Normalizar sector a mayúsculas
    df = normalizar_sector(df)

    # Ajuste de PRODUCTO PRINCIPAL
    if "PRODUCTO PRINCIPAL" in df.columns:
        df["PRODUCTO PRINCIPAL"] = df["PRODUCTO PRINCIPAL"].astype(str).str.upper()
        df["PRODUCTO PRINCIPAL"] = df["PRODUCTO PRINCIPAL"].str.replace(".", "", regex=False)
        df["PRODUCTO PRINCIPAL"] = df["PRODUCTO PRINCIPAL"].replace({"MIEL": "MIEL DE ABEJAS"})

    # Campo RELACIÓN BASURA CERO
    if all(col in df.columns for col in ["DESCRIPCIÓN", "SECTOR", "SUBSECTOR"]):
        df["RELACIÓN BASURA CERO"] = df.apply(tipo_relacion_basura_cero, axis=1)

    # Campo BASURA 0 (Sí/No)
    if "RELACIÓN BASURA CERO" in df.columns:
        df["BASURA 0"] = df["RELACIÓN BASURA CERO"].apply(
            lambda x: "Sí" if pd.notna(x) and str(x).strip() != "" and str(x).lower() != "no aplica" else "No"
        )

    return df
