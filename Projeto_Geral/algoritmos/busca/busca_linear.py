def busca_linear(lista, alvo):
    comparacoes = 0
    for i, elemento in enumerate(lista):
        comparacoes += 1
        if elemento == alvo:
            return i, comparacoes
    return -1, comparacoes
