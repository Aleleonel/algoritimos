def fatorial():
    fat = 1
    numero = 1
    while numero > 0:
        numero = int(input('Digite um numero: '))
        if numero < 0:
            break
        while numero > 0:
            fat = fat * numero
            numero -= 1
        print(fat)
        fat = 1
        numero = 1

    return fat


fatorial()