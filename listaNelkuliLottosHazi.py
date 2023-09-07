# Initialize variables for the five numbers
szam1 = int
szam2 = int
szam3 = int
szam4 = int
szam5 = int

def megfelelASzam(bekeres):
    while True:
        try:
            szam = int(input(bekeres))
            if 0 < szam < 100:
                return szam
            else:
                print("0 és 100 között adj meg számot!")
        except ValueError:
            print("Nem megfelelő a válasz amit adtál, kérlek számot adj!")

szam1 = megfelelASzam("Add meg az első számot:      ")
szam2 = megfelelASzam("Add meg a második számot:    ")
szam3 = megfelelASzam("Add meg a harmadik számot:   ")
szam4 = megfelelASzam("Add meg a negyedi számot:    ")
szam5 = megfelelASzam("Add meg az ötödik számot:    ")

print("Szám 1:", szam1)
print("Szám 2:", szam2)
print("Szám 3:", szam3)
print("Szám 4:", szam4)
print("Szám 5:", szam5)
