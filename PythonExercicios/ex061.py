p = float(input("Digite o primeiro termo desta PA: "))
r = float(input("Digite a razão dessa PA: "))
j = 1
while j <= 10:
    #print(f"O {j}° termo dessa PA é {p+(j-1)*r}")
    print(f"{p+(j-1):.0f}",end=" → ")
    j += 1
print("FIM")
