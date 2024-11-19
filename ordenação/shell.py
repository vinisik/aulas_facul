import numpy as np


def shell_sort(vetor):
    intervalo = len(vetor)

    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
            intervalo //= 2

    return vetor


ordenado = shell_sort(np.array([15, 34, 8, 3]))
print(ordenado)