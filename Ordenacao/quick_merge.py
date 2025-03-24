import random
import time

from Formatador import formatar_tempo
from Ordenator import *

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
    print(f"Tempo de execução do sorted: {formatar_tempo(end)}")

    start = time.time()
    list_merge = merge_sort(arr[:])
    end = time.time() - start
    print(f"Tempo de execução do merge sort: {formatar_tempo(end)}")
    # print(f"Lista ordenada: {list_insertion}\n")

    start = time.time()
    list_quick = quick_sort(arr[:])
    end = time.time() - start
    print(f"Tempo de execução do quick sort: {formatar_tempo(end)}")
    # print(f"Lista ordenada: {list_insertion}\n")

    start = time.time()
    list_quick = quick_sort_ramdom(arr[:])
    end = time.time() - start
    print(f"Tempo de execução do quick sort random: {formatar_tempo(end)}\n")
    # print(f"Lista ordenada: {list_insertion}\n")

sorts(10)
sorts(100)
sorts(1000)
sorts(10000)
sorts(100000)