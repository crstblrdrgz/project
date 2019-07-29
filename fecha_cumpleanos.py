import datetime
ano = int(input("Año de nacimiento(numero): "))
mes = int(input("Mes de nacimiento(numero): "))
dia = int(input("Dia de nacimiento(numero): "))

cumpleanos = datetime.datetime(year=ano, month=mes, day=dia)
hoy = datetime.datetime.now()
if cumpleanos.month > datetime.datetime.now().month:
    cumpleanos = datetime.datetime(year=datetime.datetime.now().year, month=mes, day=dia)

else:
    ano = datetime.datetime.now().year + 1
    cumpleanos = datetime.datetime(year=ano, month=mes, day=dia)

dia_restante = cumpleanos - hoy

dia_semana ={0:"Lunes",
            1:"Martes",
            2:"Miercoles",
            3:"Jueves",
            4:"Viernes",
            5:"Sabado",
            6:"Domingo"}

print("Quedan para tu cumple {}".format(dia_restante))

print("Y sera {} ".format(dia_semana[cumpleanos.weekday()]))