import os
import time
while True:
    os.system("cls")
    oldal = float(input("Négyszög oldalának a hossza cmben: "))
    oldal2 = float(input("Négyszög másik oldalának a hossza cmben: "))
    kerulet = round(2 * oldal+oldal2, 2)
    terulet = round(float(oldal**2), 2)
    if round(kerulet, 0) == kerulet:
        kerulet = round(kerulet, 0)
    if round(kerulet, 0) == terulet:
        terulet = round(terulet, 0)
    print("A síkidom kerülete kerekítve két tizedesjegyre:", kerulet, "cm")
    time.sleep(1)
    print("A síkidom területe kerekítve két tizedesjegyre:", terulet, "cm²")
    time.sleep(5)
    os.system("cls")
    a = float(input("Kérem a hasáb egyik élének a hoszát cmben:"))
    # time.sleep(1)
    b = float(input("Kérem a hasáb másik élének a hoszát cmben:"))
    # time.sleep(1)
    c = float(input("Kérem a hasáb harmadik élének a hoszát cmben:"))
    terfogat = round(a*b*c, 2)
    felulet = round(2*(a*b + a*c + b*c), 2)
    print("A hasáb térfogata kerekítve két tizedesjegyre:", terfogat, "cm³")
    time.sleep(1)
    print("A hasáb felszíne kerekítve két tizedesjegyre:", felulet,  "cm²")
    time.sleep(5)
    os.system("cls")
    ujra = input("Újraindítod? I/N  ").lower()
    if ujra != "i":
        break
