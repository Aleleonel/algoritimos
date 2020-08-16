from typing import List


def tabuada():
    linha = 1
    coluna = 1
    while linha <= 10:
        while coluna <= 10:
            res = linha * coluna
            print(f'{coluna} X {linha} = {res}', end="\t\t")
            coluna = coluna + 1
        linha += 1
        print()
        coluna = 1


tabuada()


def tabuada2():
    linha = 0
    cont: List[int] = [v*linha for v in range(10)]

    print(cont)


tabuada2()