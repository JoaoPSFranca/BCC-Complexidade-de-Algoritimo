import random
import matplotlib.pyplot as plt
import numpy as np
import time
from mochila import resolver_mochila_01
from ordenacao.bubble_sort import bubble_sort
from ordenacao.selection_sort import selection_sort
from ordenacao.insertion_sort import insertion_sort
from ordenacao.merge_sort import merge_sort
from ordenacao.quick_sort import quick_sort
from ordenacao.heap_sort import heap_sort


def plot_comparacao(resultados):
    nomes = [r[0] for r in resultados]
    tempos = [r[1] for r in resultados]
    comparacoes = [r[2] for r in resultados]
    trocas = [r[3] for r in resultados]

    x = np.arange(len(nomes))
    largura = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x - largura, tempos, largura, label='Tempo (s)')
    ax.bar(x, comparacoes, largura, label='Comparações')
    ax.bar(x + largura, trocas, largura, label='Trocas')

    ax.set_xticks(x)
    ax.set_xticklabels(nomes)
    ax.set_ylabel('Valores')
    ax.set_title('Comparação entre métodos')
    ax.legend()
    plt.title("Gráfico das Comparações")
    plt.savefig(f"comparacoes.png")
    plt.close()


def comparar_tudo():
    random.seed(42)

    nomes = ['Bubble', 'Selection', 'Insertion', 'Merge', 'Quick', 'Heap']
    vetor = [random.randint(0, 100) for _ in range(10000)]
    resultados = []

    for m in range(1, 7):
        arr = vetor.copy()
        start = time.time()
        if m == 1:
            c, s = bubble_sort(arr)
        elif m == 2:
            c, s = selection_sort(arr)
        elif m == 3:
            c, s = insertion_sort(arr)
        elif m == 4:
            c, s = merge_sort(arr)
        elif m == 5:
            c, s = quick_sort(arr)
        elif m == 6:
            c, s = heap_sort(arr)
        end = time.time()
        resultados.append((nomes[m - 1], end - start, c, s))

        print(f"Foi {m}")

    plot_comparacao(resultados)

if __name__ == "__main__":
    print("Mochila")
    print("="*40)

    pesos = [3, 2, 6, 4, 1]
    valores = [60, 40, 100, 50, 30]
    resolver_mochila_01(pesos, valores, 10)

    print("="*40)

    comparar_tudo()

    print("acabou")
