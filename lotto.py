szamok = []
sz = int
i = 1
while len(szamok) != 5:
    
    jelenlegiSzam = int(input(f"Írd be a(z) {i}. lottószámot:  "))
    if jelenlegiSzam > 0 and jelenlegiSzam <=99:
        szamok.append(jelenlegiSzam)
        i = i+1
    else:
        print("A beírt szám helytelen")
print(f"A bediktált számaid: {szamok}")
for i in range(1, 6):
    print(f"{i}.    {szamok[i-1]}")