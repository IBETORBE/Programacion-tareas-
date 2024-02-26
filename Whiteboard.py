def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return True, i, j
    return False, None, None

# Definir una matriz de ejemplo
matriz_ejemplo = [
    [1, 3, 4],
    [2, 9, 6],
    [7, 8, 9]
]

# Valor a buscar en la matriz
valor_buscado = 7

# Realizar la búsqueda
encontrado, fila, columna = buscar_valor(matriz_ejemplo, valor_buscado)

# Mostrar el resultado
if encontrado:
    print(f"El valor {valor_buscado} se encontró en la posición ({fila}, {columna}) de la matriz.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")