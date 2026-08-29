import numpy as np
import pandas as pd
import pytest

from src.analisis import (
    filtrar,
    recta_minimos_cuadrados,
    resumen_por_grupo,
    top_k,
    zscore,
)


@pytest.fixture
def df_mini():
    return pd.DataFrame({
        "grupo": ["a", "a", "b", "b"],
        "valor": [10.0, 20.0, 30.0, 40.0],
    })


def test_zscore_tiene_media_cero(df_mini):
    z = zscore(df_mini[["valor"]].to_numpy())
    assert z.mean() == pytest.approx(0.0, abs=1e-9)


def test_resumen_por_grupo_calcula_media(df_mini):
    resultado = resumen_por_grupo(df_mini, "grupo", ["valor"])
    assert resultado.loc["a", ("valor", "mean")] == pytest.approx(15.0)


def test_recta_minimos_cuadrados():
    x = np.array([1.0, 2.0, 3.0])
    y = 2 * x + 1

    a, b = recta_minimos_cuadrados(x, y)

    assert a == pytest.approx(2.0)
    assert b == pytest.approx(1.0)

def test_filtrar_supera_umbral(df_mini):
    resultado = filtrar(df_mini, "valor", 20)
    assert resultado["valor"].tolist() == [30.0, 40.0]


def test_top_k_devuelve_mayores(df_mini):
    resultado = top_k(df_mini, "valor", 2)
    assert resultado["valor"].tolist() == [40.0, 30.0]