print("Esse programa determina se três retas podem formar um triângulo.\n"
      "")

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("D"
                 "igite o comprimento da terceira reta: "))

if r1 + r2 > r3:
    if r1 + r3 >r2:
        if r2 + r3 > r1:
            print("Sim, Essas retas juntas podem formar juntas um triângulo.")
    else:
        print("Não, essas retas não podem formar juntas um triângulo.")
else:
    print("Não, essas retas não podem formar juntas um triângulo.")