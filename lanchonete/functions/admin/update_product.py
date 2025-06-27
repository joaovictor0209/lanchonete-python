import ast
import questionary

from functions.error import error
from functions.lines import lines
from functions.admin.exibe_product import exibe_product
from functions.admin.match import match_update
from functions.admin.called import called_admin

from lists.list_questionary import list_select, list_update
from lists.list_error import list_error
from const.paths import PATH_PRODUCTS

def update_product(user_found):
    
    while True:
        list_content = []
        index = 9
        lines(index)
        
        with open(PATH_PRODUCTS, "r", encoding="utf-8") as update:
            content_update = update.readlines()
            len_content = len(content_update)
            
            if len_content > 0:
                for id_update, content in enumerate(content_update):
                    format_content = ast.literal_eval(content)
                    exibe_product(format_content)
                    list_content.append(format_content)
                
                option_update = questionary.select(
                    list_select[4],
                    choices=list_update
                ).ask()
                
                index_update = list_update.index(option_update)
                match_update(index_update, list_content, user_found)
                break
            else:
                error(list_error[6])
                called_admin(user_found)