print("Digite abaixo os comprimentos das retas em questão lembrando-se de usar a \033[4;31mmesma unidade de medida\033[m.")
print("\n")
r1 = float(input("\033[32mDigite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta:\033[m "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 and r2 == r3:
        tipo = "EQUILÁTERO"
    elif r1 != r2 and r1 != r3 and r2 != r3:
        tipo = "ESCALENO"
    else:
        tipo = "ISÓSCELES"
    print(f"\n"
          f"\033[32mEssas retas juntas \033[4mPODEM\033[m \033[32mformar um triângulo do tipo \033[4m{tipo}\033[m.")
else:
    print("\n"
          "\033[31mEssas retas juntas \033[4mNÃO\033[m \033[31mpodem formar um triângulo.")

