phone_book = [{'id':1, 'name':'Емельянов Богдан', 'phone':'89141595196', 'comment':'Мой'},
              {'id':2, 'name':'Панфилов Кирилл', 'phone':'8909***2021', 'comment':'Семинарист GB'},
              {'id':3, 'name':'Тест', 'phone':'000', 'comment':'Тестовый контакт'}]


def prepare_to_save_file(phone_book: list[dict]):   # Преобразование листа справочника к формату для записи в текстовый файл
    new_list = []
    count = 1
    for item in phone_book:
        new_list += item['id'], ':', item['name'], ':', item['phone'], ':', item['comment']
        if count < len(phone_book) - 1:
            new_list += ' /n|'
        count += 1
    i = 0
    while i < len(new_list):
        new_list[i] = str(new_list[i])
        i += 2
    new_list = [''.join(new_list)]
    return new_list


print(prepare_to_save_file(phone_book))


