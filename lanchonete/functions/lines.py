from lists.list_titles import list_titles

def lines(index):
    
    for title in list_titles[index].splitlines():
        
        print(f"{title}")