valor = float(input("Digite o \033[32mvalor\033[m da casa que deseja financiar em \033[4;32mreais\033[m: R$ "))
salario = float(input("Digite o seu salário atual: R$ "))
tempo = float(input("Digite o tempo de financiamento do imóvel em \033[4;32manos\033[m: "))
#juros = float(input("Insira a taxa de juros anual: "))
#valor_juros =valor * (1+(juros/100))**(tempo)
#print(valor_juros)
prestacao = valor/(tempo*12)
print(f"\n"
      f"Para uma casa de \033[33mR$ {valor:.2f}\033[m o valor da prestação será de \033[33mR$ {prestacao:.2f}\033[m")
if prestacao <= (salario*3/10):
    print(f"\n"
          f"\033[32mParabéns! Seu financiamento foi aprovado!\033[m")
else:
    print(f"\n"
          f"Infelizmente seu financiamento não pôde ser aprovado.")