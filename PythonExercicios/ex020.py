from random import shuffle

nome0 = input('Digite o nome do primeiro aluno: ')
nome1 = input('Digite o nome do segundo aluno: ')
nome2 = input('Digite o nome do terceiro aluno: ')
nome3 = input('Digite o nome do quarto aluno: ')
lista = [nome0, nome1, nome2, nome3]
shuffle(lista)
print(f'A ordem de apresentação sorteada é {lista[0]}, {lista[1]}, {lista[2]} e por fim {lista[3]}.')




