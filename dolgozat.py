#a csoport
from random import randint
lista = [randint(0,100) for _ in range(20)]
print(lista)
parosokSzama = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        parosokSzama += 1
print(f"A listában {parosokSzama} páros szám van.")
if 0 in lista:
    print("A listában van nulla.")
else: print("A listában nicnsen nulla.")