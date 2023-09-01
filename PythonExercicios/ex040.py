nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media < 5:
    print(f"Sua média foi \033[31m{media:.1f}\033[m. Infelizmente você foi \033[31mREPROVADO\033[m.")
elif media >= 5 and media < 7 :
    print(f"Sua média foi \033[33m{media:.1f}\033[m. Você está de \033[33mRECUPERAÇÃO\033[m.")
else:
    print(f"Sua nota foi \033[34m{media:.1f}\033[m. Parabéns, você foi \033[34mAPROVADO\033[m.")