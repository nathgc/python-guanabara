a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

#Ao supor que um dos três números é o menor de início se elimina o if necessário para esse teste

#Supõe que um dos três é o menor e testa
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f"O menor número dentre esses três é {menor}")


#Supõe que um dos três é o maior e testa
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O maior número dentre esses três é {maior}")