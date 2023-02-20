import os
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *

def create_book_txt(user_data):
        id = 'id'
        first_name = 'First Name'
        second_name = 'Second Name'
        tel = 'tel'
        e_mail = 'e-mail'
        adress = 'adress'

        with open('phone_book.txt', 'w', newline = "") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [id, first_name, second_name, tel, e_mail, adress]
            )

        for user in user_data:
            with open('phone_book.txt', 'a', newline="") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(
                    user
                )
        os.system('cs||clear')
        print()
        print("Данные выгружены.")
        print()
        clear = input("Нажмите Enter ")
        os.system('cs||clear')
        return user_data