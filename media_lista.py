

numeros_usuario = []
numeros_input = ""

while numeros_input != "FIN":
    numeros_input = input("Escibe un numero (FIN para finalizar): ")
    if numeros_input != "FIN":
        numeros_usuario.append(int(numeros_input))
        print("¡Se ha añadido un numero")

suma_numeros = 0

for numero in numeros_usuario:
    suma_numeros += numero
media = suma_numeros / len(numeros_usuario)
print("Media {} ".format(media))