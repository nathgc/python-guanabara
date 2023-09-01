n1 = int(input("Digite o \033[34mprimeiro\033[m número: "))
n2 = int(input("Digite o \033[33msegundo\033[m número: "))

if n1 > n2:
    print(f"O \033[33mprimeiro valor\033[m é o \033[34mmaior\033[m.")
elif n2 > n1:
    print(f"O \033[33msegundo valor\033[m é o \033[34mmaior\033[m. ")
else:
    print("\033[33mNão existe\033[m valor maior, os dois são \033[34miguais\033[m.")

