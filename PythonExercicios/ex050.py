s = 0
cont = 0
for j in range(1,7):
    n=float(input("Digite um número: "))
    if n % 2 == 0:
        s += n
        cont +=1
print(f"\n"
      f"Você informou {cont} números pares. A SOMA dos \033[4;33mnúmeros pares\033[m digitados é \033[32m{s}\033[m! ")
