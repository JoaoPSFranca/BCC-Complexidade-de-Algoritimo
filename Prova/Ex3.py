# 3 – O código abaixo conta quantos pares de elementos em uma lista de inteiros
# nums possuem valores iguais.
from uaclient.files.notices import remove


def contar_pares_iguais(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                count += 1
    return count

# Esse código possui complexidade O(n²) por verificar todos os pares possíveis.
# a) Justifique por que o algoritmo possui complexidade O(n²).
# R. O código verifica cada item da lista n vezes, então por exemplo, em uma lista
# de 5 elementos, cada elemento será verificado 5x gerando dando um total de 25 verificações,
# ou seja, 5².

# b) Reescreva o algoritmo com complexidade O(n), utilizando apenas estruturas
# básicas do Python.
def contar_pares_iguais_reformed(nums):
    count = 0
    counts = {}

    for i in nums:
        if i in counts.keys():
            counts[i] = (counts[i] * 2) + 1
        else:
            counts[i] = 0
        print(counts)

    count = sum(counts.values())

    return count

num = [1, 2, 1, 2, 1]
count = contar_pares_iguais_reformed(num)
print(count)