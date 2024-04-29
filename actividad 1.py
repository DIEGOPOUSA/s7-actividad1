

import numpy as np

matriz = np.random.randint(0, 101, size=(3, 3))

promedio = np.mean(matriz)

suma = np.sum(matriz)

elemento_mayor = np.max(matriz)

elemento_menor = np.min(matriz)

diagonal_principal = np.diag(matriz)


print("Matriz:\n", matriz)
print("Promedio de los elementos:", promedio)
print("Suma de los elementos:", suma)
print("Elemento mayor:", elemento_mayor)
print("Elemento menor:", elemento_menor)
print("Elementos de la diagonal principal:", diagonal_principal)
