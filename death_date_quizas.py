
import datetime
import random

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 9
SEDENTARY_PENALIZATION = 7

def print_with_inderscores(mensage):
    print(mensage)
    print(len(mensage)* "-")

def ask_yes_or_not(mensage):
    response = ""
    while response != "S" and response != "N" and response != "Q":
        response = input(mensage + "[S/N/Q]")
    return response


print_with_inderscores("¡Averigua cuanto te queda de vida!")

print("Completa esta encuenta para saber cuanto tiempo de vida te queda")

birth_date = input("¿Cual es tu fecha de nacimiento? (formato: dd/mm/aaaa): ")

years_lost = 0

fumar =ask_yes_or_not("¿fumas?")

if fumar == "S":
    years_lost += SMOKER_PENALIZATION
elif fumar == "Q":
    years_lost += SMOKER_PENALIZATION / 2

beber = ask_yes_or_not("¿Bebes?")

if beber == "S":
    years_lost += DRINKER_PENALIZATION
elif beber == "Q":
    years_lost *= DRINKER_PENALIZATION / 2

deporte = ask_yes_or_not("¿Haces deporte?")

if deporte == "N":
    years_lost += SEDENTARY_PENALIZATION
elif deporte == "Q":
    years_lost *= SEDENTARY_PENALIZATION / 2

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")




base_lifespan = random.randint(AVERAGE_LIFESPAN -20, AVERAGE_LIFESPAN)
lifespan = base_lifespan - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de tu muerte {}, Te quedan {} dias de vida, Que son {} años".format(death_day.strftime("%d/%m/%Y"), days_to_death.days, int(days_to_death.days/365)))