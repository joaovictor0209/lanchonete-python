import ast
import questionary

from functions.lines import lines
from functions.error import error
from functions.clear import clear
from functions.admin.match_operators import match_delete
from functions.admin.called import called_main_operator

from const.paths import PATH_MENU
from lists.list_questionary import list_select
from lists.list_error import list_error

def delete_operator(user_found):

    while True:
        
        clear()
        index = 10
        lines(index)
        
        cod_user = user_found["cod"]
        list_content = []
        list_content_duplicates = []
        
        with open(PATH_MENU, "r", encoding="utf-8") as delete:
            content = delete.readlines()
            len_content = len(content)
            
            if len_content > 1:
                
                for item in content:
                    format_content = item.strip("\n")
                    format_content = ast.literal_eval(item)
                    list_content.append(format_content)
                    list_content_duplicates.append(format_content)
                
                
                for delete in list_content:
                    if cod_user in delete["cod"]:
                        list_content.remove(delete)
                    
                list_delete = [
                    f"ID: {users["cod"]} | {users["name"]} | Login: {users["login"]} | Cargo: {users["carg"]}"
                    for users in list_content
                ]
                    
                option_delete = questionary.select(
                    list_select[15],
                    choices=list_delete
                ).ask()
                    
                index_delete = list_delete.index(option_delete)
                match_delete(index_delete, user_found, list_content, list_content_duplicates)
            else:
                error(list_error[12])
                called_main_operator(user_found)
        break