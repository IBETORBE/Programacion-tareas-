def ordenar_fila(matriz, fila):
    # Utilizamos el algoritmo de ordenación de selección
    for i in range(len(matriz[fila])):
        min_index = i
        for j in range(i+1, len(matriz[fila])):
            if matriz[fila][j] < matriz[fila][min_index]:
                min_index = j
        matriz[fila][i], matriz[fila][min_index] = matriz[fila][min_index], matriz[fila][i]

# Definimos la matriz de ejemplo
matriz = [
    [4, 2, 1],
    [6, 5, 3],
    [9, 8, 7]
]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos una fila específica (por ejemplo, la segunda fila)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)