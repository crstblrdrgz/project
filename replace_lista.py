
valores_a_sustituir = [1, 2, "hola", "adios"]

str_a_cambiar = "hola, numero {}, numero {}, {} y {}"

for valor in valores_a_sustituir:
    str_a_cambiar = str_a_cambiar.replace("{}",str(valor), 1)
print(str_a_cambiar)