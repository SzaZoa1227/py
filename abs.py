szam = int(input("Kérem az első számot  "))
szamok = []
while szam != 0:
    if szam < 0:
        szam = szam*-1
        szamok.append(szam)
    else:
        szamok.append(szam)
    szam = int(input("Kérem a következő számot  "))

vegso = sum(szamok)/len(szamok)
print(vegso)