import questionary

from functions.lines import lines
from functions.clear import clear
from functions.admin.match import match_finish

from lists.list_questionary import list_select, list_options_finish

def info_product(list_product, user_found):
    while True:
        clear()
        
        index = 6
        lines(index)
        
        print("╔══════════════════════════════════════════════════════════════════════════╗")
        print("║             I N F O R M A Ç Õ E S   D O   P R O D U T O                  ║")
        print("╠══════════════════════════════════════════════════════════════════════════╣")
        print(f"║ 🔑 🗝️   CÓDIGO                         : {list_product[0]:<33}║")
        print(f"║ 📦 🧾  NOME  DO  PRODUTO              : {list_product[1]:<33}║")
        print(f"║ 📝 🔍  DESCRIÇÃO  DO  PRODUTO         : {list_product[2]:<33}║")
        print(f"║ 🗂️  📁  CATEGORIA  DO  PRODUTO         : {list_product[3]:<33}║")
        print(f"║ 📊 📦  QUANTIDADE  NO  ESTOQUE        : {list_product[4]:<33}║")
        print(f"║ 💲 🏷️   PREÇO  UNITÁRIO                : R${list_product[5]:<31}║")
        print(f"║ 🚚 🏭  FORNECEDOR                     : {list_product[6]:<33}║")
        print(f"║ 📅 ⏳  DATA  DE  VALIDADE             : {list_product[7]:<33}║")
        print("╠══════════════════════════════════════════════════════════════════════════╣\n\n")
        
        option_finish = questionary.select(
            list_select[1],
            choices=list_options_finish
        ).ask()
        
        index_finish = list_options_finish.index(option_finish)
        match_finish(index_finish, list_product, user_found)
        break