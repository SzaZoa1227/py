import random as r

generaltSzam = r.randint(1, 10)
probalkozasokSzama = 0
tippekSzama = 0
while True:
    tipp = int(input(f"Ide írd a tipped 1 és 10 között: "))
    tippekSzama += 1
    if tipp == generaltSzam:
        print(f"Gratulálok kitaláltad a számot {tippekSzama} próbálkozásokból")
        break
    elif tipp > generaltSzam:
        print("A tipped nagyobb mint a generált szám, próbáld újra!")
    else:
        print("A tipped kissebb mint a generált szám, próbáld újra")
    if tippekSzama == 4:
        print(f"Próbálkozásaid száma meghaladta a {tippekSzama} értéket, veszítettél.")
        break