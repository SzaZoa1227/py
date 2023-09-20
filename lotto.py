szamok = []
sz = int
i = 1
while len(szamok) != 5:
    
    jelenlegiSzam = int(input(f"Írd be a(z) {i}. lottószámot:  "))
    if jelenlegiSzam > 0 and jelenlegiSzam <=99:
        szamok.append(jelenlegiSzam)
        i = i+1
    elif ValueError:
        print("Kérlek egész számot adj meg!")
    else:
        print("Nullánál nagyobb és száznál kissebb számot adj meg!")
print(f"A bediktált számaid: {szamok}")
for i in range(1, 6):
    print(f"{i}. lottószám:   {szamok[i-1]}")