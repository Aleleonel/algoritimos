def fatorial(n):
    fat = 1
    for f in range(n, 0, -1):
        fat *= f
    return fat

print(fatorial(5))


# uma função que chama ela mesma
def fatorialrecursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorialrecursivo(n -1)


print(fatorialrecursivo(5))