#titulo = "\033[31m=\033[m"*5+"\033[36mLojas Nathan\033[36m"+"\033[31m=\033[m"*5
titulo = "\033[36m LOJAS NATHAN \033[m"
print(titulo.center(100,"="))
print("\n")
preço = float(input("\033[33mDigite o valor do produto: R$\033[m "))
print("\n"
      "\033[34mAs formas de pagamento são:\033[m\n"
      "\n"
      "\033[36m[a] A vista no cheque ou dinheiro\n"
      "[b] A vista no cartão\n"
      "[c] Em 2x no cartão\n"
      "[d] Em 3x ou mais no cartão\033[m\n")
pagamento = input("Você escolhe a forma de pagamento \033[35ma\033[m, \033[35mb\033[m, \033[35mc\033[m ou \033[35md\033[m? ")
if pagamento == "a":
    preço = preço-preço/10
    print(f"\n"
          f"Para pagamentos a vista no \033[33m no cheque ou no dinheiro\033[m há um \033[4;32mDESCONTO de \033[4;32m10%!!!\033[m"
          f" Nesse caso o valor do "
          f"produto será: \033[32mR$ {preço:.2f}\033[m.")
elif pagamento == "b":
    preço = preço - (preço/20)
    print(f"\n"
          f"Para pagamentos a vista \033[33mno cartão\033[m há um \033[4;32mDESCONTO de 5%!!!\033[m."
          f" Nesse caso o valor do produto será: \033[32mR$ {preço:.2f}\033[m.")
elif pagamento == "c":
    print(f"\n"
          f"Para pagamentos em \033[34m2x no cartão\033[m \033[4;32mNÃO há cobranças de juros!!!\033[m"
          f" Nesse caso o valor total a pagar é: \033[32mR$ {preço:.2f}\033[m.")
    print(f"Sua compra será dividida em duas parcelas de \033[32mR$ {preço / 2:.2f}.\033[m")
elif pagamento == "d":
    parcelas = int(input("Em quantas parcelas você gostaria de pagar? "))
    if parcelas > 2:
        preço = preço + (preço / 5)
        print(f"\n"
               f"Nesse caso o valor final total será de: \033[32mR$ {preço:.2f}.\033[m")
        print(f"O valor total será dividido em {parcelas:.0f} parcelas de \033[32mR$ {preço/parcelas:.2f}.\033[m")
    elif parcelas == 2:
        print(f"\n"
              f"Para pagamentos em \033[34m2x no cartão\033[m \033[4;32mNÃO há cobranças de juros!!!\033[m"
              f" Nesse caso o valor total a pagar é: \033[32mR$ {preço:.2f}\033[m.")
        print(f"Sua compra será dividida em duas parcelas de \033[32mR$ {preço / 2:.2f}.\033[m")
    else:
        preço = preço - (preço / 20)
        print(f"\n"
              f"Para pagamentos \033[33ma vista no cartão\033[m há um \033[4;32mDESCONTO de 5%!!!\033[m."
              f" Nesse caso o valor do produto será: \033[32mR$ {preço:.2f}\033[m.")
else:
    print("\n"
          "\033[31mOpção inválida!\033[m")
