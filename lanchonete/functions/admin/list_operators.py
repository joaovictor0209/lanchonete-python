import ast
import questionary

from functions.lines import lines
from functions.admin.exibe_operators import exibe_operators
from functions.admin.match_operators import match_filter
from const.paths import PATH_MENU
from lists.list_questionary import list_select, list_filter_operators

def list_operators(user_found):
    
    while True:
        
        index = 15
        lines(index)
        
        with open(PATH_MENU, "r", encoding="utf-8") as list:
            content = list.readlines()
           
            list_operator = []
            for format_users in content:
                format_content = format_users.strip("\n")
                format_content = ast.literal_eval(format_users)
                list_operator.append(format_content)
                exibe_operators(format_content)
                
            
            option_filter = questionary.select(
                list_select[12],
                choices=list_filter_operators
            ).ask()
            
            index_filter = list_filter_operators.index(option_filter)
            match_filter(index_filter, user_found, list_operator)
        
        break