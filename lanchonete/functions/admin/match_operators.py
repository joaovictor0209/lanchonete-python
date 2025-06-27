import ast
import questionary

from datetime import datetime

def match_operator(index_operator, user_found):
    from functions.clear import clear
    from functions.admin.called import called_admin
    from functions.admin.register_operator import register_operator
    from functions.admin.list_operators import list_operators
    from functions.admin.update_operator import update_operator
    from functions.admin.delete_operator import delete_operator
    
    match index_operator:
        
        case 0:
            clear()
            register_operator(user_found)
        case 1:
            clear()
            list_operators(user_found)
        case 2:
            clear()
            update_operator(user_found)
        case 3:
            clear()
            delete_operator(user_found)
        case __:
            clear()
            called_admin(user_found)
            

def match_register(index_confirm, user_found, list_operator):
    from functions.clear import clear
    from functions.success import success
    from functions.error import error
    from functions.admin.called import called_admin, called_register_operator
    
    from lists.list_success import list_success
    from lists.list_error import list_error
    from const.paths import PATH_MENU
    
    match index_confirm:
        
        case 0:
            
            while True:
                
                date_now = datetime.now()
                format_date = date_now.strftime("%d/%m/%Y")
                format_hour = date_now.strftime("%H:%M")
                
                new_operator = {
                    "cod" : list_operator[0],
                    "name" : list_operator[1],
                    "login" : list_operator[2],
                    "password" : list_operator[3],
                    "carg" : list_operator[4],
                    "date_create" : format_date,
                    "hour_create" : format_hour
                }
                
                with open(PATH_MENU, "r", encoding="utf-8") as read:
                    content = read.readlines()
                    list_logins = []
                    
                    for item in content:
                        format_item = item.strip("\n")
                        format_item = ast.literal_eval(item)
                        list_logins.append(format_item["login"])
                        
                    if list_operator[2] not in list_logins:
                        with open(PATH_MENU, "+a", encoding="utf-8") as register:
                            register.write(f"{new_operator}\n")
                        
                        success(list_success[4])
                        return called_admin(user_found)
                    else:
                        clear()
                        error(list_error[21])
                        return called_register_operator(user_found)
                
        case __:
            clear()
            return called_admin(user_found)
    

def match_filter(index_filter, user_found, list_operator):
    
    from functions.admin.called import called_admin
    from functions.admin.exibe_operators import exibe_operators
    from functions.admin.called import called_operator
    from functions.clear import clear
    from functions.lines import lines
    from functions.error import error
    
    from lists.list_questionary import list_select, list_specification_operator, list_filter_operators
    from lists.list_inputs import list_update_input
    from lists.list_error import list_error
    
    match index_filter:

        case 0:
            
            while True:
                clear()
                
                index = 8
                lines(index)
                
                option_specification = questionary.select(
                    list_select[13],
                    choices=list_specification_operator
                ).ask()
                
                index_specification = list_specification_operator.index(option_specification)
                category_spec = ["cod", "name", "login", "carg"]
                search_content = category_spec[index_specification]
                
                what_search = input(list_update_input[2])
                if what_search == "":
                    error(list_error[7])
                    continue
                
                if what_search:
                    clear()
                    
                    user_found_list = []
                    index = 16
                    lines(index)
                    
                    for return_content in list_operator:
                        if what_search.lower() in return_content[search_content].lower():
                            exibe_operators(return_content)
                            user_found_list.append(return_content)
                        
                    if not user_found_list:
                        error(list_error[11])
                        continue
                    else:
                        option_filter = questionary.select(
                            list_select[12],
                            choices=list_filter_operators
                        ).ask()
                            
                        index_filter = list_filter_operators.index(option_filter)
                        match index_filter:
                            case 0:
                                clear()
                                called_operator(user_found)
                            case __:
                                clear()
                                called_admin(user_found)
                break
        case __:
            clear()
            called_admin(user_found)


def match_update(index_update, user_found, list_users):
    
    from functions.error import error
    from functions.clear import clear
    from functions.success import success
    from functions.lines import lines
    from functions.admin.exibe_operators import exibe_operators
    from functions.admin.called import called_main_operator
    
    from lists.list_questionary import list_select, list_alter_user
    from lists.list_inputs import list_update_input
    from lists.list_error import list_error
    from lists.list_success import list_success
    
    from const.paths import PATH_MENU
    from const.cargs import CARG_ADMIN, CARG_OPERATOR
    
    while True:
        clear()
        
        index = 2
        lines(index)
        exibe_operators(list_users[index_update])
        
        info_user = list_users[index_update]
        info_alter = ["name", "login", "carg", "password"]
        
        option_update_info = questionary.select(
            list_select[6],
            choices=list_alter_user
        ).ask()
        
        index_info = list_alter_user.index(option_update_info)
        value_category = info_alter[index_info]
        
            
        if value_category == "carg":
            new_info = input(f"🔄👤  {list_update_input[4]}")
            if (new_info != CARG_ADMIN and new_info != CARG_OPERATOR):
                error(list_error[22])
                continue
        else:
            new_info = input(f"🔄👤  {list_update_input[3]}")
            
        if new_info == "":
            error(list_error[7])
            continue
        
        value = info_alter[index_info]
        info_user[value] = new_info
        list_users[index_update] = info_user
        
        with open(PATH_MENU, "w", encoding="utf-8") as update:    
            for item in list_users:
                update.write(f"{item}\n")

        success(list_success[5])
        called_main_operator(user_found)
        break


def match_delete(index_delete, user_found, list_content, list_content_duplicates):
    
    from functions.clear import clear
    from functions.lines import lines
    from functions.success import success
    from const.paths import PATH_MENU
    from functions.admin.called import called_main_operator
    
    from lists.list_success import list_success
    from lists.list_questionary import list_select, list_delete_operator
    
    while True:
        clear()
        index = 11
        lines(index)
        
        option_delete = questionary.select(
            list_select[16],
            choices=list_delete_operator
        ).ask()
        index = list_delete_operator.index(option_delete)
        
        match index:
            
            case 0:
                list_content = list_content[index_delete]
                list_content_duplicates.remove(list_content)
                
                with open(PATH_MENU, "w", encoding="utf-8") as delete:
                    for item in list_content_duplicates:
                        delete.write(f"{item}\n")
            
                success(list_success[6])
                return called_main_operator(user_found)
                
            case __:
                clear()
                return called_main_operator(user_found)