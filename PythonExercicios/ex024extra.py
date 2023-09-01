nome = 'Santo André'
Posicao = nome.strip().find('Santo')
if Posicao == 0:
    print(f'A cidade {nome} tem o nome iniciado pela palavra \'Santo\' ')
else:
    print(f'A cidade {nome} não tem o nome iniciado com a palavra \'Santo\' ')