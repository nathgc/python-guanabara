from datetime import date
maiores = 0
for j in range(0,7):
    nasc = int(input("Digite o ano de nascimento da pessoa: "))
    if date.today().year-nasc >= 21:
        maiores += 1
print(f"Nesse grupo {maiores} pessoas são MAIORES de idade e {7-maiores} pessoas são MENORES de idade.")

