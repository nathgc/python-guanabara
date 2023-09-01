s = 0
for j in range(1,501,2):
    if j%3 == 0:
        s+=j
        #print(s)
        #print(j)
print(f"A soma total dos números impares menores do que 500 é {s}!")
