import random
import time

from Projeto_Geral.utils.formatador import formatar_tempo

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

def sorts(n):
    print(f"{n} elementos: ")
    arr = []
    for i in range(n):
        x = random.randint(1, 100)
        arr.append(x)

    start = time.time()
    list_bubble = bubble_sort(arr[:])
    end = time.time() - start
    # print(f"Lista ordenada: {list_bubble}")
    print(f"Tempo de execução do bubble sort: {formatar_tempo(end)}")

    start = time.time()
    list_selection = selection_sort(arr[:])
    end = time.time() - start
    # print(f"Lista ordenada: {list_selection}")
    print(f"Tempo de execução do selection sort: {formatar_tempo(end)}")

    start = time.time()
    list_insertion = insertion_sort(arr[:])
    end = time.time() - start
    print(f"Tempo de execução do insertion sort: {formatar_tempo(end)}")
    # print(f"Lista ordenada: {list_insertion}\n")

    start = time.time()
    sorted(arr[:])
    end = time.time() - start
    print(f"Tempo de execução do sorted: {formatar_tempo(end)}\n")

sorts(10)
sorts(100)
sorts(1000)
sorts(10000)
sorts(100000)