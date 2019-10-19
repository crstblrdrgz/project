import pickle
from tkinter import *
from tkinter import ttk

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

def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact


def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    contatc = add_contact(contacts, input("Nombre: "), input("Teléfono: "), input("Email: "))
    print("Se ha añadido el contacto {} correctamente\n".format(contacts["name"]))
    sleep(2)

def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contatc = add_contact(contacts, name, phone, email)
    cols, row = frame_contact_list.grid_size()
    ttk.Label(frame_contact_list, text=contatc["name"]).grid(column=1, row=row)
    ttk.Label(frame_contact_list, text=contatc["email"]).grid(column=2, row=row)
    ttk.Label(frame_contact_list, text=contatc["phone"]).grid(column=3, row=row)

def remove_contact(contacts):
    print("\n\nBorrar contacto\n")
    email_or_name = input("Deseas buscar por: \n1-Nombre  \n2-Email\n")
    if email_or_name == "2":
      buscador_remove("email", contacts)
    if email_or_name == "1":
       buscador_remove("name", contacts)


def find_contact(contacts):

    print("\n\nBuscar contacto\n")
    email_or_name = input("Deseas buscar por: \n1-Nombre  \n2-Email\n")
    if email_or_name == "2":
        buscador("email", contacts)

    if email_or_name == "1":
        buscador("name", contacts)


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



def main():
    contacts = load_contacts()


    root = Tk()

    frame_add_contact = ttk.Frame(root, padding="30 12 30 12")
    frame_add_contact.grid()

    frame_contact_list = ttk.Frame(root, padding="30 12 30 12")
    frame_contact_list.grid()

    name = StringVar()
    email = StringVar()
    phone = StringVar()

    ttk.Label(frame_contact_list, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_contact_list, text="Email").grid(column=2, row=1)
    ttk.Label(frame_contact_list, text="Telefono").grid(column=3, row=1)

    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1, sticky=S)
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1, sticky=S)
    ttk.Label(frame_add_contact, text="Telefono").grid(column=3, row=1, sticky=S)

    name_entry = ttk.Entry(frame_add_contact, width=7, textvariable=name)
    name_entry.grid(column=1, row=2)
    ttk.Entry(frame_add_contact, width=7, textvariable=email).grid(column=2, row=2)
    ttk.Entry(frame_add_contact, width=7, textvariable=phone).grid(column=3, row=2)

    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda: add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
               ).grid(column=3, row=3)
    name_entry.focus()
    for child in frame_add_contact.winfo_children():
        child.grid_configure(padx=5, pady=5)
    for child in frame_contact_list.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
    save_contacts(contacts)
if __name__ == "__main__":
    main()