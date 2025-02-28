def buscar_valor(matriz, valor):
    """Busca un valor en una matriz bidimensional."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor encontrado en la posición ({i}, {j})"
    return "Valor no encontrado"

# Matriz bidimensional de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 6

# Realizar la búsqueda
resultado = buscar_valor(matriz, valor_a_buscar)

print(f"Matriz original:\n{matriz}")
print(f"Resultado de la búsqueda: {resultado}")


def bubble_sort(fila):
    """Ordena una lista utilizando Bubble Sort."""
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Matriz bidimensional de ejemplo
matriz = [
    [5, 2, 8],
    [4, 9, 1],
    [7, 6, 3]
]

# Fila a ordenar (en este caso, la primera fila)
fila_a_ordenar = 2

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila seleccionada
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
