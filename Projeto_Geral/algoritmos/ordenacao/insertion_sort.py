def insertion_sort(arr, verbose=False):
    comparacoes = 0
    trocas = 0

    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                trocas += 1
                j -= 1
                if verbose:
                    print(f"Movendo: {arr}")
            else:
                break
        arr[j + 1] = chave
    return arr, comparacoes, trocas
