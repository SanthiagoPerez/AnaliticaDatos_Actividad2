"""Puntos 11 a 16: dispersión, densidad y gráficos de contorno."""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    rng = np.random.default_rng(42)

    # Punto 11: dispersión de dos arrays aleatorios.
    x_aleatorio = rng.random(100)
    y_aleatorio = rng.random(100)
    fig, ax = plt.subplots()
    ax.scatter(x_aleatorio, y_aleatorio, alpha=0.75)
    ax.set(title="11. Gráfico de dispersión aleatoria", xlabel="x", ylabel="y")
    ax.grid(True, alpha=0.25)

    # Puntos 12 y 16: nube con ruido y función seno con etiquetas y leyenda LaTeX.
    x_seno = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y_seno = np.sin(x_seno) + rng.normal(0, 0.3, size=x_seno.size)
    fig, ax = plt.subplots()
    ax.scatter(x_seno, y_seno, s=22, alpha=0.7, label=r"$y=\sin(x)+\epsilon$")
    ax.plot(x_seno, np.sin(x_seno), color="crimson", label=r"$y=\sin(x)$")
    ax.set(
        xlabel="Eje X",
        ylabel="Eje Y",
        title="Gráfico de Dispersión",
    )
    ax.legend()
    ax.grid(True, alpha=0.25)

    # Punto 13: contorno de z = cos(x) + sin(y).
    eje_x = np.linspace(-2 * np.pi, 2 * np.pi, 150)
    eje_y = np.linspace(-2 * np.pi, 2 * np.pi, 150)
    grid_x, grid_y = np.meshgrid(eje_x, eje_y)
    z = np.cos(grid_x) + np.sin(grid_y)
    fig, ax = plt.subplots()
    lineas = ax.contour(grid_x, grid_y, z, levels=20, cmap="viridis")
    ax.clabel(lineas, inline=True, fontsize=8)
    fig.colorbar(lineas, ax=ax, label=r"$z=\cos(x)+\sin(y)$")
    ax.set(title="13. Gráfico de contorno", xlabel="x", ylabel="y")

    # Punto 14: color de cada punto según el conteo de su celda local.
    puntos_x = rng.random(1000)
    puntos_y = rng.random(1000)
    conteos, bordes_x, bordes_y = np.histogram2d(
        puntos_x, puntos_y, bins=30
    )
    indice_x = np.clip(np.digitize(puntos_x, bordes_x) - 1, 0, 29)
    indice_y = np.clip(np.digitize(puntos_y, bordes_y) - 1, 0, 29)
    densidad = conteos[indice_x, indice_y]
    fig, ax = plt.subplots()
    puntos = ax.scatter(puntos_x, puntos_y, c=densidad, cmap="plasma", s=20)
    fig.colorbar(puntos, ax=ax, label="Densidad local (puntos por celda)")
    ax.set(title="14. Dispersión coloreada por densidad", xlabel="x", ylabel="y")

    # Punto 15: contorno lleno de la densidad de y = sin(x) + ruido gaussiano.
    x_nube = rng.uniform(-2 * np.pi, 2 * np.pi, 2000)
    y_nube = np.sin(x_nube) + rng.normal(0, 0.3, size=x_nube.size)
    conteos_nube, bordes_x, bordes_y = np.histogram2d(
        x_nube, y_nube, bins=60
    )
    centros_x = (bordes_x[:-1] + bordes_x[1:]) / 2
    centros_y = (bordes_y[:-1] + bordes_y[1:]) / 2
    fig, ax = plt.subplots()
    niveles = ax.contourf(
        centros_x,
        centros_y,
        conteos_nube.T,
        levels=15,
        cmap="viridis",
    )
    fig.colorbar(niveles, ax=ax, label="Densidad de puntos")
    ax.set(
        title=r"15. Contorno lleno de $y=\sin(x)+\epsilon$",
        xlabel="x",
        ylabel="y",
    )

    plt.show()


if __name__ == "__main__":
    main()
