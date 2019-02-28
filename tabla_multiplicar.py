
numero_tabla = int(input("Tabla de multiplicar del numero: "))

par = 0

for multiplo in range (1, 11):
    if multiplo%2 == 0:
        print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))