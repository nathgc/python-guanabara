from unidecode import unidecode

frase = str(input('Digite uma frase: ')).strip()
print(frase.upper())

#tira acentos e transforma em maiúsculas
sem_acento = unidecode(frase).upper()

#contagem de vezes que aparece 'A'
contagem= sem_acento.count('A')
#A = FRASE.count('A')

#print(unidecode(frase).upper())


print(f'A letra \'A\' aparece {contagem} vezes na frase.\n'
      f'A primeira posição em que aparece a letra \'A\' é {sem_acento.find("A")}.\n'
      f'A posição em que a letra \'A\' aparece pela última vez é {sem_acento.rfind("A")}')
#Comando r.find procura pela direita da string (a partir do fim)

