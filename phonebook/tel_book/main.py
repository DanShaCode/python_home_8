import os
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *
from modules.data_operations.data_load import *
from modules.data_operations.data_clear import *

os.system('cs||clear')

user_data = []

menu(user_data)