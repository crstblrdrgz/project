
frase_usuario = input("Di una frase: ")

mayusculas = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Ñ", "L", "K", "J", "H", "G", "F", "D", "S", "A", "Z", "X", "C", "V", "B", "N", "M"]

n_mayusculas = 0

for letra in frase_usuario:
    if letra in mayusculas:
        n_mayusculas += 1

print("Numero de mayusculas {}".format(n_mayusculas))