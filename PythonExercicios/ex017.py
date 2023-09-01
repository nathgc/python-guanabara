import math
cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cat_adjacente,cat_oposto)
#hipotenusa = math.sqrt((pow(cat_adjacente,2) + pow(cat_oposto,2)))
print(f'A hipotenusa desse triângulo retângulo mede {hipotenusa:.2f}')

