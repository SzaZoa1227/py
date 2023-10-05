import random as r
import os
import time as t
os.system("cls")
kartyakErteke = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "D": 10,
    "K": 10,
    "A": 11
}
pakli = list(kartyakErteke.keys()) * 4


def pakliKiirasa(kinek):
    if kinek == gepKartyai:
        print(f"A gép kártyái: {gepKartyai}")
    else:
        print(f"A te kártyáid: {jatekosKartyai}, értékük: {kezbenTartottKartyakErteke(jatekosKartyai)}")


def kezbenTartottKartyakErteke(kez):
    ertek = 0
    aszokSzama = 0
    for kartya in kez:
        ertek += kartyakErteke[kartya]
        if kartya == "A":
            aszokSzama += 1
    while ertek > 21 and aszokSzama > 0:    #ha az ásszal a kártyák értéke túlmegy a 21en, levonja az ászt és 10 pontot
        ertek -= 10
        aszokSzama -= 1 
    return ertek


r.shuffle(pakli)

jatekosKartyai = [pakli.pop(), pakli.pop()]
gepKartyai = [pakli.pop()]
game = True
while game == True:
    pakliKiirasa(jatekosKartyai)
    print(f"Gép kártyáinak száma: {len(gepKartyai)}")
    t.sleep(5)
    if kezbenTartottKartyakErteke(jatekosKartyai) == 21:
        print("Blackjack! Gratulálok, nyertél!")
        pakliKiirasa(jatekosKartyai)
        t.sleep(5)
        os.system("cls")
        game = False
    elif kezbenTartottKartyakErteke(jatekosKartyai) > 21:
        print("21-en túlment a kártyáid értéke. Veszítettél.")
        pakliKiirasa(jatekosKartyai)
        pakliKiirasa(gepKartyai)
        t.sleep(5)
        os.system("cls")
        game = False
    else:
        valasz = input("Szeretnél új kártyát vagy nem? I/N").lower()
        if valasz == "i":
            jatekosKartyai.append(pakli.pop())
        elif valasz == "n":
            game = False

if kezbenTartottKartyakErteke(jatekosKartyai) <= 21:
    while kezbenTartottKartyakErteke(gepKartyai) < 17:
        gepKartyai.append(pakli.pop())
    pakliKiirasa(jatekosKartyai)
    print(f"A gép kártyáinak a száma: {len(gepKartyai)}")
    t.sleep(5)
    os.system("cls")
    if kezbenTartottKartyakErteke(gepKartyai) > 21:
        print("A gép kártyáinak értéke túlment 21-en. Gratulálok, nyertél!")
        print(f"{pakliKiirasa(gepKartyai)} Értékük: {kezbenTartottKartyakErteke(gepKartyai)}")
        t.sleep(5)
        os.system("cls")
    elif kezbenTartottKartyakErteke(gepKartyai) >= kezbenTartottKartyakErteke(jatekosKartyai):
        print("A gépnek a kárytái meghaladják a te kártyáid értékét. Veszítettél.")
        pakliKiirasa(gepKartyai)
        pakliKiirasa(jatekosKartyai)
        t.sleep(5)
        os.system("cls")
    else:
        print("A kártyáid értéke meghaladja a gép kártyáinak az értékét! Gratulálok, nyertél!")    
        pakliKiirasa(gepKartyai)
        pakliKiirasa(jatekosKartyai)
        t.sleep(5)
        os.system("cls")
