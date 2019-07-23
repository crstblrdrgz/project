

def numero_en_rango(principio, numero, final):
    solucion = None
    if numero >= principio and numero <= final:
        solucion = True
    else:
        solucion = False
    return solucion

print(numero_en_rango(1, 65, 100))

print(numero_en_rango(40, 20, 100))