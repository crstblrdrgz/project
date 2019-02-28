
pokemon_elegido = input("¿Contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 9

elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasaur"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque vamos ha usar?(Chispazo / Bola voltio): ").upper()
    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
    elif ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -=12

    print("la vida del {} ahora es de {}".format(nombre_pokemon, vida_enemigo))

    print("{} te hace un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("la vida de Pikachu ahora es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")
elif vida_pikachu <=0:
    print("¡Has perido!")

print("el combate ha terminado")