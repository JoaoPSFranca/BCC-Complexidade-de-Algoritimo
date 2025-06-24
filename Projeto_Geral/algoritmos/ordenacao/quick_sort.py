def quick_sort(arr, verbose=False):
    comparacoes = 0
    trocas = 0

    def quick_sort_rec(v):
        nonlocal comparacoes, trocas

        if len(v) <= 1:
            return v

        pivo = v[0]
        menores = []
        maiores = []

        for x in v[1:]:
            comparacoes += 1
            if x <= pivo:
                menores.append(x)
            else:
                maiores.append(x)

        if verbose:
            print(f"Pivô: {pivo} | Menores: {menores} | Maiores: {maiores}")

        esquerda = quick_sort_rec(menores)
        direita = quick_sort_rec(maiores)
        trocas += len(esquerda) + len(direita) + 1  # concatenação efetiva

        return esquerda + [pivo] + direita

    resultado = quick_sort_rec(arr)
    for i in range(len(arr)):
        arr[i] = resultado[i]
    return arr, comparacoes, trocas
