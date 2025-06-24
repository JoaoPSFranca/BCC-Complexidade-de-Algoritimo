def tsp_2opt(matriz):
    from random import randint

    def custo(caminho):
        return sum(matriz[caminho[i]][caminho[i+1]] for i in range(len(caminho)-1))

    def trocar_2opt(caminho, i, k):
        return caminho[:i] + caminho[i:k+1][::-1] + caminho[k+1:]

    n = len(matriz)
    caminho = list(range(n)) + [0]
    melhor = caminho
    melhor_custo = custo(caminho)

    melhorou = True
    while melhorou:
        melhorou = False
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                novo = trocar_2opt(melhor, i, k)
                novo_custo = custo(novo)
                if novo_custo < melhor_custo:
                    melhor = novo
                    melhor_custo = novo_custo
                    melhorou = True
        caminho = melhor

    return melhor, melhor_custo
