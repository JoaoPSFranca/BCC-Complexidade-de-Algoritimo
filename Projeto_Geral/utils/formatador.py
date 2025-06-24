def formatar_tempo(segundos):
    milisegundos = segundos * 1000
    horas = int(milisegundos // 3600000)
    milisegundos %= 3600000
    minutos = int(milisegundos // 60000)
    milisegundos %= 60000
    segundos = int(milisegundos // 1000)
    milisegundos %= 1000

    partes = []
    if horas:
        partes.append(f"{horas}h")
    if minutos:
        partes.append(f"{minutos}min")
    if segundos:
        partes.append(f"{segundos}s")
    if milisegundos:
        partes.append(f"{round(milisegundos, 2)}ms")

    return " ".join(partes) if partes else "0ms"
