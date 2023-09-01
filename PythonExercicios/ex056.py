soma = 0
idade_max = 0
jovens = 0
for j in range(1,5):
    print('-'*8,f'{j}ª PESSOA','-' *8,)
    nome = input("NOME: ").strip()
    idade = float(input("IDADE: "))
    sexo = input("SEXO[M/F]: ").strip()
    soma += idade
    if j == 1 and sexo in "mM":
        idade_max = idade
        mais_velho = nome
    if (idade >= idade_max) and (sexo in "mM"):
        idade_max = idade
        mais_velho = nome
    if sexo in "Ff" and idade < 20:
        jovens+=1
media = soma/4
print(f"\n"
      f"A MÉDIA DE IDADE desse grupo de pessoas é \033[32m{media} anos\033[m.")
print(f"\n"
      f"O homem MAIS VELHO é \033[32M{mais_velho}\033[m.")
print(f"\n"
      f"Existem \033[32m{jovens}\033[m mulher(es) com menos de 20 anos.")