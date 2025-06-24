def resolver_corte_barras():
    precos = [1, 5, 8, 9, 10, 17, 17, 20]
    n = len(precos)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], precos[j] + dp[i - j - 1])

    print(f"Lucro máximo: {dp[n]}")
