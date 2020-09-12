# 2)Escreva uma função que recebe uma entrada de texto
# (ex: “Um dois tres, vinte e quatro, vinte e cinco, trinta e três.”)
# e imprime na tela as frequências de cada palavra individual contida no texto.
# Desconsidere os acentos das palavras. Ordene os resultados pelas palavras mais frequentes primeiro.

from collections import Counter


def conta_palavras():

    frase = (input("Digite uma frase: "))
    total = ''
    total1 = 0

    # split() possibilita a separação de plavas em uma frase(string), podemos determinar
    # o ponto de separação no exemplo a baixo separei por espaço (' ') isso me deu cada palavra
    # de forma individual.
    resultado = frase.split(' ')

    # Counter/ most_common() - Mostra o resultado das palavras mais frequentes
    # onde (n) determina quantos resultados vocẽ quer mostrar.
    total = Counter(resultado).most_common(4)

    for freq in resultado:
        total1 += 1

    total2 = Counter(resultado)
    print(f'Total de palavras mais frequentes: {total}')
    print(f'Total de cada palavras : {total2}')
    print(f'Total de palavras : {total1}')

conta_palavras()