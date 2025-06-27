import time
from functions.clear import clear

def error(list_error):
    clear()
    
    print("________________________________________________________________")
    print(f"\n🛑 ❗ {list_error}")
    print("________________________________________________________________")
    
    time.sleep(3)