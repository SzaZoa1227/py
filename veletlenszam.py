import random as r
import os
os.system("cls")
for i in range(7):
    veletlenSzam = r.randint(1,35)
    if veletlenSzam % 2 == 0:
        print(f"{veletlenSzam}: Páros")
    else:
        print(f"{veletlenSzam}: Páratlan")

