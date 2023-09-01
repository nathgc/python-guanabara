#strip() para eliminar posíveis espaços indesejados no input
num =str(input('Insira um número de 0 a 9999: ')).strip()
#num = '34'
#concatenando com string de zeros para preencher possivéis digitos faltando (caso vc digite 12 por exemplo,
# vai haver zeros nas centenas e milhares
num1 = '0000'+ num
print(num1)
# pega os últimos 4 dígitos da string
num_form = num1[-4:]

print(num_form)
print(f'O número digitado foi {num}. Ele se compõe de:\n'
      f' Milhares: {num_form[0]}. \n'
      f' Centenas: {num_form[1]}.\n'
      f' Dezenas: {num_form[2]}.\n'
      f' Unidades: {num_form[3]}.')


