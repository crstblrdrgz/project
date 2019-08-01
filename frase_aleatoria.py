import random
import time
first_list = ["El ", "Un ", "algun ", "cualquier "]
second_list = ["coche ", "torpedo ", "gato ", "pajaro "]
third_list = ["es rojo", "se ha perdido", "ha explotado", "voló"]


while True:
    time.sleep(3)
    aleatorio_1 = random.randint(0, 3)
    aleatorio_2 = random.randint(0, 3)
    aleatorio_3 = random.randint(0, 3)
    frase = first_list[aleatorio_1] + second_list[aleatorio_2] + third_list[aleatorio_3]
    print(frase)
    frase = ""