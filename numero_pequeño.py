

numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario= ""
    print("¡Numero añadido!")

numero_pequeño = 9999999999

for numero in numeros_usuario:
    if numero_pequeño > numero:
        numero_pequeño = numero
print("El numero mas pequeño es: {}".format(numero_pequeño))