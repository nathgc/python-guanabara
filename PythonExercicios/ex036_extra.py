valor = float(input("Digite o \033[32mvalor\033[m da casa que deseja financiar em \033[4;32mreais\033[m: R$ "))
salario = float(input("Digite o seu salário atual: R$ "))
tempo = float(input("Digite o tempo de financiamento do imóvel em \033[4;32manos\033[m: "))
juros = float(input("Insira a taxa de juros anual em \033[4;36mporcentos\033[m: "))
valor_juros =valor * (1+(juros/100))**(tempo)
print(f"{valor_juros:.2f}")
prestacao = valor/(tempo*12)
print(f"\n"
      f"O valor total a prazo dessa casa em \033[32m{tempo} anos\033[m será \033[33mR$ {valor_juros:.2f}\033[m.\n"
      f"Nesse caso a prestação será de \033[33mR$ {prestacao:.2f}\033[m.")
if prestacao <= (salario*3/10):
    print(f"\n"
          f"\033[32mParabéns! Seu financiamento foi aprovado!\033[m")
else:
    print(f"\n"
          f"Infelizmente seu financiamento não pôde ser aprovado.")