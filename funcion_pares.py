
mis_numeros = [3, 6, 8, 98, 22, 54, 65, 7, 11, 13]

def numeros_pares(lista):
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares




print(numeros_pares(mis_numeros))