import ast

from functions.clear import clear
from functions.lines import lines
from functions.error import error
from functions.operator.called import called_operator
from functions.operator.match import match_sale

from lists.list_error import list_error
from const.paths import PATH_PRODUCTS

def register_sale(user_found):

    while True:
        clear()
        
        index = 17
        lines(index)
        
        with open(PATH_PRODUCTS, "r", encoding="utf-8") as sale:
            content = sale.readlines()
            len_content = len(content)
            
            list_prods = []
            
            if len_content > 0:
                for item in content:    
                    format_content = item.strip("\n")
                    format_content = ast.literal_eval(format_content)
                    list_prods.append(format_content)
                
                match_sale(user_found, list_prods)
            else:
                clear()
                error(list_error[6])
                called_operator(user_found)
        break