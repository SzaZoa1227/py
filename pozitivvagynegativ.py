import random as rng
import os
os.system("cls")
NULLAKSZAMA = 0
for i in range(10):
    veletlenSzam = rng.randint(-100, 100)
    if veletlenSzam >= 0:
        print(f"{veletlenSzam}: Pozitív")
    elif veletlenSzam == 0:
        NULLAKSZAMA += 1
    else:
        print(f"{veletlenSzam}: Negatív")
if NULLAKSZAMA != 0:
    print("Volt {NULLAKSZAMA} nulla a generált számok között")
else:
    print("Nem volt nulla a generált számok között")
