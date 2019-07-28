


import datetime

hoy = datetime.datetime.now()

cinco_dias_atras = hoy - datetime.timedelta(days=5)

dia_semana ={0:"Lunes",
            1:"Martes",
            2:"Miercoles",
            3:"Jueves",
            4:"Viernes",
            5:"Sabado",
            6:"Domingo"}

print(cinco_dias_atras.strftime("Hace cinco dias era el %d del mes %m del año %Y"))

print("Y era {}".format(dia_semana[cinco_dias_atras.weekday()]))