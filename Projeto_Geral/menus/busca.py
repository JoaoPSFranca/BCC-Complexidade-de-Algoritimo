from utils.gerador import gerar_vetor
from algoritmos.busca.busca_linear import busca_linear
from algoritmos.busca.busca_binaria import busca_binaria
import time
from utils.formatador import formatar_tempo

def menu_busca():
    print("\n--- BUSCA ---")
    tipo_vetor = input("Tipo de vetor (aleatória, crescente): ").strip()
    tamanho = int(input("Tamanho do vetor: "))
    vetor = gerar_vetor(tipo_vetor, tamanho)

    try:
        alvo = int(input("Elemento a ser buscado: "))
    except ValueError:
        print("Valor inválido.")
        return

    print("\n[1] Busca Linear\n[2] Busca Binária\n[0] Voltar")
    opcao = input("Escolha o algoritmo: ")

    if opcao == "1":
        inicio = time.time()
        pos, comps = busca_linear(vetor, alvo)
        tempo = time.time() - inicio
        print(f"\nBusca Linear → Posição: {pos} | Comparações: {comps} | Tempo: {formatar_tempo(tempo)}")
    elif opcao == "2":
        vetor.sort()
        inicio = time.time()
        pos, comps = busca_binaria(vetor, alvo)
        tempo = time.time() - inicio
        print(f"\nBusca Binária → Posição: {pos} | Comparações: {comps} | Tempo: {formatar_tempo(tempo)}")
    elif opcao == "0":
        return
    else:
        print("Opção inválida.")
