
apetece_helado_input = input("te apetece un helado? (si / no): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("dime si o no carajo, pa mi has dicho no")
    apetece_helado = False

tiene_dinero_input = input("tienes dinero para un helado? (si / no): ").upper()
senor_helados_input = input("Esta el señor de los helados? (si / no): ").upper()
esta_tu_tia_input = input("Estas con tu tia? (si / no ): ").upper()

apetece_helado = apetece_helado_input == "SI"
tiene_dinero = tiene_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puede_permitirselo = esta_tu_tia or tiene_dinero
senor_helados = senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and senor_helados :
    print("pues comete un helado")
else:
    print("pues nada")