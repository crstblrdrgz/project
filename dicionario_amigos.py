

salida = False
amigos = dict()
while not salida:
    accion = input("¿Que quieres hacer? [Añadir amigo [A] / [Consultar numero [C]/ Salir [S]]:  ").upper()

    if accion == "A":
        print("Vamos a añadir un amigo: ")
        print("---------------------------")
        nombre = input("Nombre: ")
        ano_nacimiento = input("Año nacimiento: ")
        amigos[nombre] = ano_nacimiento

    elif accion == "C":
        print("Consultar numero:")
        print("-------------------------")
        nombre = input("De quien quieres consultar su año de nacimiento: ")
        print(amigos[nombre])


    elif accion == "S":
        salida = True