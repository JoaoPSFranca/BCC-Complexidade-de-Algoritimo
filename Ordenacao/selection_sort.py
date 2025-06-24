import random
import time
from Projeto_Geral.utils.formatador import formatar_tempo

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+i], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = []
for i in range(50):
    x = random.randint(1,100)
    arr.append(x)

start = time.time()
list_bubble = bubble_sort(arr)
end = time.time() - start
print(f"Lista ordenada: {list_bubble}")
print(f"Tempo de execução do bubble sort: {formatar_tempo(end)}")

start = time.time()
list_selection = selection_sort(arr)
end = time.time() - start
print(f"Lista ordenada: {list_selection}")
print(f"Tempo de execução do selection sort: {formatar_tempo(end)}")
