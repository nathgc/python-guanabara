nome = input('Digite o nome: ')
#nome = 'Carlos Silva Albuquerque'

#Passando tudo para maiúsculo para comparar. Criando uma lista com as palavras no nome para evitar casos
#como Silvana darem True
Existe_Silva = 'SILVA' in nome.upper().split()
print(f'É {Existe_Silva} que existe \'Silva\' no nome {nome}.')