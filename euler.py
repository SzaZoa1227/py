import math
def eulerGeneralas(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1

    e = eulerGeneralas(n-1, memo) + 1 / math.factorial(n)
    memo[n] = e

    return e



eualer = eulerGeneralas(100)
print(eualer)
