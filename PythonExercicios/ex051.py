print('Nesse programa vamos calcular os 10 primeiros termos de uma progressão aritmética.')
p = float(input('Digite o primeiro termo dessa PA: '))
r = float(input('Digite a razão dessa PA: '))
print("\033[34m-=\033[m"*14)
for j in range(1,11):
    print(f"O {j}° termo dessa PA é: {p+r*(j-1)}")
print("\033[34m-=\033[m"*14)