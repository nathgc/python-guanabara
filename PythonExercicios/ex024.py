nome = input('Digite o nome da cidade: ')
#nome = 'Santo André'
nome = nome.strip()

#formatando a parte inicial do string para comparar com 'Santo'
nome_ini = nome[0:5].capitalize()
#print(nome[0:5])
Santo_in = 'Santo' in nome_ini
print(f'É {Santo_in} que o nome dessa cidade se inicia com \'Santo\'')

