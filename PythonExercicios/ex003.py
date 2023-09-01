n1 = input('Digite um número ')
if n1.isnumeric() == True:
    num1 = float(n1)
    n2 = input('Digite outro número ')
    if n2.isnumeric() == True:
        num2 = float(n1)
        soma = num1 + num2
        print(f'A soma desses números é {soma}!')
    else:
        print('Isso não é um número!')
else:
    print('Isso não é um número!')


