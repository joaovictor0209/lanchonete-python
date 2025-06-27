import ast

from const.paths import PATH_PRODUCTS

def generate_cod():
    
    while True:
        
        cod = 0
        list_cod = []
        
        with open(PATH_PRODUCTS, "r", encoding="utf-8") as generate:
            content = generate.readlines()
            len_content = len(content)
            
            if len_content == 0:
                cod = 100
            else:
                for format_content in content:
                    content = ast.literal_eval(format_content)
                    list_cod.append(int(content["cod"]))
                    
                cod_max_list = max(list_cod)
                cod = cod_max_list + 1
                
            return str(cod)
        break