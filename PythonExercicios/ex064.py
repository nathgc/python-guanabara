n = 0
s = 0
c = 0
while n != 999:
    n = int(input("Digite um número: "))
    c += 1
    s += n
print(f"Foram digitados {c-1} números. A soma dos números digitados foi {s-999}.")