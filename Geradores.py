def evens(limit=10):
    n = 0
    while True:
        n += 2
        if n > limit:
            return
        yield n


def odds(limit=10):
    n = 1
    while True:
        if n > limit:
            return
        yield n
        n += 2


def chain(g1, g2):
    yield from g1
    yield from g2

a = evens()
print(next(a))
print(next(a))