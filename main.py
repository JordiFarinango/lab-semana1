import matplotlib.pyplot as plt
import numpy as np

from src.analisis import recta_minimos_cuadrados, resumen_por_grupo, top_k
from src.carga import cargar, limpiar, reporte_nulos

URL = "https://archive.ics.uci.edu/static/public/183/data.csv"


def main():
    # 1. Cargar dataset crudo
    df_crudo = cargar(URL, na_values=["?"])

    # 2. Reporte de nulos antes de limpiar
    print("\n=== REPORTE DE NULOS DEL DATASET CRUDO ===")
    print(reporte_nulos(df_crudo))

    # 3. Limpiar dataset
    df_limpio = limpiar(df_crudo)

    # 4. Resumen por grupo
    print("\n=== RESUMEN POR ESTADO ===")
    resumen = resumen_por_grupo(
        df_limpio,
        "state",
        ["PopDens", "ViolentCrimesPerPop"],
    )
    print(resumen)

    # 5. Top 5 de criminalidad violenta por poblacion
    print("\n=== TOP 5 ViolentCrimesPerPop ===")
    top = top_k(df_limpio, "ViolentCrimesPerPop", 5)
    print(top[["communityname", "ViolentCrimesPerPop"]])

    # 6. Recta de minimos cuadrados
    x = df_limpio["PopDens"].to_numpy()
    y = df_limpio["ViolentCrimesPerPop"].to_numpy()

    pendiente, intercepto = recta_minimos_cuadrados(x, y)

    print("\n=== RECTA DE MINIMOS CUADRADOS ===")
    print(f"Pendiente: {pendiente}")
    print(f"Intercepto: {intercepto}")

    # 7. Grafico
    plt.scatter(x, y, alpha=0.4)

    orden = np.argsort(x)
    plt.plot(
        x[orden],
        pendiente * x[orden] + intercepto,
    )

    plt.xlabel("Densidad poblacional (PopDens)")
    plt.ylabel("Crimenes violentos por poblacion")
    plt.title("PopDens vs ViolentCrimesPerPop")

    plt.savefig("figura.png")
    plt.close()

    print("\nGrafico guardado como figura.png")


if __name__ == "__main__":
    main()