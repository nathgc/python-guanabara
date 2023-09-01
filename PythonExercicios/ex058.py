print("\033[34m-=\033[m" * 30)
print("\033[34m___________________Vamos Jogar um jogo?_____________________\033[m\n"
      "\033[34mEu vou pensar em um número de 0 a 10 e você tem que advinhar!\033[m")
print("\033[34m-=\033[m"*30)
print("")

from random import randint

chute = int(input("Advinhe o número inteiro entre 0 e 10 que o computador escolheu: "))
n = randint(0,10)
palpites = 1
while chute != n:
    print(f"\n"
          f"\033[31m______________HaHaHaHa você perdeu!__________________\033[m\n")
    if chute > n:
        print("Tente um número menor ...")
    else:
        print('Tente um número maior...')
    chute = int(input("Advinhe o número inteiro entre 0 e 10 que o computador escolheu: "))
    palpites += 1
print("\n"
      "\033[32m_______________Parece que dessa vez você venceu, mas eu voltarei!_______________\033[m\n"
         f"\n"
      f"Parabéns você acertou o número escolhido com \033[33m{palpites}\033[m tentativa(s)!")
