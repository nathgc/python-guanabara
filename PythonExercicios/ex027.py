nome = input('Digite o nome completo da pessoa: ')
#nome = 'Nathan Gomes Caldeira'

print(f'Prazer em te conhecer!\n'
      f'O primeiro nome dessa pessoa é {nome.split()[0]}.\n'
      f'O último nome dessa pessoa é {nome.split()[-1]}.')
#[-1] pega a última posição da lista
