import random
import time
import os
lehetosegek = ["kő", "papír", "olló"]
pontok = [0, 0]

while True:
    os.system('cls')
    jatekos = input("Kő, papír vagy olló? ").lower()
    gep = random.choice(lehetosegek)

    if jatekos not in lehetosegek:  # jatekos valasztasa nincsen a lehetosegek kozott
        print("Érvénytelen választás!")
        time.sleep(2)
        continue

    print("Te választásod:", jatekos)
    time.sleep(1)
    print("A gép választása:", gep)

    if jatekos == gep:
        time.sleep(2)
        print("Döntetlen!")
        time.sleep(2)
    elif (
        jatekos == "kő"
        and gep == "olló"
        or jatekos == "papír"  # minden nyertes lehetoseg
        and gep == "kő"
        or jatekos == "olló"
        and gep == "papír"
    ):
        time.sleep(2)
        print("Gratulálok! Nyertél.")
        pontok[0] += 1
    else:
        time.sleep(2)                       # ha nem a jatekos nyer
        print("A gép nyert.")
        pontok[1] += 1

    print(f"pontok: Te {pontok[0]} - {pontok[1]} Gép")
    ujjatek = ""
    