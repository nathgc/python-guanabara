n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
acao = 0

while acao != 5:
    print("-="*20)
    acao = int(input('''Digite o que você deseja:
    [1] Somar 
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    >>>>>>>>>> Sua opção é: '''))
    if acao == 1:
        print(f"\n"
              f"A soma de {n1} e {n2} é {n1+n2}.\n")
    elif acao == 2:
        print(f"\n"
              f"O produto de {n1} e {n2} é {n1*n2}.\n")
    elif acao == 3:
        if n1 >= n2:
            print(f"\n"
                  f"O maior dentre {n1} e {n2} é {n1}.\n")
        else:
            print(f"\n"
                  f"O maior dentre {n1} e {n2} é {n2}.\n")
    elif acao == 4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    elif acao not in [1,2,3,4,5]:
        print('\033[31mOPÇÃO INVÁLIDA.\033[m')