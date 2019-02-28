
frase_usuario = input("Dime una frase: ")

espacios = [" "]
puntos = ["."]
comas = [","]
n_espacios = 0
n_puntos = 0
n_comas = 0

for letra in frase_usuario:
    if letra in espacios:
        n_espacios += 1
    elif letra in puntos:
        n_puntos += 1
    elif letra in comas:
        n_comas += 1

print("Numero de espacios {}".format(n_espacios))
print("Numero de comas {}".format(n_comas))
print("Numero de puntos {}".format(n_puntos))