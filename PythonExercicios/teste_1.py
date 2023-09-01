# Jogo de RPG jogado pelo terminal estilo livro-jogo

# Define as funções do jogo
def pergunta(pergunta, opcoes):
    print(pergunta)
    for i in range(len(opcoes)):
        print(str(i + 1) + ". " + opcoes[i])
    resposta = input("Escolha uma opção: ")
    while resposta not in ["1", "2", "3", "4"]:
        resposta = input("Por favor, escolha uma opção válida: ")
    return int(resposta)

def batalha():
    print("Você entrou em uma batalha!")
    # Lógica da batalha aqui

def final():
    print("Você venceu o jogo! Parabéns!")

# Início do jogo
print("Bem-vindo ao jogo!")
print("...")
print("Você acorda em uma floresta escura e sombria.")
print("Você tem que encontrar o caminho para sair da floresta e chegar a um local seguro.")
print("Você se depara com uma bifurcação.")
escolha1 = pergunta("Qual caminho você escolhe?", ["Caminho da esquerda", "Caminho da direita"])
if escolha1 == 1:
    print("Você escolheu o caminho da esquerda.")
    escolha2 = pergunta("Você se depara com um rio. O que você faz?", ["Cruza o rio nadando", "Segue o rio", "Volta e escolhe o outro caminho"])
    if escolha2 == 1:
        print("Você tenta cruzar o rio nadando, mas é arrastado pela correnteza e morre.")
    elif escolha2 == 2:
        print("Você segue o rio e encontra uma ponte que te leva ao outro lado.")
        batalha()
    else:
        print("Você volta e escolhe o outro caminho.")
else:
    print("Você escolheu o caminho da direita.")
    escolha3 = pergunta("Você se depara com um grande urso. O que você faz?", ["Luta com o urso", "Corre", "Tenta acalmá-lo"])
    if escolha3 == 1:
        print("Você tenta lutar com o urso, mas é morto.")
    elif escolha3 == 2:
        print("Você corre, mas o urso te alcança e te mata.")
    else:
        print("Você tenta acalmar o urso e consegue. Ele te ajuda a encontrar o caminho para sair da floresta.")
        final()
