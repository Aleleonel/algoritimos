produtos = {
    '01': 'nootebok',
    '02': 'ipad'
}
valor = {
    '01': 1500,
    '02': 1000
}

compra_realizada = {}


def compra_itens():
    codigo_do_item = input('digite o código do item: ')
    quantidade = int(input('Digite a quantidade: '))
    desconto_fixo = int(input('Digite o valor do desconto fixo'))
    for k, v in produtos.items():
        if k == codigo_do_item:
            for kv, vv in valor.items():
                    if kv == codigo_do_item:
                        cont = 0
                        while cont < quantidade:
                            if quantidade >= 3:
                                valor_total = (vv * quantidade) - desconto_fixo
                                prazo_de_pagamento(valor_total, quantidade, v)
                                return quantidade, v
                                cont += 1
                            else:
                                valor_total = (vv * quantidade)
                                prazo_de_pagamento(valor_total, quantidade, v)
                                cont += 1
                                return quantidade, v, valor_total
                        imprime()

    return valor_total, prazo


def prazo_de_pagamento(valor_total, quantidade, v):

    if quantidade < 3:
        prazo = valor_total
        quantidade = quantidade
        v = v
        imprime(prazo, quantidade, v)
        return prazo

    elif quantidade >= 3:
        forma = input('Digite a forma de pagamento: [01] para A Vista / [02] para A prazo ')
        if forma == '01' and quantidade >= 3:
            prazo = valor_total - (valor_total * 10)/100
            quantidade = quantidade
            v = v
            imprime(prazo, quantidade, v)

        elif forma == '02' and quantidade >= 3:
            prazo = valor_total + (valor_total * 8)/100
            quantidade = quantidade
            v = v
            imprime(prazo, quantidade, v)

    return prazo


def imprime(prazo, quantidade, v, ):

    compra_realizada['qtd'] = quantidade
    compra_realizada['produto'] = v
    compra_realizada['preco'] = prazo
    print(compra_realizada)


compra_itens()



