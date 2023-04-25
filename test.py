import os
import time
while True:
    os.system("cls")
    oldal  = float(input("Négyzet oldalának a hossza: "))
    kerulet = 4 * float(oldal)
    terulet = oldal*oldal
    print("A négyzet kerülete:", kerulet)
    time.sleep(1)
    print("A négyzet területe:", terulet)
    time.sleep(5)
    os.system("cls")
    a = float(input("Kérem a hasáb egyik élének a hoszát:"))
    time.sleep(1)
    b = float(input("Kérem a hasáb másik élének a hoszát:"))
    time.sleep(1)
    c = float(input("Kérem a hasáb harmadik élének a hoszát:"))
    terfogat = a*b*c
    felulet = 2*(a*b + a*c + b*c)
    print("A hasáb térfogata:", terfogat)
    time.sleep(1)
    print("A hasáb felszíne:", felulet)
    time.sleep(5)
    ujra = input("Újraindítos?").lower()
    