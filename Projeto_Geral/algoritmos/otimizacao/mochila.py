def resolver_mochila_01():
    pesos = [2, 3, 4, 5]
    valores = [3, 4, 5, 6]
    capacidade = 5
    n = len(pesos)

    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    print(f"Valor máximo: {dp[n][capacidade]}")
    print("Tabela:")
    for linha in dp:
        print(linha)

def resolver_mochila_fracionaria():
    pesos = [10, 20, 30]
    valores = [60, 100, 120]
    capacidade = 50

    razao = [(valores[i]/pesos[i], pesos[i], valores[i]) for i in range(len(pesos))]
    razao.sort(reverse=True)

    total = 0
    for r, p, v in razao:
        if capacidade >= p:
            capacidade -= p
            total += v
        else:
            total += r * capacidade
            break

    print(f"Valor máximo (fracionária): {total:.2f}")
