#!/usr/bin/env python3
# coding=utf-8

import random


def adjacent_number():

    lista_adjacente = []
    lista_numeros = []
    cont = 0

    for n in range(3, 100):
        numeros = random.randint(300, 100999)
        lista_numeros.append(str(numeros))

    while cont < len(lista_numeros):
        for i in range(len(lista_numeros)):
            adjacente = (lista_numeros[i])
            contador = len(adjacente)
            inicio = 0
            final = 1
            while final < contador:
                if adjacente[inicio] == adjacente[final]:
                    if lista_numeros[i] not in lista_adjacente:
                        lista_adjacente.append(lista_numeros[i])

                inicio += 1
                final += 1
        cont += 1

    print'Lista dos adjacentes {}'.format(lista_adjacente)

    return -1


func = adjacent_number()
