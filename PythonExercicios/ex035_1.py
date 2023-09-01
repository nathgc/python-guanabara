print("\n"
      "Esse programa determina se três segmentos de reta podem formar juntos um triângulo.\n"
      "")

r1 = float(input("Digite o comprimento do primeiro segmento de reta: "))
r2 = float(input("Digite o comprimento do segundo segmento de reta: "))
r3 = float(input("Digite o comprimento do terceiro segmento de reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("SIM, esses segmentos de reta PODEM juntos formar um triângulo.")
else:
    print("\n"
          "NÂO, esses segmentos de reta NÂO PODEM formar juntos um triângulo.")

