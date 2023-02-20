import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *

def user_show(user_data):
    os.system('cs||clear')
    print()
    for user in user_data:
        print(f"ID : {user[0]} | FIRST NAME : {user[1]} | SECOND NAME: {user[2]} | TEL : {user[3]} | E-MAIL: {user[4]} | ADRESS : {user[5]}")
    print()
    menu_return = input("Нажмите Enter ")