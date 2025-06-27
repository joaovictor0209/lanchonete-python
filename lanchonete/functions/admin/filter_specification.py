import questionary

from functions.clear import clear 
from functions.lines import lines
from functions.admin.match import match_specification

from lists.list_questionary import list_select, list_specification

def filter_specification(user_found):
    
    while True:
        
        index = 8
        lines(index)
        
        option_specification = questionary.select(
            list_select[3],
            choices=list_specification
        ).ask()
        
        index_specification = list_specification.index(option_specification)
        match_specification(index_specification, user_found)
        break