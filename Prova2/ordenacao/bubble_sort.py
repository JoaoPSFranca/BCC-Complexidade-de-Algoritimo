def bubble_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
    return comparacoes, trocas
