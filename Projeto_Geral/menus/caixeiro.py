from algoritmos.tsp.forca_bruta import tsp_forca_bruta
from algoritmos.tsp.nearest_neighbor import tsp_nearest_neighbor
from algoritmos.tsp.held_karp import tsp_held_karp
from algoritmos.tsp.opt2 import tsp_2opt
from utils.formatador import formatar_tempo
from utils.visualizador import plotar_caminho
from utils.exportador import salvar_tsp

import time
import random

def gerar_coordenadas(cidades):
    return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(cidades)]

def calcular_dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def calcular_matriz(coordenadas):
    n = len(coordenadas)
    matriz = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matriz[i][j] = calcular_dist(coordenadas[i], coordenadas[j])
    return matriz

def menu_caixeiro():
    print("\n--- CAIXEIRO VIAJANTE ---")
    n = int(input("Quantidade de cidades: "))
    modo = input("Coordenadas aleatórias? (s/n): ").lower() == 's'

    if modo:
        coords = gerar_coordenadas(n)
    else:
        coords = []
        for i in range(n):
            x = float(input(f"Cidade {i+1} - X: "))
            y = float(input(f"Cidade {i+1} - Y: "))
            coords.append((x, y))

    matriz = calcular_matriz(coords)

    print("\nMétodos disponíveis:")
    print("[1] Força Bruta")
    print("[2] Held-Karp")
    print("[3] Nearest Neighbor")
    print("[4] 2-opt")
    print("[0] Voltar")
    escolha = input("Opção: ")

    inicio = time.time()
    if escolha == "1":
        caminho, custo = tsp_forca_bruta(matriz)
    elif escolha == "2":
        caminho, custo = tsp_held_karp(matriz)
    elif escolha == "3":
        caminho, custo = tsp_nearest_neighbor(matriz)
    elif escolha == "4":
        caminho, custo = tsp_2opt(matriz)
    elif escolha == "0":
        return
    else:
        print("Opção inválida.")
        return

    tempo = time.time() - inicio
    print(f"\nCaminho: {caminho}")
    print(f"Custo total: {custo:.2f}")
    print(f"Tempo: {formatar_tempo(tempo)}")
    plotar_caminho(coords, caminho)

    salvar = input("Deseja exportar os resultados em CSV? (s/n): ").lower() == 's'
    if salvar:
        salvar_tsp(caminho, custo, coords)


