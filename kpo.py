import random

lehetosegek = ["kő", "papír", "olló"]
pontok = [0, 0]

while True:
    jatekos = input("Kő, papír vagy olló? ").lower()
    gep = random.choice(lehetosegek)

    if jatekos not in lehetosegek:  # jatekos valasztasa nincsen a lehetosegek kozott
        print("Érvénytelen választás!")
        continue

    print("Te választásod:", jatekos)
    print("A gép választása", gep)

    if jatekos == gep:
        print("Döntetlen!")
    elif (
        jatekos == "kő"
        and gep == "olló"
        or jatekos == "papír"  # minden nyertes lehetoseg
        and gep == "kő"
        or jatekos == "olló"
        and gep == "papír"
    ):
        print("Gratulálok! Nyertél.")
        pontok[0] += 1
    else:                       # ha nem a jatekos nyer
        print("A gép nyert.")
        pontok[1] += 1

    print("pontok: Te {} - {} Gép".format(pontok[0], pontok[1]))
    ujjatek = input("Új játék? (I/N) ").lower()
    if ujjatek != "i":
        break
"""kiírja a két változó helyére a pontok lista első és második értékét sorrendben
                            (.format stringgé alakítja)"""
