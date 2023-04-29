import random as r
import os
nyert = 0
os.system("cls")
while nyert == 0:
    generaltSzam = r.randint(0,9999999999999)
    tipp = input(int())
    if tipp == generaltSzam:
        print("Gratulálok, nyertél!")
        nyert = 1
    elif generaltSzam > tipp:
        print("A generált szám nagyobb, mint amire Te tippeltél. Próbáld újra!")
    else:
        print("A generált szám kisebb, mint amire Te tippeltél. Próbáld újra!")
