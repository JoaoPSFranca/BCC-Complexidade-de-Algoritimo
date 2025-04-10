def formatar_tempo(milisegundos):
    milisegundos *= 1000
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