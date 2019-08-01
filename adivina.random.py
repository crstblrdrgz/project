import datetime
from time import sleep
import random
"""
frase_alegre = ["que buen dia hace", "me alegra verte", "chocolate para todos", "kebad a mitad de precio", "pizza para cenar", "felicidades!"]
muebles = ["silla", "puerta", "cama", "sofa", "mesita", "repisa", "estante"]
bebidas = ["refresco", "cafe", "gintonic", "batido", "coctel", "agua"]
frase_odio = ["tus muertos", " a ver si te muere", "desgraciao", "asqueroso", "hijo de puta", "cara mierda"]
comidas = ["kebad", "paella", "pizza", "puchero", "choco frito", "coquinas", "pollo empanado"]
frase_absurda = ["un plato es un plato", "un bonobus, ¿que es eso?", "muy españoles y mucho español", "Es el vecino el que elige al alcalde y es el alcalde el que quiere que sean los vecinos el alcalde", "Los chuches, nos suben hasta el IVA de los chuches"]
nombre_animales = ["lagarto", "tortuga", "perro", "gato", "escorpion", "araña", "aguila", "delfin"]
frase_motivadora = ["tu puedes", "ya falta poco para conseguirlo", "no te rindas", "solo un poco mas", "un ultimo esfuerzo"]
sonidos_animales = ["muuuuuu", "guau guau", "piooo piooo", "cuack cuack", "croack croack", "miiaaaauu"]
frases_tristes = ["que solo estoy", "nadie me quiere", "la pizzeria esta cerrada", "se cancelo el plan de hoy"]

"""
frases = [["que buen dia hace", "me alegra verte", "chocolate para todos", "kebad a mitad de precio", "pizza para cenar", "felicidades!"], ["silla", "puerta", "cama", "sofa", "mesita", "repisa", "estante"], ["refresco", "cafe", "gintonic", "batido", "coctel", "agua"], ["tus muertos", " a ver si te muere", "desgraciao", "asqueroso", "hijo de puta", "cara mierda"], ["kebad", "paella", "pizza", "puchero", "choco frito", "coquinas", "pollo empanado"], ["un plato es un plato", "un bonobus, ¿que es eso?", "muy españoles y mucho español", "Es el vecino el que elige al alcalde y es el alcalde el que quiere que sean los vecinos el alcalde", "Los chuches, nos suben hasta el IVA de los chuches"], ["lagarto", "tortuga", "perro", "gato", "escorpion", "araña", "aguila", "delfin"], ["tu puedes", "ya falta poco para conseguirlo", "no te rindas", "solo un poco mas", "un ultimo esfuerzo"], ["muuuuuu", "guau guau", "piooo piooo", "cuack cuack", "croack croack", "miiaaaauu"], ["que solo estoy", "nadie me quiere", "la pizzeria esta cerrada", "se cancelo el plan de hoy"]]

lista_de_unos = [1, 11, 21, 31, 41, 51]
lista_de_dos = [2, 12, 22, 32, 42, 52]
lista_de_tres = [3, 13, 23, 33, 43, 53]
lista_de_cuatro = [4, 14, 24, 34, 44, 54]
lista_cinco = [5, 15, 25, 35, 45, 55]
lista_seis = [6, 16, 26, 36, 46, 56]
lista_siete = [7, 17, 27, 37, 47, 57]
lista_ocho = [8, 18, 28, 38, 48, 58]
lista_nueve = [9, 19, 29, 39, 49, 59]
lista_cero = [0, 10, 20, 30, 40, 50]
while True:
    sleep(1)
    segundo = datetime.datetime.now().second

    for numero in lista_de_unos:
        if numero == segundo:
            segundo = 1
    for numero_dos in lista_de_dos:
        if numero_dos == segundo:
            segundo = 2
    for numero_tres in lista_de_tres:
        if numero_tres == segundo:
            segundo = 3
    for nnumero_cuatro in lista_de_cuatro:
        if nnumero_cuatro == segundo:
            segundo = 4
    for numero_cinco in lista_cinco:
        if numero_cinco == segundo:
            segundo = 5
    for numero_seis in lista_seis:
        if numero_seis == segundo:
            segundo = 6
    for numero_siete in lista_siete:
        if numero_siete == segundo:
            segundo = 7
    for numero_ocho in lista_ocho:
        if numero_ocho == segundo:
            segundo = 8
    for numero_nueve in lista_nueve:
        if numero_nueve == segundo:
            segundo = 9
    for numero_cero in lista_cero:
        if numero_cero == segundo:
            segundo = 0
    aleatorio = random.randint(0, len(frases[segundo]))
    print(frases[segundo][aleatorio - 1])