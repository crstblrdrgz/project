
frase_usuario = input("Di una frase: ")

vocales = ["a", "e", "i", "o", "u"]

lista_final = []
for letra in frase_usuario:
    if letra in vocales:
        lista_final.append(letra)


print(lista_final)