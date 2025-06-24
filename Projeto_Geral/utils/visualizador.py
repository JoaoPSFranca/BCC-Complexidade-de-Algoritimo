import matplotlib.pyplot as plt
import os

def plotar_caminho(coordenadas, caminho, titulo="Caminho do Caixeiro Viajante", filename="images/caminho_tsp.png"):
    x = [coordenadas[i][0] for i in caminho]
    y = [coordenadas[i][1] for i in caminho]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'bo-')
    for i, cidade in enumerate(caminho):
        plt.text(coordenadas[cidade][0], coordenadas[cidade][1], str(cidade), fontsize=12, color='red')

    plt.title(titulo)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(filename)
    plt.close()
    print(f"[Imagem gerada] Caminho salvo em: {os.path.abspath(filename)}")
