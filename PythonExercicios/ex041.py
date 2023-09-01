nascimento = int(input("Digite o \033[33mano de nascimento\033[m do(a) nadador(a): "))
from datetime import date
idade = date.today().year - nascimento

if idade <= 9:
    print(f"Pela sua idade esse nadador está na categoria \033[34mMIRIM\033[m.")
elif idade <= 14:
    print("Pela sua idade esse nadador está na categoria \033[34mINFANTIL\033[m.")
elif idade <= 19:
    print("Pela sua idade esse nadador está na categoria \033[34mJUNIOR\033[m.")
elif idade <= 20:
    print("Pela sua idade este nadador é da categoria \033[34mSÊNIOR\033[m.")
else:
    print("Pela sua idade esse nadador é da categoria \033[34mMASTER\033[m.")
