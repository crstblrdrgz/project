
import random
from time import sleep


print("Adivina un numero del 1 al 10")
numero_usuario = int(input("Di el numero: "))
numero_aleatorio = random.randint(1, 10)

if numero_usuario == numero_aleatorio:
    sleep(3)
    print("Muy bien, era el {}".format(numero_aleatorio))
else:
    sleep(3)
    print("Lo siento, era el {}".format(numero_aleatorio))