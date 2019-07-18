

numero_multiplicar = int(input("Numero a multiplicar: "))

for numero in range (10, 0, -1):
    print("{} X {} = {}".format(numero_multiplicar, numero, numero_multiplicar * numero))