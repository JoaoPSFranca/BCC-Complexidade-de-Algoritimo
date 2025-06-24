import csv
import os
from datetime import datetime

def salvar_ordenacao(nome_algoritmo, vetor_entrada, vetor_saida, comparacoes, trocas, tempo):
    nome_arquivo = f"resultado_ordenacao_{nome_algoritmo.lower().replace(' ', '_')}.csv"
    caminho = os.path.abspath(nome_arquivo)

    with open(nome_arquivo, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Algoritmo", nome_algoritmo])
        writer.writerow(["Data", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        writer.writerow(["Tempo (s)", f"{tempo:.6f}"])
        writer.writerow(["Comparações", comparacoes])
        writer.writerow(["Trocas", trocas])
        writer.writerow([])
        writer.writerow(["Vetor de Entrada"])
        writer.writerow(vetor_entrada)
        writer.writerow(["Vetor Ordenado"])
        writer.writerow(vetor_saida)

    print(f"[CSV gerado] Ordenação salva em: {caminho}")

def salvar_tsp(caminho, custo_total, coordenadas):
    nome_arquivo = "resultado_tsp.csv"
    caminho_abs = os.path.abspath(nome_arquivo)

    with open(nome_arquivo, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Data", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        writer.writerow(["Custo total", f"{custo_total:.2f}"])
        writer.writerow(["Caminho"])
        writer.writerow(caminho)
        writer.writerow([])
        writer.writerow(["Coordenadas das cidades"])
        writer.writerow(["Cidade", "X", "Y"])
        for i, (x, y) in enumerate(coordenadas):
            writer.writerow([i, x, y])

    print(f"[CSV gerado] Caminho TSP salvo em: {caminho_abs}")
