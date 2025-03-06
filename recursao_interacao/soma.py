import time
from Formatador import formatar_tempo

def soma_recursiva(n):
    if n == 1:
        return 1
    return n + soma_recursiva(n - 1)

def soma_iterativa(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

start = time.time()
soma_iterativa(30)
tempo = time.time() - start
print(f"tempo de iterativo: {formatar_tempo(tempo)}")

start = time.time()
soma_recursiva(30)
tempo = time.time() - start
print(f"tempo de recursiva: {formatar_tempo(tempo)}")
