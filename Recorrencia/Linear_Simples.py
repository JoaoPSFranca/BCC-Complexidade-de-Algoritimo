def somar_lista(list, i=0):
    if i == (len(list) - 1):
        return list[i]
    else:
        return list[i] + somar_lista(list, i+1)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

soma = somar_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fat = fatorial(5)

print(f"somar_lista: {soma} | fatorial: {fat}")