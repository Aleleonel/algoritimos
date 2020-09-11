from typing import List


def switch_demo(argument):

    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))


def vidro():
    return "Troca Rapida em ate 3 dias"


def colisao():
    return 'Favor entrar em conta com eventos'


def boleto():
    return 'Favor ligar para o numero (11)97151-2237'


def numbers_to_months(argument):
    switcher = {
        1: vidro,
        2: colisao,
        3: boleto

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    print(func())

digite = []
troca = ['vidro', 'Vidros', 'para-brisa', 'Para-brisas', ]
sinistros = ['colisão', 'bati', 'bateu', 'colidiu', 'acidente' ]
x = 0
digite.append(input('Olá em que posso ajuda-lo: '))
d = [x for x in digite]
for i in d:
    tr = [tr for tr in troca]
    palavra_tr = tr
    for ch_tr in palavra_tr:
        if i in troca:
            x = 1
        else:
            sin = [sin for sin in sinistros]
            palavra_sin = sin
            for ch_sin in palavra_sin:
                if i in sinistros:
                    x = 2
        numbers_to_months(x)

