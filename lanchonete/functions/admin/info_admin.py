def info_admin(user_found):
    print("╠═════════════════════════════════════════════════════════════╣")
    print("║         I N F O R M A Ç Õ E S   D O   A D M I N             ║")
    print("╠═════════════════════════════════════════════════════════════╣")
    print(f"║ 🔑 🗝️    CÓDIGO         : {user_found['cod']:<35}║")
    print(f"║ 🧑 🧾   NOME COMPLETO  : {user_found['name']:<35}║")
    print(f"║ 👤 🆔   LOGIN          : {user_found['login']:<35}║")
    print(f"║ 💼 🎯   CARGO          : {user_found['carg']:<35}║")
    print("╠═════════════════════════════════════════════════════════════╣\n\n")
