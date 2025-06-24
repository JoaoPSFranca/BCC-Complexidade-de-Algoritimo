def tsp_nearest_neighbor(matriz):
    n = len(matriz)
    visitados = [False] * n
    caminho = [0]
    visitados[0] = True
    atual = 0
    custo_total = 0

    for _ in range(n - 1):
        prox = min((j for j in range(n) if not visitados[j]),
                   key=lambda j: matriz[atual][j])
        custo_total += matriz[atual][prox]
        caminho.append(prox)
        visitados[prox] = True
        atual = prox

    caminho.append(0)
    custo_total += matriz[atual][0]
    return caminho, custo_total
