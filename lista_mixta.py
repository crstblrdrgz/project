
lista_mixta = [3, "coche", 43, "pelota", 23, "cochera"]

lista_numero = []
lista_str = []
for item in lista_mixta:
    tipo=type(item)
    if tipo == str:
        lista_str.append(item)
    else:
        lista_numero.append(item)
print(lista_numero)
print(lista_str)