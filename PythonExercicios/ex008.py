m = float(input('Digite a quantidade em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m/10
hm = m/100
km = m/1000

print(f'Essa quantidade convertida para Milímetros é igual a {mm:.0f} mm. \nEssa quantidade convertida para Centímetros é igual a {cm:.0f} cm.'
      f' \nEssa quantidade convertida para Decímetros é igual a {dm:.0f} dm. \nEssa quantidade convertida para Decâmetros é igual a {dam} dam.'
      f' \nEssa quantidade convertida para Hectômetros é igual a {hm} hm. \nEssa quantidade convertida para Quilômetros é igual a {km} km')