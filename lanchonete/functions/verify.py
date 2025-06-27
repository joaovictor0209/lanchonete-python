import ast

from functions.lines import lines
from functions.clear import clear
from functions.error import error

from functions.admin.painel_admin import painel_admin
from functions.operator.painel_operator import painel_operator

from const.paths import PATH_MENU
from const.cargs import CARG_ADMIN

from lists.list_inputs import list_inputs
from lists.list_error import list_error

def verify(index_menu):
    while True:
        clear()
        user_found = None
        id_list = None
        
        if index_menu == 0:
            index = 1
        else:
            index = 2
            
        lines(index)
        
        login = input(list_inputs[0])
        if login == "":
            error(list_error[0])
            continue
        
        password = input(list_inputs[1])
        len_password = len(password)
        min_password = 6
        
        if password == "":
            error(list_error[1])
            continue
        elif len_password < min_password:
            error(list_error[2])
            continue
        
        if login and password:
            with open(PATH_MENU, "r", encoding="utf-8") as verify:
                content = verify.readlines()
                
                for index_list, format in enumerate(content):
                    format_list = ast.literal_eval(format)
                    if (format_list["login"] == login and format_list["password"] == password):
                        user_found = format_list
                
                if user_found:
                    if user_found["carg"] == CARG_ADMIN:
                        clear()
                        painel_admin(user_found)
                    else:
                        clear()
                        painel_operator(user_found)
                else:
                    clear()
                    error(list_error[3])
                    continue
        break   