import ast
import questionary

from functions.clear import clear
from functions.lines import lines
from functions.error import error
from functions.operator.info_sale import info_sale
from functions.admin.called import called_admin
from functions.operator.called import called_operator

from lists.list_error import list_error
from lists.list_questionary import list_select, list_back

from const.paths import PATH_HISTORIC
from const.cargs import CARG_ADMIN

def see_sales(user_found):

    while True:
        clear()
        
        index = 18
        lines(index)
        
        with open(PATH_HISTORIC, "r", encoding="utf-8") as historic:
            
            content = historic.readlines()
            len_content = len(content)
            
            if len_content > 0:
            
                list_historic = []
                list_prod_historic = []
                
                for item in content:
                    format_content = item.strip("\n")
                    format_content = ast.literal_eval(format_content)
                    list_historic.append(format_content)
                
                for historic in list_historic:
                    cod = historic["cod"]
                    name_client = historic["name_client"]
                    name_prod = historic["name_prod"]
                    amount = historic["amount"]
                    final_price = historic["final_price"]
                    date_historic = historic["date_historic"]
                    hour_historic = historic["hour_historic"]
                    
                    list_prod_historic = [cod, name_client, name_prod, amount, final_price, date_historic, hour_historic]
                    info_sale(list_prod_historic)
                    
                option_back = questionary.select(
                    list_select[18],
                    choices=list_back
                ).ask()
                
                if option_back:
                    if user_found["carg"] == CARG_ADMIN:
                        clear()
                        return called_admin(user_found)
                    else:
                        clear()
                        return called_operator(user_found)
                    
                
            else:
                if user_found["carg"] == CARG_ADMIN:
                    clear()
                    error(list_error[18])
                    return called_admin(user_found)
                else:
                    clear()
                    error(list_error[18])
                    return called_operator(user_found)
        break