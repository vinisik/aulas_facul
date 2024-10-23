import numpy as np

matriz = np.array([[3, 4, 1], [3, 1, 5]])

elementos = []
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        elementos.append(matriz[i][j])

soma = sum(elementos)
print(f'Soma = {soma}')