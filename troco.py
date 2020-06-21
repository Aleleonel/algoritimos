vinte = resto = dez = dois = 0

valor = int(input('Quanto deseja trocar? \n'))

if valor:
    cinquenta = valor // 50
    resto = valor % 50
    if resto == 1:
        centavos = (resto / 5)
        print(f'Notas de Cinquenta = {cinquenta},\n'
              f'Notas de Vinte = {vinte}, \n'
              f'Notas de 10 = {dez}, \n'
              f'Notas de dois = {dois}\n'
              f'moedas de Cinquenta = {centavos}')
    else:
        vinte = resto // 20
        resto = resto % 20
        dez = resto // 10
        dois = resto % 10
        dois = dois // 2
        resto = dois % 2
        centavos = (resto / 5)
        print(f'Notas de Cinquenta = {cinquenta},\n'
              f'Notas de Vinte = {vinte},\n'
              f'Notas de 10 = {dez},\n'
              f'Notas de dois = {dois}\n'
              f'Cinquenta Centavos = {centavos}\n')