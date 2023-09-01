acertos =0
print("Quem é o autor do livro \' Admirável Mundo Novo\'?\n"
      "a) Aldous Huxley\n"
      "b) Machado de Assis\n"
      "c) Arthur Conan Doyle\n"
      "d) Charles Dickens\n")
resposta1 = input("a,b,c ou d: ")
if resposta1 == a:
    print("Resposta Certa! Parabéns")
    acertos = acertos + 1
else:
    print("Resposta Errada!")
print(f"Acertos {acertos}")


