#!/usr/bin/env python3
# coding=utf-8


def binomial(n, p):

    contador = numerador = n
    contador_denominador = denominador = p

    # Calcula o numerador de uma expressão binomial através da fatoração
    while contador > 1:
        contador -= 1
        numerador = numerador * contador
    # print numerador

    # Calcula o denominador de uma expressão binomial através da fatoração
    while contador_denominador > 1:
        contador_denominador -= 1
        denominador = denominador * contador_denominador
    # print denominador

    # Calcula a diferença entre o numerador e o denominador de uma expressão binomial
    # e fatoração deste resultado
    n_p = n-p
    contador_np = n_p
    while contador_np > 1:
        contador_np -= 1
        n_p = n_p * contador_np
    # print n_p

    # Calcula a expressão binomial
    binominal = (numerador)/(denominador * n_p)

    print binominal


bino = binomial(8, 3)