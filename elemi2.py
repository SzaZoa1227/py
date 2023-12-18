from random import randint

lista = [randint(0,1000) for _ in range(50)]

def minimum(lista):
    a = lista[0]
    for i in lista:
        if a < i:
            continue
        else: a = i
    return a
print(lista)
print(minimum(lista))
print(min(lista))

def maximum(lista):
    a = lista[0]
    for i in lista:
        if a < i:
            a = i
        else: continue
    return a

# print(maximum(lista))
# print(max(lista))




















lista2 = [randint(0,10) for _ in range(10)]
lista3 = [randint(0,10) for _ in range(10)]
print(lista2,lista3)
def metszet(lista1,lista2):
    metszet = []
    for i in lista1:
        if i in metszet:
            continue
        elif i in lista2:
            metszet.append(i)
    return metszet

print(metszet(lista2,lista3))