def merge_sort(arr):
    comparacoes = 0
    trocas = 0

    def merge_sort_rec(v):
        nonlocal comparacoes, trocas

        if len(v) > 1:
            meio = len(v) // 2
            L = v[:meio]
            R = v[meio:]

            merge_sort_rec(L)
            merge_sort_rec(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                comparacoes += 1
                if L[i] < R[j]:
                    v[k] = L[i]
                    i += 1
                else:
                    v[k] = R[j]
                    j += 1
                trocas += 1
                k += 1

            while i < len(L):
                v[k] = L[i]
                i += 1
                k += 1
                trocas += 1

            while j < len(R):
                v[k] = R[j]
                j += 1
                k += 1
                trocas += 1

    merge_sort_rec(arr)
    return comparacoes, trocas
