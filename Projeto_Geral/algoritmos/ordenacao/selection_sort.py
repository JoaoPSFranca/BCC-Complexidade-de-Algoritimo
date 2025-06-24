def selection_sort(arr, verbose=False):
    n = len(arr)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
            if verbose:
                print(f"Troca: {arr}")
    return arr, comparacoes, trocas
