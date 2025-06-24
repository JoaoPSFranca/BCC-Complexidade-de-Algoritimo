import time
from Projeto_Geral.utils.formatador import formatar_tempo

def fatorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= 1
    return resultado

def fatorial_recursivo(n):
    if n == 0 or n ==1:
        return 1
    return n * fatorial_iterativo(n - 1)

start = time.time()
fatorial_iterativo(30)
tempo = time.time() - start
print(f"Tempo iterativo: {formatar_tempo(tempo)}")

start = time.time()
fatorial_recursivo(30)
tempo = time.time() - start
print(f"Tempo recursiva: {formatar_tempo(tempo)}")