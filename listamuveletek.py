from random import randint
veletlenszamok = [randint(-5,5) for _ in range(20)]
print(veletlenszamok)

nemneg = 0
neg = 0
for i in veletlenszamok:
    if i >= 0:
        nemneg += 1
    else:
        neg += 1
print(f"A listában {nemneg} nemnegatív szám és {neg} negatív szám van benne")

nullakszama = 0
for i in veletlenszamok:
    if i == 0:
        nullakszama += 1
print(f"{nullakszama} nulla van a listában")

nemnegativ = []
negativ = []
for i in veletlenszamok:
    if i >= 0:
         nemnegativ.append(i)
    else:
        negativ.append(i)
print(f"A nemnegativ számok listája: {nemnegativ}, A negatív számok listája: {negativ}")

print("Van benne ötös" if 5 in veletlenszamok else "Nincs ötös")

i = 0
while i < 20:
    print(veletlenszamok[i],end=", ")
    i += 1  