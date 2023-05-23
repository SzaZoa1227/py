from random import randint
from os import system
from time import sleep
system("cls")
generaltSzam = randint(1, 100)
probalkozasokSzama = 0
tippekSzama = 0
while True:
    tipp = int(input("Ide írd a tipped 1 és 100 között: "))
    tippekSzama += 1
    if tipp == generaltSzam:
        print(f"Gratulálok kitaláltad a számot {tippekSzama} próbálkozásokból")
        break
    elif tipp > generaltSzam:
        print("A tipped nagyobb mint a generált szám, próbáld újra!")
    else:
        print("A tipped kissebb mint a generált szám, próbáld újra")
        
sleep(5)
system("cls")