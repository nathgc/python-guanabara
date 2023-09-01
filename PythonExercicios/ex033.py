n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 >= n2:
    if n1 >= n3:
        if n2 >= n3:
            print(f" {n1}>={n2}>={n3}\n"
                  f"O maior número é {n1}, o menor número é {n3}.")
        else:
            print(f"{n1}>={n3}>{n2}\n"
                  f"O maior número é {n1}, o menor número é {n2}.")
    else:
        #n1>=n2; n3>n1
        print(f"{n3}>={n1}>={n2}.\n"
              f"O maior número é {n3}, o menor número é {n2}.")
else:
    #n2>n1
    if n2 >= n3:
        if n1 >= n3:
            print(f"{n2}>{n1}>={n3}.\n"
                  f"O maior número {n2}, o menor é {n3}.")
        else:
            print(f"{n2}>={n3}>{n1}.\n"
                  f"O maior numero é {n2} o menor número é {n1}.")
    else:
        #n3>n2
        print(f"{n3}>{n2}>{n1}.\n"
              f"O maior número é {n3}, o menor número é {n1}.")