def fibonacci():
    n = int(input("digite um termo: "))
    ultimo = 1
    penultimo = 1

    if n == 1 or n == 2:
        print("1")
    else:
        count = 3
        while count <= n:
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
            print(f'{termo}')


def fibonacci2():
    n = int(input("Que termo deseja encontrar: "))
    ultimo = 1
    penultimo = 1

    if (n == 1) or (n == 2):
        print("1")
    else:
        for count in range(2, n):
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
            print(termo )


print(fibonacci2())
print(fibonacci())