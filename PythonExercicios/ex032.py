from datetime import date

ano = int(input("Digite o ano em questão, caso seja digitado 0 será considerado o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano < 1582:
    print("________Atenção_____________\n"
          "Essa data é anterior à implementação do calendário Gregoriano, portanto podem haver discrepâncias históricas.\n"
          " ")

if (ano % 4== 0):
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"O ano de {ano} é bissexto!")
        else:
            print(f"O ano de {ano} não é bissexto!")
    else:
        print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto.")

print(" \n"
      "Atenção, aqui estamos utilizando o calendário gregoriano!\n"
      "Os resultados não se aplicam a anos em outros calendários"
      " ou a datas anteriores à implementação desse calendário (1582)")