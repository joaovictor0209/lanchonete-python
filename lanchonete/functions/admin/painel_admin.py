import questionary

from functions.lines import lines
from functions.clear import clear

from functions.admin.info_admin import info_admin
from functions.admin.match import match_admin

from lists.list_questionary import list_select, list_option_admin

def painel_admin(user_found):

    while True:
        clear()
        
        index = 4
        lines(index)
        
        info_admin(user_found)
        
        option_admin = questionary.select(
            list_select[0],
            choices=list_option_admin
        ).ask()
        
        index_admin = list_option_admin.index(option_admin)
        match_admin(index_admin, user_found)
        break