import time
import math
from functools import lru_cache
from Formatador import formatar_tempo

def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

@lru_cache(None)
def fibonacci_memo(n):
    if n <=1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

def fibonacci_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi ** n - (1 - phi) ** n) / math.sqrt(5))

start = time.time()
fibonacci_iterativo(35)
tempo = time.time() - start
print(f"Tempo iterativo: {formatar_tempo(tempo)}")

start = time.time()
fibonacci_recursivo(35)
tempo = time.time() - start
print(f"Tempo recursivo: {formatar_tempo(tempo)}")

start = time.time()
fibonacci_memo(35)
tempo = time.time() - start
print(f"Tempo memo: {formatar_tempo(tempo)}")

start = time.time()
fibonacci_binet(35)
tempo = time.time() - start
print(f"Tempo binet: {formatar_tempo(tempo)}")