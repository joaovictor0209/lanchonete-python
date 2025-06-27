import questionary
import ast
from datetime import datetime

def match_operator(index_operator, user_found):

    from functions.close_app import close_app
    from functions.clear import clear
    from functions.see_sales import see_sales
    from functions.operator.register_sale import register_sale
    

    match index_operator:
        
        case 0:
            clear()
            return register_sale(user_found)
        case 1:
            clear()
            return see_sales(user_found)
        case __:
            clear()
            return close_app()
            
def match_sale(user_found, list_prods):
    
    from lists.list_questionary import list_select, list_options_sale, option_add_list, option_decision
    from lists.list_inputs import list_inputs
    from lists.list_error import list_error
    from lists.list_success import list_success
    
    from functions.error import error
    from functions.clear import clear
    from functions.success import success
    from functions.lines import lines
    from functions.admin.exibe_product import exibe_product
    from functions.operator.called import called_sale, called_operator
    from functions.operator.generate_cod import generate_cod
    from functions.operator.info_sale import info_sale
    from const.paths import PATH_HISTORIC, PATH_PRODUCTS
    
    while True:
        list_add_prod = []
        list_return_prod = [
            f"ID: {products["cod"]} | {products["name"]} | Categoria: {products["category"]} | Qntd: {products["amount"]} Uni | Preço: R${products["price"]} | Validade: {products["expiration"]}"
            for products in list_prods
        ]
        
        option_prod = questionary.select(
            list_select[17],
            choices=list_return_prod
        ).ask()
        
        index_prod = list_return_prod.index(option_prod)
        select_prod = list_prods[index_prod]
        exibe_product(select_prod)
        
        name_client = input(list_inputs[2])
        if name_client == "":
            error(list_error[13])
            return called_sale(user_found)
        
        if not name_client.replace(" ", "").isalpha():
            error(list_error[14])
            return called_sale(user_found)
            
        
        current_amount = int(select_prod["amount"])
        amount_client = int(input(list_inputs[3]))
        
        if amount_client == "":
            error(list_error[15])
            return called_sale(user_found)
            
        if amount_client < 0:
            error(list_error[16])
            return called_sale(user_found)
            
        if amount_client > current_amount:
            error(list_error[17])
            return called_sale(user_found)
            
        if name_client and amount_client:
            clear()
            index = 11
            lines(index)
            
            cod = generate_cod()
            price = float(select_prod["price"])
            name_prod = select_prod["name"]
            final_price = price * amount_client
            current_amount -= amount_client
            
            datenow = datetime.now()
            date_historic = datenow.strftime("%d/%m/%Y")
            hour_historic = datenow.strftime("%H:%M")
            
            info_sale_content = [cod, name_client, name_prod, amount_client, final_price, date_historic, hour_historic]
            info_sale(info_sale_content)
            
            option_finish = questionary.select(
                list_select[0],
                choices=list_options_sale
            ).ask()
            
            index_finish = list_options_sale.index(option_finish)
            
            match index_finish:    
                case 0:                                        
                    select_prod["amount"] = current_amount
                    list_prods[index_prod] = select_prod
                    list_add_prod.append(info_sale_content)
                    
                    new_historic = {
                        "cod" : info_sale_content[0],
                        "name_client" : info_sale_content[1],
                        "name_prod" : info_sale_content[2],
                        "amount" : info_sale_content[3],
                        "final_price" : info_sale_content[4],
                        "date_historic" : info_sale_content[5],
                        "hour_historic" : info_sale_content[6]
                    }
                    
                    with open(PATH_PRODUCTS, "w", encoding="utf-8") as rewrite:    
                        for item in list_prods:
                            rewrite.write(f"{item}\n")
                    
                    with open(PATH_HISTORIC, "+a", encoding="utf-8") as add_prod:
                        add_prod.write(f"{new_historic}\n")
                    
                    clear()
                    index = 19
                    lines(index)
                    
                    option_add = questionary.select(
                        list_select[19],
                        choices=option_add_list
                    ).ask()
                    
                    index_add = option_add_list.index(option_add)
                    
                    match index_add:
                        case 0:
                            new_historic = {
                                "cod" : info_sale_content[0],
                                "name_client" : info_sale_content[1],
                                "name_prod" : info_sale_content[2],
                                "amount" : info_sale_content[3],
                                "final_price" : info_sale_content[4],
                                "date_historic" : info_sale_content[5],
                                "hour_historic" : info_sale_content[6]
                            }

                            clear()                   
                            index = 7
                            lines(index)
                            
                            option_prod = questionary.select(
                                list_select[17],
                                choices=list_return_prod
                            ).ask()
                            
                            index_prod = list_return_prod.index(option_prod)
                            select_prod = list_prods[index_prod]
                            exibe_product(select_prod)
                            
                            amount = int(input(list_inputs[3]))
                            amount_prod = int(select_prod["amount"])
                            current_prod = amount_prod - amount
                            
                            cod = generate_cod()
                            price_select_prod = float(select_prod["price"])
                            final_price_prod = amount * price_select_prod
                            name_second_prod = select_prod["name"]
                            info_sale_content = [cod, name_client, name_second_prod, amount, final_price_prod, date_historic, hour_historic]
                            
                            clear()
                            lines(index)
                            info_sale(info_sale_content)
                            list_add_prod.append(info_sale_content)
                            
                            opt_decision = questionary.select(
                                list_select[0],
                                choices=option_decision
                            ).ask()
                            
                            index_decision = option_decision.index(opt_decision)
                            
                            match index_decision:
                                case 0:
                                    list_content_prod = []
                                    new_historic = {
                                        "cod" : info_sale_content[0],
                                        "name_client" : info_sale_content[1],
                                        "name_prod" : info_sale_content[2],
                                        "amount" : info_sale_content[3],
                                        "final_price" : info_sale_content[4],
                                        "date_historic" : info_sale_content[5],
                                        "hour_historic" : info_sale_content[6]
                                    }
                                    
                                    with open(PATH_HISTORIC, "r", encoding="utf-8") as read_content:
                                        content = read_content.readlines()
                                        
                                        for item in content:
                                            format_content = item.strip("\n")
                                            list_content_prod.append(format_content)
                                    
                                    list_content_prod.append(new_historic)
                                    select_prod["amount"] = current_prod
                                    list_prods[index_prod] = select_prod
                                    
                                    with open(PATH_PRODUCTS, "w", encoding="utf-8") as rewrite:    
                                        for item in list_prods:
                                            rewrite.write(f"{item}\n")
                                            
                                    with open(PATH_HISTORIC, "w", encoding="utf-8") as add_prod_txt:   
                                        for item_add_prod in list_content_prod:
                                            add_prod_txt.write(f"{item_add_prod}\n")    
                                        
                                    success(list_success[8])
                                    return called_operator(user_found)  
                                case __:
                                    clear()
                                    return called_operator(user_found)                      
                        
                        case __:
                            clear()
                            success(list_success[8])
                            return called_operator(user_found)                               
                case __:
                    clear()
                    return called_operator(user_found)
        break
    