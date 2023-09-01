import random

print('Nesse programa sortearemos o nome de um aluno para apagar o quadro')
nome0 = input('Digite o nome do primeiro aluno: ')
nome1 = input('Digite o nome do segundo aluno: ')
nome2 = input('Digite o nome do terceiro aluno: ')
nome3 = input('Digite o nome do quarto aluno: ')
lista = [nome0, nome1, nome2, nome3]
print(f'O aluno sorteado para apagar o quadro foi {random.choice(lista)}.')