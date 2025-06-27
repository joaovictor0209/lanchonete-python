import ast
import questionary

from functions.lines import lines
from functions.error import error
from functions.clear import clear
from functions.admin.match import match_delete
from functions.admin.called import called_admin

from const.paths import PATH_PRODUCTS
from lists.list_questionary import list_select
from lists.list_error import list_error

def delete_product(user_found):
    
    while True:
        list_products = []
        index = 10
        lines(index)
        
        with open(PATH_PRODUCTS, "r", encoding="utf-8") as delete:
            content_delete = delete.readlines()
            len_content = len(content_delete)
            
            if len_content > 0:
                for format_delete in content_delete:
                    content_format = ast.literal_eval(format_delete)
                    list_products.append(content_format)
                
                list_delete_product = [
                    f"ID: {products["cod"]} | {products["name"]} | Fornecedor: {products["supplier"]} | Validade: {products["expiration"]}"
                    for products in list_products
                ]
                
                option_delete = questionary.select(
                    list_select[7],
                    choices=list_delete_product
                ).ask()
                
                index_delete = list_delete_product.index(option_delete)
                match_delete(index_delete, list_products, user_found)
            else:
                clear()
                error(list_error[6])
                called_admin(user_found)
        break
        