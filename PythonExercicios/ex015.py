dias = int(input('Digite o número de dias em que o carro esteve alugado: '))
km = float(input('Digite o número de km que o carro rodou: '))
preco = (60 * dias) + (0.15 * km)
print(f'O carro esteve alugado por {dias} dias e rodou por {km} km. O preço a pagar é {preco:.2f} reais')
