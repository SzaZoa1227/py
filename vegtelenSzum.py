n = 1
szamok = []
while sum(szamok) != 1:
    szam = 1/2**n
    szamok.append(szam)
    n += 1
    print(sum(szamok))
print(f"A törtek összege {n} tört után közelítette meg a egyet.")
