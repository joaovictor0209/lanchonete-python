from datetime import datetime

from functions.lines import lines
from functions.clear import clear
from functions.error import error

from lists.list_inputs import list_input_products
from lists.list_error import list_error_products, list_error

def register_product(user_found):
   
    while True:
        clear()
        
        index = 5
        lines(index)
        
        try:
            name = input(list_input_products[0])
            if name == "":
                clear()
                error(list_error_products[0])
                continue
            
            description = input(list_input_products[1])
            if description == "":
                clear()
                error(list_error_products[1])
                continue
            
            category = input(list_input_products[2])
            if category == "":
                clear()
                error(list_error_products[2])
                continue
            
            
            amount = int(input(list_input_products[3]))
            if amount == "":
                clear()
                error(list_error_products[3])
                continue
            elif amount < 0:
                clear()
                error(list_error_products[7])
                continue
                
            
            price = float(input(list_input_products[4]))
            if price == "":
                clear()
                error(list_error_products[4])
                continue
            elif price < 0:
                clear()
                error(list_error_products[8])
                continue
            
            supplier = input(list_input_products[5])
            if supplier == "":
                clear()
                error(list_error_products[5])
                continue
            
            expiration = input(list_input_products[6])
            if expiration == "":
                clear()
                error(list_error_products[6])
                continue
            
            try:
                format_date = "%d/%m/%Y"
                date_now = datetime.now()
                str_date_now = str(date_now)
                str_date_now = str_date_now.split("-")
                datetime.strptime(expiration, format_date)
                
                year_digited = expiration.split("/")[2]
                
                if year_digited < str_date_now[0]:
                    clear()
                    error(list_error[20])
                    continue
                
            except ValueError:
                clear()
                error(list_error[19])
                continue
        
            if (name and description and category and amount and price and supplier and expiration):
                
                from functions.admin.info_product import info_product
                from functions.admin.generate_cod import generate_cod
                
                cod = generate_cod()
                
                list_product = [cod, name, description, category, amount, price, supplier, expiration]
                info_product(list_product, user_found)
                break
                
            
        except ValueError:
            clear()
            error(list_error_products[9])
            continue
        
        break