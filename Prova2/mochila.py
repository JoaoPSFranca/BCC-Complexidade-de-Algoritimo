def resolver_mochila_01(pesos, valores, capacidade):
    n = len(pesos)

    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    print(f"Valor máximo: {dp[n][capacidade]}")
    resp = ""

    print(dp[-1])

    for item in dp[-1]:
        if item == 60:
            resp += "Corda "
        elif item == 40:
            resp += "Lanterna "
        elif item == 100:
            resp += "Barraca "
        elif item == 50:
            resp += "Comida"
        elif item == 30:
            resp += "Filtro "

    print(f"Mochila result: {resp}")
