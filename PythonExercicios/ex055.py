maior = 0
menor = 0
for j in range (0,5):
    peso = float(input("Digite o peso da pessoa em kg: "))
    if j == 0:
        maior = peso
        menor = peso
    elif peso >= maior:
        maior = peso
    elif peso<= menor:
        menor = peso
print(f"\n"
      f"O MAIOR peso dentre esses é {maior} kg e o MENOR peso entre esses é {menor} kg.")