from menus.ordenacao import menu_ordenacao
from menus.busca import menu_busca
from menus.otimizacao import menu_otimizacao
from menus.caixeiro import menu_caixeiro

def main():
    while True:
        print("\n" + "="*40)
        print(" ALGORITMOS CLÁSSICOS INTERATIVOS ")
        print("="*40)
        print("[1] Ordenação")
        print("[2] Busca")
        print("[3] Otimização")
        print("[4] Caixeiro Viajante")
        print("[0] Sair")
        print("="*40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_ordenacao()
        elif opcao == "2":
            menu_busca()
        elif opcao == "3":
            menu_otimizacao()
        elif opcao == "4":
            menu_caixeiro()
        elif opcao == "0":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
