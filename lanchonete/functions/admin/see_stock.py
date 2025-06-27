import ast
import questionary

from functions.error import error
from functions.lines import lines
from functions.admin.exibe_product import exibe_stock
from functions.admin.called import called_admin
from functions.admin.match import match_stock

from lists.list_questionary import list_select, list_stock_select
from lists.list_error import list_error

from const.paths import PATH_PRODUCTS

def see_stock(user_found):
    
    while True:
        list_stock = []
        index = 12
        lines(index)
        
        with open(PATH_PRODUCTS, "r", encoding="utf-8") as stock:
            content = stock.readlines()      
            len_content = len(content)
            
            if len_content != 0:
                  
                for format_content in content:
                    format_content = format_content.strip("\n")
                    list_stock.append(format_content)
                    
                for exibe_product in list_stock:
                    format_exibe = ast.literal_eval(exibe_product)
                    exibe_stock(format_exibe)
                
                option_stock = questionary.select(
                    list_select[9],
                    choices=list_stock_select
                ).ask()
                
                index_stock = list_stock_select.index(option_stock)
                match_stock(index_stock, user_found, list_stock)
                break
            else:
                error(list_error[6])
                called_admin(user_found)