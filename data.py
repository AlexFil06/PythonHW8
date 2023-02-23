phone_book = []
path = 'phone.txt'


def open_file():
    global phone_book
    global path
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    for i in data:
        new = i.strip().split('-')
        contact = {}
        contact['name'] = new[0]
        contact['phone'] = new[1]
        contact['comment'] = new[2]
        phone_book.append(contact)
    print('Файл открыт!')
    file.close()


def get():
    global phone_book
    return phone_book


def add(new_contact: list[dict]):
    global phone_book
    phone_book.append(new_contact)


def save():
    global phone_book
    global path
    data = []
    for i in phone_book:
        new = '-'.join(i.values())
        data.append(new)
    data = '\n'.join(data)
    file = open(path, 'w', encoding='UTF-8')
    file.write(data)
    print('Контакт сохранен!')
    file.close


def find_o(find_option: str):
    global phone_book
    all_find = []
    for i in phone_book:
        for j in i.values():
            if find_option in j:
                all_find.append(i)
    return all_find


def change(ind: int, contact: dict):
    global phone_book
    phone_book.pop(ind - 1)
    phone_book.insert(ind-1, contact)
    print('Контакт изменен!')


def delete(ind):
    global phone_book
    phone_book.pop(ind - 1)
    print('Контакт удален!')
