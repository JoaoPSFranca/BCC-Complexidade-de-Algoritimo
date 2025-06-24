import random

def gerar_vetor(tipo: str, tamanho: int) -> list:
    if tipo == 'aleatória':
        return [random.randint(1, 100) for _ in range(tamanho)]
    elif tipo == 'crescente':
        return list(range(1, tamanho + 1))
    elif tipo == 'decrescente':
        return list(range(tamanho, 0, -1))
    elif tipo == 'quase ordenada':
        vetor = list(range(1, tamanho + 1))
        # embaralha 10% dos elementos
        for _ in range(max(1, tamanho // 10)):
            i, j = random.sample(range(tamanho), 2)
            vetor[i], vetor[j] = vetor[j], vetor[i]
        return vetor
    else:
        raise ValueError(f"Tipo de vetor inválido: {tipo}")
