

texto_usuario = input("introduce un texto: ")

lista_vocales = ["a", "e", "o", "u", "i"]
contador = 0
texto_final = []
resultado = ""
for caracter in texto_usuario:
    if caracter in lista_vocales:
        contador += 1
        texto_final.append(str(contador))
    else:
        texto_final.append(caracter)
print(resultado.join(texto_final))