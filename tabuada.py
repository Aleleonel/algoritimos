
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