def encontrar_ordem_ineficiente(a, b, c):
    numeros = [a, b, c]
    for i in range(len(numeros)):
        maior = True
        for j in range(len(numeros)):
            if numeros[j] > numeros[i]:
                maior = False
                break
        if maior:
            maior_num = numeros[i]
    for i in range(len(numeros)):
        menor = True
        for j in range(len(numeros)):
            if numeros[j] < numeros[i]:
                menor = False
                break
        if menor:
            menor_num = numeros[i]

    meio_num = sum(numeros) - maior_num - menor_num
    return maior_num, meio_num, menor_num

def otimizado(a, b, c):
    if a > b:
        if a > c:
            maior = a
            meio, menor = (b, c) if b > c else (c, b)
        else:
            maior, meio, menor = c, a, b
    else:
        if b > c:
            maior = b
            meio, menor = (a, c) if a > c else (c, a)
        else:
            maior, meio, menor = c, b, a
    return maior, meio, menor


a, b, c = 3, 1, 4
maior, meio, menor = encontrar_ordem_ineficiente(a, b, c)
print("Ineficiente -> Maior:", maior, "Meio:", meio, "Menor:", menor)

maior, meio, menor = otimizado(a, b, c)
print("orimizado -> Maior:", maior, "Meio:", meio, "Menor:", menor)


# Exemplo 1: Encontrar o número que mais se repete em uma lista
# Código ineficiente
def mais_frequente_ineficiente(lista):
    max_contagem = 0
    mais_frequente = None
    for i in lista:
        contagem = 0
        for j in lista:
            if i == j:
                contagem += 1
        if contagem > max_contagem:
            max_contagem = contagem
            mais_frequente = i
    return mais_frequente

def mais_frequente_otimizado(lista):
    dicio = {}
    for i in lista:
        dicio[i] = dicio[i] + 1 if i in dicio.keys() else 1
    dicio = sorted(dicio.items(), reverse=True, key=lambda item: item[1])
    return dicio[0][0]

lista_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Mais frequente (ineficiente):", mais_frequente_ineficiente(lista_numeros))
print("Mais frequente (otimizado):", mais_frequente_otimizado(lista_numeros))

# Exemplo 2: Encontrar todos os pares de números cuja soma é um valor alvo
# Código ineficiente
def encontrar_pares_ineficiente(lista, alvo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares

def encontrar_pares_otimizado(lista, alvo):
    pares = []
    for i in lista:
        numero = alvo - i
        if numero in lista and (numero, i) not in pares:
            pares.append((i, numero))
    return pares

alvo = 10
print("Mais frequente (ineficiente):", encontrar_pares_ineficiente(lista_numeros, alvo))
print("Mais frequente (otimizado):", encontrar_pares_otimizado(lista_numeros, alvo))
