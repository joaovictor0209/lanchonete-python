from functions.verify import verify
from functions.close_app import close_app
from functions.clear import clear

def match_menu(index_menu):
    
    match index_menu:
        case 0:
            clear()
            verify(index_menu)
        case 1:
            clear()
            verify(index_menu)
        case __: 
            clear()
            close_app()
    