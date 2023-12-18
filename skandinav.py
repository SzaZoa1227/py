import random as r
szamok = []
while len(szamok) < 7:
    bele = r.randint(1,35)
    if bele in szamok:
        print("Van ismetlodes")
        continue
    else:
        szamok.append(bele)
print(sorted(szamok))