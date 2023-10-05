
def megfelelASzam(bekeres):
    while True:
        try:
            szam = int(input(bekeres))
            if 0 < szam < 100:
                return szam
            else:
                print("0 és 100 között adj meg számot!")
        except ValueError:
            print("Nem megfelelő a válasz amit adtál, kérlek egész számot adj!")

for i in range(1,6):
    megfelelASzam(f"Kérem a {i}. lottószámot:   ")