import os
os.system("clear")
from math import factorial
def eulerGeneralas(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1

    e = eulerGeneralas(n-1, memo) + 1 / factorial(n)
    szamolo =+ 1
    memo[n] = e

    return e


mennyiszer = int(input("mennyiszer futtasuk le a folyamatot?    "))
euler = eulerGeneralas(mennyiszer)
print(f"{mennyiszer}:   {euler}")
