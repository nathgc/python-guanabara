i=float(input("Digite o primeiro termo dessa PA: "))
r = float(input("Digite a razão dessa PA: "))
for j in range(1,11):
    print(f"{i+j*r:.0f}",end="→ ")
print("FIM")
