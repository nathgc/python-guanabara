n = int(input("Digite um número inteiro para descobrir sua tabuada: "))
print("-="*15)
for j in range(1,11):
    print(f"{n} x {j:2} = {j*n}")
print("-="*15)