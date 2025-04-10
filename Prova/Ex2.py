import time
from Formatador import formatar_tempo

# 2 - Considere a seguinte função que calcula o n-esimo numero de Fibonacci

# a) Analise a complexidade de tempo da função abaixo
def fibonacci_ineficiente(n):
    if n <= 1:
        return n
    else:
        return fibonacci_ineficiente(n - 1) + fibonacci_ineficiente(n - 2)

# b) Reescreva uma função mais eficiente dessa função implemente
# benckmarking comparando o tempo das duas versões para n=35
def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = 35

    start = time.time()
    fibonacci_ineficiente(n)
    ineficiente = time.time() - start
    ineficiente = formatar_tempo(ineficiente)
    print(f"Tempo recursivo (ineficiente): {ineficiente}")

    start = time.time()
    fibonacci_iterativo(n)
    eficiente = time.time() - start
    eficiente = formatar_tempo(eficiente)
    print(f"Tempo iterativo (mais eficiente): {eficiente}")

    print(f"\nO tempo explícito na função de fibonacci recursiva, pode ser observada com um tempo muito maior, \nlevando cerca de {ineficiente}, enquanto o código em sua forma iterativa leva um tempo de cerca de {eficiente}. \nCom isso, podemos confirmar a grande ineficiência do código. ")