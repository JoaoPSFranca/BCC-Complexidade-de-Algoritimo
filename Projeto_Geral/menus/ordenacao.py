from utils.gerador import gerar_vetor
from utils.formatador import formatar_tempo
from algoritmos.ordenacao.bubble_sort import bubble_sort
from algoritmos.ordenacao.selection_sort import selection_sort
from algoritmos.ordenacao.insertion_sort import insertion_sort
from algoritmos.ordenacao.merge_sort import merge_sort
from algoritmos.ordenacao.quick_sort import quick_sort
from utils.exportador import salvar_ordenacao

import time

def menu_ordenacao():
    print("\n--- MÓDULO DE ORDENAÇÃO ---")
    tipo = input("Tipo de vetor (aleatória, crescente, decrescente, quase ordenada): ").strip().lower()
    tamanho = int(input("Tamanho do vetor: "))
    visualizar = input("Visualizar passo a passo? (s/n): ").strip().lower() == 's'

    vetor = gerar_vetor(tipo, tamanho)

    print("\nEscolha o algoritmo:")
    print("[1] Bubble Sort")
    print("[2] Selection Sort")
    print("[3] Insertion Sort")
    print("[4] Merge Sort")
    print("[5] Quick Sort")
    print("[0] Voltar")
    escolha = input("Opção: ")

    algoritmos = {
        "1": ("Bubble Sort", bubble_sort),
        "2": ("Selection Sort", selection_sort),
        "3": ("Insertion Sort", insertion_sort),
        "4": ("Merge Sort", merge_sort),
        "5": ("Quick Sort", quick_sort)
    }

    if escolha in algoritmos:
        nome, funcao = algoritmos[escolha]
        print(f"\nExecutando {nome}...")
        inicio = time.time()
        vetor, comparacoes, trocas = funcao(vetor.copy(), verbose=visualizar)
        tempo = time.time() - inicio

        print("\nVetor ordenado:", vetor)
        print("Tempo de execução:", formatar_tempo(tempo))
        print("Comparações:", comparacoes)
        print("Trocas:", trocas)

        salvar = input("Deseja exportar os resultados em CSV? (s/n): ").lower() == 's'
        if salvar:
            salvar_ordenacao(nome, vetor, vetor.copy(), comparacoes, trocas, tempo)

    elif escolha == "0":
        return
    else:
        print("Opção inválida.")
