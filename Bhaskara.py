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


def delta(a, b, c):
    return (b ** 2) - (4 * a * c)


def main():
    a = int(input('Digite um numero pra a:'))
    b = int(input('Digite um numero pra b:'))
    c = int(input('Digite um numero pra c:'))
    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print('A equação não possui resultados reais;')

    elif d == 0:
        print('A equação possui apenas um resultado\n'
              ' real ou possui dois resultados iguais')
        x1 = -(b + (math.sqrt(delta(a, b, c)))) / (2 * a)
        print(f'A unica raiz é = {x1}')

    else:
        if d > 0:
            print('A equação possui dois resultados distintos reais.')
            x1 = -(b + (math.sqrt(delta(a, b, c)))) / (2 * a)
            x2 = -(b - (math.sqrt(delta(a, b, c)))) / (2 * a)
            print(f'A primeria raiz é = {x1}')
            print(f'A segunda raiz é  = {x2}')

    return -1

principal = main()