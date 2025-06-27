import questionary

from functions.clear import clear
from functions.lines import lines
from functions.match import match_menu

from lists.list_questionary import list_select, list_options_menu

def main():
    clear()
    
    while True:
        line = 0
        lines(line)
        
        option_menu = questionary.select(
            list_select[0],
            choices=list_options_menu
        ).ask()
        
        index_menu = list_options_menu.index(option_menu)
        match_menu(index_menu)
        break
        