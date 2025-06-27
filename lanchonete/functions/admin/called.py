def called_admin(user_found):
    from functions.admin.painel_admin import painel_admin
    painel_admin(user_found)
    
def called_update(user_found):
    from functions.admin.update_product import update_product
    update_product(user_found)
    
def called_operator(user_found):
    from functions.admin.list_operators import list_operators
    list_operators(user_found)
    
def called_main_operator(user_found):
    from functions.admin.operators import operators
    operators(user_found)
    
def called_register_operator(user_found):
    from functions.admin.register_operator import register_operator
    register_operator(user_found)