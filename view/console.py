from .text import *

def menu () -> int:             # Выбор пункта меню
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print (input_error)

def show_contacts(book: list[dict[str,str]]):           # Отображение контактов
    if book:
        print('\n' + '=' * 67)
        for contact in book:
            uid = contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{uid:>3}. {name:<20} {phone:<20} {comment:<20}')
        print('=' * 67 + '\n')
    else:
        print(book_error)

def print_message(message: str):                    # Вывод сообщения о статусе операции
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')

def input_contact(message: str) -> dict[str, str]:          # Присвоение данных?      
    print(message)
    name = input(new_contact[0])
    phone = input(new_contact[1])
    comment = input(new_contact[2])
    return {'name': name, 'phone': phone, 'comment': comment}


def input_return(message: str) -> str:              # Вывод сообщения
    return input(message)


def prepare_to_save_file(phone_book: list[dict]) -> list:   # Преобразование листа справочника к формату для записи в текстовый файл
    new = []
    count = 0
    for item in phone_book:
        new += item['id'], ':', item['name'], ':', item['phone'], ':', item['comment']
        if count < len(phone_book) - 1:
            new += '|'
        count += 1
    new = [''.join(new)]
    new:list = new[0].split('|')
    return new