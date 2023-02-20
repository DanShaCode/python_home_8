import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *

def data_path():
    print()
    src = str(input("Введите относительный путь файла: "))
    return src

def load_data_from():
    os.system('cs||clear')
    src = data_path()
    with open(src, 'r', encoding='UTF-8') as file:
        user_data = csv.reader(file, delimiter=';')
        user_data = list(user_data)
        print()
        print("Данные загружены")
        print()
        user_await = input("Нажмите Enter")
        user_data.remove(user_data[0])
        return user_data

def data_load_to(user_data):
    os.system('cs||clear')
    print()
    src = input("Укажите, пожалуйста, относительный путь файла: ")
    id = 'id'
    first_name = 'First Name'
    second_name = 'Second Name'
    tel = 'tel'
    e_mail = 'e-mail'
    adress = 'adress'

    with open(src, 'w', newline = "") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            [id, first_name, second_name, tel, e_mail, adress]
        )

    for user in user_data:
        with open(src, 'a', newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                user
            )
    return user_data
