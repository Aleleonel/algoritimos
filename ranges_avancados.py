nomes = ['alexandre', 'rosemary', 'luna', 'kiko']
idades = [46, 53, 2, 8]

for nome, idades in zip(nomes, idades):
    print(f'{nome} tem {idades} anos')

with open('arquivo.txt') as arquivo:
    for n, linha in enumerate(arquivo, start=1):
        print(f'{n} {linha}')