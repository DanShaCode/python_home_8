import os
import time
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *

def user_change(user_data):
    os.system('cs||clear')
    print()
    user_input = str(input("Введите id персоны или 'q' для выхода в Основное меню: "))
    if user_input != 'q':
        for id in user_data:
            for user_info in id:
                if user_input == id[0]:
                        print()
                        print(f"ID : {id[0]} | FIRST NAME : {id[1]} | SECOND NAME: {id[2]} | TEL : {id[3]} | E-MAIL: {id[4]} | ADRESS : {id[5]}")
                        user_input = chg_menu()
                        if user_input == '1':
                            os.system('cs||clear')
                            print()
                            change = str(input("Введите новое Имя: "))
                            print()
                            print("Изменения сохранены")
                            print()
                            user_await = input("Нажмите Enter")
                            id[1] = change
                            print()
                            return user_data
                        if user_input == '2':
                            os.system('cs||clear')
                            print()
                            change = str(input("Введите новую Фамилию: "))
                            print()
                            print("Изменения сохранены")
                            print()
                            user_await = input("Нажмите Enter")                           
                            id[2] = change
                            return user_data
                        if user_input == '3':
                            os.system('cs||clear')
                            print()
                            change = str(input("Введите новый Телефон: "))
                            print()
                            print("Изменения сохранены")
                            print()
                            user_await = input("Нажмите Enter")
                            id[3] = change
                            return user_data
                        if user_input == '4':
                            os.system('cs||clear')
                            change = str(input("Введите новый e-mail: "))
                            print()
                            print("Изменения сохранены")
                            print()
                            user_await = input("Нажмите Enter")
                            id[4] = change
                            return user_data
                        if user_input == '5':
                            os.system('cs||clear')
                            change = str(input("Введите новый Адрес: "))
                            print()
                            print("Изменения сохранены")
                            print()
                            user_await = input("Нажмите Enter")
                            id[5] = change
                            return user_data
                        if user_input == '6':
                            os.system('cs||clear')
                            print()
                            print("Контакт удален")
                            print()
                            user_await = input("Нажмите Enter")
                            user_data.remove(id)
                            return user_data   
                        if user_input == 'q':
                            return user_data
        user_await = str(input("Введите 'q' для возврата в Меню: "))
        if user_await == 'q':
            return  user_data  
    else:
        return user_data

def chg_menu():
    print()
    print("Какие изменения вы хотите произвести?")
    print()
    print("(1) Изменить Имя")
    print()
    print("(2) Изменить Фамилию")
    print()
    print("(3) Изменить Телефон")
    print()
    print("(4) Изменить e-mail")
    print()
    print("(5) Изменить Адрес")
    print() 
    print("(6) Удалить контакт")
    print()   
    print("(q) Выход из Меню")
    print()                                        
    user_input = str(input("Введите соответствующую цифру из Меню: "))
    return user_input