import ast
import questionary

from datetime import datetime

from functions.clear import clear
from functions.success import success

from const.paths import PATH_PRODUCTS

from lists.list_success import list_success

def match_admin(index_admin, user_found):
    from functions.admin.register_product import register_product
    from functions.admin.list_products import list_products
    from functions.admin.update_product import update_product
    from functions.admin.generate_cod import generate_cod
    from functions.admin.delete_product import delete_product
    from functions.admin.operators import operators
    from functions.admin.see_stock import see_stock
    from functions.close_app import close_app
    from functions.see_sales import see_sales
    
    match index_admin:
        case 0:
            clear()
            register_product(user_found)
        case 1:
            clear()
            list_products(user_found)
        case 2:
            clear()
            update_product(user_found)
        case 3:
            clear()
            delete_product(user_found)
        case 4:
            clear()
            see_stock(user_found)
        case 5:
            clear()
            see_sales(user_found)
        case 6:
            clear()
            operators(user_found)
        case __:
            clear()
            close_app()


def match_finish(index_finish, list_product, user_found):
    from functions.admin.called import called_admin
    
    match index_finish:
        case 0:
            date_now = datetime.now()
            date_format = date_now.strftime("%d/%m/%Y")
            hour_format = date_now.strftime("%H:%M")
            
            new_product = {
                "cod" : list_product[0],
                "name" : list_product[1],
                "description" : list_product[2],
                "category" : list_product[3],
                "amount" : list_product[4],
                "price" : list_product[5],
                "supplier" : list_product[6],
                "expiration" : list_product[7],
                "date_post" : date_format,
                "hour_post" : hour_format
            }
            
            with open(PATH_PRODUCTS, "+a", encoding="utf-8") as product:
                product.write(f"{new_product}\n")
            
            success(list_success[0])
            called_admin(user_found)
                
        case __:
            clear()
            called_admin(user_found)
            

def match_filter(index_filter, user_found):
    from functions.admin.called import called_admin
    from functions.admin.filter_specification import filter_specification
    
    match index_filter:
        case 0:
            clear()
            filter_specification(user_found)
        case __:
            clear()
            called_admin(user_found)
            

def match_specification(index_specification, user_found):
    from functions.error import error
    from functions.clear import clear
    from functions.admin.exibe_product import exibe_product
    from functions.admin.list_products import list_products
    
    from lists.list_error import list_error
    from lists.list_questionary import list_select, list_filter
    
    while True:
        what_spec = None
        product_find = None
        list_product = []
        
        list_spec = {
            "cod" : 0, "name" : 1, "category" : 2, "amount" : 3, 
            "price" : 4, "supplier" : 5, "expiration" : 6
        }
        
        for index, spec in enumerate(list_spec):
            if index == index_specification:
                what_spec = spec
            
        specification = input("\nPREENCHA  NESTE  CAMPO  COM  A INFORMAÇÃO  DESEJADA\nINFORME  NESTE  CAMPO: ")
        if specification == "":
            clear()
            error(list_error[4])
            continue
        
        with open(PATH_PRODUCTS, "r", encoding="utf-8") as spec:
            clear()
            content_products = spec.readlines()

            for index_prod, products in enumerate(content_products):
                format_prod = ast.literal_eval(products)
                
                if specification.lower() == str(format_prod[what_spec]).lower():
                    list_product.append(format_prod)
                    product_find = True
                    exibe_product(format_prod)
            
            if product_find:
                option_filter = questionary.select(
                    list_select[2],
                    choices=list_filter
                ).ask()
                            
                index_filter = list_filter.index(option_filter)
                match_filter(index_filter, user_found)
            else:
                clear()
                error(list_error[5])
                list_products(user_found)
        break
    

