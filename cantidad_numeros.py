

numeros_usuario = []
numero_input = ""
print("Contador de numeros")

while numero_input != "FIN":
    numero_input = input("Di un numero: ")
    if numero_input != "FIN":
        numeros_usuario.append(int(numero_input))
        numero_input = ""
        print("¡Nnumero añadido!")

largo_lista = 0

for numero in numeros_usuario:
    largo_lista += 1

print("la lista tiene {} numeros de longitud".format(largo_lista))