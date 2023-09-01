salario = float(input("Digite o seu salário atual: R$ "))

if salario > 1250:
    print(f"O seu aumento será de R$ {salario/10:.2f}, o seu novo salário será R$ {salario +(salario/10):.2f}.")
else:
    print(f"O seu aumento será de R$ {salario*15/100:.2f}, o seu novo salário será de {salario+(salario*15/100):.2f}.")