def match_update(index_update, list_content, user_found):
    from const.paths import PATH_PRODUCTS
    
    from functions.lines import lines
    from functions.clear import clear
    from functions.error import error
    from functions.admin.exibe_product import exibe_product
    from functions.admin.called import called_update,called_admin
    from functions.success import success
    
    from lists.list_inputs import list_update_input
    from lists.list_questionary import list_select, list_update
    from lists.list_questionary import list_update_product 
    from lists.list_success import list_success 
    from lists.list_error import list_error, list_error_products
    
    
    match index_update:
        case 0:
            
            while True:
                clear()
                
                index = 9
                lines(index)
                
                list_products = [
                    f"ID: {products["cod"]} | {products["name"]} | Fornecedor: {products["supplier"]} | Validade: {products["expiration"]}"
                    for products in list_content
                ]
                
                option_product = questionary.select(
                    list_select[5],
                    choices=list_products
                ).ask()
                
                index_prod = list_products.index(option_product)
                list_product_update = list_content[index_prod]
                
                for index_update, verify_update in enumerate(list_content):
                    if verify_update["name"] in option_product:
                        exibe_product(verify_update)
                
                option_update_product = questionary.select(
                    list_select[6],
                    choices=list_update_product
                ).ask()
                
                index_update_product = list_update_product.index(option_update_product)
                category_update = ["name", "category", "description", "amount", "price", "supplier", "expiration"]
                what_update = category_update[index_update_product]

                if what_update:                        
                    what_prod_update = input(list_update_input[0])
                    if what_prod_update == "":
                        error(list_error[7])
                        continue
                    
                    if what_update == "amount":
                        if int(what_prod_update) < 0:
                            error(list_error_products[7])
                            continue
                        
                    if what_update == "price":
                        if float(what_prod_update) < 0:
                            error(list_error_products[8])
                            continue
                        
                    if what_update == "expiration":
                        format_date = "%d/%m/%Y"
                        
                        try:
                            date_now = datetime.now()
                            
                            format_valid = datetime.strptime(what_prod_update, format_date)
                            str_date = str(format_valid)
                            
                            str_date_now = str(date_now)
                            format_year_now = str_date_now.split("-")[0]

                            format_str = str_date.replace(" ", "-").split("-")
                            format_str_form = what_prod_update.split("/")[-1]
                            
                            if format_str_form < format_year_now:
                                clear()
                                error(list_error[20])
                                continue
                            
                            what_prod_update = f"{format_str[2]}/{format_str[1]}/{format_str[0]}"                             
                        except ValueError:
                            clear()
                            error(list_error[19])
                            continue
                    
                    list_product_update[what_update] = what_prod_update
                    with open(PATH_PRODUCTS, "w", encoding="utf-8") as read:
                        for format_content in list_content:
                            read.write(f"{format_content}\n")
                            
                        success(list_success[1])
                        clear()
                        
                        
                    lines(index)  
                    
                    option_decision = questionary.select(
                        list_select[0],
                        choices=list_update
                    ).ask()
                    
                    index_decision = list_update.index(option_decision)
                    match index_decision:
                        case 0:
                            clear()
                            return called_update(user_found)
                        case __:
                            clear()
                            return called_admin(user_found)

        case __:
            clear()
            return called_admin(user_found)


def match_delete(index_delete, list_products, user_found):
    from functions.clear import clear
    from functions.admin.called import called_admin
    from functions.lines import lines
    from functions.success import success
    
    from lists.list_success import list_success
    from lists.list_questionary import list_select, list_delete
    
    from const.paths import PATH_PRODUCTS
    
    
    while True:
        clear()
        
        index = 11
        lines(index)
        
        option_delete = questionary.select(
            list_select[8],
            choices=list_delete
        ).ask()
        
        index_product = list_delete.index(option_delete)
        match index_product:
            case 0:
                del list_products[index_delete]
                with open(PATH_PRODUCTS, "w", encoding="utf-8") as update_archive:
                    for content in list_products:
                        update_archive.write(f"{content}\n")
                
                success(list_success[2])
                return called_admin(user_found)
                
            case __:
                clear()
                return called_admin(user_found)
        break


def match_stock(index_stock, user_found, list_stock):
    from functions.clear import clear
    from functions.lines import lines
    from functions.error import error
    from functions.admin.called import called_admin
    from functions.admin.exibe_product import exibe_product
    from const.paths import PATH_PRODUCTS
    from functions.success import success

    from lists.list_questionary import list_select
    from lists.list_inputs import list_update_input
    from lists.list_success import list_success
    from lists.list_error import list_error

    match index_stock:
        case 0:
            while True:
                clear()
                index = 12
                lines(index)

                list_names = []
                list_prod_parser = []

                for stock in list_stock:
                    content_stock = ast.literal_eval(stock)
                    label = f"ID: {content_stock['cod']} | {content_stock['name']} | Quantidade: {content_stock['amount']} | Validade: {content_stock['expiration']}"
                    list_names.append(label)
                    list_prod_parser.append(content_stock)

                option_select = questionary.select(
                    list_select[10],
                    choices=list_names
                ).ask()

                index_select = list_names.index(option_select)
                selected_product = list_prod_parser[index_select]

                clear()
                exibe_product(selected_product)

                try:
                    new_amount = int(input(list_update_input[1]))
                    current_amount = int(selected_product["amount"])
                    modify_amount = new_amount + current_amount
                    selected_product["amount"] = modify_amount

                    list_stock[index_select] = str(selected_product)

                    with open(PATH_PRODUCTS, "w", encoding="utf-8") as update:
                        for content_update in list_stock:
                            update.write(f"{content_update}\n")

                    success(list_success[3])
                    return called_admin(user_found)

                except ValueError:
                    error(list_error[8])
                    continue
        case __:
            clear()
            called_admin(user_found)
