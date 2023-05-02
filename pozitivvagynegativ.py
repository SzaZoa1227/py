import random as rng
import os
os.system("cls")
nullakSzama = 0
for i in range(10):
    
    veletlenSzam = rng.randint(-100,100)
    if veletlenSzam >= 0:
        print(f"{veletlenSzam}: Pozitív")
    elif veletlenSzam == 0:
        nullakSzama +=1
    else:
        print(f"{veletlenSzam}: Negatív")
if nullakSzama != 0:
        print("Volt {nullakSzama} nulla a generált számok között")
else:
    print("Nem volt nulla a generált számok között")

