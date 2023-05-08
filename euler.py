import math as m
def eulerGeneralas(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1

    e = eulerGeneralas(n-1, memo) + 1 / m.factorial(n)
    memo[n] = e

    return e



euler = eulerGeneralas(100)
print(euler)
