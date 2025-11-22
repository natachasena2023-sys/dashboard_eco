from __future__ import annotations

import pandas as pd
import streamlit as st

from config import DATA_URL
from dictionaries import DEPARTMENT_CANONICAL, DEPARTMENT_COORDS, MAPEO_REGION


def normalizar_departamento(nombre: str):
    if pd.isna(nombre):
        return None
    nombre = str(nombre).strip().upper()
    return DEPARTMENT_CANONICAL.get(nombre, nombre)


def normalizar_region(region: str):
    if pd.isna(region):
        return None
    region = str(region).strip().upper()
    return region


def coordenadas_departamento(depto: str):
    if pd.isna(depto):
        return None
    depto = str(depto).strip().upper()
    return DEPARTMENT_COORDS.get(depto)


def tiene_relacion_basura_cero(valor: str) -> bool:
    if pd.isna(valor):
        return False
    texto = str(valor).strip().lower()
    return texto not in ["", "no aplica", "no disponible"]


def cargar_datos() -> pd.DataFrame:
    try:
        df = pd.read_csv(DATA_URL)
    except Exception as e:
        st.error("❌ Error cargando el dataset desde la URL configurada.")
        st.error(str(e))
        return pd.DataFrame()

    if "DEPARTAMENTO" in df.columns:
        df["DEPARTAMENTO"] = df["DEPARTAMENTO"].apply(normalizar_departamento)

    if "REGIÓN" in df.columns:
        df["REGIÓN"] = df["REGIÓN"].astype(str).str.strip().str.upper()

    if "SECTOR" in df.columns:
        df["SECTOR"] = (
            df["SECTOR"]
            .astype(str)
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.title()
        )

    if "RELACIÓN BASURA CERO" in df.columns:
        df["RELACIÓN BASURA CERO"] = df["RELACIÓN BASURA CERO"].astype(str).str.strip()

    if "AÑO" in df.columns:
        df["AÑO"] = (
            df["AÑO"]
            .astype(str)
            .str.extract(r"(\d{4})")
        )
        df["AÑO"] = pd.to_numeric(df["AÑO"], errors="coerce")

    return df
