import time
from Projeto_Geral.utils.formatador import formatar_tempo

def soma_lista_iterativa(lista):
    soma = 0
    for element in lista:
        soma += element
    return soma

def soma_lista_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista_recursiva(lista[1:])

start = time.time()
soma_lista_iterativa(range(998))
tempo = time.time() - start
print(f"tempo de iterativa: {formatar_tempo(tempo)}")

start = time.time()
soma_lista_recursiva(range(998))
tempo = time.time() - start
print(f"tempo de recursiva: {formatar_tempo(tempo)}")
