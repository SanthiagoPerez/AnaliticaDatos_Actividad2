"""Puntos 6 a 10: broadcasting e indexado de arrays."""

import numpy as np


def main() -> None:
    rng = np.random.default_rng(42)

    columna = np.array([[1], [2], [3]])
    fila = np.array([[10, 20, 30]])
    print("6. Suma con broadcasting (3x1 + 1x3):")
    print(columna + fila)

    matriz_5x5 = np.arange(1, 26).reshape(5, 5)
    print("\n7. Submatriz 2x2 desde la segunda fila y columna:")
    print(matriz_5x5[1:3, 1:3])

    ceros = np.zeros(10, dtype=int)
    ceros[3:7] = 5
    print("\n8. Array con los índices 3, 4, 5 y 6 modificados:")
    print(ceros)

    matriz_3x3 = np.arange(1, 10).reshape(3, 3)
    print("\n9. Matriz con sus filas en orden inverso:")
    print(matriz_3x3[::-1, :])

    valores = rng.random(10)
    print("\n10. Valores aleatorios mayores que 0.5:")
    print(valores[valores > 0.5])


if __name__ == "__main__":
    main()
