"""Puntos 16 a 20: histogramas de distribuciones normales."""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    rng = np.random.default_rng(42)
    datos = rng.normal(loc=0, scale=1, size=1000)
    media = datos.mean()

    # Punto 16: histograma de una distribución normal.
    # Punto 19: línea vertical para la media.
    fig, ax = plt.subplots()
    ax.hist(datos, bins=30, color="steelblue", edgecolor="white")
    ax.axvline(
        media,
        color="darkred",
        linestyle="--",
        linewidth=2,
        label=f"Media = {media:.2f}",
    )
    ax.set(
        title="16 y 19. Histograma normal y su media",
        xlabel="Valor",
        ylabel="Frecuencia",
    )
    ax.legend()

    # Punto 18: comparar distintas cantidades de bins.
    fig, axes = plt.subplots(1, 3, figsize=(13, 4), sharey=True)
    for ax, cantidad_bins in zip(axes, (10, 30, 50)):
        ax.hist(datos, bins=cantidad_bins, color="slateblue", edgecolor="white")
        ax.set(title=f"{cantidad_bins} bins", xlabel="Valor")
        ax.grid(axis="y", alpha=0.2)
    axes[0].set_ylabel("Frecuencia")
    fig.suptitle("18. Efecto del número de bins")
    fig.tight_layout()

    # Puntos 17 y 20: dos distribuciones normales en histogramas superpuestos.
    datos_a = rng.normal(loc=0, scale=1, size=1000)
    datos_b = rng.normal(loc=2, scale=0.7, size=1000)
    fig, ax = plt.subplots()
    ax.hist(
        datos_a,
        bins=30,
        alpha=0.55,
        color="royalblue",
        label=r"$N(0,1)$",
    )
    ax.hist(
        datos_b,
        bins=30,
        alpha=0.55,
        color="darkorange",
        label=r"$N(2,0.7^2)$",
    )
    ax.set(
        title="17 y 20. Histogramas superpuestos",
        xlabel="Valor",
        ylabel="Frecuencia",
    )
    ax.legend()

    plt.show()


if __name__ == "__main__":
    main()
