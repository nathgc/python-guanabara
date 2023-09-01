sexo = input("Qual o seu sexo? Digite \033[35mmasculino\033[m ou \033[35mfeminino\033[m: ")
if sexo.lower() == "masculino":
    nascimento = int(input("Digite o \033[4;31mano de nascimento\033[m: "))
    from datetime import date
    if date.today().year - nascimento < 18:
        print(f"Você \033[33mainda irá se alistar.\033[m Falta(m) cerca de \033[34m{18 - (date.today().year-nascimento)} ano(s)\033[m para que você se aliste.\n"
          f"Seu alistamento será em \033[36m{nascimento + 18}\033[m. ")
    elif date.today().year - nascimento == 18:
        print(f"\033[33mÉ a hora de você se alistar.\033[m")
    else:
        print(f"\033[33mJá passou do tempo de você se alistar.\033[m Faz(em) \033[34m{(date.today().year - nascimento) - 18} ano(s)\033[m da data do seu alistamento.\n"
          f"Seu alistamento foi em \033[36m{nascimento +18}\033[m.")
elif sexo.lower() == "feminino":
    print("\n"
          "Dado que seu sexo é \033[36mFEMININO\033[m, \033[33mNÃO É NECESSÁRIO\033[m que você se aliste.")
else:
    print("Opção de sexo \033[31mINVÁLIDA!\033[m")