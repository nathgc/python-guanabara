from unidecode import unidecode

frase = str(input('Digite a frase para ser analisada: ')).strip()

#retirando acentos da frase usando unidecode
#sem_acento = unidecode(frase)
#print(sem_acento)
frase_nova = unidecode(frase).lower()

#frase = 'Quem vigia os vigilantes?'
posicao_inicial = frase_nova.find('a', 0)

#separando frase pela letra 'a'
split_a = frase_nova.split('a')

#comprimento da parte após o último 'a'
comprimento_final = len(split_a[-1])

#A posição final é a posição do último caracter (comprimento da frase - 1) menos o numero de caracteres após o último 'a'
posicao_final = len(frase_nova)-comprimento_final-1

contagem = frase_nova.count('a')

print(f'A frase digitada foi \'{frase}\'.\n'
      f'A posição inicial da letra \'a\' é {posicao_inicial}.\n'
      f'A posição final da letra \'a\' é {posicao_final}.\n'
      f'A letra \'a\' aparece {contagem} vezes nessa frase.')