from collections import Counter
with open('arquivo.txt', 'r') as f:
    texto = f.read()


def func1(texto):
    '''Retorna dict ou seja dict[char] = quantidade de caracteres no texto'''

    chars = []
    quantity = []
    for c in texto:
        if not c in chars:
            chars.append(c)
            quantity.append(1)
        else:
            index = chars.index(c)
            quantity[index] += 1
    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]

    return d


def func2(texto):
    chars = set()
    for c in texto:
        chars.add(c)
    chars = list(chars)
    quantity = [texto.count(c) for c in chars]
    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d


def func3(texto):
    chars = list({c for c in texto})
    quantity = [texto.count(c) for c in chars]
    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d


def func4(texto):
    chars = list({c for c in texto})
    quantity = [(c, texto.count(c)) for c in chars]
    return dict(quantity)


def func5(texto):
    return dict([(c, texto.count(c)) for c in set(texto)])


def func6(texto):
    return {c: texto.count(c) for c in set(texto)}


def func7(texto):
    return Counter(texto)


print(func7(texto))
