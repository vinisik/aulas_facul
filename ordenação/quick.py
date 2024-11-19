import numpy as np


def quick_sort(vetor):
    if len(vetor) <= 1:
        return vetor

    pivo = vetor[-1]
    esquerda = np.array([x for x in vetor[:-1] if x <= pivo])
    direita = np.array([x for x in vetor[:-1] if x > pivo])

    return np.concatenate((quick_sort(esquerda), [pivo], quick_sort(direita)))


ordenado = quick_sort(np.array([15, 34, 8, 3]))
print(ordenado)
