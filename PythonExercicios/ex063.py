n = int(input("Digite o número de termos na sequência de FIbonacci: "))
seq = []
c = 1
while c <= n:
    if c == 1:
        valor = 0
    elif c == 2:
        valor = 1
    else:
        valor = seq[c-2] + seq[c-3]
    seq.append(valor)
    #print(seq)
    print(f"{valor}",end ="->")
    c += 1
print("FIM")
