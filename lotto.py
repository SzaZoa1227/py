from random import randint
szamok = []
nyeroSzamok = []
while len(nyeroSzamok) < 7:
    bele = randint(1,35)
    if bele not in nyeroSzamok:
        nyeroSzamok.append(bele)
sz = int
i = 1
while len(szamok) < 7:   
    jelenlegiSzam = int(input(f"Írd be a(z) {i}. lottószámot:  "))
    if jelenlegiSzam > 0 and jelenlegiSzam <=35 and jelenlegiSzam not in szamok:
        szamok.append(jelenlegiSzam)
        i += 1
    elif type(jelenlegiSzam) != int:
        print("Kérlek egész számot adj meg!")
    elif jelenlegiSzam > 35 or jelenlegiSzam < 1 or jelenlegiSzam in szamok:
        print("Nullánál nagyobb és 35nél kissebb számot adj meg!\nNem lehet ismétlődés")
print(f"A bediktált számaid: {sorted(szamok)}")
print(f"A nyerőszámok {sorted(nyeroSzamok)}")
talalatok = 0
for i in range(7):
    if szamok[i] in nyeroSzamok:
        talalatok += 1
print(f"Ennyi találatod van: {talalatok}")