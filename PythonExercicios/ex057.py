sexo = str(input("Digite seu sexo [M/F]: ").upper().strip())
s = ['M','F','MASCULINO','FEMININO']
while sexo not in s:
    print("Digite um sexo válido.")
    sexo = str(input("Digite seu sexo [M/F]: ").upper().strip())
if sexo == "M" or sexo == 'MASCULINO':
    print('''Sexo registrado.
Seu sexo é MASCULINO.''')
if sexo == "F" or sexo == 'FEMININO':
    print('''Sexo registrado.
Seu sexo é FEMININO.''')
