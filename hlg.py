import random as r

generaltSzam = r.randint(1, 10)
probalkozasokSzama = 0
kapottTippet = False

while True:
    tipp = int(input("A tipped 1 és 1000 között: "))

    probalkozasokSzama += 1

    if tipp == generaltSzam:
        print(
            f"Gratulálok! Eltaláltad a generált számot {probalkozasokSzama} próbálkozásból!")
        break
    elif tipp < generaltSzam:
        print("A generált szám nagyobb mint a tipped. Próbáld újra!")
    else:
        print("A generált szám kisebb mint a tipped. Próbáld újra!")

    if probalkozasokSzama % 10 == 0 and not kapottTippet:
        kapottTippet = True
        print("Kérsz segítséget? (i/n)")
        valasz = input()
        if valasz.lower() == "i":
            print(
                f"A generált szám {generaltSzam - r.randint(1,25)} és {generaltSzam + r.randint(1,25)} között van.")
