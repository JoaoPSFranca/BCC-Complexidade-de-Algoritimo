from collections import deque
import time

def formatar_tempo(milisegundos):
    horas = milisegundos // 3600000
    milisegundos %= 3600000
    minutos = milisegundos // 60000
    milisegundos %= 60000
    segundos = milisegundos // 1000
    milisegundos %= 1000

    if horas != 0:
        return f"{horas}h {minutos}m {segundos}s {round(milisegundos, 2)}ms"
    elif minutos != 0:
        return f"{minutos} minutos, {segundos} segundos, {round(milisegundos, 2)} milissegundos"
    elif segundos != 0:
        return f"{segundos}s {round(milisegundos, 2)}ms"
    elif milisegundos != 0:
        return f"{round(milisegundos, 2)}ms"

def comparar_fila_pilha():
    pilha = []
    start_time = time.time()
    for i in range(5    00000):
        pilha.append(1)
    while pilha:
        pilha.pop()
    pilha_time = time.time() - start_time

    fila = deque()
    start_time = time.time()
    for i in range(500000):
        fila.append(i)
    while fila:
        fila.popleft()
    fila_time = time.time() - start_time

    lista = []
    start_time = time.time()
    for i in range(500000):
        lista.append(i)
    while lista:
        lista.pop(0)
    lista_time = time.time() - start_time

    print(f"Tempo de operação na pilha: {formatar_tempo(pilha_time * 1000)}")
    print(f"Tempo de operação na fila: {formatar_tempo(fila_time * 1000)}")
    print(f"Tempo de operação na lista: {formatar_tempo(lista_time * 1000)}")

comparar_fila_pilha()