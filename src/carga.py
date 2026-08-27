import numpy as np
import pandas as pd


def cargar(url, na_values=None):
    return pd.read_csv(url, na_values=na_values)

def reporte_nulos(df):
    cantidad = df.isna().sum()
    porcentaje = df.isna().mean() * 100

    reporte = pd.DataFrame({
        "nulos": cantidad,
        "porcentaje": porcentaje
    })

    return reporte.sort_values("porcentaje", ascending=False)

def limpiar(df):
    df = df.copy()

    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.drop_duplicates()

    columnas_texto = df.select_dtypes(include=["object", "string"]).columns
    for columna in columnas_texto:
        df[columna] = df[columna].str.strip().str.lower()

    porcentaje_nulos = df.isna().mean()
    columnas_muy_nulas = porcentaje_nulos[porcentaje_nulos >= 0.80].index
    df = df.drop(columns=columnas_muy_nulas)

    df = df.drop(columns=["county", "community"], errors="ignore")

    columnas_numericas = df.select_dtypes(include=np.number).columns
    for columna in columnas_numericas:
        if df[columna].isna().any():
            df[columna] = df[columna].fillna(df[columna].median())

    return df.reset_index(drop=True)

def guardar(df, ruta):
    df.to_parquet(ruta, index=False)

if __name__ == "__main__":
    url = "https://archive.ics.uci.edu/static/public/183/data.csv"

    df = cargar(url, na_values=["?"])
    print(reporte_nulos(df))

    df_limpio = limpiar(df)
    guardar(df_limpio, "data/limpio.parquet")