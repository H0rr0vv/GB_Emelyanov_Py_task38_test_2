from view import menu, show_contacts, print_message, input_contact, input_return, prepare_to_save_file
import model
from view import text



def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
                print_message(text.open_successful)
            case 2:
                new_list = prepare_to_save_file(model.phone_book)
                model.save_file(new_list)
                flag = True
            case 3:
                show_contacts(model.phone_book)                
            case 4:
                new = input_contact(text.input_new_contact)
                model.add_contact(new)
                print_message(text.contact_saved(new.get('name')))
                flag = False
            case 5:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
            case 6:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
                model.change(int(index), new)
                old_name = model.phone_book[int(index) - 1].get('name')
                print_message(text.contact_change(new.get('name') if new.get('name') else old_name))
                flag = False
            case 7:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index_del)
                old_name = model.phone_book[int(index) - 1].get('name')
                model.del_contact(int(index))
                print_message(text.contact_delete(old_name))
                flag = False
            case 8:
                if flag == False:
                    exit_quesion = input(print(text.save_reminder))
                    if exit_quesion == 'Y' or 'y':
                        break
                    else:
                        new_list = prepare_to_save_file(model.phone_book)
                        model.save_file(new_list)
                        break
                else:
                    break
                    
                