
texto_usuario = input("Introduce un texto: ")

lista_vocales = ["a", "e", "o", "u"]

for vocal in lista_vocales:
    texto_final = texto_usuario = texto_usuario.replace(vocal, "i")
print(texto_final)