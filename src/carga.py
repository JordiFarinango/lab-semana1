import pandas as pd


def cargar(url, na_values=None):
    return pd.read_csv(url, na_values=na_values)