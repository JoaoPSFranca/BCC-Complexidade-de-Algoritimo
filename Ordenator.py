import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = chave

    return arr

def merge(esquerda, direita):
    resultado = []
    i, j = 0, 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2

    esquerda = arr[:meio]
    direita = arr[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)

def partition(lista, inicio, fim):
    pivo = lista[inicio]
    anterior = inicio + 1
    posterior = fim

    while True:
        while anterior <= posterior and lista[anterior] <= pivo:
                anterior += 1
        while anterior <= posterior and lista[posterior] > pivo:
            posterior -= 1

        if anterior <= posterior:
            lista[anterior], lista[posterior] = lista[posterior], lista[anterior]
        else:
            lista[inicio], lista[posterior] = lista[posterior], lista[inicio]
            return posterior

def quick_sort(arr, fim=None, inicio=0):
    if fim is None:
        fim = len(arr) - 1

    if inicio < fim:
        pivo = partition(arr, inicio, fim)
        quick_sort(arr, inicio, pivo - 1)
        quick_sort(arr, pivo + 1, fim)

    return arr

def quick_sort_ramdom(arr, fim=None, inicio=0):
    if fim is None:
        fim = len(arr) - 1

    if inicio < fim:
        pivo = random.randint(0, len(arr))
        quick_sort_ramdom(arr, inicio, pivo - 1)
        quick_sort_ramdom(arr, pivo + 1, fim)

    return arr