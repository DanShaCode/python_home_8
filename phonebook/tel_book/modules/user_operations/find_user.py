import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *

def user_search(user_data):
    os.system('cs||clear')
    print()
    print("  -= Телефонный справочник =-")
    print()
    print("       ПОИСК КОНТАКТА")
    print()
    print("=================================")
    print()
    print("(1) Найти контакт")
    print()
    print("(Enter) Назад в Основное меню")
    print()
    print('----------------------------------')
    print()
    user_await = input("Введите соответствующую цифру из меню: ")
    if user_await == '' or user_await == ' ':
        return user_data
    if user_await == '1':
        os.system('cs||clear')
        find_input = str(input("Введите данные пользователя: "))
        print()
        os.system('cs||clear')
        for user in user_data:
            flag = 0
            for data in user:
                if find_input in data:
                    if flag == 0:
                        print(f"ID : {user[0]} | FIRST NAME : {user[1]} | SECOND NAME: {user[2]} | TEL : {user[3]} | E-MAIL: {user[4]} | ADRESS : {user[5]}")
                    flag += 1
                    if flag == 1:
                        continue
        print()
        user_await = input("Нажмите Enter ")
        if user_await == '' or user_await == ' ':
            return user_data
        else:
            return user_data