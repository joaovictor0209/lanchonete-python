import ast
import questionary

from functions.clear import clear
from functions.lines import lines
from functions.error import error
from functions.admin.match import match_filter
from functions.admin.called import called_admin
from functions.admin.exibe_product import exibe_product

from const.paths import PATH_PRODUCTS

from lists.list_questionary import list_select, list_filter
from lists.list_error import list_error

def list_products(user_found):
    while True:
        clear()
        
        index = 7
        lines(index)
            
        with open(PATH_PRODUCTS, "r", encoding="utf-8") as list:
            content = list.readlines()
            len_content = len(content)
            
            if len_content != 0:
                for format in content:
                    format_content = ast.literal_eval(format)
                    exibe_product(format_content)
                
                option_filter = questionary.select(
                    list_select[2],
                    choices=list_filter
                ).ask()
                
                index_filter = list_filter.index(option_filter)
                match_filter(index_filter, user_found)
                break
            else:
                error(list_error[6])
                called_admin(user_found)