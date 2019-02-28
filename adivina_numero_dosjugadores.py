numero_adivinar = (input("Numero a adivinar: "))

ocultar = 100
while ocultar > 0:
    print("ººººººººººººººººººººº")
    ocultar -= 1

intento_adivinar = input("Adivina el numero: ")

while intento_adivinar != numero_adivinar:
    intento_adivinar = input("Adivina el numero: ")
print("FIN")