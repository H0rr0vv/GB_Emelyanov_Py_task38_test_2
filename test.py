phone_book = [{'id':1, 'name':'Емельянов Богдан', 'phone':'89141595196', 'comment':'Мой'},
              {'id':2, 'name':'Панфилов Кирилл', 'phone':'8909***2021', 'comment':'Семинарист GB'},
              {'id':3, 'name':'Тест', 'phone':'000', 'comment':'Тестовый контакт'}]


def prepare_to_save_file(phone_book: list[dict]):   # Преобразование листа справочника к формату для записи в текстовый файл
    new = []
    count = 0
    for item in phone_book:
        new += item['id'], ':', item['name'], ':', item['phone'], ':', item['comment']
        if count < len(phone_book) - 1:
            new += ' /n|'
        count += 1
    i = 0
    while i < len(new):
        new[i] = str(new[i])
        i += 1
    new = [''.join(new)]
    return new


print(prepare_to_save_file(phone_book))


