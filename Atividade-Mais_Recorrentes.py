import random
import time
from collections import Counter

def count(numeros, dicio):
    for numero in numeros:
        if numero in dicio.keys():
            dicio[numero] += 1
        else:
            dicio[numero] = 1

def count_otimizado(numeros):
    quant = Counter(numeros)
    return quant.most_common(3)

if __name__ == "__main__":
    numeros = []
    dicio = {}
    for x in range(100000):
        numeros.append(random.randint(1, 100))

    start = time.time()
    count(numeros, dicio)
    dicio_sort = sorted(dicio.items(), key=lambda item: item[1], reverse=True)
    end = time.time()

    start2 = time.time()
    dicio_sort2 = count_otimizado(numeros)
    end2 = time.time()
    print(f"""
Tempo de ordenação: 
Meu código: {(end - start) * 1000}ms
Código otimizado: {(end2 - start2) * 1000}ms

Números mais repetidos e quantidade de vezes:
{dicio_sort[0][0]} = {dicio_sort[0][1]}
{dicio_sort[1][0]} = {dicio_sort[1][1]}
{dicio_sort[2][0]} = {dicio_sort[2][1]}""")
