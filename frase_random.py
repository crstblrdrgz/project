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


while True:
    sleep(1)
    segundo = datetime.datetime.now().second
    if segundo > 9:
        segundo = datetime.datetime.now().second % 10
        aleatorio = random.randint(0, len(frases[segundo]))
        print(frases[segundo][aleatorio - 1])
    else:
        aleatorio = random.randint(0, len(frases[segundo]))
        print(frases[segundo][aleatorio - 1])