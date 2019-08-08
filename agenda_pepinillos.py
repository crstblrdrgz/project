import pickle

from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")

    return int(selected_action)


def buscador_remove(elemento, contacts):
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0
    contador_real = []
    contador_real_numero = 0
    numero_final = 0
    for contact in contacts:
        contador_real.append(contact[elemento])
        if contact[elemento].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact[elemento]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("\n\nNo se ha encontrado ninguno.\n")
        return
    print("\nSe ha borrado {}\n".format(found_contacts[contact_index][elemento]))

    for item in contador_real:
        contador_real_numero += 1
        if item == found_contacts[contact_index][elemento]:
            numero_final += contador_real_numero - 1

    contacts.pop(numero_final)
    sleep(2)



def buscador(tipo, contacts):
        search_term = input("Introducir el Email del contacto o parte de él: ")
        found_contacts = []

        print("He encontrado los siguientes contactos:")
        contact_indexes = []
        contact_counter = 0

        for contact in contacts:
            if contact[tipo].find(search_term) >= 0:
                found_contacts.append(contact)
                print("{} - {}".format(contact_counter, contact[tipo]))
                contact_indexes.append(contact_counter)
                contact_counter += 1

        contact_index = 0

        if len(contact_indexes) > 1:
            contact_index = ask_until_option_expected(contact_indexes)
        elif len(contact_indexes) == 0:
            print("No se ha encontrado ninguno.")
            volver_preguntar = input("¿Deseas volver a buscar?(S/N): ")
            if volver_preguntar == "S":
                find_contact(contacts)
            return

        print("\nInformación sobre {}\n".format(found_contacts[contact_index][tipo]))
        print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
        sleep(5)


def show_menu():
    print("\n\nAcciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(1)

def remove_contact(contacts):
    print("\n\nBorrar contacto\n")
    email_or_name = input("Deseas buscar por: \n1-Nombre  \n2-Email\n")
    if email_or_name == "2":
      buscador_remove("email", contacts)
    if email_or_name == "1":
       buscador_remove("nombre", contacts)


def find_contact(contacts):

    print("\n\nBuscar contacto\n")
    email_or_name = input("Deseas buscar por: \n1-Nombre  \n2-Email\n")
    if email_or_name == "2":
        buscador("email", contacts)

    if email_or_name == "1":
        buscador("nombre", contacts)


def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")



def main():
    contacts = load_contacts()
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()

        action = show_menu()

    save_contacts(contacts)
    print("¡Adiós!")


if __name__ == "__main__":
    main()