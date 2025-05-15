def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def busca_binaria(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio
    elif lista[meio] > alvo:
        return busca_binaria(lista, alvo, inicio, meio - 1)
    else:
        return busca_binaria(lista, alvo, meio + 1, fim)

lista = [1, 3, 5, 7, 9, 11]
alvo = 7
bin = busca_binaria(lista, alvo, 0, len(lista) - 1)
fibo = fibonacci(10)

print(f"busca_binaria: {bin} | fibonacci: {fibo}")