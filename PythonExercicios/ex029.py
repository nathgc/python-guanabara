velocidade = float(input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    print("Você ultrapassou o limite de velocidade e será multado.")
    multa = (velocidade-80)*7
    print(f"Sua multa será de R$ {multa}. ")

print("Tenha um bom dia e dirija com segurança!")