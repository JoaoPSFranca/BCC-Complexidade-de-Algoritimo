import itertools

def tsp_forca_bruta(matriz):
    n = len(matriz)
    cidades = list(range(n))
    melhor_custo = float('inf')
    melhor_caminho = []

    for perm in itertools.permutations(cidades[1:]):
        caminho = [0] + list(perm) + [0]
        custo = sum(matriz[caminho[i]][caminho[i+1]] for i in range(n))
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_caminho = caminho

    return melhor_caminho, melhor_custo
