# significados = {
#     'menear': 'Balançar a cabeça',
#     'Admoestar': 'aconselhar',
#     'Alarido': 'confusão',
#     'Alcunha': 'apelido',
#     'Ardiloso': 'manhoso'
# }
# palavra = ""
# while palavra != "ok":
#     palavra = input("Digite uma palavra ou ok para sair: ")
#     for k, v in significados.items():
#         if palavra not in significados:
#             print("Palavra não encontrada")
#             break
#         elif palavra == k:
#             print(v)


# quadrado = [i * i for i in range(10)]
# print(quadrado)

original_price = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]


def get_price(price):
    return price if price > 0 else 0


prices = [get_price(i)for i in original_price]
print(prices)