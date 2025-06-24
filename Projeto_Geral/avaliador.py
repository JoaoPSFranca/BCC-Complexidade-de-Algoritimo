import time
import matplotlib.pyplot as plt
from utils.gerador import gerar_vetor
from algoritmos.ordenacao.bubble_sort import bubble_sort
from algoritmos.ordenacao.selection_sort import selection_sort
from algoritmos.ordenacao.insertion_sort import insertion_sort
from algoritmos.ordenacao.merge_sort import merge_sort
from algoritmos.ordenacao.quick_sort import quick_sort

algoritmos = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

def testar_algoritmos(tamanho, tipo='aleatória'):
    tempos = {}
    for nome, funcao in algoritmos.items():
        vetor = gerar_vetor(tipo, tamanho)
        inicio = time.time()
        _, _, _ = funcao(vetor.copy(), verbose=False)
        tempo = time.time() - inicio
        tempos[nome] = tempo
    return tempos

def gerar_grafico(tamanhos, tipo='aleatória'):
    resultados = {nome: [] for nome in algoritmos}

    for tamanho in tamanhos:
        print(f"Testando com {tamanho} elementos...")
        tempos = testar_algoritmos(tamanho, tipo)
        for nome in resultados:
            resultados[nome].append(tempos[nome])

    for nome in resultados:
        plt.plot(tamanhos, resultados[nome], label=nome, marker='o')

    plt.title(f"Comparação de Tempo - Vetor {tipo.capitalize()}")
    plt.xlabel("Tamanho do vetor")
    plt.ylabel("Tempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"images/grafico_{tipo}.png")
    plt.show()

if __name__ == "__main__":
    tamanhos = [10, 100, 500, 1000]
    gerar_grafico(tamanhos, tipo='aleatória')
