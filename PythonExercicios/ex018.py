import math

escolha = input('Antes de inserir o valor do ângulo escolha a sua unidade. '
                'Para radianos digite r, para graus digite g: ')
# Caso ângulo em graus
if escolha == 'g':
    graus = float(input('Insira o ângulo em graus: '))
    radianos = math.radians(graus)
    # Caso tangente infinita
    if round(math.cos(radianos), 2) == 0 and math.sin(radianos) > 0:
        print(
            f'O ângulo digitado foi {graus} graus.'
            f'\nO seno desse ângulo é {math.sin(radianos):.2f}.'
            f'\nO cosseno desse ângulo é {math.cos(radianos):.2f}.'
            f'\nA tangente desse ângulo é infinito')
    else:
        # Caso tangente infinita negativa
        if round(math.cos(radianos), 2) == 0 and math.sin(radianos) < 0:
            print(
                f'O ângulo digitado foi {graus} graus.'
                f'\nO seno desse ângulo é {math.sin(radianos):.2f}.'
                f'\nO cosseno desse ângulo é {math.cos(radianos):.2f}.'
                f'\nA tangente desse ângulo é -infinito')
        else:
            print(
                f'O ângulo digitado foi {graus} graus.'
                f'\nO seno desse ângulo é {math.sin(radianos):.2f}.'
                f'\nO cosseno desse ângulo é {math.cos(radianos):.2f}.'
                f'\nA tangente desse ângulo é {math.tan(radianos):.2f}')
else:
    # caso Ângulo em radianos
    radianos = float(input(f'Insira o ângulo em radianos: '))
    # Caso tangente infinita
    if round(math.cos(radianos), 2) == 0 and math.sin(radianos) > 0:
        print(
            f'O ângulo digitado foi {radianos} radianos.'
            f'\nO seno desse ângulo é {math.sin(radianos):.2f}.'
            f'\nO cosseno desse ângulo é {math.cos(radianos):.2f}.'
            f'\nA tangente desse ângulo é infinito')
    else:
        # Caso tangente infinita negativa
        if round(math.cos(radianos), 2) == 0 and math.sin(radianos) < 0:
            print(
                f'O ângulo digitado foi {radianos} radianos.'
                f'\nO seno desse ângulo é {math.sin(radianos):.2f}.'
                f'\nO cosseno desse ângulo é {math.cos(radianos):.2f}.'
                f'\nA tangente desse ângulo é -infinito')
        else:
            print(
                f'O ângulo digitado foi {radianos} radianos.'
                f'\nO seno desse ângulo é {math.sin(radianos):.2f}.'
                f'\nO cosseno desse ângulo é {math.cos(radianos):.2f}.'
                f'\nA tangente desse ângulo é {math.tan(radianos):.2f}')
