

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
    response = None
    while response != "S" and response != "N":
        response = input(mensage + "[S/N]")
    return response == "S"

print_with_inderscores("¡Averigua cuanto te queda de vida!")

print("Completa esta encuenta para saber cuanto tiempo de vida te queda")

birth_date = input("¿Cual es tu fecha de nacimiento? (formato: dd/mm/aaaa): ")



birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

years_lost = 0

if ask_yes_or_not("¿Fumas?"):
    years_lost += SMOKER_PENALIZATION
if ask_yes_or_not("¿Bebes?"):
    years_lost += DRINKER_PENALIZATION
if not ask_yes_or_not("¿Haces deporte?"):
    years_lost += SEDENTARY_PENALIZATION

base_lifespan = random.randint(AVERAGE_LIFESPAN -20, AVERAGE_LIFESPAN)
lifespan = base_lifespan - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de tu muerte {}, Te quedan {} dias de vida, Que son {} años".format(death_day.strftime("%d/%m/%Y"), days_to_death.days, int(days_to_death.days/365)))