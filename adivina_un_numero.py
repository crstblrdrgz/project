number_to_guess = 14

user_number = int(input("Adivina un numero: "))

if user_number == number_to_guess:
    print("has ganado")
else:
    print("Has perdido")

    try_again = int(input("Intentalo de nuevo: "))
    if try_again == number_to_guess:
        print("Has ganado")
    else:
        print("Has perdido")
        try_again = int(input("Intentalo de nuevo: "))
        if try_again == number_to_guess:
            print("Has ganado")
        else:
            print("Has perdido")
            try_again = int(input("Intentalo de nuevo: "))
            if try_again == number_to_guess:
                print("Has ganado")
            else:
                print("Has perdido")
                try_again = int(input("Intentalo de nuevo: "))
                if try_again == number_to_guess:
                    print("Has ganado")
                else:
                    print("Has perdido")