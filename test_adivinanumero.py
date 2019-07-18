import os

borrarPantalla = lambda: os.system ("cls")

numero_adivinar = (input("Numero a adivinar: "))

borrarPantalla()

intento_adivinar = input("Adivina el numero: ")

while intento_adivinar != numero_adivinar:
  intento_adivinar = input("Adivina el numero: ")

print("FIN")