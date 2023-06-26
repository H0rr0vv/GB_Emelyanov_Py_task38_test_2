from .text import *
from model import PhoneBook, Contact


def menu () -> int:             # Выбор пункта меню
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print (input_error)


def show_contacts(book: PhoneBook):           # Отображение контактов
    if book.contacts:
        print('\n' + '=' * 67)
        for contact in book.contacts:
            print(contact)
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
    new = Contact(input(new_contact[0]), input(new_contact[1]), input(new_contact[2]))
    return new


def input_return(message: str) -> str:              # Вывод сообщения
    return input(message)


def prepare_to_save_file(book: PhoneBook):   # Преобразование листа справочника к формату для записи в текстовый файл
    new = []
    count = 0
    for contact in book.contacts:
        new += contact.uid, ':', contact.name, ':', contact.phone, ':', contact.comment
        if count < len(book.contacts) - 1:
            new += '\n'
        count += 1
    i = 0
    while i < len(new):
        new[i] = str(new[i])
        i += 1
    new = [''.join(new)]
    return new