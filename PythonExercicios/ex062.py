p = float(input("Digite o primeiro termo da PA: "))
r = float(input("Digite a razão da PA: "))
print("Os primeiros 10 termos dessa PA são:")
j = 1
while j <= 10:
    print(f"{p+(j-1)*r}",end = "->")
    j +=1
print("FIM")
print(j)
extra = int(input('''
Você deseja ver mais quantos termos? '''))
termos = 10 + extra
while extra != 0:
    while j <= termos:
        print(f"{p+(j-1)*r:.0f}",end="->")
        j += 1
    print("FIM")
    extra = int(input('''
Você deseja ver mais quantos termos? '''))
    termos += extra