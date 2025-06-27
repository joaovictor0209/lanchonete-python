import questionary

from functions.clear import clear
from functions.lines import lines
from functions.error import error

from lists.list_questionary import list_select, list_options
from lists.list_inputs import list_inputs_operator
from lists.list_error import list_error

from const.cargs import CARG_ADMIN, CARG_OPERATOR

def register_operator(user_found):
    
    while True:
        clear()
        
        index = 14
        lines(index)
        
        name = input(list_inputs_operator[0])
        if name == "":
            error(list_error[9])
            continue
        
        login = input(list_inputs_operator[1])
        if login == "":
            error(list_error[0])
            continue
        
        password = input(list_inputs_operator[2])
        len_password = len(password)
        
        if password == "":
            error(list_error[1])
            continue
        elif len_password < 6:
            error(list_error[2])
            continue
        
        carg = input(list_inputs_operator[3]).lower()
        if carg == "":
            error(list_error[10])
            continue
        
        if (carg != CARG_ADMIN and carg != CARG_OPERATOR):
            error(list_error[22])
            continue
        
        if name and login and password and carg: 
            from functions.admin.match_operators import match_register
            from functions.admin.generate_cod_operator import generate_cod_operator
            
            clear()
            
            index = 11
            lines(index)
            
            cod_operator = generate_cod_operator()
            list_operator = [cod_operator, name, login, password, carg]
            
            option_confirm = questionary.select(
                list_select[11],
                choices=list_options
            ).ask()
            
            index_confirm = list_options.index(option_confirm)
            match_register(index_confirm, user_found, list_operator)
        break