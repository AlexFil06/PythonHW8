from view import menu, show_contacts, new_contact_input, find_contact, input_ind
from data import open_file, get, add, save, find_o, change, delete




def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                open_file()
            case 2:
                save()
            case 3:
                pb = get()
                show_contacts(pb)
            case 4:
                new = new_contact_input()
                add(new)
            case 5:
                pb = get()
                show_contacts(pb)
                ind = input_ind()
                contact = new_contact_input()
                change(ind, contact)

            case 6:
                find = find_contact()
                result = find_o(find)
                show_contacts(result)
            case 7:
                pb = get()
                show_contacts(pb)
                ind = input_ind()
                delete(ind)
            case 8:
                print('До свидания!')
                break
