n1 = int(input("Digite um número para o cálculo do fatorial: "))
fatorial = 1
n = n1
if n1 == 0:
    print(f"O fatorial de {n1} é 1.")
else:
    while n != 1:
        fatorial = n* fatorial
        n -= 1
    print(f"O fatorial de {n1} é {fatorial}.")
