import math
"""
Essa fórmula nada mais é do que um método para encontrar as raízes reais de uma equação do segundo grau
fazendo uso apenas de seus coeficientes. Vale lembrar que coeficiente é o número que multiplica uma incógnita
em uma equação. exemplo: ax2 + bx + c = 0
Δ < 0, então a equação não possui resultados reais;
Δ = 0, então a equação possui apenas um resultado real ou
 possui dois resultados iguais (essas duas afirmações são equivalentes);
Δ > 0, então a equação possui dois resultados distintos reais.
    Portanto, para calcular as raízes de uma equação do segundo grau,
    primeiramente calcule o valor numérico de Δ.
"""


def bhaskara(a, b, c):

    # a = int(input('Digite um numero pra a:'))
    # b = int(input('Digite um numero pra b:'))
    # c = int(input('Digite um numero pra c:'))

    x1 = x2 = 0
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        print(f'Delta é igual a ===> {delta}')
        print('A equação não possui resultados reais;')

    elif delta == 0:
        print('A equação possui apenas um resultado\n' \
             ' real ou possui dois resultados iguais')
        linha1 = -(b + (math.sqrt(delta)))
        x1 = (linha1) / (2 * a)

    else:
        if delta > 0:
            print(f'Delta é igual a ===> {delta}')
            print('A equação possui dois resultados distintos reais.')
            linha1 = -(b + (math.sqrt(delta)))
            x1 = (linha1) / (2 * a)

            linha2 = -(b - (math.sqrt(delta)))
            x2 = (linha2) / (2 * a)

    print(f'X1 = {x1}')
    print(f'X2 = {x2}')

    return -1


bk = bhaskara(10, 10, 10)

