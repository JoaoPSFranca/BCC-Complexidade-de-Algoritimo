def resolver_coin_change_pd():
    moedas = [1, 2, 5]
    valor = 11
    dp = [float('inf')] * (valor + 1)
    dp[0] = 0

    for m in moedas:
        for i in range(m, valor + 1):
            dp[i] = min(dp[i], dp[i - m] + 1)

    print(f"Moedas mínimas (PD): {dp[valor]}")

def resolver_coin_change_guloso():
    moedas = [5, 2, 1]
    valor = 11
    moedas.sort(reverse=True)
    count = 0
    usados = []

    for m in moedas:
        while valor >= m:
            valor -= m
            count += 1
            usados.append(m)

    print(f"Moedas mínimas (guloso): {count}")
    print("Usadas:", usados)
