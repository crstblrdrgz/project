
tipo_operacion = input("Que operacion quieres realizar? (multiplicar / dividir / sumar / restar): ").upper()

primer_numero = (int(input("Primer numero: ")))
segundo_numero = (int(input("Segundo numero: ")))

if tipo_operacion == "MULTIPLICAR":
    resultado = primer_numero * segundo_numero

elif tipo_operacion == "DIVIDIR":
    resultado = primer_numero / segundo_numero

elif print("Resultado: {} ".format(resultado))tipo_operacion == "SUMAR":
    resultado = primer_numero + segundo_numero

elif tipo_operacion == "RESTAR":
    resultado = primer_numero - segundo_numero

