#Programa que avalia se uma frase é um palíndromo
print("Esse programa avalia se uma frase é um palíndromo. Nele desconsideramos acentos e não diferenciamos maiúsculas de minúsculas.\n")
from unidecode import unidecode
frase = input('Digite uma frase: ').strip().lower()
frase = frase.replace(' ','')
frase = unidecode(frase)
inverso = frase[::-1]
if frase == inverso:
    print('\n'
          'Essa frase/palavra \033[4mÉ\033[m um palíndromo.')
else:
    print('\n'
          'Essa frase/palavra \033[4mNÃO\033[m é um palíndromo.')