import questionary

from functions.clear import clear
from functions.lines import lines
from functions.admin.match_operators import match_operator

from lists.list_questionary import list_operators, list_select

def operators(user_found):
    
    while True:
        clear()
        
        index = 13
        lines(index)
        
        option_operator = questionary.select(
            list_select[0],
            choices=list_operators
        ).ask()
        
        index_operator = list_operators.index(option_operator)
        match_operator(index_operator, user_found)
        
        break
        