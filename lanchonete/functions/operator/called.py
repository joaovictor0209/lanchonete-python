def called_operator(user_found):
    from functions.operator.painel_operator import painel_operator
    painel_operator(user_found)
    
    
def called_sale(user_found):
    from functions.operator.register_sale import register_sale
    register_sale(user_found)