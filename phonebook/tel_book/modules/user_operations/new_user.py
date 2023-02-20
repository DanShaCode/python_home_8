import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *

def new_user_data(user_data):
    os.system('cs||clear')
    print()
    
    user_info = []
    
    uniqe_id  = str(len(user_data) + 1)
    user_info.append(uniqe_id)

    user_first = input("Введите Имя: ")
    user_info.append(user_first)
 
    print()
    user_second = input("Введите Фамилию: ")
    user_info.append(user_second)
    print()

    user_tel = input("Введите Телефон: ")
    user_info.append(user_tel)
    print()

    user_mail = input("Введите е-mail: ")
    user_info.append(user_mail)
    print()

    user_adress = input("Введите Адрес: ")
    user_info.append(user_adress)
    print()

    user_data.append(user_info)

    print("Нажмите Enter для возврата в Меню ")
    return user_data
