import time
from functions.clear import clear

def success(list_success):
    clear()
    
    print("╠══════════════════════════════════════════════════════════════════════════╣")
    print(f"║ 🎉 ✅  {list_success} {"║":^47}")
    print("╚══════════════════════════════════════════════════════════════════════════╝")
    time.sleep(3)
