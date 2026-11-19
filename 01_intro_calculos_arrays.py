import numpy as np

def main() -> None:
    rng = np.random.default_rng(42)

    print("1. Array con valores desde 10 hasta 29:")
    print(np.arange(10, 30))

    print("\n2. Suma de una matriz 10x10 llena de unos:")
    print(np.ones((10, 10), dtype=int).sum())

    array_a = rng.integers(1, 11, size=5)
    array_b = rng.integers(1, 11, size=5)
    print("\n3. Producto elemento a elemento:")
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}")
    print(f"Producto: {array_a * array_b}")

    filas, columnas = np.indices((4, 4))
    matriz = filas + columnas
    print("\n4. Matriz definida por i + j:")
    print(matriz)
    if np.linalg.matrix_rank(matriz) < matriz.shape[0]:
        print("La matriz es singular y no tiene inversa ordinaria.")
        print("Pseudoinversa de Moore-Penrose:")
        print(np.linalg.pinv(matriz))
    else:
        print(f"Inversa:\n{np.linalg.inv(matriz)}")

    valores = rng.random(100)
    indice_minimo = int(np.argmin(valores))
    indice_maximo = int(np.argmax(valores))
    print("\n5. Mínimo y máximo de 100 valores aleatorios:")
    print(f"Mínimo: {valores[indice_minimo]:.4f}, índice: {indice_minimo}")
    print(f"Máximo: {valores[indice_maximo]:.4f}, índice: {indice_maximo}")


if __name__ == "__main__":
    main()
