import os
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_TXT import *
from modules.data_operations.add_data_CSV import *

def operations_menu(user_data):
    os.system('cs||clear')
    print()
    print("(1) Экспортировать данные в CSV")
    print()
    print("(2) Экспортировать данные в TXT")
    print()
    user_input = int(input("Введите соответствующую цифру из Меню: "))
    if user_input == 1:
        user_data = create_book_csv(user_data)
        return user_data
    if user_input == 2:
        user_data = create_book_txt(user_data)
        return menu(user_data)
    else:
        return user_data