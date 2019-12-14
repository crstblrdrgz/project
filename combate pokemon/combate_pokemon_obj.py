

class Pokemon:
    vida_base = 100
    ataque = 10
    nombre = "pokemon"

    def __init__(self):
        self.vida = self.vida_base

    def atacar(self, enemigo):
        enemigo.recibir_danio(self.ataque)
    def recibir_danio(self, danio):
        self.vida -= danio
    def mostrar_vida(self):
        print("vida de {} :  {}".format(self.nombre, self.vida))



class Charmander(Pokemon):
    vida_base = 120
    ataque = 11
    nombre = "Charmander"

class Pikachu(Pokemon):
    vida_base = 75
    ataque = 21
    nombre = "Pikachu"

class Bulbasur(Pokemon):
    vida_base = 150
    ataque = 8
    nombre = "Bulbasur"

class Squirtle(Pokemon):
    vida_base = 100
    ataque = 14
    nombre = "Squirtle"