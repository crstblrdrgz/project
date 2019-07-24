
apariciones_palabras = {"Hola":0,
                        "como":0,
                        "estas":0,
                        "amigo":0}

frase = "Hola Hola como estas amigo amigo amigo"
palabra_contador = ""

def contador(palabra):
    if palabra in palabra_contador:
        apariciones_palabras[palabra] +=1

for letra in frase:
    palabra_contador += letra
    contador("Hola")
    palabra_contador = palabra_contador.replace("Hola", "nada")
    contador("como")
    palabra_contador = palabra_contador.replace("como", "nada")
    contador("estas")
    palabra_contador = palabra_contador.replace("estas", "nada")
    contador("amigo")
    palabra_contador = palabra_contador.replace("amigo", "nada")






print(apariciones_palabras)