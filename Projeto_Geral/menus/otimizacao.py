from algoritmos.otimizacao.mochila import resolver_mochila_01, resolver_mochila_fracionaria
from algoritmos.otimizacao.corte_barras import resolver_corte_barras
from algoritmos.otimizacao.coin_change import resolver_coin_change_pd, resolver_coin_change_guloso

def menu_otimizacao():
    print("\n--- OTIMIZAÇÃO ---")
    print("1. Mochila 0-1")
    print("2. Mochila Fracionária")
    print("3. Corte de Barras")
    print("4. Coin Change (Troco Mínimo)")
    print("0. Voltar")
    escolha = input("Escolha o problema: ")

    if escolha == "1":
        resolver_mochila_01()
    elif escolha == "2":
        resolver_mochila_fracionaria()
    elif escolha == "3":
        resolver_corte_barras()
    elif escolha == "4":
        print("\n1. Programação Dinâmica")
        print("2. Guloso")
        metodo = input("Escolha o método: ")
        if metodo == "1":
            resolver_coin_change_pd()
        elif metodo == "2":
            resolver_coin_change_guloso()
    elif escolha == "0":
        return
    else:
        print("Opção inválida.")
