def info_operator(user_found):
    print("╠═════════════════════════════════════════════════════════════╣")
    print("║        I N F O R M A Ç Õ E S   D O   O P E R A D O R        ║")
    print("╠═════════════════════════════════════════════════════════════╣")
    print(f"║ 🔑 🗝️    CÓDIGO         : {user_found['cod']:<35}║")
    print(f"║ 🧑 🧾   NOME COMPLETO  : {user_found['name']:<35}║")
    print(f"║ 👤 🆔   LOGIN          : {user_found['login']:<35}║")
    print(f"║ 💼 🎯   CARGO          : {user_found['carg']:<35}║")
    print("╠═════════════════════════════════════════════════════════════╣\n\n")
