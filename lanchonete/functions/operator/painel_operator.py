import questionary

from functions.lines import lines
from functions.clear import clear
from functions.operator.info_operator import info_operator
from functions.operator.match import match_operator

from lists.list_questionary import list_select, list_option_operator

def painel_operator(user_found):
    
    while True:
        clear()
        
        index = 2
        lines(index)
        info_operator(user_found)
        
        option_operator = questionary.select(
            list_select[0],
            choices=list_option_operator
        ).ask()
        
        index_operator = list_option_operator.index(option_operator)
        match_operator(index_operator, user_found)
        
        break
