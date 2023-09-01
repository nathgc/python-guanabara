from math import floor
n = int(input("Digite um número inteiro: "))
primo = True
for j in range(2,floor(n**(1/2)+1)):
    if n % j == 0:
        primo = False
        divisor = j
if primo == True:
    print(f"O número \033[32m{n:.0f}\033[m \033[4mÉ\033[m um número primo.")
else:
    print(f'O número \033[32m{n:.0f}\033[m \033[4mNÃO\033[m é primo pois é divisível, por exemplo, por {divisor}.')


