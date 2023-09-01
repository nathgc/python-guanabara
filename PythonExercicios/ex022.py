#nome = '    Nathan   Gomes Caldeira de Albuquerque   '
#Retirando espaços no início e no fim da palavra
nome = str(input('Olá, digite seu nome completo: ')).strip()
#''.join(nome.split()) junta sem colocar espaços cada um dos nomes separados que foram gerados por nome.split()
num_letras = len(''.join(nome.split()))

print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'O seu nome em minúsculas é: {nome.lower()}')
print(f'O seu nome possui {num_letras} letras')
print('O número de letras do seu primeiro nome é',len(nome.split()[0]))
