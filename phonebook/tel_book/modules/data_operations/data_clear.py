import os
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *

def remove_all_data(user_data):
    os.system('cs||clear')
    print()
    print("Внимание! Данная процедура приведет к удалению всех данных из справочника")
    print()
    print("Уверены, что хотите продолжить?")
    print()
    user_await = input("Введите Y/N: ")
    if user_await == 'Y' or user_await == 'y':
        os.system('cs||clear')
        user_data.clear()
        print()
        print("Данные удалены")
        print()
        user_await = input("Нажмите Enter")
        return user_data
    else:
        return user_data