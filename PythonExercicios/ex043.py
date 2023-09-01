altura = float(input("Digite sua \033[4;32mALTURA\033[m em \033[4;33mMETROS\033[m: "))
peso = float(input("Digite o seu \033[4;33mPESO\033[m em \033[4;33mKG\033[m: "))


imc = peso/(altura*altura)

if imc < 18.5:
    print(f"Seu imc é {imc:.1f}. Com base nele você está \033[31mABAIXO DO PESO\033[m.")
elif 18.5 <= imc < 25:
    print(f"Seu imc é \033[36m{imc:.1f}\033[m. Com base nele você está \033[32mNO PESO IDEAL\033[m.")
elif 25 < imc <= 30:
    print(f"Seu imc é \033[36m{imc:.1f}\033[m. Com base nel você está com \033[33mSOBREPESO\033[m.")
elif 30 < imc <= 40:
    print(f"Seu imc é \033[36m{imc:.1f}\033[m. Com base nele vocÊ apresenta \033[31mOBESIDADE\033[m.")
else:
    print(f"Seu imc é \033[36m{imc:.1f}\033[m. Com base nele você apresenta \033[31mOBESIDADE MORBIDA\033[m.")


