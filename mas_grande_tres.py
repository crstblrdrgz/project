

def numero_mas_grande(primero, segundo, tercero):
    numero_grande = 0
    if primero < segundo:
        numero_grande = segundo
    if segundo < tercero:
        numero_grande = tercero
    return numero_grande

print(numero_mas_grande(5, 7, 9))
