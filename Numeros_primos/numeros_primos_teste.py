import random
import time
import math
from sympy import primerange

# Função para verificar se n é um número primo segundo o AKS
def aks_primality_test(n):
    # Caso trivial
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Encontrar r, a maior base que divide (n-1) de forma não trivial
    r = find_r(n)

    # Se r for encontrado, verificamos o comportamento de n com números primos até r
    if r <= math.log(n) ** 2:
        return True

    # O Teste de Polinômios
    return polynomial_test(n, r)


def find_r(n):
    # Função para encontrar o menor r tal que o ordem de n mod r seja pequeno
    for r in range(2, n):
        # Usamos simplificação para exemplos de implementações
        if order_of_n_mod_r(n, r) > math.log(n) ** 2:
            return r
    return n


def order_of_n_mod_r(n, r):
    # Calcula a ordem de n mod r (simplificado)
    return n % r


def polynomial_test(n, r):
    # Teste de polinômio AKS (simplificado, não o algoritmo completo)
    primes = list(primerange(2, int(math.sqrt(n)) + 1))
    for p in primes:
        if n % p == 0:
            return False
    return True


def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def miller_rabin_test(n, k=5):
    # Caso trivial para n < 2
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True

    # Escreve n-1 como 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Teste de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = modular_exponentiation(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = modular_exponentiation(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Testando o código com alguns números
if __name__ == "__main__":
    start1 = time.time()
    print(f"O número 100: ")
    for i in range(1, 100):
        print(f"{i}: {miller_rabin_test(i)}")
    end1 = time.time()

    start2 = time.time()
    print(f"O número 1.000: ")
    for i in range(1, 1000):
        print(f"{i}: {miller_rabin_test(i)}")
    end2 = time.time()

    start3 = time.time()
    print(f"O número 1.000.000: ")
    for i in range(1, 1000000):
        print(f"{i}: {miller_rabin_test(i)}")
    end3 = time.time()

    print("miller_rabin_test: ")
    print(f"\nTempo 1: {(end1 - start1) * 1000}s")
    print(f"Tempo 2: {(end2 - start2) * 1000}s")
    print(f"Tempo 3: {(end3 - start3) * 1000}s")
