import datetime

mes = int(input("Mes de nacimiento(numero): "))
dia = int(input("Dia de nacimiento: "))

cumpleanos = datetime.datetime(year=datetime.datetime.now().year, month=mes, day=dia)

dia_restante = cumpleanos - datetime.datetime.now()

dia_semana ={0:"Lunes",
            1:"Martes",
            2:"Miercoles",
            3:"Jueves",
            4:"Viernes",
            5:"Sabado",
            6:"Domingo"}

print("Quedan para tu cumple {}".format(dia_restante))

print("Y sera {}".format(dia_semana[cumpleanos.weekday()]))