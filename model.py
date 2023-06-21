phone_book = []
path = 'phones.txt'


def open_file():                                                                # открытие файла
    with open(path, 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment = contact.strip().split(':')
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})


def check_id():                                                                     # Проверка id
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list) + 1}



def add_contact(new: dict):                                                     # Добавление контакта
    new.update(check_id())
    phone_book.append(new)


def search(word: str) -> list[dict]:                                        # Поиск контакта
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):                                        # Изменение контакта
    for key, field in new.items():
        if field != '':
             phone_book[index - 1][key] = field


def del_contact(index: int):                           # Удаление контакта
    phone_book.pop(int(index) - 1)
    uid = 1
    for item in phone_book:
        item['id'] = int(uid)
        uid += 1
    return phone_book
