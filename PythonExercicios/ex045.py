from time import sleep
from random import choice
import emoji
print("Olá, vamos jogar \033[32mJokenpô\033[m?")
jogador = input("Escolha \033[35mPEDRA\033[m, \033[35mPAPEL\033[m ou \033[35mTESOURA\033[m: ").lower()
jogador = jogador.strip()
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!")
lista = ["pedra","papel","tesoura"]
computador = choice(lista)

print(f"\n"
      f"Eu escolhi \033[36m{computador.upper()}\033[m.\n"
      f"")
sleep(2)
if (jogador == "pedra" and computador == "pedra") or (jogador == "papel" and computador == "papel") or (jogador == "tesoura" and computador == "tesoura"):
    print("\033[33mEmpatamos!")
    sleep(1)
    print(emoji.emojize(":neutral_face:")*15)
    sleep(1)
    print("Na próxima vencerei!\033[m")
elif (jogador == "pedra" and computador == "papel") or (jogador == "papel" and computador == "tesoura") or (jogador == "tesoura" and computador == "pedra"):
    print("\033[33mEu venci!!!")
    sleep(1)
    print(emoji.emojize(':rolling_on_the_floor_laughing:') * 15)
    sleep(1)
    print("Sabia que você não seria páreo para mim!\033[m")
    sleep(2)
    print("\n"
          "\033[31m___:::SE FUDEU:::___\033[m")
elif (jogador == "pedra" and computador == "tesoura") or (jogador == "papel" and computador == "pedra") or (jogador == "tesoura" and computador == "papel"):
    print("\033[33mPerdi. ")
    sleep(1)
    print(emoji.emojize(":loudly_crying_face:") * 15)
    sleep(1)
    print("Você teve sorte dessa vez!\033[m")
    sleep(2)
    print("\n"
          "\033[32m___:::ARRASOU!!!:::___\033[m")
else:
    print("Jogada inválida!")
