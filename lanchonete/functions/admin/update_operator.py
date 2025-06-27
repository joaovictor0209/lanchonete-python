import ast
import questionary

from functions.lines import lines
from functions.admin.match_operators import match_update
from const.paths import PATH_MENU

from lists.list_questionary import list_select

def update_operator(user_found):
    
    while True:
        
        index = 9
        lines(index)
        
        with open(PATH_MENU, "r", encoding="utf-8") as update:
            content = update.readlines()

            list_users = []
            for content_users in content:
                format_content = content_users.strip("\n")
                format_content = ast.literal_eval(content_users)
                list_users.append(format_content)

            list_option_user = [
                f"ID: {users["cod"]} | {users["name"]} | Login: {users["login"]} | Cargo: {users["carg"]}"
                for users in list_users
            ]
            
            option_update = questionary.select(
                list_select[14],
                choices=list_option_user
            ).ask()
            
            index_update = list_option_user.index(option_update)
            match_update(index_update, user_found, list_users)
                
        break