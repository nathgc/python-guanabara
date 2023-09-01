n = int(input("Digite o número em questão na base \033[4;31mdecimal\033[m: "))
print("Digite a base numérica em que deseja que este número seja convertido,\n"
                 "\033[35m[ 1 ]\033[m para \033[35mBINÁRIO\033[m\n"
                 "\033[33m[ 2 ]\033[m para \033[33mOCTAL\033[m\n"
                 "\033[32m[ 3 ]\033[m para \033[32mHEXADECIMAL\033[m")
base = int(input("Sua opção: "))
if base == 1:
    print(f"\n"
          f"Na base \033[35mBINÁRIA\033[m o número \033[4;36m{n}\033[m é: \033[35m{n:b}")
elif base == 2:
    print(f"\n"
          f"Na base \033[33mOCTAL\033[m o número \033[4;36m{n}\033[m é: \033[33m{n:o}")
elif base== 3:
    print(f"\n"
          f"Na base \033[32mHEXADECIMAL\033[m o número \033[4;36m{n}\033[m é: \033[32m{n:x}")
else:
    print("\n"
          "OPÇÃO INVÁLIDA!")



