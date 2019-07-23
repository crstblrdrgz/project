

def input_con_conformacion (pregunta):
    confirmacion = False
    dato_usuario = ""
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {}, ¿Eestas seguro? [SI / NO] ".format(dato_usuario)).upper()
        if seguro == "SI":
            confirmacion = True
    return dato_usuario



nombre = input_con_conformacion("¿Como te llamas? ")
print("Has confirmado que te llamas {} ".format(nombre))

numero = input_con_conformacion("Dime un numero: ")
print("Has confirmado que el numero es {} ".format(numero))