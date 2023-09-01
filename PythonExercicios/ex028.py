print("-=" * 30)
print("___________________Vamos Jogar um jogo?_____________________\n"
      "Eu vou pensar em um número de 0 a 5 e você tem que advinhar!")
print("-="*30)
print("")

from random import randint

chute = int(input("Advinhe o número inteiro entre 0 e 5 que o computador escolheu: "))
n = randint(0,5)

if n == chute:
   print("_______________Parece que dessa vez você venceu, mas eu voltarei!_______________\n"
         "Parabéns você acertou o número escolhido!")
else:
   print(f"______________HaHaHaHa você perdeu!__________________\n"
         f"Infelizmente você errou, o número escolhido era {n}.")
