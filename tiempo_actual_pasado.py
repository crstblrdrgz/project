import datetime


ano = int(input("Introduce el año: "))
mes = int(input("Introduce el mes: "))
dia = int(input("Introduce el dia: "))

fecha_introducida = datetime.datetime(year=ano, month=mes, day=dia)

tiempo_pasado = datetime.datetime.now() - fecha_introducida

print("Han pasado {} Horas".format(int(tiempo_pasado.total_seconds()/60/60)))