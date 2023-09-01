
s = 0
maior = 0
menor = 0
c = 0
resposta = "S"
while resposta == "S":
    n = float(input("Digite um número: "))
    resposta = input("Você deseja continuar? [S/N]").upper()
    if c == 0:
        maior = n
        menor = n
    if n >= maior:
        maior = n
    if n <= menor:
        menor = n
    s += n
    c += 1
print(f"A MÉDIA desses valores é {s/c}. O MAIOR valor digitado foi {maior}. O MENOR valor digitado foi {menor:.0f}.")
