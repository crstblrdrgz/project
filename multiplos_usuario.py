
numeros_usuario =""

lista_numeros = []

while numeros_usuario != "FIN":
 numeros_usuario = input("Introduce los numeros(escribe FIN para parar): ")
 if numeros_usuario != "FIN":
  while not numeros_usuario.isdigit():
      numeros_usuario = input("Introduce los numeros(escribe FIN para parar): ")
  lista_numeros.append(int(numeros_usuario))
  print("Numero añadido")







multiplo_dos =[]
multiplo_tres =[]
multiplo_cinco =[]
multiplo_siete =[]

for numero in lista_numeros:
 if numero % 2 == 0:
  multiplo_dos.append(numero)
 if numero % 3 == 0:
  multiplo_tres.append(numero)
 if numero % 5 == 0:
  multiplo_cinco.append(numero)
 if numero % 7 == 0:
  multiplo_siete.append(numero)


print("Multiplos de dos: {}".format(multiplo_dos))
print("Multiplo de tres: {}".format(multiplo_tres))
print("Multiplo de cinco: {}".format(multiplo_cinco))
print("Multiplo de siete: {}".format(multiplo_siete))




























