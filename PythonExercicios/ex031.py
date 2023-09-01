d = float(input("Digite a distância da viagem em km? "))

if d <= 200:
    print(f"O valor da passagem neste caso é: {d*0.5:.2f} reais. ")
else:
    print(f"Parabéns! Você é elegivél para a nossa tarifa promocional!\n"
          f"O valor da passagem neste caso é: {d*0.45:.2f} reais.")